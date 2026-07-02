# workflow run manifest V19 v10workflow

任务：飞书三星样本首批 1-10 集候选验证  
版本：V19  
日期：2026-07-01  
执行 agent：Codex 主控/主创合一  
使用的产品定义：`v2-restart/PRD_v4.md`  
使用的 workflow spec：`v2-restart/workflow_spec_v10_V3V5完整回收候选版.md`  
执行协议：`v2-restart/workflow_execution_protocol_v1.md`  
输入源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`  
目标新壳：海外豪门商战 / 家族企业权力斗争  
输出范围：首批 1-10 集  
改写力度：中度偏重  

## 总状态

- 当前状态：aborted / invalid-test
- 说明：本轮 manifest-first 已建立，但主控在执行过程中向自身注入了过多具体创作判断，已无法作为“workflow 本身是否有效”的干净测试。V19 仅保留为中断/污染样本，不进入有效验证对比。

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | `当前样本测试夹具.md`；用户已确认豪门商战、集数不动 | 本 manifest 任务区 | 足够开工 | 台词默认英文，动作/分析中文；用途为样本验证/导演审稿前候选 |
| 1 | 读源本 | aborted | 源本 txt | 中断 | 无效 | 主控污染测试，停止 |
| 2 | 源本拆文包 | aborted | 源本 | `PRD_v19_v10workflow_写作前工作稿.md` | 无效 | 该文件受主控额外创作判断影响，不作为 workflow 有效产物 |
| 3 | 二次需求确认 | pending | 拆文包 + 测试夹具 | 待补 | 待补 |  |
| 4 | 洗稿边界包 | pending | 拆文包 | 待补 | 待补 |  |
| 5 | beat sheet / outline | pending | 边界包 | 待补 | 待补 |  |
| 6 | 新壳场面迁移卡 | pending | outline + 源本节点 | 待补 | 待补 |  |
| 7 | Episode function map | pending | outline | 待补 | 待补 |  |
| 8 | Scene packet | pending | episode map | 待补 | 待补 |  |
| 9 | Screenplay draft | pending | scene packet | 待补 | 待补 |  |
| 10 | Rewrite report | pending | 正文 | 待补 | 待补 |  |
| 11 | Dialogue polish | pending | 正文 + rewrite report | 待补 | 待补 |  |
| 12 | 作者 quality gate | pending | 修订稿 | 待补 | 待补 |  |
| 13 | Story memory checkpoint | pending | 当前稿 | 待补 | 待补 |  |
| 14 | 独立 reviewer | pending | reviewer 输入包 | 待补 | 待补 | 本轮未开干净 reviewer 前不能 complete |
| 15 | 版本对比 | pending | V3 / V5 / V18 / V19 | 待补 | 待补 |  |

## 未完成步骤

Step 1-15 均不再继续执行。下一轮应另开干净 agent，以新版本号重跑。

## 不允许交付原因

V19 不是有效 workflow 测试。原因：主控给了过多具体创作指导，无法判断产物来自 workflow 还是来自主控提示。下一轮使用 V20 干净 agent 重跑。
