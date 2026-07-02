# 海外短剧洗稿器 · workflow spec v2

> 日期：2026-06-30
> 状态：当前执行版，需配合 `workflow_execution_protocol_v1.md` 留执行证据
> 对应产品定义：`PRD_v4.md`
> 上游审计：`PRD_v4_workflow_环节来源审计_2026-06-30.md`
> 用途：把 v1 中自建过重的中间表，替换为成熟项目已有产物链 + 最薄洗稿适配层

---

## 0. v2 总原则

v2 不推翻产品定义。

产品仍然是：

**把一个已被市场验证或值得参考的短剧源本，洗成一个新壳下仍然好看、能追、能付费的新剧本。**

v2 只调整执行方式：

```text
洗稿差异化层自己保留；
通用编剧层直接使用成熟产物；
不要再自造大表。
```

这里的“直接使用成熟产物”，不是只借名字。

必须同时继承对应产物的原生合同：

- `scene_draft / screenplay_draft`：场景必须有目标、行动和可读可演的剧本流；对白不能是裸对白，必须紧邻动作、表演、身体反应或空间压力。
- `dialogue_polish`：必须逐句处理表面意思、潜台词、角色声音和节奏，不能只做口语润色。
- `quality_gate_report`：先检查目标产物合同是否成立，再叠加洗稿项目自己的迁移检查。

最终交付正文不能出现 `Purpose / Action / Performance` 这类内部标签，但不能因此丢掉这些标签背后的约束。

### 0.1 必须保留的洗稿差异化层

| 层 | 必须回答 |
|---|---|
| 源本有效性迁移 | 源本为什么好看、为什么能追、为什么能付费 |
| 同构扣除 | 哪些源本事件外形、道具、证据、场景、台词不能复用 |
| 新壳等效承载 | 新壳下用什么场面、动作、关系变化承载同一体验 |
| 内部源本回指 | 新本关键场面内部能回到源本有效功能，但正文不复制源本外形 |
| 防洗飞 | 源本好看的节奏、钩子、情绪、关系功能不能丢 |
| 防改名复刻 | 不能只是换名字、身份、地点 |
| 防短剧降级 | 新事件不能变成文件、会议、冷对白、听证会 |

### 0.2 直接借成熟项目的通用编剧层

| 通用环节 | 使用来源 |
|---|---|
| 需求路由 | `short-drama /start` + `how-to-make-script routing` |
| 源本拆节点 | `oh-story 情节节点 / 拆文报告 / 写作手法` |
| 钩子、爽点、节奏 | `short-drama hook-design / satisfaction-matrix / rhythm-curve` |
| 骨架 | `beat_sheet / outline` |
| 场面 | `scene_card / scene_draft` |
| 正文 | `screenplay_draft / scene_draft` |
| 台词 | `dialogue_polish + expression lens` |
| 返修诊断 | `rewrite_report` |
| 自检 / reviewer | `quality_gate_report` |
| 连续性 | `story_memory_checkpoint / 角色状态 / 信息差 / 伏笔追踪` |
| 人工审核门 | `review gate` |

### 0.3 v2 的关键改变

v1 容易把写作前工作稿写成：

```text
必须揭露的信息
必须出现的证据
必须覆盖的剧情功能
```

v2 改成：

```text
场面目的
动作链
权力变化
关系变化
可见后果
卡点边界
禁止提前消费
```

核心口径：

**证据可以存在，但证据出现之后，人物必须被迫行动。**

### 0.4 不允许层级断裂

当前修正不增加主流程，不扩 PRD，不复活设计提纲。

它只修一个断点：

```text
源本分析出来的情绪、节奏、钩子、爽点、拉扯、角色状态
不能停在分析表或验收表里，
必须进入正文前的 episode map 和 scene packet，
再进入最终 screenplay。
```

判断一项分析是否真的被使用，不看它有没有出现在表格里，而看它有没有变成：

- 本集压力如何起、如何升、在哪里爆、在哪里停；
- 本场谁压谁、谁退、谁失控、谁被迫行动；
- 角色此刻的身体状态、遮掩状态、失控边缘；
- 爽点前的压低、看衰、误判、羞辱或危险；
- 钩子停住的最后画面、最后声音或最后动作。

如果源本高价值节点只在前文被分析，到了正文前只剩“某证据出现 / 某权限变化 / 某信息揭露”，就是层级断裂。

---

