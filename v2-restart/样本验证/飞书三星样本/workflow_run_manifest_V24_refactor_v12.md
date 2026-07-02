# workflow run manifest

任务：飞书三星样本 v12 短剧底盘接入候选版验证
版本：V24 refactor v12
日期：2026-07-01
执行 agent：干净主创 agent
使用的产品定义：v2-restart/PRD_v4.md
使用的 workflow spec：v2-restart/workflow_spec_v12_短剧底盘接入候选版.md
执行协议：v2-restart/workflow_execution_protocol_v1.md
输入源本：v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt
目标新壳：海外豪门商战 / 家族企业权力斗争
目标市场：海外短剧
集数：不变
输出范围：首批 1-10 集
输出语言：默认台词英文；动作和场景描述中文；内部分析中文
正文用途：人审稿 + AI 视频生成 page-to-screen
改写力度：中度偏重；保留源本追看机制、钩子/卡点/情绪节奏/关系拉扯/付费动力；新事件载体不能改名复刻

## 总状态

- 当前状态：complete through author chain；full v12 reviewer stage skipped by task scope
- complete 条件：Stage 0-11、13 均有真实产物、路径、pass/fail 和证据锚点；Stage 12 按本轮主创任务范围明确 skipped，不能声称 through reviewer。
- 本轮说明：入口文档默认候选仍写 v11，但本轮用户明确指定使用 v12；因此按用户指定 workflow spec 执行，并在此 manifest 中记录。

## 步骤证据表

