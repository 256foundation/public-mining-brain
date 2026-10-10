# bitaxeorg/ESP-Miner issue #1765: Cannot update from v2.12.2 on Gamma 601

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1765
> Collected: 2026-10-07
> Published: 2026-06-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1765
- State: closed
- Author: Mambo430
- Opened: 2026-06-15
- Closed: 2026-06-22
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
The unit does not update to latest firmware. It remains on v2.12.2 after using either the onboard update tool or downloading manually from Github. I receive no errors and it goes all the way through to 100%. I have restarted and cold booted the miner. No success. 

**To Reproduce**
Steps to reproduce the behavior:
1. Go to 'Update'
2. Click on 'Check'
3. Download both 'esp-miner.bin and www.bin'
4. Update AxeOS with the downloaded 'www.bin'
5. Update Firmware with downloaded 'esp-miner.bin'

**Expected behavior**
Both the AxeOS and Firmware Updates show 100% and reboot. Latest firmware expected to be loaded.

**Screenshots & Photos**
<img width="1665" height="791" alt="Image" src="https://github.com/user-attachments/assets/d423e951-e4b9-4582-9679-ea7e62738eb8" />
<img width="1667" height="788" alt="Image" src="https://github.com/user-attachments/assets/bb9971f1-7329-42c0-8c34-1963255cab53" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: Geek Science Edition
 - ESP-Miner FW version: v2.12.2
 - Hash Frequency: 800
 - Voltage: 1150
 - Pool URL, Port, User: public-pool.io, 3333, bc1qyfwz22rrwxucxeyh2754cjhkstyj6hsfgkknfj.bitaxe

**Additional context**
I have tried to use the v2.13.0 as well but it does not take. Same results.

## Comments

### mutatrum on 2026-06-16

Double check the files you downloaded. There might be old versions of `esp-miner.bin` and/or `www.bin` in your download folder. Otherwise you can also use the [webflasher](https://bitaxeorg.github.io/bitaxe-web-flasher/). Just make sure to select 'Keep configuration', otherwise you'll wipe all your settings.

### WantClue on 2026-06-19

Please report back if Mutatrum's instructions helped, otherwise this issue will automatically be closed

### Mambo430 on 2026-06-22

> Double check the files you downloaded. There might be old versions of `esp-miner.bin` and/or `www.bin` in your download folder. Otherwise you can also use the [webflasher](https://bitaxeorg.github.io/bitaxe-web-flasher/). Just make sure to select 'Keep configuration', otherwise you'll wipe all your settings.

Webflasher worked. Thank you.
