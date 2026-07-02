# workflow run manifest

任务：飞书三星样本 V23 clean run，海外豪门商战新壳首批 1-10 集洗稿验证
版本：V23 clean v11gate
日期：2026-07-01
执行 agent：clean 主创 agent
使用的产品定义：`v2-restart/PRD_v4.md`
使用的 workflow spec：`v2-restart/workflow_spec_v11_写作前故事包候选版.md`
执行协议：`v2-restart/workflow_execution_protocol_v1.md`
输入源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`
目标新壳：海外豪门商战 / 家族企业权力斗争
输出范围：首批 1-10 集

## 输入读取记录

- 已读：`AGENTS.md`
- 已读：`v2-restart/当前工作入口.md`
- 已读：`v2-restart/项目基础说明.md`
- 已读：`v2-restart/PRD_v4.md`
- 已读：`v2-restart/workflow_spec_v11_写作前故事包候选版.md`
- 已读：`v2-restart/workflow_execution_protocol_v1.md`
- 已读：源本全文，首批 1-10 集重点完整拆读，11 集后作为信息边界参照。
- 已读：`v2-restart/样本验证/飞书三星样本/当前样本测试夹具.md`
- 未读：V3 / V5 / V20 / V21 / V22 旧产物、旧 reviewer、导演反馈、版本对比、历史审计文档。

## 冲突处理

- `AGENTS.md` 中旧口径仍写“当前下一步不直接跑新样本，先整理候选 workflow”；`当前工作入口.md` 已更新为 v11 候选，并写明继续实验时默认使用 `workflow_spec_v11_写作前故事包候选版.md`。
- 本轮父任务明确要求按 v11 对同一飞书三星样本重跑 V23 clean run，因此采用 `workflow_spec_v11_写作前故事包候选版.md`。
- 测试夹具中仍写旧命名 / v2 / V9 对比口径，与本轮 V23/v11 指令冲突；本轮只采用夹具中的样本输入和已知失败点，不采用旧命名和旧 workflow 要求。

## 总状态

- partial against full v11
- clean 主创侧 Step 0-15、17 已完成；Step 16 独立 reviewer 按本轮主创任务范围跳过，需主控后续另开干净 reviewer。
- 因 Step 16 未跑，本 manifest 不能声称 full v11 through reviewer complete；只能声称 clean 主创工作链完成。

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | 父任务 + `当前样本测试夹具.md` | `PRD_v23_clean_v11gate_最小需求确认.md` | 足够开工：任务类型、新壳、市场、集数、范围、语言、用途、禁区已明确 | 锚点：文件第 0-3 节。 |
| 1 | 读源本 | pass | 源本全文；首批 1-10 集完整拆读，11 集后作信息边界参照 | `PRD_v23_clean_v11gate_Source_Bible.md` | 完整覆盖本轮范围：1-10 集功能、钩子、卡点、后续不可提前消费内容已记录 | 锚点：Source Bible 第 3、5、8 节。 |
| 2 | Source Bible | pass | 源本 + PRD v4 + v11 spec | `PRD_v23_clean_v11gate_Source_Bible.md` | 按 v11 Step 2：写出故事核、核心期待、高价值节点、信息差、源本冲突点 | 锚点：HV1-HV5；源本冲突点表。 |
| 3 | 二次需求确认 | pass | Source Bible + 初始需求 | `PRD_v23_clean_v11gate_二次需求确认.md` | 新壳能承载源本有效性，改写力度和禁区明确 | 锚点：文件第 1-6 节。 |
| 4 | Adaptation Boundary | pass | Source Bible | `PRD_v23_clean_v11gate_Adaptation_Boundary.md` | 区分保留体验、禁止外形、替代承载方向；未把强继承写成照抄事件 | 锚点：文件第 1-7 节。 |
| 5 | Creative Development Pack | pass | Adaptation Boundary | `PRD_v23_clean_v11gate_Creative_Development_Pack.md` | 新本故事成立；核心真相、角色错信、初始信息差自洽 | 锚点：文件第 2-4 节；自洽门为 pass。 |
| 6 | Stage Skeleton | pass | Creative Development Pack | `PRD_v23_clean_v11gate_Stage_Skeleton.md` | 四阶段均有追问、兑现、留白和信息边界，承接事实账本 | 锚点：阶段 A-D。 |
| 7 | Episode Pursuit Map | pass | Stage Skeleton | `PRD_v23_clean_v11gate_Episode_Pursuit_Map.md` | 每集有 Max Spike、End Button、Do Not Consume、Pressure Progression、Opposition Fuel | 锚点：Ep1-Ep10 表格。 |
| 8 | HighPressure Scene Options | pass | Episode Pursuit Map | `PRD_v23_clean_v11gate_HighPressure_Scene_Options.md` | 高压节点均做候选与优选，场面存活问通过 | 锚点：Ep2、Ep4、Ep7-8、Ep9、Ep10 优选。 |
| 9 | Playable Writer Brief | pass | Scene Options + Episode Map | `PRD_v23_clean_v11gate_Playable_Writer_Brief.md` | brief 可直接写正文；未包含 manifest/reviewer/历史争论噪音；四个存活问题可见 | 锚点：Episode 1-10 Brief。 |
| 10 | Screenplay draft | pass | Playable Writer Brief | `PRD_v23_clean_v11gate_豪门商战版_首批1-10集.md` | 按 v11 正文合同：动作/场景中文、台词英文；正文未出现内部字段；高压节点有可见动作和后果 | 锚点：Ep2 Level 42 封锁；Ep7-8 Mother Seat/金库；Ep9 Nursery；Ep10 演示舱。 |
| 11 | Rewrite report | pass | Screenplay draft | `PRD_v23_clean_v11gate_rewrite_report.md` | 先判失败层，再列症状、优先动作、回滚点；不是泛泛润色 | 锚点：文件第 1-5 节。 |
| 12 | Pressure-chain patch brief | pass | Rewrite report | `PRD_v23_clean_v11gate_pressure_chain_patch_brief.md` | 高压链路逐段核查起压/升压/爆点/收住；未默认加料 | 锚点：Ep1->Ep2、Ep7->Ep8、Ep9->Ep10。 |
| 13 | Dialogue polish | pass | Draft + patch brief | `PRD_v23_clean_v11gate_dialogue_polish.md` | 记录关键英文短台词和压缩策略；当前 screenplay 视为已完成主创台词压缩稿 | 锚点：文件第 2-5 节。 |
| 14 | 作者 ready check | pass | Dialogue polish | `PRD_v23_clean_v11gate_author_ready_check.md` | 结论 ready_for_reviewer；列出高风险节点迁移证据、风险和回滚层级 | 锚点：文件第 1-4 节。 |
| 15 | Story memory checkpoint | pass | 当前稿 | `PRD_v23_clean_v11gate_story_memory_checkpoint.md` | 记录角色状态、关系距离、权力位置、信息差、已/未兑现追问、后续禁提前消费和物件状态 | 锚点：文件第 1-8 节。 |
| 16 | 独立 reviewer | skipped | 本轮父任务指定 clean 主创交付，未要求本 agent 自行开 reviewer | 本 manifest | 允许跳过，但交付判断必须注明未跑 reviewer | clean 主创不模拟独立 reviewer。 |
| 17 | 主控版本对比与交付判断 | pass | manifest + 产物 | `PRD_v23_clean_v11gate_主创交付判断.md` | 因 clean run 限制不读旧版本，只做主创交付判断；明确 reviewer 未跑、delivery 不判 pass | 锚点：文件第 1-7 节。 |

## 未完成步骤

- Step 16 独立 reviewer 本轮由主控后续单开干净 reviewer 更合适，本 clean 主创不伪装 reviewer。

## 不允许交付原因

- 若按 full v11 through reviewer 口径：因 Step 16 独立 reviewer 未执行，不能声称完整跑完。
- 若按本轮 clean 主创任务口径：Step 0-15、17 已完成，可交主控进入 reviewer。
