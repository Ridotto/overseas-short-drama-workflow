# workflow run manifest

任务：按 PRD v4 + workflow_spec_v2 + workflow_execution_protocol_v1 重跑豪门商战版首批 1-10 集样本验证
版本：V7
日期：2026-06-30
执行 agent：主创 agent（本轮不冒充独立 reviewer）
使用的产品定义：`v2-restart/PRD_v4.md`
使用的 workflow spec：`v2-restart/workflow_spec_v2.md`
输入源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`（重点阅读 1-10 集，参考全剧结构）
目标新壳：海外豪门商战 / 家族企业权力斗争
输出范围：首批 1-10 集

## 总状态

- complete
- 本轮主创侧完成 0-13 和 15；Step 14 已由干净独立 reviewer 单独执行并输出报告。Reviewer 结论：pass。

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | `PRD_v4.md`; `workflow_spec_v2.md`; `三星样本小跑_黑手党少主.md`; `导演反馈合并判断_豪门商战1-10.md` | `PRD_v7_豪门商战版_写作前工作稿.md` 第 0 节 | 足够开工 | 沿用项目默认样本设定：豪门商战、海外短剧、1-10 集、中度偏重。 |
| 1 | 读源本 | pass | 源本 txt 1-10 集，行 57-317；参考全剧集数目录 | `PRD_v7_豪门商战版_写作前工作稿.md` 第 1 节 | 完整覆盖本轮 1-10 集范围 | 重点读取源本 1-10 集，参考旧样本分析与导演反馈。 |
| 2 | 源本拆文包 | pass | 源本 txt; PRD v4; workflow spec v2 | `PRD_v7_豪门商战版_写作前工作稿.md` 第 1 节 | 含钩子、爽点、关系/权力、信息差、禁止外形 | 源本事件载体和高辨识外形已列出。 |
| 3 | 二次需求确认 | pass | 源本拆文包 + 已确认豪门商战新壳 + 导演反馈 | `PRD_v7_豪门商战版_写作前工作稿.md` 第 2 节 | 明确改写力度、禁区、新壳承载 | 未新增用户问题；按项目当前默认和导演反馈执行。 |
| 4 | 洗稿边界包 | pass | 源本拆文包 + 导演反馈 | `PRD_v7_豪门商战版_写作前工作稿.md` 第 3 节 | 区分保留体验与替换外形 | 明确 V7 新事件载体总线。 |
| 5 | beat sheet / outline | pass | 洗稿边界包 | `PRD_v7_豪门商战版_写作前工作稿.md` 第 4 节 | 每个 beat 有变化和不可提前消费内容 | 1-10 集阶段闭环成立。 |
| 6 | 新壳场面迁移卡 | pass | outline + 源本高价值节点 + V5/V6 失败点 | `PRD_v7_豪门商战版_写作前工作稿.md` 第 5 节 | 从证据变成场面动作链 | 覆盖逼离婚、Dock 9、回归、第 7-8 集、第 9-10 集。 |
| 7 | Episode function map | pass | outline + 迁移卡 | `PRD_v7_豪门商战版_写作前工作稿.md` 第 7 节 | 每集有 opening / max spike / end button / do not consume | 10 集均有明确留存功能。 |
| 8 | Scene packet | pass | Episode function map | `PRD_v7_豪门商战版_写作前工作稿.md` 第 8 节 | 可直接喂给 writer；含动作链/权力变化/人物状态 | 10 集 scene packet 已完成。 |
| 9 | Screenplay draft | pass | Scene packet | `PRD_v7_豪门商战版_首批1-10集.md` | 导演可读；无内部字段泄漏 | 已检查正文未出现 Purpose / Action Chain / Source Function Ref 等内部字段。 |
| 10 | Rewrite report | pass | Screenplay draft | `PRD_v7_豪门商战版_rewrite_report_dialogue_polish.md` | 定位失败层，不只泛泛润色 | concept/adaptation/structure/scene/dialogue/continuity 已分层判断。 |
| 11 | Dialogue polish | pass | Screenplay draft + rewrite report | `PRD_v7_豪门商战版_rewrite_report_dialogue_polish.md` | 检查冷静台词、水词、动作替代台词 | 当前修订稿可进入作者 quality gate。 |
| 12 | 作者 quality gate | pass | V7 修订稿 + 写作前工作稿 | `PRD_v7_豪门商战版_作者质量门.md` | 按 lenses 给出 pass/revise/block 判断 | 作者结论：pass for independent reviewer。 |
| 13 | Story memory checkpoint | pass | V7 当前稿 | `PRD_v7_豪门商战版_story_memory_checkpoint.md` | 记录关系、信息差、伏笔、禁提前消费 | 可支撑后续 11-37 集。 |
| 14 | 独立 reviewer | pass | `PRD_v7_豪门商战版_reviewer输入包.md`; `PRD_v4.md`; `workflow_spec_v2.md`; 源本 txt; `PRD_v7_豪门商战版_写作前工作稿.md`; `PRD_v7_豪门商战版_首批1-10集.md` | `PRD_v7_豪门商战版_独立reviewer审稿.md` | reviewer 干净；第一轮未读作者自检、版本对比、作者解释；结论 pass | 独立 reviewer 指出术语密度和第 9 集遗物感为 observable-risk，不构成硬失败。 |
| 15 | 版本对比 | pass | V7 当前稿 + V3 + V6 + 导演反馈 | `PRD_v7_vs_v3_v6_版本对比.md` | 已判断不低于 V3，并优于 V6 的同构风险 | 建议进入独立 reviewer，不建议跳过 reviewer 给导演。 |

## 未完成步骤

无。

## 不允许交付原因

无。Step 14 独立 reviewer 已完成，报告路径：`PRD_v7_豪门商战版_独立reviewer审稿.md`。
