# 海外短剧洗稿器 · workflow spec v10 V3/V5 完整回收候选版

> 日期：2026-07-01  
> 状态：候选 workflow，待样本验证。  
> 上游产品定义：`PRD_v4.md`  
> 合并依据：`V3_V5完整对读与合并方案_2026-07-01.md`  
> 执行协议：必须配合 `workflow_execution_protocol_v1.md`，manifest-first。  

---

## 0. 这版解决什么

这版不重新定义产品。

产品仍然是：

```text
把已被市场验证或值得参考的短剧源本，
洗成一个新壳下仍然好看、能追、能付费的新剧本。
```

这版修的是之前的抽取错误：

```text
不能只抽 V3 的“方向”；
不能只抽 V5 的“关键场面卡”；
不能只抽当前版的“执行纪律”。
```

正确做法是按能力项回收：

| 来源 | 回收什么 | 不回收什么 |
|---|---|---|
| V3 | 源本有效性、迁移义务、同构红线、新壳承载判断、商战稳态 | 高同构开场、证据听证会、商业权限开挂 |
| V5 / workflow v2 | 多条内容链路、源本拆文包、Episode map、Scene packet、Story memory | 正文内部标签、枪响默认解、复杂规则解释 |
| 当前执行协议 | manifest、干净 reviewer、版本对比、不能口头冒充完成 | 用执行证明替代创作 |
| V18 / v8 | 失败证据：多条内容链路被抽薄后会写成程序感 | 不当主链 |

---

## 0.1 本版必须同时保住的多条链路

本版不是“找到一条有效链路就算 OK”。

每次跑 workflow，都要把以下链路从源本分析带到正文和 reviewer：

| 链路 | 源本分析看什么 | 写作前怎么承接 | 正文里怎么体现 | reviewer 怎么查 |
|---|---|---|---|---|
| 留存 / 钩子 / 卡点链 | 源本每集为什么让人继续看 | Episode map 的 Opening Hook / End Button / Do Not Consume | 每集最后一个具体画面、声音或动作停在答案前 | 卡点是否说完、是否没气口 |
| 情绪 / 爽点 / 压抑释放链 | 痛、爽、气、急、打脸前压低和兑现 | Pressure Progression / Max Spike | 人物被压、被看衰、再反击或被反噬 | 是否只有结果，没有蓄力和释放 |
| 主线期待 / 信息差链 | 观众等哪层真相，谁知道谁不知道 | Beat / Episode map 的信息释放边界 | 真相分层揭，不提前吃掉后续火葬场 | 信息是否空转或一次说完 |
| 人物关系 / 拉扯链 | 谁靠近、谁退、谁误会、谁试探、谁压迫 | Story state / Scene packet 的 Starting state 和 Relationship shift | 对话、动作和选择改变关系距离 | 是否角色很冷、关系没变 |
| 权力变化 / 打脸链 | 谁从高位跌下，谁被夺走什么 | Action chain / Power shift | 当众失去身份、资源、控制权、体面 | 是否只是口头赢了 |
| 同构扣除 / 新壳承载链 | 哪些外形不能复用，哪些体验必须保 | 洗稿边界包 / 迁移卡 | 新壳里发生同等强度的新场面 | 是否改名复刻或避同构洗飞 |
| 场面动作链 | 强节点靠什么动作和现场后果成立 | Scene packet / Script blocks | 证据、文件、录音触发人行动 | 是否证据播报、站桩聊天 |
| 正文表达链 | 源本的可看可听表达方式 | Screenplay contract | 干净剧本正文，不带内部字段 | 是否像说明书或流程单 |
| 连续性 / 伏笔链 | 信息差、伏笔、角色状态如何推进 | Story memory / Do Not Consume | 不让角色状态回退，不乱提前兑现 | 后续是否接得住 |

这些链路不是新增 9 个大表。

