# 256foundation/mujina pull request #119: docs(contributing): add Python prerequisite

> Source: https://github.com/256foundation/mujina/pull/119
> Collected: 2026-10-07
> Published: 2026-10-01

- Repository: 256foundation/mujina
- Type: pull request
- Number: 119
- State: open
- Author: wandiamugo
- Opened: 2026-10-01
- Closed: n/a
- Labels: none

## Description

This PR adds Python to the prerequisites list in `CONTRIBUTING.md`.

I ran into this on macOS, where the Xcode Command Line Tools provide Python 3.9.
When I ran `just checks`, the `test-scripts` step failed with:

```
ModuleNotFoundError: No module named 'tomllib'
```

That module is only in the standard library from Python 3.11, and
the guide didn't mention Python at all. Installing Python 3.14 with Homebrew fixed it.

After the change I ran `just checks`, and it passed.
