# 短剧剧本深度重构与生产 Agent Spec

日期：2026-06-28  
状态：V0.2 目标重对齐版  
前置文档：

- `/Users/jiakun/.gstack/projects/auto-script-agent/jiakun-no-git-design-20260619-022421.md`
- `/Users/jiakun/Codex/自动化编剧/research/short-drama-script-agent-external-research-2026-06-28.md`
- `/Users/jiakun/Codex/自动化编剧/research/short-drama-agent-landscape-2026-06-28.md`

## 0. 这版为什么要重写

原始方向没有变：分析优质短剧剧本，提取可复用爆款规律，最终生成足够优秀的爆款剧本。

这版要重写，不是因为目标变了，而是因为最终产物更明确了：

> 这个工具最终要产出完整剧本；分析环节是为了让生成不凭空、不低级改写、不丢强点。

因此，分析模块不能只回答“这个剧本哪里好”。它必须回答：

1. 这个旧剧本真正强的机制是什么？
2. 哪些强点必须保留？
3. 哪些只是旧稿表皮，必须替换？
4. 如何在新设定、新人物、新关系、新背景里重造同等强度的钩子、爽点、反转和危机链？
5. 新稿是否仍然适合 AI 视频制作、合规、当前市场和甲方要求？

这意味着产品表述从：

```text
Short-Drama Script Pattern Agent
```

扩展为：

```text
Short-Drama Script Transformation Agent
短剧剧本深度重构与生产 Agent
```

但底层目标仍然是：

```text
通过分析自有强剧本，提取可验证的爆款机制，并用这些机制生产新的高质量短剧剧本。
```

## 1. 产品目标

### 1.1 核心目标

输入用户自有旧剧本、甲方要求、目标集数、题材方向、制作约束，系统输出一部新的海外真人短剧开发稿。

这个新稿应该：

- 保留旧剧本经过验证的强叙事机制。
- 不做低级改名、换场景、换台词式改写。
- 重做设定、人物身份、人物关系、冲突容器、钩子表达、爽点包装、反转方式。
- 能给编剧继续改。
- 能给甲方/导演/监制看。
- 能给 AI 视频制作 agent 继续拆分镜、资产和提示词。
- 最终目标是被 AI 生成视频后流量高、赚钱多。

### 1.1.1 爆款的操作化定义

“爆款”在业务上不是单一指标，而是一个结果集合：

- 甲方愿意买。
- 平台或客户愿意继续开发。
- 导演/监制觉得能拍。
- 适合 AI 真人短剧制作。
- 投流 ROI 好。
- 完播、追更、付费或广告留存表现好。
- 最终视频流量高、赚钱多。

V1 不能直接预测全部结果。V1 先把“爆款”拆成可分析的代理指标：

```yaml
HitPotentialProxy:
  buyer_appeal:
  audience_pull:
  hook_strength:
  retention_chain:
  payoff_density:
  protagonist_engine:
  relationship_engine:
  conflict_escalation:
  production_feasibility:
  ai_video_fit:
  market_fit_overseas_live_action:
  compliance_and_platform_risk:
```

这些代理指标不是最终真相。它们用来解释为什么一个剧本可能更强，并在有真实结果数据后回填校准。

### 1.1.2 现有样本标签

当前旧剧本有总体评价，例如几颗星，但没有细到每个环节的标签。

当前这个星级来自导演评价。

因此 V1 把星级作为弱标签：

```yaml
ScriptOutcomeLabel:
  overall_rating:
  rating_source:
  rating_confidence:
  sale_or_usage_status:
  known_feedback:
  missing_granular_labels:
```

规则：

- 星级可以帮助排序强弱样本。
- 导演评价有业务价值，但它不是纯叙事强度标签。
- 星级不能直接解释“为什么强”。
- 分析模块要从高星剧本中提出机制假设，再用弱样本或低星样本做对照。
- 如果一个高星剧本某个维度很弱，说明星级可能来自其他强项，不能强行解释。

### 1.1.3 目标市场

当前默认目标市场：

```yaml
TargetMarket:
  region: overseas
  format: live_action_short_drama
  orientation: vertical_or_mobile_first
  production_mode: AI-assisted live-action style video
```

这会影响分析和生成：

