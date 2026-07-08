# 台词精修 brief

本文件给 `short-drama-write` 的 `/dialogue-polish` 使用。它是项目层固定环节，不是针对某个样片的补丁。

它吸收 `dialogue-subtext`、`wp-dialogue-polish`、`rb-dialogue`、`dialogue-mastery`、`voice-style-guide`、`verbal-rhythm`、`embodied-text-pressure` 和 `short-deslop` 中适合短剧的部分；不整接外部 skill，不接小说写作链，不接机械禁词表。

边界：

- `/episode` 负责把一场戏写出来。
- `/dialogue-polish` 负责把假东西杀掉，让台词更像活人。
- 如果场面本身没戏，不要让 polish 假装能救。

## 根本原则

台词精修不是句子美容，而是用最小改动把下面几类问题清掉：

- 作者总结句；
- 完整句病；
- 假金句；
- 同声线；
- 解释过度；
- 没处境重量的漂亮话。

`/dialogue-polish` 只拥有表达层权限：

- 可以压缩解释句。
- 可以重排对白顺序，让信息进入冲突。
- 可以补少量反应拍、停顿、动作承载。
- 可以让角色声线更分开。
- 可以删除 AI 套话、书面腔、过顺的解释和过于工整的句子。
- 可以保留或增强有效短剧套路句。

不能做：

- 改剧情事实。
- 改本集核心代价。
- 改付费窗口。
- 改真相释放顺序。
- 改人物关系。
- 新增关键桥段或新证据。
- 为了“更高级”削弱短剧强情绪。

如果发现剧情、场面任务、人物欲望或本集代价本身不成立，停止 polish，回 `episode` / `outline` 归因；不要用台词硬补结构问题。

## 输入

执行 `/dialogue-polish {N}` 前必须读取：

- `episodes/ep{NNN}.md`
- `episode-directory.md` 中对应集条目
- `characters.md`
- `creative-plan.md`
- `source-handoff.md`
- `07_禁抄边界.md`
- `dialogue-force-brief.md`
- `performance-dialogue-brief.md`
- `/Users/jiakun/Codex/自动化编剧/.local-archive/obsolete-worktrees-2026-07-04/自动化编剧-external-chain-rebuild/external_full_repos/how-to-make-script/examples/golden/dialogue-polish/artifact.md`
- `/Users/jiakun/Codex/自动化编剧/.local-archive/obsolete-worktrees-2026-07-04/自动化编剧-external-chain-rebuild/external_full_repos/how-to-make-script/examples/reference-packs/character-voice-reference-pack.md`
- `/Users/jiakun/Codex/自动化编剧/.local-archive/obsolete-worktrees-2026-07-04/自动化编剧-external-chain-rebuild/external_full_repos/how-to-make-script/examples/failures/fail-002-voice-collapse.md`
- `/Users/jiakun/Codex/自动化编剧/.local-archive/obsolete-worktrees-2026-07-04/自动化编剧-external-chain-rebuild/external_full_repos/oh-story-claudecode/skills/story-short-write/references/dialogue-mastery.md`
- `/Users/jiakun/Codex/自动化编剧/.local-archive/obsolete-worktrees-2026-07-04/自动化编剧-external-chain-rebuild/external_full_repos/oh-story-claudecode/skills/story-short-write/references/short-deslop.md`

批量执行时，必须按集数顺序读前文状态增量，避免把已心死、已失权、已破防或已交权的角色写回旧状态。

## 台词精修步骤

### 0. 先判断能不能在 polish 层解决

精修前先检查：

- 主要角色是否有表达锚点和台词武器表；
- 当前集是否有 `本集对话压力方向`；
- 旧项目若只有 `本集台词冲突任务`，按同一字段理解；
- 正文是否已经写出了场上争位置，而不只是事件说明；
- 关键台词或沉默是否改变关系、权力、信息、行动条件、体面或安全。

如果缺的是上游输入或正文执行，停止 polish 并归因。只有句长、节奏、解释、声线、反应拍、AI 味这类表达层问题，才留在本步骤修。

### 1. 锁住不可改项

先列出本集不可动的内容，不需要输出给用户，但修改时必须遵守：

- 本集赚钱功能。
- 本集一眼可懂代价。
- 本集释放 / 继续扣住的信息。
- 本集关系位置变化。
- 本集结尾债务。
- 本集状态增量。

这些内容不清楚时，不能继续 polish。

### 2. 给每个主要角色立一张极短的表达卡

每个主要说话者先内部确认 4 件事：

- **voice anchor**：这个人最稳定的表达重心。
- **pressure drift**：被逼急时怎么偏。
- **register 禁区**：什么句子一出现就不像他。
- **allowed variation**：这场戏里允许更短、更狠、更绕，还是更急、更碎。

这里用 `characters.md` 里的材料，不重新发明角色。

### 3. 给每场对话找真实目标

每个角色进入一场对话，都必须有议程：

- 想逼对方退让。
- 想掩盖真相。
- 想让旁观者站队。
- 想试探对方知道多少。
- 想保住体面。
- 想刺痛对方软肋。
- 想争取时间。
- 想把责任推给别人。

