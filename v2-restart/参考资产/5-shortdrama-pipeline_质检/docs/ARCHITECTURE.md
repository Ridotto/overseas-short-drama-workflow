# 架构说明

中文 | [English](ARCHITECTURE.en.md)

`shortdrama-pipeline` 是一个后端优先的中文短剧生产流水线。它把“生成剧本、生成主体人物图、人工审核、生成分镜视频、拼接成片”拆成清晰的状态机和 Artifact 目录，方便后续接 CLI、API、前端或外部调度系统。

## 设计目标

- 中文优先：剧本、人物设定、Seedance prompt 和审核摘要都面向中文短剧语境。
- 轻量后端：先把模型链路、状态机、日志、Artifact 和审核门槛跑稳，再扩展 UI。
- 人工可控：剧本和人物图必须审核通过后才进入下一阶段。
- 可续生产：同一项目只复用已经批准的剧本和人物资产。
- 可测试：fake provider 可以在不调用线上模型的情况下跑完整流程。

## 核心流程

```text
create job
  -> Seed 2.0 生成中文剧本
  -> 写入脚本质量报告
  -> script_review_pending
  -> approve script
  -> Seedream 逐角色生成人物图
  -> character_review_pending
  -> approve characters
  -> Seedance 2.0 生成 shot 视频
  -> ffmpeg 拼接每集成片
  -> completed
```

两个人工审核点是流水线的核心边界：

- 剧本批准前，不会生成人物图。
- 人物批准前，不会生成视频。

只有批准后的剧本和人物图会复制到 `project/latest`。因此 `continue-project` 会沿用稳定资产，不会把未审核内容当成项目基线。

## 主要模块

- `config.py`：环境变量和 `.env` 读取。
- `models.py`：Pydantic 数据模型，包括任务、项目、剧本、人物、质检和视频结果。
- `prompts.py`：中文 prompt 构造器，覆盖剧本、人物图和 Seedance shot。
- `providers.py`：fake provider 和 Ark 线上 provider，封装 Seed、Seedream、Seedance 调用。
- `pipeline.py`：状态机、阶段流转、续生产和失败处理。
- `harness.py`：Harness Hook 接口和只告警的脚本质量检查。
- `storage.py`：SQLite 任务/项目元数据和本地 Artifact 存储。
- `cli.py`：命令行和交互式 shell。
- `api.py`：FastAPI 入口，给后续前端或外部系统使用。
- `composer.py`：基于 ffmpeg 的单集视频拼接。
- `logging.py`：模型调用日志和敏感字段脱敏。

## 状态模型

用户能感知到的项目阶段包括：

- 剧本生成中
- 剧本待审核
- 剧本已批准
- 人物生成中
- 人物待审核
- 人物已批准
- 视频生成中
- 已完成

技术失败会记录为 `failed`，并保存：

- `failed_phase`：失败发生在哪个阶段。
- `last_error`：最近一次错误信息。
- `logs/model_calls.jsonl`：模型调用日志，敏感字段会脱敏。

## Artifact 目录

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

`runs/<job_id>` 保存单次任务的完整过程数据。`latest/` 只保存项目中最近一次已批准、可复用的资产。

`outputs/` 默认不会提交到 git，因为它可能包含付费模型输出、日志、SQLite 数据库和大体积媒体文件。

## 视频生成策略

Seedance 任务通常需要排队，视频阶段支持同一集内并发生成：

- 默认并发数：`2`
- 最大并发数：`5`
- 不同集之间暂时串行
- 拼接顺序始终按 `shot_order`，不按任务完成先后

这个策略可以提升吞吐，同时避免并发完成顺序影响剧情顺序。

## Harness Hook

当前 harness 保持轻量：

- 在关键阶段前后提供 hook 扩展点。
- 脚本生成后输出 `harness/script_quality_report.json`。
- 质检只评分和告警，不自动重写、不自动拒绝、不阻塞审核。

未来可以在 hook 上接更复杂的能力，例如人工审核台、脚本重写器、人物一致性检查、内容安全检查或外部工作流系统。

## 边界与扩展方向

当前项目专注后端生产链路，还不包含：

- 多用户权限
- Web 可视化编辑器
- 云端对象存储
- 成本和额度管理
- 时间线级别的视频编辑

这些能力可以建立在现有状态机和 Artifact 结构之上逐步扩展。
