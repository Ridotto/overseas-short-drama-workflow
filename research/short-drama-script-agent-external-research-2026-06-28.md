# 短剧剧本分析/评价 Agent 外部平台与开源项目拆解

日期：2026-06-28  
项目基线：`Short-Drama Script Pattern Agent` 最初 office-hours finding  
目的：补强外部参照，不替代本项目的强弱样本校准

> 重启提示：这份文件是早期外部调研笔记，不是当前产品定义。它可以帮助 Claude 了解市面工具和开源项目，但不能直接当评分体系、产品架构或实现路线使用。

更新说明：

- 这份文档是第一轮“分析/评价平台”研究，不是最终全景。
- 已补充更完整的生产链、开源项目、市场趋势、钩子标准和落地方案，见：
  `/Users/jiakun/Codex/自动化编剧/research/short-drama-agent-landscape-2026-06-28.md`

## 0. 结论先行

这轮研究没有发现一个可以直接替代本项目的成熟产品。

成熟海外平台强在影视剧本 coverage、受众/市场预测、项目融资和制片决策；国内短剧平台强在剧本生成、小说改编、分镜和 AI 视频生产；GitHub 开源项目强在格式解析、结构化 schema、分镜流水线和局部规则评测。但它们大多不解决这个项目最关键的问题：

> 如何从中文短剧强样本和弱对照样本中，抽取有证据、有时效判断、可复用、能服务 AI 视频生产的强剧本 pattern。

因此，本项目不应该照搬任何外部平台的评分体系。正确用法是：

1. 用海外平台学习“剧本如何结构化分析、如何给行业用户解释判断”。
2. 用行业评审平台学习“评分、推荐等级、多读者校准、证据引用”。
3. 用中文短剧平台学习“真实短剧生产链路、剧本到分镜到视频的交付要求”。
4. 用 GitHub 项目学习“格式吸收、schema、source map、linter、AI 视频适配”。
5. 用 2024-2026 行业变化修正时效判断，避免把早期小程序付费短剧逻辑当成唯一标准。

最值得深看和借鉴的对象：

| 类别 | 对象 | 借鉴点 | 不能照搬 |
|---|---|---|---|
| 海外剧本智能分析 | StoryFit | 情绪曲线、角色关系、受众标签、强弱对照案例 | 受众预测和成功预测黑盒 |
| 海外内容/融资决策 | Largo.ai、Cinelytic、ScriptBook | 内容 DNA、版本对比、go-to-market 元数据 | 电影/长剧财务预测 |
| 行业评审 | Slated、The Black List | 多读者、评分尺度、推荐等级、证据支撑 | Hollywood 稀缺推荐逻辑 |
| AI coverage | Prescene、OnDesk、Callaia、ScriptReader.ai | 场景引用、coverage 结构、差稿诊断、Hook Out | 通用电影剧本维度 |
| 中文短剧评价 | 剧拆拆、创一AI/咔咔猩 | 剧本诊断、结构拆解、节奏/钩子/合规/市场潜力 | 未公开 rubric 的“AI评估”宣传 |
| 中文短剧生产 | 剧火AI、PPDrama、LibTV、剧大虾、小镜故事板、知剧AI | 小说/剧本到分集、分镜、资产、视频 | 把生产工具误认为评价工具 |
| GitHub 格式解析 | screenplay-tools、screenplay-pdf-to-json、mcqx4/screenplay-parser | FDX/Fountain/PDF 解析、角色/对白/场景抽取 | 英文标准格式假设 |
| GitHub 中文短剧结构化 | ReelForge-YAML、Novel2Script Studio | source_map、YAML schema、linter、hook/cliffhanger/visual executability | 偏小说改编，不是强弱剧本评价 |
| GitHub 生产链路 | SceneFlow、Scenarix、Seedance2-Storyboard-Generator | 剧本-视频 cue、分镜、资产一致性、AI 视频工作流 | prompt 工具不等于剧本判断系统 |

最重要的判断：

1. 评价模块必须分成两层：`诊断分` 和 `生产/商业适配判断`。前者告诉哪里强弱，后者判断是否值得进入制作。
2. 每个结论必须绑定证据锚点：第几集、第几场、第几句、对应机制是什么。
3. 不要先做“爆款概率”。没有真实结果标签和弱样本对照时，只能做“强弱机制判断”和“制作适配判断”。
4. 2024-2026 短剧市场已经不再只有小程序 IAP 付费逻辑。IAA 免费短剧、平台原生、品牌短剧、AI 漫剧、精品化和合规治理都会改变评价标准。
5. 开头钩子、集尾钩子、付费/留存点、爽点兑现、主角引擎、关系引擎、冲突递进、AI 视频适配，必须成为短剧原生 P0 维度。

## 1. 研究边界

本研究不是为了回答“哪个平台最好用”，而是回答：

> 别人是如何把剧本变成可评价、可打分、可改写、可生产的视频资产的；哪些机制值得借鉴，哪些只是黑盒营销。

本项目已有基线：

- 不是通用剧本评分工具。
- 第一目标不是生成剧本，而是提取有证据的强剧本 pattern。
- 必须有强剧本和弱/普通剧本对照。
- 外部 skill、平台、开源项目只能作为假设，必须回到用户剧本 corpus 交叉验证。
- 时效性必须入库，老 pattern 不等于当前有效 pattern。

证据强度分级：

| 等级 | 含义 |
|---|---|
| High | 官方文档、公开样例、代码/测试/README 可直接验证 |
| Medium | 官方营销页或可靠媒体/访谈支撑，但缺少完整 schema/rubric |
| Low | 第三方介绍、产品宣传、无法复核的准确率/效果宣称 |
| Unknown | 未找到公开证据 |

## 2. 海外剧本智能分析平台

### 2.1 总览

