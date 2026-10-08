# 256foundation/asic-rs pull request #259: fix: make async cleanup cancellation safe

> Source: https://github.com/256foundation/asic-rs/pull/259
> Collected: 2026-10-07
> Published: 2026-05-25

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 259
- State: closed
- Author: jameshilliard
- Opened: 2026-05-25
- Closed: 2026-05-25
- Labels: none

## Description

Propagate Python cancellation into Rust futures, keep discovery and RPC work owned by parent futures, and yield during large firmware processing.

## Comments

### b-rowan on 2026-05-25

@codex review

### b-rowan on 2026-05-25

> @codex review

Fine, ill do it myself then...

Damn lazy AI :laughing:
