# 台词强度与外部参考代码级审计

日期：2026-07-06

> 定位：本文件是台词强度专项审计，只服务“台词太平 / dialogue force”问题。外部写作能力总路线以 `writing_capability_external_audit_2026-07-06.md` 为准。

范围：

- 当前主链：`shortdrama-main-controller`、`source-import`、`short-drama-write`、本地 references、contracts。
- 当前业务样本：`源本库/灰烬新生` 的蓝图、角色、集纲、正文、polish、review、run log。
- 外部归档：`external_full_repos` 下 `short-drama`、`oh-story-claudecode`、`how-to-make-script`、`shortdrama-pipeline`、`dramatron`。

本文件只做审计，不修改执行链。

## 短结论

当前项目不是完全没有台词层。

它已经有：

- `/characters` 的声线倾向；
- `/episode` 的视听表演、反应链、台词议程；
- `/dialogue-polish` 固定环节；
- `/review` 的台词评分与责任归因。

但它们现在更像“原则提醒 + 轻 polish”，还没有形成“短剧台词强度生产机制”。所以模型能写出剧情正确、动作也对，但台词仍然偏客观、偏冷静、偏说明，尤其在已经锁定结构以后，`/dialogue-polish` 容易为了避免误伤而把自己降级成低风险修字。

这次 `灰烬新生` 的核心漏点就是这个：流程走了，但台词层没有真正出力。

## 当前链路证据

### 1. 主控确实把台词精修放进正式流程

`shortdrama-main-controller/SKILL.md` 的默认流程是：

```text
当前批正文 -> 台词精修 -> internal review / 自检返修 -> clean reviewer 内容验收
```

也就是说，项目设计上已经承认 polish 在 review 前，不是 export 后补救。

### 2. `short-drama-write` 已有台词相关加载点

`short-drama-write/SKILL.md` 规定：

- `performance-dialogue-brief.md` 用于 `/episode`、`/review`；
- `dialogue-polish-brief.md` 用于 `/dialogue-polish`、`/review`；
- `/episode` 每场戏要执行 6 个问题；
- `/dialogue-polish` 要识别表层话、真实目标、声线差异、解释压缩、反应拍；
- `/review` 有台词维度。

所以“没有任何台词环节”这个判断不成立。

更准确是：有环节，但强制性不够，颗粒度不够，失败不能可靠冒出来。

## 当前样本暴露的问题

### Finding 1：`/dialogue-polish` 可以自我降级，而且不会被拦住

`灰烬新生/dialogue-polish_EP1-10.md` 明确写：

```text
本轮不做“文学化重写”，只做低风险 polish。
```

实际只记录了两项调整：

- EP1 年龄；
- EP1 key tag。

`run_log.md` 也同步写了：

```text
只做低风险 polish；修正 EP1 年龄/钥匙牌画面逻辑
```

这说明 `/dialogue-polish` 在真实运行里没有完成“台词层强度修复”，只是做了结构保护型小修。

问题不是它不能保护结构。保护结构是对的。

问题是：它保护结构之后，没有继续完成自己本该做的事，也没有声明“台词层未完成”。后面的 review 仍然通过。

### Finding 2：review 抓了结构，没有抓住“台词平”

`灰烬新生/review/review_EP1-10.md` 的残余风险主要是：

- EP1 信息偏密；
- EP5 父亲冷话重；
- EP10 接走稳但不够爆。

没有把“人物说话偏客观、偏冷静、缺少脾气和角色压力”列为风险。

这符合我们之前讨论的边界：review 不能当质量发动机。但它至少应该发现 polish 没真正执行，否则流程会误判通过。

### Finding 3：上游有声线，但没有“台词武器表”

`灰烬新生/characters.md` 里已经有声线：

- Evelyn 前期短、低、急着解释但很快停住；
- Celeste 柔、绕、把攻击包成委屈；
- Victor 短、命令式、父权审判；
- Margaret 软、回避、转移责任；
- Cole 短促、火爆。

这些是方向，但不是可直接施工的台词武器。

它还缺：

- 这个角色最常用什么方式伤人；
- 他被戳中羞耻点时怎么说；
- 他如何回避责任；
- 他在公众场合和私下是否变声；
- 哪一句是“只有他会说”的锚点句；
- 哪些说法一出现就 off-character。

结果是 writer 知道“Victor 冷”，但不一定知道 Victor 每场该如何把“冷”变成对 Evelyn 的具体伤害。