## 1. 总 workflow

```text
0. 最小需求确认
1. 读源本
2. 源本拆文包
3. 二次需求确认
4. 洗稿边界包
5. 新本 beat sheet / outline
6. 新壳场面迁移卡
7. Episode function map
8. Scene packet
9. Screenplay draft
10. Rewrite report
11. Dialogue polish
12. 作者 quality gate
13. Story memory checkpoint
14. 独立 reviewer quality gate + rewrite report
15. 主控对比 V3 / 上一版 / 本版
```

本文件的 `0-15` 是执行编号。

`PRD_v4.md` 里的 18 项是产品阶段说明，不作为 manifest 编号。

不要求每集每场都厚写。

高压节点厚写，过渡节点薄写。

---

## 2. 0. 最小需求确认

### 目标

先拿到足够开始读本子的最低信息，不要一开始把用户问爆。

### 必问

```text
任务类型：洗稿 / 改编 / 重写 / 诊断 / 审稿
源本：
新壳：
目标市场：
输出语言 / 审稿语言：
正文用途：AI 视频生成用剧本 / 人审稿 / 字幕台词版 / 双语版
集数是否变化：
本轮输出范围：
已知禁区：
```

### 输出语言默认

默认台词语言为英文，因为当前产品面向 AI 出海短剧。

但每次需求确认仍必须显式确认：

```text
台词默认英文，是否需要改成中文 / 中英双语？
动作行和场景描述使用中文、英文，还是中英双语？
本轮交付是给用户/导演审稿，还是直接进入 AI 视频生成链路？
```

如果用户没有特别指定，默认采用：

```text
英文对白 + 中文场景/动作描述 + 中文内部分析和审稿材料
```

### 当前样本默认

以下只用于当前样本验证；新项目按用户输入重填。

```text
任务类型：洗稿
源本：[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了
新壳：海外豪门商战 / 家族企业权力斗争
目标市场：海外短剧
集数：不变
本轮输出：首批 1-10 集
改写力度：中度偏重；不能只是换名，也不能丢源本有效性
```

---

## 3. 1-2. 源本拆文包

### 目标

不是复述剧情，而是把源本拆成下游能使用的节点、钩子、爽点、节奏、关系变化。

### 来源

- `oh-story`：情节节点、情绪强度、涉及人物、写作手法、原文锚点。
- `short-drama`：钩子、爽点、节奏、开场、反派、付费/留存。

### 输出结构

```text
源本拆文包

1. 一句话故事核
2. 核心期待
3. 首批 1-10 集分集功能
4. 高价值节点表
5. 钩子与卡点表
6. 爽点 / 压抑-释放表
7. 关系 / 权力变化表
8. 信息差与真相揭露路径
9. 写作手法 / 表达手法
10. 源本水分 / 烂点 / 禁止复用外形
```

### 高价值节点表字段

| 字段 | 说明 |
|---|---|
| 节点编号 | 集数 + 段落位置 |
| 客观事件 | 具体发生什么，不写抽象功能词 |
| 节点类型 | 冲突 / 情绪 / 信息 / 反转 / 打脸 / 关系质变 / 危机 |
| 情绪强度 | -9 到 +9，按源本体验判断 |
| 涉及人物 | 谁参与，谁旁观，谁不知道 |
| 写作手法 | 信息差、误会、死遁、推拉、打脸、危机钩等 |
| 观众体验功能 | 观众爽、痛、急、气、期待什么 |
| 关系/权力变化 | 谁压过谁，谁靠近/退开，谁失去主动权 |
| 信息差状态 | 观众、主角、反派分别知道什么 |
| 源本高辨识外形 | 不能照搬的事件、道具、证据、场景、台词 |

### 通过标准

- 不能只写“有反转、有钩子、有爽点”；
- 必须能回到具体节点；
- 必须能让下游知道：哪些体验要迁移，哪些外形要扣掉；
- 每个高价值节点必须写出“强度来源”：它靠什么让观众痛、爽、急、气、期待、拉扯；
- 每个高价值节点必须写出“下游写作抓手”：后续场面要保留的是压力、落差、误判、身体反应、当众后果、卡点位置，还是关系退/进。

---

## 4. 3. 二次需求确认

### 目标

读完源本后，再问真正会影响写作的取舍。

第一次需求确认只是开工许可。

第二次需求确认才决定写法。

### 用户必须回答

