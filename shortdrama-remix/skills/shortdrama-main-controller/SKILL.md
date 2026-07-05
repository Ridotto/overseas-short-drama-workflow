---
name: shortdrama-main-controller
description: Project-local controller for short-drama rewrite work in this repository. Use when the user asks to rewrite/remake/adapt/wash a validated short-drama source into a new shell, starts a project with /rewrite-* commands, asks for source import, blueprint, first batch writing, dialogue polish, clean review, continuation batches, export, or project status. Routes natural-language user intent to source-import, short-drama-write, dialogue-polish, clean reviewer, batch-state, and export without requiring global skill installation.
---

# Shortdrama Main Controller

This is the project-local front door for the short-drama rewrite product. It is not a separate writing engine. It routes user intent to the executable files already in this repo.

Use this controller before touching `source-import` or `short-drama-write` whenever the user is trying to operate the product rather than edit the repo itself.

## First Read

Read these files before running a production request:

1. `AGENTS.md`
2. `v2-restart/PRD_v4.md`
3. `shortdrama-remix/README.md`
4. `shortdrama-remix/contracts/short_drama_form_lock_v1.md`
5. `shortdrama-remix/contracts/clean_reviewer_protocol_v1.md`
6. `shortdrama-remix/skills/source-import/SKILL.md`
7. `shortdrama-remix/skills/short-drama-write/SKILL.md`

Do not ask the user to install a global Codex skill. This controller ships inside the repo and is reached through `AGENTS.md`.

## Product Contract

The user sees one product: a short-drama rewrite assistant.

The user should not need to know internal commands such as `/plan`, `/characters`, `/outline`, `/episode`, `/dialogue-polish`, `/review`, or `/batch-state`. Those are production-layer actions.

Default product flow:

```text
需求确认
-> 源本导入与有效性摘要
-> 洗稿方向 / 新壳方案摘要
-> 商业项目包 / 创作蓝图包
-> 当前批正文
-> 台词精修
-> internal review / 自检返修
-> clean reviewer 内容验收
-> 导出交付稿
-> delivery QA / export lint
-> 用户反馈 / 续批
```

Only stop for user confirmation at these gates:

1. Missing required input.
2. Source suitability or rewrite direction is unclear.
3. The rewrite scheme / new shell needs confirmation.
4. The creative blueprint needs confirmation before writing prose.
5. The completed batch needs user feedback or approval before continuation.

Everything else should advance automatically unless the user explicitly asks for manual control.

## User-Level Commands

Support natural language first. Also accept these product-level slash commands as aliases:

| User command | User meaning | Internal route |
| --- | --- | --- |
| `/rewrite-start` | Start a new rewrite project, import source, confirm direction | `source-import` then `short-drama-write /write-from-source` setup |
| `/rewrite-blueprint` | Generate or refresh creative blueprint | `/plan -> /characters -> /outline` |
| `/rewrite-write` | Write the current batch, default 1-10 | `/episode {range}`; default product flow continues to polish/review unless user says draft only |
| `/rewrite-polish` | Dialogue polish and AI-flavor cleanup | `/dialogue-polish {range}` |
| `/rewrite-review` | Content quality review | internal `/review {range}` plus clean reviewer for content acceptance when a pass claim is needed |
| `/rewrite-continue` | Continue next batch, such as 11-20 | `/batch-state` then next-batch outline/write/polish/review |
| `/rewrite-export` | Export user-facing deliverable | `/export` then `/delivery-qa` |
| `/rewrite-status` | Show current project progress and file locations | inspect project files and latest run logs |

Do not rename the internal commands. The `/rewrite-*` commands are user-facing aliases.

## Intake Rules

For a new project, collect or infer:

- source path or pasted source text;
- target new shell, or permission to propose options;
- target market;
- target platform/region when known, such as ReelShort, DramaBox, TikTok/Facebook ads, North America, Southeast Asia, or domestic platforms;
- output language for the final script;
- desired mode: blueprint only, standard first batch, multi-batch continuation, or local rewrite;
- total series scale if known;
- current batch range, default `1-10`;
- what the user wants to keep;
- what the user wants to avoid.

If the source is only a summary, fragment, link, or title, do not run the formal script-writing chain. Use blueprint/diagnosis mode and state the limitation.