### Finding 4：`episode-directory` 只定义了场面任务，没有定义台词任务

`灰烬新生/episode-directory.md` 每集有：

- 可见刺激动作；
- 一眼可懂代价；
- 反派新伤害；
- 结尾按钮；
- 高压可施工检查。

这对剧情和动作很有用。

但它没有每场或每集的“台词冲突任务”，比如：

- 这场是求信失败、装弱拱火、公开站队、父权审判、心死切割，还是反咬；
- 谁必须说短句，谁必须越说越急；
- 谁在打断谁；
- 哪句台词要造成关系位置变化；
- 哪个角色的沉默必须比解释更重。

所以正文容易完成“事件发生了”，但没有稳定完成“话刺到人了”。

## 外部项目审计结论

### `short-drama`

已接入，是当前短剧标准库来源。

它擅长：

- 题材；
- 开篇；
- 爽点；
- 钩子；
- 付费卡点；
- 节奏；
- 反派。

它不是专门的台词强度系统。继续当底盘，不足以单独解决这次问题。

### `oh-story-claudecode`

不能整包接。它大量内容是网文、小说、长篇续写和平台文口径，直接接会污染短剧剧本。

但它里面确实有更硬的台词资产：

- `story-short-write/references/dialogue-mastery.md`
- `story-short-write/references/short-craft.md`
- `story-short-write/references/short-deslop.md`
- `story-short-analyze/references/genre-catalog.md`
- `story-short-analyze/references/genre-core-mechanics.md`
- `story-short-analyze/references/genre-readers.md`
- `story-review/references/dialogue-mastery.md`
- `story-review/references/quality-rubric.md`

其中最该抽的是 `dialogue-mastery.md` 的“决策路由”：

- 压制模式；
- 反转模式；
- 心死模式；
- 情绪推动；
- 信息嵌入；
- 群众/弹幕反应；
- 权力句长：掌控者短，被压者长。

当前 `dialogue-polish-brief.md` 吸收了它的原则，但丢了“模式选择器”。这是现在最明显的损失。

`story-short-analyze` 里还有女频、追妻火葬场、死人文学、家庭婚恋、读者期待的材料。它更适合进入 `/plan` 和 `/outline` 的题材/读者校验，不适合直接给 writer 当台词规则。

### `how-to-make-script`

之前接了 `dialogue-subtext`、`wp-dialogue-polish`、`rb-dialogue`，这是对的，但还漏了一个对当前问题很关键的东西：

- `voice-style-calibration`
- `wp-voice-style-guide`
- `rb-voice-style-guide`
- `ka-character-voice-consistency`
- `ka-verbal-rhythm`
- `ka-embodied-text-pressure`

这些不是短剧爽点方法，但非常适合补“角色说话为什么不像同一个作者”的问题。

它们能提供：

- voice anchors；
- lived pressure；
- register envelope；
- variability budget；
- drift warnings；
- 朗读测试；
- 句长变化、打断、停顿；
- 人物在身体压力、关系风险、时间压力下怎么说话。

这部分当前没有完整进入项目。只靠现在的“句长、攻击方式、闪避方式、沉默方式”，粒度还是粗。

### `shortdrama-pipeline`

它不是写作能力库。

可借鉴的是工程形态：

- job 状态机；
- artifact store；
- approve/reject；
- harness；
- script quality warning；
- latest project assets。

它的 `prompts.py` 要求“中文短剧、节奏快、情绪强”，但太泛，不适合作为我们 writer 的台词方法。

它的 `harness.py` 检查的是镜头时长、镜头承载量、单镜对白密度等，适合未来做交付/分镜 QA，不适合解决“对白没脾气”。

### `dramatron`

主要价值是层级生成思想，不是短剧台词强度。当前问题不建议接。

### `ReelForge-YAML` / `duanju_create_agent`

当前本地没有找到可审计源码。现有项目文档里只有历史提及，不能拿来当已接入或可抽取依据。

## 根因判断

这次问题不是单纯“模型不会写台词”。

真正根因是：

```text
当前链路把台词强度拆成了原则、声线、polish 和 review，
但没有把它变成 writer 写每场戏前必须执行的“台词冲突模式”。
```

于是模型会优先执行更硬的东西：

- 导演节点不能改；
- 女主不能提前反杀；
- 不能破坏结构；
- 禁抄边界不能踩；
- 可见动作要保留。

这些都很硬。

