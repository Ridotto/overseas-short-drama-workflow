# PRD v4 workflow 环节来源审计

日期：2026-06-30

审计对象：

- `PRD_v4.md`
- `workflow_spec_v1.md`
- `参考资产/`
- `外部短剧工作台与写作流程研究_2026-06-30.md`
- `全局诊断_外部workflow对照_2026-06-30.md`
- 第 7-8 集稳定症状测试结果

本文不是新 PRD，也不是新规则表。

本文只回答一个问题：

**当前 workflow 的每一环，到底有没有成熟项目或现成资产支撑；没有支撑的，不能继续假装已经可靠。**

---

## 1. 总判断

现在不能再说“直接拿成熟项目的中间产物格式”。

更准确的判断是：

**当前每一环都要重新审计来源。能用现成项目接管的，就用现成项目接管；只能适配的，写清楚适配边界；完全是我们自己造的，先标成高风险。**

第 7-8 集稳定症状测试已经说明：

当前 `workflow_spec_v1.md` 不是完全无效，但它会稳定把正文导向一种坏形态：

```text
证据链完整
剧情点都覆盖
人物站着等屏幕/证人/反派自白推进
女主像审计者
高压场面像听证会
卡点边界容易提前兑现
```

这说明问题不只是某个 writer 没写好，也不是只缺“视听语言”四个字。

根本问题是：

**我们自建的中间产物，把源本有效性转成了“信息 / 证据 / 功能清单”，而不是成熟项目里更常见的“节拍 / 场景目的 / 动作链 / 表演承载 / 质量门”。**

---

## 2. 来源可信分层

### A 级：本地参考资产里已读到、可以直接作为来源

| 来源 | 能支撑什么 |
|---|---|
| `1-short-drama_短剧标准库/SKILL.md` | `/start -> /plan -> /characters -> /outline -> /episode -> /review` 的短剧创作阶段；分集目录；角色体系；单集格式；review 维度 |
| `1-short-drama_短剧标准库/references/hook-design.md` | 钩子类型、卡点机制：悬念、反转、情绪、信息、危机 |
| `1-short-drama_短剧标准库/references/rhythm-curve.md` | 单集微结构：开头钩子、中段冲突升级、结尾爽点/钩子 |
| `1-short-drama_短剧标准库/references/satisfaction-matrix.md` | 爽点类型、压抑 -> 释放、打脸/身份/逆袭/情感爆发/揭秘 |
| `2-oh-story_追踪与去AI味/README.md` | 扫榜、拆文、写作、追踪、去 AI 味的文件驱动闭环 |
| `2-oh-story_追踪与去AI味/demo_拆文样本/情节节点.md` | 情节节点拆解：节点编号、类型、情绪强度、涉及人物、手法、原文锚点 |
| `3-how-to-make-script_方法论/references/output-format-contracts.md` | `beat_sheet`、`outline`、`scene_draft`、`screenplay_draft`、`dialogue_polish`、`rewrite_report`、`quality_gate_report` 等产物契约 |
| `3-how-to-make-script_方法论/references/routing-policy.md` | 不同阶段使用不同产物，不把对白、场景、质量审查混成一锅 |
| `3-how-to-make-script_方法论/docs/adaptive-quality-checking-zh.md` | 质量审查必须先锁产物契约，再选 lens，再分硬失败/软弱项 |
| `3-how-to-make-script_方法论/references/expression-lens-triggers.md` | 台词、表达、情绪标签句、解释腔、完整句病等表达层 hard fail |
| `4-dramatron_分层生成/README.md` | 分层生成顺序：logline -> characters -> plot points/scenes -> locations -> dialogue；也提醒不能全自动盲用 |
| `5-shortdrama-pipeline_质检/models.py` | `Episode` 有 `summary/hook/shots`；`Shot` 有 location、characters、visual_description、dialogue、camera、emotion |
| `5-shortdrama-pipeline_质检/prompts.py` | 每个 shot 只表达一个核心动作或情绪推进；最多一条关键对白；可用动作/表情推进 |
| `5-shortdrama-pipeline_质检/docs/ARCHITECTURE.md` | 状态机 + 人工审核门；剧本批准前不进人物/视频阶段 |