它们是同一批产物的不同读法。缺一条，可能会出现：结构对但不吸睛、反同构对但洗飞、动作多但关系冷、钩子有但爽点没蓄力、正文像剧本格式但不像短剧。

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
14. 独立 reviewer
15. 主控版本对比
```

这条链基本沿用 `workflow_spec_v2.md`。

本版不是只改三件事；更准确是修三个连接口：

1. V3 的洗稿护栏必须进入 Step 4 / Step 5 / Step 15；
2. V3 / V5 的多条内容链路必须进入 Step 7 / Step 8 / Step 9；
3. 最终正文必须是干净 screenplay，不能带内部工作标签。

---

## 2. Step 0. 最小需求确认

目标：拿到足够开工的信息，不一开始把用户问爆。

必确认：

```text
任务类型：洗稿 / 改编 / 重写 / 诊断 / 审稿
源本：
新壳：
目标市场：
集数是否变化：
改写力度：
本轮输出范围：
输出语言 / 审稿语言：
正文用途：AI 视频生成用剧本 / 人审稿 / 字幕台词版 / 双语版
已知禁区：
```

默认：

```text
台词英文；
动作和场景描述中文；
内部分析中文；
目标是 AI 出海短剧剧本文字。
```

但必须显式问一句：

```text
台词默认英文，是否需要改成中文 / 中英双语？
动作行和场景描述用中文、英文，还是双语？
本轮交付是给导演审稿，还是直接进入 AI 视频生成链路？
```

---

## 3. Step 1-2. 源本拆文包

目标：不是复述剧情，而是拆出源本为什么好看、为什么能追、为什么能付费。

必须输出：

```text
源本拆文包

1. 一句话故事核
2. 核心期待
3. 首批分集功能
4. 高价值节点
5. 钩子与卡点
6. 爽点 / 压抑-释放
7. 关系 / 权力变化
8. 信息差与真相路径
9. 写作手法 / 表达手法
10. 水分 / 烂点 / 禁止复用外形
```

每个高价值节点必须写：

```text
客观事件：
观众体验功能：
强度来源：
关系 / 权力变化：
信息差状态：
卡点停法：
源本高辨识外形：
下游写作抓手：
```

这里要特别防止两个错误：

1. 只写“这个节点是反转 / 爽点 / 钩子”，不写它靠什么成立；
2. 写完后不传给后面的 episode map 和 scene packet。
3. 只传场面动作，不传留存、情绪、关系、信息差和权力变化。

通过标准：

```text
下游能知道：保什么体验、避什么外形、在哪里停、谁压谁、观众为什么想看下一集。
```

拆文包完成后，要给出一张“链路摘要”，只写短句，不扩成大表：

```text
本源本首批的留存链：
本源本首批的情绪 / 爽点链：
本源本首批的关系 / 拉扯链：
本源本首批的信息差链：
本源本首批的权力变化链：
本源本首批最危险的同构外形：
```

---

## 4. Step 3. 二次需求确认

目标：读完源本后，再决定真正影响写作的取舍。

主创先判断，再让用户拍板。

必须确认：

```text
新壳是否能承载源本最强追看机制；
本轮改写力度；
哪些体验必须强继承；
哪些事件外形必须换；
哪些变量可自由改；
哪些烂点必须删；
集数变化时，留存阶段如何等效重排；
用户特别想保留或避开的东西。
```

如果用户需求会削弱源本有效性，必须直接说。

不要把问题全甩给用户。

---

## 5. Step 4. 洗稿边界包

目标：把源本拆文压成薄边界，防止 writer 既洗飞又复刻。

输出：

```text
必须保留的体验功能：
必须避开的源本外形：
可以自由换的外壳变量：
必须删除 / 修复的烂点：
新壳承载风险：
本轮用户拍板项：
```

这里继承 V3 的能力：

- 迁移义务；
- 同构红线；
- 新壳承载判断；
- 阶段骨架意识。

禁止：

- 恢复成大变量矩阵；
- 把强继承理解成照抄事件；
- 为了避同构，把源本好看的钩子、节奏、关系和情绪洗掉。

---

## 6. Step 5. 新本 beat sheet / outline

目标：先搭新本骨架，再进入单集。

输出：

```text
Story Engine：
- 主角想要什么
- 阻碍是什么
- 赌注是什么
- 观众追什么

Beat List：
- Beat 编号
- 新本事件
- 源本体验功能引用
- 局势变化
- 关系变化
- 情绪变化
- 不可提前消费内容

Emotional / Retention Arc：
- 1-10 集情绪走势
- 爽点蓄力和兑现
- 男女主拉扯 / 误会 / 追悔如何递进
- 每个阶段的追问

