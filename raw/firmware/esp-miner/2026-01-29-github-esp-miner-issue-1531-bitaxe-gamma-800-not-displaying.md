# bitaxeorg/ESP-Miner issue #1531: Bitaxe Gamma 800 not displaying temperatures due to out of range readings

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1531
> Collected: 2026-10-07
> Published: 2026-01-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1531
- State: closed
- Author: jdmcroy
- Opened: 2026-01-29
- Closed: 2026-01-29
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
After updating from v2.13.0b1 to v2.13.0b2 the dashboard stopped displaying teperatures correctly.
The log file shows the following issue:

![Image](https://github.com/user-attachments/assets/b9840a96-e1d7-4a71-9c64-bf96f9d99877)
![Image](https://github.com/user-attachments/assets/9343c172-925d-496e-adf0-e2a5c5cecdd1)

power_management: Ignoring invalid temperature reading: -1.0 °C

**To Reproduce**
Steps to reproduce the behavior:
1. Update from v2.13.0b1 to v2.13.0b2


**Expected behavior**
Dashboard teperatures should be displayed.

**Screenshots & Photos**
![Image](https://github.com/user-attachments/assets/208dc9ca-faf7-4109-a95a-21e06adb6f0f)
![Image](https://github.com/user-attachments/assets/f4976c06-9704-4f07-90e7-88459c702a2d)

**Hardware (please complete the following information):**
 - Bitaxe HW version: Bitaxe Gamma 800
 - Bitaxe HW vendor: Amazon vendor Zorvionix
 - ESP-Miner FW version: v2.13.0b2
 - Hash Frequency: 2.5TH/s
 - Voltage: Input 12vdc, ASIC 1.19vdc
 - Pool URL, Port, User: solo.ckpool.org, 3333, 3GCi32MAesPCm5nzTDambSoiu4zuSeH3uR.My-Bitaxe-1

**Additional context**
Seems like any version above v2.11.0-t2 except for v2.13.0b1 which works.


## Comments

### mutatrum on 2026-01-29

Thank you for the extensive report, but unfortunately I'm closing thus as duplicate. See https://github.com/bitaxeorg/ESP-Miner/issues/1521#issuecomment-3787400158 for context.
