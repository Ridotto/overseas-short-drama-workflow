# Quickstart

This project is used inside Codex. You do not need to install extra global skills.

## 1. Open The Project

Clone the repo, then open the project root in Codex.

```bash
git clone <repo-url>
cd 自动化编剧
```

Start from the repo root, not from `v2-restart/` or `shortdrama-remix/`.

## 2. Add Your Source Script

Put a source script in `input/`, for example:

```text
input/my-source-script.txt
```

A full short-drama script works best. If you only have a summary, fragments, a link, or a title, the product can still help with diagnosis and blueprint, but it should not promise a full script-quality rewrite.

## 3. Say What You Want In Codex

Use natural language. Example:

```text
源本在 input/my-source-script.txt。
请按当前主链，把它改写成海外女频短剧。
新壳方向：豪门医疗复仇。
正文语言：English。
先做标准首批 1-10 集。
先做源本导入、洗稿方向和创作蓝图确认，不要直接写正文。
```

If you do not know the new shell yet, say:

```text
源本在 input/my-source-script.txt。
我还没想好新壳。请先分析源本为什么好看，并给我 3 个可改写方向。
```

## 4. Confirm At The Right Points

Codex should stop for your confirmation at these points:

1. source suitability and rewrite direction;
2. rewrite scheme / new shell;
3. creative blueprint;
4. completed batch script;
5. whether to continue the next batch.

You do not need to run internal commands manually.

## 5. Optional Slash Commands

Natural language is the default. These commands are advanced shortcuts:

```text
/rewrite-start       开始一个新改写项目，导入源本，确认方向
/rewrite-blueprint   生成或刷新创作蓝图
/rewrite-write       写当前批正文，默认 1-10
/rewrite-polish      台词精修和去 AI 味
/rewrite-review      干净审稿
/rewrite-continue    继续下一批，比如 11-20
/rewrite-export      导出用户交付稿
/rewrite-status      查看当前项目进度和产物位置
```

## 6. Find The Output

The source library is saved under:

```text
shortdrama-remix/源本库/{source-name}/
```

The new drama project is saved under:

```text
shortdrama-remix/新剧/{project-name}/
```

The final user-facing export should be under:

```text
shortdrama-remix/新剧/{project-name}/export/
```

If a run claims it followed the current chain, it must have a `run_log.md`.

## 7. What Not To Use

Do not start from these historical routes. They are not part of the current main working tree:

```text
v20
v3-executor-first
V63
v2-restart/workflow_spec_*
```

They remain recoverable through Git history or local archive only, not the current product entry.