```text
1. 新壳 / 目标市场 / 改写力度；
2. 集数是否变化；
3. 用户最在意的保留点；
4. 用户明确禁区；
5. 必须出现的新壳元素；
6. 本轮输出范围。
```

### Agent 先判断，再给用户拍板

这些不是开放式甩给用户的问题。主控 / 主创先基于源本分析给出建议，再让用户确认：

```text
1. 新壳能不能承载源本最强节点；
2. 哪些源本事件外形必须避开；
3. 哪些体验强继承，哪些等效迁移，哪些自由改，哪些必须删；
4. 集尾钩子和付费/留存节点是否允许等效重排；
5. 如果用户需求和源本有效性冲突，优先方案是什么。
```

### 当前样本默认判断

```text
豪门商战版不允许只是改名字；
但也不是从零原创；
源本强留存、情绪压迫、追悔火葬场、女主反击、男女主拉扯必须迁移；
黑手党、绑架、枪战、源本高辨识事件链不能整串复用；
集数不变，关键留存节点原则上保持相似阶段。
```

---

## 5. 4. 洗稿边界包

### 目标

这是项目自有的最薄适配层。

### 输出结构

```text
洗稿边界包

必须保留的体验功能：
必须换掉的源本外形：
可以自由换的外壳变量：
必须删除 / 修复的烂点：
需要用户拍板的问题：
```

### 禁止

不要扩成全剧万能变量矩阵。

不要把“强继承”理解成照抄事件。

不要把“去同构”理解成丢掉源本好看的节奏、钩子、关系和情绪。

---

## 6. 5. 新本 beat sheet / outline

### 目标

先搭新本骨架，再进入单集和场面。

### 来源

- `how-to-make-script beat_sheet / outline`
- `short-drama /plan`
- Dramatron 分层生成顺序

### 输出结构

```text
新本 beat sheet / outline

Story Engine：
- 主角想要什么
- 阻碍是什么
- 利害关系是什么

Beat List：
- Beat 编号
- 对应阶段
- 新本事件
- 源本体验功能引用
- 局势变化
- 情绪弧变化
- 不可提前消费内容

Emotional Arc：
- 1-10 集情绪走势
- 拉扯/误会/追悔/反击如何递进
```

### 通过标准

- 不能只是剧情梗概；
- 每个 beat 必须改变局势、关系、信息或情绪；
- 必须标出不可提前消费的后续内容。

---

## 7. 6. 新壳场面迁移卡

### 目标

替代 v1 的“新事件载体迁移表”。

重点不是新证据是什么，而是新壳下如何形成一场可演、可看、能推进的短剧场面。

### 来源

- `scene_card`
- `scene_draft`
- `power_shift / visual_executability`
- `shortdrama-pipeline shot` 的“一个核心动作或情绪推进”

### 适用范围

只做高风险节点：

- 前 1-3 集；
- 每集结尾卡点；
- 强危机、强羞辱、强误会、强打脸；
- 身份揭露；
- 关系质变；
- 同构风险高的源本桥段；
- 上一版被导演/reviewer 指出的失败点。

### 输出结构

```text
新壳场面迁移卡

源本节点：
源本体验功能：
源本禁止外形：
新场景目的：
新冲突动作链：
  1. 起手动作：
  2. 压迫升级：
  3. 第一次反击/反转：
  4. 不可逆后果：
权力变化：
关系变化：
信息差变化：
观众直接看到什么：
证据/文件/录音如何触发人物行动：
台词上限：
卡点停在什么动作/选择/后果前：
禁止提前消费：
同构风险：
场面降级风险：
结论：可进入 episode map / 需重建 / 放弃
```

### 通过标准

- 如果只是“放证据 -> 众人震惊 -> 反派否认 -> 再放证据”，不通过；
- 如果人物没有被迫行动，不通过；
- 如果权力/关系没有变化，不通过；
- 如果只能靠对白讲出情绪，不通过；
- 如果卡点已经把下一集核心爽点消费掉，不通过。

---

## 8. 7. Episode function map

### 目标

替代 v1 的分集功能表。

每集不是写“发生了什么”，而是写“这一集如何留住观众”。

### 来源

- `short-drama episode-directory`
- `hook-design`
- `rhythm-curve`
- `shortdrama-pipeline Episode`

### 字段

