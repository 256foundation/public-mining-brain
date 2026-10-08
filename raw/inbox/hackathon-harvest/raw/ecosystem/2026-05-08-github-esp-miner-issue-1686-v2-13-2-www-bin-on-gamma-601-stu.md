# bitaxeorg/ESP-Miner issue #1686: v2.13.2 www.bin on Gamma 601 - stuck in recovery

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1686
> Collected: 2026-10-07
> Published: 2026-05-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1686
- State: closed
- Author: dskvr
- Opened: 2026-05-08
- Closed: 2026-05-28
- Labels: none

## Description

**Describe the bug**
Went to update, it stopped at 18% I waited 24 hours, refreshed page, got recovery screen:

<img width="522" height="404" alt="Image" src="https://github.com/user-attachments/assets/cf25495f-f082-4781-938e-17cd6b4f8afa" />

Upon attempting to update from recovery, same thing happens, never get a response.

Miner was working fine and hashing for a year before this. 

**To Reproduce**
Probably not relevant

**Expected behavior**
www.bin update doesn't brick device 

**Screenshots & Photos**
above

**Hardware (please complete the following information):**
Gamma 601
don't remember the vendor
didn't write down the fw version before brick

**Additional context**
running consistently for a year, specifically, the bitaxe that bricked was amongst of my most stable bitaxes. 

I guess reflowing an esp32 is my only option? 

## Comments

### mutatrum on 2026-05-08

Can you try to use the webflasher? https://bitaxeorg.github.io/bitaxe-web-flasher

If it doesn't want to connect, try powering it on while pressing the boot button. This should put it in bootloader mode.

It is very hard to brick the ESP, so you probably just have to re-flash the device.

### WantClue on 2026-05-28

please use the webflasher as descirbed above if the issue persists please reopen another issue
