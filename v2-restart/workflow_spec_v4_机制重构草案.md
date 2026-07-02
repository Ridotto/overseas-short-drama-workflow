# 海外短剧洗稿器 · workflow spec v4 机制重构草案

> 日期：2026-06-30  
> 状态：草案，不是当前执行版  
> 上游产品定义：`PRD_v4.md`  
> 前一草案：`workflow_spec_v3_重构草案.md`  
> 机制说明：`机制重构_根因与改法_2026-06-30.md`  
> 目的：在 v3 “分析 / 创作 / 审计 / 治理拆层”的基础上，补上故事当前状态和压力链生成法，避免 writer 继续拿结果任务单写戏。  

---

## 0. 本草案解决什么

v2 / v3 的流程骨架不是全错。它们已经做对了几件事：

```text
分析源本有效性
拆开分析 / 创作 / 审计 / 治理
减少 writer 看到的证明链
用独立 reviewer 判断正文效果
```

但 V13 / V14 暴露出更深一层问题：

```text
分析层读到了源本为什么好看
-> 下传给 writer 时仍容易变成“这一集要发生什么”的结果任务单
-> writer 为完成结果，选择文件、录音、屏幕、key、系统、董事会等安全载体
-> 返修时继续换道具、补动作、补身体反应
-> 剧本越来越像流程说明，而不是人物互相逼出来的短剧强戏
```

v4 不继续补“视听语言 / 身体反应 / 禁器械 / 拉扯感”等单条规则。

v4 只修四条机制：

1. **Source Retention Anchor 前置**：先锁住源本让用户继续付费的钩子、卡点、情绪密度、节奏、爽点和期待链；
2. **Story Operating State 前置**：写正文前，writer 必须知道故事当前活到哪儿了；
3. **Pressure-chain Writer Brief**：高压场不直接写正文，先写人物欲望、阻碍、误判、选择、代价的压力链；
4. **Pressure-chain Patch Brief**：返修不直接改正文，先把 reviewer note 改写成新的压力链。

v4 不是原创剧本生成法。  
压力链必须承接源本留存锚点，否则就是方向漂移。

---

## 1. 产品锚点

本项目仍然是：

**把一个已被市场验证或值得参考的短剧源本，洗成一个新壳下仍然好看、能追、能付费的新剧本。**

交付物是剧本文字，不是分析报告。

达标必须同时满足：

1. 没洗飞源本有效性；
2. 不是改名复刻；
3. 新本作为短剧自己站得住、能追、能付费。

本项目不是：

- 从零原创短剧生成器；
- 短剧标准库套模板工具；
- 评分器；
- 视频 / 分镜 / 成片工具；
- 把导演反馈拆成一百条规则的工具。

---

## 2. v2 已确认的问题

### 2.1 外部项目不是没用，是接法变形

外部资产本身有价值：

- `short-drama`：短剧钩子、爽点、节奏、分集功能；
- `oh-story`：拆文节点、情绪强度、人物关系、写作手法；
- `how-to-make-script`：`scene_draft / screenplay_draft / rewrite_report / dialogue_polish / quality_gate_report` 的产物合同；
- `shortdrama-pipeline / Jellyfish / AgentCine`：动作、空间、表演、可生产性参照；
- `Dramatron`：分层生成顺序。

但进入本项目后，这些能力被重新加权成：

- source ref；
- carry-through evidence；
- manifest pass；
- 反同构证明；
- 字段完整；
- 版本对比。

于是创作工具变成了流程证明工具。

### 2.2 writer 输入被审计材料污染

v2 把 `scene packet` 定义成 writer 的真正输入，但这个 packet 同时塞进了：

- 源本节点编号；
- Source Function Ref；
- Forbidden Shape；
- Carry-through From Source；
- Script Blocks；
- pass 需要的正文锚点。

这会让 writer 像审计员一样写作。

v3 的核心变化仍然保留：

**writer 不再读取完整审计底稿。writer 只读写作简报。**

v4 在此基础上继续收紧：

**writer 读到的简报必须是故事状态和压力链，而不是结果任务单。**

### 2.3 pass 语义混乱

v2 中经常出现：

- manifest pass；
- 作者质量门 pass；
- pass for challenge；
- reviewer pass；
- 版本对比“不低于上一版”。

