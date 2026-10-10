# bitaxeorg/ESP-Miner issue #817: Split hashrate over multiple pools

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/817
> Collected: 2026-10-07
> Published: 2025-04-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 817
- State: closed
- Author: Uefi1
- Opened: 2025-04-02
- Closed: 2025-04-14
- Labels: none

## Description

Hello, I think it would be great to have the option in the settings to split the hashrate of an ASIC across different pools and coins. For example, if I have a speed of 500 GH/s, I would like to be able to allocate 100 GH to 5 different coins, such as BCH, eCash, Space, Fractal Bitcoin, and Peercoin. Or, for instance, allocate 250 GH to two coins, like BCH and eCash.

This would increase profitability because when mining in PROP or PPLNS mode, the reward per block would still be just 1 cent, regardless of whether the device submits shares at 500 GH/s or 10 GH/s. The smallest share will always determine the payout, so having the ability to split hashrate efficiently would be beneficial.

## Comments

### skot on 2025-04-14

This seems like a lot of complexity for minimal benefit -- especially on single chip, low hashrate miners like Bitaxe.

### MyOwn2C on 2025-04-14

This doesn’t make sense. 
Bitaxe is already “slow”
Splitting hash rate will make it even slower. 
A lot of pools will reject slow hash rate devices. 
This will eliminate Bitaxe to participate in lots of pools. 
If a pool accepts slow devices, it is not a pool you want to be in anyway. 

### Uefi1 on 2025-04-14

> This seems like a lot of complexity for minimal benefit -- especially on single chip, low hashrate miners like Bitaxe.

Honestly, I don't see any difference between 500 GH/s and 100 GH/s — in either case, the coin's required difficulty will never be reached, and it's better to rely only on the guaranteed block every 10 minutes. That's why it's better to mine several coins simultaneously at lower speeds rather than just one at the maximum speed ! @skot It would be useful in any case, and those who don't need it could simply continue directing all the power to a single coin. If it's even possible to implement, please make it happen — I'm asking you sincerely.












### zcht on 2025-04-14

Simple solution: buy two (or more) Bitaxe for pool A or B.

### Uefi1 on 2025-04-14

> Simple solution: buy two (or more) Bitaxe for pool A or B.

Hi, well first of all, it costs a significant amount of money — enough to buy a pretty good ASIC with 80-100 terahashes. And secondly, even if we're just talking about one BitAxe, it costs as much as two or three Antminer S9 units, each with 14 terahashes, which is honestly not reasonable at all. I don’t know how you could even suggest something like that, or what’s going on in your head ?












### skot on 2025-04-14

managing multiple pools, their respective work and jobs on a single ASIC with a low power CPU like the ESP32 is going to be very challenging to write for esp-miner.

This would probably be easier to prototype in your own app using [bitaxe-raw](https://github.com/bitaxeorg/bitaxe-raw)
