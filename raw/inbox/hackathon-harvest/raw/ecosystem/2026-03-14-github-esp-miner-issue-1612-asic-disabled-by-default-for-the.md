# bitaxeorg/ESP-Miner issue #1612: ASIC disabled by default for the 204

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1612
> Collected: 2026-10-07
> Published: 2026-03-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1612
- State: closed
- Author: jayrmotta
- Opened: 2026-03-14
- Closed: 2026-03-15
- Labels: none

## Description

Boards flashed with the 204 NVS won't start hashing once it's ready.

Steps to reproduce the behavior:
1. Flash a board with a binary (I used the latest release tag) using the 204 NVS file
2. Setup network and pool config
3. Restart and go to the logs page

**Expected behavior**
Everything from bootstrap to job negotiation with the pool will look normal, except you'll never see a share found.

The dashboard will report no hashrate.

**Hardware:**
 - Bitaxe HW version: Ultra 204 / LV06
 - Bitaxe HW vendor: LuckyMiner
 - ESP-Miner FW version: 2.13.1
 - Hash Frequency: 550mhz
 - Voltage: 1250mv

**Additional context**

The image below reflects it running normally before flashing the new version:

<img width="3127" height="758" alt="Image" src="https://github.com/user-attachments/assets/3a3a08de-28ac-4ec2-a0fc-e0e5597be8be" />

After some research I found out that the 204 doesn't have the property `asic_enable` set to true as many others do. My source: https://github.com/bitaxeorg/ESP-Miner/blob/master/main/device_config.h#L130.

I understand these devices have some background with the community, right now I'm just trying to help a friend who owns one of those and had a vulnerable/old firmware running.

As documented here https://gist.github.com/jayrmotta/c976b85e86ab239f42409cd73d8934ec I simply enabled it and then I got the latest binaries to work with that board.


## Comments

### mutatrum on 2026-03-15

Relevant discussion here: https://github.com/bitaxeorg/ESP-Miner/pull/857#pullrequestreview-2780895664

The problem is that we don't know if LM actually built the 204 following the released version, so first of all, ping them to supply an updated firmware or a working config to flash.

### mutatrum on 2026-03-16

To follow-up: I forgot that I had a 204 here, and that's running fine with the current firmware. So it looks like either your device is not a 204, or something else is different. You can try and flash it as a 205, as the only difference in hardware configuration is the `asic_enable` pin.

### jayrmotta on 2026-03-16

Hey @mutatrum, that's funny because as I stated before, this [gist](https://gist.github.com/jayrmotta/c976b85e86ab239f42409cd73d8934ec) is what I did to make the latest ESP-miner tag to work with that hardware, if you see in the gist the `asic_enable` pin is not set for the 204.

You can also find it is not enabled [in the main branch](https://github.com/bitaxeorg/ESP-Miner/blob/master/main/device_config.h#L130).