| 字段 | 要回答 |
|---|---|
| Episode | 第几集 |
| Title | 集标题 |
| Summary | 本集核心推进，1-2 句 |
| Opening Hook | 开头凭什么不被划走 |
| Core Friction | 本集主要摩擦/冲突 |
| Max Spike | 本集最大刺激点：爽、痛、气、急、反转、危机 |
| Change | 关系 / 局势 / 信息 / 情绪至少哪一项改变 |
| End Button | 结尾钩子，停在答案前一拍 |
| Source Function Ref | 对应源本追看功能，不是源本事件外形；高价值节点必须写源本节点编号 |
| Forbidden Shape | 本集不能复用的源本外形 |
| Do Not Consume | 本集绝不能提前消费的后续内容 |
| Pressure Progression | 本集压力如何从开头推到最大刺激点：起压 / 升压 / 爆点 / 收住 |
| Carry-through From Source | 源本节点编号 -> 本集压力推进；说明被带下来的强度：节奏、情绪密度、爽点、拉扯、钩子、关系压力 |

### 通过标准

- 每集必须有 `Max Spike`；
- 每集必须有 `End Button`；
- 每集必须有 `Do Not Consume`；
- 高压集必须有 `Pressure Progression`，不能只写一条 `Max Spike`；
- `Carry-through From Source` 不能只回指源本事件名，必须说明“源本节点 -> 本集可见压力推进”的对应关系；
- 连续两集不能只是同一种场面形态重复。

---

## 9. 8. Scene packet

### 目标

替代 v1 的“单集写作包”。

Scene packet 是正文前给 writer 的真正输入。

它不是我们自造的一张新表，而是：

```text
洗稿薄适配信息 + 高压节点短剧节拍 + scene_draft 可执行剧本块
```

洗稿薄适配信息只回答“这一场从源本迁移什么、避开什么”。

高压节点短剧节拍只回答“这一场怎么把分析出的强度写出来”。

可执行剧本块必须按 `scene_draft` 的原生合同准备：场景目标、行动、可演对白、表演/身体/空间承载。

### 来源

- `scene_card`
- `scene_draft`
- `screenplay_draft`

### 单集 scene packet 结构

```text
Episode N Scene Packet

上一集结束状态：
本集 Opening Hook：
本集目标：
本集 Source Function Ref：
本集 Max Spike：
本集 End Button：
本集 Do Not Consume：
本集 Pressure Progression：
本集 Carry-through From Source：

Scene Sequence：

Scene 1
每场必填：
- Scene：
- Source Function Ref：
- Forbidden Shape：
- Scene Objective：
- Characters：
- Location：
- Starting State：
- Action Chain：
- Relationship / Power Shift：
- Exit State：
- End Button / Do Not Consume：

高压场追加：
- Source Strength To Carry：源本节点编号 -> 本场要迁移的强度
- Character Pressure State：
- Short-drama Beat Chain：
  1. 可见动作 / 声音：
     角色身体或表演：
     压力变化：
     台词：可空，只留必要一句
  2. ...
- Script Blocks：
  - Action：
  - Dialogue：
  - Performance / Body / Space：
  - Action：
  - Dialogue：

Scene 2
...
```

### 通过标准

- writer 能只看这个包写本集；
- 不能只是一串必须出现的信息点；
- 每场必须有 `Scene Objective`、`Action Chain`、`Relationship / Power Shift` 和 `Exit State`；
- 高压场必须有 `Source Strength To Carry`、`Character Pressure State`、`Short-drama Beat Chain` 和 `Script Blocks`；
- `Short-drama Beat Chain` 必须拆到 writer 能直接写正文，每个节拍只推进一个动作或一个情绪压力；过渡场不硬填；
- 高压场不能只给“证据链 / 权限链 / 信息链”，必须给“人物被迫行动链”；
- `Script Blocks` 不能只有 Dialogue；
- 关键对白不能裸奔，必须紧邻 `Action` 或 `Performance / Body / Space`；
- 每个证据、文件、录音、屏幕信息出现后，必须触发人物动作、权力变化或关系变化；
- 对白必须有功能：攻击、防守、逼迫、拒绝、试探、威胁、揭露、反击、选择；
- 角色状态不能只在写完后的 `story_memory_checkpoint` 里记录，高压场写作前就必须写清此刻身体/情绪/遮掩/失控边缘；
- 如果一场戏只是重复上一场的信息，删或合并。

---

## 10. 9. Deliverable screenplay draft

### 目标

