# 外部写作能力完整审计

日期：2026-07-06

> 定位：本文件是外部写作能力总审计和后续产品化路线依据。台词强度专项证据见 `dialogue_force_code_audit_2026-07-06.md`。

## 先纠错

上一份 `dialogue_force_code_audit_2026-07-06.md` 不是完整写作能力审计。

它只回答了一个窄问题：

```text
为什么当前样本台词太平，以及外部资产里哪些东西能补台词火气。
```

本文件补的是更大的问题：

```text
外部资产全集里，哪些是真正的写作能力；
哪些已经进入当前主链；
哪些缺口仍存在；
哪些不应该接，避免污染短剧洗稿主链。
```

本审计是“能力级完整审计”，不是把外部项目全仓逐字合并。凡是要进入主链的能力，必须满足：

- 服务短剧洗稿，不服务泛小说、长剧、电影或视频流水线。
- 落到 `source-import`、`/plan`、`/characters`、`/outline`、`/episode`、`/dialogue-polish`、`/review`、`/batch-state` 或 `/export` 的明确责任层。
- 不让 writer 直接读完整外部项目。
- 不用“参考一下”这种软接入；必须变成执行字段、writer 必吃输入、review 边界或用户确认物。

## 外部资产现状

本机能找到的完整外部仓库在：

```text
/Users/jiakun/Codex/自动化编剧/.local-archive/obsolete-worktrees-2026-07-04/自动化编剧-external-chain-rebuild/external_full_repos/
```

包含：

- `short-drama`
- `oh-story-claudecode`
- `how-to-make-script`
- `shortdrama-pipeline`
- `dramatron`

当前 `codex/next` 已 vendor 进来的只有：

- `shortdrama-remix/vendor/short-drama`
- `shortdrama-remix/vendor/oh-story-claudecode/skills/story-import`

没有在本机找到可审计源码：

- `ReelForge-YAML`
- `duanju_create_agent`

这两者只能按历史记录处理，不能声称已完成代码级接入或可直接迁移。

## 总结论

当前主链的短剧底盘已经比较完整，缺的不是再塞一个大外部项目。

真正缺口是三块小而关键的写作能力：

1. **受众/平台适配还没有被压成轻量可执行诊断。**
   当前已有出海本地化和 genre mapping，但 `/plan` 仍偏“强节点适配”和“商业蓝图”，缺一个更小的 `audience/platform need state` 判断：目标观众为什么点开、为什么流失、当前稿和目标平台的回报是否错位。

2. **角色声线还停在倾向，没有变成台词武器。**
   当前 `/characters` 已有句长、攻击方式、闪避方式、沉默方式，但还不够施工。缺少“这个角色如何伤人、如何躲责任、被戳中后怎么失控、公众场合和私下如何变声、哪类句子一出现就 off-character”。

3. **`/episode` 前缺台词冲突模式。**
   当前有 `performance-dialogue-brief.md` 和 `dialogue-polish-brief.md`，但它们更像原则和 polish；还缺每场戏开写前的模式选择：压制、反咬、装弱、心死、求信失败、公开站队、火葬场拒绝等。没有这个，writer 会优先保证剧情正确，台词仍容易客观、冷静、没脾气。

其他能力不是没有，而是已经在主链里，或不该接。

## 按外部资产逐项审计

### 1. `short-drama`

定位：短剧标准库。

可用能力：

- 题材定义。
- 开篇规则。
- 节奏曲线。
- 爽点矩阵。
- 反派设计。
- 钩子设计。
- 付费卡点。
- 出海 genre mapping。

当前接入状态：已经接入主链。

已落点：

- `/start`、`/plan` 读 `genre-guide.md`、`opening-rules.md`、`paywall-design.md`、`rhythm-curve.md`、`satisfaction-matrix.md`
- `/characters` 读 `villain-design.md`
- `/episode` 读 `opening-rules.md`、`rhythm-curve.md`、`satisfaction-matrix.md`、`hook-design.md`
- `/review` 读形态锁和相关 brief

判断：

```text
继续当短剧底盘，不需要再重复接。
```

它不能单独解决“台词火气”和“角色说话像真人”，因为它不是台词系统。

### 2. `oh-story-claudecode`

定位：网文/小说工程资产，里面有可抽取的短篇情绪和台词强度材料。

