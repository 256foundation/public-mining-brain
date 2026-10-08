# 256foundation/asic-rs pull request #358: feat(epic): add timezone config

> Source: https://github.com/256foundation/asic-rs/pull/358
> Collected: 2026-10-07
> Published: 2026-09-10

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 358
- State: closed
- Author: cfilipescu
- Opened: 2026-09-10
- Closed: 2026-09-10
- Labels: none

## Description

## Summary

- collect the configured IANA timezone from the Epic PowerPlay timezone endpoint
- support setting the timezone through the authenticated PowerPlay API
- advertise timezone configuration support and reject invalid timezone names
- add focused collector and parser tests

Closes #356

## Testing

- cargo test --workspace
- cargo clippy -p asic-rs-firmwares-epic --all-targets -- -D warnings
- git diff --check
