# 海外真人短剧剧本 Agent 外部生态全景研究

日期：2026-06-28  
对象：短剧剧本分析、深度重构、生产 Agent  
目标市场：海外真人短剧，兼顾 AI 视频生产适配  
状态：外部材料笔记，仅供重新做产品定义时参考

> 重启提示：这份文件不是当前产品方案，也不是 rubric。里面有些结论来自公开资料和推断，后续使用前必须重新 cross check。不要直接继承这里的模块、权重或 agent 拆法。

## 0. 结论先行

之前搜过的材料没有废，但必须重新分层。

旧材料主要覆盖“剧本分析/coverage/评价平台”。它还能用，但只能作为分析层参考，不能再当作完整产品参考。现在目标更明确：最终要从自有旧剧本中提取强机制，再按甲方要求深度重构或生成新的海外真人短剧剧本，并且能交给甲方、导演、监制和 AI 视频制作 agent。

这次补查后，外部生态可以分成六层：

| 层级 | 代表对象 | 对本项目的价值 | 不能照搬 |
|---|---|---|---|
| 剧本分析 / coverage 平台 | StoryFit、Largo.ai、ScriptBook、Cinelytic/Callaia、Prescene、OnDesk、ScriptReader.ai、The Black List、Slated、Filmustage | 可解释评分、场景引用、市场/制作分离、行业报告结构 | 长片票房预测、Hollywood 稀缺推荐逻辑、黑盒成功概率 |
| 中文短剧诊断/改稿工具 | 剧拆拆、创一AI/咔咔猩 | 短剧原生维度：钩子、节奏、卖点、爽点、商业潜力、合规 | 未公开 rubric 的“AI评估”宣传 |
| 中文短剧生产平台 | 剧火AI、知剧AI、剧大虾、小镜故事板、LibTV、Coze、Pippit、小云雀、纳逗Pro、万兴剧厂 | 小说/剧本到分集、分镜、资产、提示词、视频任务的链路 | “一句话成片”“1人1天30集”等营销口径 |
| 开源 AI 短剧生产链 | Jellyfish、Toonflow、LocalMiniDrama、Huobao Drama、BigBanana、CineGen、LingGuo、AIYOU、ZJT、ai_story | 结构化 schema、证据片段、实体库、分镜、资产一致性、视频任务 | 普通成片工作台、UI 壳、无 license 代码直接复用 |
| 写作 skill / prompt / 数据集 | 0xsline/short-drama、chengbenchao/short-drama-script、YvonneMovingon/short-drama-skills、llm-script-factory、SkyScript-100M、ScreenJSON、Fountain | 候选 rubric、hook 类型、爽点矩阵、反派层级、结构化导入导出 | 把经验比例当真理；不经自有语料校准就固定权重 |
| 2024-2026 海外市场趋势 | ReelShort、DramaBox、ShortMax、GoodShort、FlexTV、MoboReels、DreameShort、PineDrama、Peacock/ReelShort | 时效判断：IAP+IAA、程序化广告、多渠道分发、本地化、专业化制作 | 早期中国小程序短剧逻辑直接平移 |

最重要的判断：

1. 市面上没有一个公开成熟平台同时解决“旧剧本强机制分析 -> 深度重构 -> 新剧本生产 -> AI 视频交付”。
2. 别人强在局部：coverage 平台会分析，生产平台会拆分镜，开源项目会做资产/任务流，但它们普遍缺“旧稿强机制证据化抽取”和“带约束的深度重构”。
3. 本项目的核心壁垒应该放在：机制抽取、证据引用、强点保留、表皮替换、重构约束、质量回归、生产字段继承。
4. 分析模块不能只是评分器。它必须把旧剧本拆成可重构资产和可生产资产。
5. 外部规则只能进入 `source_hypothesis`，必须经过用户自有剧本和结果标签校准后，才能进入正式权重。

## 1. 这次多 agent 调研如何校验

这次并行拆成六个方向：

1. 成熟商业剧本分析、coverage、影视决策平台。
2. 国内/中文 AI 短剧平台、小说改编、分镜和成片工具。
3. GitHub / 开源 AI 短剧生产链项目。
4. GitHub / 开源短剧写作 skill、prompt、schema、数据集。
5. 2024-2026 海外真人短剧市场、平台和商业化趋势。
6. 钩子、短剧叙事、观众留存、剧本质量评价标准。

主线程对结果做了三类处理：

| 处理 | 标准 |
|---|---|
| 采纳 | 官网、文档、代码、README、公开报告能互相印证，且能直接转成产品字段或判断标准 |
| 降权 | 只有媒体报道、宣传话术、第三方介绍，或与海外真人短剧目标不完全匹配 |
| 暂不使用 | 找不到官网/文档/代码证据，或只是下载站、课程索引、纯营销页 |

证据等级：

| 等级 | 含义 |
|---|---|
| High | 官网、官方文档、GitHub 代码/README、公开产品说明可复核 |
| Medium | 媒体报道、访谈、案例页、第三方报告可支撑，但缺完整 rubric/schema |
| Low | 第三方软文、产品宣传、无法复核数据 |
| Unknown | 未找到足够证据 |

## 2. 之前材料还能不能用

能用，但用途变了。

之前材料的正确位置：

| 旧材料类型 | 是否还能用 | 新用途 |
|---|---|---|
| StoryFit / Largo / ScriptBook 等海外分析平台 | 能用 | 学习如何结构化剧本、角色、情绪、受众、comps、版本比较 |
| Slated / Black List / Coverfly | 部分可用 | 学习多维评分、读者主观性、推荐等级、证据支撑 |
| Prescene / OnDesk / Callaia / ScriptReader.ai | 能用 | 学习 AI coverage、scene-level 证据引用、续看欲评分 |
| Filmustage | 高价值 | 学习生产拆解：角色、地点、道具、服装、VFX、预算、排期 |
| 早期 GitHub parser / schema | 能用 | 导入/导出和 source map，不用于短剧质量判断 |
| 之前“没有完整替代品”的判断 | 仍成立 | 但要补一句：生产链平台很多，只是不解决本项目核心问题 |

