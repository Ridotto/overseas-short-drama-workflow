# workflow run manifest V21 v11workflow

任务：飞书三星样本按 v11 候选 workflow 重跑首批 1-10 集
版本：V21 / v11workflow
日期：2026-07-01
执行 agent：v21_v11_clean_writer
使用的产品定义：
- v2-restart/项目基础说明.md
- v2-restart/PRD_v4.md
- v2-restart/PRD_v4_写作前故事包补充候选.md
使用的 workflow spec：
- v2-restart/workflow_spec_v11_写作前故事包候选版.md
- v2-restart/workflow_execution_protocol_v1.md
输入源本：
- v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt
目标新壳：海外豪门商战
输出范围：不改变源本集数；本轮只交付首批 1-10 集
输出语言：台词英文；动作和场景描述中文；内部分析中文
正文用途：人审稿，同时满足后续 AI 视频生成的 page-to-screen 写法
产物前缀：PRD_v21_v11workflow_

## 输入边界说明

- 本轮已按用户指定读取当前工作入口、项目基础说明、PRD v4、PRD v4 写作前故事包补充候选、workflow spec v11、workflow execution protocol v1 和源本。
- `当前工作入口.md` 中提到 `V3_V5完整对读与合并方案_2026-07-01.md` 是 v11 的能力回收依据，但本轮用户明确要求不要打开或参考 V3/V5/V20/V18 等旧版产物文件。为保持干净主创，本轮不读取该对读材料，也不读取旧版正文、旧版工作稿、旧版 reviewer 或旧版对比。
- 该边界不改变本轮执行的 workflow spec：本轮以 `workflow_spec_v11_写作前故事包候选版.md` 的步骤为准。
- 当前未发现 PRD、workflow spec 与本轮需求在交付范围、语言、用途、manifest-first 顺序上存在阻断性冲突。

## 总状态