这些 pass 不等价。

v4 继续拆开：

- 执行 pass；
- 写作简报 pass；
- 创作效果 pass；
- 源本迁移审计 pass；
- reviewer pass。

不能再互相背书。

### 2.4 返修默认变成加料

过去 12 版常见修法：

- 台词弱 -> 补台词优化；
- 视听弱 -> 补动作 / 身体；
- 情绪弱 -> 补血、手抖、崩溃；
- 机制感重 -> 再加“人物亲手按键”。

但坏骨架没有被拆掉。

v4 返修先判失败层，再决定是否需要压力链返修简报：

```text
场面发动机坏 -> 回写作简报 / 新壳场面重选
场面动作弱 -> 回 Pressure-chain Writer Brief / Screenplay Draft
台词水 -> dialogue polish
源本洗飞 / 同构 -> 回源本审计线
执行证据缺 -> 回 manifest / protocol
```

---

## 3. v4 总结构

```text
0. 最小需求确认
1. 源本分析底稿 Source Bible
2. 洗稿边界包 Adaptation Boundary
3. Source Retention Anchor / 源本留存锚点
4. Story Operating State / 写作前故事运行状态
5. 高压节点新场面粗验 High-pressure Scene Viability
6. 新本阶段骨架 / 分集功能 Episode Plan
7. Pressure-chain Writer Brief / 压力链写作简报
8. 干净 writer 正文 Screenplay Draft
9. 作者 rewrite report
10. Pressure-chain Patch Brief / 压力链返修简报
11. 作者 dialogue polish / 修订稿
12. 作者 ready check
13. Reviewer 第一轮：只读正文
14. Reviewer 第二轮：读审计底稿查洗飞 / 同构 / 降级
15. 主控判定失败层和回滚点
16. Story memory checkpoint
17. Manifest / 版本记录 / 交付
```

v4 不是增加规则，而是把“写作前应知道的故事状态”和“高压场如何生成”接到正确位置。

### 3.1 与 PRD v4 阶段概览的映射

PRD v4 仍是产品定义主文档。v4 workflow 草案只是把 PRD 里的产品阶段拆成更清楚的执行产物，不改变产品目标。

| PRD v4 阶段 | v4 workflow 对应产物 | 说明 |
|---|---|---|
| 需求对齐 | 最小需求确认 | 确认源本、新壳、目标市场、集数、禁区和用户偏好 |
| 源本有效性摘要 | Source Bible | 完整读源本为什么能追、能付费 |
| 源本事件载体拆解 | Source Bible 高价值节点 / 禁止外形 | 拆源本靠什么事件、场面、证据、动作、人戏成立 |
| 变量迁移策略 | Adaptation Boundary | 压成必须保留、必须替换、自由改写、删除修复 |
| 新事件载体迁移 | High-pressure Scene Viability | 判断新壳能否承载源本高压节点 |
| 正文前策略审核 | Source Retention Anchor + Story Operating State + High-pressure Scene Viability | 写前先看是否洗飞、是否原创漂移、是否场面发动机错误 |
| 洗稿方案给用户确认 | Adaptation Boundary + Episode Plan 摘要 | 给用户确认方向，不暴露完整审计底稿 |
| 新本阶段骨架 | Episode Plan | 控制首批留存闭环和阶段比例 |
| 分集功能表 | Episode Plan | 保证每集有开头、摩擦、刺激点、变化、结尾钩子 |
| 关键场面草案 | High-pressure Scene Viability + Pressure-chain Writer Brief | 只厚写高风险节点 |
| 状态追踪初始化 | Story Operating State | 写前故事运行状态 |
| 单集写作包 | Pressure-chain Writer Brief | writer 真正输入，薄而可写 |
| 首批正文初稿 | Screenplay Draft | 剧本文字 |
| 正文后短剧化返修 | Rewrite Report + Pressure-chain Patch Brief + Dialogue Polish | 先判失败层，再决定是否改压力链、正文或台词 |
| 作者自检 | Author Ready Check | 作者只能给 ready / needs rewrite / blocked |
| 独立 reviewer 分层审稿 | Reviewer 第一轮 + 第二轮 | 第一轮看正文效果，第二轮查源本迁移 |
| 主控汇总交付 | 主控判定 + Manifest / 版本记录 | 拆开 execution / creative / source_audit / continuity / delivery |