- 钩子必须跨文化易懂。
- 人物关系和冲突要适合海外短剧用户理解。
- 场景、服化道、动作、亲密、暴力、合规要按海外真人短剧和 AI 视频生产评估。
- 不能默认套国内小程序 IAP 付费点逻辑。

### 1.2 一句话定义

> 从自有旧剧本中抽取强机制，再按新需求重构或生成新的、可生产的海外真人短剧剧本。

### 1.3 不是做什么

V1 不做：

- 泛泛的 AI 写剧本。
- 只换名字和背景的浅层改写。
- 无证据的爆款概率预测。
- 完整自动成片。
- 平台推荐算法预测。
- 法律意义上的最终合规审查。
- 不经校准的黑盒评分。

## 2. 使用场景

### 2.1 主场景：自有旧剧本深度重构

用户输入：

- 一部已有短剧剧本。
- 希望保留的强点或参考段落。
- 希望变更的方向：题材、背景、人物身份、关系、风格、集数、平台、目标客户。
- AI 视频制作约束。

系统输出：

1. 旧稿解剖报告。
2. 强机制清单。
3. 表皮替换清单。
4. 新稿重构方案。
5. 新分集大纲。
6. 新剧本初稿。
7. 钩子/爽点/反转/危机链检查。
8. AI 视频适配报告。

### 2.2 次场景：已有剧本诊断与增强

用户输入一个新剧本，系统不重构，只分析：

- 哪里强。
- 哪里弱。
- 哪些钩子不成立。
- 哪些爽点没兑现。
- 哪些集数没有推进。
- 哪些地方不适合 AI 视频制作。
- 怎么改。

### 2.3 后续场景：从需求直接生成

用户输入甲方需求，系统直接生成剧本。但这不是当前优先级。

原因：没有旧稿分析能力和强机制库，直接生成容易变成漂亮废稿。

## 3. 总体链路

```text
旧剧本/参考剧本
-> 导入与结构化
-> 旧稿解剖
-> 强机制识别
-> 表皮/机制分离
-> 新需求解析
-> 重构设计
-> 新钩子/爽点/反转/危机链生成
-> 分集大纲
-> 完整剧本
-> AI 视频制作包
-> 反向检测
```

## 4. 分析模块的新定位

分析模块不是“评分器”，而是生产链路里的拆解引擎。

它要把剧本拆成三种资产：

1. `Narrative Spine`：剧情脉络和状态变化。
2. `Power Mechanisms`：真正让剧本有效的强机制。
3. `Surface Elements`：可以替换的设定、身份、场景、台词、具体事件包装。

### 4.1 分析模块必须支持的问题

对一部旧剧本，系统要能回答：

- 这个剧本为什么能抓人？
- 第一集靠什么把人拉住？
- 每集结尾为什么让人继续看？
- 主角每一阶段的状态怎么变？
- 关系为什么持续有戏？
- 爽点怎么铺、怎么爆？
- 反转在哪里改变局面？
- 危机怎么升级？
- 哪些桥段是强机制，哪些只是旧表皮？
- 哪些机制可以搬到新设定里？
- 哪些机制如果换题材就失效？
- 哪些地方不适合 AI 视频生产？

## 5. 增强后的分析模块

### 5.1 Import And Structure 模块

目的：先把剧本变成可引用、可审计、可重构的结构。

输入格式：

- Markdown
- TXT
- DOCX
- PDF
- Final Draft / FDX
- Fountain
- pasted text
- mixed format

输出字段：

```yaml
ScriptImport:
  script_id:
  title:
  source_path:
  source_type: completed_script | outline | novel | video_transcript | unknown
  format:
  episode_boundaries:
  scene_boundaries:
  line_ranges:
  character_candidates:
  dialogue_blocks:
  action_blocks:
  import_status: imported | needs-cleanup | failed | source-type-mismatch
  import_warnings:
```

规则：

- 没有集数边界，不允许做集尾钩子评价。
- 没有场次/段落边界，可以做粗分析，但 evidence confidence 必须降级。
- 如果输入其实是小说或大纲，不进入“剧本强弱评价”，进入“改编分析”。

### 5.2 Narrative Spine 脉络模块

目的：提取旧稿的主线骨架，不被具体设定干扰。

输出：

