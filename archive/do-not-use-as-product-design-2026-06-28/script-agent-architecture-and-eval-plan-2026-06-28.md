# 剧本 Agent 架构与评估修正

日期：2026-06-28  
目的：回答当前最核心的 4 个问题：

1. 这是不是一个多 agent 系统的集合版？
2. 刚才为什么分析不出什么好什么坏？
3. 后面怎么避免过拟合和拍脑袋标准？
4. 现有标准有没有市场验证，市面上有没有更好的现成方案？

## 1. 先说结论

### 1.1 这确实应该是“多 agent / 多模块集合版”

但不是“所有东西都交给 agent”。

更准确地说，它应该是：

> 一个由确定性解析层、多个独立判断层、一个重构层、一个回归验证层组成的系统。

其中：

- **该用代码/解析器的地方**不要用 agent
- **该用独立判断的地方**才用多个 agent

### 1.2 刚才分不出强弱，不是偶然，是系统设计问题

主要不是模型笨，而是我们给它的任务定义混了。

我们把这些东西揉成了一个总分：

- 剧本叙事强不强
- 适不适合海外真人短剧市场
- 适不适合拍
- 适不适合 AI 视频生成
- 合规/品牌风险高不高

这会导致一个典型错误：

> 一个故事机制其实很强，但因为贵、难拍、风险高，被一起压成 `medium`。  
> 一个故事其实很虚，但因为钩子猛、stakes 大、留存强，也被抬成 `medium`。

所以 V1 和 V2 blind test 才会出现“稳定，但拉不开”的现象。

### 1.3 现在这套标准没有被完整市场验证过

必须直接说清楚：

- **整套 full-stack 标准没有被市场验证过**
- **它只是一个 bootstrap 版**
- 它不是拍脑袋乱写，但也还不是“行业真理”

更准确的说法是：

- 里面的**局部维度**很多有行业依据
- 但**这些维度怎么加权**，目前没有被你的业务数据校准

### 1.4 市面上没有一个现成的完整答案

公开市场里没有看到一个成熟系统同时解决：

```text
旧剧本强机制分析
-> 深度重构
-> 新剧本生产
-> 海外真人短剧市场判断
-> AI 视频制作交付
```

市面上更像是：

- 有的擅长 coverage / analysis
- 有的擅长 production / storyboard / video
- 有的擅长 writing skills / prompts

但没有一个能把整条链打通，而且还经过你这种业务目标的验证。

所以正确路线不是“找现成完美系统”，而是：

> 借外部成熟子模块的思路，再用你自己的语料和结果标签把权重校准出来。

## 2. 这系统到底该怎么拆

### 2.1 推荐架构

不要把它想成一个“大编剧 agent”。

应该先按“上游分析系统”拆，而不是先按“全链路产品”拆。

当前最值得保留的上游结构是：

1. **Corpus / Intake**
   职责：导入 `docx/pdf/txt/fdx/粘贴文本`，记录来源、版本、是否污染、是否可用于 blind  
   形式：代码，不是 agent

2. **Story Spine Analyzer**
   职责：先吃整部剧的主脉络、阶段划分、主线推进、episode engine、关系推进、payoff 链  
   形式：LLM pass

3. **Mechanism Extractor**
   职责：在剧情脉络之上，再抽强机制，不只看剧情表面  
   形式：LLM pass

4. **Narrative Judge**
   职责：只判断叙事强度  
   形式：独立 agent 或独立 pass

5. **Rewrite Planner**
   职责：保留机制，替换表皮，出重构方案  
   形式：agent

6. **Regression Judge**
   职责：新稿生成后，检查强点有没有丢  
   形式：独立 agent

注意：

- `AI视频适配` 不是独立 judge 主评分，而是约束层。
- `合规` 不是独立 judge 主评分，而是风险标记层。
- `市场` 当前也不是主评分层，而是标签层。

### 2.2 真正需要多 agent 的地方

不是所有环节都需要多 agent。

真正该多 agent 的只有三类：

1. **独立判断**
   例如 Narrative / Market / Production / Compliance 分开判

2. **对抗审查**
   一个 agent 说强，另一个 agent 专门找它的问题

3. **pairwise comparison**
   不是只打绝对分，而是直接比较 A 和 B 谁更强

### 2.3 不该用 agent 的地方

这些应该尽量程序化：

- 文本导入
- 污染状态管理
- episode/scene 切分
- 行号索引
- YAML/JSON schema 落盘
- 结果聚合
- score 统计

否则噪音太大。

## 3. 刚才为什么分不出强弱

### 3.1 根因 1：目标函数混了

这是最大的根因。

你要的“好剧本”，业务上其实至少是 4 个问题：

1. 叙事强不强
2. 市场上卖不卖得动
3. 能不能拍
4. 能不能安全上线

这四个不是一回事。

### 3.2 根因 2：强稿和弱稿都可能有高 hook

我们刚才测出来最重要的事就是：

- 弱稿也可以很会钩人
- 弱稿也可以 stakes 很大
- 弱稿也可以 retention 很强

所以这些维度只能当“入场门槛”，不能当主要区分项。

### 3.3 根因 3：现在的标签太粗

目前手里主要是：

- 星级
- general 评价

但没有：

- 哪一集流失
- 哪一集付费
- 哪个 hook 更能投流
- 哪个角色关系更能撑完播
- 哪个桥段导演/监制觉得不能拍

所以标签本身很弱。

### 3.4 根因 4：样本量太少

现在只有少量强弱样本，还是不同格式混排。

