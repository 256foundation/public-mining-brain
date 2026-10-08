# bitaxeorg/ESP-Miner issue #1679: v2.14.0b1 - Under "System" tab, CPU usage displays as a negative value

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1679
> Collected: 2026-10-07
> Published: 2026-04-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1679
- State: closed
- Author: Hylinus
- Opened: 2026-04-26
- Closed: 2026-04-26
- Labels: none

## Description

**Describe the bug**
Randomly, when at the "System" tab, the CPU usage is displayed as a negative value. Refreshing the page doesn't change the value, but it will randomly reset back to a positive value.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to 'System' tab
2. Observe the "CPU Usage" value
3. Randomly, the value displayed is a negative number. Once that happens, opening the "System" tab for the same miner on a different browser will display the "CPU Usage" value as negative.

**Expected behavior**
The "CPU Usage" value should display as a positive integer.

**Screenshots & Photos**
"CPU Usage" displaying as negative value:
<img width="164" height="138" alt="Image" src="https://github.com/user-attachments/assets/fb756139-0f98-4731-bb77-3ab0ef6f29fe" />

"CPU Usage" for the same miner after it "resets" back to a positive value. Unknown how to reset.
<img width="184" height="154" alt="Image" src="https://github.com/user-attachments/assets/66033a27-90c7-4057-8c7d-d14929081b77" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: Altair Tech
 - ESP-Miner FW version: v2.14.0b1
 - ESP-IDF: v5.5.3
 - Hash Frequency: 980
 - Voltage: 1375


## Comments

### WantClue on 2026-04-26

this has been fixed and will be available in the next beta very soon
