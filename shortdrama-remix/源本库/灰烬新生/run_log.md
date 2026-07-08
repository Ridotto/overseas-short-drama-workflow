# run_log

## 2026-07-05 导演版前10集重校准

- 任务：按导演版 `灰烬新生_第3-9集分集大纲_调整版(1).docx` 和 `灰烬新生_前10集短剧结构反思报告.docx` 重做当前业务链路文档，不改程序。
- 输入：导演满意版 EP3-9；导演反思报告；现有灰烬新生源本导入包。
- 处理边界：EP3-9 不擅自改导演结构；EP1-2 按用户与导演确认方向重排为旧案污名/婚约倒计时、救命钱到账/Celeste 当前夺功。
- 关键决策：导演版名字若不撞原稿可沿用；若与原稿一模一样必须替换。Harrington 与源稿新家撞名，当前新家继续使用 `Ashford`；EP5 芒果/酒精过敏按导演版保留。
- 已更新：`00_导入说明.md`、`01_源本有效性摘要.md`、`02_集级事件账本.md`、`03_人物功能账本.md`、`04_爽点钩子账本.md`、`05_付费点与追更压力.md`、`06_可迁移结构.md`、`07_禁抄边界.md`、`08_新壳迁移建议.md`、`09_40集商业蓝图.md`、`handoff_to_short_drama_write.md`。
- Active writer 输入：`09_40集商业蓝图.md`、`handoff_to_short_drama_write.md`、`07_禁抄边界.md`；需要方向追溯时再读 `08_新壳迁移建议.md`。

## 2026-07-05 上下游一致性复核

- 任务：确认 EP3-9 分集执行纲与导演满意版一致，并同步上游账本、迁移建议、禁抄边界和 handoff，避免 writer 看到冲突规则。
- 调整：`09_40集商业蓝图.md` 的 EP3-9 进一步贴近导演版分集文本；`02_集级事件账本.md` 补齐 EP8 捡回药膏到病体下楼的连续动作；`07_禁抄边界.md` 和 `handoff_to_short_drama_write.md` 把芒果/酒精过敏从拦截项改为导演版可保留项。
- 污染控制：`10_EP1-3_english_sample.md` 标为旧样章、非当前执行输入。
- 复核结论：当前 active 输入仍是 `09_40集商业蓝图.md`、`handoff_to_short_drama_write.md`、`07_禁抄边界.md`；旧账本只作源稿证据，不是 writer 默认输入。
- 二次清理：把 `01_源本有效性摘要.md`、`02_集级事件账本.md`、`04_爽点钩子账本.md`、`06_可迁移结构.md`、`07_禁抄边界.md`、`handoff_to_short_drama_write.md` 里残留的“芒果需换表层”旧口径改为“当前导演版可保留，禁止照搬原调度台词”；`10_EP1-3_english_sample.md` 的非当前说明移到文件开头。

## 2026-07-05 正常链路执行 EP1-10

| 环节 | 输入 | 输出 | 结论 |
| --- | --- | --- | --- |
| `/write-from-source` | `handoff_to_short_drama_write.md`、`09_40集商业蓝图.md`、`07_禁抄边界.md` | `source-handoff.md`、`.drama-state.json` | 以当前导演版业务包作为 active handoff，未把旧样章当输入。 |
| `/plan` | `source-handoff.md`、`09_40集商业蓝图.md` | `creative-plan.md` | 不重判方向；锁定 TikTok 女频、40 集、50 年代轻皮肤、EP1-10 倒计时虐点链。 |
| `/characters` | `creative-plan.md` | `characters.md` | 明确 Evelyn 前 10 集为包子小白花；Celeste 是 ward/golden child；旧家自以为合理。 |
| `/outline` | `creative-plan.md`、`characters.md` | `episode-directory.md` | EP1-2 按导演确认方案重排；EP3-9 对齐导演满意版；EP10 做接走切割。 |
| `/episode 1-10` | `episode-directory.md` | `episodes/ep001.md` 到 `episodes/ep010.md` | 已生成 EP1-10 英文正文工作稿。 |
| `/dialogue-polish 1-10` | `episodes/_drafts/*_pre_dialogue_polish.md` | `episodes/ep001.md` 到 `episodes/ep010.md`、`dialogue-polish_EP1-10.md` | 只做低风险 polish；修正 EP1 年龄/钥匙牌画面逻辑，避免过度文学化。 |
| `/review 1-10` | `episodes/ep001.md` 到 `episodes/ep010.md` | `review/review_EP1-10.md` | 通过。建议不回蓝图重做，只在导演/用户复核后做局部压缩或加压。 |
| `/batch-state` | `review/review_EP1-10.md`、EP1-10 状态增量 | `batch-state.md`、`.drama-state.json` | 已记录 EP10 后人物状态、未偿还债务和 EP11-20 禁区。 |
| `/export` | `episodes/ep001.md` 到 `episodes/ep010.md` | `export/EP1-10_clean_scripts.md` | 已生成去掉内部状态/Polish Notes 的清洁阅读版。 |

