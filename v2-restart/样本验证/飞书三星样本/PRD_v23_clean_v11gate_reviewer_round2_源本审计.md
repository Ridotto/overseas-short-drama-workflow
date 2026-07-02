# PRD_v23_clean_v11gate reviewer round2（源本审计）

## 审阅范围

本轮在 round1 之后读取：

- `[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`
- `PRD_v23_clean_v11gate_Source_Bible.md`
- `PRD_v23_clean_v11gate_Adaptation_Boundary.md`
- `PRD_v23_clean_v11gate_Creative_Development_Pack.md`
- `PRD_v23_clean_v11gate_Stage_Skeleton.md`
- `PRD_v23_clean_v11gate_Episode_Pursuit_Map.md`
- `PRD_v23_clean_v11gate_HighPressure_Scene_Options.md`
- `PRD_v23_clean_v11gate_Playable_Writer_Brief.md`
- `PRD_v23_clean_v11gate_豪门商战版_首批1-10集.md`

未读取 V3 / V5 / V20 / V21 / V22 / V24 旧产物，也未读取作者自检或历史对话。

## verdict

**pass-pending-lock。**

不是 block，也不需要回到 Source Bible 或全链重跑。源本有效性迁移成立，主要外形没有改名复刻，信息边界基本守住。只建议锁两个点后交付：Episode 10 的卡点安全边界 / 文档一致性，Episode 7-8 的金库验证规则锚点。

## 红线判断

- 没洗飞源本有效性：通过。源本 1-10 的核心体验是低位妻子被替换、生死选择失子、五年后高位归来、女配假孕/野种崩塌、男主私人物件火葬场和公开跪求；新本用继承人条款、Level 42 封锁、Blackline 接管、Mother Seat / Vault、Nursery Suite 与胎心吊坠承载了同一追看链。
- 不是改名复刻：通过。源本第 7-8 集高度依赖大屏、亲子鉴定、当场验血；新本改成 Noah 现场失控、金库拒绝、席位灯灭和徽章摘除，外形已明显重建。
- 新本自己能追：通过。Episode 2、4、8、9、10 都有可见高压场和下一集追问。

## fatal blocker

无。

## should-fix risk

### 1. Episode 10 从“枪响空包弹”改成“Level 42 演示舱”后，边界包没有同步，且正文停法有施害者风险

- 回滚层级：`scene_option` / `screenplay`；同步修 `adaptation_boundary` 的本轮拍板项。
- 证据：
  - 源本第 10-11 集是枪口卡点，下一集揭示空包弹，Eve 不真杀 Dante（源本 312-323）。
  - `Adaptation_Boundary` 的本轮拍板项仍写“装着空包弹 / 记忆弹的枪对准自己；枪响黑屏，11 集再揭”（第 58 行）。
  - 后续 `HighPressure_Scene_Options` 已改成 Level 42 演示舱和白色安全气体（第 128-142 行），正文也执行为 Serena 按下红键，气体盖住 Adrian 的脸后黑屏（正文第 1099-1151 行）。
- 问题：改成演示舱本身不算同构，反而比枪更贴新本的“门 / 封锁 / 选择”母题。但当前正文会让 Serena 像是在公开复刻窒息惩罚，风险比源本空包弹更高，也和边界包“Serena 不真杀 Adrian”的锁定不一致。
- 修改建议：保留 Level 42 演示舱这个新壳场面，但把卡点改成“非致命但压迫明确”的选择前一拍，或明确安全演示不会造成真实死亡。可选写法：红键启动倒计时和白雾预充，Adrian 手贴玻璃，Serena 的手停在 `FINAL SEAL / ABORT` 之间切黑；或白气起但同时出现 `OXYGEN SAFE / DEMO MODE`，焦点落在他自愿待在门内承受恐惧和公开羞辱。不要回到源本枪口，除非决定放弃演示舱母题。
- 是否需要重审全稿：不需要。修 Episode 10 结尾并同步边界包 / 场面方案即可，窄验不引入新主线断裂。

### 2. Episode 7-8 的金库验证是合格新载体，但正文缺少一句规则锚点，容易被看成“机器版亲子鉴定”

