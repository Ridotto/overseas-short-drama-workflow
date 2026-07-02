# workflow run manifest V25 v14skillchain

任务：按 `workflow_spec_v14_skill工位链候选版.md` 对飞书三星样本跑海外豪门商战新壳首批 1-10 集。

版本：V25 v14skillchain

日期：2026-07-01

执行 agent：干净主创链执行 agent；干净 reviewer agent；主控 agent

使用的产品定义：`v2-restart/项目基础说明.md`、`v2-restart/PRD_v4.md`

使用的 workflow spec：`v2-restart/workflow_spec_v14_skill工位链候选版.md`

使用的 skill 工位规格：`v2-restart/skill_chain_spec_v1.md`

执行验收协议：`v2-restart/workflow_execution_protocol_v1.md`

输入源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`

目标新壳：海外豪门商战

输出范围：首批 1-10 集，集数不动；默认对白英文，动作行 / 场景描述中文。

## 总状态

- 状态：complete through S11
- 说明：S0-S9 由干净主创链完成；S10 由干净 reviewer 后补完成；S11 由主控完成。最终创作结论为 `revise / narrow repair`，不是 `pass`，也不是 `block`。

## 本轮 0xsline 分阶段加载记录

| 工位 | 实际加载 | 边界 |
|---|---|---|
| S0 | `v2-restart/参考资产/1-short-drama_短剧标准库/references/genre-guide.md` | 只辅助题材、市场、受众和语感确认 |
| S1 | `rhythm-curve.md` / `hook-design.md` / `satisfaction-matrix.md` | 只帮助拆源本追看机制，不压过源本 |
| S2 | 无固定 0xsline 文档 | 以源本迁移、防洗飞、防复刻为主 |
| S3 | `genre-guide.md` / `rhythm-curve.md` / `paywall-design.md` / `villain-design.md` | 只辅助故事底盘、追问兑现和反派燃料 |
| S4 | `satisfaction-matrix.md` / `hook-design.md` | 只给可写戏原料，不替 writer 排戏 |
| S5 | `opening-rules.md` / `rhythm-curve.md` / `hook-design.md` / `satisfaction-matrix.md` | 只在施工稿阶段加载短剧手艺 |
| S6 | S5 施工稿 + 已加载短剧手艺 | 从施工稿写可看可听正文 |
| S7 | `genre-guide.md` + 本项目台词 / 视听要求 | 只做台词和视听 polish，不改主线 |
| S8 | 无固定 0xsline 文档 | 只查事实、状态、伏笔、信息边界 |
| S9 | 无固定 0xsline 文档 | 作者自检与返修路由 |

## 步骤证据表

| Step | Skill | 状态 | 输入证据 | 输出证据 | Gate 判断 | 角色切换 / 备注 |
|---|---|---|---|---|---|---|
| 0 | 建 manifest | pass | `workflow_execution_protocol_v1.md`；`workflow_spec_v14_skill工位链候选版.md` | 本文件 | pass：manifest 是本轮第一个正式产物 | 主控 / run state |
| 1 | S0 需求确认 | pass | 用户任务；`项目基础说明.md`；`PRD_v4.md`；`workflow_spec_v14_skill工位链候选版.md`；阶段加载 `genre-guide.md` | `01_最小需求确认.md` | pass：新壳、集数、语言、改写方式、禁区、输出目录和 workflow 均明确，足够开工 | 已切换到需求确认 skill；未分析源本、未写正文 |
| 2 | S1 源本拆文 | pass | 源本全文；`01_最小需求确认.md`；阶段加载 `rhythm-curve.md` / `hook-design.md` / `satisfaction-matrix.md` | `02_源本拆文包.md` | pass：已覆盖首批 1-10 集追问、分集功能、高价值节点 HV1-HV9、压放结构、人物拉扯、Do Not Consume 和含混点 | 已切换到源本拆文 skill；未设计新壳 |
| 3 | S2 洗稿边界 / 变量迁移 | pass | `02_源本拆文包.md`；`01_最小需求确认.md`；`原项目能力对账表_2026-07-01.md` | `03_洗稿边界包.md` | pass：已区分强继承、等效迁移、自由改写、删除修复、同构红线、防洗飞红线和新壳承载点 | 已切换到洗稿边界 skill；未设计正文 |
| 4 | S3 新本故事架构 | pass | `02_源本拆文包.md`；`03_洗稿边界包.md`；阶段加载 `genre-guide.md` / `rhythm-curve.md` / `paywall-design.md` / `villain-design.md` | `04_新本故事开发包.md` | pass：已给出新本故事核、真相账本、角色错信、主追问、1-10 分集功能、当前故事状态、Do Not Consume 和卡点策略 | 已切换到新本故事架构 skill；未写正文 |
| 5 | S4 场面承载原料 | pass | `02_源本拆文包.md`；`03_洗稿边界包.md`；`04_新本故事开发包.md`；阶段加载 `satisfaction-matrix.md` / `hook-design.md` | `05_场面承载原料包.md` | pass：已按关键场给出源本体验功能、新壳场面载体、谁压谁、旁观者、可见后果、禁照抄外形、不可提前消费、降级风险；未替 writer 排完整戏 | 已切换到场面承载原料 skill |
| 6 | S5 writer 单集施工稿 | pass | `04_新本故事开发包.md`；`05_场面承载原料包.md`；阶段加载 `opening-rules.md` / `rhythm-curve.md` / `hook-design.md` / `satisfaction-matrix.md` | `06_writer单集短剧施工稿.md` | pass：施工稿按 1-10 集逐集排出开场、升压、释放、结尾画面和 Do Not Consume；文本像戏的粗稿，不是字段表 | 已切换到 writer 施工稿 skill；未写最终正文 |
| 7 | S6 screenplay 正文写作 | pass | `06_writer单集短剧施工稿.md`；`04_新本故事开发包.md` 当前故事状态；`05_场面承载原料包.md` 边界 | `07_screenplay正文初稿_首批1-10集.md` | pass：正文覆盖 1-10 集，保留施工稿核心强度；EP2 电梯火灾、EP4 拍卖碾压、EP7-EP8 公开审判、EP9 旧物击穿、EP10 控制权献祭均为可看可听场面 | 已切换到 screenplay writer skill；正文未使用旧版本正文 |
| 8 | S7 台词 / 视听 polish | pass | `07_screenplay正文初稿_首批1-10集.md`；`06_writer单集短剧施工稿.md`；阶段加载 `genre-guide.md` + page-to-screen 要求 | `08_台词视听polish稿_首批1-10集.md` | pass：已压缩英文对白，强化电梯、红酒、墨水、雨声、玻璃门、签字文件、枪声等视听物件；未改主线和事件顺序 | 已切换到台词 / 视听 polish skill |
| 9 | S8 连续性 / 真相 / 信息边界 | pass | `04_新本故事开发包.md`；`08_台词视听polish稿_首批1-10集.md` | `09_story_memory_checkpoint.md` | pass：已记录已播出信息、未播出 / 不可提前消费信息、角色状态、物件伏笔、下一集承接问题和连续性检查；EP10 枪响明确未解释 | 已切换到连续性和信息边界 skill；未评价爽感 |
| 10 | S9 作者自检与返修路由 | pass | S1-S8 全部产物；`08_台词视听polish稿_首批1-10集.md`；`09_story_memory_checkpoint.md` | `10_作者自检与返修路由.md` | pass：已检查洗飞、改名复刻、提前消费、核心真相、施工稿强度、高压节点、台词和下一集追问；给出明确返修路由和 author verdict | 已切换到作者自检 skill；结论为 pass to clean reviewer |
| 11 | S10 干净 reviewer | pass | Round1：`PRD_v4.md`、`workflow_spec_v14_skill工位链候选版.md`、`01_最小需求确认.md`、`03_洗稿边界包.md`、`08_台词视听polish稿_首批1-10集.md`；Round2：源本、`02_源本拆文包.md`、`04_新本故事开发包.md`、`05_场面承载原料包.md`、`06_writer单集短剧施工稿.md`、`09_story_memory_checkpoint.md` | `11_reviewer_round1_只读需求边界正文.md`；`12_reviewer_round2_源本迁移审计.md` | pass：reviewer 按两轮读取顺序完成；最终 verdict 为 `revise`，不是 `block` | 干净 reviewer 第一轮未读作者自检、源本和旧版本；第二轮仍未读作者自检和旧版本 |
| 12 | S11 主控版本对比与拍板 | pass | V25 全部产物；reviewer round1/round2；V5 / V22 / V24 样本正文与既有对比文档 | `13_主控版本对比与拍板.md` | pass：已完成 V25 vs V5 / V22 / V24 全方位对比；主控结论为 `revise / narrow repair` | 主控读取旧版本只用于 S11 对比，不影响主创产物 |

## 未完成步骤

- 无。

## 当前不允许交付原因

- V25 当前 verdict 为 `revise`。
- 必须先窄返修：EP10 去枪口外形；Celeste 真相措辞；EP6-EP10 信息重复压缩；EP7 Adrian 状态台词。
- 返修前不能作为导演送审稿或正式 workflow pass 证据。
