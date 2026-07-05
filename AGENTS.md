# 自动化编剧项目 · Agent 入口说明

默认中文交流。这个仓库的 `main` 分支是用户正式版：只保留运行产品需要的入口、PRD、主控、执行 skill、契约和必要 reference。

## 当前产品入口

用户在 Codex 里提出短剧改写、源本导入、蓝图、首批正文、续批、导出或状态查询请求时，先进入项目内主控：

```text
shortdrama-remix/skills/shortdrama-main-controller/SKILL.md
```

进入生产请求前，按顺序读：

1. `docs/PRD.md`
2. `docs/产品架构与主控路由_v1.md`
3. `shortdrama-remix/README.md`
4. `shortdrama-remix/skills/shortdrama-main-controller/SKILL.md`
5. `shortdrama-remix/contracts/short_drama_form_lock_v1.md`
6. `shortdrama-remix/contracts/clean_reviewer_protocol_v1.md`
7. `shortdrama-remix/skills/source-import/SKILL.md`
8. `shortdrama-remix/skills/short-drama-write/SKILL.md`

`shortdrama-main-controller`、`source-import` 和 `short-drama-write` 是当前可执行文件，不是参考材料。

## 产品目标

把一个已被市场验证或值得参考的短剧源本，洗成一个新壳下仍然好看、能追、能付费的新剧本。

产品交付的是剧本文字，不是分析报告。

## 用户层命令

自然语言是默认入口。也支持这些用户层别名：

```text
/rewrite-start
/rewrite-blueprint
/rewrite-write
/rewrite-polish
/rewrite-review
/rewrite-continue
/rewrite-export
/rewrite-status
```

这些只是用户层别名。底层内部命令仍由 `short-drama-write` 处理。

## 执行原则

- 先把项目当成完整短剧设计，再分批交付。
- 默认首批是 `1-10` 集，但不能把首批当孤立样片。
- 正式写正文前，必须先完成源本导入、改写方向和创作蓝图确认。
- 源本导入必须把强节点压成 `09_源本留存锚点.md`；蓝图、分集和 review 不能让这些强节点静默降级。
- 正文默认经过 `/episode -> /dialogue-polish -> /review -> clean reviewer -> /export -> /delivery-qa`，不要跳过台词精修、内容验收或交付检查。
- 每批完成后如需续写，先生成或刷新 `batch-state.md`。
- 任何声称“按当前链路执行”的运行，都必须留下 `run_log.md`。

## Reviewer 原则

需要质量判断时，reviewer 要保持干净视角。clean reviewer 的位置在 `/dialogue-polish` 和 `/export` 之间，用来做内容验收；`/export` 之后只做 delivery QA，不重新审剧情。

第一轮 reviewer 按 `shortdrama-remix/contracts/clean_reviewer_protocol_v1.md` 执行，只读正文和必要的源本 / 洗稿边界，不先读作者自检、主控结论、历史 verdict 或赞美性判断。

reviewer 首要判断：

```text
这是不是短剧？
有没有保住源本让人追、让人付费的能力？
新壳是否洗开？
强刺激有没有被解释、证据、系统或文件流程稀释？
源本强节点有没有完成同级或更优适配，而不是在蓝图、分集或正文里变软？
```

## 分支原则

- `main`：用户正式版。
- `codex/next`：后续开发素材、治理、实验和内部复盘。
- `codex/issue-*`：单个 issue 修复。
- `codex/feature-*`：单个功能实验。

不要把开发素材、历史审计或旧实验文档重新塞回 `main`。
