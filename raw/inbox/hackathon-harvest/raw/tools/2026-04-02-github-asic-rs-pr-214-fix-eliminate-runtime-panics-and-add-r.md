# 256foundation/asic-rs pull request #214: fix: eliminate runtime panics and add robustness guardrails

> Source: https://github.com/256foundation/asic-rs/pull/214
> Collected: 2026-10-07
> Published: 2026-04-02

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 214
- State: closed
- Author: ankitgoswami
- Opened: 2026-04-02
- Closed: 2026-04-02
- Labels: none

## Description

## Summary

- Fix timestamp overflow bug where `timestamp_millis() as u32` produced garbage values (millis for 2024+ are ~1.7T, overflowing `u32` max of ~4.3B) — changed to `timestamp()` (seconds, valid until 2106)
- Replace `.unwrap()` calls on network-derived data in AES encrypt/decrypt functions with proper error propagation, preventing panics on malformed miner responses
- Convert UDP listener `.expect()`/`.unwrap()` calls to graceful error handling — bind failures yield errors into the stream, recv failures log and skip
- Fix NaN-triggered panic in Epic temperature parsing by replacing `partial_cmp().unwrap()` with `total_cmp()`
- Fix fan RPM `.parse().unwrap()` and chip position `.unwrap()` panics on malformed miner data
- Add `catch_unwind` safety net around `get_miner()` with panic logging (protects Python/PyO3 callers from interpreter crashes)
- Fix memory leak in UDP listeners where `recv_buf_from` appended to buffer without clearing
- Add workspace-level clippy lints (`unwrap_used`, `expect_used`, `panic`) to prevent future regressions
- Add JoinSet task failure logging in discovery loop (previously silently swallowed)
- Change release profile from `panic = "abort"` to `panic = "unwind"` so `catch_unwind` works in release builds

![Armoring up](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGZ5aXYwbm0yc3ZkdXZvcGU2bnNjM2o4bXVqOWF0c2s2aXR4eWU0eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/j9vbNDaEQnUSgTWWFo/giphy.gif)

## Details

### Timestamp Bug (Correctness)
`MinerMessage.timestamp` is `u32` representing Unix seconds, but both whatsminer v2 and braiins v25_07 were writing `timestamp_millis() as u32` — silently truncating to meaningless values. Changed to `timestamp()`.

### Crypto Panics (Critical)
`aes_ecb_enc()`, `aes_ecb_dec()` (whatsminer v2), and `encrypt_param()` (whatsminer v3) contained `.unwrap()` on base64 decoding of **network data from miners**. Malformed responses would crash the process. Changed signatures to return `anyhow::Result<String>` and propagate errors. Deterministic operations (SHA256 hex decode, AES key construction) kept as `.expect()` with explanatory messages since they cannot fail.

### Listener Robustness
UDP listeners for AntMiner (port 14235) and WhatsMiner (port 8888) used `.expect()` on bind and `.unwrap()` on recv — crashing the entire process if the port was in use or a network error occurred. Now gracefully yields errors and skips bad packets. Also fixed a memory leak where the recv buffer was never cleared between iterations.

### Panic Safety Net
`get_miner()` is wrapped with `catch_unwind` to convert any remaining panics into `Err` values with logging, so callers (especially Python via PyO3) are never killed by an internal panic. The release profile was changed from `panic = "abort"` to `panic = "unwind"` to make this work in production.

**Tradeoff:** `panic = "unwind"` produces slightly larger release binaries (unwind tables are included) and marginally slower code compared to `abort`. This is the right tradeoff for a library — callers should never be killed by an internal panic, and the `catch_unwind` safety net only functions with unwind semantics.

### Clippy Lints
Added `[workspace.lints.clippy]` with `unwrap_used`, `expect_used`, and `panic` as warnings across all 20 workspace crates. This flags any new `.unwrap()` usage at lint time, forcing developers to make a conscious choice.

## Files Changed
- **34 files**, ~170 insertions, ~45 deletions
- 20 `Cargo.toml` files (lint configuration)
- 14 source files (bug fixes and robustness improvements)

## Test plan
- [ ] `cargo build` passes
- [ ] `cargo test` — all 17 tests pass (6 unit + 11 doc)
- [ ] `cargo clippy` — warnings are from acceptable pre-existing uses (SystemTime, HTTP client init, hardcoded constants)
- [ ] Verify timestamp values are sensible Unix seconds (not millis)
- [ ] Integration test with a real miner returning malformed responses (if available)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### b-rowan on 2026-04-02

Nice.  Like the ideas all around, good ideas to make the library more safe.
