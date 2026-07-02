# 海外短剧洗稿器 · workflow spec v3 重构草案

> 日期：2026-06-30  
> 状态：草案，不是当前执行版  
> 上游产品定义：`PRD_v4.md`  
> 前一执行版：`workflow_spec_v2.md`  
> 目的：把当前 workflow 从“证明型流程”重构为“分析支持创作、审计独立把关”的流程。  

---

## 0. 本草案解决什么

v2 的流程骨架不是全错。它的问题是：

```text
源本有效性分析
-> 被拆成很多可证明字段
-> writer 拿到过多审计材料
-> 为了防洗飞、防同构、能 pass，优先写可追溯、可解释、可过检的机制戏
-> 正文像流程证明，不像短剧强戏
```

v3 不继续补“视听语言 / 身体反应 / 禁器械 / 拉扯感”等单条规则。

v3 只做一件事：

**把分析、创作、审计、治理拆开。**

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

v3 的核心变化：

**writer 不再读取完整审计底稿。writer 只读写作简报。**

### 2.3 pass 语义混乱

v2 中经常出现：

- manifest pass；
- 作者质量门 pass；
- pass for challenge；
- reviewer pass；
- 版本对比“不低于上一版”。

这些 pass 不等价。

v3 必须拆开：

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

v3 返修先判失败层：

```text
场面发动机坏 -> 回写作简报 / 新壳场面重选
场面动作弱 -> 回 writer brief / scene draft
台词水 -> dialogue polish
源本洗飞 / 同构 -> 回源本审计线
执行证据缺 -> 回 manifest / protocol
```

---

## 3. v3 总结构

```text
0. 最小需求确认
1. 源本分析底稿 Source Bible
2. 洗稿边界包 Adaptation Boundary
3. 高压节点新场面粗验 High-pressure Scene Viability
4. 新本阶段骨架 / 分集功能 Episode Plan
5. Writer Brief 写作简报
6. 干净 writer 正文 Screenplay Draft
7. 作者 rewrite report
8. 作者 dialogue polish / 修订稿
9. 作者 ready check
10. Reviewer 第一轮：只读正文
11. Reviewer 第二轮：读审计底稿查洗飞 / 同构 / 降级
12. 主控判定失败层和回滚点
13. Story memory checkpoint
14. Manifest / 版本记录 / 交付
```

v3 不是增加步骤，而是把 v2 混在一起的东西拆层。

---

## 4. 四条线

### 4.1 分析线

服务对象：主控、审计、writer brief 生成者。

不直接服务 writer。

产物：

- `Source Bible / 源本分析底稿`
- `Adaptation Boundary / 洗稿边界包`

分析线可以厚，可以有 source ref，可以有源本节点编号。

### 4.2 创作线

服务对象：writer。

产物：

- `Writer Brief / 写作简报`
- `Screenplay Draft / 剧本正文`

创作线必须薄，不能带 manifest、质量门、版本对比、完整 source ref 大表。

### 4.3 审计线

服务对象：reviewer、主控。

产物：

- `source carry-through audit`
- `quality gate report`
- `rewrite report`

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
- 当前批次 episode plan；
- 当前集 / 当前高压场 writer brief；
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
| 高压节点粗验 | `scene_card` + `power_shift / visual_executability` | 改造用 |
| Episode Plan | `short-drama episode-directory` + `rhythm-curve` | 改造用 |
| Writer Brief | `scene_card / scene_draft` | 改造用，去掉审计字段 |
| Screenplay Draft | `screenplay_draft / scene_draft` | 直接用剧本合同 |
| Rewrite Report | `rewrite_report` | 直接用 |
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
集数是否变化：
本轮输出范围：
已知禁区：
用户特别想保留什么：
用户特别不想要什么：
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

## 3. High-pressure Scene Viability / 高压节点新场面粗验

### 目标

在完整 beat sheet 之前，先判断高压源本节点的新壳承载是否可行。

这是 v3 新增的结构性前置，不是新增规则表。

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

## 4. Episode Plan / 新本阶段骨架与分集功能

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

## 5. Writer Brief / 写作简报

### 目标

这是 writer 的真正输入。

它不是 scene packet 大表，不是审计表。

### 每集简报

```text
本集观众追问：
本集开头抓人：
本集核心摩擦：
本集最大刺激点：
本集结束前必须改变什么：
本集结尾停在哪一拍：
不能提前消费：
```

