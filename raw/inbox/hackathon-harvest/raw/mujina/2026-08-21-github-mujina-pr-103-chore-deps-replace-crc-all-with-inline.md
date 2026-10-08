# 256foundation/mujina pull request #103: chore(deps): replace crc_all with inline CRC implementations

> Source: https://github.com/256foundation/mujina/pull/103
> Collected: 2026-10-07
> Published: 2026-08-21

- Repository: 256foundation/mujina
- Type: pull request
- Number: 103
- State: closed
- Author: SusanGithaigaN
- Opened: 2026-08-21
- Closed: 2026-08-31
- Labels: none

## Description

## Problem
`crc_all` is a niche, single-maintainer crate pulled in for two fixed CRC configurations in `bm13xx/crc.rs`. The generic abstraction it provides is not needed when the parameters never change. Identified in the dependency audit (discussion #8 , issue #29 ).

## Fix
Replace `crc_all` with inline implementations of CRC-5-USB and CRC-16-CCITT-FALSE. The public API (`crc5`, `crc5_is_valid`, `crc16`) and all call sites in `protocol.rs` are unchanged. Eliminates 1 exclusive transitive dependency.

## Tests
Correctness is covered by existing test vectors in `bm13xx/crc.rs`:
- 9 CRC-5 cases from esp-miner source code (frames accepted by real BM13xx hardware)
- 1 CRC-16 case from an actual serial capture

Differential testing against `crc_all` was run locally before removal: exhaustive comparison over all 256 single-byte inputs and all 65,536 two-byte combinations confirmed identical output for both algorithms.

Fixes: #29