---

## 4. 四条线

### 4.1 分析线

服务对象：主控、审计、写作简报生成者。

不直接服务 writer。

产物：

- `Source Bible / 源本分析底稿`
- `Adaptation Boundary / 洗稿边界包`
- `Source Retention Anchor / 源本留存锚点`
- `Story Operating State / 写作前故事运行状态`

分析线可以厚，可以有 source ref，可以有源本节点编号。

### 4.2 创作线

服务对象：writer。

产物：

- `Pressure-chain Writer Brief / 压力链写作简报`
- `Screenplay Draft / 剧本正文`
- `Pressure-chain Patch Brief / 压力链返修简报`

创作线必须薄，不能带 manifest、质量门、版本对比、完整 source ref 大表。

### 4.3 审计线

服务对象：reviewer、主控。

产物：

- `source carry-through audit`
- `quality gate report`
- `rewrite report`
- `reviewer report`

审计线检查有没有洗飞、同构、降级。

### 4.4 治理线

服务对象：主控。

产物：

- `workflow_run_manifest`
- `版本对比`
- `决策与变更`

治理线只证明流程和证据，不证明剧本好看。

---

## 5. 角色分工调整

### 5.1 主控 agent

负责：

- 需求对齐；
- 控制流程；
- 决定哪些材料给 writer，哪些材料只给 reviewer；
- 判定失败层；
- 决定回滚到哪一步；
- 最终交付用户。

主控不能把所有材料塞给 writer。

### 5.2 分析 agent / 分析阶段

可以由主创 agent 完成，也可以由临时 sub-agent 辅助。

职责：

- 完整读源本；
- 做 Source Bible；
- 拆出源本高价值节点；
- 标注源本强度来源；
- 标注禁止复用外形；
- 记录源本烂点和水分。

分析层不是 writer prompt。

### 5.3 Writer agent

writer 不看完整分析底稿。

writer 只看：

- 用户需求摘要；
- 洗稿边界摘要；
- 当前故事运行状态；
- 当前批次 episode plan；
- 当前集 / 当前高压场 Pressure-chain Writer Brief；
- 必要的少量源本体验锚点。

writer 不看：

- manifest；
- 作者质量门；
- reviewer 报告；
- 版本对比；
- 完整 source ref 表；
- 外部研究材料；
- 所有历史失败记录。

### 5.4 Reviewer agent

每个首批版本单开干净 reviewer。

Reviewer 两轮：

1. 第一轮只读正文 + 最小需求，判断剧本效果；
2. 第二轮再读分析底稿和边界包，查洗飞、同构、降级。

Reviewer 不参与共创，不提前看作者自检。

---

## 6. 外部资产映射

| 环节 | 外部资产 | 用法 |
|---|---|---|
| 需求确认 | `short-drama /start` + `how-to routing` | 直接用，但加洗稿任务类型 |
| 源本分析底稿 | `oh-story 情节节点/拆文报告/写作手法` + `short-drama hook/rhythm/satisfaction` | 直接用结构，加入洗稿字段 |
| 洗稿边界包 | 无直接等价 | 本项目自建薄层 |
| Source Retention Anchor | `short-drama hook/rhythm/satisfaction/paywall` + 源本高价值节点 | 自建薄层，只保留源本让用户继续追/付费的锚点 |
| Story Operating State | `oh-story 角色状态/上下文/伏笔追踪` + `how-to-make-script continuity` | 改造成写作前坐标，不是写后存档 |
| 高压节点粗验 | `scene_card` + `power_shift / visual_executability` | 改造用 |
| Episode Plan | `short-drama episode-directory` + `rhythm-curve` | 改造用 |
| Pressure-chain Writer Brief | `scene_card / scene_draft` + `mechanics_pressure` | 改造用，去掉审计字段，加入压力链 |
| Screenplay Draft | `screenplay_draft / scene_draft` | 直接用剧本合同 |
| Rewrite Report | `rewrite_report` | 直接用 |
| Pressure-chain Patch Brief | `rewrite_report` + `mechanics_pressure` | 本项目适配，防止返修变成正文补丁 |
| Dialogue Polish | `dialogue_polish + expression lens` | 直接用，但只修表达 |
| Quality Gate | `quality_gate_report` | 直接用结构，加入洗稿 lens |
| Story Memory | `oh-story 追踪文件` + `story_memory_checkpoint` | 直接用思路 |
| Manifest | 项目自建 | 只做执行证据 |