```yaml
NarrativeSpine:
  logline:
  premise_promise:
  episode_count:
  main_arc:
  episode_chain:
    - episode:
      starting_state:
      pressure_event:
      protagonist_action:
      relationship_shift:
      reveal_or_reversal:
      payoff:
      ending_question:
      ending_state:
  phase_breaks:
    - phase_name:
      episodes:
      core_function:
```

判断重点：

- 每集是否改变故事状态。
- 每集是否推动人物关系。
- 每集是否制造新压力或兑现旧压力。
- 前 3 集、前 10 集是否有足够强的商业承诺。

### 5.3 Hook System 钩子系统模块

目的：系统化拆解所有钩子，而不是只看“有没有悬念”。

钩子类型：

- opening_hook：开头钩子。
- first_episode_hook：首集主钩子。
- episode_end_hook：集尾钩子。
- crisis_hook：危机钩子。
- identity_hook：身份钩子。
- relationship_hook：关系钩子。
- payoff_hook：爽点承诺钩子。
- paywall_or_retention_hook：付费/留存钩子。

输出：

```yaml
HookAnalysis:
  hook_id:
  episode:
  scene:
  hook_type:
  hook_position:
  hook_trigger:
  unanswered_question:
  emotional_charge:
  protagonist_stakes:
  audience_promise:
  payoff_expected_by:
  actual_payoff_episode:
  cut_point: before_answer | partial_answer | after_answer | fake_interruption
  strength:
  failure_mode:
  evidence_anchor:
```

好钩子标准：

- 立刻可懂。
- 情绪明确。
- 和主角命运绑定。
- 有明确未完成问题。
- 观众知道继续看会得到什么。
- 后续有兑现。
- 能被短视频画面表达。

差钩子标准：

- 只有设定，没有冲突。
- 只有奇观，没有人物命运。
- 只是机械打断。
- 后续很快化解且没有代价。
- 需要大量背景解释。
- 承诺和后续 payoff 无关。

### 5.4 Protagonist Engine 主角引擎模块

目的：判断主角能不能撑起连续短剧。

输出：

```yaml
ProtagonistEngine:
  protagonist:
  visible_desire:
  hidden_desire:
  wound_or_humiliation:
  initial_power_position:
  agency_level:
  secret_advantage:
  recurring_pressure:
  audience_alignment_reason:
  status_changes:
    - episode:
      from:
      to:
      trigger:
      cost:
```

强主角标准：

- 欲望清楚。
- 压力强。
- 有持续行动理由。
- 有可释放的隐藏优势或成长空间。
- 每阶段有状态变化。

弱主角标准：

- 被动承受。
- 只靠别人推动。
- 没有明确目标。
- 观众不知道为什么要站在 TA 一边。

### 5.5 Relationship Engine 关系引擎模块

目的：拆出人物关系为什么能持续产戏。

输出：

```yaml
RelationshipEngine:
  core_relationships:
    - pair:
      relationship_type:
      power_gap:
      dependency:
      secret:
      misunderstanding:
      emotional_debt:
      conflict_source:
      payoff_source:
      renewable_tension:
      relationship_turns:
        - episode:
          from:
          to:
          trigger:
```

强关系标准：

- 有权力差。
- 有秘密或误认。
- 有不能轻易分开的依赖。
- 既能制造冲突，也能制造情感 payoff。
- 每几集关系状态发生变化。

弱关系标准：

- 只有身份标签，没有行为张力。
- 误会重复拖。
- 关系不变，只是换场景吵架。
- 情绪债不清楚。

### 5.6 Conflict And Crisis Chain 冲突/危机链模块

目的：拆出压力机器，而不是孤立冲突。

输出：

```yaml
ConflictChain:
  main_obstacle:
  antagonist_force:
  conflict_sources:
  escalation_ladder:
    - episode_range:
      pressure_level:
      new_obstacle:
      protagonist_response:
      cost_or_consequence:
  crisis_points:
    - episode:
      crisis_type:
      irreversible_risk:
      hook_connection:
```

强冲突标准：

- 每阶段压力升级。
- 危机和主线目标相关。
- 主角行动会带来新代价。
- 反派/障碍不是随机出现。

弱冲突标准：

- 冲突重复。
- 只靠误会。
- 反派行为随机。
- 危机解除太容易。

### 5.7 Payoff / 爽点模块

目的：识别短剧真正让观众爽的地方，以及它如何被铺垫。