- workflow execution：complete through reviewer
- creative outcome：revise
- source carry-through：pass with revision risks
- delivery outcome：not pass
- 说明：所有本轮必须执行步骤已有产物证据；reviewer 两轮均完成，但 reviewer 结论为 `revise`，所以不能作为质量 pass 或可直接交付版本。

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | 用户任务载明任务类型、源本、新壳、集数、输出范围、语言、用途；workflow_spec_v11 Step 0 | 本 manifest 的任务栏、输入边界说明 | 足够开工：洗稿/改编、海外豪门商战、首批 1-10 集、台词英文/动作中文、人审+AI 视频生成均明确 | 未另问用户，因本轮输入已覆盖必填项 |
| 1 | 读源本 | pass | 源本 1-37 集全文，重点读取首批 1-10 集及后续全剧状态 | PRD_v21_v11workflow_Source_Bible.md | 已完整读取源本文本范围；Source Bible 已承接首批功能和后续状态 |  |
| 2 | 源本有效性包 / Source Bible | pass | 源本全文；首批 1-10 集为重点 | PRD_v21_v11workflow_Source_Bible.md | pass：见 HV1-HV8，覆盖登堂替换、生死选择、回归、女配清算、伤疤线索、假继承人、旧物火葬场、下跪求赎 | 每个高价值节点均有体验功能、强度来源、信息边界和下游抓手 |
| 3 | 二次需求确认 | pass | Source Bible + 用户需求 | PRD_v21_v11workflow_二次需求确认.md | pass：确认海外豪门商战可承载源本强机制；明确强继承、强替换、必删项 | 未向用户追问，因本轮输入已明确且读本后无阻断 |
| 4 | 洗稿边界包 / Adaptation Boundary | pass | Source Bible | PRD_v21_v11workflow_Adaptation_Boundary.md | pass：区分必须保留体验、必须避开外形、可自由变量和删除修复项 | 明确禁止车祸外形、黑帮外形和 Ep7-Ep8 认证台化 |
| 5 | 新本创作开发包 / Creative Development Pack | pass | Source Bible + Boundary | PRD_v21_v11workflow_Creative_Development_Pack.md | pass：新本有 Premise、Story Engine、角色行动方式、关系/权力状态 | 每个设定均服务后续场面：债权、港口、信托、Nightingale |
| 6 | 首批 / 全剧阶段骨架 / Stage Skeleton | pass | Creative Development Pack | PRD_v21_v11workflow_Stage_Skeleton.md | pass：1-2、3-5、6-8、9-10 四阶段均有起点、任务、兑现、追问和不可提前消费 | 防止 Ep7-Ep8 提前消费 Ep9 旧物火葬场 |
| 7 | 分集追剧提纲 / Episode Pursuit Map | pass | Stage Skeleton | PRD_v21_v11workflow_Episode_Pursuit_Map.md | pass：Ep1-Ep10 均有 Opening Hook、Max Spike、End Button、Do Not Consume、Chain Carry | 高压集 Ep2、Ep4、Ep7-Ep10 可进入 Step 8 |
| 8 | 高压场面候选与优选 | pass | Episode Pursuit Map | PRD_v21_v11workflow_HighPressure_Scene_Options.md | pass：对 Ep2、Ep4、Ep7-Ep8、Ep9、Ep10 做候选和优选；列淘汰原因 | 重点避开车祸、验血、报告和枪口 |
| 9 | 写作前故事包 / Playable Writer Brief | pass | Development Pack + Stage Skeleton + Episode Map + Scene Choice | PRD_v21_v11workflow_Playable_Writer_Brief.md | pass：writer 可只读 brief 写正文；不含 manifest、reviewer、旧版对比或审计噪音 | 给出每集追问、兑现、卡点、最后可拍瞬间和信息边界 |
| 10 | Screenplay draft | pass | PRD_v21_v11workflow_Playable_Writer_Brief.md | PRD_v21_v11workflow_豪门商战版_首批1-10集.md | pass：正文覆盖 Ep1-Ep10；台词英文、动作中文；无内部字段；高压锚点见 Ep2 helipad 火门、Ep4 债权拍卖、Ep7-Ep8 信托命名礼、Ep9 湖屋旧物、Ep10 屋顶边缘 | 正文完成后做了少量台词修订 |
| 11 | Rewrite report | pass | Screenplay draft | PRD_v21_v11workflow_rewrite_report.md | pass：定位风险层为 scene_option/screenplay/dialogue/continuity；列症状、动作、回滚点 | 未直接结构回滚 |
| 12 | Pressure-chain patch brief | pass | Rewrite report + Screenplay draft | PRD_v21_v11workflow_pressure_chain_patch_brief.md | pass：Ep1-Ep10 压力链均有起压、升压、爆点、收住；明确 Ep7 和 Ep10 风险 | 确认结构维持 |
| 13 | Dialogue polish | pass | Patch brief + Screenplay draft | PRD_v21_v11workflow_dialogue_polish.md；正文文件已修订 | pass：处理 3 处英文顺口/语法问题；保留短剧化强台词 | 未改动作行语言 |
| 14 | 作者 ready check | pass | 修订后正文 + 中间产物 | PRD_v21_v11workflow_author_ready_check.md | pass：结论 ready_for_reviewer；列高风险节点迁移、风险、不应修改项 | 允许进入 reviewer |
| 15 | Story memory checkpoint | pass | 修订后正文 + ready check | PRD_v21_v11workflow_story_memory_checkpoint.md | pass：记录角色状态、关系距离、权力位置、信息差、已兑现/未兑现追问、后续不可提前消费内容和物件状态 | 支撑后续批次 |
| 16 | 独立 reviewer | pass | Round 1：最小需求 + PRD_v21_v11workflow_豪门商战版_首批1-10集.md；Round 2：Source Bible、Boundary、Creative Pack、Stage Skeleton、Writer Brief、必要源本片段、正文 | PRD_v21_v11workflow_reviewer_round1_只读正文.md；PRD_v21_v11workflow_reviewer_round2_源本审计.md | pass for review execution；reviewer 结论 revise。Round 1 失败层 screenplay/dialogue/continuity；Round 2 失败层 source_analysis/boundary/creative_pack/writer_brief/screenplay/dialogue/continuity | reviewer 声明第一轮未读取作者自检、rewrite report、story memory、源本有效性包、边界包、开发包、阶段骨架、writer brief、旧版产物或对话历史；第二轮未读取作者 ready check/rewrite/dialogue/story memory/V3/V5/V18/V20 |
| 17 | 主控版本对比与交付判断 | skipped | 本轮用户最终回复要求不做旧版对比，由主控另做 | 无 | 用户明确旧版对比由主控另做；主创侧不执行 | 本轮最终只交付主创产物和 reviewer 结论 |

## 未完成步骤

- 无。

## 不允许交付原因

- workflow execution 可以声称 complete through reviewer。
- 不能声称质量 pass 或直接交付：reviewer 两轮结论均为 `revise`。
- 必修方向：统一 Serena 的核心骗局定义；降低 Ep1 / Ep5 / Ep10 表面相似度；增强 Ep2 火场调度、Ep4-Ep5 商战可视化、Ep7 证人链因果、Ep9 twins 伏笔和 Ep10 忏悔递进。