---

## 7. 详细流程

## 0. 最小需求确认

### 目标

拿到可以开始读源本的最低信息，不一开始问爆用户。

### 必须确认

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
用户特别想保留什么：
用户特别不想要什么：
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

### 输出

`需求确认摘要`

---

## 1. Source Bible / 源本分析底稿

### 目标

完整回答：

**源本为什么有效？**

### 结构

```text
1. 一句话故事核
2. 核心期待
3. 分集功能
4. 高价值节点
5. 钩子与卡点
6. 爽点 / 压抑-释放
7. 人物欲望与关系拉扯
8. 权力变化
9. 信息差与真相揭露路径
10. 情绪强度和情绪走势
11. 源本高辨识外形
12. 源本水分 / 烂点
```

### 高价值节点必须回答

```text
节点发生了什么？
观众为什么痛 / 爽 / 急 / 气 / 期待？
谁误判谁？
谁压谁？
谁救或不救？
谁获得/失去主动权？
这一节点靠什么具体人戏成立？
哪些外形不能复制？
如果迁移失败，最容易丢什么？
```

### 禁止

不要把 Source Bible 直接给 writer 当全文 prompt。

---

## 2. Adaptation Boundary / 洗稿边界包

### 目标

把完整分析压成洗稿边界。

### 只保留四类

```text
必须保留的体验功能：
必须换掉的源本外形：
可以自由换的外壳变量：
必须删除 / 修复的烂点：
```

### 通过标准

- 不能扩成万能变量矩阵；
- 不能把强继承理解成照抄事件；
- 不能把去同构理解成丢掉源本好看的节奏、钩子、关系和情绪。

---

## 3. Source Retention Anchor / 源本留存锚点

### 目标

从 Source Bible 和 Adaptation Boundary 里压出最薄的一层：

**源本靠什么让用户一直想继续看、继续付费？**

这不是剧情摘要，也不是 source ref 证明表。

它是后面 Story Operating State、Episode Plan 和 Pressure-chain Writer Brief 的洗稿锚点。

### 结构

```text
核心期待链：
必须等效迁移的钩子 / 卡点：
情绪密度和峰谷：
爽点压抑-释放方式：
关系拉扯：
信息差 / 真相揭露节奏：
付费前后追问惯性：
阶段节奏：
不能被新壳洗掉的体验：
```

### 通过标准

- 不能替代 Source Bible；
- 只写源本有效性，不写新剧情；
- 不复述完整剧情；
- 不写固定频率或硬套标准库比例；
- 能回答“用户为什么还想看下一集”；
- 后续压力链如果不承接这些锚点，不能判为洗稿成功。

---

## 4. Story Operating State / 写作前故事运行状态

### 目标

把 Source Bible 和 Adaptation Boundary 压成 writer 开写前必须知道的“故事当前状态”。

它不是完整分析，也不是状态大表。

它只回答：

**这个故事现在活到哪儿了？**

### 为什么需要

如果 writer 只拿到：

```text
本集要揭露 X
本集要打脸 Y
本集要让 A 后悔
```

writer 很容易安排文件、录音、屏幕、key、系统来完成结果。

如果 writer 拿到的是：

```text
谁现在想要什么
谁现在怕什么
谁误会谁
谁压着谁
关系卡在哪里
观众正在等什么
本批必须推进什么
```

正文才更可能从人物压力里长出来。

### 结构

```text
本批源本留存锚点：

主角当前状态：
- 现在想要什么：
- 现在最怕什么：
- 当前误会 / 盲点：
- 当前身体 / 情绪 / 社会位置：

核心对手当前状态：
- 现在想要什么：
- 现在最怕什么被拆穿：
- 当前筹码：
- 当前失控边缘：

关键关系状态：
- 谁靠近谁：
- 谁抗拒谁：
- 谁误判谁：
- 谁掌握主动权：
- 拉扯点是什么：

观众当前等待：
- 最大追问：
- 情绪债：
- 爽点债：
- 不能提前兑现：

本批推进要求：
- 关系必须怎么变：
- 局势必须怎么变：
- 信息必须怎么变：
- 情绪必须怎么变：
```

