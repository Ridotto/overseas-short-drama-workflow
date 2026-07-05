# Issue 与发布流程

本文服务当前正式产品包的 issue 处理、修复分支和发布检查。目标不是把流程做重，而是让用户反馈能进入正确分支，避免再次把样本修稿、旧链路复活和正式产品发布混在一起。

## Issue 进入规则

GitHub issue 分两类：

- `主链运行问题`：当前 `shortdrama-remix` 主链的可复现问题。
- `产品反馈 / 改进建议`：入口、流程、质量标准、续批、导出或文档层面的改进。

不接受空泛 issue：

- 只说“质量不好”，但没有指出源本功能丢失、短剧刺激不足、洗稿边界、台词、续批状态或导出污染。
- 要求恢复 `v20`、`v3-executor-first`、`V63` 或旧样本路线作为当前入口。
- 把单一样本人工修稿当成主链能力通过。

涉及“按当前主链执行”的反馈，优先要求提供：

```text
shortdrama-remix/新剧/{项目名}/run_log.md
```

没有 `run_log.md` 时，只能判断“产物表现”，不能声称它代表当前主链。

## 分支规则

每个明确修复使用一个独立分支：

```text
codex/issue-{issue-number}-{short-slug}
```

如果没有 GitHub issue，但仍是明确小修，可以先在 `codex/next` 做，提交信息里写清范围。不要直接在 `main` 上实验。

分支只改负责层：

- 用户入口问题：改 `README.md`、`QUICKSTART.md`、`AGENTS.md` 或 `shortdrama-main-controller`。
- 源本导入问题：改 `shortdrama-remix/skills/source-import/SKILL.md`。
- 写作链问题：改 `shortdrama-remix/skills/short-drama-write/SKILL.md` 或其 references。
- 短剧形态边界：改 `shortdrama-remix/contracts/short_drama_form_lock_v1.md`。
- 发布/反馈规则：改 `.github/` 或本文。

不要因为一个 issue 顺手重写 PRD、旧审计和多个 skill。

## 验证规则

按风险选择验证：

- 文档和 issue 模板：检查链接、模板字段和冷启动说明即可。
- 主控路由：做冷启动演练，确认能停在正确确认点。
- 写作链或台词精修：必须跑干净样本，留下 `run_log.md`。
- `batch-state`：至少跑一个 11-20 续批最小链路，检查状态不漂。
- 导出：检查用户交付稿不含内部字段，例如 `Commercial Function`、`Visible Stimulus Action`、`Info Release`、`Hook Type`、`Next Debt`、`Previously`、`State Delta Goal`、`## 状态增量`、`## Dialogue Polish Notes`、review verdict、run log 摘要、callback 记录和钩子/下集预告标签。

验证结论要区分：

- `wired`：能力已接入文件。
- `clean run pass`：按当前主链跑过并有 `run_log.md`。
- `quality evidence`：有 reviewer 或横向对比证据。
- `ready for main`：对新用户有直接价值，且不会带入开发噪音。

## 合回 main 标准

只有同时满足这些条件，才合回 `main`：

- 对新用户有直接价值。
- 不依赖 `codex/next` 的旧审计语境。
- 不暴露旧样本、旧输入、历史复盘或外部实验 worktree。
- 已按变更风险验证。
- README / QUICKSTART / AGENTS / 主控路由在需要时同步更新。

`main` 只保留产品包；`codex/next` 保留开发判断、治理素材和实验整合。

## 发布检查清单

发布前至少检查：

```text
git status --short
git diff --name-only main...HEAD
```

确认 diff 没有带入：

- `shortdrama-remix/源本库/*` 的真实源本产物；
- `shortdrama-remix/新剧/*` 的运行样本；
- `.local-archive/`；
- 旧 workflow、大体量审计或历史样本；
- 用户敏感文本。

如果需要宣称某个质量能力已经通过，不要只引用文档修改；必须引用对应 clean run 的 `run_log.md` 和 review 结论。
