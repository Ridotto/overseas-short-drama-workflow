# 外部 skill / reference 接入地图：长线状态、角色追踪、真相释放

日期：2026-07-04

## 结论

之前把“长线多批次状态包”说成只在第 11 集以后或 60-80 集续写时启用，这个判断不准。

正确判断是：

```text
只要目标是做一部完整短剧，从 /plan 开始就必须有全剧追踪骨架。
首批 1-10 集可以只输出前十集正文，但不能只按“独立前十集样片”来设计。
```

原因很简单：前十集不是孤立样片，它是完整剧的第一段销售入口。它必须知道全剧核心真相、关系变化、火葬场债务、付费压力和后续不能提前消费的东西。否则第一批很容易把强真相提前说完、把角色关系写死、把后面 50-80 集的追看空间吃掉。

但这不等于增加一个重 gate，也不等于让 writer 每次读一堆网文参考。正确做法是：

```text
/plan 生成全剧追踪骨架
/outline 把骨架压成当前批执行状态
/episode 每集只吃本集速记
每集完成后更新状态增量
下一批开始前再生成/刷新 batch-state
```

## 不做什么

不整包接 `story-long-write`、`story-short-write`、`story-review`、`story-deslop`。

不把网文、小说、电影、电视剧方法直接塞进短剧主链。

不让 writer 每次先读完整外部项目。

不增加“必须反复返工到完美”的 gate。状态追踪是输入压缩和连续性保护，不是卡死生产的审核门。

不把外部内容变成“参考一下”。凡是要接入，必须落到以下之一：

- `creative-plan.md` 里的全剧蓝图和追踪骨架；
- `characters.md` 里的角色欲望、关系反应、状态变化和声线；
- `episode-directory.md` 里的当前批小 draft、释放/扣留、状态 beat、下集债务；
- `/episode` 写作前的本集速记；
- `/review` 的责任归因。

## 本轮完整阅读记录

这里的“已读”只表示本轮主控亲自打开并读完目标文件全文，不是摘要，不是目录扫描，不是听别人转述。

### 当前主链与已接入短剧标准库

已完整读过并作为当前主链事实：

- `shortdrama-remix/README.md`
- `shortdrama-remix/contracts/short_drama_form_lock_v1.md`
- `shortdrama-remix/skills/source-import/SKILL.md`
- `shortdrama-remix/skills/source-import/references/README.md`
- `shortdrama-remix/skills/short-drama-write/SKILL.md`
- `shortdrama-remix/skills/short-drama-write/README.md`
- `shortdrama-remix/skills/short-drama-write/LICENSE`
- `shortdrama-remix/skills/short-drama-write/.gitignore`
- `shortdrama-remix/skills/short-drama-write/references/` 下 8 个短剧 reference
- `shortdrama-remix/vendor/short-drama/SKILL.md`
- `shortdrama-remix/vendor/short-drama/references/`，已与本地 8 个 reference 做一致性确认

### 长线状态 / 续写 / 真相释放候选

已完整读完：

- `vendor/oh-story-claudecode/skills/story-import/SKILL.md`
- `vendor/oh-story-claudecode/skills/story-import/references/state-tracking.md`
- `vendor/oh-story-claudecode/skills/story-import/references/character-state-reverse.md`
- `vendor/oh-story-claudecode/skills/story-import/references/length-routing.md`
- `vendor/oh-story-claudecode/skills/story-import/references/format-and-structure.md`
- `vendor/oh-story-claudecode/skills/story-import/references/structure-mapping-short.md`
- `vendor/oh-story-claudecode/skills/story-import/references/structure-mapping-long.md`
- `vendor/oh-story-claudecode/skills/story-long-write/SKILL.md`
- `vendor/oh-story-claudecode/skills/story-long-write/references/state-tracking.md`
- `vendor/oh-story-claudecode/skills/story-long-write/references/workflow-daily.md`
- `vendor/oh-story-claudecode/skills/story-long-write/references/workflow-revision.md`
- `vendor/oh-story-claudecode/skills/story-long-write/references/cross-book-recall.md`
- `vendor/oh-story-claudecode/skills/story-long-analyze/SKILL.md`
- `vendor/oh-story-claudecode/skills/story-long-analyze/references/material-decomposition.md`
- `vendor/oh-story-claudecode/skills/story-long-analyze/references/output-templates.md`
- `vendor/oh-story-claudecode/skills/story-long-analyze/references/pipeline-ops.md`

