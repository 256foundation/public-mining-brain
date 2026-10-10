# 256foundation/asic-rs pull request #230: feat: add Auradine support

> Source: https://github.com/256foundation/asic-rs/pull/230
> Collected: 2026-10-07
> Published: 2026-04-10

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 230
- State: closed
- Author: jpcomps
- Opened: 2026-04-10
- Closed: 2026-04-14
- Labels: none

## Description

## What changed
- add Auradine make and firmware support to the workspace
- implement Auradine v1 RPC and web backends
- register Auradine in miner discovery and factory construction
- add fixture-based tests for Auradine parsing and pool update safety

## Why
This adds first-class support for Auradine miners in `asic-rs`, including discovery, data collection, and control operations.

## Notes
- Auradine pool updates intentionally accept and submit only the first 3 pools
- pool updates require explicit passwords so we do not accidentally blank secrets during round-trip config writes
- mining state now considers the miner sleep state in addition to reported hashrate

## Validation
- `cargo check`
- `cargo test -p asic-rs-firmwares-auradine`
- `cargo test -p asic-rs-makes-auradine`


## Comments

### jpcomps on 2026-04-13

should be close now, some shameful 1 start indexing...so working around that makes it a bit messy but a good start. tested on a machine seems ok 

### jpcomps on 2026-04-14

Addressed the remaining status-parser placement feedback in `6c73479`:

- moved `StatusFromAuradineV1` into `backends/v1/rpc.rs` (matching existing backend pattern),
- reused that parser from the Web API flow,
- removed the separate `backends/v1/status.rs` module.

Also resolved the two open review threads tied to that refactor.
