# 自动化编剧

这是一个**海外短剧洗稿 workflow 项目**。

当前阶段不是工程实现，也不是网页产品开发阶段。现在做的事很明确：把“已验证源本的有效性”稳定迁移到新壳里，并验证 workflow 跑完后，产物是否真的更像能追、能付费的短剧。

## 当前定位

- 这是一个 **workflow / skill chain / 样本验证** 项目
- 不是从零原创剧本生成器
- 不是 reviewer 驱动的返修机器
- 不是视频分镜工程仓库

## 当前主入口

先看这些文件：

1. [AGENTS.md](./AGENTS.md)
2. [v2-restart/当前工作入口.md](./v2-restart/当前工作入口.md)
3. [v2-restart/项目基础说明.md](./v2-restart/项目基础说明.md)
4. [v2-restart/PRD_v4.md](./v2-restart/PRD_v4.md)
5. [v2-restart/specs/PRD_v4_产品契约_spec_v2.md](./v2-restart/specs/PRD_v4_产品契约_spec_v2.md)
6. [docs/决策与变更.md](./docs/决策与变更.md)
7. [v2-restart/workflow_spec_v20_产品契约编译候选版_2026-07-03.md](./v2-restart/workflow_spec_v20_产品契约编译候选版_2026-07-03.md)
8. [v2-restart/skill_chain_spec_v3_产品契约链候选版_2026-07-03.md](./v2-restart/skill_chain_spec_v3_产品契约链候选版_2026-07-03.md)

## 目录说明

- `v2-restart/`
  - 当前有效的产品定义、产品契约 spec、workflow 候选版、入口文档
- `v2-restart/支撑审计/`
  - 仍可能会查，但不再作为当前第一入口的审计、对账、外部接线材料
- `v2-restart/archive/`
  - 明确降级的旧 PRD、旧 workflow、旧提纲和废案
- `input/`
  - 本地样本源本
- `docs/`
  - 决策记录与项目说明
- `research/`
  - 外部参考与调研
- `analysis/`
  - 分析产物与早期验证材料
- `archive/`
  - 历史废案和不再作为当前方案的旧材料

## 当前工作方式

- 优先修 workflow，不优先磨某一版剧本
- 样本验证是证据，不是最终交付
- `docs/决策与变更.md` 记录阶段判断和重要调整
- 没有验证过的 workflow 不能直接升默认

## 当前已知状态

- `PRD_v4_产品契约_spec_v2` 是当前 PRD 编译源
- `v20` 是当前最新候选 workflow，但尚未通过样本验证升默认
- `v19` 是重要反查对象，但不能继续作为当前直跑源头
- 飞书三星样本与阿尔法样本都已经跑出重要证据
- 当前根因已从“中间层不成戏”上移到“PRD 到 workflow 的编译层会变形，导致用户产物、内部产物和质量责任混在一起”

## 仓库治理约定

- 项目默认使用 `main` 作为稳定分支
- 新的 workflow / 样本验证 / 重构尝试，优先走分支
- 不要把本地 session 噪音、临时上下文或 hook 日志提交进仓库
- 重要判断先写进 `docs/决策与变更.md`

## 现在最重要的问题

不是“能不能写出戏”。

而是：

> workflow 已经能把中间层接成戏了，但还没有稳定把不同源本的首批 1-10 集都拉到足够想让用户继续追、继续付费的强度下限。

进一步收口后，当前先解决：

> PRD 写的是产品形态和创作能力，但编译到 spec / workflow 时容易变成内部字段、gate、reviewer、打回和 S 编号执行合同。当前已编译出 `workflow_spec_v20` 和 `skill_chain_spec_v3`，下一步是先跑飞书三星样本验证。
