# workflow run manifest

任务：按 `workflow_spec_v6_能力回收修正版草案.md` 受控验证飞书三星样本
版本：V16_v6workflow
日期：2026-07-01
执行 agent：Codex 主控 / 主创；V16 clean creator 2 接手补齐主创侧产物
使用的产品定义：`v2-restart/PRD_v4.md`
使用的 workflow spec：`v2-restart/workflow_spec_v6_能力回收修正版草案.md`
执行验收协议：`v2-restart/workflow_execution_protocol_v1.md`
输入源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`
目标新壳：海外豪门商战
输出范围：首批 1-10 集
输出语言 / 审稿语言：正文默认英文对白；分析、审稿、对比使用中文

## 总状态

- execution_complete / delivery_revise
- V16 clean creator 2 已完成主创侧产物；V16 clean reviewer 已完成 Step 17 两轮 reviewer。
- Reviewer 结论：`revise`，不是 `block`；失败层为 `screenplay_pressure_execution / local_scene_trigger`。
- Root 主控已完成 Step 18 最终交付判断。
- 本轮执行链路已闭合，但交付状态不是 pass：V16 需要局部 revise 后才能作为候选交付稿。

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | 用户任务指定 v6 草案受控验证；`当前样本测试夹具.md`；`PRD_v4.md` 输出语言要求 | `PRD_v16_v6workflow_需求确认摘要.md` | 足够开工；已明确源本、新壳、市场、范围、语言、用途、v6 草案状态 | 不改 PRD/workflow/入口 |
| 1 | 读源本 | pass | 源本 txt；精读 1-10 集；人物设定和全剧梗概 | `PRD_v16_v6workflow_Source_Bible.md` | 覆盖本轮范围；源本锚点 HV1-HV9 对应 E1-E10 |  |
| 2 | Source Bible / 源本拆文包 | pass | 源本 1-10 集 | `PRD_v16_v6workflow_Source_Bible.md` | 按 v6 Step 1 覆盖故事核、期待、首批功能、高价值节点、钩子、爽点、关系、信息差、表达手法、禁用外形 | 锚点：HV1-HV9 |
| 3 | Adaptation Boundary / 洗稿边界包 | pass | Source Bible + 样本夹具需求 | `PRD_v16_v6workflow_Adaptation_Boundary.md` | 已区分必须保留体验、必须替换外形、自由变量、删除/修复烂点 |  |
| 4 | Source Retention Anchor / 源本留存锚点 | pass | Source Bible + Boundary | `PRD_v16_v6workflow_Source_Retention_Anchor.md` | 已压出核心期待、留存闭环、钩子、爽点周期、情绪/信息/权力走势、关系拉扯和高价值节点 |  |
| 5 | Story Operating State / 写作前故事状态 | pass | Anchor + 本轮首批范围 | `PRD_v16_v6workflow_Story_Operating_State.md` | 不是剧情摘要；已给出人物欲望/恐惧/误会/主动权、信息状态、观众等待、每集写前刷新 | 后续 writer brief 需继续承接 |
| 6 | Beat sheet / outline | pass | Boundary + Anchor | `PRD_v16_v6workflow_Beat_Sheet_Outline.md` | 承接 Source Retention Anchor；B1-B12 均改变局势、关系、信息或情绪 | 锚点：B4 二选一、B9 继承人崩裂、B12 GO LIVE |
| 7 | Episode function map | pass | Beat sheet + Anchor | `PRD_v16_v6workflow_Episode_Function_Map.md` | 每集有 Opening Hook、Core Friction、Max Spike、Change、End Button、Do Not Consume、Source Retention Carry | 锚点：E2 glass corridor、E7 Daddy Ben、E8 公开反咬、E10 GO LIVE |
| 8 | 高压节点场面迁移与优选 | pass | Anchor + Episode map | `PRD_v16_v6workflow_HighPressure_Scene_Choice.md` | 只对 HP1-HP5 高压节点做候选；没有扩到普通过渡场 | 选择：E2 玻璃服务通道、E4 儿童翼命名权、E7 ribbon ceremony、E8 同场公开反咬、E10 空 press room |
| 9 | Writer brief / Scene packet | pass | Episode map + Story Operating State + 高压节点优选 | `PRD_v16_v6workflow_Writer_Brief_Scene_Packet.md` | writer-facing brief 含 Scene Sequence；高压场才追加压力链；未塞完整审计底稿 | 每集均含功能 / 进入状态 / 动作推进 / 退出状态 |
| 10 | Screenplay draft | pass | Writer brief | `PRD_v16_v6workflow_豪门商战版_首批1-10集.md` | 英文对白；按 page-to-screen 合同写可见动作、声音、物件和空间压力；没有写成说明书 | 正文锚点：E2 blood handprint、E7 Daddy Ben、E8 Find the other one、E10 GO LIVE |
| 11 | Beat survival check | pass | Screenplay + Anchor + brief | `PRD_v16_v6workflow_Beat_Survival_Check.md` | 只抽查 5 个最高风险节点；每条检查源本体验 / brief 承接 / 正文锚点 | 抽查：E2、E5、E7、E8、E10 |
| 12 | Rewrite report | pass | Screenplay + survival check | `PRD_v16_v6workflow_rewrite_report.md` | 判断结构层 `structure_pass`；未发现需要回到 Source Anchor / writer brief / screenplay 结构重写的硬失败 | watchpoints：E1 机制词、E5 可视化、E10 忏悔短句 |
| 13 | Pressure-chain patch brief | skipped | Rewrite report | `PRD_v16_v6workflow_pressure_chain_patch_brief.md` | 明确 skipped；原因是未发现压力链 / 场面发动机 / 故事状态结构失败 | 不用 dialogue polish 修结构病 |
| 14 | Dialogue polish | pass | Rewrite report / patch brief / screenplay | `PRD_v16_v6workflow_dialogue_polish.md` | 已记录表达层口径：Serena 少解释、Adrian 罪责短句化、文件只触发动作 | 当前正文已应用该口径 |
| 15 | Author quality gate | pass | 修订稿 + 工作稿 | `PRD_v16_v6workflow_author_quality_gate.md` | 按 Contract fit、Source retention carry、Adaptation fit、Scene pressure、Expression integrity、Continuity 检查；主创侧通过 | 结论：ready_for_independent_reviewer |
| 16 | Story memory checkpoint | pass | 当前稿 | `PRD_v16_v6workflow_story_memory_checkpoint.md` | 已记录关系、信息差、伏笔/证据、角色状态、未兑现承诺、禁止下批提前消费和下一批入口 | 下批入口：Serena 手指仍停在 GO LIVE |
| 17 | Independent reviewer | pass | 第一轮：PRD v4 验收口径 + 当前样本测试夹具 + 正文；第二轮：源本 1-10 + Source Bible / Boundary / Anchor / State / Episode map / HighPressure / Writer brief / Beat survival check + 正文 | `PRD_v16_v6workflow_reviewer_round1_只读正文.md` + `PRD_v16_v6workflow_reviewer_round2_源本审计.md` | reviewer 结论：`revise`；不是洗飞 / 改名复刻 / 系统性短剧降级；链路基本闭合，但 E3、E8、E9-E10 需局部修稿 | failure_layer：screenplay_pressure_execution / local_scene_trigger；callback：Step 13 pressure-chain patch brief + Step 14 dialogue polish + local Step 10 screenplay revision |
| 18 | Version comparison / 主控交付判断 | pass | 当前稿 + V3 + V14 + V15 + reviewer 两轮结论 | `PRD_v16_v6workflow_vs_v3_v14_v15_版本对比.md` + `PRD_v16_v6workflow_主控判定.md` | 主控判定：execution_complete / delivery_revise；V16 证明 v6 链路可跑通，但 reviewer revise 未清，不能作为可交付 pass | callback：局部回 Step 13 / Step 14 / Step 10 修 E3、E8、E9-E10 |

## 未完成步骤

- 无执行步骤未完成。

## 不允许交付原因

- 独立 reviewer 已执行，但结论为 `revise`，仍有必须修稿项。
- 本轮可以声称 v6 草案受控验证执行链路闭合，不能声称 V16 是可交付 pass，也不能据此把 v6 升为正式 workflow。
