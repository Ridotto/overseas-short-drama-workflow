# Blind Eval Comparison V2

日期：2026-06-28

## 结果矩阵

| blind_id | narrative_strength | production_fit_live_action | ai_video_fit | compliance_risk | market_fit |
|---|---|---:|---:|---|---:|
| V2-S1 | medium | 3 | 2 | high | 3 |
| V2-S2 | weak | 3 | 2 | high | 3 |
| V2-S3 | medium | 3 | 2 | high | 2 |
| V2-S4 | medium | 3 | 2 | high | 3 |

## 直接结论

V2 比 V1 好一点，但还不够。

好一点的地方：

- V1 把 4 份脚本全部压成 `medium`。
- V2 至少开始出现分层，`V2-S2` 被拉到了 `weak`。

不够的地方：

- 其余 3 份仍然都在 `medium`。
- 如果拿现有弱标签做粗对照，系统还是没能把 4 星和 1 星样本稳定拉开。

## 这说明什么

这不说明 blind eval 没意义，恰恰说明：

1. 现在的分析器已经能稳定输出结构化判断。
2. 但它还没有找到真正能分强弱的核心判别维度。

目前最像判别器的维度有：

- `choice_density`
- `agency_balance`
- `repeated_humiliation_loop`
- `misunderstanding_dependency`
- `control_without_relationship_growth`

目前仍然过于饱和、拉不开的维度有：

- `hook_strength`
- `stakes_specificity`
- `retention_chain`

因为这些维度在强稿和弱稿里都能被做得很高。

## 关键判断

当前系统最容易犯的错，不是“看不见问题”，而是：

> 把“很能钩人、很能卡点”误当成“叙事足够强”。

这就是为什么：

- S3 这种 `shock/VFX 型弱法` 还能拿到 `medium`
- S4 这种 `禁忌羞辱高压型弱法` 也还能拿到 `medium`

它们都很会抓人，但未必真的更强。

## 下一步该怎么改

1. 不再把 `hook / stakes / retention` 当主判别项，它们更像“基础门槛”。
2. 把真正拉强弱的权重移到：
   `agency_balance`
   `choice_density`
   `mechanism_variety`
   `relationship_growth_quality`
3. 新增一个显式扣分项：
   `pseudo_strength_penalty`
   用来专门处理“强刺激但弱稳态”的稿子。
4. 下一轮不要只做 absolute scoring。
   加一个 pairwise comparison：
   让 agent 在两份剧本之间直接回答“哪份更强，为什么”，有时比绝对打分更容易拉开。

## 当前最可信的结果

这轮最可信的不是“谁是 strong”，而是下面两条：

1. S1 的稳定判断是：
   强商业引擎，但叙事仍被重复羞辱和误会拖住，所以不是稳 strong。
2. S3 / S4 的稳定判断是：
   它们都不是“没钩子”的弱稿，而是“假强点很多”的弱稿。

这两条对后面建真正的判别系统最有价值。
