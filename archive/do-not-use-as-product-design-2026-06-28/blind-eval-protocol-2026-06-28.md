# 剧本分析模块 Blind Eval 协议

日期：2026-06-28  
目的：验证系统是否能在**不看标签**的前提下，独立判断剧本强弱与机制质量

## 1. 为什么需要这份协议

只要分析前已经看到了：

- 星级
- 人工备注
- “这是强稿/弱稿”的先验分类

那一轮结果就不能当有效 eval，只能当：

- 语料 intake
- 机制发现
- 特征候选整理

不能用来证明：

- 系统有没有足够强
- 系统的强弱判断是否独立成立
- 哪些规则应该正式定权

## 2. 评估原则

blind eval 的核心是：

> 先独立分析，后揭晓标签，再对比。

顺序不能反。

## 3. 输入约束

blind pass 输入里**禁止出现**：

- `评级`
- `备注`
- `强/弱/普通` 人工结论
- 文件名中明显暴露质量判断的信息
- 任何“这篇很好/很差”的口头提示

允许输入：

- 匿名 script id
- 正文文本
- 格式信息
- 必要的目标市场信息

推荐匿名化输入形态：

```yaml
BlindScriptPacket:
  blind_id:
  source_text_path:
  target_market: overseas_live_action_short_drama
  metadata:
    language:
    format_type:
    episode_count_if_known:
```

## 4. 正式评估流程

### Phase A：盲分析

系统只看匿名正文，对每份剧本输出：

```yaml
BlindAnalysisResult:
  blind_id:
  independent_score:
    hook:
    retention:
    payoff:
    relationship_engine:
    protagonist_engine:
    reversal_quality:
    production_fit:
    compliance_risk:
  predicted_bucket:
    strong | medium | weak
  confidence:
  strong_mechanisms:
  weak_mechanisms:
  evidence_spans:
  rewrite_orders:
```

要求：

- 每个判断必须带原文证据。
- 不允许引用任何外部标签。
- 不允许在这一阶段读备注。

### Phase B：冻结结果

盲分析输出一旦写入文件，就冻结。

冻结后禁止：

- 根据标签回改分数
- 根据备注重写原结论
- 补“早知道它是一星所以我觉得它弱”式解释

允许追加：

- 对比结果
- 误差分析
- 后验校准建议

### Phase C：揭晓标签并对比

对比时再读取：

- Base `评级`
- Base `备注`
- 其他已有人工评价

比较维度：

1. `bucket hit`
   `strong / medium / weak` 是否命中
2. `relative ranking`
   系统排序和人工排序是否一致
3. `mechanism agreement`
   系统指出的强弱点，是否和人工备注能对上
4. `production agreement`
   系统识别的制作风险，是否和业务直觉一致
5. `false confidence`
   系统是否在弱稿上给出过高自信

## 5. 最小评分设计

第一版不要追求复杂统计，先做最小可用评估：

```yaml
BlindEvalScorecard:
  blind_id:
  predicted_bucket:
  revealed_rating:
  bucket_match: true | false
  notable_alignment:
  notable_mismatch:
  should_update_rule_cards:
```

## 6. 当前样本怎么处理

当前这 4 份样本已经被看过 `评级`，其中还有一次误带出 `备注` 的操作失误。

因此：

- 它们**不能**再被称为严格 blind eval 样本。
- 它们只能保留为：
  `feature discovery`
  `规则候选发现`
  `格式归一验证`
  `中间 schema 设计`

## 7. 接下来怎么做才干净

有两种做法。

### 做法 A：新样本盲评

最干净。

步骤：

1. 从 Base 或其他来源拿一批新剧本。
2. 先匿名化。
3. 只给正文，不给评分和备注。
4. 跑 blind pass。
5. 再揭晓标签。

### 做法 B：当前样本继续做“伪盲后的独立打分”

可以做，但不能叫严格 blind。

适用场景：

- 先快速做内部 rubric 迭代
- 先看系统是否能稳定输出结构化判断

限制：

- 结果只能用于 prompt / rubric 改进
- 不能用于对外宣称有效性

## 8. 下一步推荐

当前最合理的顺序：

1. 保留现有 4 份样本作为 `feature discovery`。
2. 基于这 4 份先做 `RuleCard` 候选库。
3. 再拿一批**我没看过标签**的新样本，跑第一轮真正 blind eval。

## 9. 当前文件状态

以下文件已明确标记为**非 blind eval**：

- `/Users/jiakun/Codex/自动化编剧/analysis/first-pass-2026-06-28/first-pass-structured-extraction.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/first-pass-2026-06-28/first-pass-structured-extraction.yaml`
