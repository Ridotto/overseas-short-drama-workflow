# workflow run manifest

任务：飞书三星样本豪门商战版 V11 正式 workflow 主创侧重跑 / 局部修订  
版本：V11  
日期：2026-06-30  
执行 agent：V11 干净主创 agent  
使用的产品定义：`v2-restart/PRD_v4.md`  
使用的 workflow spec：`v2-restart/workflow_spec_v2.md`  
使用的执行协议：`v2-restart/workflow_execution_protocol_v1.md`  
使用的 goal 控制：`v2-restart/goal_run_control_2026-06-30.md`  
输入源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`  
目标新壳：海外豪门商战 / 家族企业权力斗争  
目标市场：海外短剧  
输出范围：首批 1-10 集  
对比基线：`PRD_v3_豪门商战版_首批1-10集.md`、`PRD_v10_豪门商战版_首批1-10集.md`  
轮次说明：V11 是 goal 第 3 轮。V10 为 protocol-fail 内容参考，不是合格执行样本。  
禁止项确认：不修改 PRD / 设计提纲 / workflow spec / 执行协议 / goal control；不读取 `中断产物/` 中任何 V10 中断稿；Step 14 独立 reviewer 由主控后续另开。

## 总状态

- partial
- 当前已完成：manifest-first stub 已先于其他 V11 产物建立；Step 0-13、15 已完成。
- Step 14 独立 reviewer blocked：不由本 agent 执行，必须由主控另开干净 reviewer / challenge。
- 本轮总状态为 partial，不能声称 workflow complete。

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | `当前样本测试夹具.md`；`goal_run_control_2026-06-30.md`；本次任务指令 | 本 manifest：任务头、轮次说明、禁止项确认 | 足够开工：源本、新壳、市场、集数、输出范围、改写力度、禁区均明确 | manifest stub 已在 V11 其他正式产物前建立 |
| 1 | 读源本 | pass | 源本 txt 第 57-317 行完整覆盖第 1-10 集；`PRD_v4.md`；`workflow_spec_v2.md`；`workflow_execution_protocol_v1.md`；`goal_run_control_2026-06-30.md`；`当前样本测试夹具.md`；V3 正文；V9 正式工作稿；V10 正式内容稿与 challenge 汇总 | `PRD_v11_豪门商战版_写作前工作稿.md` Step 1-2 | 已覆盖本轮范围；未读取 `中断产物/` | 读源本范围：源本第 1-10 集；已收敛为 S1-E1 至 S1-E10 锚点 |
| 2 | 源本拆文包 | pass | 源本第 1-10 集；V9 正式拆文；V10 正式工作稿 | `PRD_v11_豪门商战版_写作前工作稿.md` Step 1-2 | 列出 S1-E1 至 S1-E10 的体验功能、强度来源、下游抓手、禁止外形；带出 S1-E2/E7/E8/E9/E10 必须 carry-through 的强度 |  |
| 3 | 二次需求确认 | pass | `当前样本测试夹具.md`；`goal_run_control_2026-06-30.md`；`PRD_v10_6agent_challenge汇总.md` | `PRD_v11_豪门商战版_写作前工作稿.md` Step 3 | 明确 V11 不改文档、不读中断产物、重点修机制密度/Chloe反扑/Marcus伏笔/E9 packet |  |
| 4 | 洗稿边界包 | pass | 源本拆文包；V10 共同问题 | `PRD_v11_豪门商战版_写作前工作稿.md` Step 4 | 区分必须保留、必须避免、必须新增或修正；明确术语必须转成动作后果 |  |
| 5 | beat sheet / outline | pass | Step 4 洗稿边界包 | `PRD_v11_豪门商战版_写作前工作稿.md` Step 5 | B1-B10 均改变局势/关系/信息/情绪；B3/B4 提前埋 Marcus 第一笔钱；B10 不和解 |  |
| 6 | 新壳场面迁移卡 | pass | outline + 源本高价值节点 | `PRD_v11_豪门商战版_写作前工作稿.md` Step 6 | M1-M6 均写出源本节点、禁用外形、动作链、权力变化或卡点；M5 专门定义 E9 托管箱火葬场 |  |
| 7 | Episode function map | pass | outline + 迁移卡 | `PRD_v11_豪门商战版_写作前工作稿.md` Step 7 | E1-E10 均有 Opening Hook、Max Spike、End Button、Do Not Consume、Pressure Progression、Carry-through From Source |  |
| 8 | Scene packet | pass | episode map；V9/V10 正式锚点；V10 challenge 对 Step 8 的 revise | `PRD_v11_豪门商战版_写作前工作稿.md` Step 8 | E1-E6 复用列 V9/V10 锚点；E7/E8/E10 Scene 2 明确 Inherited From；E9 有完整 Scene 1-3、角色压力、短剧节拍和 Script Blocks | 没有用正文倒推 Step 8 pass |
| 9 | Screenplay draft | pass | `PRD_v11_豪门商战版_写作前工作稿.md` Step 8 scene packet | `PRD_v11_豪门商战版_首批1-10集.md` | 正文为 Episode + INT. 场景格式，未泄露 scene packet 内部字段；E7/E8/E9/E10 高压节点均有动作、身体、空间、权力变化和可拍卡点 | 正文锚点：E7 红键/压腕；E8 root-key碎杯/CEO key/旧语音；E9 托管箱/胎心/空发布会大厅；E10 直播认罪/手铐/Arden bridge |
| 10 | Rewrite report | pass | `PRD_v11_豪门商战版_首批1-10集.md`；V10 challenge 汇总 | `PRD_v11_豪门商战版_rewrite_report_dialogue_polish.md` Rewrite Report | 定位 execution / scene packet / scene / adaptation / structure / dialogue 层问题，并列优先动作；不是泛泛润色 |  |
| 11 | Dialogue polish | pass | V11 正文 + rewrite report | `PRD_v11_豪门商战版_rewrite_report_dialogue_polish.md` Dialogue Polish；修订已折入 V11 正文 | 列 Target Lines、Subtext Benchmarks、Voice Adjustments、Rhythm Notes、Revised/Cut Lines；判断哪些解释句要动作化 |  |
| 12 | 作者 quality gate | pass | V11 正文 + 写作前工作稿 + rewrite/dialogue polish | `PRD_v11_豪门商战版_作者质量门.md` | 按 contract_fit、mechanics_pressure、continuity、expression、adaptation、carry-through 检查；作者侧结论为 `pass for 6-agent challenge` | 不等于 reviewer pass |
| 13 | Story memory checkpoint | pass | V11 当前稿 | `PRD_v11_豪门商战版_story_memory_checkpoint.md` | 记录关系、信息差、伏笔/证据、角色状态、未兑现承诺、禁止下批提前消费和第 11 集安全入口 |  |
| 14 | 独立 reviewer | blocked | 需要主控另开干净 reviewer / challenge | 无 | 本 agent 不执行，不能判 pass | 按任务指令，本轮结束不声称 complete |
| 15 | 版本对比 | pass | V11 当前稿 + V3 + V10 | `PRD_v11_vs_v3_v10_版本对比.md` | 按 spec Step 15 比较源本有效性、同构风险、短剧场面、动作链、台词、钩子、关系、continuity 和读感；结论：V11 不低于 V3，作者侧优于 V10，可进 6-agent challenge | V10 是 protocol-fail 内容参考，不是合格执行样本 |

## 未完成步骤

- Step 14 blocked：必须由主控后续另开干净 reviewer / challenge。

## 不允许交付原因

- `workflow_spec_v2.md` Step 14 要求独立 reviewer quality gate + rewrite report。
- 本 agent 身份是 V11 主创 agent，不能代替干净 reviewer。
- 因此 V11 当前是主创侧 partial run：Step 0-13、15 pass；Step 14 blocked。
- 不能声称 workflow complete，也不能直接替代 6-agent challenge。
