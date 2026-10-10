# bitaxeorg/ESP-Miner issue #166: Bitaxe Supra 400 - "Gh*: 0.0 W/Th: inf"

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/166
> Collected: 2026-10-07
> Published: 2024-04-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 166
- State: closed
- Author: Vincnet64
- Opened: 2024-04-21
- Closed: 2024-04-21
- Labels: none

## Description

Hello,

**Describe the bug**
I received my Bitaxe Supra 400 the last week, i applied the configuration notice and **it worked only 2 days without touching**. Since the screen displays "**Gh*: 0.0 W/Th: inf**" or "****Gh*: 0.0 W/Th: nan****" and I have sometime "Input Voltage Danger: Low voltage" on AxeOS web page.

**To Reproduce**
I dont know... 

**Expected behavior**
Bitaxe working with a Hashrate.

**Screenshots & Photos**
![thumbnail_IMG_3670](https://github.com/skot/ESP-Miner/assets/167650758/bebca526-36fc-43ee-a540-3a3f35b561bb)

**Hardware (please complete the following information):**
 - Bitaxe Supra 400 (model (1368)
 - PSU: EU 5V 4A
 - Bitaxe HW vendor: D central tech 
 - ESP-Miner FW version: 2.1.0 intial 
 - Pool URL, Port, User: Public-pool.io 21496

**Additional context**
I thought it was coming from the firmware, so I upgraded to V2.1.3 but nothing changed. Then I tried to flash it via https://wantclue.github.io/bitaxe-web-flasher/, by clicking on "Bitaxe Supra" but the screen of the Bitaxe, i had "**Auto test, Power: Fail**", then I I tried to clean everything via ESP Tool (espressif.github.io), then put back the "esp-miner-factory-401-v2.1.0.bin" and I came back to my original problem with the display " **Gh*: 0.0 W/Th: nan**".

Could you help me because I'm lost. Does this power supply need to be changed (I am in France) ? Is it coming from the firmware? I appreciate your help....

Thx
Vincent

## Comments

### MyOwn2C on 2024-04-21

Bad power supply. Change to a new one, at least 20W or higher. 

### skot on 2024-04-21

Please reach out on the OSMU Discord for tech support. https://discord.gg/osmu
