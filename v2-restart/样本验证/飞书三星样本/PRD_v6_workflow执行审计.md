# PRD v6 workflow 执行审计

日期：2026-06-30

审计对象：

- `workflow_spec_v2.md`
- `PRD_v5_豪门商战版_写作前工作稿.md`
- `PRD_v6_豪门商战版_首批1-10集.md`
- `PRD_v6_豪门商战版_主控自评.md`

## 结论

V6 没有完整跑完 `workflow_spec_v2.md` 的 0-15 步。

准确说：

- V5 曾经跑过一套写作前工作稿，覆盖了 0-8 的主要中间产物；
- V6 主要是在 V5 的骨架上重出第 9 步 screenplay draft；
- V6 没有重新生成 0-8；
- V6 没有正式跑 10-15；
- V6 的“主控自评”只能算局部作者自评，不能等同于正式 `rewrite report / dialogue polish / quality gate / reviewer / 版本对比`。

所以不能说“workflow 每一步都做到了”。

## 逐步审计

| workflow 步骤 | V6 实际状态 | 判断 |
|---|---|---|
| 0. 最小需求确认 | 沿用 V5：豪门商战、集数不变、中度偏重、首批 1-10 | 沿用，不是 V6 重做 |
| 1. 读源本 | V5 subagent 读过源本；V6 没有重新读完整源本 | 沿用，不是 V6 重做 |
| 2. 源本拆文包 | 存在于 V5 写作前工作稿 | 沿用 |
| 3. 二次需求确认 | 存在于 V5 写作前工作稿，实际没有和用户再次确认新变化 | 部分做到 |
| 4. 洗稿边界包 | 存在于 V5 写作前工作稿 | 沿用 |
| 5. 新本 beat sheet / outline | 存在于 V5 写作前工作稿 | 沿用 |
| 6. 新壳场面迁移卡 | 存在于 V5 写作前工作稿，但没有因 V6 暴露的表演/情绪问题重做 | 沿用且不足 |
| 7. Episode function map | 存在于 V5 写作前工作稿 | 沿用 |
| 8. Scene packet | 存在于 V5 写作前工作稿，但 scene packet 本身对人物状态、表演强度要求不够具体 | 沿用且不足 |
| 9. Screenplay draft | V6 重新输出，消除了内部字段泄漏；后续又补了人物情绪动作 | 做了，但第一轮不足 |
| 10. Rewrite report | 没有按 workflow 输出正式 rewrite report | 未做 |
| 11. Dialogue polish | 没有按 workflow 做逐句台词功能/水词/潜台词 polish | 未做 |
| 12. 作者 quality gate | `PRD_v6_主控自评` 有部分自检，但不是正式 quality gate | 部分做到 |
| 13. Story memory checkpoint | 没有为 V6 更新 story memory checkpoint | 未做 |
| 14. 独立 reviewer quality gate + rewrite report | 没有单开干净 reviewer 审 V6 | 未做 |
| 15. 主控对比 V3 / 上一版 / 本版 | 没有做 V6 vs V5 / V4 / V3 正式对比 | 未做 |

## 根因

这次失败不是 `workflow_spec_v2.md` 里没有这些步骤，而是执行时把“重跑”误缩成了“重跑正文出口”。

也就是说：

```text
应该做：从写作前中间产物到正文后的检查，完整跑一遍。
实际做：沿用 V5 中间产物，只重写 screenplay draft，并做了一个不完整自评。
```

这会导致两个问题：

1. 中间产物里没有被修正的弱点，会继续传导到正文；
2. 正文暴露的问题只能靠用户指出后临时补，无法被 workflow 自己抓住。

## 目前最危险的薄弱点

### 1. Scene packet 对人物状态要求太弱

V5 的 scene packet 写了：

- Action Chain
- Performance / Body / Space
- Dialogue Functions

但它仍然容易被模型理解成：

```text
这里补一点动作；
这里补一点表演；
然后继续写台词。
```

它没有强迫 writer 在高压节点持续写出：

- 人物身体失控；
- 情绪如何改变呼吸、动作、声音；
- 旁人如何被这个状态影响；
- 空间如何压迫角色；
- 台词前后身体状态是否变化。

这就是 V6 第一轮仍然“人物冷静”的直接原因。

### 2. Dialogue polish 根本没跑

用户指出“人物说话太冷静”，这本来应该被第 11 步抓住。

但 V6 没有正式跑 Dialogue polish，所以它没检查：

- 这句台词前角色身体状态是什么；
- 这句台词是不是太完整、太冷静；
- 这句台词是否能被动作替代；
- 每轮对白有没有压力升级；
- 高压节点的人物声音是否变形、打断、失控。

### 3. 作者 quality gate 不够正式

`PRD_v6_主控自评` 更像主控 note，不是 workflow 要的正式 quality gate。

它指出了一些风险，但没有按固定 lenses 全面检查：

- adaptation_fit
- scene_mechanics
- hook_retention
- expression_integrity
- continuity_invariants

### 4. 没有独立 reviewer

V6 还没被干净 reviewer 看过。

所以现在的判断仍然污染在主控自己的上下文里。

## 下一步应该怎么做

不要继续立刻手改正文。

应该从 V6 当前问题反推回 workflow 的实际执行：

1. 先补做 V6 的 `rewrite report`：明确失败层到底是 scene、dialogue、performance 还是 adaptation。
2. 再补做 V6 的 `dialogue polish`：重点查“冷静台词”“水词”“可以用动作替代的台词”。
3. 再补做 V6 的正式 `作者 quality gate`。
4. 然后单开干净 reviewer 审 V6。
5. reviewer 后再决定是否局部改正文。

这不是新增流程。

这是把原本 workflow 里已经写着、但这次没有执行的步骤补上。