| 平台 | 类型 | 输入 | 输出 | 生成剧本 | 生产链路 | 证据强度 |
|---|---|---|---|---|---|---|
| StoryFit | 剧本/故事智能分析、受众洞察 | 剧本/内容文本，具体文件格式未完全公开 | 角色网络、情绪强度、结构、主题、受众画像、comps | 未见公开证据 | 开发到营销发行建议 | High |
| Largo.ai | 内容洞察、受众模拟、财务预测 | script、video、brief | genre/emotion DNA、角色、受众模拟、票房/流媒体预测 | 未见公开证据 | 开发、融资、发行、版本分析 | High/Medium |
| ScriptBook | 剧本预测分析 | 英文标准电影剧本 PDF | story DNA、票房、目标受众、分级、地域预测 | 本平台未见 | greenlight/融资 | Medium |
| Cinelytic / Callaia / ScriptSense | 影视决策智能、AI coverage、IP 管理 | script、项目变量、IP 资料 | coverage、预算、comps、演员建议、发行预测、版本比较、production breakdown | 不生成完整剧本 | 开发、预算、发行、IP 管理 | High |
| Vault AI | 预测内容智能/消费者洞察 | idea/content lifecycle，公开格式不细 | 受众共鸣、市场表现、营销策略 | 未见公开证据 | 偏决策和营销 | Medium |
| Filmustage | AI 前期制作/剧本拆解 | 任意语言/格式剧本，含 short/vertical drama | 场景拆解、角色/道具/地点/VFX/服装 tag、排期、预算 | 不生成完整剧本 | 直接进入前期制作 | High |

### 2.2 StoryFit

StoryFit 最值得看的不是“AI 预测成功”，而是它如何把剧本文本转成多个可解释的结构化层：

- 角色中心性和角色互动网络。
- 场景/幕级情绪强度。
- 结构、主题、角色、受众匹配。
- 与类似作品的 comparison。
- 受众年龄/性别、genre audience、audience affinity。

对本项目的启发：

- 可以借鉴情绪峰谷、角色关系中心性、强弱作品对照的报告结构。
- 可以把“情绪强度曲线”改造成短剧维度里的“压力-兑现-新问题”曲线。
- 不能把 StoryFit 的受众预测当成短剧爆款判断依据。它的公开证据不是中文竖屏短剧，也不是付费点/爽点专项。

对钩子/付费点覆盖：

- 公开证据里没有直接看到“前 3 秒/前 30 秒钩子”“集尾付费点”的产品字段。
- 可作为 proxy 的是 opening emotional intensity、scene/episode level emotional intensity、audience pull。
- 本项目必须自定义短剧钩子 schema。

来源：

- https://storyfit.com/
- https://storyfit.com/script-analysis-famous-screenplays/
- https://storyfit.com/take-a-look-at-first-look/
- https://storyfit.com/predicting-audience-sentiment-storyfit-x-kouo/

### 2.3 Largo.ai

Largo.ai 的重点是内容洞察、受众模拟和商业预测。它公开强调：

- 上传 script、video 或 brief。
- 分析 genre、emotion、角色、关系、选角、受众。
- 用 digital twins 做受众模拟。
- 对不同剧本/剪辑版本进行比较。
- 支持融资、发行、流媒体表现等预测。

对本项目的启发：

- 借鉴“版本对比”：同一剧本改稿前后，钩子、节奏、爽点、制作风险如何变化。
- 借鉴 genre/emotion DNA，但要换成短剧原生标签。
- 受众模拟可以作为后期 P2，不应该在 V1 变成核心判断。

不能照搬：

- 电影/TV 的财务预测。
- 演员、发行、票房/流媒体预测。
- 黑盒准确率宣传。

来源：

- https://home.largo.io/largo-content-insights/
- https://home.largo.io/largo-rapid-insights/
- https://home.largo.io/largo-ai-now-includes-powerful-new-tools/

### 2.4 ScriptBook

ScriptBook 是典型的“剧本成功预测/greenlight”平台。公开信息中，它强调：

- NLP、ML、story feature engineering。
- 大量剧本参数和结果数据。
- 360 analysis、story DNA、target demographics、MPAA、territory forecast。
- 上传标准电影剧本 PDF，公开信息显示英文、标准格式、非扫描 PDF，且不适合 short form。

对本项目的启发：

- 可以借鉴“把剧本转成 feature vector”的思路。
- 可以借鉴报告结构：故事 DNA、目标受众、市场定位。

不能照搬：

- 票房/财务预测。
- 英文长片剧本参数。
- 对 short form 不友好的格式假设。

来源：

- https://www.scriptbook.io/scriptbook
- https://www.scriptbook.io/technology
- https://upload.scriptbook.io/

### 2.5 Cinelytic / Callaia / ScriptSense

这一组的价值在于它把剧本 coverage 和影视商业决策连接起来。

Callaia 公开的 coverage 维度包括：

- premise
- originality
- dialogue
- structure
- logic
- character
- conflict
- tone
- pacing
- craft

还可输出：

- logline、synopsis
- genre percentage、keywords
- comparable films
- actor recommendations
- budget、release timing、go-to-market 信息

对本项目的启发：

- coverage 报告可以采用“维度分 + rationale + evidence”的结构。
- 可以保留 go-to-market 元数据，但不能让它压过短剧机制分析。
- “premise/originality/dialogue/structure”这些通用维度必须降级为 support 维度，短剧 P0 应该是钩子、爽点、留存、付费/继续看动机。

来源：

- https://www.cinelytic.com/
- https://thecinelyticgroup.com/
- https://www.callaia.ai/
- https://www.callaia.ai/faq
- https://www.callaia.ai/use_cases
- https://scriptsense.app/

### 2.6 Filmustage

Filmustage 不适合当“剧本好坏判断器”，但非常适合做“AI 视频制作适配”参考。

它公开强调：

- 任意语言/格式剧本。
- 支持 short & vertical dramas。
- 自动拆 cast、props、locations、VFX、wardrobe。
- 进入 schedule、budget、call sheet、risk analysis。

对本项目的启发：

- 生产可行性要独立成维度，不要混进故事好坏。
- AI 视频风险标签应该包括：角色数、场景数、道具、车辆、人群、打斗、亲密、VFX、动物/儿童、连续性敏感、角色视觉一致性。
- 好剧本如果最强爽点无法被当前 AI 视频稳定表达，也应该被标为“生产高风险”。

来源：

- https://filmustage.com/
- https://filmustage.com/script-breakdown/
- https://filmustage.com/ai-script-analysis/
- https://filmustage.com/blog/how-to-break-down-a-vertical-drama-script-for-production/
- https://filmustage.com/blog/how-to-write-a-vertical-drama-script/

## 3. 行业评审与 AI Coverage 机制

### 3.1 总览

