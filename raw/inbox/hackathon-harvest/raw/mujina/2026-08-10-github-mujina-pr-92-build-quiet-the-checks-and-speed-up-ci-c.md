# 256foundation/mujina pull request #92: build: quiet the checks and speed up CI caching

> Source: https://github.com/256foundation/mujina/pull/92
> Collected: 2026-10-07
> Published: 2026-08-10

- Repository: 256foundation/mujina
- Type: pull request
- Number: 92
- State: closed
- Author: rkuester
- Opened: 2026-08-10
- Closed: 2026-08-11
- Labels: none

## Description

Fixes from auditing the supply-chain hardening's first CI run (PR #91).

- `just checks` now runs warning-free: allow cargo's duplicate crate versions (not actionable) and clarify unescaper's unparseable license declaration.
- The build toolchain image rebuilds only when a tool changes: tool setup moves to tools.just, the only file the container copies, and the CI cache key comes from the justfile's BUILD_TAG, so the key and the image tag cannot drift.
- On a cache key miss, restore-keys falls back to the nearest saved cache instead of starting cold.
- setup-just v4 retires GitHub's Node 20 deprecation warning.
