# 外部参考最低必要接入审计

日期：2026-07-04

> 更新口径：本文件是较早的最低必要接入审计，其中“长线状态只在多批次阶段启用”的判断已被修正。最新完整读档和接入判断见 `external_skill_reference_integration_map_2026-07-04.md`。

## 结论先行

当前不是“所有参考都要接”，也不是“参考不能接”。
最低必要原则是：

```text
参考必须按需读取；
必须服务当前短剧洗稿产品；
必须落到蓝图、角色、分集执行包、正文或 review；
不得把电影、电视剧、小说、泛 AI 写作方法带进主链。
```

## 完整阅读口径

本文件里的“读过”，只指主控在本轮完整打开并读完对应文件全文，不指摘要、不指目录扫描、不指听别人转述。

已完整读完的范围：

- 当前已接入执行面：
  - `shortdrama-remix/README.md`
  - `contracts/short_drama_form_lock_v1.md`
  - `skills/source-import/SKILL.md`
  - `skills/source-import/references/README.md`
  - `skills/short-drama-write/SKILL.md`
  - `skills/short-drama-write/README.md`
  - `skills/short-drama-write/LICENSE`
  - `skills/short-drama-write/.gitignore`
  - `skills/short-drama-write/references/` 下 8 个短剧 reference
  - `vendor/short-drama/SKILL.md`
- 已确认与本地副本完全一致、无需重复读正文的冻结原件：
  - `vendor/short-drama/README.md`
  - `vendor/short-drama/LICENSE`
  - `vendor/short-drama/.gitignore`
  - `vendor/short-drama/references/` 下 8 个 reference
- 本轮可接入候选，已完整读完：
  - `how-to-make-script/skills/scene-writing/SKILL.md`
  - `how-to-make-script/knowledge/20-workflows/wp-scene-writing.md`
  - `how-to-make-script/knowledge/60-rubrics/rb-scene-draft.md`
  - `how-to-make-script/skills/dialogue-subtext/SKILL.md`
  - `how-to-make-script/knowledge/20-workflows/wp-dialogue-polish.md`
  - `how-to-make-script/knowledge/60-rubrics/rb-dialogue.md`
- 本轮排除项，已完整读完主文件或明确列出的排除证据：
  - `oh-story/story-deslop/SKILL.md`
  - `oh-story/story-deslop/references/anti-ai-writing.md`
  - `oh-story/story-deslop/references/banned-words.md`
  - `oh-story/story-review/SKILL.md`
  - `oh-story/story-short-write/SKILL.md`
  - `oh-story` 追踪 demo 的 `角色状态.md`、`伏笔.md`、`上下文.md`、`时间线.md`

没有完整读完、因此不得声称已接入或可抽取的范围：

- `story-review/references/` 与 `story-review/scripts/`
- `story-short-write/references/` 与 `story-short-write/scripts/`
- `story-deslop/scripts/`

这些文件不进入本轮候选接入。后续如果要从其中任意一个文件抽取能力，必须先把目标文件全文读完，再做最小接入判断。

## “按需接”的两种情况

### 1. 已接入，但按阶段读取

`short-drama` 标准库属于这一类。

当前 `skills/short-drama-write/SKILL.md` 已明确在不同阶段读取：

- `/start`、`/plan`：`genre-guide.md`、`opening-rules.md`、`paywall-design.md`、`rhythm-curve.md`、`satisfaction-matrix.md`
- `/characters`：`villain-design.md`
- `/episode`：`opening-rules.md`、`rhythm-curve.md`、`satisfaction-matrix.md`、`hook-design.md`
- `/review`：`contracts/short_drama_form_lock_v1.md`

这些 reference 已经完整复读过；问题只剩执行质量。

### 2. 还没正式接入，但可评估后接

`how-to-make-script`、`oh-story` 的局部文件属于这一类。
有些思想已经被编进 `short-drama-write` 和 contract，但原参考文件还没有作为“某阶段必须读取的本地 reference”正式接入。

## 候选参考逐项判断

