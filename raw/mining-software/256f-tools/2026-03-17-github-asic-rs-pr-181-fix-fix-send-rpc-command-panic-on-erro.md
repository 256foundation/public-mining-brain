# 256foundation/asic-rs pull request #181: fix: fix send_rpc_command panic on error

> Source: https://github.com/256foundation/asic-rs/pull/181
> Collected: 2026-10-07
> Published: 2026-03-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 181
- State: closed
- Author: NeroWeNeed
- Opened: 2026-03-17
- Closed: 2026-03-17
- Labels: none

## Description

## Summary
- send_rpc_command can panic if write_all or read_to_end error, crashing the thread or application
- Logs reason why these commands fail and returns None
