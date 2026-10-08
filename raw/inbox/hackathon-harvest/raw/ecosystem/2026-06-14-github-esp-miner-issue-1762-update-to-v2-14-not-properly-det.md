# bitaxeorg/ESP-Miner issue #1762: Update to v2.14 not properly detected ?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1762
> Collected: 2026-10-07
> Published: 2026-06-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1762
- State: closed
- Author: RastaTaz
- Opened: 2026-06-14
- Closed: 2026-06-14
- Labels: none

## Description

**Describe the bug**
After update firmware and AxeOS to v2.14.0 on BitAxe Gamma, AxeOS update not properly detected resulting in a warning on dashboard page for versions mismatch (OS vs firmware).
Indeed: AxeOS version stuck to previous one (v2.13.1) : see screenshot in appropriate section of issue.

Tried to upload several times the www.bin file (download via WebUI link or on the Github release page) without any change in this behaviour.

**To Reproduce**
Steps to reproduce the behavior:
On BitAxe Gamma device in version 2.13.1 (OS & firmware):
1. Update Firmware to v2.14.0
2. Update AxeOS to v2.14.0
3. Connect to dashboard page
4. See error

**Expected behavior**
No version mismatch message on dashboard & system pages.

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.
<img width="1518" height="151" alt="Image" src="https://github.com/user-attachments/assets/a703b6d4-a42d-4977-a4eb-599bd78a4dfe" />

<img width="472" height="594" alt="Image" src="https://github.com/user-attachments/assets/850966c1-e44f-44f3-af0d-e0c1bb4016b7" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma
 - Bitaxe HW vendor: Unknow (Amazon or Aliexpress, can't remember...)
 - ESP-Miner FW version: v2.14.0
 - Hash Frequency: 1.4 Th/s
 - Voltage: 1.15v
 - Pool URL, Port, User: public-pool.io:21496

**Additional context**
Not much that I found pertinent, but don't hesitate to ask, I'll be glad to contribute

## Comments

### WantClue on 2026-06-14

Please try to reflash the www.bin and the esp-miner.bin this should resolve it

### RastaTaz on 2026-06-14

Hi @WantClue ,
Thanks for taking time to answer my issue.

Although I already tried to reflash www.bin several times before, I did what you advised:
1. flash www.bin
2. flash esp-miner.bin after the auto-restart from previous flash

=> No more warning on dashboard page to be seen and version for AxeOS is now v2.14.0 in system page.
So your resolution worked out of the box: thanks a lot !
