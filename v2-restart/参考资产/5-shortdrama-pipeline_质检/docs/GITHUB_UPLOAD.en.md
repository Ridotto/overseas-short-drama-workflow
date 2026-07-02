# GitHub Upload Guide

[中文](GITHUB_UPLOAD.md) | English

Use this guide when publishing the local project to GitHub or when checking that future updates only include source code, tests, configuration templates, and documentation.

## 1. Check Local State

```bash
git status --short
git ls-files
```

Tracked files should only include source code, tests, configuration templates, and documentation. They should not include:

- `.env`
- `.venv/`
- `outputs/`, `outputs_*/`
- SQLite databases
- model logs
- generated videos, images, or audio files

## 2. Run Verification

```bash
source .venv/bin/activate
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q
python -m compileall src/shortdrama_pipeline
```

Tests use fake providers by default. They do not call online models or consume credits.

## 3. Scan for Secrets

Scan the tracked working tree:

```bash
git grep -n -I -E "(ark-[A-Za-z0-9_-]{12,}|Bearer[[:space:]]+[A-Za-z0-9._~+/=-]{12,}|AKLT[A-Za-z0-9%._~+/=-]{12,}|X-Tos-(Credential|Signature)=)" -- . ':!uv.lock'
```

Scan git history:

```bash
git log --all -p -- . ':!uv.lock' | rg -n "(ark-[A-Za-z0-9_-]{12,}|Bearer\\s+[A-Za-z0-9._~+/=-]{12,}|AKLT[A-Za-z0-9%._~+/=-]{12,}|X-Tos-(Credential|Signature)=)"
```

Expected result: no real keys, Authorization tokens, signed TOS URLs, or usable credentials should appear.

## 4. Initialize and Commit

If the directory is not a git repository yet:

```bash
git init
git branch -M main
```

Review the diff before staging:

```bash
git diff
git add README.md README.en.md SECURITY.md docs/ src/ tests/ pyproject.toml .env.example .gitignore .github/workflows/ci.yml uv.lock
git status --short
git commit -m "Initial shortdrama pipeline"
```

Avoid blindly running `git add .` without checking the working tree first.

## 5. Push to GitHub

If GitHub CLI is installed and authenticated:

```bash
gh repo create shortdrama-pipeline --private --source=. --remote=origin --push
```

If the repository already exists:

```bash
git remote add origin git@github.com:<your-user-or-org>/shortdrama-pipeline.git
git push -u origin main
```

Use a public repository only if you are certain the project is ready to be public.

## 6. After Upload

After pushing, check:

- the GitHub file list only contains necessary source and documentation files
- GitHub Actions passes
- Chinese and English README links work
- the Security policy opens from GitHub's sidebar
- the repository About section has a description and topics

If you share the project externally, keep real `.env` files, model outputs, and generated videos in local or private storage only.
