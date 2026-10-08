# 256foundation/asic-rs pull request #146: feature: add setpools for whatsminer

> Source: https://github.com/256foundation/asic-rs/pull/146
> Collected: 2026-10-07
> Published: 2026-02-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 146
- State: closed
- Author: b-rowan
- Opened: 2026-02-24
- Closed: 2026-02-24
- Labels: none

## Description

- Adds setpools for whatsminer v2 and v3
- Fixes a small bug where power was being sent as `{"watts": x}` instead of just `x` in `set_power_limit` for whatsminer V3