爽点类型：

- face_slap：打脸。
- revenge：复仇。
- rescue：救援/保护。
- reveal：身份/真相揭露。
- regret：对手后悔。
- humiliation_reversal：羞辱反转。
- status_rise：地位上升。
- emotional_confirmation：感情确认。
- audience_superiority：观众知道更多。

输出：

```yaml
PayoffAnalysis:
  payoff_id:
  episode:
  payoff_type:
  setup_episode:
  setup_pressure:
  release_action:
  target_of_payoff:
  emotional_effect:
  cost_after_payoff:
  next_question_created:
  strength:
  evidence_anchor:
```

强爽点标准：

- 有足够压力铺垫。
- 兑现清楚。
- 改变局面。
- 对手付出代价。
- 爽完制造新问题。

弱爽点标准：

- 无铺垫。
- 只是吵赢。
- 兑现太轻。
- 重复同一种打脸。
- 爽完故事没有变化。

### 5.8 Reversal And Information Control 反转/信息控制模块

目的：判断反转是不是改变故事状态，而不是硬拧。

输出：

```yaml
ReversalAnalysis:
  reversal_id:
  episode:
  reversal_type: identity | status | relationship | alliance | truth | danger | emotion
  prior_belief:
  new_information:
  who_knows_before:
  who_learns_now:
  story_state_change:
  setup_quality:
  payoff_connection:
  risk:
```

强反转标准：

- 有前置信息。
- 改变权力、关系、危险或目标。
- 让观众重新理解前面的事。
- 连接后续钩子。

弱反转标准：

- 没铺垫。
- 只为惊讶。
- 不改变局面。
- 反转之后人物行为不变。

### 5.9 Character And Plot Change 变化轨迹模块

目的：短剧不能只看事件列表，要看状态变化。

输出：

```yaml
ChangeMap:
  character_changes:
    - character:
      episode:
      status_from:
      status_to:
      emotional_from:
      emotional_to:
      knowledge_from:
      knowledge_to:
  relationship_changes:
    - pair:
      episode:
      power_from:
      power_to:
      trust_from:
      trust_to:
  plot_state_changes:
    - episode:
      world_state_before:
      world_state_after:
      irreversible_change:
```

核心问题：

- 每集有没有真实变化？
- 变化是人物、关系、信息、权力、危险中的哪一种？
- 有没有连续几集只换事件不换状态？

### 5.10 AI Video Fit AI 视频适配模块

目的：判断剧本能不能被 AI 视频生产链路稳定执行。

输出：

```yaml
AIVideoFit:
  location_count:
  recurring_locations:
  speaking_character_count:
  recurring_character_count:
  asset_reuse_opportunities:
  high_risk_scenes:
    - episode:
      scene:
      risk_type:
      reason:
      rewrite_suggestion:
  continuity_risks:
  prompt_complexity:
  visual_clarity:
  estimated_fit: ai-friendly | mixed | high-risk | live-action-only
```

高风险项：

- 群戏。
- 复杂打斗。
- 车辆/爆炸/大型动作。
- 儿童/动物。
- 亲密/擦边。
- 大量换景。
- 微妙表演承担强情绪。
- 复杂道具和连续性。
- 角色外貌难保持一致。

### 5.11 Compliance And Recency 合规/时效模块

目的：防止旧套路在当前市场和监管下失效。

输出：

```yaml
ComplianceAndRecency:
  compliance_risks:
    - risk_type:
      episode:
      evidence:
      severity:
      needs_human_review:
  recency_status:
  decay_risk:
  business_mode_fit:
  platform_context:
```

时效分类：

- evergreen-craft
- current-market-pattern
- aging-pattern
- stale-or-risky-pattern

规则：

- 旧剧本里的强点不自动等于当前强点。
- 如果旧稿强点依赖早期小程序 IAP 逻辑，要重新检查。
- 如果强点依赖擦边、拜金、暴力复仇、低俗标题，需要标风险。

## 6. 机制 / 表皮分离

这是深度重构的核心。

### 6.1 机制是什么

机制是故事产生效果的底层结构。

例子：

```text
公开压迫 -> 主角隐忍 -> 对手加码 -> 主角释放隐藏优势 -> 权力反转 -> 新危机出现
```

机制可以保留。

### 6.2 表皮是什么