### 通过标准

- 薄，不超过 writer 能一眼读完的规模；
- 不放完整 source ref；
- 不放 reviewer 意见；
- 不放 manifest / pass 证据；
- 能直接帮助 writer 判断人物为什么行动；
- 能看出本批要承接哪些源本留存锚点；
- 如果缺少主拉扯、主动权或观众等待，不能进入高压节点粗验。

### 与 Story Memory Checkpoint 的关系

```text
Story Operating State：写前使用，给 writer 创作坐标；
Story Memory Checkpoint：写后使用，保存本批改动后的新状态。
```

---

## 5. High-pressure Scene Viability / 高压节点新场面粗验

### 目标

在完整 beat sheet 之前，先判断高压源本节点的新壳承载是否可行。

这是沿用 v3 的结构性前置，不是新增规则表。

### 适用范围

只处理高风险节点：

- 前 1-3 集；
- 强危机；
- 强羞辱；
- 强误会；
- 强打脸；
- 身份揭露；
- 关系质变；
- 源本高辨识桥段；
- 上一轮被导演 / reviewer 指出的失败点。

### 每个节点只问 6 件事

```text
1. 源本强度来自哪里？
2. 新壳中谁和谁发生直接冲突？
3. 这一场的人际发动机是什么？
4. 文件 / 屏幕 / key / 机构流程是否只是工具，而不是发动机？
5. 这一场结束谁失去什么，谁获得什么？
6. 卡点停在哪个未完成动作 / 选择 / 后果前？
```

### 结论

```text
可进入 Episode Plan
需要重选场面发动机
该源本节点不适合当前新壳，需用户拍板
```

### 失败信号

- 新壳载体只能靠系统、文件、授权、屏幕、会议完成；
- 人物没有当场欲望和选择；
- 场面成立依赖大量解释；
- 源本强度只剩剧情功能，没有人际压迫；
- 卡点只剩信息揭露，没有动作/选择/后果。

---

## 6. Episode Plan / 新本阶段骨架与分集功能

### 目标

控制首批的留存闭环，不写厚大纲。

### 结构

```text
Story Engine：
- 主角想要什么
- 阻碍是什么
- 利害关系是什么

Episode Map：
- Episode
- Opening Hook
- Core Friction
- Max Spike
- Change：关系 / 局势 / 信息 / 情绪
- End Button
- Do Not Consume
- 本集观众追问
```

### writer 可见程度

writer 可以看到当前批次的 Episode Plan。

但 Episode Plan 中不要塞完整 source ref 证明链。

---

## 7. Pressure-chain Writer Brief / 压力链写作简报

### 目标

这是 writer 的真正输入。

它不是 scene packet 大表，不是审计表。

它要避免结果式任务单。

高压场不能只告诉 writer：

```text
这一集要揭露什么；
这一集要打脸谁；
这一集要卡在哪。
```

必须先告诉 writer：

**这场戏如何从人物欲望、阻碍、误判、选择、代价里被逼出来。**

### 每集简报

```text
本集故事当前状态：
本集必须承接的源本留存锚点：
本集观众追问：
本集开头抓人：
本集核心摩擦：
本集最大刺激点：
本集结束前必须改变什么：
本集结尾停在哪一拍：
不能提前消费：
```

### 高压场压力链

```text
源本留存锚点：
场面发动机：
谁想要什么：
谁阻止谁：
谁误判谁：
谁先施压：
对方怎么挡 / 逃 / 骗 / 反击：
压力怎么加码：
谁被迫做不可逆选择：
这个选择让谁付出可见代价：
谁获得/失去主动权：
观众应该感到什么：痛 / 爽 / 急 / 气 / 期待 / 心疼
可用工具：文件 / 屏幕 / 道具 / 录音等，只能辅助
禁用外形：源本高辨识桥段 / 道具 / 台词 / 事件链
最后停住的动作 / 声音 / 后果：
```

### 压力链通过标准

