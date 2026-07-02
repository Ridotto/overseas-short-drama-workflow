# 海外短剧洗稿器 · workflow spec v6 能力回收修正版草案

> 日期：2026-07-01
> 状态：草案，不是当前正式执行版；已按 `workflow_spec_v6_草案审查_2026-07-01.md` 小修连接点。
> 上游：`PRD_v4.md`
> 主骨架来源：`workflow_spec_v2.md`
> 修正依据：`原项目能力全集盘点_2026-07-01.md`、`原项目能力对账表_2026-07-01.md`
> 可吸收但不照搬：`workflow_spec_v4_机制重构草案.md`、`workflow_spec_v5_创作优选草案.md`

---

## 0. v6 的定位

v6 不重写产品。

产品仍然是：

**把一个已被市场验证或值得参考的短剧源本，洗成一个新壳下仍然好看、能追、能付费的新剧本。**

v6 也不把 v5 继续扩成主流程。

v6 只做一件事：

```text
把原项目已经有的能力重新接回正式链路，
保证它们不是只停在分析表、自检表或历史文档里，
而是能一路进入 writer 输入、正文和 reviewer 判错。
```

一句话：

**v2 是主骨架；v4 补写前状态和压力链；v5 只保留高压节点场面优选；v6 把这些放回正确层级。**

---

## 1. v6 要修的真实问题

不是“原项目没有钩子、爽点、节奏、拉扯、视听语言”。

这些原项目都有。

问题是它们经常发生三种断裂：

### 1.1 分析有，writer 没吃到

源本拆文里可能已经写了：

```text
这一集靠什么钩子留住人；
爽点如何蓄力和释放；
男女主关系怎么拉扯；
源本高压节点为什么有冲击；
角色此刻是什么状态；
观众正等哪一下。
```

但到 writer 手里变成：

```text
本集必须揭露 X；
必须证明 Y；
必须避开源本外形 Z；
必须回指源本节点编号。
```

这会把创作变成证明题。

### 1.2 能力放错层

如果视听承载、台词功能、拉扯感只出现在 reviewer 或自检里，writer 写正文时不会自动执行。

这些能力必须在写作前就变成：

```text
故事当前状态；
本集留存任务；
本场压力链；
角色此刻的欲望、误判、恐惧、遮掩、选择和代价。
```

### 1.3 局部修法挤掉全局能力

v5 抓到“高压场面要优选”是对的。

但它不能替代：

```text
源本拆文
留存钩子
卡点气口
爽点周期
节奏密度
主线期待
人物关系
变量迁移
连续性
台词表达
自检 reviewer
```

所以 v5 只保留为“高压节点场面迁移”的局部工具。

---

## 2. v6 的主原则

### 2.1 主流程不换血

v6 保留 v2 的主链路：

```text
需求确认
源本拆文包
洗稿边界包
beat sheet / outline
Episode function map
Scene packet / writer brief
Screenplay draft
Rewrite report
Dialogue polish
Quality gate
Story memory checkpoint
Independent reviewer
Version comparison
```

这些是主链路，不允许被 v5 或任何局部草案替代。

### 2.2 修连接，不堆规则

v6 不新增“视听语言规则”“拉扯规则”“爽点规则”这种孤立条目。

v6 只要求每项关键能力都能走完这条链：

```text
源本拆文包
  -> Source Retention Anchor
  -> Story Operating State
  -> Episode function map
  -> Writer brief
  -> Screenplay draft
  -> Reviewer
```

如果某项能力只在源本分析里出现，到了 writer brief 没了，就算断。

### 2.3 writer-facing brief 不塞审计底稿

分析线可以厚。

writer 输入必须薄。

这里不是说“分析和写作必须拆成两个互不相干的人”。

主创 agent 可以完整拥有源本分析上下文，也应该理解源本为什么好看；但进入正文写作时，不能把完整审计底稿原样塞进写作界面。写作界面要把分析压成故事状态、场面任务和压力链。

writer-facing brief 不应该塞入一堆：

```text
source_ref
carry-through evidence
manifest pass
forbidden shape 大表
版本对比证明
```

writer 应该看到：

```text
这一集观众在等什么；
谁压谁；
谁误会谁；
谁想要什么；
谁阻止谁；
压力怎么加码；
谁被迫选择；
代价是什么；
卡在哪个未完成动作 / 反应 / 后果前。
```

### 2.4 防同构不能压过防洗飞

顺序是：