不能整接。

原因：

- 默认口径偏网文、小说、章节制。
- 容易把短剧剧本污染成内心独白、爽文段落或小说旁白。
- `story-review` 是网文审稿，不是短剧付费体验审稿。
- `story-deslop` 的机械禁词风险太高，可能误删有效短剧套路。

可迁移能力：

| 来源 | 能力 | 适合落点 | 判断 |
| --- | --- | --- | --- |
| `story-import` | 本节速记、状态追踪、结构映射 | `series-state-brief.md`、`/plan`、`/outline`、`/episode`、`/batch-state` | 已接入为长线状态骨架 |
| `story-short-write/dialogue-mastery.md` | 压制/反转/心死/情绪推动/信息嵌入等台词模式 | `/episode` 写前、`/dialogue-polish`、`/review` | 已吸收原则，但模式选择器还没够硬 |
| `story-short-write/short-craft.md` | 情绪宁烈不温、一节一炸点、强情绪接动作 | `/outline`、`/episode` | 可抽小段，不整接 |
| `story-short-write/emotional-methods.md` | 欺压、忍耐、爆发、打脸、情绪裂口 | `/plan`、`/outline`、`/episode` | 适合女频情绪链，但要短剧化 |
| `story-short-analyze/genre-readers.md` | 读者/平台期待差异 | `/plan` 的受众平台复核 | 可抽轻量判断，不直接给 writer |
| `story-short-analyze/genre-core-mechanics.md` | 类型核心与情绪回报 | `/plan`、`/outline` | 可用于目标产物画像 |

当前主链缺口：

```text
oh-story 的“台词模式选择器”没有完整落到 /episode 写作前。
```

它不应该变成新 workflow，只应该瘦身成一小段 writer 必吃的施工口径。

### 3. `how-to-make-script`

定位：影视/剧本 craft、受众、声线、改稿诊断工具箱。

不能整接。

原因：

- 里面有电影、电视剧、commercial、互动叙事和泛开发工具，不是短剧洗稿专用。
- `scene-writing` 和 `dialogue-subtext` 有价值，但太影视化时会把短剧写克制。
- 许多 skill 是开发流程、团队协作或质量报告，不该进入 writer 上下文。

当前已接入：

- `scene-writing`
- `wp-scene-writing`
- `rb-scene-draft`
- `dialogue-subtext`
- `wp-dialogue-polish`
- `rb-dialogue`

这些已经合并进：

- `performance-dialogue-brief.md`
- `dialogue-polish-brief.md`

本轮确认的新候选：

| 来源 | 能力 | 适合落点 | 判断 |
| --- | --- | --- | --- |
| `voice-style-calibration` | voice anchors、lived pressure、register envelope、drift warnings | `/characters` | 应接，但要短剧化成“台词武器表” |
| `wp-voice-style-guide` | 表达锚点、可变区间、失真红线 | `/characters`、`/dialogue-polish` | 应抽取 |
| `rb-voice-style-guide` | 评估声线指南是否可执行 | `/review` 轻检查 | 可抽取 |
| `ka-character-voice-consistency` | 声音来自欲望、羞耻点、身份成本 | `/characters` | 应抽取 |
| `ka-verbal-rhythm` | 句长变化、打断、停顿、朗读测试 | `/episode`、`/dialogue-polish` | 应抽取 |
| `ka-embodied-text-pressure` | 身体压力、关系风险、时间成本进入语言 | `/episode` | 应抽取 |
| `audience-insight` | 受众段、需求状态、错位风险 | `/plan` | 应轻量接 |
| `wp-audience-fit-note` | audience fit note | `/plan` | 应轻量接 |
| `ka-audience-need-state` | 观众不是人口标签，而是观看任务 | `/plan` | 应轻量接 |

当前主链缺口：

```text
how-to 的“声线校准”和“受众需求状态”还没有正式产品化。
```

但不建议接成两个新大环节。正确落点：

- `/plan` 增加极轻的受众/平台回报错位判断。
- `/characters` 增加角色台词武器表。
- `/episode` 和 `/dialogue-polish` 吃角色台词武器，不再临场泛泛要求“声线不同”。

### 4. `shortdrama-pipeline`

定位：生产流水线、状态机、产物管理、视频分镜 QA。

可用能力：