Multi-chain Carry：
- 留存链如何从源本等效迁移
- 情绪 / 爽点链如何蓄力和兑现
- 关系 / 拉扯链如何推进
- 信息差链如何分层释放
- 权力变化链如何变成可见后果
```

通过标准：

- 不能只是剧情梗概；
- 每个 beat 必须改变局势、关系、信息或情绪；
- 必须标出不可提前消费；
- 必须保留源本留存阶段惯性，但不机械照抄秒点。

---

## 7. Step 6. 新壳场面迁移卡

目标：把源本高价值节点迁成新壳里可演、可看、能推进的短剧场面。

只做高风险节点：

- 前 1-3 集；
- 每集结尾卡点；
- 强羞辱、强危机、强误会、强打脸；
- 身份揭露；
- 关系质变；
- 同构风险高的源本桥段；
- 上一版导演 / reviewer 指出的失败点。

输出：

```text
源本节点：
源本体验功能：
源本禁止外形：
新场景目的：
新冲突动作链：
  1. 起手动作：
  2. 压迫升级：
  3. 第一次反击 / 反转：
  4. 不可逆后果：
权力变化：
关系变化：
信息差变化：
观众直接看到什么：
证据 / 文件 / 录音如何触发人物行动：
台词上限：
卡点停在什么动作 / 选择 / 后果前：
禁止提前消费：
同构风险：
场面降级风险：
结论：可进入 episode map / 需重建 / 放弃
```

通过标准：

- 如果只是“放证据 -> 众人震惊 -> 反派否认 -> 再放证据”，不通过；
- 如果人物没有被迫行动，不通过；
- 如果权力 / 关系没有变化，不通过；
- 如果只能靠对白讲出情绪，不通过；
- 如果卡点已经把下一集核心爽点说完，不通过。

注意：

```text
场面迁移卡是高压节点工具，不是全剧主轴。
它不能挤掉源本拆文、钩子、爽点、关系、信息差和 episode map。
```

---

## 8. Step 7. Episode function map

目标：每集写“如何留住观众”，不是只写“发生了什么”。

字段：

| 字段 | 要回答 |
|---|---|
| Episode | 第几集 |
| Title | 集标题 |
| Summary | 本集核心推进，1-2 句 |
| Opening Hook | 开头凭什么不被划走 |
| Core Friction | 本集主要摩擦 / 冲突 |
| Max Spike | 本集最大刺激点 |
| Change | 关系 / 局势 / 信息 / 情绪至少哪一项改变 |
| End Button | 结尾钩子，停在答案前一拍 |
| Source Function Ref | 对应源本追看功能，不是源本事件外形 |
| Forbidden Shape | 本集不能复用的源本外形 |
| Do Not Consume | 本集绝不能提前消费的后续内容 |
| Pressure Progression | 起压 / 升压 / 爆点 / 收住 |
| Carry-through From Source | 源本节点如何进入本集压力推进 |
| Chain Carry | 本集承接哪几条链：留存 / 情绪爽点 / 关系拉扯 / 信息差 / 权力变化 |

通过标准：

- 每集必须有 `Max Spike`；
- 每集必须有 `End Button`；
- 每集必须有 `Do Not Consume`；
- 高压集必须有 `Pressure Progression`；
- `Carry-through From Source` 不能只写源本事件名，必须写源本强度如何变成本集压力；
- `Chain Carry` 不能每集都泛写全选，必须写本集真正承担的 2-4 条主链；
- 连续两集不能只是同一种场面形态重复。

---

## 9. Step 8. Scene packet

目标：给 writer 真正能写正文的输入。

Scene packet 不能是审计表，不能是证明清单。

它应该告诉 writer：

```text
这一集从什么状态进；
谁压谁；
谁想靠近 / 逃开 / 遮掩 / 反击；
压力怎么升；
什么东西被当众夺走、暴露、截断或反转；
关系和权力怎么变；
最后停在哪个可拍瞬间。
```

它还要告诉 writer：

```text
这一集主要承接哪几条链；
哪一条不能丢；
哪一条只是背景，不能抢戏。
```

### 单集结构

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
本集 Chain Carry：

Scene Sequence：

Scene 1
- Scene：
- Source Function Ref：
- Forbidden Shape：
- Scene Objective：
- Characters：
- Location：
- Starting State：
- Action Chain：
- Relationship / Power Shift：
- Chain Function：本场主要服务哪条链
- Exit State：
- End Button / Do Not Consume：
```

