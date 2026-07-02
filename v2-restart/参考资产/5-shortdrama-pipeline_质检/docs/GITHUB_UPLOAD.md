# GitHub 发布指南

中文 | [English](GITHUB_UPLOAD.en.md)

这份文档用于把本地项目发布到 GitHub，或在后续更新时确认仓库里只包含应该公开的代码和文档。

## 1. 确认本地状态

```bash
git status --short
git ls-files
```

确认已跟踪文件只包含源码、测试、配置模板和文档，不应包含：

- `.env`
- `.venv/`
- `outputs/`、`outputs_*/`
- SQLite 数据库
- 模型日志
- 生成的视频、图片、音频

## 2. 运行验证

```bash
source .venv/bin/activate
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q
python -m compileall src/shortdrama_pipeline
```

测试默认使用 fake provider，不会调用线上模型，也不会消耗额度。

## 3. 扫描密钥

工作区扫描：

```bash
git grep -n -I -E "(ark-[A-Za-z0-9_-]{12,}|Bearer[[:space:]]+[A-Za-z0-9._~+/=-]{12,}|AKLT[A-Za-z0-9%._~+/=-]{12,}|X-Tos-(Credential|Signature)=)" -- . ':!uv.lock'
```

历史扫描：

```bash
git log --all -p -- . ':!uv.lock' | rg -n "(ark-[A-Za-z0-9_-]{12,}|Bearer\\s+[A-Za-z0-9._~+/=-]{12,}|AKLT[A-Za-z0-9%._~+/=-]{12,}|X-Tos-(Credential|Signature)=)"
```

预期结果：不应出现真实 Key、Authorization token、TOS 签名 URL 或其他可用凭据。

## 4. 初始化并提交

如果还没有 git 仓库：

```bash
git init
git branch -M main
```

提交前建议显式检查差异：

```bash
git diff
git add README.md README.en.md SECURITY.md docs/ src/ tests/ pyproject.toml .env.example .gitignore .github/workflows/ci.yml uv.lock
git status --short
git commit -m "Initial shortdrama pipeline"
```

不要在不看状态的情况下盲目 `git add .`。

## 5. 推送到 GitHub

如果 GitHub CLI 已安装且已登录：

```bash
gh repo create shortdrama-pipeline --private --source=. --remote=origin --push
```

如果仓库已经存在：

```bash
git remote add origin git@github.com:<your-user-or-org>/shortdrama-pipeline.git
git push -u origin main
```

只有在明确希望公开项目时，才把仓库设为 public。

## 6. 发布后检查

推送后建议检查：

- GitHub 文件列表是否只包含必要源码和文档。
- GitHub Actions 是否通过。
- README 的中英文链接是否正常。
- Security policy 是否能在 GitHub 右侧入口打开。
- 仓库 About 区域是否补充了 description 和 topics。

如果之后要分享给外部用户，建议保持真实 `.env`、模型输出和视频产物只在本地或私有存储中流转。
