# bitaxeorg/ESP-Miner issue #1498: 800xxx not reporting correctly in FW 2.12.2

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1498
> Collected: 2026-10-07
> Published: 2026-01-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1498
- State: closed
- Author: GitFerretKG
- Opened: 2026-01-10
- Closed: 2026-01-11
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
Fan speed and RPM not reported at all/correctly
Input voltage and power not reported at all/correctly
ASIC 1, ASIC 2, voltage regulator temperature not reported at all/correctly


**To Reproduce**
Steps to reproduce the behavior:
1. Flashed from 2.12.0 to 2.12.2, issue occurred
2. Reverted back to 2.12.0, issue corrected
3. Tried on more flash to 2.12.2, problem reoccurred
4. Seems to be the FW ESP file only, AxeOS 2.12.0 or 2.12.2 made no difference

<img width="780" height="633" alt="Image" src="https://github.com/user-attachments/assets/9d54cac8-d6b0-403c-ac8b-4428a96b7c46" />
<img width="1619" height="902" alt="Image" src="https://github.com/user-attachments/assets/a59067cf-2549-4a62-b7b3-3094a9deab0f" />
<img width="1616" height="886" alt="Image" src="https://github.com/user-attachments/assets/060a4926-7970-4c10-857b-883939f3307e" />
<img width="1616" height="900" alt="Image" src="https://github.com/user-attachments/assets/906e382e-b44d-44a7-bc9e-de95ea9d7704" />

5. Screen shots

**Expected behavior**
AxeOS to report device data correctly.

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.

**Hardware (please complete the following information):**
Device Model | GammaTurbo
Board Version | 800
ASIC Type | 2x BM1370
Uptime | 20 minutes, 5 seconds
Reset Reason | Software reset via esp_restart
Wi-Fi SSID | CLS
Wi-Fi Status | Connected!
Wi-Fi RSSI | -41 dBm
Wi-Fi IPv4 | 192.168.2.106
Wi-Fi IPv6 | FE80::226E:F1FF:FEA7:AC00
MAC Address | 20:6E:F1:A7:AC:00
Free Heap Memory | 8.21 MB
• Internal | 106 kB
• Spiram | 8.14 MB
Firmware Version | v2.12.0
AxeOS Version | v2.12.0
ESP-IDF Version | v5.5.1
- Hash Frequency: 625 MHz
- Voltage: 1150
- Pool URL, Port, User:
     - americas.mining-dutch.nl:9996
     - BlockFerret.bitaxe800kg

**Additional context**
Will the 800xxx boards/units be supported after FW 2.12.0?


## Comments

### WantClue on 2026-01-11

This device is not supported, it's a development unit that's why it does have xxx in it's model name
