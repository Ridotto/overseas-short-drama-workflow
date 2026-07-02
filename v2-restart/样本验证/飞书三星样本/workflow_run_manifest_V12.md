# workflow_run_manifest_V12

任务：飞书三星样本豪门商战版首批 1-10 集 V12 局部修稿  
版本：V12  
日期：2026-06-30  
执行 agent：V12 干净主创 agent  
Goal round：第 4 轮  
使用的产品定义：`v2-restart/PRD_v4.md`  
使用的 workflow spec：`v2-restart/workflow_spec_v2.md`  
使用的执行协议：`v2-restart/workflow_execution_protocol_v1.md`  
使用的 goal 控制：`v2-restart/goal_run_control_2026-06-30.md`  
输入源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`  
目标新壳：海外豪门商战 / 家族企业权力斗争  
输出范围：首批 1-10 集，局部修第 7-10 集 + 证据口径收紧

## 总状态

- partial
- 本 manifest 已先于其他 V12 正式产物创建。
- V10 定位：protocol-fail，只能作为内容参考，不能作为正式执行证据。
- V11 定位：正式执行成立，但质量结论为 revise；可作为局部问题定位和修订参考，不能作为 pass 基准。
- V12 定位：goal 第 4 轮，必须持续更新本 manifest，不事后倒补。

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | `当前样本测试夹具.md`；用户本轮 V12 指令；`goal_run_control_2026-06-30.md` | 本 manifest | 足够开工：任务类型、源本、新壳、目标市场、集数、本轮范围、禁区均明确。 | V12 只做局部修稿，不全量重写；V10 为内容参考，V11 为上一轮正式 revise。 |
| 1 | 读源本 | pass | `v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt` 第 1-10 集，行 57-317 | 本 manifest Step 1 记录 | 完整覆盖本轮首批范围；源本 S1-E1 到 S1-E10 的追看链、强节点和禁止复用外形均已读取。 | 关键源本锚点：S1-E2 车祸求救被拒；S1-E7 当众拆 Lily 但 Dante 仍护错；S1-E8 Lily 反咬男主同罪；S1-E9 旧物火葬场；S1-E10 跪求不原谅。 |
| 2 | 源本拆文包 | pass | 源本第 1-10 集；V11 工作稿源本高价值节点；V11 challenge 共同 revise 点 | `PRD_v12_豪门商战版_写作前工作稿.md` `Step 1-2. 源本拆文包`，行 30 起 | 满足 spec Step 2：列出故事核、核心期待、高价值节点、强度来源、禁止复用外形和下游写作抓手。 | 关键锚点：S1-E7 男主护错；S1-E8 男主同罪；S1-E9 火葬场；S1-E10 不原谅。 |
| 3 | 二次需求确认 | pass | 用户本轮 V12 指令；`goal_run_control_2026-06-30.md`；`PRD_v11_6agent_challenge汇总.md` | `PRD_v12_豪门商战版_写作前工作稿.md` `Step 3. 二次需求确认`，行 66 起 | 改写力度、禁区、修稿范围、新壳承载均明确。 | 明确不全量重写；E7/E8/E10 局部修，E9 保留，E1-E6 为复用验证。 |
| 4 | 洗稿边界包 | pass | Step 2 拆文包；V11 共同 revise 点 | `PRD_v12_豪门商战版_写作前工作稿.md` `Step 4. 洗稿边界包`，行 79 起 | 区分保留体验、必须替换外形和 V12 局部新增承载。 | 新增承载聚焦直播污名/倒计时、Adrian 口读手确认、Marcus 第二页关系刺。 |
| 5 | beat sheet / outline | pass | Step 4 边界包 | `PRD_v12_豪门商战版_写作前工作稿.md` `Step 5. 新本 beat sheet / outline`，行 103 起 | 每个 beat 均写出源本体验功能、局势/情绪变化和不可提前消费内容。 | B7/B8/B10 分别对应本轮三处主修节点。 |
| 6 | 新壳场面迁移卡 | pass | Step 5 beat sheet；源本节点 S1-E7/S1-E8/S1-E10 | `PRD_v12_豪门商战版_写作前工作稿.md` `Step 6. 新壳场面迁移卡`，行 126 起 | 满足 spec Step 6：高风险节点有场面目的、动作链、权力/关系变化、可见后果、卡点和同构扣除。 | M1 明确 E1-E6 只是复用验证；M2/M3/M5 是 V12 厚修迁移卡。 |
| 7 | Episode function map | pass | Step 5 outline；Step 6 迁移卡 | `PRD_v12_豪门商战版_写作前工作稿.md` `Step 7. Episode function map`，行 206 起 | 每集有 Max Spike、End Button、Do Not Consume、Pressure Progression、Carry-through From Source。 | E7/E8/E10 有明确压力推进；E9 保留强火葬场。 |
| 8 | Scene packet | pass | Episode function map；迁移卡 M1-M5 | `PRD_v12_豪门商战版_写作前工作稿.md` `Step 8. Scene packet`，行 221 起 | 满足 spec Step 8：E7/E8/E10 高压场有 Scene Objective、Action Chain、Power Shift、Character Pressure State、Short-drama Beat Chain 和 Script Blocks。 | E1-E6 明确为“复用验证通过”；E7 亲口命令+红键；E8 口读+确认；E10 Marcus 第二页单钩。 |
| 9 | Screenplay draft | pass | `PRD_v12_豪门商战版_写作前工作稿.md` Step 8 Scene packet | `PRD_v12_豪门商战版_首批1-10集.md` | 满足 spec Step 9：正文未混入内部字段；高压场有动作、身体、空间、当众后果和可拍集尾。 | 锚点：E7 行 767 起，`Hold her at the rail.` 行 947；E8 行 1009 起，`No medical exception.` 行 1124、确认键行 1152、SH-0827 行 1170；E10 行 1386 起，`听见了` 行 1544、`但我没说原谅` 行 1557、`第二页` 行 1608。 |
| 10 | Rewrite report | pass | `PRD_v12_豪门商战版_首批1-10集.md`；V11 challenge 共同 revise 点 | `PRD_v12_豪门商战版_rewrite_report_dialogue_polish.md` `Rewrite Report`，行 7 起 | 满足 spec Step 10：定位 failure layer 为 scene / adaptation / structure / continuity / expression，并列 must-restructure 行动。 | 关键修订：E7 直播污名+倒计时；E8 Adrian 口读手确认；E10 删除 Chloe/trusteeship 强钩，只留 Marcus 第二页。 |
| 11 | Dialogue polish | pass | V12 正文 + rewrite report | `PRD_v12_豪门商战版_rewrite_report_dialogue_polish.md` `Dialogue Polish`，行 38 起 | 满足 spec Step 11：按目标台词、潜台词、角色声音、节奏、修订/删除台词审计；正文已按 polish 标准写成。 | 锚点：`Hold her at the rail.` 行 45；`No medical exception` 行 48；`第二页，你藏了五年` 行 50；Beat survival check 行 81 起。 |
| 12 | 作者 quality gate | pass | V12 正文；V12 工作稿；rewrite/dialogue polish | `PRD_v12_豪门商战版_作者质量门.md` | 满足 spec Step 12：覆盖 contract_fit、mechanics_pressure、continuity、expression、adaptation、carry-through；列 hard fails、weaknesses、correction ladder、recheck plan。 | 作者结论为 `pass for 6-agent challenge`，不等于独立 reviewer pass。Carry-through evidence 行 28 起；hard fails 行 38 起；作者结论行 76 起。 |
| 13 | Story memory checkpoint | pass | V12 正文；V12 作者质量门 | `PRD_v12_豪门商战版_story_memory_checkpoint.md` | 满足 spec Step 13：记录关系、信息差、伏笔/证据、角色状态、未兑现承诺、禁止下批提前消费和下一批入口。 | 关键锚点：Serena/Adrian 不原谅行 11；Serena/Marcus 追问行 12；Arden bridge 第二页行 33；下一批入口行 61 起。 |
| 14 | 独立 reviewer | pending | 未执行 | 未产出 | 未判断 | 本轮主创侧结束后应由主控另开干净 6-agent challenge；reviewer 第一轮不应读作者质量门。 |
| 15 | 版本对比 | pass | `PRD_v3_豪门商战版_首批1-10集.md`；`PRD_v11_豪门商战版_首批1-10集.md`；V10 内容参考口径 | `PRD_v12_vs_v3_v11_版本对比.md` | 满足 spec Step 15：比较 V12 vs V3、V12 vs V11，判断不低于 V3、作者侧优于 V11，并说明不直接进入用户 review。 | V12 明确进步行 78 起；可能退步行 93 起；是否允许进入 review 行 108 起。 |

## 未完成步骤

Step 14 尚未完成。

## 不允许交付原因

当前完成 Step 0-13、15；Step 14 独立 reviewer / 6-agent challenge 尚未执行，不能声称 workflow complete。
