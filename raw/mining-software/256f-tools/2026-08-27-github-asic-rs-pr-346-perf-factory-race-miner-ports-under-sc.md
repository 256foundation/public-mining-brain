# 256foundation/asic-rs pull request #346: perf(factory): race miner ports under scan limit

> Source: https://github.com/256foundation/asic-rs/pull/346
> Collected: 2026-10-07
> Published: 2026-08-27

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 346
- State: closed
- Author: DanNicolau
- Opened: 2026-08-27
- Closed: 2026-08-27
- Labels: none

## Description

early exit discovery once we find a live port, no need to wait for other ports, gives some performance benefit