If the target market, platform, or output language indicates overseas work, set overseas mode as an internal state from the start. Do not add a separate user-facing gate; use the conservative localization policy: protect existing effective material first, require evidence for every localization suggestion, and let the user confirm direction or depth unless they explicitly delegate that decision.

## Mode Routing

### Blueprint / Diagnosis

Use when source material is incomplete, the user only wants direction, or the rewrite premise is not confirmed.

Stop after source analysis, rewrite scheme, and creative blueprint. Do not write episodes.

### Standard First Batch

Default. Treat the project as a full short-drama series, but deliver the first batch first.

Default range is `1-10`. Do not treat these episodes as a sample detached from the rest of the series.

### Multi-Batch Continuation

Use when the user asks for 11-20, later batches, 60 episodes, 80 episodes, or a complete series.

Before writing the next batch, refresh or generate `batch-state.md`. Track consumed truths, relationship state, unresolved debts, paid hooks, and forbidden early reveals.

### Local Rewrite / Repair

Use only when the project already has a blueprint and episode files. Fix the smallest responsible layer:

- dialogue/AI flavor -> `/dialogue-polish`;
- thin scene execution -> `/episode`;
- weak episode mission -> `/outline`;
- broken character behavior -> `/characters`;
- wrong project premise -> `/plan` or source direction.

Do not silently rewrite upstream artifacts when the user asked for a local fix.

## Production Rules

- Every claim that a run followed the current chain must be backed by `run_log.md`.
- Source import has its own `_import_log.md`; the new-drama project has `run_log.md`. The controller must link them: `run_log.md` should name the source library and `_import_log.md` path. If either side is missing, report the exact evidence gap instead of treating the whole chain as fully proven.
- The controller must check or create `run_log.md` as soon as a production project starts. If generated files exist but `run_log.md` is missing or incomplete, report that as a validation gap instead of treating the run as fully proven.
- User-visible blueprint and writer input must describe the same story. Do not create separate hidden剧情.
- If the source library was imported with the current contract, `09_源本留存锚点.md` must be present and `/plan` must include a strong-node adaptation audit. If an older source library lacks it, route back to `source-import` for a retention-anchor backfill before claiming the current chain is complete.
- Strong source nodes cannot disappear between source-import, blueprint, outline, episode, and review. If they are merged, delayed, downgraded, or deleted, the reason and user-confirmation status must be explicit.
- Clean reviewer is a content-acceptance gate before `/export`. It judges whether the polished script is actually good enough; it is not an export formatter and should not be used to re-review delivery packaging.
- After `/export`, run delivery QA / export lint. It checks only final-file integrity, ordering, missing episodes, metadata, and internal-field leakage; it must not rewrite or re-judge the story.
- `episodes/` are production working drafts; the user-facing final deliverable is `/export`. The final script cannot include internal tags such as `Commercial Function`, `Visible Stimulus Action`, `One-Glance Cost`, `State Delta Goal`, `Hook Type`, `Next Debt`, `Previously`, `## 状态增量`, `Dialogue Polish Notes`, review scores, run logs, or callback notes.
- Common names, short dramatic lines, and genre tropes are allowed. Only high-recognition surface combinations are hard rewrite risks.
- If a failure has a responsible layer, return once to that layer. Do not create invisible infinite callback loops before the user sees a blueprint or script.

## Multi-Agent Policy

The main controller owns the user relationship and final decision.

- `source-import`, `short-drama-write`, and `/dialogue-polish` may run in the main controller unless isolation is needed.
- Clean reviewer must follow `contracts/clean_reviewer_protocol_v1.md` when making a quality-pass claim. It should not read author self-review, main-controller conclusions, prior praise, or earlier verdicts before first verdict.
- Helper agents are allowed only for bounded side work such as external reference audits, genre research, or independent review.
- Nested sub-agent delegation is off by default. If a helper needs another helper, route that request back to the main controller.

## Status Command

For `/rewrite-status`, report:

- current mode;
- source library path;
- new project path;
- `run_log.md` status;
- latest confirmed gate;
- completed files;
- next recommended action;
- missing run logs or validation gaps.

Be explicit when a capability is wired but not yet clean-run validated.