之前材料不能继续这样用：

1. 不能把海外长片/剧集评分标准直接当短剧爆款标准。
2. 不能把 coverage 平台当成生产工具。
3. 不能把“好剧本”缩成文学分。
4. 不能在缺少自有样本校准时做“爆款概率预测”。

## 3. 商业剧本分析 / coverage / 决策平台

这些平台强在分析、筛选、行业沟通，不强在短剧重构生产。

| 平台 | 功能链路 | 输出维度 | 生成剧本 | 生产拆解 | 借鉴点 | 风险 |
|---|---|---|---|---|---|---|
| StoryFit | 上传剧本，分析故事、角色、受众、comps、版本 | 角色网络、情绪强度、主题、受众 affinity、viewership potential | 不主打 | 弱 | 角色中心性、情绪曲线、版本对比 | 受众预测黑盒，非短剧原生 |
| Largo.ai | 上传 script/video/brief，做内容洞察和受众模拟 | genre/emotion DNA、角色、关系、受众、comps、预测 | 不主打 | 弱 | emotion arc、audience simulation、market fit | 长片/流媒体预测不能直接套 |
| ScriptBook | 上传标准英文 screenplay，生成 360 分析 | story DNA、受众、分级、comps、财务/地区预测 | 不主打 | 弱 | feature vector、结构化 story DNA | 英文长片格式、票房预测不适合短剧 |
| Cinelytic / Callaia | script coverage + 预算/发行/ROI/人才分析 | premise、originality、dialogue、structure、logic、character、conflict、pacing | 不主打 | 中 | coverage + 商业决策一体化 | Hollywood 项目逻辑 |
| Vault AI | 内容/故事 DNA + 消费者洞察 | audience demand、affinity、emotional response、角色洞察 | 不主打 | 弱 | 角色驱动受众情绪 | 模型不可审计 |
| Filmustage | 上传剧本，自动 breakdown | 场景、人物、道具、地点、服装、VFX、排期、预算 | 不主打 | 强 | 生产可行性、预算/排期风险 | 不解决故事好坏 |
| Slated | 完成长片剧本分析和融资沟通 | Script Score、Project Score、财务预测 | 不主打 | 弱 | 文本分 / 项目分 / 财务分分离 | 长片投资逻辑 |
| The Black List | 职业读者评价和行业曝光 | overall、premise、plot、character、dialogue、setting | 不生成 | 无 | overall 不等于平均分、主观性显式化 | 稀缺推荐平台逻辑 |
| Prescene | AI coverage + script chat | coverage、角色拆解、market-ready scorecard、场景引用 | 不主打 | 中 | 结论绑定场景引用 | AI coverage 质量要人工校验 |
| OnDesk | 面向 studio/agency 的 AI coverage | plot、character、dialogue、pacing、marketability | 不生成 | 弱 | IP 安全、不训练、先筛后深读 | 案例自证 |
| ScriptReader.ai | AI coverage + scene continuation score | concept、plot、structure、dialogue、engagement、pacing、逐场续看欲 | 不主打 | 弱 | 每场“想不想继续看”评分 | 样例质量需复核 |
| ScriptSense / Jumpcut | IP 库 + coverage + chat + mandate 匹配 | coverage、draft comparison、notes、budget top sheets、角色/mandate 检索 | 不主打 | 中 | 甲方需求匹配、旧资产检索 | 非短剧专用 |

来源：

- StoryFit: https://storyfit.com/
- StoryFit ScriptCheck: https://storyfit.com/scriptcheck-supercharges-your-script-process/
- Largo.ai: https://home.largo.io/largo-content-insights/
- ScriptBook: https://www.scriptbook.io/scriptbook
- Cinelytic: https://www.cinelytic.com/
- Callaia: https://www.callaia.ai/
- Vault AI: https://vault-ai.com/
- Filmustage: https://filmustage.com/script-breakdown/
- Slated: https://get.slated.com/analysis/
- The Black List help: https://help.blcklst.com/
- Prescene: https://www.prescene.ai/
- OnDesk: https://www.itsondesk.com/
- ScriptReader.ai: https://scriptreader.ai/
- ScriptSense: https://scriptsense.app/

对本项目的吸收方式：

```yaml
AnalysisReport:
  script_summary:
  logline:
  genre_tags:
  audience_fit:
  comparable_titles:
  episode_map:
  character_network:
  emotional_curve:
  scene_level_continuation_score:
  evidence_backed_findings:
  market_fit:
  production_fit:
  rewrite_orders:
```

不能吸收：

- 长片票房/财务预测。
- “AI 成功概率”宣传。
- Hollywood 标准格式假设。
- 单一总分决定生死。

## 4. 中文短剧平台与工具

中文短剧工具更接近短剧生产现实，但它们多数不是海外真人短剧专用。

### 4.1 诊断 / 改稿工具

| 平台 | 链路 | 输入 | 输出 | 评价维度 | 证据强度 | 可借鉴 |
|---|---|---|---|---|---|---|
| 剧拆拆 | 剧本/视频 -> 10 维诊断 -> 单集桥段 -> 改稿建议 | docx、txt、粘贴、mp4 | 每集问题清单、改稿建议、桥段拆解、视频转剧本 | 事件、情绪、台词、节奏、结构、逻辑、氛围、卖点、格式、合规 | High | 短剧诊断维度、每集问题清单、改稿建议 |
| 创一AI / 咔咔猩 | 剧本上传 -> 评估/优化 -> 爆款对标 -> 生成/分镜/API | 剧本、小说、视频、灵感 | 商业潜力评级、完整剧本、分镜、视频 | 爽点密度、角色吸引力、连贯性、悬念有效性、节奏、市场契合、钩子牵引 | Medium/High | B2B 剧本医生、合规审查、市场潜力 |

