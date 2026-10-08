# 256foundation/asic-rs pull request #28: feat: add adaptive concurrency and configurable timeout to MinerFactory

> Source: https://github.com/256foundation/asic-rs/pull/28
> Collected: 2026-10-07
> Published: 2025-08-06

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 28
- State: closed
- Author: s0kil
- Opened: 2025-08-06
- Closed: 2025-08-06
- Labels: none

## Description

- Add adaptive concurrency scaling based on IP count (25-200 concurrent)
- Add configurable discovery timeout with with_timeout() methods
- Auto-calculate optimal concurrency when IPs are set
- Maintain backward compatibility with manual overrides