| 对象 | 类型 | 评分/推荐机制 | 对本项目价值 | 风险 |
|---|---|---|---|---|
| Slated | 剧本/成片分析 + 融资平台 | 10 类 1-5 分，合成 100 分 Script Score；Strong Pass 到 Strong Recommend | 学评分尺度、多人评审、证据引用 | 电影融资导向 |
| The Black List | 剧本托管 + 行业评价 | 1-10 分；8+ 触发曝光/推荐 | 学多读者一致性和高分触发机制 | 非改稿工具，非短剧 |
| Coverfly | 历史剧本平台/竞赛聚合 | 已于 2025-09-01 停止服务 | 只借榜单/跨来源聚合思想 | 2026 已不可作为活平台 |
| Prescene | AI screenplay workbench | coverage、scene citation、market scorecard | 学“剧本问答 + 场景证据引用 + 开发工作流” | rubric 未完全公开 |
| OnDesk | AI coverage + 内容库 | pass/consider/recommend 样例、strength/weakness | 学团队内容库、差稿因果诊断、版本比较 | 正式分数表不公开 |
| Callaia | AI Coverage+ | 维度分 + 4/5 + Recommend 样例 | 学报告结构和分项 rationale | 电影指标需改写 |
| ScriptReader.ai | AI scene/script analysis | 场景级多维评分、Hook Out、continue reading | 学场景必要性、下一场钩子、turn potency | 格式/中文支持未知 |

### 3.2 Slated

Slated 的公开评分体系很有参考价值，因为它明确把评分拆成维度、等级和推荐语：

- Character
- Conflict
- Craft
- Dialogue
- Logic
- Originality
- Pacing
- Premise
- Structure
- Tone

每项 1-5 分，再合成 100 分 Script Score。公开等级包括：

- 90+ exceptional
- 80+ excellent
- 70+ above average
- 60+ below average
- 60 以下 poor

推荐等级包括：

- Strong Pass
- Pass
- Consider
- Recommend
- Strong Recommend

对本项目的启发：

- 可以借“维度分 + 权重 + 推荐等级 + 证据页码/时间码”。
- 不要照搬维度和权重。本项目需要把 Character/Structure/Pacing 改写成短剧 P0 维度。
- 推荐等级应该改成生产语义，例如：`可进入制作`、`小改后制作`、`需重构`、`拒绝制作`、`只保留素材/人设`。

来源：

- https://help.slated.com/en/articles/31116-how-do-your-readers-assess-each-script

### 3.3 The Black List

The Black List 的价值不是维度多，而是行业评价机制：

- 人工专业读者。
- 1-10 分。
- 8+ 是高分信号。
- 一个 8+ 可触发更多曝光；两个 8+ 可显示 Black List Recommended。
- 2026 官方公开过评价一致性数据，说明它关注不同读者之间的一致性。

对本项目的启发：

- 单次 AI 判断不可靠，后续可以做多评审视角：结构评审、短剧商业评审、AI 视频制作评审、合规风险评审。
- 可以让高分触发动作：进入 pattern library、进入改稿建议、进入生产评估。
- 不能照搬 Hollywood 的“稀缺推荐”逻辑。短剧生产需要更高吞吐，不是只有极少数剧本被推荐。

来源：

- https://help.blcklst.com/kb/guide/en/writers-pROPvK6l0J/Steps/2683802
- https://blcklst.substack.com/p/how-consistent-are-black-list-evaluations

### 3.4 Prescene / OnDesk / Callaia / ScriptReader.ai

这些工具适合作为 AI coverage 的形态参考。

可借鉴：

- 剧本上传后生成 coverage。
- scene-by-scene 分析。
- 角色拆解。
- dialogue & pacing 评价。
- theme/tone/motif。
- comparable titles。
- budget/schedule/pitch materials。
- Script Chat：对剧本提问，并带场景引用。
- strengths / weaknesses / recommendation。
- 场景级 Hook Out、Scene Necessity、Turn Potency、Compelled to keep Reading。

对本项目的启发：

- 不要只出一段“这个剧本不错”。要出维度、证据、问题、改法、生产影响。
- 差稿诊断要因果化。例如不是“节奏慢”，而是“第 2-4 集没有改变主角压力/关系状态，导致第 5 集付费点前没有足够情绪债”。
- 每场/每集都应该回答：这场是否改变故事状态？是否制造下一场动机？是否有爽点/压力/信息增量？

来源：

- https://www.prescene.ai/
- https://www.prescene.ai/features
- https://www.prescene.ai/pricing
- https://www.itsondesk.com/
- https://www.callaia.ai/
- https://scriptreader.ai/

## 4. 中文短剧 / AI 短剧平台

### 4.1 总览

| 平台 | 定位 | 输入 | 输出 | 是否评剧本 | 是否写剧本 | 是否分镜 | 是否视频生产 | 判断 |
|---|---|---|---|---|---|---|---|---|
| 创一AI/咔咔猩 | 短剧剧本评估 + 创作 + 拉片 | 剧本、视频、短片参考 | 评估报告、剧本、拉片/分镜、视频转剧本 | 是 | 是 | 是 | 有宣传 | 评价+生产前端 |
| 剧拆拆 | AI 短剧拆稿/诊断工具 | docx/txt/粘贴正文、视频 | 10 维诊断、单集桥段分析、批注、视频转剧本 | 是，核心 | 不主打 | 有视频转剧本/骨架 | 否 | 最像评价竞品 |
| StoryPlay | AI 短剧剧本创作平台 | 灵感、题材、策划文本 | 策划、初稿、润色、分发、剧本转视频 | 未见证据 | 是 | 有分镜关键词 | 有宣传 | 写作/协作工具 |
| 知剧AI | 智能短剧创作平台 | 创意、小说文本 | 分集大纲、角色、台本、分镜脚本、封面、Word | 未见证据 | 是 | 是 | 未见可靠成片证据 | 改编/生成工具 |
| 剧火AI | AI 编剧 + 导演，一人短剧工作室 | 一句话、小说/剧本文件 | 策划、分镜、角色场景、配音、AI 视频 | 未见证据 | 是 | 是 | 是 | 生产工具 |
| PPDrama | 从剧本到分镜/素材/视频 | 剧本文件 | 剧本解析、人物场景管理、分镜表、图片/视频、配音 | 未见证据 | 部分构思 | 是 | 是 | 生产前期工具 |
| LibTV | AI 视频创作工具/Agent 平台 | 自然语言、图/视频参考 | 图/视频生成编辑、短剧剧本到分镜到成片 | 未见证据 | 是 | 是 | 是 | Agent 生产工具 |
| 剧大虾 | 一站式 AI 短剧制作平台 | 主题、已有剧本 | 剧本、角色/场景/道具、分镜、视频 | 未见证据 | 是 | 是 | 是 | 项目化生产工具 |
| 小镜故事板 | AI 分镜脚本与视频提示词工具 | 故事/脚本 | 镜号、画面、时长、运镜、资产库、生图词、视频词、导出 | 未见证据 | 不主打 | 是，核心 | 不直接成片 | 分镜/资产工具 |