### B 级：外部研究文档里记录过，但这次未重新打开原 repo 的来源

这些可以作为候选来源，但下一次正式改 workflow 前，最好回原项目再复核一次。

| 来源 | 研究文档记录的可借点 | 当前处理 |
|---|---|---|
| Toonflow-app | 源材料导入、事件提取、故事骨架、改编策略、监督审核、逐集剧本 | 可借流程边界，但不能直接声称已完全接管 |
| ReelForge-YAML | `opening_hook`、`cliffhanger`、`power_shift`、`visual_executability`、`source_ref` | 可借检查维度，但不能把 shot/YAML 硬塞成剧本格式 |
| Jellyfish | 剧本到分镜、元素抽取、资产一致性、可生产性 | 只适合作为可生产性参照，不是剧情好看标准 |
| huobao-drama | script_rewriter / storyboard_breaker 边界 | 可借“剧本阶段和分镜阶段分开”的原则 |
| AgentCine / story-shot-agent | 表演指导、source_text、动作/画面/音频拆分 | 可借到视频前的场面可执行性 |

### C 级：我们项目必须自有，但只能做最薄适配层

成熟项目里没有直接等价的“海外短剧洗稿器”。

所以以下能力必须项目自有，但不能继续膨胀：

| 项目自有能力 | 为什么外部没有直接成品 | 处理原则 |
|---|---|---|
| 源本有效性迁移 | 外部多是从零创作或小说改编，不是“爆款源本洗新壳” | 只做源本功能到新本承载的映射，不发明审美大全 |
| 同构扣除 | 洗稿才需要判断“哪些源本外形不能复用” | 做薄，不要把所有变量都锁死 |
| 新壳等效承载 | 新事件必须承载源本体验，但不能复制源本桥段 | 用成熟项目的 scene/beat/action 工具承载，不自造大表 |
| 源本回指 | 新本不能抄源本，但每个强节点要能回到源本有效功能 | 内部可回指，正文输出不暴露源本外形 |

---

## 3. 每一环来源审计

### 1. 需求确认摘要

当前状态：基本合理，但表述是我们自建。

成熟来源：

- `1-short-drama` 的 `/start`：题材、受众、基调、集数、语言/出海模式。
- `how-to-make-script` 的 routing：先确认 intent / medium / stage / output / constraints。

判断：

**可保留，但应改成成熟来源的 intake 逻辑，不要自造一套问题清单。**

应接管的要点：

- 先确认“这是洗稿 / 改编 / 重写 / 审稿”哪一种任务。
- 先确认新壳、集数、市场、语言、输出范围。
- 如果用户只说“豪门商战”，还不够；必须二次确认改写边界。

---

### 2. 源本有效性摘要

当前状态：方向对，但“五层分析”是我们融合出来的。

成熟来源：

- `oh-story` 的 `拆文报告 / 情节节点 / 写作手法`。
- `short-drama` 的 hook / rhythm / satisfaction / villain / opening。

判断：

**不能继续只用我们自己的五层表。应改成“源本拆文包”。**

更可靠的来源形态：

```text
源本拆文包
1. 一句话故事核
2. 分集/节点功能
3. 情节节点表：节点、类型、情绪强度、涉及人物、手法、原文锚点
4. 钩子与卡点
5. 爽点与压抑-释放
6. 关系/权力变化
7. 信息差和真相揭露路径
8. 写作手法/表达手法
```

当前五层表可以降级成阅读顺序，不再当主产物。

---

### 3. 源本事件载体拆解

当前状态：比较接近成熟来源，但字段仍是我们自建。

成熟来源：