```text
先保住源本有效体验；
再扣掉源本高辨识外形；
再找新壳下同等强度的承载方式。
```

不能为了不像源本，把强危机、强羞辱、强拉扯洗成文件、会议、授权、屏幕、冷对白。

---

## 3. v6 总 workflow

```text
0. 最小需求确认
1. 源本拆文包 Source Bible
2. 洗稿边界包 Adaptation Boundary
3. Source Retention Anchor / 源本留存锚点
4. Story Operating State / 写作前故事状态
5. Beat sheet / outline
6. Episode function map
7. 高压节点场面迁移与优选
8. Writer brief / Scene packet
9. Screenplay draft
10. Beat survival check
11. Rewrite report
12. Pressure-chain patch brief
13. Dialogue polish
14. Author quality gate
15. Story memory checkpoint
16. Independent reviewer
17. Version comparison / 主控交付判断
```

说明：

- 0-2 基本沿用 v2。
- 3-4 吸收 v4，但只作为连接层，不替代源本拆文包；Story Operating State 是写作前状态快照，进入每批、每集或高压节点 writer brief 前都要按最新 episode map / story memory 刷新。
- 7 吸收 v5，但只用于高压节点，不作为全局主轴。
- 8 是 writer 真正输入，必须把审计底稿压成可写的故事状态和压力链。
- 10 是新加的轻量检查，不是新流程大环节，只抽查“最高风险的关键节拍是否活到正文里”。

---

## 4. 四条线

### 4.1 分析线

服务对象：主控、写作简报生成者、reviewer 第二轮。

产物：

- Source Bible / 源本拆文包；
- Adaptation Boundary / 洗稿边界包；
- Source Retention Anchor / 源本留存锚点；
- Story Operating State / 写作前故事状态。

特点：

- 可以有源本节点编号；
- 可以厚；
- 可以记录源本外形、同构风险、证据和锚点；
- 不直接塞给 writer。

### 4.2 创作线

服务对象：writer。

产物：

- Episode function map 的写作摘要；
- 高压节点场面选择结论；
- Writer brief / Scene packet；
- Screenplay draft；
- Pressure-chain patch brief；
- Dialogue polish。

特点：

- 薄；
- 可写；
- 不像审计表；
- 不要求 writer 证明源本对应关系；
- 只要求 writer 写出短剧强戏。

### 4.3 审计线

服务对象：作者自检、reviewer、主控。

产物：

- Beat survival check；
- Rewrite report；
- Quality gate；
- Reviewer report；
- Source carry-through audit。

特点：

- 查有没有洗飞、同构、降级、长剧化、状态漂移；
- 判断失败层；
- 不把所有问题都推给正文润色。

### 4.4 治理线

服务对象：主控。

产物：

- workflow_run_manifest；
- 版本对比；
- 决策与变更；
- 用户 / 导演反馈回流。

特点：

- 证明流程有没有执行；
- 不证明剧本好不好；
- 不参与创作判断。

---

## 5. 详细步骤

## 0. 最小需求确认

沿用 v2。

必须确认：

```text
任务类型：洗稿 / 改编 / 重写 / 诊断 / 审稿
源本：
新壳：
目标市场：
输出语言 / 审稿语言：
正文用途：AI 视频生成用剧本 / 人审稿 / 字幕台词版 / 双语版
集数是否变化：
本轮输出范围：
改写力度 / 变量边界：
已知禁区：
```

原则：

```text
先拿最小信息开读源本；
读完源本后再做二次需求确认。
```

---

## 1. Source Bible / 源本拆文包

沿用 v2，但必须防止写成剧情摘要。

输出至少包含：

```text
1. 一句话故事核
2. 核心期待
3. 首批分集功能
4. 高价值节点表
5. 钩子与卡点表
6. 爽点 / 压抑-释放表
7. 关系 / 权力变化表
8. 信息差与真相揭露路径
9. 写作手法 / 表达手法
10. 源本水分 / 烂点 / 禁止复用外形
```

每个高价值节点必须回答：

```text
客观事件是什么；
观众为什么痛、爽、急、气、期待、心痒；
它靠什么产生强度：危机、羞辱、误会、关系撕裂、身份反转、身体伤害、当众后果、信息差；
谁压过谁；
谁知道什么；
卡点停在哪一拍；
哪些外形不能复用。
```

这一步的产物是分析底稿，不直接给 writer 全量阅读。

---

## 2. Adaptation Boundary / 洗稿边界包