把内部 `scene packet` 写成真正可读、AI 生成链路可视化可执行、可交付的剧本正文。

核心合同：**正文页上写出来的东西，应该基本等于最终 AI 成片里能看见和听见的东西。**

正文不是剧情说明，也不是给后续环节脑补的提示词。动作、声音、物件、身体反应、空间变化和人物可见状态，必须能直接落到画面和声音里；剧情功能、心理判断和作者意图不能替代这些可见内容。

这一环不是把 `Scene Objective / Action / Performance / End Button` 等字段展开成说明书，而是把这些内部判断消化成画面、行动、声音、人物反应和对白。

这不是新增一轮 screenplay-clean，也不是先写说明书再清洗。第 9 步产出的第一版正文就必须是剧本正文。

### 来源

- `screenplay_draft`
- `scene_draft`
- `short-drama /episode`
- `output-format-contracts.md` 中 `screenplay_draft` 的原生合同

### 输出层边界

`scene packet` 是内部写作包；`screenplay draft` 是最终正文。两者不能混在一起。

最终正文禁止出现以下内部字段：

- `Purpose`
- `Action`
- `Performance`
- `Dialogue Functions`
- `Source Function Ref`
- `Evidence triggers what action`
- `Hook Type`
- `Keywords`
- `End Button`
- `Do Not Consume`

这些字段只留在写作前工作稿、作者自检或 reviewer 报告里，不能进入正文。

但字段名删除，不等于约束删除。

正文必须让读者直接看见：

- 角色此刻的身体状态；
- 空间压力或环境压力；
- 对白前后发生了什么动作；
- 这句对白如何改变局势、关系或人物状态。

正文必须消化 `Short-drama Beat Chain`。

不要求把每个节拍写成镜头编号，但高压场里每个关键节拍都必须能在正文里找到对应的动作、声音、身体反应、空间压力或当众后果。

### Beat survival check

Screenplay draft 完成后，作者必须抽查本批最重要的高压节点，证明：

```text
源本节点编号 -> Scene packet 节拍 -> 正文中的具体动作 / 声音 / 身体反应 / 当众后果
```

如果节拍只剩对白解释、结果陈述或文件/屏幕信息，必须退回 scene packet 或 screenplay draft。

### screenplay 正文格式

用 Hollywood screenplay 的基本写法做正文基准，但不追求 Final Draft 分页精确度。

好莱坞剧本格式和“每场写清楚画面里发生什么”不矛盾。这里使用它作为正文容器：场景标题、动作行、人物名、台词、必要声音和屏幕文字。

这里借用好莱坞格式的核心不是排版，而是 page-to-screen：剧本里写了什么，最终画面和声音里就应该基本出现什么。区别是本项目服务 AI 出海短剧，所以动作行必须写到 AI 能生成画面，不能只给后续 AI 视频链路留想象空间。

```text
# Episode N: Title

INT. / EXT. LOCATION - DAY / NIGHT

可被观众看见或听见的动作、环境、物件、身体反应、空间变化。
每段动作行尽量短，只写正在发生的事情，不写作者解释。

CHARACTER
(必要时才写简短括号提示)
默认英文台词，除非需求确认指定中文或双语。

SFX: 必要声音。
ON SCREEN: 必要屏幕文字。

INT. / EXT. NEXT LOCATION - DAY / NIGHT
...
```

### 写法硬要求

- 动作行只写画面里能看见、听见、AI 能生成的东西；不能写“她很痛苦”“他终于意识到”“这一场建立关系反转”这类内心或功能说明；
- 情绪必须落到可视化行为：停顿、退后、抓住、推开、跪下、撕毁、摔碎、失手、失控、旁人反应、空间压迫、当众后果；
- 关键对白不能裸奔。每段关键对白前后必须有动作、表演、身体状态、空间变化或他人反应承接；
- 重要场面不能靠文件、会议、冷对白完成；文件和对白可以存在，但必须触发观众能直接看到的行动或局势变化；
- 每个高压场景必须有清楚的行动链：谁逼谁、谁退、谁反击、谁失去东西、谁获得权力；
- 台词要短、准、有功能；不能用多轮低信息对白解释剧情；
- 不要用镜头术语堆砌导演指令，除非这个镜头本身就是钩子或信息揭露；
- 每集结尾必须停在一个 AI 能生成的最后画面、最后声音或最后动作上，不得把 `Do Not Consume` 的答案提前说完。

