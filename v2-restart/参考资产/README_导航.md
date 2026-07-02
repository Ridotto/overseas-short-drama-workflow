# 参考资产导航（供 Codex review 用）

> 这些是从 6 个开源项目里**精选**出来的有用部分（非完整 repo），用于"拆开适配成我们自己的新项目"。
> 每个目录对应设计提纲 v2 里的某个环节。下面说明：每个项目**拿什么、补我们哪个环节、对应设计提纲哪一节**。
> ⚠️ 这些是参考来源，不是直接成品。需经适配改造（剔除不对口部分、加海外短剧内核）。

---

## 目录总览

| 目录 | 来源项目 | star | 拿来补什么 | 对应设计提纲节 |
|---|---|---|---|---|
| `1-short-drama_短剧标准库` | 0xsline/short-drama | 731 | 钩子/爽点矩阵/节奏曲线/反派四层/付费点/海外赛道/出海合规 | §13 短剧标准库 |
| `2-oh-story_追踪与去AI味` | worldwonderer/oh-story-claudecode | 3.2k | 4个追踪文件模板 / 去AI味禁用词+脚本 / 拆文方法 / 11写作手法 / 文件驱动架构 | §7 连续性管理、§5.5 去AI味 |
| `3-how-to-make-script_方法论` | XucroYuri/how-to-make-script | 11 | rewrite_report四层诊断 / 镜头感hard-fail / check-lens质检 / 输出契约 | §4.3 分层诊断、§5.4 镜头感 |
| `4-dramatron_分层生成` | google-deepmind/dramatron | 1.1k | 分层一致性生成 / 标记解析 / 前缀注入 / 选择性上下文 | §5.2 重构管线 |
| `5-shortdrama-pipeline_质检` | drasstry/shortdrama-pipeline | — | 可量化质检计数器 / suggestion字段 / 人工审核门 | §6.2 评分机制工程门 |

---

## 各目录精读指引

### 1-short-drama_短剧标准库 ★最对口
**这是全套短剧创作标准，几乎可直接改造成我们的"短剧标准库"。**
- `references/hook-design.md` — 钩子5类×5子模式 + 叠加规则
- `references/satisfaction-matrix.md` — 爽点矩阵5类 + ★强度 + 主副辅配比
- `references/rhythm-curve.md` — 节奏四段配比公式（起势/攀升/风暴/决战）
- `references/villain-design.md` — 反派四层体系（我们原本完全没有）
- `references/paywall-design.md` — 付费/留存卡点位置表
- `references/opening-rules.md` — 开场6模板 + 黄金法则
- `references/genre-guide.md` — 13题材 + **海外S/A赛道 + 8条中式陷阱替代**（最对口本项目）
- `references/compliance-checklist.md` — 合规（国内部分剔除，只用出海补充）
- `SKILL.md` — 整体工作流（选题→骨架→角色→分集→逐集→评分→合规）

**适配要点**：剔除国内合规导向，强化海外赛道；爽点矩阵/钩子清单直接做成评分打标量表。

### 2-oh-story_追踪与去AI味 ★架构启发
**核心价值：连续性管理 + 去AI味 + "文件驱动闭环"架构。**
- `demo_追踪机制/追踪/` — **4个追踪文件实样**（伏笔.md/角色状态.md/时间线.md/上下文.md）→ 把"章"改"集"直接用
- `scripts/` — 去AI味 check 脚本（check-ai-patterns 等）→ 做成台词 lint
- `demo_拆文样本/` — 拆文报告/写作手法/情节节点 实样 → 对标我们分析机制（它更细、全量化、带原文锚点）
- `_claude_skills/`（原 .claude）— 它的 skill/agent/hook 定义 → 看它怎么编排"分析→对标→写作→追踪"
- `README.md` — 总览

**架构启发**：分析产物=source of truth，写作 skill 消费它，追踪文件全程防漂移。我们"分析旧爆款→重构→输出新剧本"可 1:1 套这个架构。

### 3-how-to-make-script_方法论 ★方法论最系统
**它把"写+评+诊断"做成机器可读的契约结构。**
- `references/output-format-contracts.json` + `.md` — 30类输出契约（找 rewrite_report / quality_gate_report / audience_proxy_report）
- `references/check-lens-matrix.json` — 7个质检镜（mechanics_pressure / continuity_invariants / operational_feasibility 等）
- `docs/adaptive-quality-checking-zh.md` — 自适应质检机制
- `references/expression-lens-triggers.md` — **情绪标签句 hard-fail 规则**（治镜头感）
- `docs/multilingual-visual-language-layer-zh.md` — 视觉语言层
- `references/agent-team-roles.json` + `expert-subagent-library.json` — 专家角色（Rewrite Triage Lead 等）
- `docs/how-to-create-a-screenplay-research-zh.md` — 创作研究方法论

**重点拿**：rewrite_report 的"四层诊断(概念/结构/场景/对白)+三级分级"；情绪标签句 hard-fail。

### 4-dramatron_分层生成 ★重构骨架
- `dramatron.ipynb` — **核心全在这里**：分层 prompt（logline→characters→scenes→dialog）、标记解析、前缀注入、选择性上下文。
- `README.md` — 方法总览

**拿来做重构管线**：旧剧本逆向抽取成 logline/人物表/beat表/地点表 → 按新设定逐层重生。
**避开其短板**：它自承"套路化"、纯top-down不可回改 → 我们要加"下层回写上层"校对环 + 人审。

### 5-shortdrama-pipeline_质检 ★工程质检
- `harness.py` — **可量化质检计数器**（shot时长/动作过载/对白过载阈值 + 减分公式）
- `models.py` — 数据模型（Episode 有独立 hook 字段、ScriptQualityIssue 带 suggestion）
- `prompts.py` — 它强调的质量标准
- `pipeline.py` — 状态机（含人工审核门）
- `docs/ARCHITECTURE.md`

**拿来**：用计数器做零成本可量化质检门（适配到剧本层）；每个扣分点附 suggestion 改法。

---

## 适配总原则（对应设计提纲 §11 TODO）

1. **拆现成**：能改造的直接拆（short-drama 标准库、oh-story 追踪+去AI味、how-to-make-script 诊断、Dramatron 管线、shortdrama 质检）。
2. **去不对口**：剔除国内合规、视频生产、镜头级JSON输出、票房预测——这些和"海外纯剧本输出"冲突。
3. **自建差异化**：海外真人AI短剧爆款内核（前3秒钩子+卡点+竖屏+AI可生成性）、情绪曲线数值化、期望-惊奇评分、重构专用管线——没有现成的，是我们的核心。

> 完整设计见 `../设计提纲_v2.md`。
