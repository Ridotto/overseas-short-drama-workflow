# Workflow Run Manifest：EP8 Writer 层重接单集验证

本 manifest 只记录一次单集诊断，不代表完整 workflow 跑通。

## Run Metadata

- Run ID：EP8-writer-reconnect-2026-07-01
- 样本：飞书三星样本 / 豪门商战版
- 使用主流程：不完整跑主流程；沿用 V24 上游材料，单独替换 writer 写作方式
- 测试集：Episode 8
- 是否改 PRD：否
- 是否改当前默认 workflow：否

## 输入材料

- V24 正文：`PRD_v24_refactor_v12_豪门商战版_首批1-10集.md`
- V24 分集追问：`PRD_v24_refactor_v12_Episode_Pursuit_Directory.md`
- V24 场面承载：`PRD_v24_refactor_v12_Scene_Carrier_Pack.md`
- V24 Writer Brief：`PRD_v24_refactor_v12_Playable_Writer_Brief.md`
- V5 强度参照：`PRD_v5_豪门商战版_首批1-10集.md`
- 短剧手艺参照：
  - `hook-design.md`
  - `rhythm-curve.md`
  - `satisfaction-matrix.md`

## 本次执行步骤

| Step | 动作 | 产物 | 状态 |
|---|---|---|---|
| 1 | 收拢 EP8 上游输入，不改上游 | `01_EP8_上游输入包_不改.md` | pass |
| 2 | writer 先写单集短剧施工稿 | `02_EP8_writer短剧施工稿.md` | pass |
| 3 | writer 从施工稿写新 EP8 正文 | `03_EP8_新正文_施工稿驱动版.md` | pass |
| 4 | 对比 V24 / V5 / 新 EP8 | `04_EP8_对比判定.md` | pass |
| 5 | 判断是否值得写候选 workflow | `workflow_spec_v13_writer层重接候选版.md` | pass |

## 本次结论

单集验证显示：writer 先写短剧施工稿，再写正文，比直接从规格写正文更能保住现场压迫、人物动作、关系变化和卡点。

这不是正式验收，只是支持新增候选 workflow。正式化前仍需要完整首批样本验证。
