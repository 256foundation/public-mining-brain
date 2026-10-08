# 256foundation/asic-rs issue #116: Bug: Incorrect Unit for Marathon Miner hashrates

> Source: https://github.com/256foundation/asic-rs/issues/116
> Collected: 2026-10-07
> Published: 2025-12-11

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 116
- State: closed
- Author: NeroWeNeed
- Opened: 2025-12-11
- Closed: 2025-12-24
- Labels: none

## Description

Marathon Miner is reporting itself in the wrong unit for it's HashRate Data Field.

## Comments

### b-rowan on 2025-12-11

Should just need to change the unit value here - https://github.com/256foundation/asic-rs/blob/8c50162edbcf569580f73b9dcb4a6bfa39c34750/src/miners/backends/marathon/v1/mod.rs#L466

### s0kil on 2025-12-24

Fixed https://github.com/256foundation/asic-rs/pull/117