- 回滚层级：`screenplay`，必要时回 `writer_brief` 补清楚本集可见规则。
- 证据：
  - `HighPressure_Scene_Options` 已承认该候选“功能类似亲子鉴定”，要求不能让金库机器说了算，必须靠 Noah 护子、席位灯灭、徽章被摘撑起现场后果（第 79-82 行、第 158 行）。
  - 正文 Episode 7 只说“Tomorrow morning. The heir vault opens”，Episode 8 只让 Leo 把手放到徽章上后红灯报错（正文第 784-789 行、第 814-829 行）。
  - 源本对应段落是大屏证据、亲子报告、当场验血（源本第 233-264 行），这是本轮明确要避开的高辨识外形。
- 问题：正文已经有 Noah 冲出护子、Chloe 摘徽章、席位灯灭，现场后果是够的；但金库规则太省，观众可能把它理解成换皮亲子鉴定机器。
- 修改建议：加一条极短、可拍的规则锚点，不展开技术解释。例如在 Episode 7 钥匙盒旁加 `HEIR REGISTRY / LIVE GUARDIAN MATCH REQUIRED`，或让管家说一句 “The vault reads the heir registry and the guardian trust.” 然后马上进入 Leo 按手、红灯、Noah 破防。核心是让机器只是触发器，高潮仍落在 Noah 护子和 Chloe 被摘席。
- 是否需要重审全稿：不需要。窄验 Episode 7-8 规则补丁即可。

### 3. Episode 8 的反咬功能成立，但台词可以更明确“操控选择”，避免重复消费 Episode 6 的怀孕揭示

- 回滚层级：`screenplay` / `dialogue`。
- 证据：
  - `Source_Bible` 要求 Ep6 只让 Adrian 知道怀孕和伤疤，Ep9 才释放双胎与私人物件（第 139-141 行）。
  - 正文 Ep6 只给 `PREGNANT. EMERGENCY TRANSFER. FETAL DISTRESS.`，没有双胎和物件（正文第 669-671 行）。
  - 正文 Ep8 Chloe 说 “You left your real baby behind that glass. You gave the order. I only showed you which door to open.”（正文第 897 行）。
- 问题：信息边界没有破，双胎和物件仍留到 Ep9（正文第 930-964 行）。但 Ep8 的台词前半“real baby”略像重复 Ep6 怀孕揭示；真正新信息应该是 Chloe 承认她诱导 Adrian 看见哪扇门、做出哪次选择。
- 修改建议：把 Ep8 台词压到操控选择上，例如 “I did not lock her in. I made you look at my door first. You chose the rest.” 这样既不提前说双胎，也更精准打到男主罪责。
- 是否需要重审全稿：不需要。窄修 Episode 8 一句台词。

## optional optimization

### 1. Episode 1 的医学信封物件建议换名，避免“碎纸柜”误读

- 回滚层级：`screenplay`。
- 证据：正文 Episode 1 写 Serena 把 `PRIVATE MEDICAL` 信封塞进金属碎纸柜保密投递口，但又说明没有启动粉碎。
- 修改建议：如果它是后续可追溯物件，改成 `secure evidence slot / compliance lockbox` 更清楚。
- 是否需要重审全稿：不需要。

### 2. `Playable_Writer_Brief` 可保持，不需要加厚

- 回滚层级：无。
- 证据：brief 已按集给 Current Story State、Episode Pursuit、Selected Scene Carrier、Information Boundary、Last Frame 和四个存活问题，且没有塞完整 Source Bible。
- 修改建议：不要因为 reviewer 风险再往 brief 里加大表。只把两个锁点的短规则补进去即可。
- 是否需要重审全稿：不需要。

## 不该修改项

- 不要回到源本第 7-8 集的大屏、报告、床照、验血链。新本的 Noah 护子 + 金库拒绝 + 席位摘除方向是对的。
- 不要把 Ep9 双胎和胎心吊坠提前。当前 Ep9 的两张婴儿床、双份信托、两段胎心是本批火葬场最有效的私人物件。
- 不要削弱 Ep2 的 Level 42 二选一。它是源本生死选择在新壳里最强的承载点。
- 不要让 Marcus 抢 Serena 的复仇动作。当前正文基本守住了“Marcus 提供背书，Serena 自己落子”。

