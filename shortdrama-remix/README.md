# shortdrama-remix 当前主链入口

这个目录现在是 `自动化编剧` 项目的当前主执行链，不是参考资产，也不是方法论库。

它在最终产品架构里的位置是“生产层”。用户入口在项目内主控：

```text
skills/shortdrama-main-controller/SKILL.md
```

产品分层：

```text
用户层：自然语言 / rewrite-* 高级命令 / 未来网页入口
主控层：shortdrama-main-controller
生产层：source-import / short-drama-write / clean reviewer / 按需 helper agent
能力层：skills / references / contracts / state
```

用户不直接面对本目录里的多个 skill。主控负责把用户需求、源本、新壳方向、蓝图确认、正文交付和反馈回流串起来；本目录负责把这些动作变成可执行产物。

执行时直接读并使用本目录里的本地执行副本：

- `skills/shortdrama-main-controller/SKILL.md`
- `skills/source-import/SKILL.md`
- `skills/short-drama-write/SKILL.md`
- `contracts/short_drama_form_lock_v1.md`

`vendor/` 里的外部原件只作冻结来源和追溯证据，不作为当前产品直跑入口。不要再把这些文件抽成 workflow 摘要、检查项或“可参考方法”。如果生产失败，修本目录里的可执行文件或具体产物，不回到外层 v20 / v3 / V63 继续堆规则。

任何新增能力只有进入以下三类交接物，才算接入当前产品：

1. 用户可确认的商业项目包 / 创作蓝图包；
2. writer 必须消费的分集执行包；
3. reviewer / polish 的硬边界。

只留下“可参考”“建议采纳”“知识库摘要”的内容，不算接入。

当前原则：

1. 最终产物必须是短剧剧本，不是电视剧、网剧、小说、故事梗概或 screenplay 泛型稿。
2. `oh-story-claudecode` 只保留 `story-import` 相关冻结来源，用于追溯源本导入、拆解和状态追踪的来源。
3. `short-drama` 是短剧写稿执行底座：直接复制并执行它的 `SKILL.md` 和 references，不做摘要替代。
4. `how-to-make-script` 不整包进主链；当前只把 `dialogue-subtext` 的台词层能力蒸馏成本地 `dialogue-polish-brief.md`，由 `/dialogue-polish` 固定执行。
5. `shortdrama-pipeline` 不进入文本原型，也不预设为后续运行壳；未来如确实需要，只能单点参考任务状态或 artifact 目录组织，不能接它的剧本到视频主链。

硬约束文件：

- `contracts/short_drama_form_lock_v1.md`
- `contracts/clean_reviewer_protocol_v1.md`

已复制执行文件：

- `skills/source-import/SKILL.md`（从 `oh-story-claudecode/skills/story-import/SKILL.md` 改造后的短剧源本导入入口）
- `skills/short-drama-write/SKILL.md`（从 `short-drama/SKILL.md` 改造后的源本驱动短剧写稿入口）
- `vendor/short-drama/SKILL.md` 与 `vendor/short-drama/references/`（冻结原件；本地执行使用 `skills/short-drama-write/`）
- `vendor/oh-story-claudecode/skills/story-import/`（冻结来源；当前源本导入只执行本地改造后的 `skills/source-import/SKILL.md`）

任何 writer / reviewer / quality gate 只要发现稿子滑向电视剧、网剧或泛型戏剧，必须先打回短剧形态，不允许继续做风格润色。

## 当前执行原则

用户层先进入 main controller；生产层先跑 copied files，再改 copied files：

1. 用户自然语言默认由 `skills/shortdrama-main-controller/SKILL.md` 路由。
2. 用户层高级命令统一使用 `/rewrite-start`、`/rewrite-blueprint`、`/rewrite-write`、`/rewrite-polish`、`/rewrite-review`、`/rewrite-continue`、`/rewrite-export`、`/rewrite-status`。
3. 源本吸收从 `skills/source-import/SKILL.md` 进入；它是本地复制并改造后的执行文件，不是摘要。
4. 短剧写稿从 `skills/short-drama-write/SKILL.md` 的 `/write-from-source -> /plan -> /characters -> /outline -> /episode -> /dialogue-polish -> /review` 进入。
5. `/plan` 负责用户可见的商业项目包 / 创作蓝图包；`/outline` 负责分集执行包；`/episode` 负责正文初稿；`/dialogue-polish` 负责台词目标、声线、潜台词和去 AI 味；`/review` 负责自检和 callback 归因。
6. 蓝图、分集执行包和正文必须是一条剧情理解，不允许“给用户看的故事”和“给 writer 的隐藏剧情”分裂。
7. 长线追踪从 `/plan` 开始以轻量全剧骨架启用；首批 1-10 集只吃当前批和本集速记，`batch-state.md` 用于批次完成后的续写汇总。详见 `external_skill_reference_integration_map_2026-07-04.md`。
8. 当前不使用 `how-to-make-script` 整包，只使用已经落成本地 brief 的台词层能力。
9. `vendor/` 只保留当前链路需要的冻结来源，便于追溯和继续移植；不要直接从 vendor 原入口跑当前产品链。
10. 如果执行失败，先看失败发生在哪个 copied file，再改本地副本。

## 运行产物

当前 main 不提交源本库和新剧运行样本，只保留占位目录。新项目运行时会写入：

- `源本库/{源本名}/`
- `新剧/{新剧名}/`

历史样本和 V68 clean run 已从新 main 工作树清出，本地保全在 `.local-archive/pre-main-replacement-2026-07-04/shortdrama-runtime/`。GitHub main 只保留可复用产品链，不带旧样本产物。

当前已处理的链路缺口：既有样本证明 copied files 能跑出完整文本；V65 / V66 / 非同型样本进一步证明“源本赚钱功能 -> 新壳等价刺激动作 -> 一眼可懂代价 -> 反派主动新伤害 -> 本集兑现 -> 下一债务”这条生产链能阶段性通过。

该机制已接进：

- `skills/source-import/SKILL.md` 的源本账本与写稿交接包；
- `skills/short-drama-write/SKILL.md` 的 `/plan`、`/outline`、`/episode`、`/dialogue-polish`；
- `contracts/short_drama_form_lock_v1.md` 的短剧形态锁。

当前下一步不是继续改旧样本文本，也不是回外层扩 workflow，而是把本目录按 PRD 的产品架构收口：

- 蓝图写成用户可确认、writer 可执行的小 draft；
- 角色设定必须能下传到正文里的状态、反应和声线；
- 分集目录升级为分集执行包，承担首批强度地板、信息释放和追看债务；
- 正文写法强化视听语言、人物反应链；台词层通过 `/dialogue-polish` 固定精修；
- reviewer 调整为硬伤归因和有限 callback，不做机械禁词，不无限回上游。

只有上述可执行文件发生实质修改后，才需要重新跑 clean sample，并且必须留下本次 `run_log.md`。