来源：

- 剧拆拆: https://www.juchaichai.com/
- 创一AI/咔咔猩相关报道: https://www.sohu.com/a/980193435_116132
- 咔咔猩 API 报道: https://ex.chinadaily.com.cn/exchange/partners/114/rss/channel/cn/columns/07pz5d/stories/WS6a30f924a310d709c2fb861e.html

判断：

1. 剧拆拆的 10 维诊断最接近我们要的“短剧分析模块”。
2. 创一/咔咔猩的“商业潜力”值得参考，但公开 rubric 不足，不能照搬。
3. 这类工具证明“钩子、节奏、卖点、平台适配、合规”必须是一等字段。

### 4.2 小说/剧本到分集/分镜工具

| 平台 | 链路 | 输出物 | 可借鉴 | 限制 |
|---|---|---|---|---|
| 知剧AI | 创意/小说 -> 分集大纲 -> 角色/关系图谱 -> 台本 -> 分镜 -> Word | 大纲、角色、台本、分镜、封面 | 角色关系图谱、分集/台本导出 | 不见强商业评价 |
| 小镜故事板 | 故事 -> 结构分析 -> 镜头预估 -> 分镜脚本 -> 资产库 -> 生图/视频提示词 | 镜号、画面、时长、运镜、资产库、PDF/Excel | 故事到分镜桥接、资产库、镜头数量/节奏密度 | 不直接生成完整剧本 |
| StoryPlay | 灵感/题材 -> 剧本策划 -> 初稿/润色 -> 分镜 -> 剧本转视频 | 策划、剧本、分镜、多模态内容 | 短剧模型和多模态链路 | 官网细节不足 |

来源：

- 知剧AI: https://www.zhijuu.com/
- 小镜故事板: https://xjstoryboard.com/
- StoryPlay: https://storyplay.cn/

判断：

这些平台提醒我们，分析模块输出不能停在“故事评价”。它要给后续分镜和视频端准备这些资产：

```yaml
ProductionReadableScript:
  episode:
  scene:
  beat:
  hook:
  conflict:
  characters:
  location:
  props:
  visible_action:
  dialogue:
  emotion:
  shot_candidate:
  image_prompt_seed:
  video_prompt_seed:
```

### 4.3 文本到视频 / 成片平台

| 平台 | 链路 | 可借鉴 | 风险 |
|---|---|---|---|
| 剧火AI | 想法/小说/剧本 -> AI 编剧 -> 角色/场景 -> 分镜 -> Seedance 2.0 -> 配音配乐 -> 竖屏成片 | 全链路项目化、Seedance 提示词、AI 仿真人剧约束 | 成片质量和效率宣传需打折 |
| 剧大虾 | 主题/剧本 -> 角色/场景/道具 -> 分镜 -> AI 漫剧/视频 -> 协作 | 素材库、角色/场景/道具连续性 | 不主打深度剧本诊断 |
| LibTV | Agent/画布 -> 脚本/角色/图生视频/音频生视频 -> 故事板/视频 | Agent 可调用视频能力、画布工作流 | 官网信息较少，短剧质量维度弱 |
| Coze / 扣子 | Agent -> 剧本/分镜/视频/剪映工程 | 可复用工作流、Seedance、剪映工程导出 | 具体 agent 质量参差 |
| Pippit / 小云雀 | 剧本/小说 -> 角色生命周期 -> 场景/分镜 -> Seedance -> 短剧成片 | dramatic pacing、cliffhanger、角色生命周期 | “全球首个”等宣传需降权 |
| 纳逗Pro | IP/脚本/素材 -> 编剧/导演/美术/摄录/剪辑/宣发 agent -> 成片 | 专业影视链路、IP/资产/商用授权 | 不专注短剧爽点 |
| 万兴剧厂 / Vidu | 小说 IP -> 剧本拆解 -> 资产提取 -> 分镜 -> 视频/配音/音效/口型 -> 后剪辑 | 漫剧/真人剧工作流、资产批量提取 | 更偏生产，不解决爆款判断 |

来源：

- 剧火AI: https://juhuo.cn/
- 剧大虾: https://www.judaxia.art/
- LibTV: https://www.liblib.tv/
- LibTV skills: https://github.com/libtv-labs/libtv-skills
- Coze 视频制作文档: https://docs.coze.cn/cozespace_video
- Pippit AI Drama: https://www.pippit.ai/create/short-dramas
- 纳逗Pro: https://nadoupro.iqiyi.com/
- 万兴剧厂: https://www.reelmate.cn/

关键判断：

1. 这类平台证明市场已经从“AI 写剧本”转向“AI 短剧生产工作流”。
2. 它们强在角色/场景/道具/分镜/视频，不强在判断旧剧本强机制。
3. 如果我们只做一个“一句话成片 UI”，没有差异化。
4. 我们应把它们当下游接口参考，而不是上游分析标准。

## 5. GitHub / 开源 AI 短剧生产链

### 5.1 最值得拆 schema 的项目

| 项目 | stars / license / 活跃度 | 真实度 | 主要链路 | 最值得借的字段 |
|---|---|---|---|---|
| Forget-C/Jellyfish | 4633 / Apache-2.0 / 2026 活跃 | 真开源 | script -> entity -> shot -> frame prompt -> video task | EvidenceSpan、EntityEntry、弱 ID、实体合并、shot division、相邻镜头承接、screen direction、composition anchor |
| HBAI-Ltd/Toonflow-app | 10584 / Apache-2.0 / 2026 活跃 | 真开源 | 小说/剧本 -> 资产抽取 -> 分镜表 -> 分镜图 -> 视频 prompt | o_script、o_assets、o_storyboard、o_videoTrack、资产-分镜关联、导演规划、连贯性自检 |
| xuanyustudio/LocalMiniDrama | 733 / MIT / 2026 活跃 | 真开源 | story -> storyboard -> video，本地数据和异步任务 | storyboard segments、model map、angle_h/v/s、frame_prompts、async_tasks |
| chatfire-AI/huobao-drama | 12990 / 无 license / 2026 活跃 | 有真实代码 | idea/script -> drama -> episode -> characters/scenes/storyboard/video | dramas、episodes、characters、scenes、storyboards、shot_type、angle、movement、prompt、first/last frame |

