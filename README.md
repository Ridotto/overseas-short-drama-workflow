# 自动化编剧

这是一个在 Codex 里使用的短剧改写产品原型。

它的目标很简单：把一部已被市场验证或值得参考的短剧源本，改写成新壳下仍然好看、能追、能付费的新短剧剧本。

当前形态不是网页 App，也不是命令行工具。用户在 Codex 里打开这个仓库，然后用自然语言和主控 agent 对话。

## 快速开始

1. 把源本放进 `input/`。
2. 在 Codex 里打开仓库根目录。
3. 直接告诉 Codex 你想怎么改写。

示例：

```text
源本在 input/my-source-script.txt。
请把它改写成海外女频短剧。
新壳方向：豪门医疗复仇。
正文语言：English。
先做标准首批 1-10 集。
先做源本导入、改写方向和创作蓝图确认，不要直接写正文。
```

更完整的使用说明见 [QUICKSTART.md](./QUICKSTART.md)。

## 产品入口

Codex 会从项目入口说明进入主控：

```text
AGENTS.md
shortdrama-remix/skills/shortdrama-main-controller/SKILL.md
```

用户不需要记内部命令。自然语言是默认入口。

高级用户也可以使用这些别名：

```text
/rewrite-start
/rewrite-blueprint
/rewrite-write
/rewrite-polish
/rewrite-review
/rewrite-continue
/rewrite-export
/rewrite-status
```

## 工作流

默认生产链：

```text
源本导入
-> 改写方向确认
-> 创作蓝图
-> 当前批正文
-> 台词精修
-> 审稿
-> 导出交付稿
-> 续批或反馈返修
```

首批默认是 `1-10` 集，但产品会把它当成完整短剧的一部分来设计，而不是孤立样片。

## 产物位置

源本导入产物：

```text
shortdrama-remix/源本库/{源本名}/
```

新剧项目：

```text
shortdrama-remix/新剧/{新剧名}/
```

用户交付稿：

```text
shortdrama-remix/新剧/{新剧名}/export/
```

任何声称“按当前链路执行”的运行，都应该在项目产物里留下 `run_log.md`。

## 项目结构

```text
AGENTS.md
QUICKSTART.md
docs/
  PRD.md
  产品架构与主控路由_v1.md
input/
shortdrama-remix/
  contracts/
  skills/
  源本库/
  新剧/
```

运行输入和生成产物默认不提交到 Git。

## 开发分支

`main` 是用户正式版，只保留使用产品需要的内容。

开发素材、历史审计、旧实验和后续治理放在 `codex/next` 分支或本地归档中，不放在 `main` 的当前文件树里。
