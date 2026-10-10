# 256foundation/asic-rs pull request #131: bugfix/antminer-sleep-mode-detection

> Source: https://github.com/256foundation/asic-rs/pull/131
> Collected: 2026-10-07
> Published: 2026-01-28

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 131
- State: closed
- Author: glitchpixelz
- Opened: 2026-01-28
- Closed: 2026-01-28
- Labels: none

## Description

Fix AntMinerV2020 mining-state detection when bitmain-work-mode is returned as a numeric string. Treat "1" (sleep) as not mining, alongside "stopped", "idle", and "sleep"