### 4.2 创一AI / 咔咔猩

公开证据显示它最接近“评价 + 生产前端”的方向。

公开能力：

- 剧本采购、剧本评估、剧本写作、智能拉片。
- 视频转分镜、视频转剧本。
- “剧本医生 API”相关报道提到智能评估、结构拆解、内容品控、合规审查、叙事逻辑拆解、市场潜力预测。
- 访谈中提到节奏评分、市场契合度、钩子/节奏量化标准。

可借鉴：

- B 端实际关心的不是“写得好不好”，而是初筛、品控、市场潜力、合规、结构拆解。
- “剧本医生”应输出可改稿、可生产的结果，而不是文学点评。

不能照搬：

- 未公开完整 rubric。
- “市场潜力预测”属于黑盒宣传，不能作为本项目 V1 标准。

来源：

- https://www.creatifyone.com/
- https://ex.chinadaily.com.cn/exchange/partners/114/rss/channel/cn/columns/07pz5d/stories/WS6a30f924a310d709c2fb861e.html
- https://adg.csdn.net/697079ec437a6b40336a6a82.html

### 4.3 剧拆拆

剧拆拆是这轮里最像本项目“评价/诊断工具”的中文产品。

公开能力：

- 上传剧本或粘贴正文。
- 支持 docx、txt。
- 10 维并行诊断。
- 每集问题清单和改稿建议。
- 视频理解，转每集分镜和剧情骨架。

公开维度接近：

- 事件
- 情绪
- 台词
- 节奏
- 结构
- 逻辑
- 氛围
- 卖点
- 格式
- 合规

公开页面中还出现：

- 桥段密度
- 转折节奏
- 情感曲线
- 钩子分布
- 卡点设计
- 主副线
- 人物动机
- 商业钩子
- 平台适配
- 转化点

可借鉴：

- 维度组合很接近短剧评价。
- “问题清单 + 改稿建议”比单纯评分更有用。
- 公开强调格式和合规，说明这两项是实际交付风险。

不能照搬：

- 公开信息仍不足以确认评分算法、阈值和稳定性。
- “商业钩子/转化点”不等于我们的付费点/留存点，需要样本校准。

来源：

- https://www.juchaichai.com/

### 4.4 生产类平台：剧火AI、PPDrama、LibTV、剧大虾、小镜故事板、知剧AI

这些平台大多不是评价工具，但对“AI 视频制作适配”很有价值。

共性链路：

```text
创意/小说/剧本
-> 剧本/分集/台本
-> 角色、场景、道具资产
-> 分镜表 / 镜头脚本
-> 生图词 / 视频词
-> 配音 / 字幕 / 音效
-> 视频生成或视频生产包
```

对本项目的启发：

- 剧本分析输出不能只给编剧看，也要给导演/监制/AI 视频 agent 看。
- 必须结构化输出角色、场景、道具、镜头、视觉一致性、资产复用、生成难度。
- 剧本好坏和可生产性要分开：一个文本上不错的剧本，如果场景/角色/动作复杂度过高，AI 生产风险也高。

来源：

- StoryPlay：https://storyplay.cn/
- 知剧AI：https://www.zhijuu.com/
- 剧火AI：https://juhuo.cn/
- PPDrama：https://www.ppdrama.cn/
- LibTV：https://www.liblib.tv/
- LibTV skill：https://raw.githubusercontent.com/libtv-labs/libtv-skills/main/skills/libtv-skill/SKILL.md
- 剧大虾：https://www.judaxia.art/
- 小镜故事板：https://xjstoryboard.com/

## 5. GitHub 开源项目

### 5.1 总览

这轮 GitHub 搜索最重要的结论是：

> 独立、成熟、可复用的“AI screenplay coverage/evaluator”开源项目很少；真正有价值的是格式解析、结构化 schema、source map、linter、分镜/视频生产链路。

高价值项目：

| Repo | 主要能力 | 价值 | 风险 |
|---|---|---|---|
| https://github.com/wildwinter/screenplay-tools | Fountain/FDX parse/write，多语言，元素模型 | 标准格式入口 | 不处理中文短剧和混乱格式 |
| https://github.com/SMASH-CUT/screenplay-pdf-to-json | clean PDF 剧本转 JSON | PDF 吸收参考 | OCR/脏 PDF 弱，偏英文格式 |
| https://github.com/mcqx4/screenplay-parser | FDX/Fountain -> scene JSON，shotlist | 轻量 schema 参考 | 测试少，shotlist 是启发式 |
| https://github.com/ifrost/afterwriting-labs | Fountain 后处理、统计、PDF、FDX import | 统计和导出参考 | 偏 Fountain 生态 |
| https://github.com/wangzichang224-design/ReelForge-YAML | 中文网文 -> 竖屏短剧 YAML，source_map，评测器 | 最贴近短剧 schema/linter | 偏小说改编，不是剧本强弱评价 |
| https://github.com/wordxzl03-oss/novel2script-studio-mvp | Evidence-RAG、episode-first schema、linter、改编开发包 | 证据链和工作台思路强 | 工程重，不能直接搬 |
| https://github.com/taruma/SceneFlow | 剧本-视频同步，cue 类型，staging/brief | 分镜/视频对齐参考 | 不做剧本评价 |
| https://github.com/yakupbulbul/scenarix | AI 短剧端到端，剧本/图/配音/字幕/视频/评分 | 生产链路参考 | 依赖外部 API，评分是 LLM judge |
| https://github.com/liangdabiao/Seedance2-Storyboard-Generator | Claude Skill + Seedance 2.0 工作流 | 短剧视频生成提示词、资产编号、延长视频链路 | 不是评价系统 |

### 5.2 格式解析层

#### screenplay-tools

最适合作为标准格式解析参考。它支持：