### 高压场简报

```text
场面发动机：
谁想要什么：
谁阻止谁：
谁误判谁：
谁必须当众做选择：
谁付出可见代价：
谁获得/失去主动权：
观众应该感到什么：痛 / 爽 / 急 / 气 / 期待 / 心疼
可用工具：文件 / 屏幕 / 道具 / 录音等，只能辅助
禁用外形：源本高辨识桥段 / 道具 / 台词 / 事件链
最后停住的动作 / 声音 / 后果：
```

### writer brief 禁止出现

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

## 6. Screenplay Draft / 剧本正文

### 目标

writer 按简报写正文。

正文必须像剧本，不像说明书、审稿表、流程单。

### 来源

- `how-to-make-script screenplay_draft`
- `scene_draft`
- `short-drama episode`

### 写法底线

- 只写观众能看见 / 听见的东西；
- 高压场必须有行动、空间、身体、他人反应或当众后果；
- 台词短、准、有功能；
- 结尾停在可拍的最后动作 / 声音 / 画面；
- 文件、屏幕、key、录音可以出现，但不能替人物完成戏。

---

## 7. Rewrite Report / 返修诊断

### 目标

初稿后先判断坏在哪层，不直接润色。

### 失败层

```text
concept：产品方向 / 新壳方向错
source_analysis：源本有效性没读出
adaptation_boundary：保留/替换边界错
scene_engine：场面发动机错
episode_structure：分集留存错
screenplay：正文写法错
dialogue：台词问题
continuity：状态追踪问题
execution：流程证据问题
```

### 返修原则

如果是 `scene_engine` 错，不能只加身体反应或润色台词。

---

## 8. Dialogue Polish / 台词修订

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

## 9. Author Ready Check / 作者准备送审检查

### 目标

作者不能给自己质量 pass。

作者只给：

```text
ready for reviewer
needs rewrite
blocked
```

### 检查项

- 是否按 writer brief 写完；
- 是否明显偏离用户需求；
- 是否明显洗飞；
- 是否明显同构；
- 是否明显像说明书 / 流程单；
- 是否有未处理的 rewrite_report hard issue。

作者检查不等于 reviewer pass。

---

## 10. Reviewer 第一轮：正文效果审

### 输入

只读：

- 用户需求摘要；
- 本批正文。

不读：

- 作者自检；
- Source Bible；
- 洗稿边界包；
- writer brief；
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
```

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

## 11. Reviewer 第二轮：源本迁移审计

### 输入

读取：

- Source Bible；
- Adaptation Boundary；
- Episode Plan；
- Writer Brief；
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
```

---

## 12. 主控判定

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
| 场面发动机错 | 高压节点新场面粗验 |
| 分集留存错 | Episode Plan |
| writer 被证明链压住 | Writer Brief |
| 正文像说明书 | Screenplay Draft |
| 台词水 | Dialogue Polish |
| 洗飞 / 同构 | Source Bible / Adaptation Boundary |
| 伏笔/关系漂移 | Story Memory |
| 执行证据缺 | Manifest / Protocol |

---

## 13. Story Memory Checkpoint

### 目标

每批写完保存可继续状态，不重写整本分析。

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

---

## 14. Manifest / 版本记录

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

## 15. 需要删除 / 降级的 v2 内容

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

## 16. v3 成功标准

第一阶段不是证明能自动产出爆款。

v3 的成功标准是：

1. 分析底稿完整，但不污染 writer；
2. writer brief 足够薄，能让 writer 写戏；
3. reviewer 第一轮只读正文也能判断是否像短剧；
4. reviewer 第二轮能定位有没有洗飞 / 同构 / 降级；
5. manifest 不再被误用成质量背书；
6. 返修能回到正确层级，而不是正文层加料；
7. 同一个源本重跑时，正文不再稳定滑向流程证明 / 机制戏。

---

## 17. 下一步验证方式

不要直接跑完整 1-10 集。

先做一个小验证：

```text
同一个源本高压节点
-> 旧 v2 scene packet
-> 新 v3 writer brief
-> 两个干净 writer 分别写同一集或同一高压场
-> reviewer 第一轮只读正文
-> 比较哪一个更像短剧强戏
```

如果 v3 writer brief 仍然写成机制戏，说明重构还没解决问题。

如果 v3 明显减少流程感，再把 v3 扩成正式 `workflow_spec_v3.md`。

