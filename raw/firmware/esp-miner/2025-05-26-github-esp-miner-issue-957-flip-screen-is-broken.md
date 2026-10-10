# bitaxeorg/ESP-Miner issue #957: Flip screen is broken

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/957
> Collected: 2026-10-07
> Published: 2025-05-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 957
- State: closed
- Author: mutatrum
- Opened: 2025-05-26
- Closed: 2025-05-26
- Labels: none

## Description

Currently the flip screen functionality results in a garbled screen. Somewhere between `v2.7.1` and `dev-latest` it broke. It might be a dependency upgrade, or something changed in the display code.

![Image](https://github.com/user-attachments/assets/11747741-3461-4809-83d8-5504519ede2d)

## Comments

### ghost on 2025-05-26

PR#938 seems to be the cause for it, before that was added it was fine.

Test firmwares

https://github.com/bitaxeorg/ESP-Miner/actions/runs/15171558009  (with PR#938)

https://github.com/bitaxeorg/ESP-Miner/actions/runs/15169264355  (PR#928 without PR#938)

![Image](https://github.com/user-attachments/assets/e16d280f-be0d-40f7-b301-02f68d760cb0)

Firmware -> PR#928 - flipped with no issue with display.

![Image](https://github.com/user-attachments/assets/4a7762bc-290e-4d71-8003-8be665af88e8)

### mutatrum on 2025-05-26

Fixed by #958
