# workflow run manifest

任务：飞书三星样本按 v10 workflow 完整验证，产出 V20 候选
版本：V20
日期：2026-07-01
执行 agent：干净主创 agent
使用的产品定义：`v2-restart/PRD_v4.md`
使用的 workflow spec：`v2-restart/workflow_spec_v10_V3V5完整回收候选版.md`
执行协议：`v2-restart/workflow_execution_protocol_v1.md`
输入源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`
目标新壳：海外豪门商战 / 家族企业权力斗争
目标市场：海外短剧
集数：不变
输出范围：首批 1-10 集
输出语言：动作和场景描述中文；台词英文；内部分析中文
正文用途：AI 出海短剧剧本文字，兼供人审稿
改写力度：中度偏重；不能只是换名，也不能丢源本有效性

## 总状态

- workflow execution：complete through reviewer。
- quality outcome：`revise`。
- delivery outcome：not pass / 不建议送用户或导演当作通过稿。
- 作者侧完成 Step 0-13、Step 15。
- Step 14 独立 reviewer 已补跑两轮，最终结论 `revise`。
- 作者侧质量结论：`revise`。
- 主控结论：V20 是有效的 workflow 验证样本，但不是质量通过样本。

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | `当前样本测试夹具.md`；用户任务消息；`workflow_spec_v10_V3V5完整回收候选版.md` Step 0 | `PRD_v20_v10workflow_写作前工作稿.md` Step 0 | 目标新壳、市场、集数、改写力度、输出范围、语言、用途均足够开工 | 本轮不再问用户，由夹具和任务指令替代拍板 |
| 1 | 读源本 | pass | `[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`，完整读取 1-1467 行；重点使用 1-10 集 | `PRD_v20_v10workflow_写作前工作稿.md` Step 1-2 | 已覆盖源本全剧和首批 1-10 集，未只读局部 |  |
| 2 | 源本拆文包 | pass | 源本 txt；PRD v4；v10 spec Step 1-2 | `PRD_v20_v10workflow_写作前工作稿.md` Step 1-2：故事核、核心期待、首批分集功能、HV1-HV6、链路摘要 | 拆出留存、情绪、关系、信息差、权力变化和禁止复用外形 | 高价值节点包括孕检、弃救、觉醒、回归、假孕、旧物、跪求 |
| 3 | 二次需求确认 | pass | 拆文包 + `当前样本测试夹具.md` | `PRD_v20_v10workflow_写作前工作稿.md` Step 3 | 明确新壳承载、强继承、强替换、不可提前消费 | 样本验证不再询问用户 |
| 4 | 洗稿边界包 | pass | Step 2 拆文包 | `PRD_v20_v10workflow_写作前工作稿.md` Step 4 | 区分必须保留体验、必须避开外形、可自由变量、烂点修复、新壳风险 |  |
| 5 | Beat sheet / outline | pass | Step 4 边界包 | `PRD_v20_v10workflow_写作前工作稿.md` Step 5：Story Engine、Beat List、Emotional / Retention Arc、Multi-chain Carry | 每个 beat 改变局势 / 关系 / 情绪 / 信息，标出不可提前消费 |  |
| 6 | 新壳场面迁移卡 | pass | Step 5 outline + 源本 HV 节点 | `PRD_v20_v10workflow_写作前工作稿.md` Step 6：迁移卡 1-5 | 高风险节点均给出动作链、权力变化、关系变化、信息差变化、卡点 | 第 2 集同构风险仍留给 reviewer |
| 7 | Episode function map | pass | Step 5 outline + Step 6 迁移卡 | `PRD_v20_v10workflow_写作前工作稿.md` Step 7 | 1-10 集都有 Opening Hook、Max Spike、End Button、Do Not Consume、Pressure Progression、Chain Carry |  |
| 8 | Scene packet | pass | Step 7 episode map | `PRD_v20_v10workflow_写作前工作稿.md` Step 8 | 每集有进入状态、动作推进、关系 / 权力变化、退出状态和最后一拍 |  |
| 9 | Screenplay draft | pass | Step 8 scene packet | `PRD_v20_v10workflow_豪门商战版_首批1-10集.md` | 正文为干净 screenplay，无内部字段；关键锚点：Ep2 freight lift、Ep4 credit freeze、Ep8 heir wall red seal、Ep9 sealed floor、Ep10 biometric submit | 当前正文同时作为 dialogue-polished 版本 |
| 10 | Rewrite report | pass | V20 正文 | `PRD_v20_v10workflow_rewrite_report.md` | 定位 failure layer，未用泛泛润色替代结构判断；识别第 2 集同构、第 7-8 集机制感风险 | 作者侧判断 `revise-pass` 进入后续自检 |
| 11 | Dialogue polish | pass | V20 正文 + rewrite report | `PRD_v20_v10workflow_dialogue_polish.md`；修订落在 `PRD_v20_v10workflow_豪门商战版_首批1-10集.md` | 区分保留 / 删除 / 动作化，未用台词修 scene 层问题 | 当前正文即 polish 后版本 |
| 12 | 作者 quality gate | pass | V20 正文 + rewrite/dialogue polish | `PRD_v20_v10workflow_author_quality_gate.md` | 按 contract_fit、adaptation_fit、carry_through_integrity、mechanics_pressure、continuity_invariants、expression_integrity 检查；作者侧结论 `revise` | 不是独立 reviewer pass |
| 13 | Story memory checkpoint | pass | V20 正文 | `PRD_v20_v10workflow_story_memory_checkpoint.md` | 记录关系、信息差、伏笔、角色状态、未兑现承诺、禁提前消费、下一批入口 | 可支撑 11 集后续写 |
| 14 | 独立 reviewer | pass / revise | 干净 reviewer；第一轮只读产品定义、workflow 审稿要求、V20 正文、manifest；第二轮再读源本、写作前工作稿和 workflow 证据 | `PRD_v20_v10workflow_reviewer_round1_只读正文.md`；`PRD_v20_v10workflow_reviewer_round2_源本审计.md` | reviewer 结论 `revise`：不是 pass，也不是 block | 主要问题：7-8 集同构扣除不足、信息释放过满、机制验证戏偏重 |
| 15 | 主控版本对比 | pass | V20 正文；写完 V20 后读取 V3 / V5 / V18 正文与相关自检 / reviewer 摘要；未读取 V19 | `PRD_v20_v10workflow_vs_v3_v5_v18_整体对比.md` | 已整体比较 V3 / V5 / V18 / V20；作者侧结论为 `partial / revise`；补跑 reviewer 后质量结论仍为 `revise` | V20 明显优于 V18，但不自封通过 |

## 未完成步骤

- 无。

## 不允许交付原因

- 独立 reviewer 最终判定 `revise`，不是 `pass`。
- 作者 quality gate 自判 `revise`，不能当成用户 / 导演可直接送审的 pass。
- 第 7-8 集同构扣除和信息差切分未过 v10 关键门槛。
- 第 8 集提前说穿 Adrian 弃救、切电、流产责任，削弱第 9 集旧物火葬场的首次击穿效果。