来源：

- Jellyfish: https://github.com/Forget-C/Jellyfish
- Toonflow: https://github.com/HBAI-Ltd/Toonflow-app
- LocalMiniDrama: https://github.com/xuanyustudio/LocalMiniDrama
- Huobao Drama: https://github.com/chatfire-AI/huobao-drama

这些项目对分析模块的启发：

```yaml
EvidenceSpan:
  source_id:
  episode_no:
  scene_no:
  line_start:
  line_end:
  excerpt:
  confidence:

EntityEntry:
  weak_entity_key:
  normalized_name:
  aliases:
  entity_type:
  first_appearance:
  appearances:
  evidence_spans:

MechanismEvidence:
  mechanism_type:
  evidence_spans:
  involved_entities:
  strength:
  confidence:
  validation_status:
```

这些项目对生产模块的启发：

```yaml
ProductionChain:
  episode:
    scenes:
      beats:
        shots:
          source_excerpt:
          location:
          time:
          characters:
          props:
          action:
          result:
          dialogue:
          narration:
          atmosphere:
          shot_type:
          angle_h:
          angle_v:
          angle_s:
          movement:
          duration:
          image_prompt:
          video_prompt:
          first_frame_image:
          last_frame_image:
          reference_images:
          continuity_from_prev:
          continuity_to_next:
          screen_direction:
          composition_anchor:
          model_profile:
          retry_guidance:
          qc_flags:
```

### 5.2 生产流程可参考，但不宜作为主架构

| 项目 | 判断 |
|---|---|
| LingGuoAI/LingGuo-Drama | 有真实 CRUD/job/video adapter，字段完整，但 license 缺失，偏常规生产流 |
| xhongc/ai_story | 有阶段 processor、prompt 管理、rewrite 节点，安装复杂，机制分析浅 |
| yubowen123/AIYOU | 节点类型设计可参考：DRAMA_ANALYZER、SCRIPT_PLANNER、STORYBOARD_SPLITTER、CHARACTER_NODE |
| jeffstric/ZJT | 多 agent、角色/地点/道具、first/last frame、多参考图视频模式值得看 |

来源：

- LingGuo Drama: https://github.com/LingGuoAI/LingGuo-Drama
- ai_story: https://github.com/xhongc/ai_story
- AIYOU: https://github.com/yubowen123/AIYOU_open-ai-video-drama-generator
- ZJT: https://github.com/jeffstric/ZJT

### 5.3 概念可参考，但不能当主依据

| 项目 | 判断 |
|---|---|
| BigBanana-AI-Director | 产品概念强，Script-to-Asset-to-Keyframe 术语有用；但公开仓库后续主要是 Docker/文档，不是持续源码开源；CC BY-NC-SA，商用谨慎 |
| CineGen-ShortDrama | 小型 React/Gemini 原型，可参考极简 types，不是完整系统 |
| Open-AI-Micro-Drama-Generator | README 口号大于实现，适合看最小接口 |
| YubAI-DramaFlow | docs/templates/examples，适合方法论，不是应用代码 |
| Z5 ai-drama-platform | Next/Prisma 原型，Panel 字段可参考，成熟度一般 |

来源：

- BigBanana: https://github.com/shuyu-labs/BigBanana-AI-Director
- CineGen: https://github.com/UllrAI/CineGen-ShortDrama
- Open-AI-Micro-Drama-Generator: https://github.com/Anil-matcha/Open-AI-Micro-Drama-Generator
- YubAI-DramaFlow: https://github.com/xiaoqinyudan2022-hue/YubAI-DramaFlow
- Z5 ai-drama-platform: https://github.com/Z5Research/ai-drama-platform

## 6. GitHub / 开源写作 skill、schema、数据集

这些项目不能当标准答案，但能提供候选维度。

| 项目 | 可复用 | 需要警惕 |
|---|---|---|
| 0xsline/short-drama | genre、opening、hook、paywall、rhythm、satisfaction、villain、compliance；5 类钩子、爽点矩阵、四层反派 | 比例和权重模板化，需语料验证 |
| chengbenchao/short-drama-script | 1+3+N 角色矩阵、四级卡点、一句话故事、核心冲突、爽点清单、3-5-3 结构 | 标杆剧本库版权/题材/海外适配需审 |
| 021gink/short-drama-ai-skills | Updream/Seedance/可灵/Pika 提示词、分镜、角色、场景、审核筛查 | 视频 prompt，不是剧本评价 |
| YvonneMovingon/short-drama-skills | 剧本到镜头序列；信息密度、无新信息不切镜、台词超 8 秒强拆、单镜不超 12 秒 | 分镜/视频规则，不直接判断好剧本 |
| SumOneHK/short-drama-scriptwriter | 阶段门禁、项目状态、独立质检、海外市场与平台分离、本地化贯穿 | 明确不适用于真人拍摄短剧，内容边界不能照搬 |
| hermes-skill-short-drama-master | 多维会审、质量关卡、提交前预审、角色锁定、废片率控制 | 效率/废片率指标是自称 |
| llm-script-factory | 6 阶段工作站：创意、结构、分场、正文、润色、剧本医生；本地 JSON 存档 | DTG 理论需要验证 |
| SkyScript-100M | 短剧 script / shooting script 数据集，适合学习 script -> shooting script | 不能代表海外真人短剧市场趋势 |
| Fountain / screenplay-tools / ScreenJSON | 导入、导出、结构化剧本中间格式 | 不含短剧专属字段 |

来源：

