# bitaxeorg/ESP-Miner issue #1631: Device frequency is set low - See settings

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1631
> Collected: 2026-10-07
> Published: 2026-03-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1631
- State: closed
- Author: igiannako
- Opened: 2026-03-24
- Closed: 2026-03-26
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
Regardless of the device Frequency parameter set, the settings drops to minimum value (385 for a 2yo Bitaxe Ultra).

**To Reproduce**
Nothing in particular. I change the frequency to default 485, save, restart, and after a couple of minutes drops to 385 (minimum)

**Expected behavior**
Frequency should be remain as set.

**Screenshots & Photos**

<img width="1521" height="1067" alt="Image" src="https://github.com/user-attachments/assets/1b5817d8-d619-4cc0-aea5-6a0ac9f58edc" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: Ultra 205
 - Bitaxe HW vendor: Bitronics (2yo device)
 - ESP-Miner FW version: v2.13.1
 - Hash Frequency: 485 (Default)
 - Voltage: 1200 (Default)
 - Pool URL, Port, User: localhost

**Additional context**
Add any other context about the problem here.


## Comments

### mutatrum on 2026-03-24

Can you open a tab with the logs, set the frequency to default and see if you can catch whatever happens when it goes back to 385?

### ghost on 2026-03-25

I've not seen this issue here on my Ultra 205 (from Solosatoshi).



### WantClue on 2026-03-26

This appears to be because your device is overheating. You should check your heatsink and thermalpaste. If your device overheats it will lower the frequency by 100 which is exactly what you are experiencing