可迁移结论：

- `追踪/伏笔.md`、`时间线.md`、`角色状态.md`、`上下文.md` 的思想有用，但不能照搬成小说工程目录。
- “本节速记”非常适合改造成短剧的“本集速记”：只给本集写作必须知道的角色状态、真相释放、未偿债务、禁提前消费项。
- 每章后更新追踪的思想有用，但短剧里应变成“每集完成后更新状态增量”，不能让它变成每集都大修蓝图。
- `剧情/节奏.md`、`剧情/情绪模块.md` 作为权威输入的思想有用，应转成我们自己的“全剧节奏/情绪模块骨架”，进入 `/plan` 和 `/outline`，而不是让 writer 直接读网文长篇文件。

### 角色关系 / 情绪 / 商业节奏候选

已完整读完：

- `story-long-write/references/character-relations.md`
- `story-long-write/references/character-design-methods.md`
- `story-long-write/references/emotional-arc-design.md`
- `story-long-write/references/plot-emotion-system.md`
- `story-long-write/references/outline-rhythm.md`
- `story-long-write/references/commercial-core-methods.md`
- `story-long-write/references/outline-conflict.md`
- `story-long-write/references/plot-core-methods.md`
- `story-long-write/references/opening-design.md`

可迁移结论：

- 角色关系最有用的不是“关系类型表”，而是“关系必须有变化弧线、重要关系要有考验、配角不能站桩、角色行为由欲望/恐惧/当前状态推导”。
- 情绪弧最有用的是“调动和释放必须成对”“闭环一个期待时下一个开环已在运行”“解决一个麻烦时埋下下一个麻烦”。
- 商业核心最有用的是“核心卖点不能偏移”“同一卖点可以多角度重复”“每段剧情必须知道自己在卖什么情绪”。
- 冲突结构最有用的是“每个事件要有价值改变”“冲突必须有明确结果”“信息只有变成观众疑问才有价值”。
- 这些都应该被编进我们自己的短剧执行口径，不应该让 writer 每次直接读长篇网文 reference。

### 短篇网文写作候选

已完整读完 `story-short-write/references/` 下全部文件：

- `banned-words.md`
- `cross-book-recall.md`
- `dialogue-mastery.md`
- `emotional-methods.md`
- `genre-writing-formulas.md`
- `genre-writing-techniques.md`
- `hooks-chapter.md`
- `hooks-paragraph.md`
- `hooks-suspense.md`
- `output-contract.md`
- `quality-checklist.md`
- `reversal-toolkit.md`
- `short-craft.md`
- `short-deslop.md`
- `short-format.md`
- `villain-and-reveal.md`
- `writing-workflow.md`

可迁移结论：

- `short-craft.md` 的“情绪宁烈不温”“情绪必须接具体动作/物件”“疏密分配”“一动一静”有用，但它是短篇网文，不是短剧剧本，不能整接。
- `dialogue-mastery.md` 的权力博弈、心死模式、对话议程、声线差异有用，可转成短剧台词和人物反应要求。
- `hooks-*` 和 `reversal-toolkit.md` 的期待链、真相释放、反转铺垫有用，但要转成“本集释放/继续扣住/下一债务”，不能沿用章节字数和短篇小说结构。
- `short-deslop.md` 比长篇去 AI 味更接近我们的需求：它强调不能误删有功能的强情绪。但它仍是网文口径，只能抽轻 polish 原则，不能做整套 reviewer。
- `banned-words.md` 太容易把有效短剧套路洗掉，不接成机械禁词。
- `output-contract.md` 是 story-short-analyze 与 story-short-write 的文件契约，不适合直接进入当前短剧主链。

### how-to-make-script 候选

已完整读完：

