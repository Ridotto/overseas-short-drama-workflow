# PRD v10 豪门商战版作者 quality gate

对应正文：`PRD_v10_豪门商战版_首批1-10集.md`  
对应写作前工作稿：`PRD_v10_豪门商战版_写作前工作稿.md`  
对应 rewrite / dialogue polish：`PRD_v10_豪门商战版_rewrite_report_dialogue_polish.md`  
结论：作者侧 `pass for independent reviewer/challenge`。不等于独立 reviewer 通过。

## 1. Target Contract & Scope

本次检查范围：V10 首批 1-10 集，重点复查 V9 challenge 指出的第 7-10 集。

目标产物合同：

1. `scene_draft / screenplay_draft`：正文必须是可读可拍剧本，不泄露内部字段。
2. `dialogue_polish`：关键台词有表面意思、潜台词、角色声音和节奏，不只是改短句。
3. 洗稿适配：源本有效功能迁移，但关键事件载体重建，不能只是改名。
4. `carry_through_integrity`：源本强度必须进入 episode map、scene packet 和 screenplay。
5. V10 局部目标：Step 8 E7-E10 高压 scene packet 真正可验收；Chloe 有有效反扑；第 10 集留下第 11 集追问。

## 2. Selected Lenses & Rationale

| Lens | 选择原因 |
|---|---|
| contract_fit | 先查正文是不是剧本，不是说明书或 scene packet。 |
| mechanics_pressure | V10 的核心是第 7-10 集是否从机制揭示变成人物行动和空间后果。 |
| continuity_invariants | 新增 `emergency trust access` 必须从第 7 集接到第 10 集，不得漂移。 |
| expression_integrity | 防止 grants / trust access / referral 术语变解释腔。 |
| adaptation_fit | 检查是否洗飞、改名复刻、短剧降级。 |
| carry_through_integrity | 检查源本节点 -> episode map -> scene packet -> 正文是否有锚点。 |

## 3. Hard Fails

| 硬失败项 | 判断 | 证据 |
|---|---|---|
| 正文不是剧本 / 内部字段泄漏 | pass | 正文采用 Episode + INT. 场景格式；未发现 `Scene Objective / Source Function Ref / End Button / Do Not Consume / Script Blocks` 等内部字段进入正文。 |
| Step 8 Scene packet 仍过薄 | pass | `写作前工作稿` Step 8 对 E7-E10 均补了 Character Pressure State、Short-drama Beat Chain、Script Blocks 和 Do Not Consume。 |
| 第 7-8 集仍只靠系统/权限自动揭示 | pass | 第 7 集加入 Chloe 冻结医疗 grants、Serena 血指印救场、Adrian 担保；第 8 集加入安保抓腕、Adrian 亲手拦 Chloe、Chloe 联邦投诉。 |
| Chloe 后半段无有效反扑 | pass | Chloe 第 7 集设公益付款陷阱，第 8 集发送联邦投诉，第 10 集拿血指印回执反咬 Serena。 |
| 第 10 集收得太满 | pass | Adrian 认罪并被捕，但调查员转向 Serena，留下“第二份 referral / trust breach”追问。 |
| 源本有效性没迁移 | pass | 保留被替代、致命误判、失子、回归夺权、拆女配、男主同罪、旧物火葬场、跪求不原谅。 |
| 改名复刻 | pass | 仍扣除车祸、火海、黑帮、假孕、亲子鉴定、保险箱、小毛衣、雨夜下跪、枪口测试。 |
| 短剧降级为文件/会议/冷对白 | pass with risk | 文件/屏幕均触发动作或后果：医疗款冻结、血指印、安保抓腕、CEO key、旧语音、手铐、证物袋。风险是术语仍需 reviewer 判断可读性。 |

## 4. Carry-through Evidence

