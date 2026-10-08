# 256foundation/asic-rs pull request #297: docs: add vnish v1.3.4 API schema

> Source: https://github.com/256foundation/asic-rs/pull/297
> Collected: 2026-10-07
> Published: 2026-06-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 297
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-24
- Closed: 2026-06-24
- Labels: none

## Description

Adds the AnthillOS/VNish **1.3.4** OpenAPI schema (pulled from the miner's own `/docs/api-doc.json` on an S19 Pro Hydro, firmware build 2026-06-15), same format as the existing `v1.2.6`/`v1.2.7`.

Notably it documents **`POST /mining/throttle`** (`ThrottleSettings.percent`, 20–100) — new since 1.2.x and what the asic-rs VNish backend uses for throttle control (cf. #289).
