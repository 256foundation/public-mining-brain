# bitaxeorg/ESP-Miner issue #1186: random device overheats when rapidly restarting axe

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1186
> Collected: 2026-10-07
> Published: 2025-08-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1186
- State: closed
- Author: 0xf0xx0
- Opened: 2025-08-11
- Closed: 2025-10-27
- Labels: bug

## Description

**Describe the bug**
When restarting your axe multiple times (say, its flatlining and refusing to come back up), sometimes itll complain about a device overheat that never happened.

**To Reproduce**
Steps to reproduce the behavior:
1. Reboot the axe multiple times
2. eventually itll go into overheat mode

**Expected behavior**
The axe shouldnt trip overheat mode.


**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 602
 - Bitaxe HW vendor: GekkoScience
 - ESP-Miner FW version: 72be37b0 (v2.10.0b2)
 - Hash Frequency: 550
 - Voltage: 1065

**Additional context**
Unsure how to consistently reproduce this, i tend to get it after restarting from a power fault.


## Comments

### skot on 2025-08-19

I have seen this too. There is some sort of race condition at boot with reading the temp sensors and I2C init.

### Rulpen on 2025-09-04

This happens with my Gammas since v2.8.x

### 0xf0xx0 on 2025-10-03

> I have seen this too. There is some sort of race condition at boot with reading the temp sensors and I2C init.

i think i just encountered a related issue, my axe was happily hashing away after a flash and the asic temp was nil, resulting in the minimum fan speed being used. i probably shouldve let it heat up a little longer to see if itd wake up, but risking a chip probably isnt worth it x3 vreg temp was just fine though.

### skot on 2025-10-03

> i think i just encountered a related issue, my axe was happily hashing away after a flash and the asic temp was nil, resulting in the minimum fan speed being used. i probably shouldve let it heat up a little longer to see if itd wake up, but risking a chip probably isnt worth it x3 vreg temp was just fine though.

nil as in 0 or -1? 

Both of these are not real ASIC temps; we should have the fan running at full speed in these cases.



### 0xf0xx0 on 2025-10-03

nil as in the ui displayed `--`, so likely -1 (i didnt check the api)

### skot on 2025-10-03

> nil as in the ui displayed `--`, so likely -1 (i didnt check the api)

ah okay. in the case we should defintiely default the fan to full speed. @WantClue