- 0xsline/short-drama: https://github.com/0xsline/short-drama
- chengbenchao/short-drama-script: https://github.com/chengbenchao/short-drama-script
- 021gink/short-drama-ai-skills: https://github.com/021gink/short-drama-ai-skills
- YvonneMovingon/short-drama-skills: https://github.com/YvonneMovingon/short-drama-skills
- SumOneHK/short-drama-scriptwriter: https://github.com/SumOneHK/short-drama-scriptwriter
- hermes-skill-short-drama-master: https://github.com/woqianfu/hermes-skill-short-drama-master
- llm-script-factory: https://github.com/oidahdsah0/llm-script-factory
- SkyScript-100M: https://github.com/vaew/SkyScript-100M
- screenplay-tools: https://github.com/wildwinter/screenplay-tools
- ScreenJSON: https://screenjson.com/

建议扩展短剧 schema：

```yaml
ShortDramaScriptJSON:
  metadata:
    target_market:
    production_mode:
    source_rating:
    source_hypothesis:
    corpus_validation_status:
  episodes:
    - episode_no:
      duration_target:
      opening_hook:
      micro_goal:
      obstacle:
      stakes:
      protagonist_choice:
      reversal:
      payoff:
      relationship_delta:
      cliffhanger:
      paywall_or_ad_trigger:
      production_risk:
      ai_video_fit:
      evidence_spans:
  entities:
    characters:
    relationships:
    locations:
    props:
  mechanisms:
    hook_types:
    satisfaction_types:
    conflict_types:
    power_shift_chain:
    information_gap_chain:
```

## 7. 2024-2026 海外真人短剧市场时效判断

这部分直接影响分析权重。

### 7.1 关键变化

| 趋势 | 对剧本 Agent 的影响 |
|---|---|
| 市场从 2024 爆发进入 2025-2026 高供给竞争 | 不能只问“题材热不热”，要问“能不能低成本快速测试、剪出投流素材、前几集留人” |
| 美国仍是收入锚点，下载增长在东南亚、拉美、印度 | 目标市场要参数化，不能默认单一美国女性用户 |
| 商业化从 IAP 扩到 IAP + IAA + 订阅 + 程序化广告 | 付费点、广告解锁点、订阅诱因都要标注 |
| 分发从独立 App 外溢到 TikTok、Peacock、Google TV、传统流媒体 | 剧本要同时适配 App 内付费和外部平台投放/预告 |
| 题材从 romance/billionaire/werewolf/mafia/revenge 扩到家庭、悬疑、恐怖、动画、男性向 | tag 体系不能只有旧套路，要支持新题材变量 |
| 真人制作专业化，但仍要低成本高速 | 分析模块必须输出预算/场景/演员/动作/亲密/暴力风险 |
| AI 短剧/漫剧增长快，但真人情绪表演仍有优势 | AI 适配不是“全 AI 替代”，而是分镜、预演、多版本广告、低成本测试 |
| 暴力、厌女、虐女桥段开始有反噬 | 不能把“刺激”当唯一目标，要有品牌安全和平台风险 |

来源：

- Sensor Tower 2025 short drama apps: https://sensortower.com/blog/state-of-short-drama-apps-2025
- Sensor Tower 2026 short drama apps: https://sensortower.com/report/state-of-short-drama-apps-2026
- adjoe short drama apps rewarded engagement: https://adjoe.io/blog/short-drama-apps-rewarded-engagement/
- Business Insider micro dramas revenue / ReelShort / DramaBox: https://www.businessinsider.com/micro-dramas-reelshort-dramabox-billion-dollar-business-in-us-2025-9
- DramaBox / The Trade Desk partnership: https://www.prnewswire.com/news-releases/the-trade-desk-powers-open-internet-growth-with-dramabox-short-drama-partnership-302752834.html
- Peacock / ReelShort: https://www.businessinsider.com/peacock-reelshort-micro-dramas-bravo-hollywood-short-form-vertical-video-2026-5
- SAG-AFTRA verticals agreement: https://www.sagaftra.org/turning-industry-its-side-sag-aftra-goes-vertical-new-agreement
- WIRED on ReelShort localization: https://www.wired.com/story/china-reel-short-dramas-video-social-media

### 7.2 哪些旧经验还可用

仍可用：

1. 前几集免费，关键 cliffhanger 诱发付费/广告解锁。
2. 强类型、强情绪、强反转。
3. 复仇、逆袭、豪门、婚恋、身份差、羞辱-反击等底层爽感。
4. 数据驱动迭代。
5. 低成本、快生产、快投放、快复制。

可能过时：

1. 直译中文网文/小程序爽点。
2. 单纯靠虐女、扇耳光、怀孕受辱拉留存。
3. 只做 IAP 付费墙，不考虑广告解锁和订阅。
4. 只盯美国白人中年女性。
5. “拍得糙才像短剧”。

## 8. 好钩子 / 差钩子标准

好钩子不是刺激越大越好，而是：

> 3-6 秒内让观众明确：谁被逼到什么位置，马上会失去什么，我缺哪条关键信息，下一秒为什么必须看。

### 8.1 Hook Rubric

总分 30，第一集开场、每集开头、集尾 cliffhanger 都可用。

| 维度 | 分值 | 好钩子 | 差钩子 |
|---|---:|---|---|
| 即时清晰度 | 0-5 | 3-6 秒内出现人物、冲突、处境，不靠旁白铺世界观 | 天气、背景、人物履历、空镜、慢慢进入 |
| 情绪爆点 | 0-5 | 羞辱、背叛、危险、欲望、禁忌、身份压迫至少一个立刻可感 | 有点怪但不痛不痒 |
| 信息差 / 好奇缺口 | 0-5 | 观众知道一部分，但缺关键答案 | 什么都藏，观众不知道该好奇什么 |
| Stakes | 0-5 | 失败代价具体：孩子、身份、婚姻、家族、生命、名誉、控制权 | 只有“很麻烦”“很危险” |
| 关系/权力变化 | 0-5 | 两人关系发生可见位移：弱到强、爱到恨、控制到反控 | 只有事件，没有关系位移 |
| 可兑现性 | 0-5 | 下一场/下一集能兑现或升级，不骗点击 | 下集秒解、无代价解除、谜底无关主线 |

