# workflow run manifest

任务：用 `workflow_spec_v3_重构草案.md` 跑同一豪门商战样本的完整验证流程，并与 V3 / V8 / V12 对比  
版本：V13-v3workflow  
日期：2026-06-30  
执行 agent：Codex 主控 / 主创  
使用的产品定义：`v2-restart/PRD_v4.md`  
使用的 workflow spec：`v2-restart/workflow_spec_v3_重构草案.md`  
使用的执行协议：`v2-restart/workflow_execution_protocol_v1.md` 的 manifest-first / 证据留存原则；步骤表按 v3 草案 0-14 重排  
输入源本：`v2-restart/样本验证/飞书三星样本/[修改版] 黑手党少主痛哭求原谅_前妻她杀疯了.txt`  
目标新壳：海外豪门商战 / 家族企业权力斗争  
目标市场：海外短剧  
集数：不变  
输出范围：首批 1-10 集  
改写力度：中度偏重；不能只是换名，也不能丢源本有效性  

## 总状态

- 当前状态：complete
- 说明：本轮按 `workflow_spec_v3_重构草案.md` 的验证流程完成。`complete` 只表示本轮步骤和证据闭合，不表示导演终稿。
- creative_status：creative_pass with local notes
- source_audit_status：source_audit_pass
- delivery_status：not director-final，建议局部修稿后再送导演

## 步骤证据表

| Step | 名称 | 状态 | 输入证据 | 输出证据 | Gate 判断 | 备注 |
|---|---|---|---|---|---|---|
| 0 | 最小需求确认 | pass | `当前样本测试夹具.md` + 用户本轮要求“拿新版跑完整流程，同样的内容要求” | 本 manifest 头部 | pass：豪门商战、集数不变、首批 1-10、中度偏重、对比 V3/V8/V12 已明确 | 同一内容要求已继承 |
| 1 | 源本分析底稿 Source Bible | pass | 源本 1-10 集，行 57-317 | `PRD_v13_v3workflow_Source_Bible.md` | pass：列出首批体验链、每集追问、强场面来源、不能机械继承项 | 分析底稿不直接给 writer 当 prompt |
| 2 | 洗稿边界包 Adaptation Boundary | pass | Source Bible + `当前样本测试夹具.md` | `PRD_v13_v3workflow_Adaptation_Boundary.md` | pass：区分强继承体验、替换外形、禁止写法、允许辅助工具 | 用于审计线 |
| 3 | 高压节点新场面粗验 | pass | Source Bible + Boundary | `PRD_v13_v3workflow_HighPressure_Scene_Viability.md` | pass：开局、不可逆损失、回归、7-8 集揭谎、10 集终钩均做新壳承载粗验 | 先验场面发动机 |
| 4 | 新本阶段骨架 / 分集功能 | pass | Boundary + 高压节点粗验 | `PRD_v13_v3workflow_Episode_Plan_Writer_Brief.md` | pass：1-10 集均有开场钩子、摩擦、高压落点、结尾按钮 | 控制 1-10 集留存闭环 |
| 5 | Writer Brief 写作简报 | pass | Episode Plan | `PRD_v13_v3workflow_Episode_Plan_Writer_Brief.md` 第 5 节 | pass：给 writer 的是薄 brief，没有 source ref 表、manifest、版本对比、reviewer 意见 | writer 不读审计证明链 |
| 6 | 干净 writer 正文 Screenplay Draft | pass | `PRD_v13_v3workflow_Episode_Plan_Writer_Brief.md` | `PRD_v13_v3workflow_豪门商战版_首批1-10集.md` | pass：1-10 集正文已完成；Episode 2 / 7 / 8 / 10 有高压场面锚点 | 输出 1-10 集正文 |
| 7 | 作者 rewrite report | pass | Screenplay Draft | `PRD_v13_v3workflow_rewrite_report_dialogue_polish.md` | pass：报告明确指出解决点、未解决风险和返修入口 | 定位失败层，不写泛泛自夸 |
| 8 | 作者 dialogue polish / 修订稿 | pass | Draft + rewrite report | `PRD_v13_v3workflow_rewrite_report_dialogue_polish.md` + 正文 Episode 6 修订 | pass：说明本轮写作时内化 dialogue polish，并实际修订 Episode 6 内部心理句为闪回画面 | 未另出修订稿，正文文件即当前修订稿 |
| 9 | 作者 ready check | pass | 修订稿 | `PRD_v13_v3workflow_author_ready_check.md` | pass：作者判定 ready for reviewer，且未自称最终通过 | 不等同 reviewer |
| 10 | Reviewer 第一轮：只读正文 | pass | `PRD_v13_v3workflow_豪门商战版_首批1-10集.md` + `当前样本测试夹具.md` | `PRD_v13_v3workflow_reviewer_round1_只读正文.md` | pass：reviewer 结论 `creative_pass`，但列局部返修建议 | 不先读作者自检，不读源本分析 |
| 11 | Reviewer 第二轮：读审计底稿 | pass | Source Bible + Boundary + HighPressure + Writer Brief + 正文 | `PRD_v13_v3workflow_reviewer_round2_源本审计.md` | pass：reviewer 结论 `source_audit_pass`，局部问题不构成退回大改 | 查洗飞 / 同构 / 降级 |
| 12 | 主控判定失败层和回滚点 | pass | 作者自检 + reviewer 两轮 + 版本对比 | `PRD_v13_v3workflow_主控判定.md` | pass：判定 V13 是当前正向样本，但不是导演终稿；建议局部修稿，不改 workflow | 判断是否可交付或需回滚 |
| 13 | Story memory checkpoint | pass | 当前稿 | `PRD_v13_v3workflow_story_memory_checkpoint.md` | pass：记录关系、信息差、伏笔、未兑现承诺、禁止提前消费和下一批入口 | 保存后续批次状态 |
| 14 | Manifest / 版本记录 / 交付 | pass | 当前全部产物 + V3 / V8 / V12 | `PRD_v13_v3workflow_vs_v3_v8_v12_整体对比.md` + 本 manifest | pass：整体对比已完成，且没有替代 reviewer；已明确 V13 不等同导演终稿 | 对比旧版，不能用版本对比替代 reviewer |

## 未完成步骤

无。

## 仍不建议直接交付导演的原因

- Reviewer 两轮均通过，但均指出局部返修点；
- 第 7 集亲子爆雷触发偏硬；
- 第 6 / 9 集旧物出现偏方便；
- 第 1 集商业术语略密；
- 第 10 集纸面投降可继续压缩。

## 本轮产物清单

- `PRD_v13_v3workflow_Source_Bible.md`
- `PRD_v13_v3workflow_Adaptation_Boundary.md`
- `PRD_v13_v3workflow_HighPressure_Scene_Viability.md`
- `PRD_v13_v3workflow_Episode_Plan_Writer_Brief.md`
- `PRD_v13_v3workflow_豪门商战版_首批1-10集.md`
- `PRD_v13_v3workflow_rewrite_report_dialogue_polish.md`
- `PRD_v13_v3workflow_author_ready_check.md`
- `PRD_v13_v3workflow_reviewer_round1_只读正文.md`
- `PRD_v13_v3workflow_reviewer_round2_源本审计.md`
- `PRD_v13_v3workflow_story_memory_checkpoint.md`
- `PRD_v13_v3workflow_vs_v3_v8_v12_整体对比.md`
- `PRD_v13_v3workflow_主控判定.md`
