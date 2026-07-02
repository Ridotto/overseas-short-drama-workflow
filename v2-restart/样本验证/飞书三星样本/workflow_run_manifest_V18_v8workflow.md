# workflow run manifest

任务：飞书三星样本按 v8 workflow 重跑 V18
版本：V18 / v8workflow
日期：2026-07-01
执行 agent：v18_v8_clean_creator
使用产品定义：`v2-restart/PRD_v4.md`
使用 workflow spec：`v2-restart/workflow_spec_v8_创作抓手合并候选版.md`
源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`
新壳：海外豪门商战 / 家族企业权力斗争
目标市场：海外短剧
集数：不变
改写力度：中度偏重
输出范围：首批 1-10 集
正文默认：中文动作/场景描述 + 英文对白

## 总状态

- execution_status: complete
- delivery_status: revise

## 步骤证据表

| Step | 名称 | 状态 | 输出文件 | Gate 判断 | 备注 |
|---|---|---|---|---|---|
| 0 | 最小需求卡 | pass | `PRD_v18_v8workflow_最小需求卡.md` | 足够开工：源本、新壳、市场、集数、改写力度、输出范围、语言、用途、禁区均已锁定 | 锚点：需求卡第 1-6 节 |
| 1 | 主创读本笔记 | pass | `PRD_v18_v8workflow_主创读本笔记.md` | 已读出首批追看机制，不只是剧情摘要 | 锚点：读本笔记第 2-5 节、第 10 节 |
| 2 | 二次需求确认 | pass | `PRD_v18_v8workflow_二次需求确认.md` | 已明确新壳可承载、力度、变量边界、外形禁区 | 锚点：二次确认第 1-6 节 |
| 3 | 洗稿方案 | pass | `PRD_v18_v8workflow_洗稿方案.md` | 已说明怎么洗，新壳故事发动机成立 | 锚点：洗稿方案第 1-9 节 |
| 4 | 关键场面迁移卡 | pass | `PRD_v18_v8workflow_关键场面迁移卡.md` | 高压节点有动作链、权力变化、卡点和禁止提前消费，可直接支撑正文 | 锚点：KC1-KC8 |
| 5 | 首批写作简报 | pass | `PRD_v18_v8workflow_首批写作简报.md` | 已把迁移卡分配进 1-10 集写作 | 锚点：EPISODE 1-10 |
| 6 | 首批正文 | pass | `PRD_v18_v8workflow_豪门商战版_首批1-10集.md` | 是剧本文字，不是说明书；高压场已消化迁移卡 | 锚点：EP1 门禁失效与调度电话；EP2 切割工具撤走；EP4 胸针摘除与保镖换边；EP7-E8 股东会证据触发程序后果；EP10 直播认罪卡点 |
| 7 | 作者问题清单 | pass | `PRD_v18_v8workflow_作者问题清单.md` | 已诚实指出洗飞、同构、短剧降级、旧版/源本更强处和需要 reviewer 特别看的位置 | 锚点：作者问题清单第 1-6 节 |
| 8 | 干净 reviewer | pass | `PRD_v18_v8workflow_reviewer.md` | 两轮审稿已完成，reviewer 未读作者问题清单；结论 revise，不是 block | 锚点：reviewer 读取记录、第一轮、第二轮、失败层、结论 |
| 9 | 主控判定与版本对比 | pass | `PRD_v18_v8workflow_vs_v3_v5_v17_整体对比.md`；`PRD_v18_v8workflow_主控判定.md` | 已整体对比 V3 / V5 / V17 / V18，并给出主控结论 | delivery_status 为 revise，不建议给导演 |

## 未完成步骤

无。Step 0-9 均已完成。

## 不允许交付原因

本轮可以声称 v8 workflow 已完整跑完，但不能声称文本质量通过。Reviewer 与主控均判 `revise`，V18 不建议给导演。
