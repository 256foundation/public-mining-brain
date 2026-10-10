# 256foundation/mujina issue #9: feat(bitaxe): implement closed-loop fan control based on temperature

> Source: https://github.com/256foundation/mujina/issues/9
> Collected: 2026-10-07
> Published: 2025-11-22

- Repository: 256foundation/mujina
- Type: issue
- Number: 9
- State: open
- Author: rkuester
- Opened: 2025-11-22
- Closed: n/a
- Labels: contributor-friendly

## Description

Add automatic fan speed control that adjusts based on ASIC temperature. Currently the fan runs at 100% as a safe default.

See esp-miner's PID-based fan control implementation:
https://github.com/bitaxeorg/esp-miner/blob/66e4f1e63172f69a212d116ed8963fe36da62cb7/main/tasks/power_management_task.c#L109-L161
