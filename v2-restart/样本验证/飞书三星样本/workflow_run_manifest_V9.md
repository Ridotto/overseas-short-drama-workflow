# workflow run manifest

任务：飞书三星样本豪门商战版 V9 首批 1-10 集真实 workflow 验证  
版本：V9  
日期：2026-06-30  
执行 agent：干净主创测试 agent  
使用的产品定义：`v2-restart/PRD_v4.md`  
使用的 workflow spec：`v2-restart/workflow_spec_v2.md`  
使用的执行协议：`v2-restart/workflow_execution_protocol_v1.md`  
输入源本：`[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`  
目标新壳：海外豪门商战 / 家族企业权力斗争  
目标市场：海外短剧  
输出范围：首批 1-10 集  
对比基线：`PRD_v3_豪门商战版_首批1-10集.md`；上一轮交付版 `PRD_v8_豪门商战版_首批1-10集.md`

## 总状态

- partial
- Step 0-13、15 有产物和证据，作者侧可进入独立 reviewer。
- Step 14 独立 reviewer 未执行。本 agent 是主创测试 agent，未单开 reviewer；因此本轮不能声称 workflow complete。

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | `当前样本测试夹具.md`：源本、新壳、目标市场、集数、本轮输出、改写力度、V3/V8 基线 | 本 manifest 任务头；`PRD_v9_豪门商战版_写作前工作稿.md` Step 0 | 足够开工：豪门商战新壳、首批 1-10 集、V3/V8 对比边界均明确 |  |
| 1 | 读源本 | pass | 源本 txt 全文 1-1467 行；首批 1-10 集重点复读 57-317 行 | `PRD_v9_豪门商战版_写作前工作稿.md` Step 1-2 | 覆盖本轮 1-10 集，并读到后续全剧走向以避免状态误判 |  |
| 2 | 源本拆文包 | pass | 源本 S1-E1 到 S1-E10；全剧梗概和后续 11-37 集 | `PRD_v9_豪门商战版_写作前工作稿.md` Step 1-2：源本拆文包 | 按 spec Step 2：列出一句话故事核、首批分集功能、高价值节点、钩子、爽点、关系、信息差、禁止复用外形 | 关键节点锚点：S1-E1 到 S1-E10 |
| 3 | 二次需求确认 | pass | 拆文包 + `当前样本测试夹具.md` 默认判断 | `PRD_v9_豪门商战版_写作前工作稿.md` Step 3 | 明确改写力度、新壳承载、关键留存节点和禁区；无额外用户待拍板项 | 当前样本验证使用夹具默认判断 |
| 4 | 洗稿边界包 | pass | Step 2 源本拆文包 | `PRD_v9_豪门商战版_写作前工作稿.md` Step 4 | 区分保留体验与替换外形：保留失子/回归/拆女配/火葬场，扣除黑帮、车祸、假孕、亲子、保险箱、枪口 |  |
| 5 | beat sheet / outline | pass | Step 4 洗稿边界包 | `PRD_v9_豪门商战版_写作前工作稿.md` Step 5 | 每个 beat 改变局势、关系、信息或情绪；列出不可提前消费内容 | Beat B1-B10 |
| 6 | 新壳场面迁移卡 | pass | outline + 源本节点 S1-E1/S1-E2/S1-E7/S1-E8/S1-E9/S1-E10 | `PRD_v9_豪门商战版_写作前工作稿.md` Step 6 | 高风险节点均有新冲突动作链、权力变化、关系变化、卡点和禁止提前消费 | 迁移卡 M1-M6 |
| 7 | Episode function map | pass | outline + 迁移卡 | `PRD_v9_豪门商战版_写作前工作稿.md` Step 7 | 每集有 Opening Hook、Max Spike、End Button、Do Not Consume、Pressure Progression、Carry-through From Source | 高压集锚点：E2、E7、E8、E9、E10 |
| 8 | Scene packet | pass | episode function map | `PRD_v9_豪门商战版_写作前工作稿.md` Step 8 | 符合 `scene_card / scene_draft` 合同：每集有动作链、权力变化、出口状态；高压场有短剧节拍和正文可转化动作 | Scene packet 覆盖 Episode 1-10 |
| 9 | Screenplay draft | pass | scene packet | `PRD_v9_豪门商战版_首批1-10集.md` | 按 `screenplay_draft / scene_draft` 合同：正文为剧本格式，无内部字段；关键节点有动作、身体、空间和屏幕反馈 | 正文锚点：Episode 2 `DENY`；Episode 7 红键；Episode 8 CEO key；Episode 9 托管箱；Episode 10 直播认罪 |
| 10 | Rewrite report | pass | V9 正文 + V3/V8 旧问题 | `PRD_v9_豪门商战版_rewrite_report_dialogue_polish.md` Rewrite Report | 定位 failure layer，不只泛泛润色；明确第 2、7、8、9、10 集的 scene/adaptation 风险 |  |
| 11 | Dialogue polish | pass | V9 正文 + rewrite report | `PRD_v9_豪门商战版_rewrite_report_dialogue_polish.md` Dialogue Polish；修订已折入 `PRD_v9_豪门商战版_首批1-10集.md` | 按 `dialogue_polish` 合同列目标台词、表面意思、潜台词、角色声音、节奏处理；不是只改短句 |  |
| 12 | 作者 quality gate | pass | 修订稿 + 写作前工作稿 + rewrite/dialogue polish | `PRD_v9_豪门商战版_作者质量门.md` | 按 `quality_gate_report`：contract_fit、mechanics_pressure、continuity、expression、adaptation、carry_through 均检查；作者侧结论为 `pass for independent reviewer` | 不等于 reviewer pass |
| 13 | Story memory checkpoint | pass | V9 当前稿 | `PRD_v9_豪门商战版_story_memory_checkpoint.md` | 记录关系、信息差、伏笔/证据、角色状态、未兑现承诺、禁止下批提前消费、下一批安全入口 |  |
| 14 | 独立 reviewer | blocked | 需要独立 reviewer 输入包和干净 reviewer | 无 | 未执行独立 reviewer，因此不能判 pass；本轮不能 complete | 主控需另开干净 reviewer，且 reviewer 第一轮不读作者质量门/版本对比 |
| 15 | 版本对比 | pass | V9 当前稿 + V3 基线 + V8 上一版 | `PRD_v9_vs_v3_v8_版本对比.md` | 按 spec Step 15：比较源本有效性、同构风险、短剧场面、动作链、台词、钩子、关系、continuity 和读感；结论不建议直接给导演，只允许进 reviewer |  |

## 未完成步骤

- Step 14 独立 reviewer：blocked，未单开干净 reviewer。

## 不允许交付原因

- `workflow_spec_v2.md` Step 14 要求独立 reviewer quality gate + rewrite report。
- 本次 agent 身份是主创测试 agent，已完成主创侧写作、返修、自检、状态追踪和版本对比，但没有独立 reviewer 产物。
- 因此本轮状态只能是 partial，不能声称完整 workflow complete。

## 产物路径

- `v2-restart/样本验证/飞书三星样本/PRD_v9_豪门商战版_写作前工作稿.md`
- `v2-restart/样本验证/飞书三星样本/PRD_v9_豪门商战版_首批1-10集.md`
- `v2-restart/样本验证/飞书三星样本/PRD_v9_豪门商战版_rewrite_report_dialogue_polish.md`
- `v2-restart/样本验证/飞书三星样本/PRD_v9_豪门商战版_作者质量门.md`
- `v2-restart/样本验证/飞书三星样本/PRD_v9_豪门商战版_story_memory_checkpoint.md`
- `v2-restart/样本验证/飞书三星样本/PRD_v9_vs_v3_v8_版本对比.md`