表皮是机制的具体包装：

- 人物职业。
- 家庭背景。
- 时代背景。
- 具体事件。
- 具体场景。
- 台词。
- 道具。
- 桥段顺序。
- 羞辱方式。
- 反击方式。

深度重构时，表皮大部分应该替换。

### 6.3 Mechanism Card

每个旧稿强点都要抽成卡片：

```yaml
MechanismCard:
  mechanism_id:
  source_script:
  source_episode:
  source_scene:
  mechanism_type:
  original_surface:
  abstract_mechanism:
  narrative_function:
  audience_effect:
  timing_function:
  dependency:
  keep_reason:
  replace_required:
  reusable_conditions:
  transformation_notes:
```

### 6.4 保留/替换规则

保留：

- 情绪机制。
- 权力变化。
- 信息释放节奏。
- 危机升级逻辑。
- payoff 链条。
- 关系拉扯机制。
- 钩子承诺结构。

替换：

- 身份设定。
- 场景。
- 台词。
- 具体羞辱/打脸事件。
- 具体反转包装。
- 人物名字和职业。
- 视觉表达方式。

## 7. 重构设计模块

### 7.1 输入

```yaml
TransformationBrief:
  source_script_id:
  target_title_working:
  target_genre:
  target_episode_count:
  target_audience:
  target_platform_or_market:
  business_mode:
  target_market: overseas_live_action_short_drama
  transformation_depth: L1 | L2 | L3 | L4
  client_requirements:
  must_keep_mechanisms:
  must_avoid:
  new_setting_preferences:
  ai_video_constraints:
  compliance_constraints:
```

### 7.2 输出

```yaml
TransformationPlan:
  new_premise:
  new_logline:
  new_world:
  new_protagonist:
  new_core_relationships:
  new_antagonist_force:
  mechanism_mapping:
    - source_mechanism_id:
      new_expression:
      changed_surface:
      retained_function:
      risk:
  hook_chain:
  payoff_chain:
  crisis_chain:
  episode_plan:
  ai_video_plan:
```

### 7.3 重构强度等级

重构深度不是固定值，要由每次任务的 brief 决定。

| 等级 | 含义 | 适用情况 |
|---|---|---|
| L1 表层改写 | 改名字、地点、少量台词 | 只适合内部快速测试，不作为主路线 |
| L2 包装替换 | 换题材/身份，但桥段顺序仍相似 | 适合赶交付，但要标相似风险 |
| L3 机制重构 | 保留底层机制，重做设定、关系、事件、钩子表达 | 默认推荐 |
| L4 类型迁移 | 把机制迁移到完全不同题材/关系/市场 | 高价值，但需要更多人工审 |

默认目标是 L3，但系统必须支持每次生成前指定 `transformation_depth`。浅层和深层不是道德判断，而是交付策略；关键是系统要明确标注保留了什么、替换了什么、风险在哪里。

## 8. 新稿生成模块

生成不是凭空写，而是基于：

- 旧稿强机制。
- 新设定。
- 新人物关系。
- 新钩子链。
- 新爽点链。
- 新危机链。
- 目标集数。
- AI 视频适配约束。

### 8.1 生成层级

```text
Series Bible
-> Episode Outline
-> Beat Sheet
-> Full Episode Script
-> Production Notes
-> AI Video Brief
```

### 8.2 Series Bible 输出

```yaml
SeriesBible:
  title:
  logline:
  genre_lane:
  audience_fantasy:
  protagonist:
  core_relationships:
  antagonist_force:
  world_rules:
  emotional_promise:
  hook_strategy:
  payoff_strategy:
  visual_style:
  ai_video_constraints:
```

### 8.3 Episode Outline 输出

```yaml
EpisodeOutline:
  episode:
  opening_state:
  hook:
  main_event:
  protagonist_action:
  relationship_turn:
  conflict_escalation:
  payoff:
  reversal:
  ending_hook:
  next_promise:
```

### 8.4 完整剧本输出

每集剧本必须保留：

- 集数。
- 场次。
- 角色。
- 对白。
- 动作。
- 场景。
- 钩子标记。
- 爽点标记。
- 反转标记。
- AI 视频风险标记。

## 9. 反向检测模块

新稿生成后，必须反向检查。

### 9.1 强机制保留检测

问题：

