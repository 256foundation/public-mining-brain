# 256foundation/asic-rs pull request #336: chore: ignore the build artifacts the test scripts generate

> Source: https://github.com/256foundation/asic-rs/pull/336
> Collected: 2026-10-07
> Published: 2026-08-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 336
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-24
- Closed: 2026-08-25
- Labels: none

## Description

`.gitignore` covers `/target` but nothing the Python side produces — even though `scripts/run_python_tests.py` is the documented way to run the suite, and `maturin develop` writes a compiled extension module straight into `python/pyasic_rs/`.

In a debug build that file is **~390 MB**, so `git add -A` after a test run produces a commit GitHub refuses outright at its 100 MB limit. I hit exactly this while working on another branch. pytest and mypy also leave caches beside the sources.

Adds the usual Python patterns:

```
__pycache__/
*.py[cod]
*.so
*.pyd
*.dylib
.pytest_cache/
.mypy_cache/
.ruff_cache/
.venv/
*.egg-info/
```

Nothing matching these is tracked today (`git ls-files` confirms), so this only affects generated output.

**One judgment call left open:** `uv.lock` is produced by the same run and is currently untracked. Lockfiles are often committed deliberately, so I have not ignored it — happy to add it, or to commit the generated one instead, whichever you prefer.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ErTo1a4BgYptp5tC8r1oHR
