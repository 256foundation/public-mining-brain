# bitaxeorg/ESP-Miner issue #512: Chip-Temperature 2.3.0 -> 2.4.0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/512
> Collected: 2026-10-07
> Published: 2024-11-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 512
- State: closed
- Author: mark0st83
- Opened: 2024-11-23
- Closed: 2024-11-23
- Labels: none

## Description

I took the plunge yesterday and updated my Gamma 601 to version 2.4.0. Everything seems to have worked so far.

However, the fan is now running much faster than before. The chip temperature is showing about 10 degrees Celsius warmer than before.
Because of this, the fan is running about 2000 RPM faster.

The frequency and voltage remain the same, but this isn’t visible in the 2.3.0 screenshot.

What temperature or operating condition is considered correct now?

![IMG_5218](https://github.com/user-attachments/assets/5e2ca17a-2402-457a-9434-af3652cedb54)
![IMG_5217](https://github.com/user-attachments/assets/9f068650-9f07-4dd9-8357-67cbd2c9ff53)


## Comments

### ghost on 2024-11-23

2.4.0 fixes an issue with temps being under reported in 2.3.0.

https://github.com/skot/ESP-Miner/pull/484

### mark0st83 on 2024-11-23

Ok, so the 45 degrees reported in 2.3.0 was wrong? Ok thats a lot „inaccurat“ 😅

### skot on 2024-11-23

Gamma ASIC temperature measurement before v2.4.0 was incorrect. It could be too high or too low.

### mark0st83 on 2024-11-23

Thank you for the clearification