- 旧稿强机制是否仍然存在？
- 新表达是否同等强？
- 情绪效果是否下降？
- payoff 是否变弱？
- 钩子承诺是否清楚？

输出：

```yaml
MechanismRetentionCheck:
  mechanism_id:
  retained: yes | partial | no
  new_location:
  strength_delta: stronger | same | weaker | unknown
  reason:
  fix_suggestion:
```

### 9.2 表皮重复检测

不是版权检测，而是防止低级改写。

检查：

- 是否保留了过多相同场景。
- 是否保留了过多相同桥段顺序。
- 是否只是换身份但事件功能完全一样。
- 是否台词结构过近。
- 是否人物关系表皮没有真正重做。

输出：

```yaml
SurfaceSimilarityCheck:
  risk_level: low | medium | high
  repeated_elements:
  rewrite_required:
```

### 9.3 新稿短剧强度检测

复跑分析模块：

- 开头钩子。
- 集尾钩子。
- 主角引擎。
- 关系引擎。
- 冲突递进。
- 爽点兑现。
- 反转/信息控制。
- AI 视频适配。
- 合规/时效。

## 10. 外部信息重新归纳

补充全景研究后，之前的外部搜索不是作废，而是被重新分层。

详见：

```text
/Users/jiakun/Codex/自动化编剧/research/short-drama-agent-landscape-2026-06-28.md
```

### 10.1 已确认的信息

1. 海外成熟平台主要是影视剧本 coverage、受众预测、融资/发行决策。它们可借鉴报告结构、场景引用、市场/制作分离，但不能照搬长片票房预测。
2. 中文短剧诊断工具更接近短剧原生维度。剧拆拆、创一AI/咔咔猩的价值在于钩子、节奏、卖点、合规、商业潜力等维度。
3. 中文短剧生产平台已经很丰富，包括剧火AI、知剧AI、剧大虾、小镜故事板、LibTV、Coze、Pippit、纳逗Pro、万兴剧厂等。它们证明“剧本 -> 分镜 -> 资产 -> 视频”的链路已经成熟，但不等于解决剧本强机制判断。
4. GitHub 真正有用的是生产链 schema 和证据化结构。Jellyfish、Toonflow、LocalMiniDrama、Huobao Drama 等值得借字段，不值得照搬成普通成片工作台。
5. 写作 skill、prompt、短剧方法论可以作为候选假设，但必须带 `source_hypothesis` 和 `corpus_validation_status`。
6. 2024-2026 海外真人短剧已经不能只按早期小程序 IAP 逻辑评价。IAP、IAA、订阅、广告解锁、程序化广告、多渠道分发都要进入判断。
7. 目前公开生态里仍没看到一个成熟方案同时打通“旧剧本强机制证据化分析 -> 深度重构 -> 新剧本生产 -> AI 视频交付”。

### 10.2 外部参照使用边界

```yaml
ExternalReferenceLayer:
  analysis_coverage:
    role: learn report structure and evidence-backed scoring
    examples:
      - StoryFit
      - Largo.ai
      - ScriptBook
      - Cinelytic
      - Prescene
      - OnDesk
      - ScriptReader.ai
    weight: medium
  short_drama_diagnosis:
    role: learn hook, rhythm, sell-point, compliance dimensions
    examples:
      - 剧拆拆
      - 创一AI
      - 咔咔猩
    weight: high
  production_chain:
    role: learn schema and handoff fields
    examples:
      - Jellyfish
      - Toonflow
      - LocalMiniDrama
      - Huobao Drama
      - 剧火AI
      - 小镜故事板
      - Coze
      - LibTV
    weight: high
  writing_skills:
    role: hypothesis source only
    examples:
      - 0xsline/short-drama
      - chengbenchao/short-drama-script
      - YvonneMovingon/short-drama-skills
      - llm-script-factory
    weight: medium_low
  market_trends:
    role: recency and target-market weighting
    examples:
      - ReelShort
      - DramaBox
      - ShortMax
      - Sensor Tower
      - DataEye
    weight: high
```

### 10.3 规则校准要求

每条外部规则进入系统前，都必须包装成 `RuleCard`：