验证说明：本轮正文不使用 `10_EP1-3_english_sample.md`；该文件仍为旧样章/非当前输入。最终给外部阅读时优先看 `export/EP1-10_clean_scripts.md`。

## 2026-07-06 中文最终剧本导出

- 任务：基于 EP1-10 英文清洁版生成中文版最终剧本，供中文审稿/导演阅读。
- 输入：`export/EP1-10_clean_scripts.md`。
- 输出：`export/EP1-10_中文最终剧本.md`。
- 处理边界：不改英文正文、不改蓝图、不改人物状态；保留 Evelyn、Celeste、Ashford、Whitmore 等英文人名/家族名，正文和对白转为中文。
- 验证：已检查中文版无 `状态增量`、`Dialogue Polish Notes`、`Commercial Function`、`Visible Stimulus Action`、`Hook Type` 等内部施工标签；无 `Harrington`、`Twelve-year-old`、`registration tag` 残留。

## 2026-07-07 writer 输入契约真实项目 rerun（/episode only）

- 任务：验证“收窄 writer 直读输入面”后，真实项目 EP2 的首稿是否比旧稿更像人在场上说话。
- 处理方式：不覆盖现有 `episodes/ep002.md`；只在 `episodes/_drafts/` 下生成本次 rerun。
- 直读输入：`characters.md`、`episode-directory.md`、EP1 已释放状态，外加按当前 `short-drama-write/SKILL.md` 点名读取的外部原文资产。
- 明确不直读：`creative-plan.md` 全文、`source-handoff.md` 全文、整套账本/审计包。
- 输出：
  - `episodes/_drafts/ep002_writer_direct_packet_2026-07-07.md`
  - `episodes/_drafts/ep002_writer_contract_rerun_2026-07-07.md`
- 验证口径：只看 `/episode` 首稿，不看 `/dialogue-polish`，不把 review 当首稿质量来源。
- 当前判断：这轮 rerun 的首稿更收、更像活人，公开夺功的压力也更集中；但这 still 只是 `/episode` 首稿验证，不等于整条商业交付链已经自动追平商业稿。

## 2026-07-07 writer 输入契约真实项目 rerun（EP3 / /episode only）

- 任务：继续验证同一真实项目在连续集数上是否也能受益于新的 writer 输入契约，而不是只对单个 scene 有效。
- 处理方式：不覆盖现有 `episodes/ep003.md`；只在 `episodes/_drafts/` 下生成本次 rerun。
- 直读输入：`characters.md`、`episode-directory.md`、本次 EP2 rerun 已释放状态，外加当前 `short-drama-write/SKILL.md` 点名的外部原文资产。
- 明确不直读：`creative-plan.md` 全文、`source-handoff.md` 全文、整套账本/审计包。
- 输出：
  - `episodes/_drafts/ep003_writer_direct_packet_2026-07-07.md`
  - `episodes/_drafts/ep003_writer_contract_rerun_2026-07-07.md`
- 验证口径：只看 `/episode` 首稿，不看 `/dialogue-polish`，重点看“亲情遗物和家庭位置被夺”是否写成可见场面，而不是解释摘要。
- 当前判断：EP3 rerun 也延续了这轮改法的优点，冲突更集中在胸针、站位和资格分配上；说明它不是只对 EP2 单点生效。

## 2026-07-07 writer 输入契约真实项目 rerun（EP4 / /episode only）

- 任务：继续验证这轮改法对另一类虐点是否也稳定生效，不只会写“公开夺功”或“遗物被夺”，还要能处理“被忽视 + 生日落空 + 主动压回真相”。
- 处理方式：不覆盖现有 `episodes/ep004.md`；只在 `episodes/_drafts/` 下生成本次 rerun。
- 直读输入：`characters.md`、`episode-directory.md`、本次 EP3 rerun 已释放状态，外加当前 `short-drama-write/SKILL.md` 点名的外部原文资产。
- 明确不直读：`creative-plan.md` 全文、`source-handoff.md` 全文、整套账本/审计包。
- 输出：
  - `episodes/_drafts/ep004_writer_direct_packet_2026-07-07.md`
  - `episodes/_drafts/ep004_writer_contract_rerun_2026-07-07.md`