- `oh-story/demo_拆文样本/情节节点.md`：节点编号、类型、情绪强度、涉及人物、手法、原文引用。
- ReelForge 研究记录里的 `source_ref / provenance`。

判断：

**可保留，但应改成 oh-story 情节节点的结构，再叠加洗稿特有字段。**

成熟项目直接给我们的部分：

- 节点编号；
- 客观事件；
- 情绪类型和强度；
- 涉及人物；
- 写作手法；
- 原文锚点。

洗稿项目只额外加三列：

- 观众体验功能；
- 高辨识外形；
- 是否禁止复用。

不要继续扩成大表。

---

### 4. 变量迁移策略

当前状态：项目自建，无成熟项目直接等价。

成熟来源：

- how-to-make-script 的 `boundary_map / scope_correction` 能提供“边界管理”思路。
- 但没有一个成熟项目直接提供“洗稿变量强继承/等效迁移/自由改写/必须删除”。

判断：

**这是项目特有适配层，必须保留，但要压到最薄。**

当前风险：

变量表太容易变成“锁死规则”或“默认深度化”。

建议：

只保留四个结果：

```text
必须保留的体验功能
必须换掉的源本外形
可以自由换的外壳变量
必须删除/修复的烂点
```

不要把它做成全剧万能变量矩阵。

---

### 5. 新事件载体迁移

当前状态：最高风险之一。这个环节是我们自建的，而且稳定症状测试证明它会滑成“证据揭露链”。

成熟来源：

- how-to-make-script 的 `scene_card`：单场景目的、冲突、情感出口。
- how-to-make-script 的 `scene_draft`：必须有 `Scene / Purpose / Action`，对白不能裸奔。
- shortdrama-pipeline 的 `Shot`：每个 shot 只表达一个核心动作或情绪推进。
- ReelForge 研究记录里的 `power_shift / visual_executability`。
- Toonflow 研究记录里的 adaptation strategy，但需回原项目复核。

判断：

**不能继续使用当前“新事件载体迁移表”作为主中间产物。**

它应该被替换为：

```text
新壳场面迁移卡
1. 源本体验功能
2. 源本禁止外形
3. 新场景目的
4. 新冲突动作链
5. 第一轮压迫
6. 第一次反击/反转
7. 权力变化
8. 关系变化
9. 可见后果
10. 卡点停在什么动作前
```

重点不是“新证据是什么”，而是：

**证据出现之后，谁被迫做什么。**

---

### 6. 正文前策略审核

当前状态：我们自建的审核表。

成熟来源：

- how-to-make-script 的 `quality_gate_report`。
- adaptive quality checking：先锁产物契约，再选 lens，再区分 hard fail / weighted weakness。

判断：

**应直接改为 quality gate，不要自建审核问卷。**

审核对象不应是“这几个字段填没填”，而是：

- 当前产物契约是什么；
- 硬失败是什么；
- 哪些弱点会影响下一阶段；
- 修正阶梯是什么；
- 修完后重查什么。

---

### 7. 洗稿方案

当前状态：用户可见层，基本必要。

成熟来源：

- how-to-make-script 的 `path_options / boundary_map / development_brief`。
- shortdrama-pipeline 的人工审核门。

判断：

**可保留，但它不是创作产物，是人工拍板门。**

应该用户可见的是：

- 这版怎么避免改名复刻；
- 这版怎么避免洗飞；
- 哪些强节点会换成什么新场面；
- 首批覆盖哪个留存闭环；
- 哪些问题需要用户拍板。

不要把内部大表给用户。

---

### 8. 新本阶段骨架

当前状态：可保留，但来源混杂。

成熟来源：

- `short-drama` 的 `/plan`：故事骨架、三幕/阶段、节奏波形、爽点分布、付费卡点。
- how-to-make-script 的 `beat_sheet / outline`。
- Dramatron 的分层顺序：logline -> characters -> plot/scenes -> dialogue。

判断：

**应改名为“新本 beat sheet / outline”，用成熟产物接管。**