沿用 v2。

只保留四类：

```text
必须保留的体验功能：
必须换掉的源本外形：
可以自由换的外壳变量：
必须删除 / 修复的烂点：
```

禁止扩成全剧万能变量矩阵。

通过标准：

- 能说清源本好看的东西是什么；
- 能说清哪些外形不能复用；
- 不把“去同构”理解成改得越大越好；
- 不把“强继承”理解成照抄事件。

---

## 3. Source Retention Anchor / 源本留存锚点

这是 v6 从 v4 吸收的连接层。

它不是替代 Source Bible，而是从 Source Bible 里压出 writer 和 episode map 必须继承的追看发动机。

结构：

```text
源本核心期待：
首批留存闭环：
关键钩子 / 卡点气口：
爽点蓄力与兑现周期：
情绪密度走势：
信息密度走势：
情节 / 权力变化走势：
人物关系拉扯主线：
反派压力阶梯：
绝不能洗掉的高价值节点：
```

通过标准：

- 不能只写“复仇、追悔、打脸”这种类型词；
- 必须写出观众为什么继续看；
- 必须写出源本首批追看惯性；
- 必须能指导 Episode function map。

失败信号：

```text
只剩源本节点编号；
只剩剧情功能；
只剩同构红线；
没有钩子、爽点、节奏、拉扯和期待链。
```

---

## 4. Story Operating State / 写作前故事状态

这是 v6 从 v4 吸收的第二个连接层。

它解决的问题：

```text
writer 写正文前不知道故事当前活到哪儿，
于是只能按结果任务单写。
```

结构：

```text
本批开始时：
- 主角想要什么；
- 主角怕什么；
- 主角误会什么；
- 主角身体 / 情绪状态；
- 男主 / 女主 / 反派各自掌握什么信息；
- 谁有主动权；
- 谁在压谁；
- 谁正在靠近 / 退开 / 试探 / 误判；
- 观众此刻最想看什么；
- 本批必须推进什么；
- 本批绝不能提前消费什么。
```

通过标准：

- 不是剧情摘要；
- 不是人物设定表；
- 必须给 writer 当前场面的创作坐标；
- 必须能接到 Episode function map 和 writer brief。

和 Story memory 的区别：

```text
Story Operating State：写前使用；
Story Memory Checkpoint：写后保存。
```

刷新规则：

```text
Story Operating State 不是一次性前置文档。
首次可在 beat sheet 前初始化；
进入每批、每集或每个高压节点 writer brief 前，必须按最新 Episode function map / Story memory 刷新。
如果状态和 episode map 冲突，先改状态快照，不直接写正文。
```

---

## 5. Beat sheet / outline

沿用 v2。

输出：

```text
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
- 本批情绪走势
- 拉扯 / 误会 / 追悔 / 反击如何递进
```

通过标准：

- 不能只是剧情梗概；
- 每个 beat 必须改变局势、关系、信息或情绪；
- 必须承接 Source Retention Anchor。

---

## 6. Episode function map

沿用 v2，并补强“源本能力传递”。

每集字段：

| 字段 | 要回答 |
|---|---|
| Episode | 第几集 |
| Title | 集标题 |
| Summary | 本集核心推进 |
| Opening Hook | 开头凭什么不被划走 |
| Core Friction | 谁和谁发生正面摩擦 |
| Max Spike | 本集最大刺激点 |
| Change | 关系 / 局势 / 信息 / 情绪哪一项改变 |
| End Button | 结尾钩子，停在答案前一拍 |
| Do Not Consume | 本集绝不能提前消费什么 |
| Source Retention Carry | 从源本留存锚点继承什么：钩子、爽点、情绪、信息、权力变化、拉扯 |
| Risk | 本集最容易洗飞、同构、降级或长剧化的点 |

通过标准：

- 每集必须能说清“观众为什么继续看”；
- 不能只写剧情功能；
- `Max Spike` 不能只有结果，必须有蓄力来源；
- `End Button` 必须是画面、声音、动作、选择或反应前一拍；
- `Source Retention Carry` 不能只写源本事件名。

---

## 7. 高压节点场面迁移与优选

这是 v6 从 v5 吸收的局部能力。

适用范围只限：

```text
前 1-3 集；
每集结尾卡点；
强危机；
强羞辱；
强打脸；
强误会；
强关系质变；
身份 / 真相揭露；
源本高辨识桥段；
上一版被导演 / reviewer 点名失败的场面。
```