### 内部字段到正文的转换方式

| 内部字段 | 正文里怎么处理 |
| --- | --- |
| Scene Objective | 删除，不出现在正文；只用于选择该场动作 |
| Action | 改写成连续可拍动作 |
| Performance / Body / Space | 融进动作行，不保留字段名 |
| Dialogue Functions | 改成具体台词，台词不解释功能 |
| End Button | 变成集尾最后画面 / 声音 / 动作 |
| Do Not Consume | 不写进正文，只作为不要提前消费的边界 |

### 不合格信号

- 正文看起来像说明书、流程单、审稿表；
- 场景里反复出现“Purpose / Action / Performance”之类标签；
- 读者能看懂作者想表达什么，但想象不出画面怎么拍；
- 人物说了痛苦、愤怒、崩溃、冷漠、心软，但正文没有给出身体状态、动作、空间或他人反应；
- 人物只站着轮流说话，动作只服务于“补充描写”，没有推动权力、关系或局势；
- 高压节点主要靠“报告显示、文件证明、某人解释”完成；
- 结尾写成概念钩子，而不是一个具体可拍的最后瞬间。

---

## 11. 10. Rewrite report

### 目标

初稿后先诊断坏在哪层，不要直接润色。

### 来源

- `rewrite_report`

### 输出结构

```text
Rewrite Report

Failure Layer：
- concept / structure / scene / dialogue / continuity / adaptation

Root Symptoms：
- 至少 2 条

Prioritized Actions：
- 先改什么
- 后改什么

Classification：
- must-restructure
- suggested
- observable-risk
```

### 通过标准

如果问题在 scene，不允许只做 dialogue polish。

如果问题在 adaptation，不允许只补动作描写。

---

## 12. 11. Dialogue polish

### 目标

只处理台词和表达，不拿它修结构。

这一环使用 `dialogue_polish` 的原生合同，不是泛泛“润色台词”。

它必须把每句问题台词拆成：目标台词、表面意思、潜台词、声音调整、节奏调整。

### 来源

- `dialogue_polish`
- `expression lens`

### 检查点

```text
这句台词是否应该存在，还是应该删掉并改成动作/表演/停顿/空间压力？
每句台词的功能是什么？
表面意思是什么？
潜台词是什么？
角色声音是否区分？
有没有解释性桥段？
有没有完整句病？
有没有情绪标签句？
有没有所有人都像同一个 AI？
连续两三轮对白是否有新信息、新压力或新关系变化？
```

### 输出

输出结构：

```text
Dialogue Polish

Target Lines：
Subtext Benchmarks：
Voice Adjustments：
Rhythm Notes：
Revised Lines / Cut Lines：
```

只改：

- 水词；
- 解释腔；
- 情绪标签句；
- 同声台词；
- 低信息多轮对话；
- 明明能用动作/表演表达却用嘴说的句子。

Dialogue polish 不能只把长句改短。

如果一场戏的问题是“人物没有被压迫到行动 / 情绪没有外化 / 节奏没升起来”，必须退回 scene packet 或 screenplay draft 修，不允许只在台词层硬润色。

---

## 13. 12. 作者 quality gate

### 目标

作者自检改成正式质量门。

### 来源

- `quality_gate_report`
- adaptive quality checking
- `check-lens-matrix.json` 的 `bundle.narrative-scene-dialogue`

### 输出结构

```text
Quality Gate Report

Target Contract & Scope：
Selected Lenses & Rationale：
Carry-through Evidence：
Hard Fails：
Weighted Weaknesses：
Correction Ladder：
Recheck Plan：
```

### 必选 lenses

| Lens | 看什么 |
|---|---|
| contract_fit | `scene_draft / screenplay_draft / dialogue_polish` 的原生合同是否成立 |
| mechanics_pressure | 场景压力、行动推进、权力变化是否成立 |
| continuity_invariants | 关系、信息差、伏笔、证据、角色状态是否接得住 |
| expression_integrity | 台词、表达、AI 味、角色声音是否成立 |
| adaptation_fit | 有没有洗飞 / 改名复刻 / 短剧降级 |
| carry_through_integrity | 源本拆文包里的情绪、节奏、钩子、爽点、拉扯、角色状态是否真的进入了 episode map、scene packet 和正文 |

执行顺序：

