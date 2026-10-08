# bitaxeorg/ESP-Miner issue #1770: AxeOS www.bin update stuck on v2.12.2 after uploading v2.14.0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1770
> Collected: 2026-10-07
> Published: 2026-06-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1770
- State: closed
- Author: balowner
- Opened: 2026-06-17
- Closed: 2026-06-17
- Labels: none

## Description

**Describe the bug**
After updating ESP-Miner firmware to v2.14.0, the AxeOS (www.bin) remains on v2.12.2 despite uploading the v2.14.0 www.bin file multiple times. The dashboard shows the warning: "Firmware (v2.14.0) and AxeOS (v2.12.2) versions do not match."

**To Reproduce**
1. Go to Update page
2. Download both esp-miner.bin and www.bin from v2.14.0 release
3. Upload esp-miner.bin via "Update Firmware" → success, firmware updates to v2.14.0
4. Upload www.bin via "Update AxeOS" → upload appears to complete but AxeOS remains on v2.12.2
5. Repeated the www.bin upload multiple times, same result
6. Rebooted device, no change

**Expected behavior**
AxeOS should update to v2.14.0 matching the firmware version.

**Screenshots & Photos**
<img width="1531" height="89" alt="Image" src="https://github.com/user-attachments/assets/2a88453d-4fda-4bdb-be39-64888c8965e2" />

**Hardware (please complete the following information):**
- Bitaxe HW version: Gamma 602
- ESP-Miner FW version: v2.14.0 (previously v2.12.2)
- Hash Frequency: 750 MHz
- Voltage: 1150 (Default)
- ASIC Type: BM1370

## Comments

### ghost on 2026-06-17

Check the files you downloaded. There might be old versions of esp-miner.bin and/or `www.bin` in your download folder.

Delete the files from your PC and download them again within AxeOS or get them from the link below and flash them both again - `www.bin` first. 
https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.14.0

### balowner on 2026-06-17

@STSMiner1  Great, thanks! I downloaded it directly via AxeOS, and it seems an old file was listed there. It worked using your link. I'm really grateful to you!
