# 256foundation/emberone00-pcb issue #34: measure at least the first ASIC temp diodes

> Source: https://github.com/256foundation/emberone00-pcb/issues/34
> Collected: 2026-10-07
> Published: 2025-04-24

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 34
- State: open
- Author: skot
- Opened: 2025-04-24
- Closed: n/a
- Labels: enhancement

## Description

BM1362 ASICs all have internal temp diodes. It's a little tricky measuring these with all the floating grounds we have. But we could at least measure the internal temp of the first ASIC, which is global GND referenced.

Prolly switch one of the TMP1075 air temp sensors out for a EMC2101.
