# 256foundation/asic-rs pull request #247: fix(epic): detect xilinx control boards in v1 backend

> Source: https://github.com/256foundation/asic-rs/pull/247
> Collected: 2026-10-07
> Published: 2026-05-01

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 247
- State: closed
- Author: cfilipescu
- Opened: 2026-05-01
- Closed: 2026-05-03
- Labels: none

## Description

## Summary
- add explicit detection for Xilinx-based control boards in the EPic v1 backend version parser
- map matched platforms to `AntMinerControlBoard::Xilinx` instead of falling back to `EPicUMC`
- preserve existing behavior for other known and unknown board strings
