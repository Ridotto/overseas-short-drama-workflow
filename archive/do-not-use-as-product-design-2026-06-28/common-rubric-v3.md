# Blind Analysis Rubric V3

日期：2026-06-28  
目的：把“主引擎判断”和“约束检查”彻底拆开，避免所有稿子被压成 `medium`

## 0. 这版到底改什么

V1 的问题：

- 把太多东西揉成一个总分

V2 的问题：

- 已经拆出了 `NarrativeStrength / Production / Compliance / Market`
- 但 `NarrativeStrength` 里维度还是太多、太平均
- 仍然容易把“很会钩人”和“叙事真的强”混在一起

V3 的核心改动只有三条：

1. **先判主引擎**
2. **NarrativeStrength 只保留最少的核心维度**
3. **AI 视频适配、合规、市场全部降级成约束/标签，不再参与主评分**

## 1. 主引擎优先

每份剧本先识别主引擎，只能选 1 个主引擎，最多 1 个辅助引擎。

```yaml
PrimaryEngine:
  identity_flip
  revenge_counterattack
  taboo_relationship
  career_comeback
  pregnancy_bloodline
  survival_escape
  family_betrayal
  hidden_power

SecondaryEngine:
  public_humiliation_flip
  rescue
  misunderstanding_backfire
  inheritance_war
  forced_contract
  audience_knowledge_gap
```

规则：

- 不允许把 3-4 个引擎都说成主引擎。
- 如果主引擎说不清，这稿大概率已经不够稳。

## 2. NarrativeStrength 只看 5 件事

### 2.1 核心维度

| 维度 | 问的问题 |
|---|---|
| `hook_chain` | 开场和每次关键卡点，是否都服务主引擎，而不是乱炸 |
| `protagonist_drive` | 主角是否持续主动推动，不只是被剧情推着走 |
| `relationship_voltage` | 核心关系是否持续变化，而不是只重复一个姿态 |
| `reversal_payoff_integrity` | 反转和 payoff 是否真的改局，而不是只补信息/只加刺激 |
| `anti_repetition` | 推进是否在长新东西，而不是重复羞辱、重复误会、重复救场 |

每项 `1-5`。

### 2.2 Narrative bucket

```text
strong:
  5 个核心维度里至少 3 个 >= 4
  且没有 2 个及以上 <= 2
  且主引擎明确、持续、没有被辅助引擎抢戏

medium:
  有明确主引擎，也有可追看性
  但至少 2 个核心维度卡住

weak:
  主引擎不清
  或者主要靠重复羞辱/重复误会/重复救场撑长度
  或者 payoff 不能真正兑现前面承诺
```

## 3. 明确的假强点惩罚

V3 不再泛泛写风险，而是专门打“假强点”。

```yaml
PseudoStrengthPenalty:
  repeated_humiliation_loop:
  misunderstanding_dependency:
  rescue_dependency:
  control_without_relationship_growth:
  spectacle_without_narrative_gain:
```

规则：

- 任意 2 项严重成立：不得判 `strong`
- 任意 3 项严重成立：默认 `weak` 候选

## 4. 约束层，不参与主评分

### 4.1 AI 视频适配

只做约束，不评分进主 bucket。

```yaml
AIVideoFit:
  character_consistency_pressure:
  scene_count_pressure:
  action_complexity_pressure:
  continuity_pressure:
  visual_clarity:
  final_bucket: low | medium | high
```

### 4.2 合规

只做 blocker / warning，不评分进主 bucket。

```yaml
ComplianceFlags:
  sexual_coercion:
  minor_coding:
  gore_or_extreme_violence:
  humiliation_abuse:
  platform_brand_safety:
  final_bucket: low | medium | high
```

### 4.3 市场

市场先不打重分，只记录标签。

```yaml
MarketTags:
  trope_family:
  ad_hook_types:
  cross_cultural_clarity:
  likely_audience:
  note:
```

## 5. 输出格式

```yaml
blind_id:
format_observation:
primary_engine:
secondary_engine:
narrative_strength:
  bucket: strong | medium | weak
  scores:
    hook_chain:
    protagonist_drive:
    relationship_voltage:
    reversal_payoff_integrity:
    anti_repetition:
  pseudo_strength_penalty:
    repeated_humiliation_loop:
    misunderstanding_dependency:
    rescue_dependency:
    control_without_relationship_growth:
    spectacle_without_narrative_gain:
ai_video_fit:
  final_bucket:
compliance_flags:
  final_bucket:
market_tags:
overall_take:
strong_mechanisms:
weak_mechanisms:
rewrite_priority:
evidence_spans:
```

## 6. 为什么这版更适合现在

因为你现在最想知道的不是：

- 它是不是一个完美的全方位作品

而是：

- 它的主引擎强不强
- 它是不是靠假强点撑着
- 后面改写时哪些强点必须保，哪些脏东西必须去

V3 就是为这个问题写的。

## 7. 外部公开样本的使用边界

公开 title 页、剧情页、平台热度证明不能直接定权。

它们最多只做：

```yaml
PublicReference:
  title:
  platform:
  verified_assets:
  trope_family:
  likely_engine_guess:
  note:
```

也就是说：

- 它们只能告诉我们“市场上公开出现过什么题材/引擎”
- 不能直接告诉我们“这些机制怎么加权”

## 8. 下一轮怎么测

下一轮不要再只做 absolute scoring。

必须加：

### Pass A：单本 blind 判断

输出上面的 V3 schema。

### Pass B：pairwise comparison

对每组剧本问：

```text
哪一本主引擎更强？
哪一本更依赖假强点？
哪一本更值得保留脉络做深度重构？
```

### Pass C：后验揭标签

最后才对照：

- 星级
- 备注
- 其他外部结果

## 9. 当前一句话版本

> V3 不再问“这本全面不全面”，只问“它靠什么强，它是真的强，还是只是看起来强”。  
