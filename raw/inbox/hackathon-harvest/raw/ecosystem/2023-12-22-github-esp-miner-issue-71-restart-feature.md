# bitaxeorg/ESP-Miner issue #71: Restart-Feature

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/71
> Collected: 2026-10-07
> Published: 2023-12-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 71
- State: closed
- Author: ray77
- Opened: 2023-12-22
- Closed: 2024-01-05
- Labels: none

## Description

Interrupting the power supply works much better than the "Restart button" in the front end of ESP-Miner. Some errors, like "Danger: Voltage too low" only occures after a soft reset, but not after restarting via power supply.

## Comments

### WantClue on 2024-01-05

> Interrupting the power supply works much better than the "Restart button" in the front end of ESP-Miner. Some errors, like "Danger: Voltage too low" only occures after a soft reset, but not after restarting via power supply.

This restart button does exactly the same as a "hard" reset via power supply. It forces the ESP to reboot and reestablish a connection with the ASIC. The "Voltage too low" occurs every time the power measure meter detect too low voltage. This behavior will be changed in future versions and lowered before actually displaying this issue.
