# asic-rs Supported Devices

> Sources: 256 Foundation (asic-rs documentation, Supported Devices), collected 2026-10-07; 256 Foundation (asic-rs README), collected 2026-10-07
> Raw: [asic-rs supported devices](../../raw/tools/docs-asic-rs-supported-devices.md); [asic-rs README](../../raw/tools/github-256foundation-asic-rs.md)
> Updated: 2026-10-07

## Overview

The asic-rs documentation publishes the exact list of miners the library can identify, plus a matrix of which controls work on which firmware. The page is generated from the Rust source, so it tracks the code. WhatsMiner dominates the model count because every hardware sub-version is its own entry. This article summarizes the list. For the library itself, see [asic-rs](asic-rs.md).

## Firmware types

The support matrix has one row per firmware type:

- Stock firmware: AntMiner, Auradine, AvalonMiner, Bitaxe, Elphapex, FutureBit, Nerdaxe, Proto, SealMiner, VolcMiner and WhatsMiner.
- Aftermarket and other firmware: Braiins, LuxOS, Marathon, UMC OS and VNish.

## What the matrix tracks

For each firmware type the matrix marks thirteen functions: pools config, scaling config, tuning config, fan config, light, power limit, restart, pause/resume, firmware upgrade, password change, factory reset of settings, restore stock OS, and reading logs.

Each cell has one of three values: every backend subtype supports it, support is mixed or conditional, or no backend subtype supports it.

The collected copy of the page lost the cell symbols. The per-firmware results cannot be read from it. Check the live page, or call the library's `supports_*` checks against a real miner.

## Models by make

| Make | Models and families |
|------|---------------------|
| AntMiner | 61 models across 24 families |
| Auradine | 5 models across 5 families |
| AvalonMiner | 21 models across 11 families |
| Bitaxe | 4 models across 4 families |
| Braiins | 2 models across 1 family |
| Elphapex | 3 models across 2 families |
| ePIC | 2 models across 2 families |
| FutureBit | 2 models across 2 families |
| Nerdaxe | 4 models across 4 families |
| Proto | 1 model across 1 family |
| SealMiner | 1 model across 1 family |
| VolcMiner | 1 model across 1 family |
| WhatsMiner | 499 models across 32 families |

## Notes on each make

### AntMiner

The list is not only Bitcoin machines. It includes D, DR, E, HS, K, KA, KS, L and Z series models alongside the S and T series.

- The S19 family is the largest, with 18 models.
- The S21 family has 11 models.
- The S17 family has 4 models. The S9 and T17 families have 3 each.
- The S23 family has 1 model, the S23 HYD.

Several models are matched under more than one name. Hydro models are recognized as both HYD. and HYDRO, for example.

### WhatsMiner

Families run from M20 to M79. Each entry is a full hardware version string, such as `M30S++VH10`. The largest families:

| Family | Models |
|--------|--------|
| M30 | 101 models |
| M60 | 67 models |
| M50 | 61 models |
| M63 | 54 models |
| M31 | 41 models |
| M66 | 34 models |
| M53 | 27 models |
| M61 | 22 models |

### Bitaxe and Nerdaxe

Both are listed by chip, not by product name. Each has four entries: `BM1366`, `BM1368`, `BM1370` and `BM1397`. The Nerdaxe `BM1370` entry also matches the NerdQAxe++.

### The rest

- **Auradine:** AH3880, AI2500, AI3680, AT1500 and AT2880.
- **AvalonMiner:** from the 7xx family up to the 15xx family, plus the NANO3, NANO3S and Q.
- **Braiins:** the Braiins Mini Miner BMM 100 and BMM 101.
- **Elphapex:** DG1, DG1+ and DG-Home1.
- **ePIC:** the BLOCKMINER 520i and the ANTMINER S19J PRO DUAL.
- **FutureBit:** Apollo1 and Apollo2.
- **Proto:** the RIG.
- **SealMiner:** the A2.
- **VolcMiner:** the VOLCMINER D1.

## Firmware that reports extra state

The README names the firmware that fills in the detailed operating state field: ePIC/UMC, VNish, Braiins REST (25.07+), MARA and Proto. Developer-fee connection health comes from ePIC/UMC, VNish and LuxOS.

## See Also

- [asic-rs](asic-rs.md)
- [BTC Toolkit](btc-toolkit.md)
- [Hydrapool Hardware Tests](../hydrapool/hydrapool-hardware-tests.md)