| 外部参考 | 本轮完整读过的文件 | 是否接入 | 接入方式 | 原因 |
| --- | --- | --- | --- | --- |
| `how-to-make-script / scene-writing` | `skills/scene-writing/SKILL.md`、`knowledge/20-workflows/wp-scene-writing.md`、`knowledge/60-rubrics/rb-scene-draft.md` | 接，但不单独成文件 | 最新已合并进 `performance-dialogue-brief.md`，只给 `/episode` 和 `/review` 按需读 | 它正好补“场面是否真的发生变化、对白是否有动作承载”，但不能让它决定剧情 |
| `how-to-make-script / dialogue-subtext` | `skills/dialogue-subtext/SKILL.md`、`knowledge/20-workflows/wp-dialogue-polish.md`、`knowledge/60-rubrics/rb-dialogue.md` | 接，但不单独成文件 | 最新已合并进 `performance-dialogue-brief.md`，只给 `/episode` polish 和 `/review` 按需读 | 它能补台词解释腔、同声线、潜台词弱，但只能改表达，不能改剧情 |
| `oh-story / story-deslop` | `skills/story-deslop/SKILL.md`、`references/anti-ai-writing.md`、`references/banned-words.md` | 暂不整接 | 只保留已编入的轻 polish 原则；暂不让 writer 读完整网文去 AI 味 | 原文件是网文口径，规则很厚，容易把短剧台词磨成小说自然文；只有 clean run 暴露 AI 味硬伤时再接瘦身版 |
| `oh-story / 状态追踪 demo` | `追踪/角色状态.md`、`追踪/伏笔.md`、`追踪/上下文.md`、`追踪/时间线.md` | 不整接，需重做本地瘦身版 | 最新判断见 `external_skill_reference_integration_map_2026-07-04.md`：长线追踪从 `/plan` 开始以轻量全剧骨架启用，首批只吃当前批和本集速记 | 原 demo 适合长篇工程追踪，不能原样污染短剧；但“状态骨架/本集速记/批次汇总”必须进入产品链 |
| `oh-story / story-review` | `skills/story-review/SKILL.md` | 不接，且不抽附属 reference | 不进入当前 reviewer | 它是网文多视角审查，平台和口径不对；`references/` 和 `scripts/` 未进入候选，后续若要抽某个文件必须另行全文读取 |
| `oh-story / story-short-write` | `skills/story-short-write/SKILL.md` | 不接，且不抽附属 reference | 不进入当前主链 | 它是短篇网文写作链，默认第一人称、8000 字短篇、小节制和小说题材风格包，会污染短剧产品 |
| Dramatron | 未列入本轮接入候选 | 不接 | 仅历史启发 | 原创分层生成，不适合源本洗稿短剧生产链 |
| shortdrama-pipeline | 未列入本轮接入候选 | 不接 | 仅历史启发 | 视频/质检流水线，不是当前文本主创能力 |

## 最低必要接入决定

本节是早一轮的最低必要判断，保留作历史证据。后续完整接入图已经把它修正为：

1. `series-state-brief.md`
2. `performance-dialogue-brief.md`

其中 `scene-action-brief.md` 和 `dialogue-subtext-brief.md` 不再作为两个独立文件创建，而是合并进 `performance-dialogue-brief.md`，避免 writer 同时吃太多碎 reference。

早一轮曾建议接两块：

1. `scene-action-brief.md`
2. `dialogue-subtext-brief.md`

它们必须是本地瘦身 reference，不是外部整包。

## 具体接入规则

### `scene-action-brief.md`

来源：

- `scene-writing/SKILL.md`
- `wp-scene-writing.md`
- `rb-scene-draft.md`

只保留：

- scene function
- conflict
- change point
- playable action
- dialogue carrier
- scene end state

禁止带入：

- 泛 screenplay 产物形态；
- 多 agent router；
- 电影/电视剧场景节奏；
- 让 scene-writing 自己发明剧情。

读取时机：

- `/episode` 写正文前；
- `/review` 判断场面弱、裸对白、站着解释时。

必须影响：

- 正文每场戏是否改变信息、关系、权力或行动条件；
- 压迫性对白后是否有动作/表演承载；
- review 的责任层归因。

### `dialogue-subtext-brief.md`

来源：

- `dialogue-subtext/SKILL.md`
- `wp-dialogue-polish.md`
- `rb-dialogue.md`

只保留：

- surface speech vs real objective
- cut explanation, restore strategy
- voice separation
- subtext
- dialogue economy

禁止带入：

- 金句化；
- 电影对白课腔；
- 为了潜台词牺牲短剧直给刺激；
- 改剧情、改真相释放、改人物关系。

读取时机：

- `/episode` 的去 AI 味轻 polish；
- `/review` 判断台词解释腔、同声线、裸对白时。

必须影响：

- 台词是否服务当前目标对抗；
- 每个角色是否有声线差异；
- 信息是否藏在冲突里，而不是说明书式说完。

## 当前不接的原因

`story-deslop`、`story-review`、`story-short-write` 都不是短剧洗稿主链。
它们的完整参考太厚，且是网文 / 小说口径；如果现在整接，会带来三类风险：

1. 把短剧台词磨成小说自然文；
2. 把 reviewer 变成网文审稿，而不是短剧付费体验审稿；
3. 让 writer 上下文里出现太多与当前任务无关的规则，注意力分散。

## 下一步

本节已被 `external_skill_reference_integration_map_2026-07-04.md` 修正。当前下一步不再创建 `scene-action-brief.md` / `dialogue-subtext-brief.md` 两个文件，而是执行：

1. 新增 `skills/short-drama-write/references/series-state-brief.md`
2. 新增 `skills/short-drama-write/references/performance-dialogue-brief.md`
3. 修改 `skills/short-drama-write/SKILL.md`：
   - `/plan`、`/characters`、`/outline`、`/episode`、`/batch-state` 接入 `series-state-brief.md`
   - `/episode` 与 `/review` 接入 `performance-dialogue-brief.md`
   - `/batch-state` 改为批次完成后的续写状态汇总
4. 不接 `story-deslop` 完整包，不接 `story-review`，不接 `story-short-write`

完成后再做 clean run。
