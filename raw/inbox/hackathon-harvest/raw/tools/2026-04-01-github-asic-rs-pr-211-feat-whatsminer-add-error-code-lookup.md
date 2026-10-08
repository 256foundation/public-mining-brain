# 256foundation/asic-rs pull request #211: feat(whatsminer): add error code lookup for GetMessages (#201)

> Source: https://github.com/256foundation/asic-rs/pull/211
> Collected: 2026-10-07
> Published: 2026-04-01

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 211
- State: closed
- Author: ankitgoswami
- Opened: 2026-04-01
- Closed: 2026-04-01
- Labels: none

## Description

WhatsMiner V1, V2, and V3 backends returned empty or missing message text from GetMessages. Port the WhatsMiner error code lookup table to Rust so consumers get actionable descriptions like "Power input voltage is lower than 230V for high power mode." instead of empty strings.
