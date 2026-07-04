# Quickstart

This project runs inside Codex. You do not need to install extra global skills.

## 1. Open The Project

Clone the repo, then open the project root in Codex.

```bash
git clone <repo-url>
cd 自动化编剧
```

## 2. Add Your Source Script

Put a source script in `input/`, for example:

```text
input/my-source-script.txt
```

A complete short-drama script works best. If you only have a summary, fragments, a link, or a title, the product can still help with diagnosis and blueprint work, but it should not promise a full script-quality rewrite.

## 3. Tell Codex What You Want

Use natural language. Example:

```text
源本在 input/my-source-script.txt。
请把它改写成海外女频短剧。
新壳方向：豪门医疗复仇。
正文语言：English。
先做标准首批 1-10 集。
先做源本导入、改写方向和创作蓝图确认，不要直接写正文。
```

If you do not know the new shell yet, say:

```text
源本在 input/my-source-script.txt。
我还没想好新壳。请先分析源本为什么好看，并给我 3 个可改写方向。
```

## 4. Confirmation Points

Codex should stop for confirmation at these points:

1. source suitability and rewrite direction;
2. rewrite scheme / new shell;
3. creative blueprint;
4. completed batch script;
5. whether to continue the next batch.

Everything else should advance automatically unless you ask for manual control.

## 5. Optional Slash Commands

Natural language is the default. These commands are shortcuts:

```text
/rewrite-start       开始一个新改写项目，导入源本，确认方向
/rewrite-blueprint   生成或刷新创作蓝图
/rewrite-write       写当前批正文，默认 1-10
/rewrite-polish      台词精修和去 AI 味
/rewrite-review      审稿
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

If a run claims it followed the current chain, it must include a `run_log.md`.

## 7. Report Problems

Use the GitHub issue templates:

- `主链运行问题` for reproducible problems in the current `shortdrama-remix` chain.
- `产品反馈 / 改进建议` for workflow, quality, continuation, export, or documentation feedback.

If a problem claims the current chain was followed, include the relevant `run_log.md` path. Do not paste full private source scripts or complete generated scripts into public issues.
