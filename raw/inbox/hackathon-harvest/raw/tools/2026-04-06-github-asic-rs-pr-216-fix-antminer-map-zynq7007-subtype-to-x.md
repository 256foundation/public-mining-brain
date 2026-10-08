# 256foundation/asic-rs pull request #216: fix(antminer): map zynq7007 subtype to Xilinx control board

> Source: https://github.com/256foundation/asic-rs/pull/216
> Collected: 2026-10-07
> Published: 2026-04-06

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 216
- State: closed
- Author: jpcomps
- Opened: 2026-04-06
- Closed: 2026-04-06
- Labels: none

## Description

## Summary
- normalize Antminer control board subtype strings by stripping non-alphanumeric characters before matching.
- add explicit support for `zynq7007` so Xilinx control boards reported by `miner_type.cgi` resolve correctly.
- keep existing control board mappings unchanged while fixing missing control board detection for affected miners.

## Validation
- `cargo test -p asic-rs-makes-antminer`