- job 状态机。
- artifact store。
- approve/reject。
- latest assets。
- harness warning。
- 分镜时长、镜头承载量、单镜对白密度检查。

不可用作：

- writer 文本能力。
- 台词火气能力。
- 短剧商业蓝图能力。

代码判断：

- `prompts.py` 的脚本提示只要求“中文短剧、节奏快、情绪强、每集结尾钩子”，过于泛化。
- `harness.py` 检查的是镜头时长、镜头过载、单镜对白密度、集时长偏差；它是分镜/交付 QA，不是剧情写作判断。
- `pipeline.py` 的状态机有工程价值，但不应进入文本主创。

判断：

```text
暂不接写作链。
```

后续如果项目做 UI、队列、批次追责、latest/canon 管理，可以借它的工程形态。

### 5. `dramatron`

定位：分层生成和协作式剧作实验。

可借：

- logline -> characters -> plot points -> locations -> dialogue 的层级思想。

不适合：

- 源本洗稿。
- 短剧付费卡点。
- 台词火气。
- TikTok/ReelShort/DramaBox 式商业节奏。

判断：

```text
仅保留历史启发，不接主链。
```

### 6. `ReelForge-YAML` / `duanju_create_agent`

当前本机没有找到完整源码。

历史记录里提过它们可能有：

- badcase 量化。
- source traceability。
- 张力 K 线。
- 产物追责。
- 自检结构。

但由于源码不存在，不能进入本轮代码级审计结论。

判断：

```text
不能声称已接，不能直接迁移。
```

## 按当前主链逐层对照

### `source-import`

当前能力：

- 源本有效性。
- 集级事件账本。
- 人物功能账本。
- 爽点钩子账本。
- 付费点与追更压力。
- 可迁移结构。
- 禁抄边界。
- 目标市场/本地化适配复核。
- 源本留存锚点。

缺口：

- 不大。
- 可以补 `source-span traceability` 的思想，但当前已有 `07_禁抄边界.md` 和 `09_源本留存锚点.md`，不能再加厚。

建议：

```text
不新增大能力，只保留现有口径。
```

### `/plan`

当前能力：

- 商业项目包。
- 强节点适配审计。
- 出海/平台本地化策略。
- 保护现稿有效点。
- 高置信建议必须有证据和推理链路。
- 全剧追踪骨架。

缺口：

- 受众/平台的“观看需求状态”还不够显性。
- 现在能判断 TikTok、女频、出海，但还缺一句更硬的问题：

```text
这个目标观众为什么在前 5-30 秒停住？
她想拿到什么回报？
当前稿哪里会让她提前滑走？
```

建议：

```text
在 /plan 里加一个轻量 audience/platform fit note，不开新环节。
```

### `/characters`

当前能力：

- 角色欲望、恐惧、面具。
- 关系反应差异。
- 主动施压能力。
- 声线倾向。
- 首批角色状态。

缺口：

- 声线倾向还不能稳定指导正文台词。
- 缺“台词武器表”。

建议：

```text
在 characters.md 里新增每个主要角色的台词武器表。
```

字段应该是：

- 常用施压方式。
- 常用逃责方式。
- 被戳中羞耻点时的失控方式。
- 对女主/反派/公众/权力对象分别如何变声。
- 一句“只有他/她会说”的锚点句。
- off-character 红线。

### `/outline`

当前能力：

- 每集小 draft。
- 源本赚钱功能。
- 新壳可见刺激动作。
- 一眼可懂代价。
- 释放/扣留。
- Max Spike。
- 反派新伤害。
- 强度适配检查。
- 高压可施工检查。

缺口：

- 分集包对“这一集是什么台词冲突模式”不够明确。

建议：

```text
不新增厚字段，只在每集执行包里把高压可施工检查改得更像台词任务。
```

例如：

- 本集主要压制方式。
- 本集女主求信/心死/反击阶段。
- 本集反派话术类型。
- 本集必须出现的关系位置变化句。

### `/episode`

当前能力：

- 动作链检查。
- 每场戏 6 个问题。
- 反应链。
- 可见代价。
- 角色声线倾向。
- 状态增量。

缺口：

- 没有强制选择“台词冲突模式”。

建议：

```text
在 /episode 写作前加最小 dialogue-force mode，不输出给用户。
```