- 验证口径：只看 `/episode` 首稿，不看 `/dialogue-polish`，重点看“被忽视”和“主动压回真相”是否也能落成可见动作和关系变化。
- 当前判断：EP4 rerun 也成立。它不靠硬冲突台词撑，而是靠花、蛋糕、礼服、笑声、掉出来的 Ashford envelope 和 Wilson 被拦住这几个东西，把痛感落出来了。

## 2026-07-07 writer 输入契约真实项目专项测试（EP5 中文商业稿对照）

- 任务：不再继续泛测集型，而是回到用户最关心的“高压场景台词火气”问题，拿用户此前给过的中文商业稿做直接对照。
- 商业稿基准：`/Users/jiakun/Downloads/[修改版]灰烬新生.docx` 中 `第五集` 的芒果蛋糕逼吃段落。
- 处理方式：不跑整集，只抽当前链路里最可比的 `EP5 芒果蛋糕逼吃` 场景，生成中文 `/episode` 首稿，不看 `/dialogue-polish`。
- 输出：
  - `episodes/_drafts/ep005_writer_direct_packet_zh_benchmark_2026-07-07.md`
  - `episodes/_drafts/ep005_writer_contract_rerun_zh_2026-07-07.md`
  - `review/ep005_vs_commercial_benchmark_2026-07-07.md`
- 结论：当前版本在人话感和角色分声线上优于旧英文稿，但对比商业稿，仍欠“辱感 / 火气 / 当场踩人的狠度”；尚不能声称达到或超过商业稿线。

## 2026-07-07 Phase 1.5 /episode-debug 5 no-fallback proof

- 任务：把 Phase 1 的链路定义推进到“当前样本真的能基于新 schema 跑出 no-fallback compile-only 证据”。
- 范围：只做 `episode-directory.md` 当前批 schema backfill + EP4/EP5/EP6 相关集段；不重写剧情，不生成新成稿。
- 允许上游输入（schema backfill 阶段）：`creative-plan.md`、`batch-state.md`、旧 `episode-directory.md`、已确认正文状态增量。
- 禁止 `/episode-debug` 输入：`creative-plan.md` 全文、`source-handoff.md` 全文、`09_源本留存锚点.md`、`opening-rules.md`、`rhythm-curve.md`、`satisfaction-matrix.md`、`hook-design.md`、外部 raw assets。
- 输出：
  - `episode-directory.md` 当前批头部 + EP4/EP5/EP6 新 schema backfill
  - `_debug/ep005_episode_working_memo_no_fallback_2026-07-07.md`
  - `_debug/ep005_scene_decision_packet_no_fallback_2026-07-07.md`
  - `_debug/ep005_writer_decision_summary_no_fallback_2026-07-07.md`
- 旧 `_debug/ep005_*_2026-07-07.md` 已标记为 legacy / fallback / not accepted as Phase 1.5 proof。

## 2026-07-07 Phase 3 /episode EP5 受控 rerun

- 任务：只用 Phase 1.5 通过后的 allowlist + Phase 2 kernel，重跑 EP5 中文高压场景，验证 `/episode` 本身的成稿质量。
- `/episode` 默认输入：
  - `series-state-brief.md`
  - `dialogue-force-brief.md`
  - `performance-dialogue-brief.md`
  - `characters.md`
  - `episode-directory.md`
- `episode-directory` 只读取：
  - 当前批执行包头部
  - EP5 writer 直读区
  - EP5 系统校验区
  - 必要 EP4 状态
  - 必要 EP6 债务 / 钩子约束
- 禁止输入：
  - `creative-plan.md`
  - `source-handoff.md`
  - `09_源本留存锚点.md`
  - `opening-rules.md`
  - `rhythm-curve.md`
  - `satisfaction-matrix.md`
  - `hook-design.md`
  - 外部 raw assets
- 输出：
  - `episodes/_drafts/ep005_phase3_rerun_zh_2026-07-07.md`
  - `_debug/ep005_episode_working_memo_phase3_no_fallback_2026-07-07.md`
  - `_debug/ep005_scene_decision_packet_phase3_no_fallback_2026-07-07.md`
  - `_debug/ep005_writer_decision_summary_phase3_no_fallback_2026-07-07.md`
  - `_debug/ep005_phase3_comparison_2026-07-07.md`
- 结果：no-fallback；未调用 `/dialogue-polish` 或 `/review`；保留 source facts、EP4 承接、EP6 未偿债务与商业钩子。