### 高压场追加

```text
Source Strength To Carry：
Character Pressure State：
Short-drama Beat Chain：
  1. 可见动作 / 声音：
     角色身体或表演：
     压力变化：
     台词：可空，只留必要一句
  2. ...
Script Blocks：
  - Action：
  - Dialogue：
  - Performance / Body / Space：
  - Action：
  - Dialogue：
```

通过标准：

- writer 能只看这个包写本集；
- 每场有 `Scene Objective`、`Action Chain`、`Relationship / Power Shift`、`Exit State`；
- 每场必须知道自己主要服务哪条链，不允许所有场都写成同一种“揭露 / 震惊 / 反击”；
- 高压场有 `Character Pressure State`、`Short-drama Beat Chain`、`Script Blocks`；
- Script Blocks 不能只有 Dialogue；
- 每个证据、文件、录音、屏幕信息出现后，必须触发人物动作、权力变化或关系变化；
- 如果一场戏只是重复上一场的信息，删或合并。

---

## 10. Step 9. Screenplay draft

目标：写成真正可读、可视化、可给 AI 生成链路使用的剧本正文。

核心合同：

```text
正文页上写出来的东西，应该基本等于最终 AI 成片里能看见和听见的东西。
```

正文不能出现内部字段：

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

但字段背后的约束必须被消化进正文。

### 正文格式

用 Hollywood screenplay 的基本写法做正文容器，不追求 Final Draft 分页。

```text
# Episode N: Title

INT. / EXT. LOCATION - DAY / NIGHT

可被观众看见或听见的动作、环境、物件、身体反应、空间变化。
每段动作行尽量短，只写正在发生的事情，不写作者解释。

CHARACTER
(必要时才写简短括号提示)
英文台词，除非需求确认指定中文或双语。

SFX: 必要声音。
ON SCREEN: 必要屏幕文字。
```

### 写法要求

- 动作行只写画面里能看见、听见、AI 能生成的东西；
- 情绪必须落到可视化行为、身体反应、空间压力或当众后果；
- 关键对白不能裸奔，前后必须有动作、状态、空间或他人反应承接；
- 重要场面不能靠文件、会议、冷对白完成；
- 文件和对白可以存在，但必须触发观众能直接看到的行动或局势变化；
- 每个高压场景必须有行动链：谁逼谁、谁退、谁反击、谁失去东西、谁获得权力；
- 台词短、准、有功能，不用多轮低信息对白解释剧情；
- 每集结尾停在具体可拍的最后画面、声音或动作上。

### Beat survival check

正文完成后，作者只抽查 3-5 个最高风险节点：

```text
源本节点 -> Episode map -> Scene packet -> 正文中的动作 / 声音 / 身体反应 / 当众后果
```

这是抽查，不是全量证明大表。

如果节点只剩对白解释、文件展示或结果陈述，必须退回 Step 8 或 Step 9。

---

## 11. Step 10. Rewrite report

目标：先判断坏在哪层，不直接润色。

输出：