不要再让阶段骨架只写“前段/中段/后段大概发生什么”。

必须回答：

- 故事引擎；
- 阶段节拍；
- 每次局势怎么变；
- 情绪弧怎么走；
- 哪些源本节点在相似阶段等效迁移。

---

### 9. 分集功能表

当前状态：方向对，成熟来源强。

成熟来源：

- `short-drama` 的 `episode-directory.md`。
- `shortdrama-pipeline` 的 `Episode`: title / summary / hook / shots。
- `hook-design` 与 `rhythm-curve` 的单集微结构。

判断：

**可保留，但要用成熟来源重写字段。**

推荐字段：

```text
Episode
1. 集数/标题
2. 本集 summary
3. 本集开头钩
4. 本集核心摩擦
5. 最大刺激点
6. 本集变化：关系/局势/信息/情绪
7. 结尾 hook/button
8. 禁止提前消费的下一集内容
```

尤其要补最后一项。

第 8 集提前吃掉第 9 集，就是因为这个边界没锁住。

---

### 10. 关键场面草案

当前状态：方向对，但仍然是我们自建字段，且执行容易变成“补动作装饰”。

成熟来源：

- how-to-make-script 的 `scene_card`。
- how-to-make-script 的 `scene_draft` 契约：`Scene / Purpose / Action`，对白必须绑定动作或表演。
- shortdrama-pipeline 的 shot 原则：每个 shot 一个核心动作或情绪推进。

判断：

**应替换为“scene card -> scene draft”的成熟链路。**

不是问：

```text
有没有身体反应？
有没有空间压力？
有没有道具？
```

而是问：

```text
这场戏的 Purpose 是什么？
第一个 Action 让谁占上风？
第二个 Action 如何升级？
第三个 Action 让谁失去什么？
Dialogue 是否绑定 Performance 或 Action？
这场结束后权力/关系/信息状态是否改变？
```

这比我们自己列“动作、身体、空间、道具”更可靠。

---

### 11. 状态追踪

当前状态：成熟来源强。

成熟来源：

- `oh-story` 的追踪文件：伏笔、时间线、角色状态、上下文。
- how-to-make-script 的 `story_memory_checkpoint`。

判断：

**这一环可以直接用成熟项目的思路。**

建议不要自建四张新表，而是直接采用：

```text
关系状态
信息差状态
伏笔/证据
角色状态
下一安全入口
```

每次写完一批，只做 delta 更新，不全文重写。

---

### 12. 单集写作包

当前状态：最高风险之一。稳定症状测试证明当前写作包会把 writer 带成 checklist 写法。

成熟来源：

- how-to-make-script 的 `scene packet / scene_card / scene_draft`。
- `short-drama` 的 `/episode` 单集格式。
- `shortdrama-pipeline` 的 Episode + Shot 结构。

判断：

**当前单集写作包不能继续信。**

它应该被替换为：

```text
单集 scene packet
1. 上一集卡点
2. 本集 opening hook
3. 本集 scene sequence
4. 每场 Purpose
5. 每场 Action chain
6. 每场 power shift / relationship shift
7. 可见证据如何触发人物动作
8. Dialogue 上限和功能
9. 本集 button/cliffhanger
10. 禁止提前消费
```

重点变化：

不要再给 writer 一串“必须揭露的信息点”。

必须给 writer 一串“场面动作如何升级”。

---

### 13. 首批正文初稿

当前状态：当前 PRD 只说“写出可读剧本文字”，太泛。

成熟来源：

- how-to-make-script 的 `screenplay_draft`。
- how-to-make-script 的 `scene_draft`。
- short-drama 的 episode format。
- shortdrama-pipeline 的 shot/action 约束。

判断：

**正文初稿应按 screenplay/scene draft 写，不应让模型自由散文式写。**

成熟来源里最关键的硬点：