来源：

- TikTok creative best practices: https://ads.tiktok.com/help/article/creative-best-practices
- Shore Scripts coverage categories: https://www.shorescripts.com/screenplay-coverage/
- Black List evaluation dimensions: https://blcklst.substack.com/p/how-consistent-are-black-list-evaluations
- TV Calling coverage guide: https://www.tv-calling.com/script-coverage-a-brief-reference-guide/
- Script Reader Pro scene choice: https://www.scriptreaderpro.com/screenplay-scene/

### 8.2 三个位置的钩子

| 位置 | 标准 |
|---|---|
| 第一集开场 | 类型承诺 + 主角处境 + 核心不公/欲望 + 一个未解问题 |
| 每集开头 | 不能只接上一集台词，要重新给微冲突：逼问、证据、误读、亲密打断、目标受阻 |
| 集尾 cliffhanger | 卡在选择前一秒、真相揭开前一秒、反击刚开始、代价刚显形 |

好 cliffhanger 的一句话测试：

```text
观众能不能说出：我想知道 X 会不会发生？
```

如果不能，说明钩子是空的。

## 9. 好剧本 / 差剧本标准

好剧本不是“每集都有反转”，而是：

> 每集都有可追踪的欲望、阻力、选择、代价、关系变化和兑现。

### 9.1 100 分 rubric

| 模块 | 分值 | 好剧本标准 | 差剧本信号 |
|---|---:|---|---|
| Premise / 类型承诺 | 12 | 一句话说清类型、欲望、反差、卖点 | 设定很多，没有可卖 logline |
| 剧集引擎 | 16 | 每集有目标、阻力、反转、未解问题 | 事件流水账，无因果推进 |
| 人物关系引擎 | 16 | 主角、对手、stakes person 形成三角拉扯，关系每 1-3 集变化 | 角色只服务情节，关系不变 |
| 留存结构 | 18 | 开头 hook、中段升级、结尾卡点 | 单集像传统长剧过场，结尾自然结束 |
| 爽点/虐点/反转/Payoff | 16 | 受辱-压迫-选择-反击-兑现闭环清楚 | 只堆巴掌、下跪、吼叫，无铺垫无代价 |
| 台词与场景经济 | 10 | 台词揭示人物、推进冲突、暴露信息差 | 解释性对白、寒暄、人物声口一样 |
| 真人/AI 生产可行性 | 12 | 9:16、近景脸部、少场景、少角色、动作清楚，可拆镜头 | 大场面、多人混战、抽象心理戏、无法视觉化 |

分数解释：

| 分数 | 结论 |
|---:|---|
| 90+ | 可进入投放素材拆条和分镜生产 |
| 80-89 | 可重构后进入分镜/生产 |
| 70-79 | 有强点，但需要结构性重构 |
| 60-69 | 局部桥段可复用，整剧不适合直接开发 |
| <60 | 只保留少量素材或设定，不能作为强机制样本 |

### 9.2 Agent 可检测信号

| 信号 | 字段 | 说明 |
|---|---|---|
| 文本证据 | `evidence_spans` | 每个判断必须引用原文，不能只说“感觉弱” |
| 结构证据 | `episode_start / mid_turn / episode_end / scene_count` | 开头无冲突、结尾无未解问题直接扣留存 |
| 情绪曲线 | `humiliation / fear / desire / relief / revenge / romance / tension` | 平线差；一直高强度但无释放也差 |
| 信息差 | `audience_knows / character_knows / hidden_truth / reveal_timing` | 必须具体，不标空泛“有悬念” |
| Stakes | `loss_if_fail / deadline / consequence` | 代价越具体越高 |
| Choice | `options / tradeoff / chosen_action` | 主角必须面对真选择 |
| Reversal | `before_state / trigger / after_state` | 反转必须改变权力、目标、关系或信息 |
| Payoff | `setup_episode / payoff_episode / emotional_release` | 只埋不还损伤信任，只还不升级断追看 |
| 关系变化 | `relation_before / relation_after / power_delta / trust_delta / desire_delta` | 强短剧靠关系电压，不靠事件数量 |
| AI 可拍性 | `visible_action / camera / lighting / location / cast_count` | 抽象心理戏要改成可见动作 |

## 10. 爆款代理指标

用户定义的爆款是结果集合：甲方愿意买，导演/监制觉得能拍，适合 AI 视频生产，投流 ROI 好，完播/追更/付费/广告表现好，最终流量高、赚钱多。

V1 不能直接预测这个结果，只能做代理指标。

建议把当前 spec 的 `HitPotentialProxy` 扩成：

```yaml
HitPotentialProxy:
  traffic_hook:
    score:
    evidence:
    can_cut_5_ad_hooks:
  episode_retention:
    score:
    key_drop_risks:
    episode_nodes:
  monetization_fit:
    score:
    iap_nodes:
    ad_unlock_nodes:
    subscription_trigger:
  market_trope_fit:
    score:
    tags:
    fresh_variation:
  localization_fit:
    score:
    target_market:
    cultural_friction:
  narrative_mechanism_strength:
    score:
    strong_mechanisms:
    weak_mechanisms:
  relationship_engine:
    score:
    power_map:
    pressure_chain:
    emotional_debt:
  production_feasibility:
    score:
    budget_risks:
    cast_location_props:
  ai_video_fit:
    score:
    visualizable_actions:
    difficult_shots:
  compliance_brand_safety:
    score:
    platform_risks:
    advertiser_risks:
```

## 11. 分析模块应该增强成什么

### 11.1 当前最小可用分析链

