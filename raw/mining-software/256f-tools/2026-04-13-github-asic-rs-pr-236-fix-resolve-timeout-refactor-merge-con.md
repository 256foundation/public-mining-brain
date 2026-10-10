# 256foundation/asic-rs pull request #236: fix: resolve timeout refactor merge conflicts

> Source: https://github.com/256foundation/asic-rs/pull/236
> Collected: 2026-10-07
> Published: 2026-04-13

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 236
- State: closed
- Author: cfilipescu
- Opened: 2026-04-13
- Closed: 2026-04-13
- Labels: none

## Description

## Summary
- resolve merge conflicts from the timeout/refactor work across core, firmware RPC backends, and miner factory code
- align RPC error handling and stream write/read call sites with the current `RPCError` variants so clippy and compile checks pass
- remove outdated Python factory builder methods and stale timeout calls introduced by conflict overlap

## Validation
- cargo clippy --all-targets -- -Dwarnings

## Comments

### b-rowan on 2026-04-13

Fix for CI issues - https://github.com/256foundation/asic-rs/pull/237

Once that gets merged, you can rebase and squash then it should pass.
