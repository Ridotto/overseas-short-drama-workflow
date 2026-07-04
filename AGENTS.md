# 自动化编剧 next 分支 · 开发接手说明

默认中文交流。当前目录是：

```text
/Users/jiakun/Codex/自动化编剧-next
```

当前分支是：

```text
codex/next
```

这个 worktree 不是用户正式版。它是后续开发、治理、素材保留和实验整合区。

正式版在：

```text
/Users/jiakun/Codex/自动化编剧
```

正式版分支是：

```text
main
```

## 分支边界

- `main`：用户正式版，只保留能让新用户 clone 后直接使用的产品包。
- `codex/next`：开发版，保留旧文档、外部参考审计、架构判断、历史失败证据和后续治理素材。
- `codex/issue-*`：单个 issue 修复。
- `codex/feature-*`：单个功能实验。

不要把 `codex/next` 里的开发素材直接塞回 `main`。只有成熟、稳定、对新用户有用的内容，才通过明确提交合回 `main`。

## 开发入口

进入本 worktree 后，先读：

1. `docs/开发接手入口.md`
2. `docs/项目状态地图_2026-07-04.md`
3. `docs/决策与变更.md` 的最新段落
4. `shortdrama-remix/README.md`
5. `shortdrama-remix/skills/shortdrama-main-controller/SKILL.md`
6. `shortdrama-remix/skills/source-import/SKILL.md`
7. `shortdrama-remix/skills/short-drama-write/SKILL.md`

需要产品定义时，再读：

```text
v2-restart/PRD_v4.md
v2-restart/项目基础说明.md
```

需要追溯外部参考接入时，再读：

```text
shortdrama-remix/external_skill_reference_integration_map_2026-07-04.md
shortdrama-remix/external_reference_minimum_audit_2026-07-04.md
shortdrama-remix/architecture_alignment_checkpoint_2026-07-04.md
```

## 当前产品方向

产品目标不变：

```text
把一个已被市场验证或值得参考的短剧源本，
洗成一个新壳下仍然好看、能追、能付费的新剧本。
```

当前主链仍是：

```text
shortdrama-remix/
```

用户层入口是：

```text
shortdrama-remix/skills/shortdrama-main-controller/SKILL.md
```

底层执行链：

```text
source-import
-> short-drama-write /write-from-source
-> /plan
-> /characters
-> /outline
-> /episode
-> /dialogue-polish
-> /review
-> clean reviewer when needed
-> /batch-state or /export
```

## 开发原则

- 先判断问题属于产品形态、主控路由、源本导入、写作链、台词精修、reviewer、续批状态，还是用户文档。
- 不要为了一个样本继续打补丁；要改就改链路中真正负责的文件。
- 外部参考不能作为“建议参考”丢给 agent，必须变成可执行步骤、writer 必吃输入、reviewer 边界或用户确认物。
- 不要复活旧 workflow 作为主入口。旧链路只能当证据、素材或失败模式。
- clean run 结论必须和样本修稿分开；不要把人工救稿当成主链能力。
- 所有声称“按当前主链执行”的运行都必须留下 `run_log.md`。

## 旧文档使用规则

旧文档有价值，但不能无脑继承。

- `docs/项目状态地图_2026-07-04.md`：用来理解多线程、多 worktree、多方案的最终判断。
- `docs/决策与变更.md`：用来追溯为什么走到当前主链，尤其是失败原因和已验证结论。
- `shortdrama-remix/external_skill_reference_integration_map_2026-07-04.md`：用来查哪些外部参考已经读过、接过、拒绝过。
- `shortdrama-remix/architecture_alignment_checkpoint_2026-07-04.md`：用来防止上下文压缩后忘记视听语言、长线状态、首批强度、reviewer 和 callback 的落点。
- `docs/仓库治理_2026-07-04.md`：只用于理解 main / next / archive 的治理边界。

这些文档不能直接复制进 `main`。如果要把其中结论产品化，必须重写成正式版用户文档、主控规则或执行 skill。

## 发布规则

在 `codex/next` 里开发完成后：

1. 先在 next 内验证。
2. 把真正成熟的变更整理成小提交。
3. 确认不会把旧素材、审计、历史状态地图带入正式版。
4. 再合回 `main`。

默认不要在 `main` 上做实验。
