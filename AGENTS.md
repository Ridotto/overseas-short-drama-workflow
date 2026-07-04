# 自动化编剧项目 · Agent 入口说明

默认中文交流。这个项目当前仍在产品流程验证阶段，不是工程实现阶段。

## 当前唯一主链

当前不要再直跑 `v20`、`v3-executor-first`、`V63`，也不要继续把外部短剧方法抽成摘要、检查项或 workflow 字段。

当前主链已经切到：

```text
shortdrama-remix/
```

用户在 Codex 里跑本项目时，普通入口不是旧 workflow，也不是手动记内部 slash command。短剧改写、源本导入、蓝图、首批正文、续批、导出或状态查询请求，先进入项目内主控：

```text
shortdrama-remix/skills/shortdrama-main-controller/SKILL.md
```

进入项目后，先按顺序读：

1. `v2-restart/当前工作入口.md`
2. `v2-restart/项目基础说明.md`
3. `v2-restart/PRD_v4.md`
4. `shortdrama-remix/README.md`
5. `shortdrama-remix/skills/shortdrama-main-controller/SKILL.md`
6. `shortdrama-remix/contracts/short_drama_form_lock_v1.md`
7. `shortdrama-remix/skills/source-import/SKILL.md`
8. `shortdrama-remix/skills/short-drama-write/SKILL.md`
9. `shortdrama-remix/vendor/short-drama/SKILL.md`
10. `shortdrama-remix/vendor/short-drama/references/`
11. `docs/产品架构与主控路由_v1.md`
12. `docs/仓库治理_2026-07-04.md`
13. `docs/决策与变更.md`

`shortdrama-remix/skills/shortdrama-main-controller/SKILL.md`、`shortdrama-remix/skills/source-import/SKILL.md` 和 `shortdrama-remix/skills/short-drama-write/SKILL.md` 是当前可执行文件，不是参考材料。

## 当前产品判断

当前主文档仍是 `v2-restart/PRD_v4.md`。产品目标没有变：

```text
把一个已被市场验证或值得参考的短剧源本，
洗成一个新壳下仍然好看、能追、能付费的新剧本。
```

最新根因判断：

```text
v20/v3 这类 workflow 能把文件跑齐，也能局部增强短剧感，
但它们仍会把外部短剧方法编译成字段、协议、检查项和 reviewer 口径。
真正缺的不是更多 workflow，而是直接执行短剧写作 skill：
源本导入 -> 源本赚钱力账本 -> 新壳迁移 -> 商业项目包 -> 分集目录 -> 分集正文 -> 台词精修。
```

因此当前主链直接使用 `shortdrama-remix`：

- `shortdrama-main-controller` 负责接用户自然语言和 `/rewrite-*` 用户层命令，选择模式、推进确认点、调度生产链和归因返修；
- `source-import` 负责把源本拆成可迁移账本、爽点钩子账本、付费压力、禁抄边界和写稿交接包；
- `short-drama-write` 负责直接按短剧 skill 产出商业项目包、角色、分集目录、分集正文、台词精修和 review；
- `short_drama_form_lock_v1` 负责锁定最终产物必须是短剧，不得滑成电视剧、网剧、小说或泛型 screenplay；
- `vendor/short-drama` 原样保留外部短剧 skill 和 references，后续执行以本地冻结文件为准。

用户层高级命令统一使用：

```text
/rewrite-start
/rewrite-blueprint
/rewrite-write
/rewrite-polish
/rewrite-review
/rewrite-continue
/rewrite-export
/rewrite-status
```

这些只是用户层别名。底层内部命令仍保留 `/write-from-source`、`/plan`、`/characters`、`/outline`、`/episode`、`/dialogue-polish`、`/review`、`/batch-state`、`/export`。

## 降级为历史证据的旧链路

以下内容仍有证据价值，但不再作为当前直跑入口：

- `v3-executor-first/`
- `v2-restart/workflow_spec_v20_产品契约编译候选版_2026-07-03.md`
- `v2-restart/skill_chain_spec_v3_产品契约链候选版_2026-07-03.md`
- `v2-restart/archive/superseded-v19-2026-07-03/`
- `v2-restart/archive/history-pre-v19-2026-07-03/`
- `archive/do-not-use-as-product-design-2026-06-28/`

这些已经从当前 main 工作树清出或降级为历史证据，只能从 Git 历史 / 本地归档追溯失败模式、对比样本和验证旧判断，不能复活成当前方案。

## 当前下一步

当前不要继续修样本文本，不要继续扩 workflow，不要再把外部方法写成“请参考”。

当前下一步：

1. 以 `shortdrama-remix/skills/shortdrama-main-controller/SKILL.md` 作为产品入口；
2. 用自然语言或 `/rewrite-*` 用户层命令触发项目；
3. 主控按需调用 `skills/source-import/SKILL.md` 和 `skills/short-drama-write/SKILL.md`；
4. 正文默认按 `/episode -> /dialogue-polish -> /review` 跑，不跳过台词精修；
5. 每批完成后如需续写，先生成或刷新 `batch-state.md`；
6. 若正文仍弱，必须回到对应可执行步骤或本地 skill 文件本身修改，不得在外层再堆 workflow 摘要。

当前已有验证证据：

```text
V68 clean run 证明新版主链底盘可以产出过线的 EP1-10 短剧样本。
```

具体运行样本不进入新 main；本地保全在 `.local-archive/pre-main-replacement-2026-07-04/shortdrama-runtime/`，GitHub 上以文档证据为准。

## 运行记录规则

任何 agent 只要声称“按当前主链执行”，必须留下本次 `run_log.md`。

run log 至少写清：

- 使用的入口 skill 文件；
- 源本库路径；
- 新剧项目路径；
- 执行到哪个命令；
- 产出了哪些文件；
- 哪些步骤没有做。

没有 run log，只能说“有产物”，不能声称“按当前主链完整执行”。

## Reviewer 原则

Reviewer 仍然每次单开干净临时 agent，不做长期固定工位。

Reviewer 第一轮只读正文和必要的源本 / 洗稿边界，不读作者自检，不读主控结论。

Reviewer 首要问题不是“格式是否齐”，而是：

```text
这是不是短剧？
有没有保住源本让人追、让人付费的能力？
新壳是否洗开？
强刺激有没有被证据、系统、文件、听证会稀释？
```

## 记录规则

重要决策和阶段性结果记录到 `docs/决策与变更.md`。

不要把临时想法、旧方案复活或大段推演继续塞进设计提纲。
