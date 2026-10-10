# bitaxeorg/ESP-Miner issue #58: Automatic Fan Control causing BM1366 overheating

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/58
> Collected: 2026-10-07
> Published: 2023-11-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 58
- State: closed
- Author: ozbibi
- Opened: 2023-11-22
- Closed: 2023-11-29
- Labels: none

## Description

Introduced in v2.0.2, the formula used for automatic fan control incorrectly calculates the fan speed, resulting in potential overheating of the BM1335 on the Bitaxe Ultra.

Looking at the [automatic_fan_speed()](https://github.com/skot/ESP-Miner/blob/v2.0.2/main/tasks/power_management_task.c#L147) function, the minimum fan speed is based on `result` set to 25 when the chip temperature is below 50 degrees c.

In my case, this set the fan speed to ~ 2150RPM (for a Noctua NF-A4x10 5V PWM) on a cold start of the Bitaxe. As the chip temperature iincreases (say from starting at 36c), it reaches 50c at which point `result` is set to 0, causing the fan to stop spinning, and the chip temperature to rise rapidly to the threshold temperature before the fan starts spinning fast enough to cool it down.

Formula should be changed to `result = ((chip_temp - min_temp) / range) * 75 + 25;` for the expected fan speeds to be calculated correctly
