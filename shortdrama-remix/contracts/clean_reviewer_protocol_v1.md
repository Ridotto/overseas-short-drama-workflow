# Clean Reviewer Protocol v1

## 目的

clean reviewer 用来判断 polish 后的剧本内容是否真的过线，不负责继续写戏，不负责替主控证明之前判断正确，也不负责导出排版检查。

它的价值在于第一眼相对干净：先看产物和必要输入，再给 verdict；不能先读作者自评、主控表扬、历史 pass 结论或返修理由。

clean reviewer 的默认位置是 `/dialogue-polish` 和 `/export` 之间。`/export` 之后如果还需要检查，只做 delivery QA / export lint：查漏集、乱序、内部字段泄漏、元信息和排版完整性，不重新判断剧情好不好。

## 允许读取

clean reviewer 第一轮可以读取：

- 当前待审正文，默认读已 polish 的 `episodes/` 或用户指定的待审剧本文字。
- `creative-plan.md`
- `characters.md`
- `episode-directory.md`
- `source-handoff.md`
- `07_禁抄边界.md`
- `09_源本留存锚点.md`
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
- 洗稿边界是否通过；
- 源本强节点是否完成综合适配并达到同级或更优，是否存在静默降级、删除或证据/流程替代强戏；
- 出海/平台适配是否按已确认策略执行；
- `run_log.md` 是否足以证明当前链路执行过。

内容层通过不等于最终交付通过；最终交付通过还需要 `/export` 后的 delivery QA / export lint。delivery QA 只查交付文件是否干净完整，不推翻 clean reviewer 的内容 verdict，除非发现 export 误删、漏集或污染导致用户可见稿已经不是被验收过的内容。

## 不做什么

- 不新增剧情。
- 不替 writer 现场修正文。
- 不把台词小毛病升级成蓝图失败。
- 不把没有证据的本地化偏好包装成硬伤。
- 不因为常见人名、常见短句或短剧套路句就判复刻；必须看是否组成高识别表层组合。
