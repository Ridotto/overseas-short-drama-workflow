# short-drama-write local execution copy

本目录是 `shortdrama-remix` 当前主链里的本地执行副本，不是外部 `short-drama` 项目的原始安装说明。

权威执行文件是：

```text
shortdrama-remix/skills/short-drama-write/SKILL.md
```

冻结来源保存在：

```text
shortdrama-remix/vendor/short-drama/
```

不要从这里引导用户安装全局 skill，也不要按外部原项目的 `/start -> 选题立项` 方式运行。本项目是源本驱动洗稿链，必须先有 `source-import` 产出的源本库和 `handoff_to_short_drama_write.md`。

## 当前内部链路

```text
/write-from-source
-> /plan
-> /characters
-> /outline
-> /episode
-> /dialogue-polish
-> /review
-> /batch-state 或 /export
```

用户层入口不在本文件，而在：

```text
shortdrama-remix/skills/shortdrama-main-controller/SKILL.md
```

## 当前责任边界

- `/plan`：生成用户可确认的商业项目包 / 创作蓝图包。
- `/characters`：把角色欲望、关系反应、状态和声线落成可执行输入。
- `/outline`：生成当前批分集执行包，锁住每集赚钱功能、可见代价、信息释放和下一债务。
- `/episode`：写生产工作稿，可保留内部锚点和 `## 状态增量`，但正文结尾不得输出 `钩子：`、`本集钩子`、`下集预告`、`End Hook` 或 `> Next:`。
- `/dialogue-polish`：只做台词、声线、解释压缩、反应拍和去 AI 味，不改剧情事实。
- `/review`：做质量归因，不负责生产剧情。
- `/export`：生成用户交付稿，必须清理内部施工字段、状态增量、台词精修记录、review 痕迹、run log 摘要和 callback 记录。

## 出海模式

出海不是额外用户流程。用户目标市场、平台或输出语言指向出海时，主控自动设置 overseas mode。

`/overseas` 只保留为内部模式标记或旧命令兼容：用户直接输入时，视为“用户确认目标是出海”，随后回到当前生产步骤，不新增一轮切换流程。

本地化策略遵守：

```text
先保护现稿有效点
-> 再识别有证据的适配风险
-> 再给少量高置信建议
-> 用户确认后才进入 outline / episode 执行
```

## 运行证据

每个新剧项目必须有：

```text
run_log.md
```

`run_log.md` 要引用源本库和本次导入的：

```text
源本库/{源名}/_import_log.md
```

没有对应运行日志时，只能说“产物存在，但运行证据缺失”，不能声称按当前主链完整执行。
