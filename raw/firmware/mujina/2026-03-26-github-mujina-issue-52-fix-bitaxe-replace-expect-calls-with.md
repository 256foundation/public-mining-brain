# 256foundation/mujina issue #52: fix(bitaxe): replace `expect()` calls with proper error handling

> Source: https://github.com/256foundation/mujina/issues/52
> Collected: 2026-10-07
> Published: 2026-03-26

- Repository: 256foundation/mujina
- Type: issue
- Number: 52
- State: closed
- Author: rkuester
- Opened: 2026-03-26
- Closed: 2026-06-16
- Labels: contributor-friendly

## Description

There are several `expect()` calls in `mujina-miner/src/board/bitaxe.rs` that will panic on hardware failures or unexpected state. A panic takes down the whole process (or at minimum the task), leaving the system in an unknown state with hardware potentially half-initialized. If there's a reasonable chance something can fail, we should handle it with a proper error path.

Examples include `expect()` calls in `spawn_stats_monitor` that assume peripherals and channels are present. These should propagate errors instead of panicking.

Found during review of #33.
