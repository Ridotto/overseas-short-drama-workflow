# Clean Reviewer Protocol v1

## 目的

clean reviewer 用来判断当前产物是否真的过线，不负责继续写戏，也不负责替主控证明之前判断正确。

它的价值在于第一眼相对干净：先看产物和必要输入，再给 verdict；不能先读作者自评、主控表扬、历史 pass 结论或返修理由。

## 允许读取

clean reviewer 第一轮可以读取：

- 当前待审正文，优先读 `export/` 里的用户交付稿；如果还没导出，读已 polish 的 `episodes/`，但必须标注“交付层未审”。
- `creative-plan.md`
- `characters.md`
- `episode-directory.md`
- `source-handoff.md`
- `07_禁抄边界.md`
- `short_drama_form_lock_v1.md`
- `run_log.md`，只用于确认链路证据是否存在，不用于提高质量判断。

## 禁止先读

clean reviewer 第一轮 verdict 前不得读取：

- 作者自检报告；
- 主控对本稿的质量结论；
- 之前 clean review 的 pass/fail 结论；
- 用户或 agent 对样本的表扬；
- 为了修稿写的局部补丁说明。

如已读到这些内容，必须在报告里说明“不是严格 clean review”。

## 必须分开判断

报告必须分清：

- 内容层是否通过；
- 交付呈现层是否通过；
- 洗稿边界是否通过；
- 出海/平台适配是否按已确认策略执行；
- `run_log.md` 是否足以证明当前链路执行过。

内容层通过不等于最终交付通过；最终交付通过必须以 `/export` 后的用户可见稿为依据。

## 不做什么

- 不新增剧情。
- 不替 writer 现场修正文。
- 不把台词小毛病升级成蓝图失败。
- 不把没有证据的本地化偏好包装成硬伤。
- 不因为常见人名、常见短句或短剧套路句就判复刻；必须看是否组成高识别表层组合。