角色的表面话和真实目标可以不同。没有真实目标的台词，多半是作者在解释设定。

### 4. 先判硬伤，再修句子

下面这些先判为硬伤，不要边修边放过：

- 主要角色说话遮住名字后仍像同一个人。
- 高压场景里所有人都用完整、均衡、过分准备好的句子。
- 关键冲突全靠解释推进。
- 角色说的是作者总结，不是当场要说的话。
- 反派把自己的羞辱策略说得太明。
- 被压角色把委屈写成逻辑辩论。
- 关键高压回合只有裸对白，没有动作、物件、沉默或站位承接。

如果这些硬伤存在，不能只做轻微润色后放行。

### 5. 压缩说明书式信息

以下台词要压：

- 读者已经知道的信息。
- 角色不该在高压场合完整解释的背景。
- 连续陈述制度、流程、合同、授权、调查结果。
- 问答式一问一答，只为了把信息说完。

压法：

- 把完整说明改成半句话。
- 把说明移到动作、物件、屏幕、门牌、徽章、投票、沉默里。
- 让对方打断、否认、抢夺、转移责任。
- 保留会改变权力、关系、行动条件的信息，删掉说明欲。

如果压完后观众看不懂本集代价，说明不是台词问题，是场面动作承载不足，回 `/episode`。

### 6. 校正句长和节奏

短剧台词经常靠句长表现权力，但不能机械套模板。

- 掌控者通常更短、更冷、更少解释。
- 被压者通常更急、更长、更想证明。
- 装弱者通常更绕、更软、更借旁观者施压。
- 心死者会从解释变成短句、停顿、动作决定。

做一遍内部朗读测试：

- 读出来是不是所有人都一个速度、一个长度、一个冷静度？
- 哪里该被打断却没有？
- 哪句太完整，完整得像排练过？
- 哪句太漂亮，一看就是作者在找句子？

项目正文不用 `…… / —— / --` 做节奏，改用短句、换行、动作 beat、半句话和沉默。

### 7. 把处境重量补回台词

活人感不来自更华丽的词，而来自压力真的进了嘴。

关键句后优先补这些承接：

- 手、门、门禁、座位、徽章、药、玻璃、手机、录音、胸牌、伤口。
- 视线移开、手停住、声音发干、站位改变、称呼变化。
- 先处理眼前风险，再顾得上说完整的话。

不要给每句机械配动作。只在权力变化、情绪断裂、信息爆开、钩子形成时补。

### 8. 去 AI 味，但不洗掉短剧火气

删或改：

- 空泛情绪总结：`仿佛世界失去颜色`、`一丝痛楚涌上心头`。
- 标签腔：`沉声道`、`淡淡地说`、`嘴角微扬`。
- 论文体：`事实上`、`由此可见`、`不难看出`。
- 过度工整的审判排比。
- 太漂亮但没处境重量的句子。
- 所有人都完整句、解释句、同一种冷静。
- 弱化副词扎堆：`微微`、`淡淡`、`缓缓`、`轻轻`。

保留：

- 有具体反应承载的强情绪。
- 有功能的短剧短句。
- 常见但有效的冲突话术。
- 角色心死、反杀、拒绝、火葬场的直给句。

判断标准：这句是否服务当前角色的目标、压力和关系位置。服务就留；只是漂亮、顺滑、说明、总结，就删。

## 禁抄口径

`/dialogue-polish` 不能用机械字符串黑名单。

常见人名、通用短句、短剧套路句、常见动作功能可以保留。只有当台词和源本形成高识别组合时才改：

- 同一关系。
- 同一场景。
- 同一道具或调度。
- 独特长句表达。
- 同一事件顺序。

如果只是 `don't touch me`、`go away`、`leave` 这类常见短句，不得单独作为返工理由。

## 输出

执行后保存：

- 覆盖 `episodes/ep{NNN}.md` 为当前 canon。
- 如有旧稿，先保存到 `episodes/_drafts/ep{NNN}_pre_dialogue_polish.md`。
- 批量执行时逐集保存。

文件末尾必须保留并同步 `## 状态增量`。台词精修不能新增状态事实；只允许把已写出的状态表达得更清楚。

同时在本集末尾追加一段很短的内部记录：

```markdown
## Dialogue Polish Notes

- 处理重点：
- 声线修正：
- 反应拍：
- 未改动的硬约束：
```

最终 `/export` 时必须移除 `Dialogue Polish Notes` 和其他内部字段，不进入用户交付稿。

## 快速自检

- 每个主要说话者是否有真实目标？
- 这场戏里主要角色遮住名字后还能区分吗？
- 是否还有作者总结句、完整句病、假金句？
- 是否存在大段说明书式对白？
- 掌权 / 失权 / 心死 / 装弱的句长是否变化？
- 压迫性台词后是否有必要反应拍？
- 是否误删了有效短剧套路句？
- 是否新增了剧情事实？如果新增，必须撤回。
