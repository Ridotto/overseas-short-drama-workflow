# Blind Analysis Rubric V1

日期：2026-06-28  
用途：给多个独立 sub-agent 使用的统一剧本分析说明  
约束：禁止读取任何标签、备注、星级、人工评价

## 1. 任务目标

你要独立分析一份海外真人短剧剧本文本，并输出：

1. 结构化分析结果
2. 强机制与弱机制
3. `strong / medium / weak` 三档预测
4. 所有关键判断的原文证据

这不是改稿任务，不是生成任务，也不是迎合现有标签的解释任务。

## 2. 禁止项

你**不能**：

- 假设这份剧本已经被判定为好或坏
- 使用任何星级、备注、人工标签
- 根据题材偏见直接判死刑
- 只根据梗概写结论，必须回到正文证据

## 3. 分析依据

请综合以下几类依据做判断，但不要引用它们的名称，只吸收为分析标准：

1. 通用叙事标准：
   `goal / obstacle / stakes / choice / reversal / payoff / relationship change / information gap`
2. 短剧原生标准：
   `opening hook / episode retention / cliffhanger / public flip / emotional release / monetization node`
3. 生产标准：
   `live-action feasibility / AI video fit / scene-count / cast pressure / action complexity`
4. 合规与市场标准：
   `brand safety / taboo intensity / platform risk / cross-cultural clarity`

## 4. 输出矩阵

每份剧本都按同一矩阵输出，分数范围 `1-5`：

| 维度 | 解释 |
|---|---|
| `hook_strength` | 开头抓人程度，是否在极短时间内建立冲突/欲望/危险/禁忌/身份差 |
| `goal_clarity` | 主角目标是否清晰 |
| `stakes_specificity` | 失败代价是否具体，不是抽象“会很惨” |
| `choice_density` | 关键场景是否真的由角色选择推动，而不是被剧情硬推 |
| `reversal_quality` | 反转是否改变局面、权力或关系，而不只是补信息 |
| `relationship_engine` | 核心关系是否持续变化，是否能提供情绪电压 |
| `payoff_chain` | payoff 是不是一串，而不是一次性释放 |
| `retention_chain` | 每集/每段是否持续制造“还要看下去”的理由 |
| `format_integrity` | 格式是否清楚，剧本是否容易被解析进系统 |
| `production_fit_live_action` | 是否适合海外真人短剧拍摄 |
| `production_fit_ai_video` | 是否适合后续 AI 视频生成 |
| `compliance_risk` | 风险越高分越低 |
| `market_fit_overseas` | 是否适合海外真人短剧用户理解和消费 |

## 5. 强制输出字段

输出必须包含：

```yaml
blind_id:
format_observation:
overall_judgment:
  predicted_bucket: strong | medium | weak
  confidence: low | medium | high
scores:
  hook_strength:
  goal_clarity:
  stakes_specificity:
  choice_density:
  reversal_quality:
  relationship_engine:
  payoff_chain:
  retention_chain:
  format_integrity:
  production_fit_live_action:
  production_fit_ai_video:
  compliance_risk:
  market_fit_overseas:
strong_mechanisms:
weak_mechanisms:
main_risks:
rewrite_priority:
evidence_spans:
  - line_ref:
    why_it_matters:
```

## 6. 证据要求

至少给出 `8` 个证据锚点。

证据锚点必须覆盖至少这些方面：

1. 开场
2. 一个中段冲突
3. 一个关系变化点
4. 一个反转点
5. 一个 payoff 或 cliffhanger
6. 一个 production risk
7. 一个 compliance / taboo risk
8. 一个你认为最能代表强或弱的核心片段

## 7. 结论写法

结论必须长这样：

1. 先说这稿子的核心引擎是什么
2. 再说它最强的 3 个地方
3. 再说它最弱的 3 个地方
4. 最后给 `strong / medium / weak`

不能写成：

- “我感觉它像 4 星”
- “这应该是爆款”
- “这看起来一般”

## 8. 额外要求

- 不要为了显得客观而把所有分数打在中间。
- 如果是弱稿，也要指出它的真实强点。
- 如果是强稿，也要指出它真正的结构风险。
- 生产适配和市场适配必须单独判断，不能混成一个分。