相比之下，“台词要有脾气”只是软要求。模型为了不误伤结构，就会写得稳、客观、少冒险。

这解释了为什么剧情框架正确，但人物说话仍然像在完成事实。

## 建议接法

不要整接外部 skill。

也不建议新增一个常驻 agent。

建议做一次小而硬的链路修补：

### 1. 新增或升级本地 `dialogue-force-brief.md`

它不是替代 `dialogue-polish-brief.md`，而是负责“台词强度生产”。

边界：

- `performance-dialogue-brief.md`：场面、动作、反应链。
- `dialogue-force-brief.md`：台词冲突模式、权力句长、角色武器、打断和沉默。
- `dialogue-polish-brief.md`：成稿后压说明、去同声线、修 AI 味。

### 2. `/characters` 增加“台词武器表”

每个主要角色至少产出：

- 语言目标；
- 常用攻击方式；
- 常用防御/闪避方式；
- 羞耻点被戳中时的语言反应；
- 公共场合 vs 私下的变声；
- 一句“只有他/她会说”的锚点句；
- off-character 红线。

这来自 `voice-style-calibration`，但要压成短剧口径。

### 3. `/outline` 增加“本集台词冲突任务”

每个高压集至少标一个模式：

- 求信失败；
- 装弱拱火；
- 父权审判；
- 公开站队；
- 反咬甩锅；
- 心死切割；
- 新家冷判；
- 群众放大。

并写清：

- 谁短；
- 谁长；
- 谁打断；
- 谁沉默；
- 哪一句话必须造成关系/权力变化。

### 4. `/episode` 写每场前必须选择台词模式

不输出给用户，但正文必须体现。

这一步最关键，因为台词强度不能只靠 polish 事后补。事后能修句子，但很难把整场对话的权力流补出来。

### 5. `/dialogue-polish` 禁止再用“低风险 polish”跳过台词职责

它仍然不能改剧情事实。

但如果原稿台词偏平，它必须做两件事之一：

- 在不改事实的范围内重写台词力度；
- 或明确判定“台词问题来自 episode/outline，当前 polish 无法修”，并回对应层。

不能再出现“只做低风险 polish，然后通过”的情况。

### 6. `/review` 只做兜底，但要抓“polish 未执行”

review 不负责写好台词。

但它应该检查：

- `Dialogue Polish Notes` 是否只是空泛说明；
- 台词是否有真实目标和权力变化证据；
- 主要角色遮名后是否可区分；
- 高压场是否有打断、短句、失语、沉默或句长变化；
- 如果没有，责任归到 `/dialogue-polish` 或 `/episode`。

## 不建议做的事

- 不要把 `oh-story` 整个 `story-short-write` 接进来。
- 不要把 `story-review` 整体接进 clean reviewer。
- 不要把 `how-to-make-script` 的电影/泛剧本方法全接。
- 不要让 writer 全目录扫描外部项目。
- 不要为了“台词强”把 Evelyn 前 10 集写成嘴炮反杀。她可以软、可以忍，但其他人必须更毒、更偏执、更会伤人；她的沉默也要有重量。

## 最小可执行修复

如果只做一轮项目级修补，我建议改这些文件：

1. `shortdrama-remix/skills/short-drama-write/references/dialogue-polish-brief.md`
2. `shortdrama-remix/skills/short-drama-write/references/performance-dialogue-brief.md`
3. `shortdrama-remix/skills/short-drama-write/SKILL.md`

如果愿意更干净一点：

4. 新增 `shortdrama-remix/skills/short-drama-write/references/dialogue-force-brief.md`

我更推荐新增第 4 个文件，因为当前 `dialogue-polish-brief.md` 已经承担“事后精修”，不应该再塞太多“写作前施工”。把生产层和 polish 层分清，执行会更稳。

## 验收方式

不要用全剧重跑先验收。

先做一个小验证：

1. 用 `灰烬新生` EP5 或 EP9 作为局部样本；
2. 只按新规则重跑 `/episode` 或 `/dialogue-polish`；
3. 对比旧版：
   - 角色是否更有脾气；
   - Celeste 是否更会软刀；
   - Victor/Margaret 是否更像自以为合理的伤害者；
   - Evelyn 是否仍然是包子小白花，但沉默更痛；
   - 是否没有改掉导演节点。

小样本过了，再更新主链和跑 1-10。否则直接大改全链，风险还是会回到“规则变多，执行变散”。