### 7.1 先做新壳场面迁移

每个高压节点先回答：

```text
源本节点：
源本体验功能：
源本冲击来源：
源本禁止外形：
新壳约束：
新场面必须承载的强度：
```

### 7.2 再做场面候选

对最关键节点，允许做 2-3 个候选。

每个候选只写：

```text
候选场面一句话：
谁压谁：
谁被迫行动：
最大可见冲击：
关系 / 权力变化：
卡点能停在哪：
同构风险：
降级风险：
```

### 7.3 选择一个方案

选择标准：

```text
最能迁移源本体验；
最不像源本外形；
最有短剧冲击；
最能推进人物关系和主线期待；
最能被 AI 出海短剧画面承载。
```

禁止：

- 不为了“新”而丢源本有效性；
- 不为了“可追溯”而变成证据链；
- 不把所有场面都做候选，只有高压节点需要。
- 普通过渡场、低压关系场、功能承接场不做 Scene Option Pitch；这些场只需要在 Scene Sequence 里交代功能、状态变化和出入口。

---

## 8. Writer brief / Scene packet

这是 v6 最关键的修点。

v2 的 Scene packet 仍然保留，但要拆成两层：

```text
审计层 scene packet：给主控 / reviewer；
writer-facing brief：给 writer。
```

writer-facing brief 不能像审计表。

### 8.1 writer-facing brief 结构

```text
Episode N Writer Brief

上一集最后停在：
本集观众正在等：
本集必须吃到的阶段性东西：
本集绝不能提前消费：

本集故事状态：
- 谁有主动权：
- 谁被误会：
- 谁在忍：
- 谁快失控：
- 谁正在靠近 / 退开：

本集压力推进：
1. 起压：
2. 升压：
3. 爆点：
4. 收住 / 卡住：

Scene Sequence：
- Scene 1：
  - 功能：
  - 进入状态：
  - 动作推进：
  - 退出状态：
- Scene 2：
  - 功能：
  - 进入状态：
  - 动作推进：
  - 退出状态：

高压场压力链：
- 谁想要什么：
- 谁阻止谁：
- 谁误判了什么：
- 压力怎么加码：
- 谁被迫选择：
- 谁立刻失去什么：
- 卡在哪个未完成动作 / 反应 / 后果前：

正文写法边界：
- 台词少说什么；
- 必须让观众看到什么；
- 不能变成什么弱形态；
- 源本外形禁区一句话。
```

Scene Sequence 的作用：

```text
把“本集任务”拆成可写的场景顺序。
它不是分镜表，也不是审计表。
普通过渡场只写功能、进入状态、动作推进、退出状态；
高压场才追加压力链。
```

### 8.2 writer 不该看到

writer-facing brief 禁止塞入：

```text
完整 Source Bible；
大段源本剧情；
大表 source_ref；
carry-through evidence；
manifest pass；
版本对比；
自检结论；
reviewer 旧评语；
过多字段名。
```

### 8.3 通过标准

- writer 能只看 brief 写正文；
- brief 让 writer 写戏，不是写证明；
- brief 有故事状态、场景顺序、压力推进和卡点边界；
- brief 继承源本留存锚点，但不复制源本外形；
- brief 不把台词、证据、屏幕、文件当成场面发动机。

---

## 9. Screenplay draft

沿用 v2 的 page-to-screen 合同。

正文核心：

```text
剧本里写出来的东西，应该基本等于最终 AI 成片里能看见和听见的东西。
```

正文允许使用 Hollywood screenplay 基本容器：

```text
INT. / EXT. LOCATION - DAY / NIGHT
动作行
CHARACTER
对白
SFX:
ON SCREEN:
```

但目的不是排版，而是让动作、声音、身体反应、空间变化、当众后果能进入 AI 视频生成链路。

不合格信号：

- 像说明书；
- 像审计表；
- 人物站着轮流说话；
- 关键情绪只靠对白；
- 高压节点主要靠文件、会议、屏幕、录音、解释；
- 结尾把答案说完；
- 动作只是补充描写，没有推动权力、关系或局势。

---

## 10. Beat survival check

这是轻量检查，不是新大表。

作者写完后，只抽查本批最关键的高压节点。

边界：

```text
每批只抽查 3-5 个最高风险节点；
每条只写 3 行以内：源本体验 / brief 承接 / 正文锚点；
不做全量追溯；
不写长篇解释；
不把它扩成新的证明材料。
```