- 每个高压场必须有 5-7 个因果压力拍；
- 每条压力链必须承接源本留存锚点，不能写成另一个原创故事；
- 每个压力拍必须由人物行动或人物反应推动；
- 爆点必须来自人物被迫选择、失控、误判或反击，不来自作者安排；
- 文件 / 屏幕 / key / 录音 / 机构流程只能改变人物行为，不能替人物完成戏；
- 如果删掉所有文件、屏幕、系统提示，这场戏仍应剩下人和人的冲突；
- 如果保住了人物冲突，但丢了源本钩子、卡点、情绪密度、爽点节奏或追问惯性，也不能通过；
- 如果压力链写不出来，不能进入正文。

### Pressure-chain Writer Brief 禁止出现

- 大段源本文字；
- 完整 source ref 表；
- manifest 证据；
- quality gate 字段；
- reviewer 意见；
- 版本对比；
- 外部项目来源说明；
- “必须证明迁移了 S1-E7”这类审计语言。

### 通过标准

writer 只看这个 brief，应该能写出一场戏，而不是写一份证明。

---

## 8. Screenplay Draft / 剧本正文

### 目标

writer 按简报写正文。

正文必须像剧本，不像说明书、审稿表、流程单。

核心合同：**正文页上写出来的东西，应该基本等于最终 AI 成片里能看见和听见的东西。**

正文不是剧情说明，也不是给后续环节脑补的提示词。动作、声音、物件、身体反应、空间变化和人物可见状态，必须能直接落到画面和声音里；剧情功能、心理判断和作者意图不能替代这些可见内容。

这里的 screenplay 采用 Hollywood screenplay 的基本容器：场景标题、动作行、人物名、台词、必要声音和屏幕文字；不追求 Final Draft 分页精确度。

好莱坞格式和“每场写清楚画面里发生什么”不矛盾。这里借用好莱坞格式的核心不是排版，而是 page-to-screen：剧本里写了什么，最终画面和声音里就应该基本出现什么。本项目服务 AI 出海短剧，所以动作行必须写到 AI 能生成画面，不能只给后续 AI 视频链路留想象空间。

### 来源

- `how-to-make-script screenplay_draft`
- `scene_draft`
- `short-drama episode`

### 写法底线

- 只写观众能看见 / 听见、AI 能生成的东西；
- 高压场必须有行动、空间、身体、他人反应或当众后果；
- 台词短、准、有功能；默认台词为英文，除非需求确认指定中文或双语；
- 结尾停在 AI 能生成的最后动作 / 声音 / 画面；
- 文件、屏幕、key、录音可以出现，但不能替人物完成戏。

---

## 9. Rewrite Report / 返修诊断

### 目标

初稿后先判断坏在哪层，不直接润色。

### 失败层

```text
concept：产品方向 / 新壳方向错
source_analysis：源本有效性没读出
adaptation_boundary：保留/替换边界错
source_retention：源本留存锚点被压错或丢失
story_operating_state：写前故事状态缺失或错误
scene_engine：场面发动机错
episode_structure：分集留存错
pressure_chain：高压场压力链不成立或变成原创
screenplay：正文写法错
dialogue：台词问题
continuity：状态追踪问题
execution：流程证据问题
```

### 返修原则

如果是 `scene_engine` 错，不能只加身体反应或润色台词。

---

## 10. Pressure-chain Patch Brief / 压力链返修简报

### 目标

把 rewrite report / reviewer note 先改写成可执行的压力链返修方案，再进入正文修订。

这是为了防止返修变成：

```text
文件太弱 -> 换成监控
情绪太弱 -> 加手抖 / 加血 / 加跪下
台词太水 -> 删几句
机制感太重 -> 让人物亲手按键
```

这些都可能是症状层补丁。

### 每个被点名高压场必须回答

```text
原场问题属于哪层：
原场为什么失败：
旧写法中哪些内容要删掉：
新的场面发动机：
谁先施压：
对方怎么挡 / 逃 / 骗 / 反击：
压力怎么加码：
谁被迫做不可逆选择：
爆点出现后谁立刻失去什么：
哪些文件 / 屏幕 / 道具只能保留为辅助：
正文应该改哪一段：
```

### 通过标准

