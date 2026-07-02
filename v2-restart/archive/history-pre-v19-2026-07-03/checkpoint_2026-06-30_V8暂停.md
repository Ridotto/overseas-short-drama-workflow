# 自动化编剧项目 checkpoint：V8 暂停

日期：2026-06-30

## 1. 当前状态

当前项目暂停。

不要继续修 V8，不要自动开 V9，不要继续补丁式修改 workflow。

V8 已按修正后的 `PRD_v4.md + workflow_spec_v2.md + workflow_execution_protocol_v1.md` 跑完，manifest 状态为 `complete`，但这只能说明流程被完整执行，不代表项目已经解决“稳定写出好短剧”的核心问题。

用户判断：继续修下去收益很低，当前先封存状态。

## 2. 当前主文档

- `项目基础说明.md`
- `PRD_v4.md`
- `workflow_spec_v2.md`
- `workflow_execution_protocol_v1.md`
- 本 checkpoint

`设计提纲_v8.md` 仍只作为历史设计推演和规则池，不作为当前执行入口。

## 3. V8 产物

目录：

`v2-restart/样本验证/飞书三星样本/`

主要文件：

- `workflow_run_manifest_V8.md`
- `PRD_v8_豪门商战版_写作前工作稿.md`
- `PRD_v8_豪门商战版_首批1-10集.md`
- `PRD_v8_豪门商战版_rewrite_report_dialogue_polish.md`
- `PRD_v8_豪门商战版_作者质量门.md`
- `PRD_v8_豪门商战版_story_memory_checkpoint.md`
- `PRD_v8_豪门商战版_reviewer输入包.md`
- `PRD_v8_豪门商战版_独立reviewer审稿.md`
- `PRD_v8_豪门商战版_版本对比.md`

## 4. 对 V8 的主控判断

V8 是当前几版里相对最好的一版，但不是终稿，也不能作为项目成功证据。

相对进步：

- 第 2 集补上 Adrian 当场拒绝医疗例外的可见动作；
- 第 7-8 集从纯证据播报改善为信托台、胸针摘除、账户冻结、担保键、CEO key、权限卡变灰等可见动作；
- 第 9-10 集的托管箱、胎心音、公开认罪、“听见了但不原谅”较稳定。

主要残余问题：

- 第 7-8 集仍偏公司系统戏，`信托台 / rescue token / CEO key / legal hold / referral` 等机制理解成本较高；
- 连续 boardroom 空间仍有会议戏风险；
- 人物情绪和身体状态比旧版强，但整体还不够成熟短剧的直观、外放和自然；
- workflow 能让产物比旧版更完整，但没有证明它能稳定产出高质量短剧。

## 5. 当前禁止事项

在用户没有重新明确要求前：

- 不继续修 V8；
- 不自动生成 V9；
- 不继续扩 PRD；
- 不继续扩设计提纲；
- 不继续把导演反馈拆成更多规则；
- 不把 V8 reviewer 的 `pass` 当成导演可接受或产品成功。

## 6. 如果之后恢复

恢复时先问清用户想走哪条路：

1. 等导演反馈；
2. 放弃当前豪门商战样本继续修，改用别的样本；
3. 暂停写作实验，只回头重审 workflow 是否值得保留；
4. 直接把现有项目里成熟的剧本/对白/场面合同抽出来，重建一个更小的 skill，而不是继续沿着 V8 打补丁。

恢复前必须先读本 checkpoint。

