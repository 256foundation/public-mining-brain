# bitaxeorg/ESP-Miner issue #1499: BitAxe GT not showing Power, Voltage, Heat, Fan RPM

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1499
> Collected: 2026-10-07
> Published: 2026-01-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1499
- State: closed
- Author: Ty-Stelow
- Opened: 2026-01-10
- Closed: 2026-01-11
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
When updating to v2.12.2 on the BitAxe Gamma Turbo the below listed items on the dashboard did not work: 

(See Screen Shots)

1. Power
2. Input Voltage
3. ASIC Temparature
4. Fan RMS

**To Reproduce**
Steps to reproduce the behavior:
Common updating of the  esp-miner.bin then the www.bin

**Expected behavior**
The Dashboard visulations show the correct information

**Screenshots & Photos**

<img width="1900" height="958" alt="Image" src="https://github.com/user-attachments/assets/8de6f92d-610f-4efa-b304-231e736945f4" />
<img width="1894" height="954" alt="Image" src="https://github.com/user-attachments/assets/0586846a-45a3-48a8-8cbb-8b6632f26561" />

**Hardware (please complete the following information):**
See Attachment:

<img width="673" height="677" alt="Image" src="https://github.com/user-attachments/assets/3c4c247c-e6ba-4ad3-b531-e33e4d3f67c5" />

**Additional context**
After updating the fan ran a full speed but the miner conituned to contrubute shares.  It should be noted that this was on my local DigiByte Node. 


## Comments

### WantClue on 2026-01-11

The board 800 is not supported and was only for development so are all the x versions

### Ty-Stelow on 2026-01-11

So, confiriming there will be no updates for the BitAxe Gamma Turbo?