| Stage | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | Run Manifest + Minimal Need | pass | 用户任务；PRD_v4.md；workflow_spec_v12_短剧底盘接入候选版.md；workflow_execution_protocol_v1.md | PRD_v24_refactor_v12_最小需求确认.md | 最小需求已显式确认：任务类型、新壳、市场、集数、范围、语言、用途、改写力度均足够开工 | manifest 是本轮第一个正式产物 |
| 1 | Source Bible / 源本有效性包 | pass | 源本全文：1-37 集；首批重点 1-10 集 | PRD_v24_refactor_v12_Source_Bible.md | pass；锚点：HV1 白月光怀孕登堂入室、HV2 事故中男主二选一、HV3 五年后身份回归压场、HV4 公开揭穿 Lily、HV5 物件火葬场、HV6 当众跪求原谅 | 已标出源本事实冲突和禁止复用外形 |
| 2 | Adaptation Boundary / 洗稿边界包 | pass | PRD_v24_refactor_v12_Source_Bible.md | PRD_v24_refactor_v12_Adaptation_Boundary.md | pass；锚点：必须保留的体验功能、必须避开的源本外形、新壳承载风险 | 明确不用黑帮/军火/车祸/枪/保险箱等源本高辨识外形 |
| 3 | Short Drama Creative Plan / 短剧创作方案 | pass | Source Bible；Adaptation Boundary；genre/rhythm/satisfaction/hook/paywall 参考 | PRD_v24_refactor_v12_Short_Drama_Creative_Plan.md | pass；锚点：Core Truth Ledger、Core Pursuit、Payoff Logic、Overseas Boundary | 锁定 Billionaire revenge + Hidden Identity + Second Chance dark romance |
| 4 | Character & Opposition Bible / 角色关系与对抗发动机 | pass | Stage 1-3；villain-design；oh-story 状态追踪思想 | PRD_v24_refactor_v12_Character_Opposition_Bible.md | pass；锚点：Serena / Adrian / Chloe / Victor 行动发动机、反派层级、关系变化目标 | Chloe 和 Blackwell Empire 均保留可持续阻力 |
| 5 | Stage Rhythm Plan / 阶段节奏与追问计划 | pass | Stage 1-4；rhythm-curve、paywall-design、hook-design、satisfaction-matrix | PRD_v24_refactor_v12_Stage_Rhythm_Plan.md | pass；锚点：全剧阶段 A-E、首批 1-10 节奏波形、首批不可提前消费 | 首批 10 集切在 Go Live 自白前 |
| 6 | Episode Pursuit Directory / 分集追剧目录 | pass | Stage Rhythm Plan；Source Bible；Adaptation Boundary | PRD_v24_refactor_v12_Episode_Pursuit_Directory.md | pass；锚点：Episode 1-10 每集 Opening Hook、End Button、Next-Episode Payoff、Forbidden Shape | 每集都有追问、兑现义务、不可提前消费 |
| 7 | Scene Carrier Pack / 场面承载包 | pass | Episode Pursuit Directory；opening-rules；screenplay-to-video bridge | PRD_v24_refactor_v12_Scene_Carrier_Pack.md | pass；锚点：SC1 年会离婚、SC2 双玻璃电梯火灾、SC4 Trust Hearing、SC7 Go Live 自毁卡点 | 高压节点均有现场动作和可见后果 |
| 8 | Playable Writer Brief / 可写剧本简报 | pass | Stage 3-7 | PRD_v24_refactor_v12_Playable_Writer_Brief.md | pass；锚点：Episode Pursuit、Selected Scene Carrier、Information Boundary、Four Survival Questions | brief 保留可写戏信息，不带完整审计噪音 |
| 9 | Screenplay Draft / 首批正文 | pass | PRD_v24_refactor_v12_Playable_Writer_Brief.md | PRD_v24_refactor_v12_豪门商战版_首批1-10集.md | pass；锚点：Ep2 双玻璃电梯火灾、Ep4 债权冻结、Ep7 Trust Hearing、Ep8 DNA 崩盘、Ep9 双胞胎手环、Ep10 Go Live | 正文台词英文，动作/场景中文；不带 workflow 标签 |
| 10 | Author Quality Pass / 作者自检与表达返修 | pass | PRD_v24_refactor_v12_豪门商战版_首批1-10集.md | PRD_v24_refactor_v12_Author_Quality_Pass.md | pass；锚点：Failure Layer、四个存活问、Root Symptoms、Prioritized Actions、Rollback Point | 自检结论：reviewer-ready，但 delivery 未 pass |
| 11 | Story Memory / 状态追踪 | pass | Screenplay Draft；Author Quality Pass | PRD_v24_refactor_v12_Story_Memory.md | pass；锚点：当前时间线、角色状态、信息差、未兑现追问、下一批安全入口 | 记录了直播、手环、CEO 徽章、Marcus 证词等伏笔物件 |
| 12 | Clean Reviewer / 干净审稿 | skipped | 本轮任务未要求主创调用独立 reviewer；且当前 agent 是主创，不冒充干净 reviewer | skipped | 允许跳过：主控任务要求产出至少不含 reviewer 文件；本轮交付主创产物，后续可由主控另开干净 reviewer | v12 workflow 有此阶段，但本任务最小产物未要求 reviewer；不能据此声称 through reviewer |
| 13 | Controller Delivery Judgment / 主控交付判断 | pass | Stage 0-11；本轮按用户限制不读取旧版本对比稿 | PRD_v24_refactor_v12_主创交付判断.md | pass for 主创交付判断；锚点：Workflow Execution、Creative Outcome、Source Carry-Through、Delivery Outcome、最强/最弱 | 不替代主控；不做旧版对比 |

## 未完成步骤

- Stage 12 Clean Reviewer：skipped。原因：本轮任务指定当前 agent 为干净主创，最小产物未要求 reviewer；主创不能冒充独立 reviewer。
- 旧版本对比：未执行。原因：本轮明确禁止读取 V3 / V5 / V20 / V21 / V22 / V23 旧产物。

## 不允许交付原因

- 不能声称完成 v12 through reviewer。
- 不能声称 delivery pass。
- 可以声称：本轮 V24 refactor v12 主创链路已完成，产物可交给主控安排干净 reviewer 和版本对比。
