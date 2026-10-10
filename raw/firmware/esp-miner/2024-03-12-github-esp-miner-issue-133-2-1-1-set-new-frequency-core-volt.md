# bitaxeorg/ESP-Miner issue #133: 2.1.1 set new frequency, core voltage, and fan settings (1366 Ultra)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/133
> Collected: 2026-10-07
> Published: 2024-03-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 133
- State: closed
- Author: Lhowa
- Opened: 2024-03-12
- Closed: 2024-03-15
- Labels: none

## Description

After flashing to 2.1.1 (initial upgrade killed screen from 2.1, flashing to any other factory wont connect to wifi) my Frequency is stuck at 50, voltage at 990, and automatic fan control is switched off with fan speed stuck at 100. I noticed that I can turn auto fan on and save plus restart and it saves the setting. But if I try and update frequency and voltage to 485/1200 everything just reverts back to the above. 

On 2.1 I noticed that my miner was spitting out 0.00 Gh/s and showing as offline in pools. 
<img width="1101" alt="Screenshot 2024-03-12 at 9 05 38 AM" src="https://github.com/skot/ESP-Miner/assets/35153642/497c9a2c-f6eb-4446-b87b-723cc7b1c6d6">


## Comments

### benjamin-wilson on 2024-03-12

This looks like over temp protection

### Lhowa on 2024-03-12

Interesting, just got the card yesterday. Only had this problem on 2.1.1. But when I flash to any other version now it fails to connect to my ssid. 

### TiberiusSky on 2024-03-13

i can not find the fan speed on the new 2.1.1 GUI.
100% is not enough. I need the RPM's !!!
Please ad this again in the next version.

Thanks al lot

### benjamin-wilson on 2024-03-15

You must turn off automatic fan control to see the manual fan speed. Please contact the manufacturer if you continue to have setup issues.
