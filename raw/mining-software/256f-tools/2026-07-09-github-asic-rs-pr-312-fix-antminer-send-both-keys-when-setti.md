# 256foundation/asic-rs pull request #312: fix(antminer): send both keys when setting sleep mode

> Source: https://github.com/256foundation/asic-rs/pull/312
> Collected: 2026-10-07
> Published: 2026-07-09

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 312
- State: closed
- Author: b-rowan
- Opened: 2026-07-09
- Closed: 2026-07-31
- Labels: none

## Description

This should gurantee that the miner actually turns on and off properly when sending mode, since the return value comes directly from the conf, it may not always be what the backend expects.

Fixes: #310
