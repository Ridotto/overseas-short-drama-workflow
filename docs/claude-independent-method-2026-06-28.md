# Claude Independent Method

日期：2026-06-28  
来源：Claude 第二轮只读复核后的独立方法论提案  
原始来源：`/Users/jiakun/Codex/自动化编剧/.context/claude-review/resp-r2-2026-06-28.json`

> 重启提示：这是 Claude 的独立评判方法草案，不是完整产品方案。它可以作为“如何减少假精确、用对比代替绝对打分”的参考，但不应直接决定产品工作流。

## 核心原则

1. 判别器只回答一个问题：
   **这本能不能在前几集留住人，并且在该爽的地方真的爽到。**

2. 判别必须是：
   **pairwise**
   而不是 absolute scoring。

## 四层结构

### Layer 0

确定性结构层，代码完成，不评分：

- episode_count
- scene_count_per_episode
- speaking_characters
- location_count
- episode_end_markers
- dialogue_to_action_ratio

### Layer 1

核心判别层，只看 3 个维度：

- `D1 主角驱动力`
  主角主动推动，还是被剧情/反派/巧合推着走
- `D2 爽点兑现完整度`
  前面埋下的压力，后面是否真的兑现且改局
- `D3 推进的非重复性`
  剧情是靠长新东西推进，还是靠重复羞辱/误会/救场撑集数

### Layer 2

诊断层，不参与判别：

- primary_engine
- secondary_engine
- hook_markers
- mechanism_cards

### Layer 3

硬约束层，不参与主评分：

- ai_video_blocker
- compliance_blocker

## PairwiseJudgment

对每对剧本输出：

```yaml
PairwiseJudgment:
  winner: A | B
  margin: clear | slight
  decisive_dimension: D1 | D2 | D3
  pseudo_strength_tiebreaker:
    repeated_humiliation
    misunderstanding_dependency
    rescue_dependency
    control_without_growth
    spectacle_only
  evidence_A:
  evidence_B:
```

## 禁止打分的东西

以下不进入主判别：

- hook_strength
- stakes
- retention
- AI 视频适配
- 合规风险
- 市场热度/题材热度
- 人物弧光完整度
- 主题深度
- 总分

## 伪强点惩罚

```yaml
PseudoStrengthTiebreaker:
  repeated_humiliation_loop
  misunderstanding_dependency
  rescue_dependency
  control_without_growth
  spectacle_without_narrative_gain
```

## 输出要求

最终输出：

1. 4 份样本的 pairwise 排序
2. 每一对为什么谁比谁强
3. 每份样本的 primary_engine / secondary_engine
4. 哪些样本主要靠“假强点”在撑