- Fountain
- Final Draft FDX
- 解析为统一 Script/Element 模型
- 元素包括 scene heading、action、character、dialogue、parenthetical、transition、section、synopsis 等
- 多语言实现：JS、Python、C#、C++
- MIT 许可

对本项目的用法：

- 如果用户后续剧本有 FDX/Fountain，可参考其元素模型。
- 不要假设中文短剧都会是标准 screenplay 格式。
- 可以借它的 Element 设计，但要加 Episode/Scene/Beat/Hook/Payoff 等短剧字段。

来源：

- https://github.com/wildwinter/screenplay-tools

#### screenplay-pdf-to-json

适合参考 clean PDF 剧本解析。

公开能力：

- PDF -> JSON。
- 输出 page、scene_info、scene。
- 支持 ACTION、CHARACTER、TRANSITION、DUAL_DIALOGUE。
- 明确说明 clean PDF 效果较好，不适合 OCR PDF。

对本项目的用法：

- PDF 解析可以借 page/坐标/段落/角色对白抽取。
- 必须在 importer 里标注 OCR、重复文本、页眉页脚、错行等风险。
- 中文 PDF 不一定适用，需要单独实测。

来源：

- https://github.com/SMASH-CUT/screenplay-pdf-to-json

#### mcqx4/screenplay-parser

轻量级 FDX/Fountain 解析器，输出 scene JSON：

- heading
- location_type
- location
- time_of_day
- action
- characters
- dialogue_count
- shot_estimate

对本项目的用法：

- 可借 scene JSON 最小字段。
- shot_estimate 只能当粗略启发，不是镜头设计。

来源：

- https://github.com/mcqx4/screenplay-parser

### 5.3 中文短剧结构化 / 评测项目

#### ReelForge-YAML

这是最贴近本项目“结构化短剧 schema + 规则评测”的开源参考之一。

公开能力：

- 3 章以上小说转竖屏短剧 YAML。
- episodes -> shots。
- 每集 hook_summary、emotional_curve、cliffhanger。
- visual_track / audio_track 分离。
- source_ref 和 source_map。
- visual_bible 固定角色和资产。
- 规则化评测：黄金三秒、结尾钩子、权力翻转、视觉可执行性、角色连续性、来源追溯。
- badcase 报告和 critic-generator 局部优化。

对本项目的启发：

- source_map/source_ref 是必须借鉴的。
- “Schema valid 不等于好短剧”这个原则非常重要。
- 硬指标可以先做护栏，而不是一上来预测爆款。
- hook、cliffhanger、power_shift、visual_executability、continuity 很适合进入 P0/P1。

不能照搬：

- 它偏小说改编，不是已有剧本强弱评价。
- 它把“首镜头必须 opening_hook”等作为生成约束，但我们的评价模块要能判断“这个 hook 是否有效”，不能只看字段名。

来源：

- https://github.com/wangzichang224-design/ReelForge-YAML

#### Novel2Script Studio

这是更工程化的竖屏微短剧改编工作台。

公开能力：

- Evidence-RAG + Bounded Agent。
- Episode-first schema。
- IP 诊断、故事圣经、前 10 集分集大纲、前 3 集完整剧本。
- 三类溯源、来源绑定、原文高亮。
- short-drama linter。
- 钩子、留存节点、策划标记层、分集节奏板。
- 忠实度、Diff、改编日志。
- 开发包导出。

对本项目的启发：

- “AI 负责写，代码负责证明，界面负责让人掌控”是非常适合本项目的原则。
- Episode-first 比 Scene-first 更适合短剧。
- AI 输出必须落进 schema，不应以游离纯文本存在。
- Linter 和 source validation 可以成为 V1 护栏。

不能照搬：

- 它是小说改编工作台，不是 pattern library。
- 工程范围大，不适合本项目 V1 直接实现。

来源：

- https://github.com/wordxzl03-oss/novel2script-studio-mvp

### 5.4 生产链路项目

#### SceneFlow

价值在剧本-视频同步和 cue 结构：

- script text + cues。
- shot/camera/audio/VFX/environment 类型。
- staging blocks。
- AI 视频 adherence 评估 UI。

可借鉴：

- 给 AI 视频 agent 的输出不应只有剧本文字，而应包括 cue、staging、visual brief。

来源：

- https://github.com/taruma/SceneFlow

#### Scenarix

端到端 AI 短剧生产参考：

- 剧本。
- 图像。
- 配音。
- 字幕。
- 竖屏视频。
- quality score。

可借鉴：

- 系列 bible、episode JSON、质量评分、MCP 工具链。

风险：

- 依赖外部 API。
- 评分多为 LLM judge，不能作为硬证据。

来源：

- https://github.com/yakupbulbul/scenarix

#### Seedance2-Storyboard-Generator

这个项目对 AI 视频生产约束很有价值。公开 README 强调：

- Claude Code + Skill + Seedance 2.0。
- 从故事到多集视频。
- 剧本创作、素材规划、生图、分镜脚本、逐集生成视频。
- 角色/场景/道具编号：C/S/P。
- Seedance 时间轴格式。
- 15 秒视频延长。
- 风格一致性、角色一致性、敏感词、参考图数量、视频参考数量、复杂提示词不稳定等限制。

对本项目的启发：

- AI 视频适配不是附加项，而是短剧剧本评价的一部分。
- 评价模块应输出：角色/场景/道具资产复用、尾帧衔接风险、提示词复杂度、敏感词风险、动作/群戏/VFX 风险。

来源：

- https://github.com/liangdabiao/Seedance2-Storyboard-Generator

## 6. 2024-2026 时效判断

### 6.1 关键变化

2024-2026 的短剧市场不应再被简化为“小程序 IAP 单集付费投流”。

公开资料显示，行业正在发生几类变化：

1. 商业模式多元化：IAP、IAA、会员免费、平台分账、品牌短剧、电商短剧、出海订阅/内购并行。
2. 平台多元化：小程序之外，红果、抖音端原生、快手、长视频平台、电视大屏、品牌/电商场景都在参与。
3. 监管强化：分类分层审核、备案号/许可证号、白名单、专项治理。
4. 精品化趋势：现实、文旅、普法、科普、非遗、品牌、传统文化、精品 IP 改编被鼓励。
5. AI 制作成为变量：AI 漫剧、低成本视频生产、“一人一剧组”出现，但真人 AI 短剧稳定商业质量仍需谨慎。

来源：

