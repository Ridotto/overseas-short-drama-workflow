# workflow spec v6 草案审查

> 日期：2026-07-01
> 审查对象：`workflow_spec_v6_能力回收修正版草案.md`
> 结论：方向成立，但建议小修后再跑样本。

---

## 1. 总判断

v6 没有再把项目带成另一个产品。

它守住了三件事：

1. 产品仍是洗稿，不是从零原创；
2. v2 仍是主骨架，v4 只作为连接层，v5 只作为高压节点局部工具；
3. 原项目里的钩子、卡点、爽点、节奏、拉扯、信息差、连续性、台词、自检 reviewer 都被拉回链路里。

所以 v6 不是废稿。

但它还不能直接拿去跑样本，因为有几个连接点还容易误解。

---

## 2. 主要通过点

### 2.1 产品锚点没漂

v6 开头明确：

```text
把一个已被市场验证或值得参考的短剧源本，洗成一个新壳下仍然好看、能追、能付费的新剧本。
```

这和 `PRD_v4.md` 一致。

它也明确 v5 不扩成主流程，只保留为高压节点局部工具。

### 2.2 原项目能力被拉回来了

v6 不再只盯“场面强不强”。

它补回了：

- 钩子；
- 卡点；
- 爽点周期；
- 节奏密度；
- 主线期待；
- 人物关系；
- 变量迁移；
- 连续性；
- 台词表达；
- reviewer。

这解决了前一版最大问题：把原项目能力压窄。

### 2.3 修的是连接，不是堆规则

v6 的核心链路是：

```text
Source Bible
-> Source Retention Anchor
-> Story Operating State
-> Episode function map
-> writer-facing brief
-> screenplay
-> reviewer
```

这个方向对。

它解决的是“分析有、正文没吃到”的问题，而不是继续补“视听语言规则 / 拉扯规则 / 爽点规则”。

### 2.4 writer-facing brief 是对的

v6 把 writer 输入和审计底稿拆开，这是必要的。

writer 不该拿着 source_ref、carry-through evidence、manifest pass、版本对比证明去写戏。之前剧本像程序，核心原因之一就是 writer 输入太像审计材料。

---

## 3. 必须小修的问题

### 问题 1：`writer 不读审计底稿` 容易被误解成“分析和写作拆成两个互不相干的人”

PRD v4 的原则是：

```text
源本分析和写剧本必须由同一个主创 agent 承担。
```

原因是写作需要继承分析里的创作判断。

v6 说 writer 不读完整审计底稿，这句话方向对，但需要补清楚：

```text
主创可以完整拥有源本分析上下文；
但进入正文写作时，writer-facing brief 不能把完整审计底稿原样塞给写作界面。
```

也就是说，问题不是“同一个 agent 不能知道分析”，而是“写正文时不能被审计表牵着走”。

如果不补这句，后续 agent 可能把分析和写作硬拆开，反而丢掉源本细节。

### 问题 2：`Story Operating State` 的位置可能被理解成一次性前置，后面不更新

v6 当前把 `Story Operating State` 放在 `Beat sheet / outline` 前面。

这不是完全错，但容易有误解：

```text
Story Operating State 不是写一次就固定；
它应该先初始化，再在 Episode function map / writer brief 前刷新。
```

否则它会出现两个风险：

1. 还没做新本阶段骨架，就提前写死故事状态；
2. 到真正写某一集时，状态已经和 episode map 不一致。

建议补一句：

```text
Story Operating State 是写作前状态快照，不是一次性文档；每批、每集或每个高压节点进入 writer brief 前都要按最新 Episode map / Story memory 刷新。
```

### 问题 3：writer-facing brief 现在是“单集级”，但还缺“场景级”承接方式

v6 的 writer brief 写了：

```text
本集压力推进
高压场压力链
正文写法边界
```

这比 v2 好。

但如果一集有多场，它还不够清楚：

```text
哪些场景薄写；
哪些场景厚写；
每场的进入状态和退出状态是什么；
高压场之外的过渡场怎么不空转。
```

这个问题不需要加大表，但要补一个轻量结构：

```text
Scene Sequence：
- Scene 1：功能 / 进入状态 / 动作推进 / 退出状态
- Scene 2：功能 / 进入状态 / 动作推进 / 退出状态
- 高压场追加压力链
```

否则 writer 可能只按“本集任务”写成一坨剧情，而不是可执行剧本。

### 问题 4：`Beat survival check` 有价值，但可能再次变成证明题

v6 新增 Beat survival check 是对的。

但它现在说：

```text
源本高价值节点 -> Anchor -> Episode map -> Writer brief -> Screenplay
```

这很容易被执行者写成长篇证明。

建议补边界：

```text
每批只抽查 3-5 个最高风险节点；
每条只写 3 行：源本体验 / brief 承接 / 正文锚点；
不写长篇解释，不做全量追溯。
```

否则它会把 v6 又拖回证明题。

### 问题 5：v6 还没明确“什么时候可以跳过高压候选”

v6 已经说高压候选只用于高压节点，这是对的。

但还可以再收紧一句：

```text
普通过渡场、低压关系场、功能承接场，不做 Scene Option Pitch。
```

不然执行时可能每场都搞候选，流程又变重。

---

## 4. 不建议改的地方

### 4.1 不要删除 Source Retention Anchor

它是 v6 最关键的连接件。

如果删掉，源本拆文又会直接跳到 episode map，钩子、爽点、节奏、拉扯仍然可能丢。

### 4.2 不要恢复 v2 的完整 Scene packet 给 writer

v2 的 Scene packet 能力很全，但太容易把 writer 变成审计员。

v6 拆成“审计层 scene packet / writer-facing brief”是必要修正。

### 4.3 不要把 v5 继续扩

v5 的场面候选和版本优选有用，但只能局部用。

一旦继续扩成主轴，项目又会丢掉源本留存、爽点、节奏、人物关系和变量迁移。

---

## 5. 是否可以进入样本验证

我的判断：

```text
现在不建议直接跑。
```

先做一次小修，改上面 5 个连接点。

改完后可以跑受控样本。

受控样本必须检查：

```text
1. writer-facing brief 是否真的薄；
2. Source Retention Anchor 里的钩子/爽点/节奏/拉扯是否进入 writer brief；
3. screenplay 是否不再像审计说明；
4. Beat survival check 是否只做轻量抽查；
5. reviewer 能否指出失败层，而不是泛泛说“不够短剧”。
```

---

## 6. 人话结论

v6 的方向是对的。

它已经把原项目能力拉回来了，也没有继续把 v5 放大成主流程。

但还差一步：把几个容易误解的连接口写死。

尤其是：

```text
不是把分析和写作拆开；
而是同一个主创拥有分析判断，但写正文时只吃压缩后的 writer brief。
```

这句话如果不补，后面又会出新的交接问题。

