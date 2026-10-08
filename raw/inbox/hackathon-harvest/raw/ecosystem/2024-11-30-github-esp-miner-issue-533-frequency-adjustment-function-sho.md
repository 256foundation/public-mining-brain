# bitaxeorg/ESP-Miner issue #533: frequency adjustment function should work for all ASICs

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/533
> Collected: 2026-10-07
> Published: 2024-11-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 533
- State: closed
- Author: skot
- Opened: 2024-11-30
- Closed: 2025-11-25
- Labels: bug

## Description

It looks like the power_management task has a loop to check for frequency changes, but it doesn't look like `do_frequency_transition()` is valid for all different ASIC types. This should probably be a function pointer in ASIC_functions to the proper ASIC-specific function to transition the frequency.

https://github.com/skot/ESP-Miner/blob/e9b30ba7795a4cdc368c8046a1d2a01cbb840cbc/main/tasks/power_management_task.c#L285-L294