- 返修必须有减法，不只加料；
- 如果原场发动机错，必须允许拆掉原场重写；
- 如果问题只是台词水，才进入 Dialogue Polish；
- 如果问题是源本洗飞或新壳不承载，不能在正文层修；
- 如果返修 brief 仍然只是在替换道具或补身体反应，判为未通过。

---

## 11. Dialogue Polish / 台词修订

### 目标

只修台词和表达，不修结构。

### 必须判断

```text
这句台词是否应该存在？
是否能改成动作 / 停顿 / 表情 / 空间压力？
台词功能是什么？
潜台词是什么？
角色声音是否区分？
连续两三轮对白是否有新压力或新信息？
```

如果场面发动机错，`dialogue polish` 必须退回 `rewrite report`，不能假装修好了。

---

## 12. Author Ready Check / 作者准备送审检查

### 目标

作者不能给自己质量 pass。

作者只给：

```text
ready for reviewer
needs rewrite
blocked
```

### 检查项

- 是否按 Pressure-chain Writer Brief 写完；
- 是否明显偏离用户需求；
- 是否明显洗飞；
- 是否明显同构；
- 是否明显像说明书 / 流程单；
- 是否有未处理的 rewrite_report hard issue。

作者检查不等于 reviewer pass。

---

## 13. Reviewer 第一轮：正文效果审

### 输入

只读：

- 用户需求摘要；
- 本批正文。

不读：

- 作者自检；
- Source Bible；
- 洗稿边界包；
- Pressure-chain Writer Brief；
- manifest；
- 版本对比；
- reviewer 争论。

### 目标

判断正文作为短剧是否成立。

### 输出

```text
creative_pass
creative_revise
creative_block

failure_layer：
callback_target：
reason：
```

第一轮 reviewer 不读源本审计材料，所以不能判定“是否洗飞”的最终结论。

但它必须判断正文层失败发生在哪里，例如：

```text
hook_retention：开头或结尾追看不足
scene_engine：高压场没有戏
screenplay：正文像说明书 / 不像剧本
dialogue：台词水 / 像电视剧聊天
pacing：节奏拖 / 空转
continuity_observed：仅凭正文可见的关系或信息断裂
```

这些 failure_layer 给主控做 callback，不等于最终审计结论。

### 看什么

- 是否想继续看；
- 每集开头是否抓人；
- 高压场是否有戏；
- 人物是否互相逼迫；
- 台词是否水；
- 是否像电视剧聊天；
- 是否像流程证明；
- 情绪是否被看见；
- 卡点是否停在答案前一拍。

---

## 14. Reviewer 第二轮：源本迁移审计

### 输入

读取：

- Source Bible；
- Adaptation Boundary；
- Source Retention Anchor；
- Story Operating State；
- Episode Plan；
- Pressure-chain Writer Brief；
- 正文；
- 必要源本片段。

### 目标

判断：

- 有没有洗飞；
- 有没有改名复刻；
- 有没有短剧降级；
- 有没有提前消费；
- 有没有继承烂点；
- 有没有丢掉源本关键留存和情绪功能。

### 输出

```text
source_audit_pass
source_audit_revise
source_audit_block

failure_layer：
callback_target：
reason：
```

第二轮必须检查链路是否断开：

```text
Source Bible
-> Source Retention Anchor
-> Story Operating State
-> Episode Plan
-> Pressure-chain Writer Brief
-> 正文
```

如果源本分析里有钩子、卡点、情绪密度、爽点节奏、关系拉扯或期待链，但后续只剩机制事件、证据、文件或结果任务，必须判 `source_audit_revise` 或 `source_audit_block`，并标明断在哪一层。

---

## 15. 主控判定

主控必须把结论拆开：

```text
execution_status：
creative_status：
source_audit_status：
continuity_status：
delivery_status：
```

### 不能交付的情况

- creative_status 不是 pass；
- source_audit_status 不是 pass；
- execution_status 是 protocol-fail；
- reviewer 第一轮没跑；
- 作者 ready check 还留有 hard issue。

### 回滚规则

