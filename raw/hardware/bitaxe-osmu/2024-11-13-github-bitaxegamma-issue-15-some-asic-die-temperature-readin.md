# bitaxeorg/bitaxeGamma issue #15: some ASIC die temperature readings are incorrect

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/15
> Collected: 2026-10-07
> Published: 2024-11-13

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 15
- State: closed
- Author: skot
- Opened: 2024-11-13
- Closed: 2025-03-04
- Labels: bug

## Description

On some BM1370 units the die temperature readings collected by the EMC2101 are incorrect. We've seen readings both too high and too low. Both at idle and while mining.

Initially it appears some units are affected and others are not. 

## Comments

### skot on 2024-11-13

might be related to #13, and probably the cause of #12

### skot on 2025-03-04

This has been fixed with better temp diode tuning on the EMC2101