检查链：

```text
源本高价值节点
-> Source Retention Anchor
-> Episode function map
-> Writer brief
-> Screenplay 正文
```

每条只回答：

```text
源本要迁移的体验是什么；
writer brief 里怎么承接；
正文里对应哪个动作 / 声音 / 身体反应 / 空间压力 / 当众后果 / 卡点画面；
有没有被降级成对白、文件、屏幕、说明。
```

如果发现：

```text
分析里有，正文没有；
brief 有，正文只剩对白；
源本是强冲击，新本是冷信息；
```

必须回到 writer brief 或 screenplay draft，不允许只做 dialogue polish。

---

## 11. Rewrite report

沿用 v2。

目标：

```text
先判断坏在哪层，不直接润色。
```

失败层：

| 失败层 | 回哪 |
|---|---|
| 源本有效性丢 | Source Bible / Source Retention Anchor |
| 改名复刻 | Adaptation Boundary / 高压节点场面迁移 |
| 短剧降级 | 高压节点场面迁移 / Writer brief |
| 场面发动机坏 | Writer brief |
| 正文可视化弱 | Screenplay draft |
| 台词水 | Dialogue polish |
| 状态漂移 | Story Operating State / Story memory |
| 执行证据缺 | Manifest / protocol |

---

## 12. Pressure-chain patch brief

这是 v6 从 v4 吸收的返修连接层。

它只在 rewrite report 判断问题属于“场面发动机 / 压力链 / 故事状态”时使用。

作用：

```text
把 reviewer note 先改写成新的压力链，
再改正文。
```

每个被点名高压场必须回答：

```text
原场坏在哪里：
坏的是事件载体、压力链、角色状态、台词，还是正文可视化：
新压力链：
- 谁想要什么：
- 谁阻止谁：
- 新误判是什么：
- 压力如何加码：
- 谁被迫行动：
- 代价是什么：
- 新卡点停在哪：
本次要删除什么：
本次不能只加什么：
```

通过标准：

- 必须有减法；
- 不能只补动作、补血、补台词；
- 不能保留坏发动机再贴情绪；
- 必须承接 Source Retention Anchor。

---

## 13. Dialogue polish

沿用 v2。

只处理台词和表达，不拿它修结构。

每句问题台词判断：

```text
这句该不该存在；
能不能改成动作 / 停顿 / 表演 / 空间压力；
如果必须说，功能是什么；
表面意思是什么；
潜台词是什么；
角色声音是否区分；
是否解释腔、完整句病、AI 味；
连续两三轮对白是否有新信息、新压力或新关系变化。
```

如果问题是场面不成立，必须退回 writer brief 或 screenplay draft。

---

## 14. Author quality gate

沿用 v2 的 `quality_gate_report`，但必须先查“能力传递”。

检查顺序：

1. **Contract fit**：正文是不是剧本，不是说明书。
2. **Source retention carry**：源本留存锚点有没有进入 episode map / writer brief / 正文。
3. **Adaptation fit**：有没有洗飞、同构、短剧降级。
4. **Scene pressure**：高压场是否由人物欲望、阻碍、误判、选择、代价推动。
5. **Expression integrity**：台词是否功能化，是否低信息聊天。
6. **Continuity**：状态、伏笔、信息差是否接得住。

硬失败：

- Source Retention Anchor 写了钩子、爽点、节奏、拉扯，但 writer brief 没带；
- writer brief 带了，但正文只剩信息/证据/对白；
- Scene packet / brief 像审计表，导致正文像流程说明；
- 高压节点没有人物被迫行动；
- dialogue polish 被拿来修结构病；
- manifest complete 被当成质量 pass。

---

## 15. Story memory checkpoint

沿用 v2，但补一句：

```text
写后保存的 story memory，下一批必须先压成新的 Story Operating State，再给 writer。
```

输出：

```text
关系状态：
信息差状态：
伏笔 / 证据状态：
角色状态：
未兑现承诺：
禁止下批提前消费：
下一批安全入口：
```

---

## 16. Independent reviewer

沿用 v2 的干净 reviewer 原则。

Reviewer 分两轮：

### 第一轮：只读正文

输入：

```text
用户需求；
PRD v4 验收标准；
首批正文。
```

不读：

```text
作者自检；
Source Bible；
writer brief；
版本解释；
旧 reviewer；
旧导演反馈。
```

先判断：