1. 先查 `contract_fit`。如果剧本正文没有达到剧本产物合同，不允许用“剧情逻辑对”放行。
2. 再查 `adaptation_fit`。如果源本有效性洗飞或只是改名复刻，不允许用“写得更顺”放行。
3. 再查 `carry_through_integrity`。如果分析层有的强度，正文层只剩机制、证据或信息，必须返修到 scene packet。
4. 最后查表达、连续性和局部弱项。

### 硬失败

以下情况不能 pass：

- 源本高价值节点在拆文包里写了情绪/节奏/爽点/钩子，但新本正文只落成机制事件；
- Episode function map 有 `Max Spike`，但 scene packet 没有压力推进链；
- Scene packet 有 `Script Blocks`，但高压场没有角色压力状态和短剧节拍；
- 正文逻辑正确，但高压节点主要靠文件、会议、屏幕、解释对白完成；
- dialogue polish 只改句子，没有判断哪些对白应该删掉或动作化。

`Carry-through Evidence` 只列本批高价值节点，不扩成全量大表。每条必须能追到：

```text
源本节点编号 -> episode map -> scene packet -> screenplay 正文锚点
```

---

## 14. 13. Story memory checkpoint

### 目标

每批写完保存可继续状态。

### 来源

- `oh-story` 追踪文件
- `story_memory_checkpoint`

### 输出结构

```text
Story Memory Checkpoint

关系状态：
信息差状态：
伏笔 / 证据状态：
角色状态：
未兑现承诺：
禁止下批提前消费：
下一批安全入口：
```

### 规则

只做 delta 更新。

不要重写全部分析。

---

## 15. 14. 独立 reviewer

### 目标

干净 reviewer 不读作者自检，先独立审。

### 来源

- `quality_gate_report`
- `rewrite_report`

### 输入

Reviewer 分两段审，避免被作者意图带偏。

第一段只读：

- 用户需求；
- PRD v4 验收标准；
- 首批修订稿。

先判断正文效果：

- 像不像短剧；
- 淡不淡；
- 能不能追；
- 有没有改名复刻、剧情说明书、站桩聊天、证据链代替场面。

第二段再读定位材料：

- 用户需求；
- 源本拆文包；
- 洗稿边界包；
- 新本 beat sheet / outline；
- 新壳场面迁移卡；
- Episode function map；
- Scene packet；
- 首批修订稿；
- PRD v4 验收标准。

Reviewer 第一轮不要读：

- 作者 quality gate；
- 作者解释；
- 旧外部反馈；
- 旧版正文。

### 输出

```text
Reviewer Quality Gate
Reviewer Rewrite Report
结论：pass / revise / block
```

Reviewer 必须指出失败层，不能只说“加强视听语言”。

Reviewer 不能只验证剧情逻辑和产物格式。

必须单独判断：

- 源本拆文包里的强度有没有被带到正文；
- Episode function map 的压力推进有没有进入 scene packet；
- Scene packet 的短剧节拍有没有进入 screenplay；
- 如果没有，失败层是 source analysis / episode map / scene packet / screenplay / dialogue polish / quality gate 哪一层。

---

## 16. 15. 版本对比

### 目标

如本轮有旧版参照，必须比较：

1. 用户指定基线；
2. 上一轮交付版。

当前样本验证中，用户指定基线是 V3；上一轮交付版按本轮实际版本填写。

### 比较维度

| 维度 | 判断 |
|---|---|
| 源本有效性 | 有没有比基线 / 上一版更洗飞 |
| 同构风险 | 有没有比基线 / 上一版更像改名 |
| 短剧场面 | 高压节点是不是更能演、更能看 |
| 动作链 | 是否减少证据播报和站桩聊天 |
| 台词 | 是否减少水词、解释腔、同声 |
| 钩子 / 卡点 | 是否更准，是否避免提前消费 |
| 拉扯 / 关系 | 男女主、主反关系是否更有压迫、靠近、退开、误会、试探 |
| continuity | 关系、信息差、伏笔是否更稳 |
| 读感 | 是否至少不低于基线 |

### 结论格式

```text
本版 vs 用户指定基线：
本版 vs 上一版：
本版进步：
本版退步：
是否允许进入用户 review：
下一步：
```

---

## 17. 样本专属信息

样本角色名、具体集数失败点、V3/V4/V8 对比和导演旧反馈不写进通用 workflow。

当前样本的输入、基线和已知失败点放在：

`样本验证/飞书三星样本/当前样本测试夹具.md`
