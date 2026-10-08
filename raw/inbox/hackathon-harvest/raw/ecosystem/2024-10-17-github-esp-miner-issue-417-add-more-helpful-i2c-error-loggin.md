# bitaxeorg/ESP-Miner issue #417: Add more helpful I2C error logging

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/417
> Collected: 2026-10-07
> Published: 2024-10-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 417
- State: closed
- Author: skot
- Opened: 2024-10-17
- Closed: 2025-04-01
- Labels: enhancement

## Description

The new I2C library doesn't provide very helpful I2C error logging. Here is what we see with a missing OLED;
<img width="723" alt="image" src="https://github.com/user-attachments/assets/e4d4a489-7f22-476c-ae8e-be93557ba1b0">

We can probably change this to log which device the I2C transaction failed on.

## Comments

### mutatrum on 2025-04-01

Fixed by #552
