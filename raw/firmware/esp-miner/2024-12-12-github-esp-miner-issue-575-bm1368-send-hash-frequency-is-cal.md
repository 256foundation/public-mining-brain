# bitaxeorg/ESP-Miner issue #575: BM1368_send_hash_frequency is called on all devices when frequency change is requested.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/575
> Collected: 2026-10-07
> Published: 2024-12-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 575
- State: closed
- Author: mutatrum
- Opened: 2024-12-12
- Closed: 2025-06-11
- Labels: accepted

## Description

The function `do_frequency_transition` is _only_ in bm1368.c, which calls `BM1368_send_hash_frequency` function. This function is called on all devices. This works because they apparently use the same command.

https://github.com/skot/ESP-Miner/blob/ba6be3c3bbb827df471e22bf2ecc54112d3fd82c/main/tasks/power_management_task.c#L287-L296

https://github.com/skot/ESP-Miner/blob/ba6be3c3bbb827df471e22bf2ecc54112d3fd82c/components/asic/bm1368.c#L181-L208

## Comments

### mutatrum on 2024-12-18

Duplicate of or related to #533 

### mutatrum on 2025-06-11

Fixed by #747
