# Goal Run Control

> 对应目标文件：`/Users/jiakun/.codex/attachments/ff212521-6c36-4db3-9711-fc8e20d76f01/goal-objective.md`  
> 日期：2026-06-30  
> 用途：约束本轮 goal 执行，避免自动跑偏、无限扩文档或把中途产物当正式版本。

## 1. 当前轮次

- V9 = goal 第 1 轮真实产出测试。
- V9 已完成：真实剧本、主控自评、6-agent challenge。
- V9 结论：6 个 challenge 均为 `revise`，无 `block`，无 `pass`。
- V9 未达标，不能 complete。
- V10 = goal 第 2 轮产出测试，但 6-agent challenge 中出现执行可靠性 `block`。
- V10 内容稿可以作为后续对比参考，但不能作为“新 agent 已稳定按 workflow 跑通”的合格样本。
- V10 block 原因不是 PRD 或创作流程大方向，而是执行协议失效：`workflow_run_manifest_V10.md` 的文件时间晚于写作前工作稿和正文，不能证明 manifest-first。
- V11 = goal 第 3 轮正式测试，manifest-first 成立，主创侧 workflow 可稳定跑到 partial；6-agent challenge 结论为 2 pass / 4 revise / 0 block。
- V11 未达标，不能 complete。共同 revise 点集中在样本文本第 7-10 集，不是 PRD / workflow / 外部资产复用问题。

误开的 V10 中途产物已隔离到：

`样本验证/飞书三星样本/中断产物/V10_auto_started_then_interrupted_2026-06-30/`

这些文件不算正式版本，不参与后续对比。

## 2. 下一步

正式 V12 = goal 第 4 轮。

正式测试必须先建立 `workflow_run_manifest_V12.md`，再写其他产物。

如果已经写出正文或工作稿但没有 manifest，本次测试无效，产物必须隔离，不能作为正式轮次。

V12 必须解决 V11 的两个层面问题：

### A. 运行协议问题

1. 第一动作只能是建立 `workflow_run_manifest_V12.md` stub；
2. manifest stub 建立后，才能创建写作前工作稿、正文、质量门等产物；
3. 每个步骤完成后必须更新 manifest，不能最终倒补；
4. 若 manifest 创建时间晚于主要产物，本轮直接判 `protocol-fail`；修改时间晚于正文是持续回写的正常结果。

### B. 内容质量问题

V12 只解决 V11 challenge 的共同 revise 点：

1. 修第 7 集：让 Chloe 反咬更一眼懂，减少“合规投诉自动生效”，让 Adrian 必须亲手选择继续压 Serena；
2. 修第 8 集：减少系统/录音宣判感，让 Adrian 用当下动作承接旧罪；
3. 修第 10 集：保留直播认罪和“不原谅”，后半只留一个主钩，避免 trusteeship / Chloe / Marcus 三连发挤压情绪余味；
4. 补 Marcus 伏笔：用无解释动作做关系刺，不提前解释；
5. 补 Serena 少量不可控身体反应，不加原谅或心软；
6. 收紧证据口径：E1-E6 标为复用验证，不写成完整自足 packet；dialogue polish 要么产出修订版正文，要么改为“写作时内化”；
7. 更新 manifest、作者质量门、版本对比；
8. 再开 6 个干净 challenge。

不修改 PRD、设计提纲、workflow，除非 V12 证明当前 workflow 仍然失效。

## 3. 停止条件

每轮结束后必须先归并真实产物和 6-agent challenge，再判断是否继续。

可以停下的情况：

1. 达标：真实剧本达到合格标准，6 个 challenge 无阻塞问题；
2. 跑满：最多 5 轮后仍不合格；
3. 阻塞：反复症状无法靠当前方法继续改；
4. 用户明确要求停止。

不能因为“有 revise”就机械自动下一轮；必须先写清：

- revise 是阻塞还是非阻塞；
- 问题是文档、workflow、中间产物、执行，还是样本文本；
- 是否继续修，为什么。

## 4. 邮件通知

只要本 goal 停下来，无论原因是达标、跑满、blocked 或用户要求停止，都必须发邮件通知。

默认收件人：`nukaij.liu@gmail.com`

邮件至少包括：

- 停止原因；
- 最终状态：pass / revise / blocked / max-rounds / user-stopped；
- 最终版本路径；
- 每轮产物路径；
- 6-agent challenge 总结；
- 剩余风险和下一步建议。

## 5. 轮次上限

最多 5 轮。

当前已消耗：

- 第 1 轮：V9
- 第 2 轮：V10（protocol-fail，内容可参考，不能作为稳定执行样本）
- 第 3 轮：V11（正式执行成立，质量 revise，不能 complete）

剩余：

- 最多 2 轮：V12-V13
