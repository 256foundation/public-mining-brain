# 256foundation/emberone00-pcb issue #59: docs(schematic): rename active-low signal nets to include _N suffix

> Source: https://github.com/256foundation/emberone00-pcb/issues/59
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 59
- State: closed
- Author: rkuester
- Opened: 2026-03-19
- Closed: 2026-03-21
- Labels: none

## Description

Three signal nets use active-high naming but are actually active low. Adding an `_N` suffix would make the schematic less confusing when writing firmware and driver software.

| Current name | Proposed name | Comments |
|---|---|---|
| `RST` | `CHAIN_RST_N` | Drives NRSTI on the BM1362 chain; `CHAIN_` prefix avoids confusion with the per-chip `RST_N` nets on the ASIC sheets |
| `THERM` | `THERM_N` | TMP451 THERM output is open-drain, asserts low on over-temperature |
| `SMB_ALRT` | `SMB_ALRT_N` | TPS546 alert is open-drain, asserts low on fault |

Net renames only, no electrical changes.

## Comments

### skot on 2026-03-21

added in v6.1

### rkuester on 2026-03-21

Thanks!
