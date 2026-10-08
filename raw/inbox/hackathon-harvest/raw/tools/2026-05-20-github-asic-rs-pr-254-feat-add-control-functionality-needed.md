# 256foundation/asic-rs pull request #254: feat: add control functionality needed by proto fleet

> Source: https://github.com/256foundation/asic-rs/pull/254
> Collected: 2026-10-07
> Published: 2026-05-20

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 254
- State: closed
- Author: b-rowan
- Opened: 2026-05-20
- Closed: 2026-05-21
- Labels: none

## Description

Adds `ReadLogs`, `FactoryReset`, and `ChangePassword` traits for miner firmwares that have meta files.  Added blank implementations for the other ones for now, but this follows the same pattern as the other control traits, adding a function to execute the functions and a function for `supports_{function}`.

Added for epic, braiins, and vnish, since those have API documentation in git.
