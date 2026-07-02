# Architecture

[中文](ARCHITECTURE.md) | English

`shortdrama-pipeline` is a backend-first workflow for Chinese short-drama generation. It turns script generation, character image generation, human review, shot-level video generation, and final composition into a clear state machine plus a predictable artifact layout. The same backend can be driven by CLI, API, a future web UI, or an external scheduler.

## Design Goals

- Chinese-first: scripts, character setups, Seedance prompts, and review summaries are written for Chinese short-drama production.
- Backend-first: stabilize the model chain, state machine, logs, artifacts, and review gates before building a UI.
- Human-controlled: scripts and character images must be approved before the next expensive stage starts.
- Project continuation: an existing project only reuses approved scripts and approved character assets.
- Testable: fake providers can run the complete workflow without calling online models.

## Core Flow

```text
create job
  -> generate Chinese script with Seed 2.0
  -> write script quality report
  -> script_review_pending
  -> approve script
  -> generate character images with Seedream
  -> character_review_pending
  -> approve characters
  -> generate shot videos with Seedance 2.0
  -> compose episode videos with ffmpeg
  -> completed
```

The two human review gates are core pipeline boundaries:

- Character images are not generated before script approval.
- Videos are not generated before character approval.

Only approved scripts and approved character images are copied into `project/latest`. As a result, `continue-project` reuses stable creative assets instead of unreviewed outputs.

## Main Modules

- `config.py`: environment variables and `.env` loading.
- `models.py`: Pydantic models for jobs, projects, scripts, characters, quality reports, and video results.
- `prompts.py`: Chinese prompt builders for scripts, character images, and Seedance shots.
- `providers.py`: fake and Ark-backed providers for Seed, Seedream, and Seedance.
- `pipeline.py`: state machine, stage transitions, project continuation, and failure handling.
- `harness.py`: Harness Hook interface plus warning-only script quality checks.
- `storage.py`: SQLite job/project metadata and local artifact storage.
- `cli.py`: command-line interface and interactive shell.
- `api.py`: FastAPI entrypoint for future frontends or external systems.
- `composer.py`: ffmpeg-based episode composition.
- `logging.py`: model-call logging with sensitive field redaction.

## State Model

User-facing project stages include:

- script generating
- script review pending
- script approved
- character generating
- character review pending
- character approved
- video generating
- completed

Technical failures are stored as `failed`, with:

- `failed_phase`: the stage where the failure happened.
- `last_error`: the most recent error message.
- `logs/model_calls.jsonl`: model-call logs with sensitive fields redacted.

## Artifact Layout

```text
outputs/
  projects/
    <project_id>/
      latest/
        script/
        characters/
        videos/
      runs/
        <job_id>/
          input.json
          status.json
          script/
          characters/
          shots/
          videos/
          harness/
          logs/
```

`runs/<job_id>` stores the full data for one job. `latest/` stores only the latest approved assets that are safe to reuse within the project.

`outputs/` is ignored by git because it may contain paid model outputs, logs, SQLite databases, and large media files.

## Video Generation Strategy

Seedance tasks often spend time in queue, so the video stage supports bounded concurrency within one episode:

- default concurrency: `2`
- maximum concurrency: `5`
- episodes are still processed serially
- final composition always sorts by `shot_order`, not by completion time

This improves throughput while preserving story order.

## Harness Hook

The current harness stays intentionally lightweight:

- It exposes hook points before and after key stages.
- It writes `harness/script_quality_report.json` after script generation.
- Quality checks only score and warn. They do not rewrite, reject, or block review.

Future hooks can connect to a review dashboard, script rewriter, character-consistency checker, content-safety checker, or an external workflow system.

## Boundaries and Extension Points

The project currently focuses on the backend production chain. It does not yet include:

- multi-user permissions
- a web-based visual editor
- cloud object storage
- cost and quota management
- timeline-level video editing

Those capabilities can be built on top of the current state machine and artifact structure.
