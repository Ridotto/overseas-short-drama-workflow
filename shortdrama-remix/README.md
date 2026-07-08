# shortdrama-remix

这是当前短剧改写产品的生产目录。

用户入口不在这里，而在仓库根目录和主控：

```text
AGENTS.md
skills/shortdrama-main-controller/SKILL.md
```

本目录负责把用户确认后的源本、方向和蓝图变成可执行产物。

## 目录结构

```text
contracts/
  short_drama_form_lock_v1.md
skills/
  shortdrama-main-controller/
  source-import/
  short-drama-write/
源本库/
新剧/
```

## 执行文件

- `skills/shortdrama-main-controller/SKILL.md`：用户意图路由、确认点、状态查询和返修归因。
- `skills/source-import/SKILL.md`：源本导入、赚钱力账本、禁抄边界和写稿交接包。
- `skills/short-drama-write/SKILL.md`：创作蓝图、角色、分集目录、正文、台词精修、review、续批状态和导出。
- `contracts/short_drama_form_lock_v1.md`：短剧形态锁。
- `contracts/clean_reviewer_protocol_v1.md`：clean reviewer 的读取边界和 verdict 分层。

## 默认链路

```text
source-import
-> short-drama-write /write-from-source
-> /plan
-> /characters
-> /outline
-> /episode
-> /dialogue-polish
-> /review
-> clean reviewer 内容验收
-> /batch-state or /export
-> /delivery-qa
```

关键执行口径：

- `/episode` 不全文回流 `creative-plan.md`；当当前项目存在由 `/plan` 生成、并已作为用户确认蓝图使用的 `creative-plan.md` 时，只抽取当前批 / 当前集所需的 blueprint slice。writer 以该蓝图切片为骨架，结合 `episode-directory.md` 当前集硬锚点填血肉；`source-handoff`、源本账本、raw assets、debug、draft、comparison、review、polish、export、run evidence 仍禁止作为 writer 直读输入。
- `/dialogue-polish` 是整集逐场 final surface pass，负责压短句、砍水词、清翻译腔、清假金句、清解释句 / 作者句、拉开声线，并检查关键处是否需要打断、停顿、沉默、反应、身体反应、动作、物件或空间表层。它只改“怎么说、怎么演出来”，不能改剧情事实、真相顺序、人物关系、本集核心代价、结尾债务、状态增量、付费窗口或已确认蓝图承诺。

## 运行产物

源本导入产物：

```text
源本库/{源本名}/
```

新剧项目：

```text
新剧/{新剧名}/
```

用户交付稿：

```text
新剧/{新剧名}/export/
```

`源本库/` 和 `新剧/` 是运行目录。默认不提交生成内容，只保留 `.gitkeep`。

## 硬规则

- 最终产物必须是短剧剧本，不是电视剧、网剧、小说、故事梗概或泛型 screenplay。
- 用户可见蓝图和 writer 输入必须讲同一个故事，不能拆成两套剧情。
- 源本强节点从 `09_源本留存锚点.md` 进入蓝图、分集和 review；不得在下游静默降级、删除或改成证据/流程/说明。
- 正文必须有可见冲突、当场代价、人物反应链、追看债务和付费压力。
- 台词精修只能压解释、补反应拍、调整声线和去 AI 味，不得改剧情事实、人物关系、付费窗口或真相释放顺序。
- internal reviewer 负责质量判断和返修归因，不负责新写剧情；clean reviewer 负责 export 前内容验收。
- `/delivery-qa` 只检查导出交付稿是否漏集、乱序、元信息错误或泄漏内部字段，不重新审剧情。
- callback 只能回到明确责任层；不要在用户看到蓝图或正文前无限循环。