```text
Script Intake
-> Format Normalize
-> Episode / Scene / Beat Map
-> Evidence Span Index
-> Entity & Relationship Graph
-> Hook / Goal / Obstacle / Stakes / Choice / Reversal / Payoff Extraction
-> Power Mechanism Map
-> Retention / Monetization / Market / Production Scorecard
-> Strong Mechanism Inventory
-> Surface Element Inventory
-> Rewrite Orders
-> Production Handoff Fields
```

### 11.2 每集必须抽取的字段

```yaml
EpisodeAnalysis:
  episode_no:
  summary:
  opening_hook:
    hook_type:
    hook_question:
    first_3s_visual:
    score:
    evidence_spans:
  micro_goal:
  obstacle:
  stakes:
  protagonist_choice:
    options:
    tradeoff:
    chosen_action:
  reversal:
    before_state:
    trigger:
    after_state:
  payoff:
    setup:
    release:
    remaining_debt:
  relationship_delta:
    relation_before:
    relation_after:
    power_delta:
    trust_delta:
    desire_delta:
  cliffhanger:
    type:
    question:
    next_episode_expected_answer:
    score:
  monetization_node:
    iap_fit:
    ad_unlock_fit:
    subscription_fit:
  production_fit:
    location_count:
    cast_count:
    props:
    difficult_actions:
    ai_video_risks:
  evidence_spans:
```

### 11.3 全剧必须抽取的字段

```yaml
ScriptMechanismMap:
  premise:
  genre_tags:
  market_tags:
  protagonist_engine:
  antagonist_pressure:
  relationship_engine:
  power_shift_chain:
  information_gap_chain:
  payoff_chain:
  retention_chain:
  monetization_chain:
  trope_variations:
  localization_risks:
  production_risks:
  ai_video_fit:
  compliance_risks:
  strong_mechanisms:
  weak_mechanisms:
  surface_elements:
  replaceable_elements:
  non_negotiable_mechanisms:
```

## 12. 重构模块应该如何承接分析

深度重构不是“洗稿改名”，而是保留机制、替换表皮、重造表达。

### 12.1 旧稿拆成三类资产

| 类型 | 含义 | 处理方式 |
|---|---|---|
| Narrative Spine | 状态变化、因果链、危机链 | 可以保留抽象脉络，但不能照搬具体表达 |
| Power Mechanisms | 钩子、爽点、反转、关系压力、信息差、付费点 | 必须保留强度，允许换题材/身份/场景/事件 |
| Surface Elements | 角色名字、职业、地点、具体桥段、台词、场面包装 | 默认可替换 |

### 12.2 重构 brief 必须有深度参数

```yaml
TransformationBrief:
  target_market:
  target_platform:
  target_episode_count:
  production_mode:
  transformation_depth:
    level: L1 | L2 | L3 | L4
    preserve:
      - mechanism
      - relationship_shape
      - retention_chain
    replace:
      - setting
      - character_identity
      - scene_packaging
      - dialogue
  client_requirements:
  forbidden_elements:
  desired_tropes:
  production_constraints:
```

### 12.3 重构质量回归

新稿生成后必须反扫：

1. 旧稿强机制是否还在。
2. 钩子强度是否下降。
3. 爽点是否变少或提前泄掉。
4. 关系压力是否变平。
5. 主角是否失去主动选择。
6. 反转是否只改信息、不改局面。
7. 付费/广告节点是否变弱。
8. 海外本地化是否可信。
9. AI 视频成本是否上升。
10. 合规/品牌风险是否增加。

## 13. 不能被外部平台误导的地方

1. 成片平台解决生产链，不等于解决剧本质量。
2. 角色一致性多数指视觉一致，不等于动机、关系和情绪弧一致。
3. “一键成剧”很容易生成漂亮废稿。
4. 爆款套路有用，但不经样本验证会走向同质化。
5. 国内小程序爽点不能直接搬到海外真人短剧。
6. 评分不能黑盒，必须有原文证据。
7. AI 视频可行性不能反过来阉割剧本强机制，但必须提示成本和替代表达。
8. 不要把几颗星的总体评价当成细粒度标签。星级只能帮助排序，不能解释机制。

## 14. 对现有 spec 的修改建议

当前 spec 方向是对的，但需要补三块。

### 14.1 加外部参照分层

在 spec 的外部研究部分增加：

```yaml
ExternalReferenceLayer:
  analysis_coverage:
    role: learn report structure and evidence-backed scoring
    weight: medium
  short_drama_diagnosis:
    role: learn hook, rhythm, sell-point, compliance dimensions
    weight: high
  production_chain:
    role: learn schema and handoff fields
    weight: high
  writing_skills:
    role: hypothesis source only
    weight: medium_low
  market_trends:
    role: recency and target-market weighting
    weight: high
```

### 14.2 加假设/校准状态

每个外部规则都必须带：

```yaml
RuleCard:
  rule_id:
  rule_text:
  source:
  source_type:
  evidence_strength:
  market_scope:
  recency_status:
  source_hypothesis:
  corpus_validation_status: untested | weakly_supported | supported | contradicted | stale
  last_validated_at:
```

### 14.3 加 production handoff schema

分析模块输出不应只给报告，还要给生产端：

```yaml
ProductionHandoff:
  character_bible:
  relationship_map:
  location_table:
  prop_table:
  episode_scene_table:
  beat_table:
  shot_candidate_table:
  prompt_seed_table:
  ai_video_risk_table:
  compliance_table:
```

## 15. 下一步不该做什么

现在不该立刻做：

1. 做完整 UI。
2. 做一键成片。
3. 固定爆款权重。
4. 直接集成某个开源生产工作台。
5. 用外部 skill 规则直接评用户剧本。
6. 大规模写生成模块。

原因很简单：如果分析层没校准，后面的生成只会把错误放大。

## 16. 下一步应该做什么

### 16.1 最小正确动作

用用户自有剧本做一个小型 benchmark：