- `skills/scene-writing/SKILL.md`
- `knowledge/20-workflows/wp-scene-writing.md`
- `knowledge/60-rubrics/rb-scene-draft.md`
- `skills/dialogue-subtext/SKILL.md`
- `knowledge/20-workflows/wp-dialogue-polish.md`
- `knowledge/60-rubrics/rb-dialogue.md`

可迁移结论：

- 场面写作、潜台词、对白经济有用。
- 不能带入电影/电视剧的可拍性和镜头课口径。
- 适合做成短剧本地瘦身 reference，强制服务 `/episode` 和 `/review`，但不能让它们决定剧情。

### shortdrama-pipeline 候选

已完整读完：

- `vendor/shortdrama-pipeline/README.md`
- `vendor/shortdrama-pipeline/docs/ARCHITECTURE.md`

没有读完：

- `harness.py`
- `models.py`
- `pipeline.py`
- `prompts.py`

判断：

- 只可借鉴 `runs/`、`latest/`、状态机、approved assets 这类产物管理思想。
- 不进入短剧文本创作能力。
- 代码未读，所以不能声称借用了它的 pipeline 逻辑。

## 未读且不得作为依据的范围

以下内容本轮没有完整读完，因此不得在后续改造中偷偷拿来当依据：

- `story-review/references/`
- `story-review/scripts/`
- `story-deslop/scripts/`
- `story-short-write/scripts/`
- `story-long-write/references/` 中未在上面列出的其他文件
- `story-long-write/scripts/`
- `shortdrama-pipeline` 的 Python 代码文件
- 各外部项目没有列入候选的其他文档

如果后续要从这些文件中抽能力，必须先单独完整读完目标文件，再写接入判断。

## 长线追踪什么时候启用

### 默认启用：从 /plan 开始

只要用户的目标是“做一部剧”，即使当前只先输出前十集，也默认启用轻量全剧追踪骨架。

`/plan` 应该生成或内嵌：

- 全剧核心卖点和不能偏移的主情绪；
- 长期真相账本：哪些真相早揭、晚揭、不能揭；
- 关系状态账本：核心关系从哪里到哪里，哪些关系不能倒退；
- 角色状态账本：主角、主要反派、火葬场对象在全剧中的欲望、恐惧、面具、破防点；
- 伏笔 / 债务账本：哪些债务必须回收，哪些钩子不能空头；
- 爽点兑现账本：已兑现什么，后面不能重复同一方式空转。

这不是给用户看的额外表格，而是蓝图的一部分。用户看到的是自然语言小 draft，下游吃到的是同一内容的执行锚点。

### 当前批启用：/outline 必须压成前十集执行状态

`/outline` 不只是列 1-10 集剧情，还要把全剧追踪骨架压成当前批状态：

- 本批释放哪些真相；
- 本批继续扣哪些真相；
- 本批每集让哪个角色位置变化；
- 本批每集偿还什么，又留下什么债；
- 哪些后续大真相不能在本批提前消费；
- 哪些源本强功能已经迁移，哪些还欠着。

这一步必须影响 `episode-directory.md`，否则追踪只是摆设。

### 单集启用：/episode 只吃本集速记

writer 写第 N 集时，不应该重读全套长线文档。它只需要本集速记：

```text
上一集状态：
本集必须推进的关系/真相/债务：
本集不能提前说破的答案：
本集必须可见的代价：
本集结束后必须留下的新状态：
```

这样既能保住长线，又不会让上下文太厚、注意力飘移。

### 每集完成后更新状态增量

每集写完后，只更新“增量”，不重写全剧：

- 新释放了什么；
- 谁知道了什么，谁还不知道；
- 哪段关系发生了不可逆变化；
- 哪个角色的面具裂了，或新的伪装成立了；
- 哪个债务已偿还，哪个债务转成下一集/下一批债务；
- 哪个桥段/动作已用过，后面不要重复空转。

### batch-state 的新定位

`batch-state.md` 不应该是“第 11 集以后才第一次出现的东西”。

它的新定位应该是：

- 首批写作时，状态骨架在 `creative-plan.md` 和 `episode-directory.md` 中已经存在；
- 首批正文完成后，生成或刷新 `batch-state.md`；
- 继续第 11 集以后时，必须先读取 `batch-state.md`；
- `batch-state.md` 不能替代下一批蓝图，只负责把已确认事实、关系状态、真相释放和禁区带过去。