- 广电总局 2025 分类分层、白名单通知：https://www.nrta.gov.cn/art/2025/2/5/art_113_70148.html
- 广电总局 2026 微短剧精品创作传播计划：https://www.nrta.gov.cn/art/2026/5/26/art_113_73378.html
- 广电总局 2026 专项治理：https://www.nrta.gov.cn/art/2026/6/3/art_114_73404.html
- QuestMobile 2026 短剧行业洞察：https://www.questmobile.com.cn/research/report/2041710682848727041/
- 新华社/人民日报《中国网络视听发展研究报告 2026》：https://www.news.cn/politics/20260416/cac5d121fdbf4dd88a92f22bc2218e9d/c.html

### 6.2 时效分类

| 类型 | 定义 | 示例 | 处理方式 |
|---|---|---|---|
| evergreen-craft | 常青故事机制 | 清晰欲望、压力、选择、冲突递进、情绪兑现、因果反转 | 可作为基本 craft，但不自动当 differentiator |
| current-market-pattern | 当前市场/平台有效模式 | IAA 免费短剧、红果/抖音端原生、AI 漫剧、品牌短剧、横屏精品、文旅/普法/非遗 | 需要标日期、平台、市场 |
| aging-pattern | 曾经有效但需复核 | 只按小程序 IAP 设计全剧、固定第 8-12 集付费卡点、只追投流 ROI | 需要新样本确认 |
| stale-or-risky | 过时或高风险 | 拜金霸总、软色情擦边、畸形婚恋、暴力复仇、封建糟粕、低俗标题、诱导充值、侵权 IP | 不作为正向 pattern，只作风险 |

### 6.3 对本项目的影响

评价模块不能硬编码“第几集必须付费”。正确做法是记录：

- 商业模式：IAP / IAA / 会员 / 品牌 / 电商 / 出海。
- 留存机制：继续看理由、广告容忍理由、付费理由、复看理由。
- 钩子位置：前 3 秒、前 10 秒、前 30 秒、首集、集尾、付费/转化点。
- payoff 兑现：同集、下一集、1-2 集后、长期延迟、未兑现。
- 平台/市场：国内、海外、红果/抖音/快手/小程序/品牌。
- 时效状态：current、aging、stale、evergreen。

## 7. 好剧本 / 差剧本 / 合适剧本

### 7.1 好剧本标准

短剧语境下的“好剧本”不是文学意义上的好，而是：

1. 开头进入快，能在前 3-30 秒建立压力、关系差、身份差或未完成问题。
2. 主角引擎清楚：主角想要什么，为什么现在必须行动，为什么观众站在 TA 一边。
3. 关系引擎可持续：爱恨、误会、身份、利益、依赖、背叛、保护、嫉妒能持续制造戏。
4. 冲突递进快，每 1-3 集改变局面，而不是重复同一种羞辱。
5. 爽点有积累和兑现：压迫 -> 证据/能力/身份释放 -> 对手付代价 -> 新代价出现。
6. 集尾钩子不是机械切断，而是在身份将揭露、惩罚将发生、关系将反转、选择不可逆处切断。
7. 反转改变故事状态，不只是临时吓人。
8. 每集有信息增量、情绪增量或关系位移。
9. 场景、角色、动作复杂度适合 AI 视频或目标制作方式。
10. 不依赖明显过时、擦边、侵权或高合规风险套路。

### 7.2 差剧本标准

差剧本不等于文笔差，更多是“不适合短剧目标”：

1. 开头只铺设定，不给冲突。
2. 主角被动，没有持续行动引擎。
3. 角色只有标签，没有可持续选择。
4. 关系静止，十几集仍是同一种羞辱/误会。
5. 冲突靠误会硬拖，不升级。
6. 爽点低级重复，打脸无代价、无新局面。
7. 集尾钩子只是“有人推门/主角震惊/下集再说”。
8. 反转频繁但无因果。
9. 格式混乱到无法稳定保留集数/场次/对白。
10. 场景多、角色多、动作复杂，导致 AI 视频成本和失败率高。
11. 题材/表达存在合规红线或明显时效衰退。

### 7.3 合适剧本标准

“合适”比“好”更接近本项目目标。

一个剧本适合进入 AI 短剧生产，至少要满足：

- 故事机制适合短剧，而不是只适合小说。
- 情绪和动作能被视频表达。
- 角色、场景、道具可资产化。
- 强场面不是全靠复杂群戏、微妙表演、难生成动作或不可控 VFX。
- 格式可解析，能保留 episode/scene/line 证据。
- 有明确可改方向，而不是从 premise 开始就错。

## 8. 钩子专项标准

### 8.1 好开头钩子

好开头钩子不是“有悬念”，而是短时间内建立一个观众必须继续看的未完成问题。

标准：

1. 立刻可懂：不需要长背景。
2. 情绪明确：羞辱、危险、背叛、误认、欲望、压迫、反击至少有一个强信号。
3. 人物绑定：不是随机事件，而是主角命运被改变。
4. 有承诺：观众知道继续看会得到什么答案或爽点。
5. 有差异：身份差、权力差、关系差、信息差、利益差至少有一个。
6. 可视频表达：能在竖屏短镜头里看清。
7. 不是纯遮挡信息：不能只靠“其实另有隐情”拖延。
8. 不欺骗观众：后续必须兑现承诺。

### 8.2 差开头钩子

1. 只有设定，没有冲突。
2. 只有奇观，没有人物命运。
3. 只有问题，没有情绪。
4. 需要解释太多背景。
5. 主角不行动，只被介绍。
6. 反常识但无后续承诺。
7. 视觉难表达，靠旁白解释。
8. 后续 payoff 与钩子无关。

### 8.3 好集尾钩子

1. 在答案前切断，而不是答案后切断。
2. 切在不可逆选择、身份揭露、惩罚发生、关系反转、证据曝光前。
3. 让观众知道下一集会解决哪个具体问题。
4. 解决一个问题时制造更强问题。
5. 不重复同一种“震惊脸”。
6. 1-2 集内兑现关键承诺，否则会变成骗看。

### 8.4 差集尾钩子

1. 机械打断一句话。
2. 下集开头很快化解，没有代价。
3. 没有新信息、新压力或关系变化。
4. 每集都是同一种来人/电话/推门。
5. 承诺不清，观众不知道继续看什么。
6. 靠假悬念拖时间。

### 8.5 付费点 / 留存点

