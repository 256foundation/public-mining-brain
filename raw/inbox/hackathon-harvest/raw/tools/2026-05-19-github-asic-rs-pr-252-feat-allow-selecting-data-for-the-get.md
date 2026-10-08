# 256foundation/asic-rs pull request #252: feat: allow selecting data for the `get_data` return

> Source: https://github.com/256foundation/asic-rs/pull/252
> Collected: 2026-10-07
> Published: 2026-05-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 252
- State: closed
- Author: b-rowan
- Opened: 2026-05-19
- Closed: 2026-05-25
- Labels: none

## Description

Also adds the ability to remove `data.hashboards.chips` to account for data constraints, since it can be a very large part of the data and most situations don't require it.