不是新增文档大工程，而是 writer 写每场戏前必须明确：

- 这场是压制、反咬、装弱、求信失败、心死、公开站队、还是火葬场拒绝？
- 谁短句掌权，谁长句失控？
- 谁打断谁？
- 哪句台词造成关系位置变化？
- 压迫后哪个动作/物件/沉默承接？

### `/dialogue-polish`

当前能力：

- 表层话/真实目标。
- 句长和权力。
- 声线差异。
- 潜台词。
- 反应拍。
- 去 AI 味。
- 禁抄口径。

缺口：

- 它应该修台词，但不能承担生产强度的主责。
- 如果 `/episode` 写得太平，polish 容易为了不改剧情而降级成轻修。

建议：

```text
让 /episode 先吃 dialogue-force mode；/dialogue-polish 只负责二次校准，不当发动机。
```

### `/review`

当前能力：

- 质量评分。
- 责任层归因。
- 强节点适配复核。
- 本地化复核。
- 台词精修完成检查。

缺口：

- 不应把 review 变成质量发动机。
- 但必须能发现 `/dialogue-polish` 没真正执行、或正文完全没落实台词冲突模式。

建议：

```text
review 只做兜底验收和归因。
```

如果台词平：

- 角色武器表缺失：回 `/characters`。
- 分集没有台词冲突任务：回 `/outline`。
- 正文没执行：回当前 `/episode`。
- 只是表达软：回 `/dialogue-polish`。

### `/batch-state`

当前能力：

- 批次续写状态。
- 已释放/继续扣住。
- 关系状态。
- 真相债务。

缺口：

- 与当前“台词平”问题关系不大。

建议：

```text
暂不动。
```

### `/export`

当前能力：

- 清除施工层。
- 不改剧情台词。

缺口：

- 与写作能力关系不大。

建议：

```text
暂不动。
```

## 不建议接入的东西

不要整接：

- `oh-story/story-short-write`
- `oh-story/story-review`
- `oh-story/story-deslop`
- `oh-story/story-long-write`
- `how-to-make-script` 全仓
- `shortdrama-pipeline` writer prompt
- `dramatron`
- 找不到源码的 `ReelForge-YAML` / `duanju_create_agent`

原因：

```text
它们不是短剧洗稿主链本身。
整接会增加上下文、稀释主任务、引入小说/影视/工程流水线污染。
```

## 推荐后续产品化顺序

### 第一优先级：角色台词武器表

落点：`/characters`

来源：

- `how-to-make-script/voice-style-calibration`
- `wp-voice-style-guide`
- `ka-character-voice-consistency`
- `ka-verbal-rhythm`
- `ka-embodied-text-pressure`
- `oh-story/dialogue-mastery`

目标：

```text
让 writer 写正文前知道每个角色怎么用话伤人、躲责任、求信、心死、施压和失控。
```

### 第二优先级：`/episode` 台词冲突模式

落点：`/episode`

来源：

- `oh-story/dialogue-mastery`
- `oh-story/short-craft`
- 当前 `performance-dialogue-brief.md`
- 当前 `dialogue-polish-brief.md`

目标：

```text
不要等 polish 救台词。正文生成时就要带着这场戏的台词冲突模式写。
```

### 第三优先级：`/plan` 受众平台轻诊断

落点：`/plan`

来源：

- `how-to-make-script/audience-insight`
- `wp-audience-fit-note`
- `ka-audience-need-state`
- `oh-story/genre-readers`

目标：

```text
只回答目标观众为什么点开、为什么继续看、哪里会流失。
```

不要做市场报告，不要让它自动决定题材，更不要替用户拍板大方向。

## 最终判断

当前项目不是缺一套完整写作系统。

它已经有：

- 源本吸稿。
- 商业蓝图。
- 强节点适配。
- 出海本地化。
- 角色状态。
- 分集执行包。
- 正文生成。
- 台词精修。
- review 归因。
- 批次状态。
- 导出清理。

真正缺的是把外部资产里的三个能力接得更硬、更小、更短剧化：

```text
受众平台轻诊断 -> 角色台词武器表 -> episode 台词冲突模式
```

其中最先该做的是：

```text
角色台词武器表 + episode 台词冲突模式
```

因为这正中当前样本“剧情对，但台词太平”的根因。
