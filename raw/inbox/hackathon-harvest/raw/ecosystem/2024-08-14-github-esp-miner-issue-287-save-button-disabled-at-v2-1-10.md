# bitaxeorg/ESP-Miner issue #287: Save-Button disabled at v2.1.10

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/287
> Collected: 2026-10-07
> Published: 2024-08-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 287
- State: closed
- Author: kisenberg
- Opened: 2024-08-14
- Closed: 2024-08-14
- Labels: none

## Description

**Describe the bug**
After update from v2.1.9 to v2.1.10 used provided www.bin and esp-miner.bin, save-button at settings ist disabled.
It only temporaly works after removing the disabled-attribute in code.

**Hardware (please complete the following information):**
 - Bitaxe HW version: Supra 400 and Supra 401
 - ESP-Miner FW version: 2.1.10

## Comments

### WantClue on 2024-08-14

Can you hard reset the bitaxe?
Also if this doesn't help try to factory flash v2.1.10
It could be that this issue is caused by 2.1.9 which we removed for this and many other reasons

### kisenberg on 2024-08-14

Shame on me. After removing PSU and repowering, save button works.
Thank you.