- 每个场景必须有 Purpose；
- 每个场景必须有 Action；
- 对白不能裸奔；
- 对白需要 Performance 或 Action 承载；
- 可选 SFX/BGM/镜头提示，但不能堆术语。

这会直接处理“全是台词、站桩聊天”的稳定风险。

---

### 14. 正文后短剧化返修

当前状态：方向对，但我们自建了返修条目。

成熟来源：

- how-to-make-script 的 `rewrite_report`。
- how-to-make-script 的 `dialogue_polish`。
- expression lens：解释腔、情绪标签句、完整句病、角色同声。

判断：

**应拆成两个成熟产物，而不是一个“短剧化返修”。**

推荐：

```text
先 rewrite_report：
失败发生在概念 / 结构 / 场景 / 对白哪层？

再 dialogue_polish：
只处理台词，不假装能修结构问题。
```

如果 scene 本身没冲突，不能只润色对白。

---

### 15. 作者自检

当前状态：必要，但当前自检表是我们自建。

成熟来源：

- `quality_gate_report`。
- adaptive quality checking。

判断：

**作者自检应变成作者版 quality gate，而不是自由反省。**

必须有：

- Target Contract & Scope；
- Hard Fails；
- Weighted Weaknesses；
- Correction Ladder；
- Recheck Plan。

作者不能只说“我担心视听语言”。

---

### 16. 独立 reviewer 分层审稿

当前状态：方向对，成熟来源强。

成熟来源：

- how-to-make-script 的 `quality_gate_report`。
- how-to-make-script 的 `rewrite_report`。
- oh-story 的多 agent review 思路。

判断：

**可保留，但 reviewer 应直接用成熟报告结构。**

Reviewer 不应该只按我们自建失败层打勾。

更好的做法：

```text
先 quality gate 判断能不能交付
再 rewrite report 判断若失败，失败在哪层
最后给 correction ladder
```

---

### 17. 主控汇总交付

当前状态：必要，但产品原创成分高。

成熟来源：

- how-to-make-script 的 Room Captain / handoff packet 思路。
- shortdrama-pipeline 的 artifact/status/review gate。

判断：

**可保留，不是质量核心。**

主控只负责合并：

- 作者 quality gate；
- reviewer quality gate；
- rewrite report；
- 用户/导演反馈。

不要让主控再发明新标准。

---

### 18. 用户 / 导演反馈回流

当前状态：方向对，但分类是我们自建。

成熟来源：

- how-to-make-script 的 `rewrite_report`：Failure Layer / Root Symptoms / Prioritized Actions / Classification。
- adaptive quality checking 的 recheck。

判断：

**应改为“反馈 -> failure layer -> correction ladder -> recheck”，不要继续自建反馈字典。**

导演反馈不能直接变规则。

它应该先被归到：

```text
源本分析失败
改编/迁移失败
结构/节拍失败
场景失败
对白失败
表达失败
连续性失败
卡点失败
```

然后再决定回哪一环。

---

## 4. 哪些环节现在最不可信

按风险排序：

### 第一高危：单集写作包

原因：

- 稳定症状测试已经证明，它会把 writer 带成“信息点覆盖模式”。
- 它没有采用成熟项目的 scene packet / scene_draft 契约。
- 它给了“要揭露什么”，但没有给“谁被迫做什么动作”。

处理：

**替换，不是修补。**

---

### 第二高危：新事件载体迁移

原因：

- 这是洗稿项目自有环节，但当前表格太像“新证据设计表”。
- 它没稳定转成场面动作链。

处理：

**保留这个环节的产品必要性，但换成熟项目的 scene_card / action chain 承载。**

---

### 第三高危：关键场面草案

原因：

- 它知道要动作、身体、空间、道具。
- 但这些字段容易变成装饰，不能保证 scene purpose 和 action progression。

处理：

**替换为 scene_card -> scene_draft。**

---

### 第四高危：正文后短剧化返修

原因：

- 现在它混了场景重写、对白压缩、卡点修正。
- 成熟项目明确区分 rewrite_report 和 dialogue_polish。

