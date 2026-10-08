# 256foundation/asic-rs pull request #402: feat(pools): add worker suffix helpers

> Source: https://github.com/256foundation/asic-rs/pull/402
> Collected: 2026-10-07
> Published: 2026-10-01

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 402
- State: closed
- Author: cfilipescu
- Opened: 2026-10-01
- Closed: 2026-10-01
- Labels: none

## Description

## Summary

- Add consuming `use_worker_suffix(suffix)` helpers to `PoolConfig` and `PoolGroupConfig`. The caller supplies the exact text to append, including the separating dot.
- Add `clear_worker_suffix()` helpers that keep the account username before the first dot and remove the worker name. Worker names may contain additional dots.
- Keep pool config types and serialized pool config files unchanged.

```rust
let group = group.use_worker_suffix(".worker.with.periods");
let account_only = group.clear_worker_suffix();
```

These helpers change pool usernames. They do not toggle a firmware's own unique-worker-ID setting.

## Validation

- `cargo test -p asic-rs-core --locked` (26 passed)
- `cargo fmt --all`
- `git diff --check`
