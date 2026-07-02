from __future__ import annotations

import re
from typing import Any

from shortdrama_pipeline.models import Episode, ScriptBundle, ScriptQualityIssue, ScriptQualityReport, Shot


class Harness:
    def before_script(self, ctx: dict[str, Any]) -> Any:
        return None

    def after_script(self, ctx: dict[str, Any], script: Any) -> Any:
        return None

    def before_script_review(self, ctx: dict[str, Any], script: Any) -> Any:
        return None

    def after_script_approved(self, ctx: dict[str, Any], script: Any) -> Any:
        return None

    def before_character_generation(self, ctx: dict[str, Any], script: Any) -> Any:
        return None

    def after_character_generation(self, ctx: dict[str, Any], characters: Any) -> Any:
        return None

    def before_character_review(self, ctx: dict[str, Any], characters: Any) -> Any:
        return None

    def after_character_approved(self, ctx: dict[str, Any], characters: Any) -> Any:
        return None

    def before_video_generation(self, ctx: dict[str, Any], shot: Any) -> Any:
        return None

    def after_video_generation(self, ctx: dict[str, Any], shot: Any, video: Any) -> Any:
        return None


class ScriptQualityHarness(Harness):
    _ACTION_MARKERS = ("，", "、", "并", "同时", "随后", "然后", "接着", "冲", "跑", "追", "拉", "推", "转身")
    _CAMERA_SPLIT_PATTERN = re.compile(r"\s*(?:/|->|→|>|｜|\|)\s*")

    def after_script(self, ctx: dict[str, Any], script: ScriptBundle) -> ScriptQualityReport:
        shot_issues: list[ScriptQualityIssue] = []
        episode_warnings: dict[str, list[str]] = {}

        for episode in script.episodes:
            shot_issues.extend(self._collect_shot_issues(episode))

            duration_warning = self._build_episode_duration_warning(episode)
            if duration_warning is not None:
                episode_warnings.setdefault(episode.episode_id, []).append(duration_warning)

        overall_score = self._calculate_score(shot_issues, episode_warnings)
        summary = self._build_summary(shot_issues, episode_warnings)
        recommendation = "仅输出质量预警，不阻塞流程；可优先处理 high_warning，再按 warning 微调分镜。"

        return ScriptQualityReport(
            job_id=str(ctx.get("job_id", "")),
            overall_score=overall_score,
            summary=summary,
            episode_warnings=episode_warnings,
            shot_issues=shot_issues,
            recommendation=recommendation,
        )

    def _collect_shot_issues(self, episode: Episode) -> list[ScriptQualityIssue]:
        issues: list[ScriptQualityIssue] = []
        for shot in episode.shots:
            if shot.duration_seconds < 4 or shot.duration_seconds > 10:
                issues.append(
                    ScriptQualityIssue(
                        level="warning",
                        episode_id=episode.episode_id,
                        shot_id=shot.shot_id,
                        title="shot_duration_out_of_range",
                        detail=f"镜头时长 {shot.duration_seconds}s，建议控制在 4-10s。",
                        suggestion="拆分过长镜头或合并过短镜头，保持单镜头信息密度稳定。",
                    )
                )

            if self._is_shot_overloaded(shot):
                issues.append(
                    ScriptQualityIssue(
                        level="warning",
                        episode_id=episode.episode_id,
                        shot_id=shot.shot_id,
                        title="shot_overload",
                        detail="镜头内动作、人物或机位切换偏多，单镜承载量可能过高。",
                        suggestion="减少同镜头中的任务数量，优先保留最关键的动作或机位表达。",
                    )
                )

            if len(shot.dialogue) > 1:
                issues.append(
                    ScriptQualityIssue(
                        level="warning",
                        episode_id=episode.episode_id,
                        shot_id=shot.shot_id,
                        title="dialogue_too_dense",
                        detail=f"当前镜头包含 {len(shot.dialogue)} 句对白，超过单镜头 1 句的轻量建议。",
                        suggestion="将对白拆到相邻镜头，或改为动作/表情推进信息。",
                    )
                )
        return issues

    def _is_shot_overloaded(self, shot: Shot) -> bool:
        action_score = sum(shot.visual_description.count(marker) for marker in self._ACTION_MARKERS)
        character_overload = len(shot.characters) > 3
        camera_overload = self._camera_segment_count(shot.camera) > 3
        return action_score >= 5 or character_overload or camera_overload

    def _camera_segment_count(self, camera: str) -> int:
        stripped = camera.strip()
        if not stripped:
            return 0

        slash_segments = [segment for segment in self._CAMERA_SPLIT_PATTERN.split(stripped) if segment]
        if len(slash_segments) > 1:
            return len(slash_segments)

        textual_segments = re.split(r"[、，,；;]", stripped)
        return len([segment for segment in textual_segments if segment.strip()])

    def _build_episode_duration_warning(self, episode: Episode) -> str | None:
        declared_duration = episode.duration_seconds
        if declared_duration <= 0:
            return None

        actual_duration = sum(shot.duration_seconds for shot in episode.shots)
        gap_ratio = abs(declared_duration - actual_duration) / declared_duration
        if gap_ratio <= 0.10:
            return None

        level = "warning" if gap_ratio <= 0.25 else "high_warning"
        return (
            f"{level}: 声明集时长 {declared_duration}s，与分镜合计 {actual_duration}s 相差 "
            f"{gap_ratio * 100:.1f}%。"
        )

    def _calculate_score(
        self, shot_issues: list[ScriptQualityIssue], episode_warnings: dict[str, list[str]]
    ) -> float:
        penalty = 0
        for issue in shot_issues:
            penalty += 5 if issue.level == "warning" else 8
        for warnings in episode_warnings.values():
            for warning in warnings:
                penalty += 10 if warning.startswith("high_warning") else 5
        return round(max(0.0, 100.0 - penalty), 1)

    def _build_summary(
        self, shot_issues: list[ScriptQualityIssue], episode_warnings: dict[str, list[str]]
    ) -> str:
        high_warning_count = sum(
            1
            for warnings in episode_warnings.values()
            for warning in warnings
            if warning.startswith("high_warning")
        )
        warning_count = len(shot_issues) + sum(len(warnings) for warnings in episode_warnings.values()) - high_warning_count
        return (
            f"检测到 {warning_count} 条 warning"
            f"{f'，{high_warning_count} 条 high_warning' if high_warning_count else ''}；"
            "当前结果仅用于提示，不阻塞后续流程。"
        )


class HarnessManager:
    def __init__(self, harnesses: list[Harness] | None = None):
        self.harnesses = harnesses or []

    def run(self, hook_name: str, *args: Any) -> list[dict[str, Any]]:
        reports: list[dict[str, Any]] = []
        for harness in self.harnesses:
            hook = getattr(harness, hook_name)
            result = hook(*args)
            if result is not None:
                reports.append({"harness": harness.__class__.__name__, "result": result})
        return reports
