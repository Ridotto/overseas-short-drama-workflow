# 自动化编剧项目 · Agent 入口说明

默认中文交流。这个项目当前仍在产品流程验证阶段，不是工程实现阶段。

## 当前主入口

进入项目后，先看：

1. `v2-restart/当前状态_2026-07-01_重收口.md`
2. `v2-restart/当前工作入口.md`
3. `v2-restart/项目基础说明.md`
4. `v2-restart/PRD_v4.md`
5. `v2-restart/全版本能力回收总账_2026-07-01.md`
6. `v2-restart/能力归层与交接矩阵_2026-07-01.md`
7. `v2-restart/workflow重建交接链草案_2026-07-01.md`
8. `v2-restart/原项目能力全集盘点_2026-07-01.md`
9. `v2-restart/原项目能力对账表_2026-07-01.md`
10. `v2-restart/全量要求层级交接对账表_2026-07-01.md`
11. `v2-restart/层级归位表_2026-07-01.md`
12. `v2-restart/skill_chain_spec_v1.md`
13. `v2-restart/workflow_spec_v16_全能力交接候选版.md`
14. `v2-restart/workflow_spec_v15_工位合同候选版.md`
15. `v2-restart/workflow_spec_v2.md`
16. `v2-restart/workflow_execution_protocol_v1.md`
17. `v2-restart/样本验证/`

`v2-restart/设计提纲_v8.md` 只作为参考文档、设计推演和规则池。只有当 `PRD_v4.md` 和当前 workflow 来源不够细、需要追溯设计原因时才看。

## 不要默认继承的旧方向

不要把以下内容当当前产品方案：

- `v2-restart/设计提纲_v1草案.md` 到 `v2-restart/设计提纲_v7.md`
- `v2-restart/第一阶段PRD与验证设计.md`
- `v2-restart/机制卡片_*.md`
- `v2-restart/机制诊断_*.md`
- `v2-restart/重构方案_*.md`
- `v2-restart/盲测/`
- `archive/do-not-use-as-product-design-2026-06-28/`

这些只作历史线索，除非任务明确要求追溯。

## 当前产品判断

当前主文档是 `v2-restart/PRD_v4.md`。

当前没有已通过验证的正式候选执行细则。

`workflow_spec_v16_全能力交接候选版.md` 是当前最新候选 workflow，但尚未正式化。

`workflow_spec_v15_工位合同候选版.md` 是 v16 的直接前身，只作来源和对照，不再作为当前最新候选。

`workflow_spec_v8_创作抓手合并候选版.md` 已跑出 V18，结果为执行完成但交付不达标，不能继续当默认 workflow。

`workflow_spec_v14_skill工位链候选版.md` 已跑出 V25，方向有效但产物仍未达送审标准，不能正式化。

当前最新根因判断：不是缺短剧概念，而是源本有效性、外部短剧手艺和 V5 的场面发动机没有稳定变成 writer 当下可执行的生产动作。重点检查 S3/S4/S5/S8/S9 的交接物是否干净。

当前重收口已经新增三份前置产物：`全版本能力回收总账_2026-07-01.md`、`能力归层与交接矩阵_2026-07-01.md`、`workflow重建交接链草案_2026-07-01.md`。它们不是正式 workflow spec，但下一版 workflow spec 必须以它们为依据，不能再直接选某个旧版本当母版。

注意：不要把 v16 误读成“只管短剧感”。短剧手艺必须生效，但不能挤掉源本有效性、洗稿边界、新壳承载、钩子卡点、爽点压放、人物关系、拉扯、信息差、反派压力、Do Not Consume、连续性和海外市场语感。

任何 agent 只要声称“跑 workflow / 重跑 / 按流程产出”，必须同时遵守 `v2-restart/workflow_execution_protocol_v1.md`，为本次运行留下轻量 `run_log`。没有 run log，只能说“有产物”，不能声称“按 workflow 完整执行”。

如果使用某个实验 workflow，run log 步骤以该 workflow 自身编号为准，并在 run log 里明确写出使用的 workflow spec。

如果入口文档、PRD、workflow spec 或用户指令之间出现冲突，不能自行选择一个继续跑；必须先报告冲突并说明会影响哪些步骤。

产品目标是：把一个已被市场验证或值得参考的短剧源本，洗成一个新壳下仍然好看、能追、能付费的新剧本。

第一阶段先验证 skill / workflow 原型，不先做网页 App，不先写工程 spec。

## Agent 分工原则

- 主控 agent 可以按需主动调用临时 sub-agent，尤其用于独立审稿、并行查资料、交叉核对散落材料；但方向、范围、优先级和最终拍板必须回到主控。
- 主控 agent：负责和用户对齐、拍板、汇总。
- 主创 agent：负责源本分析、事件载体拆解、变量迁移、新事件载体迁移、单集写作包、写新本、短剧化返修；分析和写作不要拆成两个互不相干的 agent。主创写完并返修后必须先做作者自检。
- Reviewer：每个剧本或每个首批版本单开干净临时 sub-agent，不做长期固定工位，避免上下文污染。Reviewer 第一轮不要读取主创自检，先独立审。

固定的是 reviewer 协议和审稿标准，不固定 reviewer 实例。

主控最后对比作者自检和 reviewer 意见，再决定是否改稿、等用户/导演反馈，或继续下一批。

主控不能只看最终剧本。主控必须看本次 `run_log`，确认每一步是否有产物、交接是否脏、writer 是否吃了不该吃的东西。run log 不做质量证明，不能替代剧本质量判断。

注意：旧样本 V7 的执行记录 complete 只证明旧 workflow 被执行，不证明剧本质量合格。旧样本 V7 不能作为合格样本或导演可送审基准，只能作为旧执行记录误导质量判断的证据。

## 当前下一步

当前不要继续修 V18 正文，也不要继续从 v8 小修。

当前下一步：

1. 不改 PRD；
2. 不继续修 V25 正文；
3. 不把 v15 直接正式化；
4. 不把 v16 直接正式化；
5. 先对 `workflow_spec_v16_全能力交接候选版.md` 做静态对齐检查；
6. 再用同一飞书三星样本完整跑首批 1-10 集；
7. 对比 V5 / V22 / V24 / V25 / v16 新版，确认产物是否显著提升。

旧 checkpoint / goal 文件只作历史记录，不作为当前下一步。

## 记录规则

重要决策和阶段性结果记录到 `docs/决策与变更.md`。

不要把临时想法、旧方案复活或大段推演继续塞进设计提纲。