```text
Rewrite Report

Failure Layer：
- concept / structure / scene / dialogue / continuity / adaptation / carry-through

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

规则：

- 如果问题在 scene，不允许只做 dialogue polish；
- 如果问题在 adaptation，不允许只补动作描写；
- 如果问题是源本强度没传下来，必须回 Step 7 / Step 8。

---

## 12. Step 11. Dialogue polish

目标：只处理台词和表达，不拿它修结构。

检查：

```text
这句台词是否应该存在，还是应该删掉改成动作 / 表演 / 停顿？
每句台词的功能是什么？
表面意思是什么？
潜台词是什么？
角色声音是否区分？
有没有解释腔？
有没有情绪标签句？
有没有低信息多轮对白？
有没有明明能用动作表达却用嘴说？
```

如果一场戏的问题是人物没有被压迫到行动，必须退回 Step 8 / Step 9，不允许只润色台词。

---

## 13. Step 12. 作者 quality gate

输出：

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

必选 lens：

| Lens | 看什么 |
|---|---|
| contract_fit | 正文是不是剧本，不是说明书 |
| adaptation_fit | 有没有洗飞 / 改名复刻 / 短剧降级 |
| carry_through_integrity | 源本钩子、爽点、情绪、拉扯是否进了正文 |
| mechanics_pressure | 场景压力、行动推进、权力变化 |
| continuity_invariants | 关系、信息差、伏笔、角色状态 |
| expression_integrity | 台词、AI 味、角色声音 |

硬失败：

- 源本高价值节点在拆文包里写了强度，但正文只落成机制事件；
- Episode map 有 Max Spike，scene packet 没有压力推进；
- Scene packet 有 Script Blocks，正文没有动作 / 身体 / 空间承接；
- 正文逻辑正确，但高压节点主要靠文件、会议、屏幕、解释对白完成；
- Dialogue polish 只改句子，没有判断哪些对白应该删掉或动作化。

---

## 14. Step 13. Story memory checkpoint

目标：每批写完保存后续可继续状态。

输出：

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

只做 delta，不重写全部分析。

---

## 15. Step 14. 独立 reviewer

Reviewer 必须干净。

第一轮只读：

- 用户需求；
- PRD v4 验收标准；
- 首批正文。

先判断正文效果：

- 像不像短剧；
- 淡不淡；
- 能不能追；
- 有没有改名复刻；
- 有没有剧情说明书；
- 有没有站桩聊天；
- 有没有证据链代替场面。

第二轮再读：

- 源本拆文包；
- 洗稿边界包；
- beat sheet / outline；
- 新壳场面迁移卡；
- Episode function map；
- Scene packet；
- 首批正文；
- PRD v4 验收标准。

Reviewer 第一轮不要读：

- 作者 quality gate；
- 作者解释；
- 旧外部反馈；
- 旧版正文。

Reviewer 必须指出失败层：

```text
source analysis / beat-outline / episode map / scene packet / screenplay / dialogue polish / quality gate / adaptation
```

不能只说“加强视听语言”。

Reviewer 还必须判断哪条链断了：

```text
留存 / 钩子 / 卡点链
情绪 / 爽点 / 压抑释放链
主线期待 / 信息差链
人物关系 / 拉扯链
权力变化 / 打脸链
同构扣除 / 新壳承载链
场面动作链
正文表达链
连续性 / 伏笔链
```

如果只是局部台词差，回 Step 11。

如果是某条内容链没传到正文，回 Step 7 或 Step 8。

如果是新壳承载错，回 Step 4 或 Step 6。

---

## 16. Step 15. 主控版本对比

必须比较：

1. 用户指定基线；
2. 上一轮交付版；
3. 当前正向样本，如本项目当前至少应看 V3 / V5；
4. 本轮新稿。

比较维度：

| 维度 | 判断 |
|---|---|
| 源本有效性 | 有没有比基线更洗飞 |
| 同构风险 | 有没有比基线更像改名 |
| 短剧场面 | 高压节点是不是更能演、更能看 |
| 动作链 | 是否减少证据播报和站桩聊天 |
| 台词 | 是否减少水词、解释腔、同声 |
| 钩子 / 卡点 | 是否更准，是否避免提前消费 |
| 爽点 / 压抑释放 | 是否保住蓄力和兑现周期 |
| 拉扯 / 关系 | 男女主、主反关系是否更有压迫、靠近、退开、误会、试探 |
| continuity | 关系、信息差、伏笔是否更稳 |
| 正文形态 | 是否像剧本，而不是说明书 |
| 读感 | 是否至少不低于 V3 / V5 中较好的部分 |

结论格式：

```text
本版 vs 用户指定基线：
本版 vs 上一版：
本版 vs V3：
本版 vs V5：
本版进步：
本版退步：
是否允许进入用户 / 导演 review：
下一步：
```

---

## 17. 本候选版的禁区

不要把这版误用成：

- 从零原创短剧 workflow；
- 大表填空器；
- 只要 manifest complete 就算完成；
- 只要 reviewer pass 就算导演会满意；
- 只要有 page-to-screen 文字就算有画面感；
- 只要有动作就算短剧场面成立；
- 只要避开源本外形就算洗得好。

本项目的根仍然是：

```text
源本为什么让人追、让人付费；
新本是否把这股追看劲迁到了新壳里。
```

---

## 18. manifest 口径

任何使用本 spec 的运行，必须先建立：

```text
workflow_run_manifest_<版本号>_v10workflow.md
```

manifest 步骤按本文件 0-15。

没有 manifest，不能声称完整跑完。

manifest complete 只说明执行证据完整，不说明剧本质量 pass。
