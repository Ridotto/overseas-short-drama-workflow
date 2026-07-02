# workflow run manifest

任务：飞书三星样本，按 `workflow_spec_v4_机制重构草案.md` 完整跑首批 1-10 集
版本：V15_v4workflow
日期：2026-06-30
执行 agent：Codex 主控 / 主创，后续独立 reviewer 另开干净临时 agent
使用的产品定义：`v2-restart/PRD_v4.md`
使用的 workflow spec：`v2-restart/workflow_spec_v4_机制重构草案.md`
执行说明：v4 仍是机制重构草案。本轮是用户明确要求的完整样本验证，不代表 v4 已正式替代 `workflow_spec_v2.md`。
输入源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`
目标新壳：海外豪门商战 / 家族企业 / 集数不变
输出范围：首批 1-10 集，含完整 workflow 产物、reviewer、版本对比

## 总状态

- complete
- 说明：本轮按 `workflow_spec_v4_机制重构草案.md` 完整跑完首批 1-10 集验证。`complete` 只表示本次流程和证据闭合，不表示 v4 已正式替代 v2，也不表示 V15 是导演终稿。
- creative_status：creative_pass
- source_audit_status：source_audit_pass
- delivery_status：candidate checkpoint

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | 用户已确认：豪门商战、集数不动、完整跑、完整对比 | `PRD_v15_v4workflow_需求确认摘要.md` | 足够开工；已说明 v4 为草案验证 |  |
| 1 | Source Bible / 源本分析底稿 | pass | 源本 txt；已覆盖 1-10 集 | `PRD_v15_v4workflow_Source_Bible.md` | 覆盖故事核、分集功能、高价值节点、钩子、爽点、关系、权力、信息差、情绪、禁用外形、水分烂点 | 锚点：HV1-HV9 |
| 2 | Adaptation Boundary / 洗稿边界包 | pass | Source Bible | `PRD_v15_v4workflow_Adaptation_Boundary.md` | 已区分必须保留体验、必须替换外形、自由变量、删除/修复烂点 |  |
| 3 | Source Retention Anchor / 源本留存锚点 | pass | Source Bible + Boundary | `PRD_v15_v4workflow_Source_Retention_Anchor.md` | 已压出追剧/付费锚点，不复述完整剧情 |  |
| 4 | Story Operating State / 写作前故事运行状态 | pass | Source Retention Anchor + Boundary | `PRD_v15_v4workflow_Story_Operating_State.md` | 已说明人物欲望、恐惧、误会、关系、观众等待和本批推进 |  |
| 5 | High-pressure Scene Viability / 高压节点新场面粗验 | pass | Source Bible + Story Operating State | `PRD_v15_v4workflow_HighPressure_Scene_Viability.md` | 高压节点均有人际发动机；文件/屏幕/机构流程只作辅助 |  |
| 6 | Episode Plan / 新本阶段骨架与分集功能 | pass | Retention Anchor + Scene Viability | `PRD_v15_v4workflow_Episode_Plan.md` | 每集有 opening hook、core friction、max spike、change、end button、do not consume、追问 |  |
| 7 | Pressure-chain Writer Brief / 压力链写作简报 | pass | Story Operating State + Episode Plan | `PRD_v15_v4workflow_PressureChain_Writer_Brief.md` | 每集压力链承接源本留存锚点，并给出动作/选择/代价/卡点 |  |
| 8 | Screenplay Draft / 剧本正文 | pass | `PRD_v15_v4workflow_PressureChain_Writer_Brief.md` | `PRD_v15_v4workflow_豪门商战版_首批1-10集.md` | 正文按 1-10 集完整产出；高压场锚点：E2 glass door、E7 Daddy、E9 second band、E10 live button |  |
| 9 | Rewrite Report / 返修诊断 | pass | 初稿正文 | `PRD_v15_v4workflow_rewrite_report.md` | 已定位失败层；判断为 minor polish，无 scene_engine hard issue |  |
| 10 | Pressure-chain Patch Brief / 压力链返修简报 | pass | Rewrite Report | `PRD_v15_v4workflow_pressure_chain_patch_brief.md` | 已判定不做结构返修，防止返修变加料；列明 E1/E6/E8/E10 判断 |  |
| 11 | Dialogue Polish / 台词修订 | pass | 初稿 + Patch Brief | `PRD_v15_v4workflow_dialogue_polish.md` | 判断台词可送审；提醒 E8/E10 不再加解释和忏悔演讲 |  |
| 12 | Author Ready Check / 作者准备送审检查 | pass | 正文 + rewrite/polish 文件 | `PRD_v15_v4workflow_author_ready_check.md` | 作者只给 ready for reviewer，不自判最终 pass |  |
| 13 | Reviewer 第一轮：只读正文 | pass | `PRD_v15_v4workflow_需求确认摘要.md` + `PRD_v15_v4workflow_豪门商战版_首批1-10集.md` | `PRD_v15_v4workflow_reviewer_round1_只读正文.md` | reviewer 结论 `creative_pass`；未读源本分析、作者自检、manifest、旧稿 | 干净临时 reviewer |
| 14 | Reviewer 第二轮：源本迁移审计 | pass | Source Bible + Boundary + Retention Anchor + Story Operating State + Scene Viability + Episode Plan + Writer Brief + 正文 + 源本 1-10 | `PRD_v15_v4workflow_reviewer_round2_源本审计.md` | reviewer 结论 `source_audit_pass`；链路未断，两个 callback 均为 polish 级 | 干净临时 reviewer |
| 15 | 主控判定失败层和回滚点 | pass | 作者自检 + reviewer 两轮 + story memory + 正文 | `PRD_v15_v4workflow_主控判定.md` | 判定 candidate checkpoint；不回滚，不直接宣称导演终稿 |  |
| 16 | Story memory checkpoint | pass | V15 正文 | `PRD_v15_v4workflow_story_memory_checkpoint.md` | 已记录关系、人物、信息差、伏笔、未兑现承诺、禁止提前消费和下一批入口 |  |
| 17 | Manifest / 版本记录 / 交付 | pass | 全部产物 + V3 / V8 / V12 / V13 / V14 | `PRD_v15_v4workflow_vs_v3_v8_v12_v13_v14_完整对比.md` + 本 manifest | 完整对比已完成；明确 V15 与 V14 非单向碾压，V15 为候选 checkpoint |  |

## 未完成步骤

无。

## 不允许交付原因

无协议层阻断。

注意：本轮可以作为 `candidate checkpoint` 交付讨论，但不等于导演终稿；如继续修，只建议做 E5 / E8 局部 polish，不建议回滚流程或扩 PRD。

## 本轮产物清单

- `PRD_v15_v4workflow_需求确认摘要.md`
- `PRD_v15_v4workflow_Source_Bible.md`
- `PRD_v15_v4workflow_Adaptation_Boundary.md`
- `PRD_v15_v4workflow_Source_Retention_Anchor.md`
- `PRD_v15_v4workflow_Story_Operating_State.md`
- `PRD_v15_v4workflow_HighPressure_Scene_Viability.md`
- `PRD_v15_v4workflow_Episode_Plan.md`
- `PRD_v15_v4workflow_PressureChain_Writer_Brief.md`
- `PRD_v15_v4workflow_豪门商战版_首批1-10集.md`
- `PRD_v15_v4workflow_rewrite_report.md`
- `PRD_v15_v4workflow_pressure_chain_patch_brief.md`
- `PRD_v15_v4workflow_dialogue_polish.md`
- `PRD_v15_v4workflow_author_ready_check.md`
- `PRD_v15_v4workflow_reviewer_round1_只读正文.md`
- `PRD_v15_v4workflow_reviewer_round2_源本审计.md`
- `PRD_v15_v4workflow_story_memory_checkpoint.md`
- `PRD_v15_v4workflow_主控判定.md`
- `PRD_v15_v4workflow_vs_v3_v8_v12_v13_v14_完整对比.md`