在这种情况下，如果强行定权，就很容易过拟合。

### 3.5 根因 5：过分依赖绝对打分

很多时候：

- “这本是不是 strong”

不如：

- “A 和 B 哪本更强，为什么”

更容易判断。

所以 pairwise comparison 会比 absolute scoring 更适合早期。

## 4. 怎么避免过拟合

### 4.1 不要直接学“最好的剧本长什么样”

因为你自己也说了：

> 你拿不到真正意义上的全市场最优剧本。

所以系统不应该学“唯一正确模板”，而应该学三层：

1. **通用叙事层**
   goal / stakes / choice / reversal / payoff / relationship growth

2. **市场层**
   哪些 trope、钩子、付费点在目标市场更有效

3. **私有语料层**
   你的历史剧本和业务结果里，哪些机制真的有效

### 4.2 数据集要分三层

不要一锅炖。

建议拆成：

1. **exploration set**
   用来发现机制

2. **calibration set**
   用来调权重

3. **holdout blind set**
   用来测系统

如果混在一起，永远会高估系统能力。

### 4.3 每条规则都要有状态

不是写进 rubric 就算真理。

每条规则都应该有：

```yaml
RuleCard:
  source:
  source_type:
  hypothesis:
  validation_status:
  market_scope:
  stale_risk:
```

状态至少区分：

- `untested`
- `supported`
- `contradicted`
- `stale`

### 4.4 用“伪强点惩罚”专门打假

现在最危险的是：

> 一堆剧本看起来很强，其实只是刺激很强。

所以应该单独设：

- `pseudo_strength_penalty`

重点打这几类：

- repeated_humiliation_loop
- misunderstanding_dependency
- rescue_dependency
- control_without_relationship_growth

### 4.5 周期性刷新市场判断

海外真人短剧变化快。

所以市场层和 production 层不能永久固化，至少要周期刷新。

## 5. 这套标准哪些是有行业依据的

### 5.1 有依据的部分

这些不是凭空造的：

- `场景级续看欲`
  参考 [ScriptReader.ai](https://scriptreader.ai/)
- `剧情/角色/结构/节奏/logic/dialogue` 这类 coverage 维度
  参考 [The Black List](https://help.blcklst.com/), [Shore Scripts](https://www.shorescripts.com/screenplay-coverage/)
- `受众/market fit/comps`
  参考 [StoryFit](https://storyfit.com/), [Largo.ai](https://home.largo.io/largo-content-insights/)
- `生产拆解`
  参考 [Filmustage](https://filmustage.com/script-breakdown/)
- `短剧诊断维度`
  参考 [剧拆拆](https://www.juchaichai.com/)
- `前 3 秒钩子`
  参考 [TikTok Creative Best Practices](https://ads.tiktok.com/help/article/creative-best-practices)

### 5.2 没有被完整验证的部分

这些部分现在还没有被市场完整验证：

- 这些维度在“海外真人短剧”里到底怎么加权
- production/compliance 到底该多大程度影响“好剧本”判断
- 你的历史剧本里哪些机制才真正对应 ROI / 完播 / 甲方购买

所以现在不能说：

> 我们已经有行业标准了

只能说：

> 我们已经有一套带行业依据的 bootstrap 标准，但还没被你的业务数据校准。

## 6. 市面上有没有更好的

### 6.1 有更好的“局部”

但没有更好的“整体”。

更好的局部包括：

- 剧本 analysis / coverage：StoryFit、Largo、ScriptBook、Callaia、Prescene、OnDesk、ScriptReader.ai
- 中文短剧诊断：剧拆拆、创一AI/咔咔猩
- 生产链 / 开源：Jellyfish、Toonflow、LocalMiniDrama、Huobao Drama

### 6.2 没有更好的“一体化成品”

至少公开信息里没有。

所以你的问题不是“要不要找个现成更好的”，而是：

> 哪些现成模块值得借，哪些必须自己校准。

## 7. 现在到底该怎么改

### 7.1 立刻要做的

1. 固定 V2 的分层输出
   NarrativeStrength / ProductionSuitability / ComplianceRisk / MarketFit

2. 新增 `pseudo_strength_penalty`

3. 不再只做 absolute scoring
   加 pairwise comparison

4. 强弱样本继续 blind 跑
   但先不要扩大样本量太快

### 7.2 接下来一轮评估应该怎么设计

下一轮建议这样做：

1. 每份剧本先独立打：
   `NarrativeStrength`
   `ProductionSuitability`
   `ComplianceRisk`
   `MarketFit`

2. 再做 pairwise：
   `A vs B 哪本叙事更强`
   `A vs B 哪本更适合拍`
   `A vs B 哪本更适合海外真人短剧`

3. 再揭晓标签做对照

### 7.3 真正的多 agent 系统该怎么演进

先后顺序应该是：

1. **先把判别器做稳**
2. **再把重构器接上**
3. **再把 writer 接上**
4. **最后才做 production handoff 全链路**

别反过来。

如果判别器不稳，后面的 writer 和重构器只会把错误放大。

## 8. 当前最重要的真实结论

你现在最该信的不是哪个脚本被判成什么，而是下面这三条：

1. 这个系统现在还**不够强**，因为它能稳定评论，但还不能稳定拉开强弱。
2. 问题不在“模型完全不会分析”，而在“判别目标和权重结构设计不对”。
3. 方向不是继续拍脑袋写标准，而是：
   **用行业已有的局部标准做 bootstrap，再用你的私有数据做校准。**
