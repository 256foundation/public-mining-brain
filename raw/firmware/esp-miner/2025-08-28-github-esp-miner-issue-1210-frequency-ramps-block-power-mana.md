# bitaxeorg/ESP-Miner issue #1210: Frequency ramps block power_management_task

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1210
> Collected: 2026-10-07
> Published: 2025-08-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1210
- State: open
- Author: mutatrum
- Opened: 2025-08-28
- Closed: n/a
- Labels: bug

## Description

Currently, a multi-step frequency change is done from the power_management_task. This stops the fan controller from working while it's ramping up.

A possible improvement would be to have a separate frequency_controller_task, that can both do the initial frequency ramp and any subsequent changes. This way, the power_management_task can just handle the fan and overheat control.

Voltage adjustments could also be moved into this new task.

## Comments

### KillerInk on 2025-09-07

hm global_state hast this
https://github.com/bitaxeorg/ESP-Miner/blob/3bd85f9efd8d83b1a6ceb9462962f9d7503c50c7/main/global_state.h#L117

and putting this in
`if(GLOBAL_STATE->ASIC_initalized){`
https://github.com/bitaxeorg/ESP-Miner/blob/3bd85f9efd8d83b1a6ceb9462962f9d7503c50c7/main/tasks/power_management_task.c#L193-L213
`}`
would avoid to set it till its ramped up
