# Blind Eval Comparison

日期：2026-06-28

## 结果矩阵

| blind_id | predicted_bucket | confidence | hook | choice | reversal | relationship | payoff | live_action_fit | ai_video_fit | compliance_risk | market_fit |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| S1 | medium | high | 5 | 3 | 4 | 4 | 4 | 2 | 2 | 2 | 3 |
| S1B | medium | high | 5 | 3 | 4 | 5 | 4 | 2 | 2 | 2 | 3 |
| S2 | medium | medium | 5 | 3 | 4 | 4 | 4 | 2 | 1 | 1 | 3 |
| S3 | medium | high | 5 | 2 | 3 | 4 | 4 | 3 | 2 | 1 | 3 |
| S3B | medium | medium | 5 | 2 | 4 | 4 | 4 | 3 | 2 | 1 | 3 |
| S4 | medium | high | 5 | 3 | 4 | 5 | 4 | 3 | 2 | 1 | 2 |

## 重复样本漂移

- S1 vs S1B:
  结论一致，都是 `medium`。主要漂移在 `relationship_engine` 和 `format_integrity`，差 1 分；说明对 S1 的整体判断稳定。
- S3 vs S3B:
  结论一致，都是 `medium`。主要漂移在 `reversal_quality` 和 `confidence`，差异很小；说明对 S3 的整体判断也稳定。

## 横向观察

- strongest_by_consensus:
  从 narrative feel 看，S1 和 S2 都被认为“机制够强”；但由于 production/compliance 被一起计入，最终没有被推到 `strong`。
- weakest_by_consensus:
  S3 和 S4 都被识别出明显结构问题，但也都没有被压到 `weak`，而是停在 `medium`。
- disagreement_hotspots:
  最大分歧不在强弱方向，而在“关系引擎”与“反转质量”这种较主观项上。
- rubric_confusing_dimensions:
  当前 rubric 最大问题不是不稳定，而是**把叙事强度、生产可拍性、AI 视频适配、合规风险混成了一个总档位**。
  结果就是：强故事但高风险的稿子，也会被压成 `medium`；
  弱结构但高刺激的稿子，也会因为 hook 和 stakes 太强，被抬到 `medium`。

## 后验对照

- revealed_labels:
  S1=4 星，S2=4 星，S3=1 星，S4=1 星。
- bucket_match:
  如果把 `4 星≈strong`、`1 星≈weak` 当作粗标签，那么这轮 blind eval 的**最终档位 0 命中**，因为 4 个脚本全部被判成了 `medium`。
- notable_false_positives:
  S3、S4 虽然被识别出大量风险，但当前 rubric 仍给了 `medium`，说明它对“高刺激弱稳态”惩罚不够。
- notable_false_negatives:
  S1、S2 的核心叙事机制其实被识别出来了，但被 production/compliance 拉低，说明当前 rubric 对“强机制”奖励不够，或层级混淆。

## 当前结论

- 这次 blind 跑出来的最真实结论不是“哪个剧本好”，而是：**当前分析系统还不够强，因为它能稳定描述问题，但不能稳定拉开强弱档位。**
- 稳定性：
  还可以。重复样本 S1/S1B、S3/S3B 都没有跑飞。
- 区分度：
  明显不够。4 个样本全部压成 `medium`，说明现在的 rubric 更像“结构化评论器”，还不是“强弱判别器”。
- 根因：
  当前总档位把至少 4 件不同的事绑在了一起：
  `故事机制强度`
  `生产可拍性`
  `AI 视频适配`
  `合规/品牌风险`

## 下一步修改方向

1. 把总评拆成双层甚至三层：
   `NarrativeStrength`
   `ProductionSuitability`
   `ComplianceRisk`
   必要时再单列 `MarketFit`
2. 让最终 bucket 先只反映 `NarrativeStrength`，不要被 production/compliance 一票拉平。
3. 单独增加“弱稳态惩罚项”：
   `重复羞辱循环`
   `误会/伪证依赖`
   `角色主动性不足`
   `关系合法性/可信度不足`
4. 下一轮继续 blind，但要求 agent 在输出里同时给：
   `story_bucket`
   `production_bucket`
   `risk_bucket`
