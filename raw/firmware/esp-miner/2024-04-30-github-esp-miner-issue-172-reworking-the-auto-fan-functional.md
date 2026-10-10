# bitaxeorg/ESP-Miner issue #172: Reworking the auto fan functionality

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/172
> Collected: 2026-10-07
> Published: 2024-04-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 172
- State: closed
- Author: WantClue
- Opened: 2024-04-30
- Closed: 2025-04-16
- Labels: enhancement, good first issue

## Description

This is just an open issue to keep track of a potential rework for the auto fan functionality. Despite the fact that it works, it does tune the fan way too often and way too harsh. A slighter approach is needed. Maybe stages of ramp up and down.


## Comments

### tdb3 on 2024-06-04

Was this addressed since this Issue was opened?

If not, it seems like this could be somewhat straightforward tweak to `automatic_fan_speed()`.

https://github.com/skot/ESP-Miner/blob/38fb4ae999c039ac5bdd5adf8267d94e98442192/main/tasks/power_management_task.c#L189-L208

Looks like fan speed is adjusted every 2s, and done so with a smooth adjustment rather than a stepped one.

https://github.com/skot/ESP-Miner/blob/38fb4ae999c039ac5bdd5adf8267d94e98442192/main/tasks/power_management_task.c#L185C9-L185C28

Here are some initial/thoughts/alternatives:
 - Option 1: Keep fan speed adjustment as-is (smooth adjustment once every 2s based on chip temperature).  Slight pitch variation may be heard as the fan speed is balances.
 - Option 2: Use a stepped fan speed with some hysteresis around step points.  Chip temperature is allowed to vary more than option 1.  Fan speed adjusts in stepped levels, which will have different noise/pitch characteristics.  Changes from one step to another is likely more noticeable than option 1.
 - Option 3:  Introduce more lag in fan speed adjustment (slower ramp up and slower ramp down), almost like fan speed based on a moving average of chip temperature over a window.  Chip temperature is allowed to vary more than option 1 but less than option 2.  There would need to be a safety for this, to ramp up fan speed quickly if throttle threshold is reached.

### skot on 2024-10-10

There has been some talk of implementing PID fan control..

### WantClue on 2025-04-16

done with PID controller

### nexus-labs-admin on 2025-09-06

Hello, I have a BitAxe on `v2.10.0`. And I have this issue. The fan is going up and down and the sound is really annoying as it is cyclically going up-and-down.

Settings a fixed fan speed does not help. Because at low settings it overheats, and on higher it is just constantly too loud. As temperature at my place changes over day (yeah, freaking sun ... ) it is impossible to set it just right.

It would be great to have some setting for the hysteresis of this. 🙏
