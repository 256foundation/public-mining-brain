# bitaxeorg/ESP-Miner issue #39: Asic model invalid

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/39
> Collected: 2026-10-07
> Published: 2023-10-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 39
- State: closed
- Author: Dolu89
- Opened: 2023-10-02
- Closed: 2023-10-02
- Labels: none

## Description

I tried to flash my bitaxe to the latest version but I now got Invalid asic model on the screen.
Model is BM1397

It's broken since this commit https://github.com/skot/ESP-Miner/commit/706ee510ba509d9a04445e87a3d426ddaccd9f98
It works great on the previous one (bc4afd39b70b874ed5ab2743dddde888670b908b)

Tell me if you need more info, I don't know what to provide


## Comments

### johnny9 on 2023-10-02

You need to write manufacturing data into flash once. Specifically the field "asicmodel". You can use bitaxetool to write this info. Documentation will be coming shortly but if you need more info check the OSMU discord.