- 像不像短剧；
- 能不能追；
- 淡不淡；
- 像不像改名；
- 像不像说明书；
- 有没有站桩聊天；
- 高压节点有没有冲击；
- 集尾有没有卡住。

### 第二轮：读审计材料

输入：

```text
Source Bible；
Adaptation Boundary；
Source Retention Anchor；
Story Operating State；
Episode function map；
Writer brief；
Beat survival check；
Screenplay draft。
```

检查：

```text
Source Bible -> Source Retention Anchor 是否丢东西；
Anchor -> Episode map 是否丢钩子、爽点、节奏、拉扯；
Episode map -> Writer brief 是否变成结果任务单；
Writer brief -> Screenplay 是否只剩对白/文件/屏幕；
如果失败，失败层在哪里。
```

Reviewer 结论：

```text
pass / revise / block
failure_layer:
callback_target:
reason:
must_fix:
optional:
```

---

## 17. Version comparison / 主控交付判断

沿用 v2。

如有旧版参照，必须比较：

1. 用户指定基线；
2. 上一版；
3. 本版。

比较维度：

| 维度 | 判断 |
|---|---|
| 源本有效性 | 有没有更洗飞 |
| 同构风险 | 有没有更像改名 |
| 短剧场面 | 高压节点是不是更有戏 |
| 钩子 / 卡点 | 是否保留气口，是否提前消费 |
| 爽点 | 是否有蓄力和兑现 |
| 节奏 / 密度 | 是否空转、注水、过冷或过满 |
| 拉扯 / 关系 | 是否有靠近、退开、误会、试探、伤害、保护 |
| 台词 | 是否减少水词、解释腔、同声 |
| 视听承载 | 是否能被 AI 成片看见/听见 |
| continuity | 状态是否接住 |
| 读感 | 是否像短剧，是否像剧本而不是程序 |

主控不能只看 manifest。

主控必须判断：

```text
execution pass
creative pass
source audit pass
delivery pass
```

四者不能互相替代。

---

## 18. 从 v2 / v4 / v5 吸收和降级

### 18.1 v2 保留为主骨架

保留：

- 源本拆文包；
- 洗稿边界包；
- beat sheet / outline；
- Episode function map；
- Scene packet；
- screenplay draft；
- rewrite report；
- dialogue polish；
- quality gate；
- story memory；
- reviewer；
- version comparison。

### 18.2 v4 吸收为连接层

吸收：

- Source Retention Anchor；
- Story Operating State；
- Pressure-chain Writer Brief；
- Pressure-chain Patch Brief。

但它们不能让项目变成原创生成器。

它们只服务：

```text
让源本好看的东西在新壳里继续发动。
```

### 18.3 v5 降级为局部工具

只吸收：

- Scene Option Pitch；
- Scene Choice Gate；
- Version Preference Review。

适用范围：

```text
高压节点；
关键场面迁移；
版本优选。
```

不能用于替代：

- 源本拆文；
- 留存骨架；
- 爽点周期；
- 节奏密度；
- 人物关系；
- 变量迁移；
- 连续性。

---

## 19. v6 成功标准

v6 不以“文档更完整”为成功。

成功标准只有这些：

1. 源本拆文里的钩子、卡点、爽点、节奏、关系、信息差能在 writer brief 里找到；
2. writer brief 不再像审计表，而像可写的故事状态和压力链；
3. screenplay draft 不再像说明书、流程单或程序语言；
4. reviewer 能定位失败层，而不是只说“加强视听语言”；
5. 返修有减法，不再只补动作、补血、补台词；
6. 版本对比能承认旧版局部更好，并把好处吸收回来；
7. manifest 只证明执行，不再冒充质量。

---

## 20. 下一步验证方式

v6 不能直接升正式版。

下一步如果验证，应按同一个源本跑首批样本，但必须做到：

```text
1. manifest-first；
2. 明确使用 v6 草案；
3. 写作前产物必须包含 Source Retention Anchor、Story Operating State、Episode map、writer-facing brief；
4. writer-facing brief 不得夹带完整审计底稿；
5. 正文完成后做 Beat survival check；
6. reviewer 第一轮只读正文；
7. reviewer 第二轮再查源本迁移链；
8. 最后必须和 V3、上一版、局部强版本对比。
```

如果验证失败，不直接补新规则。

先问：

```text
是哪条能力没传下去？
是放错层？
是 writer 输入污染？
是返修只加不减？
还是这套 v6 方向本身不成立？
```
