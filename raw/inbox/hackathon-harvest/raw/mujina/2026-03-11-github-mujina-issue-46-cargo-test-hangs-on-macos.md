# 256foundation/mujina issue #46: cargo test hangs on macOS

> Source: https://github.com/256foundation/mujina/issues/46
> Collected: 2026-10-07
> Published: 2026-03-11

- Repository: 256foundation/mujina
- Type: issue
- Number: 46
- State: closed
- Author: rkuester
- Opened: 2026-03-11
- Closed: 2026-03-11
- Labels: none

## Description

`cargo test` hangs indefinitely on macOS. `transport::serial::tests::test_concurrent_read_write` blocks and never completes.

The issue does not reproduce on Linux, where the same test passes without hanging.

Found in 7942a3d.
