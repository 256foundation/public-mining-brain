# 256foundation/mujina pull request #116: fix(scheduler): leave excess threads idle when extranonce2 space is small

> Source: https://github.com/256foundation/mujina/pull/116
> Collected: 2026-10-07
> Published: 2026-09-28

- Repository: 256foundation/mujina
- Type: pull request
- Number: 116
- State: open
- Author: j-kon
- Opened: 2026-09-28
- Closed: n/a
- Labels: none

## Description

## Problem

When an incoming job's extranonce2 space holds fewer values than the number of eligible hash threads, such as a 1-byte EN2 space with 256 values and 257 eligible threads, `Extranonce2Range::split(eligible.len())` returns `None`.

The scheduler previously called `.expect()` on that result, causing the scheduler task to panic while the daemon itself remained alive.

## Solution

- Limit assignment to the number of threads the EN2 space can support.
- Leave excess threads idle instead of panicking or dropping the entire job.
- Emit a structured warning containing:
  - source
  - eligible thread count
  - EN2 space size
  - assigned thread count
  - idle thread count
- Preserve existing behavior when the EN2 space can support all eligible threads.
- Leave version-bit / `ntime` splitting and source status reporting to their dedicated follow-up work.

## Tests

The first commit reproduces the original bug with a regression test marked `#[should_panic]`.

The fix commit removes `#[should_panic]` and verifies:

- 255 threads / 256 EN2 values: all threads receive work
- 256 threads / 256 EN2 values: all threads receive work
- 257 threads / 256 EN2 values: 256 receive non-overlapping work and 1 remains idle

Local checks:

- `cargo fmt --check`
- `cargo clippy --release --locked -- -D warnings`
- `cargo test`
- `just checks`
- both commits validated independently

`just ci` was not run locally because Podman is not installed.

Closes #114