| 源本节点 | 源本强度 | Episode map 锚点 | Scene packet 锚点 | Screenplay 正文锚点 | 判断 |
|---|---|---|---|---|---|
| S1-E2 | 女主求救，男主拒救，造成不可逆失子 | Step 7 Episode 2 | Step 8 E1-6 继承锚点 | Episode 2：`MEDICAL EXCEPTION DENIED`、拘押车流血、急救室长音 | pass |
| S1-E7 | 当众拆女配，男主仍护错 | Step 7 Episode 7 `她拿人做盾` | Step 8 Episode 7 Scene Packet | Episode 7：grants 冻结、Serena 血指印 emergency payout、Chloe 胸针回收、Adrian 红键担保 | pass |
| S1-E8 | 女配崩盘但男主同罪被钉住 | Step 7 Episode 8 `她反咬了一口` | Step 8 Episode 8 Scene Packet | Episode 8：安保抓 Serena、Adrian 扣住 Chloe 手腕、CEO key、旧拒医语音、Chloe 联邦投诉 | pass |
| S1-E9 | 旧物火葬场，从知道到崩溃 | Step 7 Episode 9 | Step 8 Episode 9 Scene Packet | Episode 9：托管箱、胎心音、监护仪长音、手被箱口划破、二次背罪新闻 | pass |
| S1-E10 | 当众跪求但不原谅 | Step 7 Episode 10 `第二份 referral` | Step 8 Episode 10 Scene Packet | Episode 10：直播认罪、手铐、不原谅、调查员转向 Serena、Chloe “欢迎回来” | pass |

## 5. Weighted Weaknesses

### W1. 商战/法律机制仍有理解成本

表现：第 7-10 集引入 `medical grants / emergency signature / trust access / federal review`。  
当前缓解：每个机制都绑定可见动作：付款失败、血指印、安保抓腕、证物袋、调查员转向 Serena。  
是否阻断：不阻断作者侧；必须给 reviewer 重点看。

### W2. 第 10 集满足感比 V9 少

表现：V9 的认罪闭环更完整；V10 为了留下第 11 集追问，故意让 Serena 也被调查员点名。  
判断：这是 goal 指定修法，不是失误。风险是 reviewer 可能觉得首批爽点被新危机冲淡。

### W3. Chloe 反扑更强，但可能提升她的“开挂感”

表现：她提前布置公益付款陷阱、新闻稿和联邦投诉。  
当前缓解：这些都来自她仍掌握 Foundation 和媒体叙事，不是凭空黑客能力；她场内仍失权。  
是否阻断：不阻断，但需 reviewer 判断可信度。

### W4. Marcus 仍偏风险提醒者

表现：第 7 和第 10 集 Marcus 提醒 Serena，不深入自己的利益动机。  
判断：首批可接受；后续 11-37 集必须发展他与 Serena 的控制/保护冲突。

## 6. Correction Ladder

如 reviewer / challenge 指出问题，按以下顺序回修：

1. 若说“第 7-8 集仍机制密”：压缩术语，只保留可见后果，不删除 Chloe 反扑。
2. 若说“Chloe 反扑开挂”：补她借 Foundation 权限和媒体预案的前置动作，或削弱投诉即时性。
3. 若说“第 10 集爽点被冲淡”：增强 Adrian 认罪的公开代价，同时保留 Serena 被调查的尾钩。
4. 若说“Serena 像审计者”：强化她亲自救人、切断麦克风、拿走徽章、拒绝原谅的动作。
5. 若说“第 11 集追问不够尖”：把结尾从配合调查升级为临时限制令 / root-key 被扣押，但需避免过度堆钩子。

## 7. Recheck Plan

已做：

- 检索正文内部字段：未发现内部 scene packet 字段进入正文。
- 对照 V9 challenge 汇总：Step 8、7-10 机制感、Chloe 反扑、第 10 集追问均已处理。
- 检查第 8/9 集托管箱边界：第 8 只给编号，第 9 才开箱。
- 检查 Chloe 反扑链：第 7 设局，第 8 投诉，第 10 反咬。
- 检查第 10 集不和解：Serena 只说“听见了。但我没说原谅。”

待独立 reviewer / challenge：

- 第 7-8 集是否仍显得像包装过的机制戏。
- Chloe 反扑是否有效但不过度。
- 第 10 集新危机是否比 V9 更适合第 11 集追看。
- V10 是否相对 V9 实质进步，而不是增加复杂度。

## 8. 作者结论

作者侧结论：`pass for independent reviewer/challenge`。

理由：

- Step 8 E7-E10 已补齐高压 scene packet；
- 正文承接了人物被迫行动链；
- Chloe 有有效反扑；
- 第 10 集没有收满；
- 源本有效性未洗飞，高辨识外形未复用。

限制：

- 本文件不能替代独立 reviewer；
- full workflow 仍需 Step 14 / 6-agent challenge 后才能判断是否 complete。