```text
3 部高星 / 强评价旧剧本
2 部普通或弱评价旧剧本
```

每部跑同一套分析模板：

1. 导入并保留 episode / scene / line source map。
2. 抽取每集 hook、goal、obstacle、stakes、choice、reversal、relationship_delta、cliffhanger、payoff、production_fit。
3. 生成强机制清单。
4. 生成弱点和掉线风险。
5. 和总体星级做对照。
6. 找出“高星剧本共同机制”和“低星剧本缺失机制”。
7. 把外部规则标成 supported / contradicted / untested。

### 16.2 第一版输出模板

```markdown
# Script Analysis Report

## Verdict
总分：
结论：
适合重构深度：

## Evidence-backed Scores
- Hook:
- Retention:
- Payoff:
- Relationship Engine:
- Market Fit:
- Production Fit:
- AI Video Fit:

## Strong Mechanisms To Preserve
1.
2.
3.

## Surface Elements To Replace
1.
2.
3.

## Episode Table
| Ep | Hook | Goal | Stakes | Choice | Reversal | Cliffhanger | Payoff | Risk |

## Rewrite Orders
1.
2.
3.

## Production Handoff
- Characters:
- Locations:
- Props:
- Difficult shots:
- Prompt seeds:
```

### 16.3 第二步才做重构实验

选 1 部强剧本，做一次受控重构：

```text
输入：旧剧本 + 甲方 brief + 重构深度 L3
输出：新设定、新人物关系、新前 5 集大纲、新第 1 集正文
检测：旧强机制是否保留，新稿是否更适合海外真人短剧和 AI 视频生产
```

如果这个小实验都不能保住强点，就不要进入完整 60-90 集生成。

## 17. 最终产品定位

这个项目不应该被定位成普通“AI 短剧生成器”。

更准确的定位是：

> Evidence-backed Short Drama Script Intelligence & Transformation Agent  
> 一个能从自有旧剧本中抽取爆款机制，并把机制重构成新海外真人短剧剧本的生产型 agent。

它要服务四类人/系统：

| 对象 | 需要什么 |
|---|---|
| 甲方 | 这剧为什么能卖，题材/市场/风险是什么 |
| 导演/监制 | 这剧能不能拍，角色/场景/成本/风险是什么 |
| 编剧 | 哪些强点必须保留，哪里必须重写 |
| AI 视频 agent | 角色、场景、分镜、动作、提示词、风险字段 |

真正的核心不是“写得快”，而是：

```text
读得准 -> 拆得细 -> 保得住强点 -> 换得掉表皮 -> 生成后还能反向检测
```

## 18. 附：重点来源索引

商业分析 / coverage：

- https://storyfit.com/
- https://home.largo.io/largo-content-insights/
- https://www.scriptbook.io/scriptbook
- https://www.cinelytic.com/
- https://www.callaia.ai/
- https://filmustage.com/script-breakdown/
- https://get.slated.com/analysis/
- https://www.prescene.ai/
- https://www.itsondesk.com/
- https://scriptreader.ai/
- https://scriptsense.app/

中文短剧平台：

- https://www.juchaichai.com/
- https://juhuo.cn/
- https://www.zhijuu.com/
- https://xjstoryboard.com/
- https://www.judaxia.art/
- https://www.liblib.tv/
- https://docs.coze.cn/cozespace_video
- https://www.pippit.ai/create/short-dramas
- https://nadoupro.iqiyi.com/
- https://www.reelmate.cn/

开源生产链：

- https://github.com/Forget-C/Jellyfish
- https://github.com/HBAI-Ltd/Toonflow-app
- https://github.com/xuanyustudio/LocalMiniDrama
- https://github.com/chatfire-AI/huobao-drama
- https://github.com/shuyu-labs/BigBanana-AI-Director
- https://github.com/UllrAI/CineGen-ShortDrama
- https://github.com/LingGuoAI/LingGuo-Drama
- https://github.com/xhongc/ai_story
- https://github.com/yubowen123/AIYOU_open-ai-video-drama-generator
- https://github.com/jeffstric/ZJT

写作 skill / schema / 数据：

- https://github.com/0xsline/short-drama
- https://github.com/chengbenchao/short-drama-script
- https://github.com/021gink/short-drama-ai-skills
- https://github.com/YvonneMovingon/short-drama-skills
- https://github.com/SumOneHK/short-drama-scriptwriter
- https://github.com/oidahdsah0/llm-script-factory
- https://github.com/vaew/SkyScript-100M
- https://github.com/wildwinter/screenplay-tools
- https://screenjson.com/

海外市场 / 时效：

- https://sensortower.com/blog/state-of-short-drama-apps-2025
- https://sensortower.com/report/state-of-short-drama-apps-2026
- https://adjoe.io/blog/short-drama-apps-rewarded-engagement/
- https://www.businessinsider.com/micro-dramas-reelshort-dramabox-billion-dollar-business-in-us-2025-9
- https://www.prnewswire.com/news-releases/the-trade-desk-powers-open-internet-growth-with-dramabox-short-drama-partnership-302752834.html
- https://www.businessinsider.com/peacock-reelshort-micro-dramas-bravo-hollywood-short-form-vertical-video-2026-5
- https://www.sagaftra.org/turning-industry-its-side-sag-aftra-goes-vertical-new-agreement
- https://www.wired.com/story/china-reel-short-dramas-video-social-media

钩子 / 叙事 / 视频提示词：

- https://ads.tiktok.com/help/article/creative-best-practices
- https://www.shorescripts.com/screenplay-coverage/
- https://blcklst.substack.com/p/how-consistent-are-black-list-evaluations
- https://www.tv-calling.com/script-coverage-a-brief-reference-guide/
- https://www.scriptreaderpro.com/screenplay-scene/
- https://developers.openai.com/api/docs/guides/video-generation
- https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide
- https://deepmind.google/models/veo/prompt-guide/
