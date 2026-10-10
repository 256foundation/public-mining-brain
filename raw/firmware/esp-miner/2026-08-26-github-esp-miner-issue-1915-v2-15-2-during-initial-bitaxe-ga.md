# bitaxeorg/ESP-Miner issue #1915: v2.15.2: During Initial Bitaxe Gamma 601 Setup, Scanning WiFi Caused Setup Device to Disconnect

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1915
> Collected: 2026-10-07
> Published: 2026-08-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1915
- State: open
- Author: cbkhoo1492006
- Opened: 2026-08-26
- Closed: n/a
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
1. Factory flash Bitaxe Gamma 601 (v2.15.0) without retaining configuration.
2. Connect to it (Bitaxe_XXXX), then on web configuration page, click Scan. 

**Expected behavior**
After click Scan, after awhile, should shown a list of WiFi SSID in range to be selected.
But, while scanning, suddenly setup device (android/computer) get disconnected by itself, need to manually connect to it again. (It never return WiFi SSID list.)
Proceed to try scan again, but end up being get disconnected again.
Solution, is to manually keyin the SSID to complete initial setup.

After initial setup completed (601 successfully connected to WiFi), hold boot for 5 seconds, to go to initial WiFi configuration. But this is seem not affected, as device return list of scanned WiFi SSID in range and setup device does not get disconnected.

Tested on v2.14.2 and it does not affected by this issue. This probably true for any version below it but can't confirm it as I have not tested it.

**Hardware (please complete the following information):**
 - Bitaxe HW version: Bitaxe Gamma 601
 - Bitaxe HW vendor: Minerfixes
 - ESP-Miner FW version: v2.15.0
 - Hash Frequency: 525 MHz (Default)
 - Voltage: 1150mV (Default)
