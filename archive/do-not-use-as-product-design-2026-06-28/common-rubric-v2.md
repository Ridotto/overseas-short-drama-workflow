# Blind Analysis Rubric V2

日期：2026-06-28  
目的：解决 V1 把 `叙事强度 / 生产可拍性 / AI 视频适配 / 合规风险` 混成一个总档位，导致所有脚本塌成 `medium` 的问题

## 1. 核心改动

V2 不再只给一个总 bucket。

改为四层输出：

```yaml
NarrativeStrength:
ProductionSuitability:
ComplianceRisk:
MarketFit:
```

其中：

- `NarrativeStrength` 决定剧本本身是否强。
- `ProductionSuitability` 只判断是否适合拍和适合做 AI 视频。
- `ComplianceRisk` 只判断上线/平台/品牌风险。
- `MarketFit` 只判断目标市场是否吃这套。

## 2. 最终 bucket 规则

最终 `strong / medium / weak` 只由 `NarrativeStrength` 决定。

不要再让以下问题直接把强故事压成 `medium`：

- 场面太贵
- AI 不好做
- 合规风险高

这些要单列风险，不该直接覆盖故事判断。

## 3. NarrativeStrength 评分矩阵

每项 `1-5`：

| 维度 | 解释 |
|---|---|
| `hook_strength` | 开头抓人是否成立 |
| `goal_clarity` | 主角目标是否清楚且持续 |
| `stakes_specificity` | 失败代价是否具体 |
| `choice_density` | 关键推进是否来自角色选择 |
| `reversal_quality` | 反转是否改局面、关系、权力或信息结构 |
| `relationship_engine` | 核心关系是否持续提供情绪电压 |
| `payoff_chain` | payoff 是否是延迟兑现的一串，而不是单点 |
| `retention_chain` | 每集/每段是否持续创造继续看的理由 |
| `mechanism_variety` | 推进方式是否多样，不只是重复羞辱或重复误会 |
| `agency_balance` | 主角是否不仅承受，还能主动改变局面 |

### NarrativeStrength bucket

```text
strong:
  hook_strength >= 4
  relationship_engine >= 4
  payoff_chain >= 4
  retention_chain >= 4
  and at least 6 of 10 dimensions >= 4
  and no more than 2 core dimensions <= 2

medium:
  above average but not enough strong criteria

weak:
  4 or more core dimensions <= 2
  or narrative progression heavily depends on repeated humiliation / repeated misunderstanding / repeated rescue
```

## 4. Weakness penalties

V2 明确加入 4 个惩罚项，不单独打分，但必须判断：

```yaml
WeaknessPenalties:
  repeated_humiliation_loop:
  misunderstanding_dependency:
  rescue_dependency:
  control_without_relationship_growth:
```

规则：

- 任意两项严重成立，`NarrativeStrength` 不得判 `strong`。
- 三项严重成立，默认降到 `weak` 候选，再看证据是否能拉回 `medium`。

## 5. ProductionSuitability

这个维度单独看，不参与故事强弱 bucket。

```yaml
ProductionSuitability:
  live_action_fit: 1-5
  ai_video_fit: 1-5
  scene_complexity:
  cast_pressure:
  action_vfx_pressure:
  continuity_pressure:
```

## 6. ComplianceRisk

也单独看，不直接覆盖 `NarrativeStrength`。

```yaml
ComplianceRisk:
  sexual_coercion_risk:
  minor_or_young_coding_risk:
  violence_gore_risk:
  humiliation_abuse_risk:
  brand_safety_risk:
  final_bucket: low | medium | high
```

## 7. MarketFit

```yaml
MarketFit:
  trope_match:
  cross_cultural_clarity:
  audience_pull:
  public_ad_hookability:
  overseas_live_action_fit:
```

## 8. 强制输出格式

```yaml
blind_id:
format_observation:
narrative_strength:
  bucket: strong | medium | weak
  scores:
    hook_strength:
    goal_clarity:
    stakes_specificity:
    choice_density:
    reversal_quality:
    relationship_engine:
    payoff_chain:
    retention_chain:
    mechanism_variety:
    agency_balance:
  weakness_penalties:
    repeated_humiliation_loop:
    misunderstanding_dependency:
    rescue_dependency:
    control_without_relationship_growth:
production_suitability:
  live_action_fit:
  ai_video_fit:
  scene_complexity:
  cast_pressure:
  action_vfx_pressure:
  continuity_pressure:
compliance_risk:
  final_bucket:
market_fit:
  overseas_live_action_fit:
overall_take:
strong_mechanisms:
weak_mechanisms:
rewrite_priority:
evidence_spans:
```

## 9. 使用建议

下一轮 blind eval 必须：

1. 先按 V2 跑。
2. 先看 `NarrativeStrength` 是否能把强弱样本拉开。
3. 再看 `ProductionSuitability` 和 `ComplianceRisk` 是否解释为什么“强故事不一定能拍”。