不能再只按“第 8-12 集固定付费”理解。应该按商业模式拆：

| 模式 | 关键问题 |
|---|---|
| IAP 单集付费 | 观众为什么现在愿意付费？付费后会得到什么答案/爽点？ |
| IAA 免费广告 | 观众为什么愿意继续看广告？每几分钟有新回报？ |
| 会员/平台免费 | 观众为什么收藏、追更、完播？ |
| 品牌短剧 | 故事动机和品牌场景是否自然？ |
| 出海 | 文化门槛、题材翻译性、关系张力是否可跨市场理解？ |

## 9. 格式吸收与导入契约

### 9.1 外部项目给出的启发

外部平台和开源项目说明，格式吸收必须分层：

1. 标准格式：Fountain、FDX，可以用 parser 解析 scene heading、action、character、dialogue。
2. PDF：clean PDF 可以抽 page、scene、character、dialogue；OCR PDF 需要降级。
3. DOCX/TXT/Markdown：需要启发式识别集数、场次、角色、对白。
4. 小说/大纲：不是剧本，需要走“改编/结构化”链路，不能当作已完成剧本评价。
5. 视频/成片：可以做 video-to-script 或拉片，但证据锚点变成时间码。

### 9.2 本项目 V1 导入契约

V1 importer 必须输出：

- `script_id`
- `source_path`
- `format`
- `confidentiality`
- `import_status`
- `episode_boundaries`
- `scene_boundaries`
- `character_candidates`
- `dialogue_blocks`
- `action_blocks`
- `line_ranges`
- `import_warnings`

导入状态：

| 状态 | 含义 | 是否可提取 pattern |
|---|---|---|
| imported | 结构基本可信 | 可以 |
| needs-cleanup | 集数/场次/对白有局部问题 | 只能做低置信分析 |
| failed | 无法保留关键边界 | 不允许提取 pattern |
| source-type-mismatch | 输入其实是小说/大纲/视频拉片 | 转入改编/拉片流程，不当剧本评价 |

### 9.3 格式差异风险

不同格式能否吸收，不应只回答“支持/不支持”，而要标风险：

- 是否保留集数。
- 是否保留场次。
- 是否保留页码/行号。
- 是否区分对白和动作。
- 是否识别角色别名。
- 是否能处理多人对白。
- 是否有 OCR 错误。
- 是否重复页眉页脚。
- 是否混入注释、拍摄说明、分镜。
- 是否需要人工标注。

## 10. 建议的分析/评价模块

### 10.1 P0：V1 必须有

| 模块 | 输出 | 为什么是 P0 |
|---|---|---|
| 格式吸收与证据锚点 | episode/scene/line/source warnings | 没有证据锚点，所有评价都不可审计 |
| 开头钩子 | first_hook_position、hook_type、hook_promise、hook_effectiveness | 短剧留存入口 |
| 集尾钩子 | cliffhanger_type、cut_point、unresolved_question、payoff_timing | 连续观看/付费核心 |
| 主角引擎 | desire、pressure、wound/status、agency、audience_alignment | 主线能否持续 |
| 关系引擎 | core_pair、power_gap、secret/dependency、renewability | 短剧持续冲突来源 |
| 冲突递进 | obstacle_type、escalation_ladder、episodes_without_pressure | 判断是不是重复拖集 |
| 爽点/情绪兑现 | payoff_type、setup_distance、payoff_strength、next_question | 判断是否有短剧快感 |
| 反转/信息控制 | reveal_type、state_change、audience_knowledge_gap | 判断反转是否有效 |
| 强弱对照 | strong_vs_contrast_difference、discriminating | 防止抽出正确废话 |
| AI 视频适配 | locations、characters、asset_reuse、risk_scenes | 服务最终生产 |
| 合规/风险预警 | risk_tags、source_evidence、needs_human_review | 2026 必须考虑 |

### 10.2 P1：重要但可第二阶段

- 题材/人设/情绪 tag。
- 平台/商业模式匹配：IAP、IAA、会员、品牌、电商、出海。
- 付费点/留存点专项。
- 题材拥挤度和衰退风险。
- 角色视觉标签稳定性。
- 品牌植入自然度。
- 横屏/大屏精品化潜力。
- 版本对比：改稿前后变化。

### 10.3 P2：暂不应该硬做

- 爆款概率。
- 精确付费转化。
- 平台推荐算法预测。
- 单剧 ROI。
- AI 生产成本节省比例。
- 题材一定爆/一定死。

这些需要真实结果标签、平台数据或至少较多弱/失败样本。

## 11. 推荐评分与标签设计

### 11.1 不建议一开始做总分

总分会掩盖问题。例如：

- 钩子强但 AI 制作很难。
- 文本不错但付费点弱。
- 爽点多但合规高风险。
- 老套路熟练但时效衰退。

V1 更适合用“分项判断 + 推荐动作”。

### 11.2 推荐动作

建议替代 Hollywood 的 Pass/Consider/Recommend：

| 推荐动作 | 含义 |
|---|---|
| 可进入制作 | 核心短剧机制成立，生产风险可控 |
| 小改后制作 | 主体可用，但钩子/付费点/生产复杂度需修 |
| 需重构 | premise/主角/关系/冲突中有关键缺陷 |
| 拒绝制作 | 机制弱、风险高、无明显修复价值 |
| 仅保留素材/人设 | 人设、设定或桥段可用，但剧本整体不成立 |
| 待证据 | 格式或上下文不足，不能下判断 |

### 11.3 标签体系

建议先用以下 tag：

```yaml
story_tags:
  genre_lane:
  protagonist_engine:
  relationship_engine:
  conflict_source:
  payoff_type:
  hook_type:
  cliffhanger_type:
  reversal_type:
  audience_fantasy:
  risk_tags:

production_tags:
  ai_fit:
  location_complexity:
  character_count_risk:
  asset_reuse:
  action_complexity:
  continuity_risk:
  prompt_complexity:

market_tags:
  business_mode:
  platform_context:
  recency_status:
  decay_risk:
  compliance_risk:
```

### 11.4 PatternEntry 应扩展字段

在已有 finding 的 `PatternEntry` 基础上，建议补充：

