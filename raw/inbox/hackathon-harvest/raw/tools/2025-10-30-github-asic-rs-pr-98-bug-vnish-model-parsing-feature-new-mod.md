# 256foundation/asic-rs pull request #98: bug: vnish model parsing + feature: new model [S19jPro+]

> Source: https://github.com/256foundation/asic-rs/pull/98
> Collected: 2026-10-07
> Published: 2025-10-30

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 98
- State: closed
- Author: b-rowan
- Opened: 2025-10-30
- Closed: 2025-10-30
- Labels: none

## Description

Swapped to parsing miner in vnish info response, which matches the stock fw model.

Also added support for S19j Pro+.

Linting fix moved default for hashrates from an impl to a `#[default]` definition.