处理：

**拆开，先诊断层级，再改对应层。**

---

### 第五高危：源本有效性摘要

原因：

- “五层分析”是我们自己抽象的。
- 不是不能用，但不应该压过 oh-story 的节点化拆文和 short-drama 的短剧机制。

处理：

**降级为阅读提示，主产物改成源本拆文包。**

---

## 5. 哪些环节可以直接保留

### 状态追踪

成熟来源强：oh-story + story_memory_checkpoint。

保留，但按成熟项目文件驱动方式改。

### 分集功能表

成熟来源强：short-drama episode-directory + Episode hook。

保留，但补 opening hook / 最大刺激点 / button / 禁止提前消费。

### Reviewer

成熟来源强：quality_gate_report + rewrite_report。

保留，但换成熟报告结构。

### 人工确认门

成熟来源强：shortdrama-pipeline 的 review gates。

保留，但只作为拍板门，不当创作表。

---

## 6. 下一版 workflow 应该怎么改

不是加更多规则，而是把自建中间产物换成成熟项目已有产物。

建议下一版 workflow 改成：

```text
0. 最小需求确认
   来源：short-drama /start + how-to-make-script routing

1. 源本拆文包
   来源：oh-story 拆文报告 / 情节节点 / 写作手法
   叠加：short-drama hook / rhythm / satisfaction

2. 洗稿边界包
   来源：项目特有薄适配层
   内容：必须保留体验、禁止复用外形、可自由改变量、必须修复烂点

3. 新本 beat sheet / outline
   来源：how-to-make-script beat_sheet / outline + short-drama plan

4. 新壳场面迁移卡
   来源：scene_card + ReelForge power_shift/visual_executability 思路
   目标：把源本功能转成新场面动作链

5. Episode function map
   来源：short-drama episode-directory + shortdrama-pipeline Episode
   必须有：summary / opening hook / max spike / end hook / 禁止提前消费

6. Scene packet
   来源：how-to-make-script scene_card / scene_draft
   必须有：Purpose / Action chain / Performance / Dialogue limit

7. Screenplay draft
   来源：screenplay_draft / scene_draft
   要求：对白不能裸奔，必须绑定动作或表演

8. Rewrite report
   来源：how-to-make-script rewrite_report
   先判断坏在哪层

9. Dialogue polish
   来源：dialogue_polish + expression lens
   只处理台词和表达，不拿它修结构

10. Quality gate
    来源：quality_gate_report
    作者自检和 reviewer 都用它

11. Story memory checkpoint
    来源：oh-story 追踪 + story_memory_checkpoint
    每批写完更新
```

这样改后，PRD 仍然可以保持不厚。

真正要改的是 `workflow_spec_v1.md`，把我们自建的几个中间表替换成成熟产物链。

---

## 7. 当前不该做什么

1. 不该继续补“视听语言、落差、拉扯感”的孤立规则。
2. 不该继续让“新事件载体迁移表”长成更复杂的证据表。
3. 不该继续把导演反馈逐条写进 PRD。
4. 不该只靠免责声明说“这些表不要机械执行”。
5. 不该把视频分镜工具的 shot 格式硬塞进剧本文档。

---

## 8. 当前最小结论

PRD v4 的产品方向仍然成立：

**这是基于源本的海外短剧洗稿器，不是从零原创，也不是评分器，也不是视频生产工具。**

但 `workflow_spec_v1.md` 的若干中间产物不应继续盲信。

当前最该改的不是产品定义，而是执行工序：

**把自建的“信息/证据/功能清单式中间产物”，替换为成熟项目已有的“拆文节点、beat sheet、scene card、scene draft、rewrite report、quality gate、story memory checkpoint”。**

唯一必须自有的部分，是洗稿适配层：

```text
源本有效功能
禁止复用外形
新壳等效场面
内部源本回指
```

这层必须薄，不能再变成新规则系统。