```yaml
pattern_entry:
  pattern_id:
  pattern_type:
  origin:
  evidence:
  trigger_condition:
  story_mechanism:
  audience_effect:
  reuse_rule:
  contrast_evidence:
  discriminating:
  pattern_class:
  recency_status:
  decay_risk:
  business_mode_fit:
  ai_video_fit:
  hook_promise:
  payoff_timing:
  failure_mode:
  reviewer_decision:
```

## 12. 强弱对照规则

这轮外部研究再次确认：没有弱样本对照，系统会把短剧常识当成爆款规律。

强弱对照要问：

1. 强剧本的 hook 是否更早、更清楚、更绑定主角命运？
2. 弱剧本是否也有 cliffhanger，但只是机械打断？
3. 强剧本的爽点是否改变局面，弱剧本是否只是重复打脸？
4. 强剧本的主角是否持续行动，弱剧本是否被动挨打？
5. 强剧本的关系是否能持续产戏，弱剧本是否只靠误会拖？
6. 强剧本的反转是否有因果，弱剧本是否硬拧？
7. 强剧本是否更适合 AI 视频生产，弱剧本是否最强场面难拍？

`discriminating: yes` 必须有对照证据。否则只能是 `basic-craft` 或 `unknown`。

## 13. 对本项目下一步的建议

### 13.1 不要先做完整 agent

下一步不应该是写完整系统，也不应该继续无限竞品研究。

正确动作：

1. 用这份外部研究更新研究基线。
2. 建一个小型校准包：3 个强剧本 + 2 个普通/弱剧本。
3. 对每个剧本标 3-5 个强/弱瞬间。
4. 用 P0 维度跑一遍人工/半自动分析。
5. 看这些维度能不能真正区分强弱。

### 13.2 先做最小闭环

最小闭环应该是：

```text
导入剧本
-> 保留集/场/行证据
-> P0 维度分析
-> 生成候选 pattern
-> 强弱对照
-> 用户 approve/reject/needs-evidence
-> pattern library
```

不要先做：

- 爆款概率。
- 自动生成完整剧本。
- 复杂 UI。
- 云端服务。
- 长期市场预测。

### 13.3 第一版文档/文件结构

建议本地文件结构：

```text
scripts/
  strong/
  contrast/
index/
  script-index.csv
  source-registry.md
annotations/
  manual-marks.md
  import-warnings.md
patterns/
  candidate-patterns.jsonl
  approved-patterns.jsonl
  reviews.jsonl
reports/
  calibration-report.md
  external-research.md
```

## 14. 关键来源列表

### 海外平台

- StoryFit：https://storyfit.com/
- StoryFit 剧本分析案例：https://storyfit.com/script-analysis-famous-screenplays/
- Largo.ai：https://home.largo.io/largo-content-insights/
- ScriptBook：https://www.scriptbook.io/scriptbook
- Cinelytic：https://www.cinelytic.com/
- Callaia：https://www.callaia.ai/
- ScriptSense：https://scriptsense.app/
- Filmustage：https://filmustage.com/

### 行业评审 / Coverage

- Slated 评分说明：https://help.slated.com/en/articles/31116-how-do-your-readers-assess-each-script
- The Black List 帮助文档：https://help.blcklst.com/kb/guide/en/writers-pROPvK6l0J/Steps/2683802
- The Black List 一致性文章：https://blcklst.substack.com/p/how-consistent-are-black-list-evaluations
- Prescene：https://www.prescene.ai/
- OnDesk：https://www.itsondesk.com/
- ScriptReader.ai：https://scriptreader.ai/

### 中文短剧平台

- 创一AI/咔咔猩：https://www.creatifyone.com/
- 剧拆拆：https://www.juchaichai.com/
- StoryPlay：https://storyplay.cn/
- 知剧AI：https://www.zhijuu.com/
- 剧火AI：https://juhuo.cn/
- PPDrama：https://www.ppdrama.cn/
- LibTV：https://www.liblib.tv/
- 剧大虾：https://www.judaxia.art/
- 小镜故事板：https://xjstoryboard.com/

### GitHub

- screenplay-tools：https://github.com/wildwinter/screenplay-tools
- screenplay-pdf-to-json：https://github.com/SMASH-CUT/screenplay-pdf-to-json
- mcqx4/screenplay-parser：https://github.com/mcqx4/screenplay-parser
- afterwriting-labs：https://github.com/ifrost/afterwriting-labs
- ReelForge-YAML：https://github.com/wangzichang224-design/ReelForge-YAML
- Novel2Script Studio：https://github.com/wordxzl03-oss/novel2script-studio-mvp
- SceneFlow：https://github.com/taruma/SceneFlow
- Scenarix：https://github.com/yakupbulbul/scenarix
- Seedance2-Storyboard-Generator：https://github.com/liangdabiao/Seedance2-Storyboard-Generator

### 时效与行业

- 广电总局 2025 分类分层、白名单通知：https://www.nrta.gov.cn/art/2025/2/5/art_113_70148.html
- 广电总局 2026 精品创作传播计划：https://www.nrta.gov.cn/art/2026/5/26/art_113_73378.html
- 广电总局 2026 专项治理：https://www.nrta.gov.cn/art/2026/6/3/art_114_73404.html
- QuestMobile 2026 短剧行业洞察：https://www.questmobile.com.cn/research/report/2041710682848727041/
- 新华社/人民日报 中国网络视听发展研究报告 2026：https://www.news.cn/politics/20260416/cac5d121fdbf4dd88a92f22bc2218e9d/c.html

## 15. 最终建议

本项目最好的定位不是“又一个 AI 评剧本工具”，而是：

> 一个本地优先、证据优先、短剧原生、可持续校准的剧本 pattern research system。

它应该吸收外部项目的成熟部分：

- Slated / Black List 的评分和多评审机制。
- Prescene / OnDesk / Callaia 的 coverage 报告结构。
- StoryFit / Largo 的情绪、角色、受众和版本比较思路。
- 剧拆拆 / 创一AI 的短剧诊断方向。
- Filmustage / PPDrama / 小镜 / Seedance workflow 的生产适配视角。
- ReelForge / Novel2Script 的 schema、source map、linter、证据链。

但核心判断必须回到用户自己的语料：

- 强剧本里反复出现的机制。
- 弱剧本里缺失、变弱或放错位置的机制。
- 当前市场和 AI 制作条件下仍然有效的机制。
- 能被甲方、导演、监制和视频制作 AI agent 继续使用的结构化结论。

下一步只做一件事：用 3 强 + 2 弱样本跑校准，不再继续堆框架。
