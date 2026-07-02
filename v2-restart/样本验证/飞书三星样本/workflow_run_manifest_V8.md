# workflow run manifest

任务：按当前入口文件完整跑一轮 V8 workflow，生成豪门商战版首批 1-10 集
版本：V8
日期：2026-06-30
执行 agent：干净主创 agent
使用的产品定义：v2-restart/PRD_v4.md
使用的 workflow spec：v2-restart/workflow_spec_v2.md
使用的执行验收协议：v2-restart/workflow_execution_protocol_v1.md
输入源本：v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt
目标新壳：海外豪门商战 / 家族企业权力斗争
输出范围：首批 1-10 集

## 总状态

- complete
- 本轮 V8 workflow 已执行完 0-15 步。独立 reviewer 第一轮 `revise`，主创按意见返修第 2、7、8 集后，reviewer 第二轮复核结论为 `pass`。当前允许进入主控汇总 / 导演确认；残余风险为第 7-8 集同一 boardroom 空间连续使用，非阻断项。

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | AGENTS.md；v2-restart/当前工作入口.md；v2-restart/workflow_spec_v2.md 第 2 节当前样本默认 | 本 manifest | 足够开工：任务类型、源本、新壳、市场、集数、本轮范围、禁区已明确 | 默认需求来自当前 spec 与任务指令 |
| 1 | 读源本 | pass | 源本 txt 1-1467 行 | PRD_v8_豪门商战版_写作前工作稿.md 第 1 节 | 已完整覆盖源本全本；本轮重点覆盖 1-10 集并记录后续禁止提前消费 | 已读全本，避免后续状态漂移 |
| 2 | 源本拆文包 | pass | 源本 txt 1-1467 行 | PRD_v8_豪门商战版_写作前工作稿.md 第 1 节 | 含钩子、爽点、关系/权力、信息差、禁止外形 | 拆的是功能与事件载体，不复述剧情 |
| 3 | 二次需求确认 | pass | 拆文包 + 当前样本默认判断 + 已知导演反馈 | PRD_v8_豪门商战版_写作前工作稿.md 第 2 节 | 明确改写力度、禁区、新壳承载 | 未新增用户问题；按当前样本默认继续 |
| 4 | 洗稿边界包 | pass | 拆文包 | PRD_v8_豪门商战版_写作前工作稿.md 第 3 节 | 区分保留体验和替换外形 | 明确车祸、亲子鉴定、保险箱、雨夜跪地等外形扣除 |
| 5 | beat sheet / outline | pass | 边界包 | PRD_v8_豪门商战版_写作前工作稿.md 第 4 节 | 每个 beat 有变化和不可提前消费 | 建立资本犯罪/公开背锅/托管箱火葬场新载体 |
| 6 | 新壳场面迁移卡 | pass | outline + 源本高价值节点 | PRD_v8_豪门商战版_写作前工作稿.md 第 5 节 | 已从证据链转为场面动作链 | 覆盖逼离婚、错误签字、回归、信托、同罪、托管箱、认罪 |
| 7 | Episode function map | pass | outline + 迁移卡 | PRD_v8_豪门商战版_写作前工作稿.md 第 6 节 | 10 集均有 opening / max spike / end button / do not consume | 连续场面形态做了区分 |
| 8 | Scene packet | pass | episode map | PRD_v8_豪门商战版_写作前工作稿.md 第 7-8 节 | 符合 scene_draft 合同；含场景目标、动作、身体/空间压力、权力变化 | 关键对白绑定 Action / Performance / Body / Space |
| 9 | Screenplay draft | pass | PRD_v8_豪门商战版_写作前工作稿.md 第 7-8 节 | PRD_v8_豪门商战版_首批1-10集.md | 符合 screenplay_draft 合同：导演可读、无内部字段泄漏、高压场景有动作/身体/空间/屏幕反馈承载 | 已用检索确认未出现 Purpose / Action / Performance / Source Function Ref / End Button / Do Not Consume 等内部字段 |
| 10 | Rewrite report | pass | PRD_v8_豪门商战版_首批1-10集.md | PRD_v8_豪门商战版_rewrite_report_dialogue_polish.md 第 1 节 | 已定位 concept / structure / scene / dialogue / continuity / adaptation 层级，不只泛泛润色 | 结论：无 must-restructure |
| 11 | Dialogue polish | pass | PRD_v8_豪门商战版_首批1-10集.md + rewrite report | PRD_v8_豪门商战版_rewrite_report_dialogue_polish.md 第 2 节 | 按 dialogue_polish 合同处理 Target Lines / Subtext / Voice / Rhythm / Revised Lines；修订已折入正文 | 已处理解释腔、自白依赖、过激测试等风险 |
| 12 | 作者 quality gate | pass | PRD_v8_豪门商战版_首批1-10集.md + PRD_v8_豪门商战版_写作前工作稿.md | PRD_v8_豪门商战版_作者质量门.md | 先查 contract_fit，再查 adaptation_fit；作者侧结论 pass for independent reviewer | 不等于独立 reviewer 通过 |
| 13 | Story memory checkpoint | pass | PRD_v8_豪门商战版_首批1-10集.md | PRD_v8_豪门商战版_story_memory_checkpoint.md | 已记录关系/信息差/伏笔/禁提前消费/下一批安全入口 | 支撑后续 11-37 集 |
| 14 | 独立 reviewer | pass | PRD_v8_豪门商战版_reviewer输入包.md；PRD_v8_豪门商战版_首批1-10集.md；PRD_v4.md；workflow_spec_v2.md；源本 txt | PRD_v8_豪门商战版_独立reviewer审稿.md | 独立 reviewer 第一轮结论 revise；主创返修第 2、7、8 集后，第二轮复核 pass | reviewer 第一轮未读作者 quality gate、rewrite report、版本对比、旧版正文、导演旧反馈；第二轮只复核修订段和自己的上一轮意见 |
| 15 | 版本对比 | pass | PRD_v8 当前稿 + PRD_v3_豪门商战版_首批1-10集.md + PRD_v7_豪门商战版_首批1-10集.md | PRD_v8_豪门商战版_版本对比.md | 已判断 V8 不低于 V3，且在同构扣除上优于 V7；建议进入独立 reviewer，不直接送导演 | V7 仅作对比/失败证据 |

## 未完成步骤

无。

## 不允许交付原因

无。当前可声称本轮 workflow complete；但导演是否接受仍需导演确认。