| 失败层 | 回到哪里 |
|---|---|
| 新壳不承载 | 二次需求确认 / 洗稿边界包 |
| 源本留存锚点丢失 | Source Bible / Source Retention Anchor |
| 故事当前状态错误 | Story Operating State |
| 场面发动机错 | 高压节点新场面粗验 |
| 分集留存错 | Episode Plan |
| writer 被证明链压住 | Pressure-chain Writer Brief |
| 压力链写成原创 / 没承接源本留存锚点 | Source Retention Anchor / Pressure-chain Writer Brief |
| 正文像说明书 | Screenplay Draft |
| 返修只换道具 / 只加动作 / 只贴情绪 | Pressure-chain Patch Brief |
| 台词水 | Dialogue Polish |
| 洗飞 / 同构 | Source Bible / Adaptation Boundary |
| 伏笔/关系漂移 | Story Operating State / Story Memory |
| 执行证据缺 | Manifest / Protocol |

---

## 16. Story Memory Checkpoint

### 目标

每批写完保存可继续状态，不重写整本分析。

它不是 writer 写前唯一的状态来源。

写前使用的是 `Story Operating State`，写后保存的是 `Story Memory Checkpoint`。

### 结构

```text
关系状态：
人物状态：
信息差状态：
伏笔 / 证据：
未兑现承诺：
禁止提前消费：
下一批入口：
```

来源：

- `oh-story` 追踪文件；
- `story_memory_checkpoint`。

### 规则

- 只记录本批导致的状态变化；
- 不重写 Source Bible；
- 不把质量判断写成状态事实；
- 下一批 Pressure-chain Writer Brief 必须先读取上一批 checkpoint，再压成新的 Story Operating State；
- 如果下一批直接看旧 episode plan 写作，而不看状态变化，不能判为 pass。

---

## 17. Manifest / 版本记录

### 目标

证明执行顺序和证据存在。

### 明确边界

manifest 只回答：

```text
步骤是否发生；
产物是否存在；
输入输出是否可追踪；
是否违反 protocol。
```

manifest 不回答：

```text
剧本是否好看；
是否能交付；
是否能付费；
是否像短剧。
```

版本对比只回答：

```text
相对上一版改了什么；
是否解决上一版指出的问题；
是否引入新风险。
```

版本对比不能替代 reviewer。

---

## 18. 需要删除 / 降级的 v2 内容

### 删除 writer-facing 内容

- writer-facing 的完整 `carry-through evidence`；
- writer-facing 的完整 source ref 表；
- writer-facing 的质量门字段；
- writer-facing 的版本对比；
- writer-facing 的 reviewer 意见；
- “必须证明迁移了某源本节点”的审计语言。

### 降级内容

- `workflow_run_manifest`：降级为治理证据；
- `版本对比`：降级为主控记录；
- `作者质量门 pass`：改为 `ready for reviewer / needs rewrite / blocked`；
- `dialogue polish 已内化`：必须变成实际修订或明确跳过理由；
- `复用验证通过`：只能表示 unchanged / not revalidated，不能等同完整 packet pass。

---

## 19. v4 成功标准

第一阶段不是证明能自动产出爆款。

v4 的成功标准是：

1. 分析底稿完整，但不污染 writer；
2. Source Retention Anchor 能锁住源本让用户追下去、付下去的钩子、卡点、情绪密度、节奏和期待链；
3. Story Operating State 能让 writer 知道故事当前活到哪儿；
4. Pressure-chain Writer Brief 能让高压场从人物欲望、阻碍、误判、选择、代价里长出来；
5. 新压力链不能写成另一个原创故事，必须承接源本留存锚点；
6. 返修能先改压力链，再改正文，而不是只换道具或加身体反应；
7. reviewer 第一轮只读正文也能判断是否像短剧；
8. reviewer 第二轮能定位有没有洗飞 / 同构 / 降级；
9. manifest 不再被误用成质量背书；
10. 同一个源本重跑时，正文不再稳定滑向流程证明 / 机制戏。

---

## 20. 下一步验证方式

不要直接跑完整 1-10 集。

先做一个小验证：

```text
同一个源本高压节点
-> 旧 v3 writer brief
-> 新 v4 source retention anchor + story operating state + pressure-chain writer brief
-> 两个干净 writer 分别写同一集或同一高压场
-> reviewer 第一轮只读正文
-> 比较哪一个更像短剧强戏
```

如果 v4 仍然写成机制戏，说明重构还没解决问题。

如果 v4 明显减少流程感，再决定是否替代当前执行版。