```yaml
RuleCard:
  rule_id:
  rule_text:
  source:
  source_type:
  evidence_strength: high | medium | low | unknown
  market_scope:
  recency_status: current | aging | stale | unknown
  source_hypothesis:
  corpus_validation_status: untested | weakly_supported | supported | contradicted | stale
  last_validated_at:
```

没有经过自有剧本校准的规则，只能影响提示词和候选分析，不能进入正式评分权重。

### 10.4 当前最优先的验证

外部工具再多，也不能替代自有旧剧本强机制拆解。

下一步不是继续无限搜索，而是拿用户自有样本做小型 benchmark：

- 3 部高星/强评价旧剧本。
- 2 部普通或弱评价旧剧本。
- 同一套分析模板。
- 输出每集 hook、goal、obstacle、stakes、choice、reversal、relationship_delta、cliffhanger、payoff、production_fit。
- 和总体星级对照，验证哪些外部规则在用户语料里成立。

## 11. V1 成功标准

V1 的最终方向是生成完整剧本，但第一阶段不能直接以“写完整剧本”作为唯一成功标准。先证明分析和重构链路能保住强点。

V1 成功标准：

1. 能导入 1 部自有旧剧本，并保留集/场/行证据。
2. 能输出旧稿的 Narrative Spine。
3. 能识别 20-40 个 MechanismCard。
4. 能把机制分成 must-keep、optional、surface-only、stale-risk。
5. 能根据一个新 brief 生成 TransformationPlan。
6. 能生成前 3 集新分集大纲。
7. 能检测新大纲是否保留旧稿强机制。
8. 能指出新稿和旧稿过近的表皮元素。
9. 能给出 AI 视频适配风险。
10. 能把旧剧本总体星级作为弱标签使用，但不把星级当成解释本身。
11. 能按海外真人短剧目标市场输出钩子、关系、冲突和制作适配判断。

V1 不成功的表现：

- 只是把旧剧本换名字。
- 分析结果都是“节奏好、人物强、钩子强”这种空话。
- 抽不出证据锚点。
- 生成新稿后强点丢了。
- 新稿钩子弱于旧稿。
- AI 视频生产风险没有被提前发现。

## 12. V1 数据结构

### 12.1 核心对象

```yaml
ScriptImport
NarrativeSpine
HookAnalysis
ProtagonistEngine
RelationshipEngine
ConflictChain
PayoffAnalysis
ReversalAnalysis
ChangeMap
AIVideoFit
ComplianceAndRecency
MechanismCard
TransformationBrief
TransformationPlan
MechanismRetentionCheck
SurfaceSimilarityCheck
ReviewDecision
```

### 12.2 ReviewDecision

用户必须能审：

```yaml
ReviewDecision:
  target_id:
  target_type: mechanism | hook | payoff | transformation_plan | generated_episode
  decision: approve | reject | keep_but_rework | needs-evidence | surface-only | stale-risk
  reason:
  created_at:
```

## 13. V1 工作目录建议

```text
scripts/
  source/
  normalized/
  transformed/
analysis/
  imports/
  narrative-spines/
  hooks/
  mechanisms/
  ai-video-fit/
briefs/
  transformation-briefs/
plans/
  transformation-plans/
outputs/
  episode-outlines/
  scripts/
  production-briefs/
reviews/
  review-decisions.jsonl
reports/
  source-analysis.md
  transformation-report.md
```

## 14. 下一步执行建议

现在不要继续扩大竞品搜索。

下一步应该做一个非常小的真实校准：

1. 选 1 部你自己的旧剧本。
2. 选一个新目标方向，例如换题材、换人物关系、换背景、换目标集数。
3. 先只分析前 3-5 集。
4. 输出 Narrative Spine、HookAnalysis、MechanismCard。
5. 你人工确认哪些机制必须保留。
6. 再做 TransformationPlan。
7. 只生成前 1-3 集新大纲，不急着写完整剧本。
8. 反向检查：强点还在吗？表皮是不是换得足够深？AI 视频能做吗？

如果这一步跑通，再扩展到完整剧本。

## 15. 关键判断

分析模块要增强，但不是为了把评分表做得更复杂。

它真正要服务的是：

> 重构时不丢强点，生成时不变成低级改写，交付时能进入视频生产。

所以接下来所有模块都应该围绕三个问题：

1. 旧稿为什么强？
2. 新稿怎么保留这个强？
3. 新稿有没有变成另一部真正成立的短剧？