## 建议接入形态

### 1. 新增本地 reference：`series-state-brief.md`

来源：

- `state-tracking.md`
- `workflow-daily.md`
- `workflow-revision.md`
- `plot-core-methods.md`
- `story-long-analyze` 的节奏/情绪模块思想

只保留：

- 全剧追踪骨架；
- 本集速记；
- 每集状态增量；
- batch-state 续写协议；
- 热 / 暖 / 冷元素风险；
- 真相释放、关系状态、角色状态、未偿债务。

禁止带入：

- 网文章节阈值；
- 每 3 章、每 50 章这类小说工程规则；
- 卷/书/地图体系；
- 强制每集回上游重修的 gate。

### 2. 新增或合并本地 reference：`performance-dialogue-brief.md`

来源：

- `how-to-make-script / scene-writing`
- `how-to-make-script / dialogue-subtext`
- `story-short-write / short-craft.md`
- `story-short-write / dialogue-mastery.md`
- `story-short-write / short-deslop.md`

只保留：

- 场面必须产生变化；
- 压迫性台词后必须有可见反应链；
- 情绪不能只写“看了一眼、转身离开”；
- 冷静角色可以冷静，但要让场面更痛、更压、更羞辱；
- 台词必须有角色目标、关系位置和权力差；
- 去 AI 味只能压表达、删空话、补动作承载，不能改剧情。

禁止带入：

- 泛影视镜头课；
- 小说第一人称内心独白；
- 机械禁词；
- 为了“自然”把短剧强情绪磨掉。

### 3. 不新增一堆 agent

当前产品形态仍然应该是：

```text
主控 agent
  -> source-import
  -> short-drama-write
  -> clean reviewer
```

外部参考优先变成本地 brief 或被编入现有 skill。只有当某个环节需要独立产物并有清晰输入输出时，才考虑单独 agent。

目前不建议为长线追踪新开常驻 agent。它应该是 `short-drama-write` 的状态能力，而不是新的工作流。

## 对当前文件的影响判断

当前 `skills/short-drama-write/SKILL.md` 已经有很多正确能力：

- `/plan` 已经要求信息流、全剧粗纲、当前批集纲、当前批状态与禁区；
- `/characters` 已经要求欲望、恐惧、面具、关系反应、声线；
- `/outline` 已经要求本集释放/继续扣住、人物状态 beat、下集债务；
- `/episode` 已经要求动作链、人物状态、视听语言、反应链；
- `/review` 已经有信息释放、人物状态、连贯性和 callback。

真正缺口不是“没有这些词”，而是：

```text
长线状态还没有被明确成从 /plan 开始的全剧追踪骨架；
/episode 还没有明确只吃本集速记；
每集写完后的状态增量还没有成为固定动作；
batch-state 的定位还停留在“多批次后启用”，这会误导后续 agent。
```

所以后续修改应该很克制：

1. 改 `README.md` 和架构检查点，纠正“长线只多批次启用”的口径。
2. 在 `skills/short-drama-write/references/` 新增 `series-state-brief.md`。
3. 在 `skills/short-drama-write/references/` 新增或合并 `performance-dialogue-brief.md`。
4. 小改 `short-drama-write/SKILL.md`：
   - `/plan` 生成全剧追踪骨架；
   - `/outline` 生成当前批状态；
   - `/episode` 写前读取本集速记，写后更新状态增量；
   - `/batch-state` 改为续写前的批次状态汇总，而不是唯一长线入口。
5. 不改样本文本，不先跑 clean run。只有可执行文件改完后，再跑新样本验证。

## 给用户看的解释

长线能力不是“以后写到第 11 集再打开”，而是“从一开始就知道这是一部完整剧，只是先交付前十集”。

但用户不需要看到一堆工程表。用户应该看到的是完整自然语言蓝图：这部剧讲什么、人物怎么变、真相怎么放、前十集为什么抓人、后面还欠什么。

writer 也不应该被一堆外部参考污染。writer 应该吃到的是已经压缩好的本集速记和执行锚点。

这才是既保住完整剧，又不把系统做成规则怪谈的做法。
