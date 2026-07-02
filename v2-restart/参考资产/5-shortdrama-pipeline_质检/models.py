from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from pathlib import Path

from pydantic import BaseModel, Field, field_validator


class JobStatus(StrEnum):
    CREATED = "created"
    SCRIPTING = "scripting"
    SCRIPT_REVIEW_PENDING = "script_review_pending"
    SCRIPT_APPROVED = "script_approved"
    CHARACTER_DESIGNING = "character_designing"
    CHARACTER_REVIEW_PENDING = "character_review_pending"
    CHARACTER_APPROVED = "character_approved"
    SHOT_PLANNING = "shot_planning"
    VIDEO_GENERATING = "video_generating"
    COMPOSING = "composing"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"
    CANCELLED = "cancelled"


class JobCreate(BaseModel):
    topic: str
    duration_seconds: int = Field(gt=0)
    episode_count: int = Field(gt=0)
    ratio: str = "9:16"
    style: str = "竖屏短剧，强反转，真实影视感"
    notes: str = ""
    project_id: str | None = None

    @field_validator("topic")
    @classmethod
    def topic_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("短剧主题不能为空")
        return value.strip()


class JobRecord(BaseModel):
    job_id: str
    project_id: str | None = None
    status: JobStatus
    topic: str
    duration_seconds: int
    episode_count: int
    ratio: str
    style: str
    notes: str = ""
    artifact_dir: Path
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    failed_phase: str | None = None
    last_error: str | None = None


class ProjectRecord(BaseModel):
    project_id: str
    title: str
    latest_job_id: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ProjectSnapshot(BaseModel):
    project_id: str
    title: str
    latest_job_id: str | None = None
    latest_job_status: str | None = None
    script_status: str = "not_started"
    character_status: str = "not_started"
    video_status: str = "not_started"
    failed_job_count: int = 0


class CharacterProfile(BaseModel):
    character_id: str
    name: str
    role: str
    age_range: str
    appearance: str
    personality: str
    costume_style: str
    voice_style: str
    consistency_prompt: str
    approved_reference_image: str | None = None
    approved_reference_url: str | None = None


class Shot(BaseModel):
    shot_id: str
    shot_order: int | None = None
    duration_seconds: int = Field(gt=0)
    scene_location: str
    characters: list[str]
    visual_description: str
    dialogue: list[str] = Field(default_factory=list)
    camera: str
    emotion: str
    seedance_prompt: str = ""
    reference_images: list[str] = Field(default_factory=list)
    video_path: str | None = None


class Episode(BaseModel):
    episode_id: str
    title: str
    duration_seconds: int = Field(gt=0)
    summary: str
    hook: str
    shots: list[Shot]


class ScriptBundle(BaseModel):
    series_title: str
    series_bible: str
    characters: list[CharacterProfile]
    episodes: list[Episode]


class ScriptQualityIssue(BaseModel):
    level: str = "warning"
    episode_id: str
    shot_id: str | None = None
    title: str
    detail: str = ""
    suggestion: str = ""


class ScriptQualityReport(BaseModel):
    job_id: str
    overall_score: float | None = Field(default=None, ge=0, le=100)
    summary: str = ""
    episode_warnings: dict[str, list[str]] = Field(default_factory=dict)
    shot_issues: list[ScriptQualityIssue] = Field(default_factory=list)
    recommendation: str = ""


class CharacterImage(BaseModel):
    character_id: str
    prompt: str
    image_path: str
    source_url: str | None = None
    approved_path: str | None = None
    approved_url: str | None = None


class VideoResult(BaseModel):
    episode_id: str
    shot_id: str
    task_id: str
    video_path: str
