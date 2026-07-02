from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
import uuid
from typing import Callable

from shortdrama_pipeline.composer import EpisodeComposer
from shortdrama_pipeline.config import Settings
from shortdrama_pipeline.harness import HarnessManager, ScriptQualityHarness
from shortdrama_pipeline.logging import ModelCallLogger, PipelineEventLogger
from shortdrama_pipeline.models import JobCreate, JobRecord, JobStatus, ScriptBundle
from shortdrama_pipeline.prompts import build_seedance_prompt
from shortdrama_pipeline.providers import ImageProvider, ScriptProvider, VideoProvider
from shortdrama_pipeline.storage import ArtifactStore, JobStore, ProjectStore

MIN_SEEDANCE_DURATION_SECONDS = 4
TARGET_SEEDANCE_DURATION_SECONDS = 10
MAX_SEEDANCE_DURATION_SECONDS = 15


class PipelineRunner:
    def __init__(
        self,
        artifact_store: ArtifactStore,
        job_store: JobStore,
        project_store: ProjectStore,
        script_provider: ScriptProvider,
        image_provider: ImageProvider,
        video_provider: VideoProvider,
        harness_manager: HarnessManager,
        pipeline_logger: PipelineEventLogger,
        model_logger: ModelCallLogger,
        settings: Settings | None = None,
        progress_callback: Callable[[str, dict], None] | None = None,
    ):
        self.artifact_store = artifact_store
        self.job_store = job_store
        self.project_store = project_store
        self.script_provider = script_provider
        self.image_provider = image_provider
        self.video_provider = video_provider
        self.harness_manager = harness_manager
        self.pipeline_logger = pipeline_logger
        self.model_logger = model_logger
        self.settings = settings or Settings()
        self.progress_callback = progress_callback
        self.composer = EpisodeComposer()
        self.script_quality_harness = ScriptQualityHarness()

    def create_job(self, request: JobCreate) -> JobRecord:
        project_id = request.project_id
        if project_id is None:
            project_id = self.project_store.create_project(request.topic).project_id
        else:
            self.project_store.get_project(project_id)

        job_id = self._next_job_id()
        artifact_dir = self.artifact_store.create_job_dir(job_id, project_id=project_id)
        request = request.model_copy(update={"project_id": project_id})
        self.job_store.create_job(request, artifact_dir, job_id=job_id)
        self.artifact_store.write_json(job_id, "input.json", request.model_dump(mode="json"))
        try:
            if request.project_id and self._project_has_reusable_assets(project_id):
                return self._continue_project_from_latest(job_id, project_id)
            return self._run_script_phase(job_id, request)
        except Exception as exc:
            if self.job_store.get_job(job_id).status != JobStatus.FAILED:
                self._fail_job(job_id, JobStatus.SCRIPTING.value, exc)
            raise

    def approve_script(self, job_id: str) -> JobRecord:
        job = self.job_store.get_job(job_id)
        self.artifact_store.register_job_dir(job_id, job.artifact_dir)
        if job.status != JobStatus.SCRIPT_REVIEW_PENDING:
            raise ValueError(f"当前状态不允许批准剧本：{job.status.value}")

        script_data = self.artifact_store.read_json(job_id, "script/reviewed_script.json")
        script = ScriptBundle.model_validate(script_data)
        self.harness_manager.run("after_script_approved", {"job_id": job_id}, script)
        if job.project_id is not None:
            self.artifact_store.copy_to_project_latest(job_id, job.project_id, "script")
            for relative_path in ["characters", "shots", "videos"]:
                self.artifact_store.delete_from_project_latest(job.project_id, relative_path)
            self.project_store.update_latest_job(job.project_id, job_id)
        self._transition(job_id, JobStatus.SCRIPT_APPROVED)
        try:
            return self._run_character_phase(job_id, script)
        except Exception as exc:
            if self.job_store.get_job(job_id).status != JobStatus.FAILED:
                self._fail_job(job_id, JobStatus.CHARACTER_DESIGNING.value, exc)
            raise

    def approve_characters(self, job_id: str) -> JobRecord:
        job = self.job_store.get_job(job_id)
        self.artifact_store.register_job_dir(job_id, job.artifact_dir)
        if job.status != JobStatus.CHARACTER_REVIEW_PENDING:
            raise ValueError(f"当前状态不允许批准人物形象：{job.status.value}")

        script = ScriptBundle.model_validate(self.artifact_store.read_json(job_id, "script/reviewed_script.json"))
        characters = self.artifact_store.read_json(job_id, "characters/character_profiles.json")
        self.harness_manager.run("after_character_approved", {"job_id": job_id}, characters)
        if job.project_id is not None:
            self.artifact_store.copy_to_project_latest(job_id, job.project_id, "script")
            self.artifact_store.copy_to_project_latest(job_id, job.project_id, "characters")
            for relative_path in ["shots", "videos"]:
                self.artifact_store.delete_from_project_latest(job.project_id, relative_path)
            self.project_store.update_latest_job(job.project_id, job_id)
        self._transition(job_id, JobStatus.CHARACTER_APPROVED)
        return self._run_video_phase(job, script, characters)

    def continue_job(self, job_id: str) -> JobRecord:
        job = self.job_store.get_job(job_id)
        if job.status == JobStatus.SCRIPT_REVIEW_PENDING:
            return self.approve_script(job_id)
        if job.status == JobStatus.CHARACTER_REVIEW_PENDING:
            return self.approve_characters(job_id)
        return job

    def reject_script(self, job_id: str, reason: str) -> JobRecord:
        job = self.job_store.update_status(job_id, JobStatus.SCRIPT_REVIEW_PENDING, last_error=reason)
        self.pipeline_logger.log(job_id, "script_rejected", {"reason": reason})
        self.artifact_store.write_json(job_id, "status.json", job.model_dump(mode="json"))
        return job

    def regenerate_script(self, job_id: str, notes: str = "") -> JobRecord:
        job = self.job_store.get_job(job_id)
        request = JobCreate(
            topic=job.topic,
            duration_seconds=job.duration_seconds,
            episode_count=job.episode_count,
            ratio=job.ratio,
            style=job.style,
            notes=notes or job.notes,
            project_id=job.project_id,
        )
        return self._run_script_phase(job_id, request)

    def reject_characters(self, job_id: str, reason: str) -> JobRecord:
        job = self.job_store.update_status(job_id, JobStatus.CHARACTER_REVIEW_PENDING, last_error=reason)
        self.pipeline_logger.log(job_id, "characters_rejected", {"reason": reason})
        self.artifact_store.write_json(job_id, "status.json", job.model_dump(mode="json"))
        return job

    def regenerate_character(self, job_id: str, character_id: str) -> JobRecord:
        job = self.job_store.get_job(job_id)
        self.artifact_store.register_job_dir(job_id, job.artifact_dir)
        script = ScriptBundle.model_validate(self.artifact_store.read_json(job_id, "script/reviewed_script.json"))
        target = next(profile for profile in script.characters if profile.character_id == character_id)
        character_dir = self.artifact_store.job_dir(job_id) / "characters" / character_id
        image = self.image_provider.generate_character_image(job_id, target, str(character_dir))
        target.approved_reference_image = image.approved_path
        target.approved_reference_url = image.approved_url
        self.artifact_store.write_json(job_id, f"characters/{character_id}/profile.json", target.model_dump(mode="json"))
        characters = self.artifact_store.read_json(job_id, "characters/character_profiles.json")
        for item in characters:
            if item["character_id"] == character_id:
                item.update(target.model_dump(mode="json"))
        self.artifact_store.write_json(job_id, "characters/character_profiles.json", characters)
        self.pipeline_logger.log(job_id, "character_regenerated", {"character_id": character_id})
        return self.job_store.get_job(job_id)

    def cancel_job(self, job_id: str) -> JobRecord:
        job = self.job_store.get_job(job_id)
        if job.status == JobStatus.COMPLETED:
            return job
        return self._transition(job_id, JobStatus.CANCELLED)

    def _run_script_phase(self, job_id: str, request: JobCreate) -> JobRecord:
        self._transition(job_id, JobStatus.SCRIPTING)
        self.harness_manager.run("before_script", {"job_id": job_id})
        last_exc: Exception | None = None
        script = None
        for attempt in range(1, 3):
            try:
                script = self.script_provider.generate_script(job_id, request)
                break
            except Exception as exc:
                last_exc = exc
                if attempt == 2:
                    raise
                self.pipeline_logger.log(
                    job_id,
                    "script_generation_retry",
                    {"attempt": attempt, "error": str(exc)},
                )
        if script is None:
            raise RuntimeError("剧本生成失败") from last_exc
        self.artifact_store.write_json(job_id, "script/series_bible.json", {"series_bible": script.series_bible})
        self.artifact_store.write_json(
            job_id,
            "script/episodes.json",
            [episode.model_dump(mode="json") for episode in script.episodes],
        )
        self.artifact_store.write_json(job_id, "script/reviewed_script.json", script.model_dump(mode="json"))
        self.artifact_store.write_json(job_id, "script/review.md", {"摘要": script.series_bible, "剧名": script.series_title})
        self.harness_manager.run("after_script", {"job_id": job_id}, script)
        report = self.script_quality_harness.after_script({"job_id": job_id}, script)
        self.artifact_store.write_json(
            job_id,
            "harness/script_quality_report.json",
            report.model_dump(mode="json"),
        )
        self.harness_manager.run(
            "before_script_review",
            {
                "job_id": job_id,
                "script_quality_report_path": "harness/script_quality_report.json",
            },
            script,
        )
        return self._transition(job_id, JobStatus.SCRIPT_REVIEW_PENDING)

    def _run_character_phase(self, job_id: str, script: ScriptBundle) -> JobRecord:
        self._transition(job_id, JobStatus.CHARACTER_DESIGNING)
        self.harness_manager.run("before_character_generation", {"job_id": job_id}, script)
        character_records = []
        for profile in script.characters:
            character_dir = self.artifact_store.job_dir(job_id) / "characters" / profile.character_id
            self._emit_progress(
                "character_generation_started",
                {
                    "job_id": job_id,
                    "character_id": profile.character_id,
                    "character_name": profile.name,
                },
            )
            image = self.image_provider.generate_character_image(job_id, profile, str(character_dir))
            profile.approved_reference_image = image.approved_path
            profile.approved_reference_url = image.approved_url
            self.artifact_store.write_json(
                job_id,
                f"characters/{profile.character_id}/profile.json",
                profile.model_dump(mode="json"),
            )
            (Path(character_dir) / "seedream_prompt.txt").write_text(image.prompt, encoding="utf-8")
            character_records.append(profile.model_dump(mode="json"))
            self._emit_progress(
                "character_generation_completed",
                {
                    "job_id": job_id,
                    "character_id": profile.character_id,
                    "character_name": profile.name,
                    "approved_path": image.approved_path,
                    "approved_url": image.approved_url,
                },
            )
        self.artifact_store.write_json(job_id, "characters/character_profiles.json", character_records)
        self.harness_manager.run("after_character_generation", {"job_id": job_id}, character_records)
        self.harness_manager.run("before_character_review", {"job_id": job_id}, character_records)
        return self._transition(job_id, JobStatus.CHARACTER_REVIEW_PENDING)

    def _run_video_phase(self, job: JobRecord, script: ScriptBundle, characters: list[dict]) -> JobRecord:
        self._transition(job.job_id, JobStatus.SHOT_PLANNING)
        for episode_index, episode in enumerate(script.episodes, start=1):
            expanded_shots = self._normalize_episode_shots(episode.shots)
            for shot_index, shot in enumerate(expanded_shots, start=1):
                shot.shot_order = shot_index
                shot.seedance_prompt = build_seedance_prompt(
                    series_title=script.series_title,
                    episode_number=episode_index,
                    shot_number=shot_index,
                    shot=shot,
                    style=job.style,
                )
                shot.reference_images = [
                    character.get("approved_reference_url") or character["approved_reference_image"]
                    for character in characters
                    if character.get("character_id") in shot.characters
                    and (character.get("approved_reference_url") or character.get("approved_reference_image"))
                ]
            episode.shots = expanded_shots
            self.artifact_store.write_json(job.job_id, f"shots/{episode.episode_id}.json", episode.model_dump(mode="json"))

        if job.project_id is not None:
            self.artifact_store.copy_to_project_latest(job.job_id, job.project_id, "shots")

        self._transition(job.job_id, JobStatus.VIDEO_GENERATING)
        job_dir = self.artifact_store.job_dir(job.job_id)
        try:
            for episode in script.episodes:
                shot_paths = self._generate_episode_videos(job, episode, job_dir)
                self._transition(job.job_id, JobStatus.COMPOSING)
                final_path = job_dir / "videos" / episode.episode_id / "final.mp4"
                self.composer.compose(shot_paths, final_path)
        except Exception as exc:
            self._fail_job(job.job_id, JobStatus.VIDEO_GENERATING.value, exc)
            raise

        if job.project_id is not None:
            self.artifact_store.copy_to_project_latest(job.job_id, job.project_id, "videos")
            self.project_store.update_latest_job(job.project_id, job.job_id)
        return self._transition(job.job_id, JobStatus.COMPLETED)

    def _continue_project_from_latest(self, job_id: str, project_id: str) -> JobRecord:
        for relative_path in ["script", "characters"]:
            self.artifact_store.copy_from_project_latest(project_id, job_id, relative_path)

        job = self.job_store.get_job(job_id)
        script = ScriptBundle.model_validate(self.artifact_store.read_json(job_id, "script/reviewed_script.json"))
        characters = self.artifact_store.read_json(job_id, "characters/character_profiles.json")
        self._transition(job_id, JobStatus.SCRIPT_APPROVED)
        self._transition(job_id, JobStatus.CHARACTER_APPROVED)
        return self._run_video_phase(job, script, characters)

    def _project_has_reusable_assets(self, project_id: str) -> bool:
        project = self.project_store.get_project(project_id)
        if project.latest_job_id is None:
            return False
        latest_dir = self.artifact_store.project_latest_dir(project_id)
        return (
            (latest_dir / "script" / "reviewed_script.json").exists()
            and (latest_dir / "characters" / "character_profiles.json").exists()
        )

    def _transition(self, job_id: str, status: JobStatus) -> JobRecord:
        previous = self.job_store.get_job(job_id).status if self._job_exists(job_id) else None
        job = self.job_store.update_status(job_id, status)
        self.artifact_store.write_json(job_id, "status.json", job.model_dump(mode="json"))
        self.pipeline_logger.log(
            job_id,
            "state_changed",
            {"from": previous.value if previous else None, "to": status.value},
        )
        return job

    def _job_exists(self, job_id: str) -> bool:
        try:
            self.job_store.get_job(job_id)
            return True
        except KeyError:
            return False

    def _next_job_id(self) -> str:
        return f"job_{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:8]}"

    def _emit_progress(self, event: str, payload: dict) -> None:
        if self.progress_callback is not None:
            self.progress_callback(event, payload)

    def _generate_episode_videos(self, job: JobRecord, episode, output_dir: Path) -> list[Path]:
        ordered_results: dict[int, Path] = {}
        with ThreadPoolExecutor(max_workers=self.settings.seedance_concurrency) as executor:
            future_map = {}
            for shot in episode.shots:
                self.harness_manager.run("before_video_generation", {"job_id": job.job_id}, shot)
                future = executor.submit(
                    self.video_provider.generate_shot_video,
                    job.job_id,
                    episode.episode_id,
                    shot,
                    str(output_dir),
                )
                future_map[future] = shot

            for future in as_completed(future_map):
                shot = future_map[future]
                video = future.result()
                shot.video_path = video.video_path
                ordered_results[shot.shot_order or 0] = Path(video.video_path)
                self.harness_manager.run("after_video_generation", {"job_id": job.job_id}, shot, video)

        return [ordered_results[index] for index in sorted(ordered_results)]

    def _normalize_episode_shots(self, shots: list) -> list:
        split_shots = self._split_long_shots(shots)
        normalized_groups: list[list] = []
        current_group: list = []
        current_duration = 0

        for shot in split_shots:
            if not current_group:
                current_group = [shot]
                current_duration = shot.duration_seconds
                continue

            if current_duration < MIN_SEEDANCE_DURATION_SECONDS or current_duration + shot.duration_seconds <= TARGET_SEEDANCE_DURATION_SECONDS:
                current_group.append(shot)
                current_duration += shot.duration_seconds
                continue

            normalized_groups.append(current_group)
            current_group = [shot]
            current_duration = shot.duration_seconds

        if current_group:
            normalized_groups.append(current_group)

        if len(normalized_groups) >= 2:
            last_duration = sum(shot.duration_seconds for shot in normalized_groups[-1])
            previous_duration = sum(shot.duration_seconds for shot in normalized_groups[-2])
            if last_duration < MIN_SEEDANCE_DURATION_SECONDS and previous_duration + last_duration <= MAX_SEEDANCE_DURATION_SECONDS:
                normalized_groups[-2].extend(normalized_groups.pop())

        return [self._merge_shot_group(group) for group in normalized_groups]

    def _split_long_shots(self, shots: list) -> list:
        split = []
        for shot in shots:
            if shot.duration_seconds <= TARGET_SEEDANCE_DURATION_SECONDS:
                split.append(shot)
                continue
            remaining = shot.duration_seconds
            part = 1
            while remaining > 0:
                current_duration = min(TARGET_SEEDANCE_DURATION_SECONDS, remaining)
                split.append(
                    shot.model_copy(
                        update={
                            "shot_id": f"{shot.shot_id}_part{part}",
                            "duration_seconds": current_duration,
                        }
                    )
                )
                remaining -= current_duration
                part += 1
        return split

    def _merge_shot_group(self, shots: list) -> object:
        if len(shots) == 1:
            return shots[0]

        def _unique(values: list[str]) -> list[str]:
            seen = set()
            ordered = []
            for value in values:
                if value and value not in seen:
                    seen.add(value)
                    ordered.append(value)
            return ordered

        merged_dialogue = [line for shot in shots for line in shot.dialogue if str(line).strip()]
        return shots[0].model_copy(
            update={
                "shot_id": "__".join(shot.shot_id for shot in shots),
                "duration_seconds": sum(shot.duration_seconds for shot in shots),
                "scene_location": " -> ".join(_unique([shot.scene_location for shot in shots])),
                "characters": _unique([character for shot in shots for character in shot.characters]),
                "visual_description": " 随后，".join(shot.visual_description for shot in shots if shot.visual_description),
                "dialogue": merged_dialogue,
                "camera": "；".join(_unique([shot.camera for shot in shots])),
                "emotion": "；".join(_unique([shot.emotion for shot in shots])),
            }
        )

    def _fail_job(self, job_id: str, phase: str, exc: Exception) -> JobRecord:
        job = self.job_store.update_status(job_id, JobStatus.FAILED, failed_phase=phase, last_error=str(exc))
        self.artifact_store.write_json(job_id, "status.json", job.model_dump(mode="json"))
        self.pipeline_logger.log(
            job_id,
            "job_failed",
            {"phase": phase, "error": str(exc)},
        )
        return job
