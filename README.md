# 自动化编剧

这是一个在 Codex 里使用的短剧改写产品原型。目标是把一个已验证或值得参考的短剧源本，改写成新壳下仍然好看、能追、能付费的新短剧剧本。

当前不是网页 App，也不是命令行工具。用户在 Codex 里打开本仓库，用自然语言和主控 agent 对话。

## 快速开始

1. 把源本放进 `input/`。
2. 在 Codex 里打开仓库根目录。
3. 直接说你想怎么改写。

示例：

```text
源本在 input/my-source-script.txt。
请按当前主链，把它改写成海外女频短剧。
新壳方向：豪门医疗复仇。
正文语言：English。
先做标准首批 1-10 集。
先做源本导入、洗稿方向和创作蓝图确认，不要直接写正文。
```

更详细的上手说明见 [QUICKSTART.md](./QUICKSTART.md)。

## 当前产品入口

当前入口是项目内主控：

```text
shortdrama-remix/skills/shortdrama-main-controller/SKILL.md
```

Codex 应先通过 [AGENTS.md](./AGENTS.md) 进入主控，再由主控调度生产链。

用户不需要手动掌握内部命令。自然语言是默认入口。高级用户也可以使用这些别名：

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

这些是用户层命令。底层仍由 `source-import`、`short-drama-write`、`dialogue-polish`、clean reviewer 和 `batch-state` 执行。

## 当前主链

当前唯一生产链在：

```text
shortdrama-remix/
```

生产层文件：

- `shortdrama-remix/skills/source-import/SKILL.md`
- `shortdrama-remix/skills/short-drama-write/SKILL.md`
- `shortdrama-remix/contracts/short_drama_form_lock_v1.md`

内部默认链路：

```text
source-import
-> short-drama-write(/write-from-source /plan /characters /outline /episode)
-> /dialogue-polish
-> /review
-> clean reviewer
-> /batch-state 或 /export
```

## 产品原则

- 先做完整短剧项目，再分批交付。即使用户只要 1-10 集，也不能把首批当孤立样片。
- 用户确认的是源本理解、洗稿方向、创作蓝图和最终成稿，不是内部工位。
- 创作蓝图必须是用户可读的小 draft，同时也是 writer 的主上游。
- 正文必须像短剧：有可见冲突、当场代价、人物反应链、追看债务和付费压力。
- clean reviewer 必须保持干净视角，不能先读主控结论或作者自检。
- 任何声称“按当前主链执行”的运行都必须留下 `run_log.md`。

## 不要从这里开始

以下内容已经从当前 main 工作树清出，或降级为历史证据，不是当前入口：

- `v3-executor-first/`
- `v2-restart/workflow_spec_v20_产品契约编译候选版_2026-07-03.md`
- `v2-restart/skill_chain_spec_v3_产品契约链候选版_2026-07-03.md`
- `v2-restart/archive/`
- `archive/do-not-use-as-product-design-2026-06-28/`

它们只能从 Git 历史或本地归档追溯失败模式、对比样本和历史判断，不能复活成当前方案。

## 产物位置

源本库：

```text
shortdrama-remix/源本库/{源本名}/
```

新剧项目：

```text
shortdrama-remix/新剧/{新剧名}/
```

用户交付稿：

```text
shortdrama-remix/新剧/{新剧名}/export/
```

## 当前状态

`shortdrama-remix` 已经成为当前主链。V68 clean run 证明主链底盘可以产出过线的 EP1-10 短剧样本。之后新增了项目级 `/dialogue-polish` 环节；它已接入主链，但如需宣称该环节也已 clean-run 验证，需要另跑一次干净样本。

## 仓库治理状态

当前 main 候选只保留新用户运行产品所需的入口、PRD、主控、生产 skill、短剧契约和冻结来源。运行输入与生成产物默认不入 Git：

- 源本放入 `input/`
- 源本导入产物写入 `shortdrama-remix/源本库/`
- 新剧项目写入 `shortdrama-remix/新剧/`

历史样本、旧 workflow、旧审计和旧输入脚本已从当前工作树清出。本地保全位置见 [docs/仓库治理_2026-07-04.md](./docs/仓库治理_2026-07-04.md)。
