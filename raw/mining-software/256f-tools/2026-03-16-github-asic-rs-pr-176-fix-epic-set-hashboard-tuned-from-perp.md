# 256foundation/asic-rs pull request #176: fix(epic): set hashboard tuned from perpetual tune optimization

> Source: https://github.com/256foundation/asic-rs/pull/176
> Collected: 2026-10-07
> Published: 2026-03-16

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 176
- State: closed
- Author: cfilipescu
- Opened: 2026-03-16
- Closed: 2026-03-16
- Labels: none

## Description

## Summary
- populate `hashboard.tuned` for ePIC miners from `/Summary/PerpetualTune/Algorithm/*/Optimized`
- apply the parsed tuned value consistently across all parsed hashboards
- avoid using `Running`, since tuning state should reflect optimization status
