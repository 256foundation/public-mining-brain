# bitaxeorg/ESP-Miner issue #1365: Feature Request - Support for W5500 Ethernet module

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1365
> Collected: 2026-10-07
> Published: 2025-11-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1365
- State: open
- Author: CryptoTech-Guy
- Opened: 2025-11-18
- Closed: n/a
- Labels: wontfix

## Description

Using LAN instead of WiFi can provide faster and more stable connection with less latency.
It's currently supported by the great work done in [this repo](https://github.com/CryptoIceMLH/ESP-Miner-NerdQAxePlusLAN)
(Tnx to @CryptoIceMLH and @shufps )

It will be great if we can have official support for the W5500 and this work can be merged into the official firmware.

Tnx!

## Comments

### shufps on 2025-11-24

small disclaimer, I had and have and will have nothing to do with CryptoIces project^^

### tbshfr on 2025-11-28

I created a cleaner fork that preserves the git history and aims to be more maintainable: [ESP-Miner-Lan](https://github.com/tbshfr/ESP-Miner-Lan). 
If ethernet support is within the scope of this project, I can open a pull request. 
There would need to be some changes, like checking whether UART or SPI should be initialized, but i think it would be managable. 
Its also only tested on the bitaxe 601, so it should probably only be initialized on devices that have been tested.
If its not in scope of this project, i will  try to keep the fork up to date
