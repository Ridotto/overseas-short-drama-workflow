# shortdrama-remix 架构对齐检查点

日期：2026-07-04

本文件用于防止上下文压缩后丢失当前判断。后续 agent 如果接手，先读：

1. `../v2-restart/PRD_v4.md`
2. `README.md`
3. `skills/source-import/SKILL.md`
4. `skills/short-drama-write/SKILL.md`
5. `contracts/short_drama_form_lock_v1.md`
6. 本文件

## 当前判断

当前不再回 `v20`、`v3` 或旧 workflow 扩规则。`shortdrama-remix` 是当前第一条可执行生产链。

下一步不是“继续写一个更大的 workflow”，也不是立刻做网页 App，而是把当前主链按最终产品架构收口：

```text
用户层：主控 agent / 未来网页入口
生产层：source-import / short-drama-write / clean reviewer / delivery QA / 按需 helper agent
能力层：skills / references / contracts / state
```

外部 skill、reference、题材包、helper 输出只有进入以下三类交接物，才算真正接入产品：

- 用户可确认的商业项目包 / 创作蓝图包；
- writer 必须消费的分集执行包；
- reviewer / polish 的硬边界。

只留“参考一下”“可采纳建议”“知识库摘要”，不算接入。

## 已讨论能力的归位

| 能力 | 不单独开新 workflow | 应落入 |
| --- | --- | --- |
| 蓝图小 draft | 不做表格集合 | `short-drama-write` 的 `/plan`，输出 `creative-plan.md` |
| 信息流 / 真相梯度 | 不做散规则 | `/plan` 和 `/outline`，写进每集释放、继续扣住、下一债务 |
| 首批强度目标 | 不做外置 reviewer 兜底 | `/plan` 首批商业密度表 + `/outline` 首批通过标准 |
| 源本强节点适配 | 不新增分析大包，不让 writer 临场补 | `source-import` 产出 `09_源本留存锚点.md`；`/plan` 综合用户需求、新壳、角色、项目目标、目标受众做强节点适配审计；`/outline` 做高压可施工检查；`/review` 查静默降级 |
| 角色设定 / 欲望 / 关系反应 | 不做固定模板 | `/characters` 产出人物功能、阶段状态、关系反应、声线倾向；`/episode` 必须执行 |
| 视听语言 / 人物状态写到戏里 | 不做泛影视技法库 | `/episode` 的场面执行要求：动作、空间、身体、物件、声音、反应链 |
| 去 AI 味 / 台词压缩 | 不允许改剧情 | `/dialogue-polish` 固定执行，只能压表达、声线、潜台词、反应拍，不能改蓝图和事件 |
| reviewer 严格度 | 不做机械禁词 | contract + `/review`：禁可识别组合复刻，不禁通用人名、短句、套路句 |
| callback | 不允许无限回上游 | contract + `/review`：失败回对应责任层，同一问题最多一次上游返修 |
| 交付检查 | 不让 clean reviewer 重审导出稿 | clean reviewer 在 `/export` 前做内容验收；`/delivery-qa` 在 `/export` 后只查漏集、乱序、内部字段泄漏和导出误删 |
| clean run | 不在文件没改完前空跑 | 可执行文件发生实质改动后再跑，并必须留下 `run_log.md` |
| 长剧本 / 60-80 集续写 | 不做首批后的临时补丁 | 从 `/plan` 开始有轻量全剧追踪骨架；首批只吃当前批和本集速记，批次完成后再汇总 `batch-state.md` |

## 本轮要改的文件

1. `README.md`
   - 明确 `shortdrama-remix` 是生产链，不是方法库。
   - 明确三层产品架构和当前下一步。

2. `contracts/short_drama_form_lock_v1.md`
   - 把旧的 `场景施工稿` 口径改成 `分集执行包 / 当前批集纲`。
   - 增加视听语言、人物状态、reviewer callback、去 AI 味权限边界。

3. `skills/source-import/SKILL.md`
   - 源本账本补足信息释放、角色状态压力、视听承载特征。
   - 写稿交接包必须支持蓝图和 writer 执行包，不只支持剧情迁移。
   - 2026-07-05 补充：新增 `09_源本留存锚点.md`，把源本强节点和同级或更优强度目标压成下游强制继承锚点。

4. `skills/short-drama-write/SKILL.md`
   - `/plan` 生成完整商业项目包 / 创作蓝图包，五块都像小 draft。
   - `/plan` 必须完成强节点适配审计，不允许强节点静默降级、删除或待优化承载继续下游。
   - `/characters` 锁住角色功能、欲望、关系反应、阶段状态和声线倾向。
   - `/outline` 变成分集执行包，包含信息释放、角色状态 beat、首批强度目标、强度适配检查和高压可施工检查。
   - `/episode` 强化视听语言、动作反应链和人物状态执行。
   - `/dialogue-polish` 固定执行台词目标、声线差异、潜台词、解释压缩和去 AI 味。
   - `/review` 调整严格度和 callback，不做机械禁词、不无限回上游，并把强节点静默降级列为硬伤。
   - `/export` 后新增 `/delivery-qa` 交付检查；clean reviewer 仍负责 export 前内容验收，不负责排版/清理层。

5. `docs/决策与变更.md`
   - 记录本轮架构对齐。

## 当前不做

- 不开新县城。
- 不新建 v21/v4 workflow。
- 不把外部项目再抽成摘要。
- 不直接修样本文本。
- 不把长线追踪做成重 gate；轻量全剧骨架从 `/plan` 开始，具体接法见 `external_skill_reference_integration_map_2026-07-04.md`。
- 不跑 clean sample，除非本轮可执行文件改完后需要验证实质生成变化。
