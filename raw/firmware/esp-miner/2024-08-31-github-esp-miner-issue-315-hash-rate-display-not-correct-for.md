# bitaxeorg/ESP-Miner issue #315: Hash rate display not correct for graphing

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/315
> Collected: 2026-10-07
> Published: 2024-08-31

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 315
- State: closed
- Author: zcht
- Opened: 2024-08-31
- Closed: 2024-10-10
- Labels: none

## Description

**Describe the bug**
With higher ASIC clock rates and therefore higher hash rates for a bitaxis, the scaling of the display is not output correctly. This example shows a Bitaxe Supra with the current 2.1.10 firmware. In my case, a hash speed range between 900-1430 Gh/s is delivered. See corresponding markings. 

**To Reproduce**
Steps to reproduce the behavior:

**Caution, only carry out steps with sufficient cooling to avoid damage.** 

1. Set 800 Mhz and 1.375 vCore
1. Switch to the dashboard and wait until the hash speed is displayed in the graph

**Screenshots & Photos**
<img width="935" alt="anzeige" src="https://github.com/user-attachments/assets/2c813660-4cb5-448e-9d73-437dfbeca17d">

**Hardware:**
 - Bitaxe HW version: Supra 400 - BM1368
 - Bitaxe HW vendor: D-Central
 - ESP-Miner FW version: 2.1.10
 - Hash Frequency: 800
 - Voltage: 1.375
 - Pool URL, Port, User: solo ckpool or publicpool



## Comments

### mrv777 on 2024-09-28

I'll add if the number is under 10 to show 2 decimal places, I think that will be good then
