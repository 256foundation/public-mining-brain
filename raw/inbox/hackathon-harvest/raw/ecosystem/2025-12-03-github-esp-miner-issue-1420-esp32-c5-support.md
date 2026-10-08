# bitaxeorg/ESP-Miner issue #1420: ESP32-C5 support

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1420
> Collected: 2026-10-07
> Published: 2025-12-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1420
- State: closed
- Author: rcfibersolutions
- Opened: 2025-12-03
- Closed: 2025-12-03
- Labels: none

## Description

Just wandering if or when esp32 c5 may get developed? 

It would be great to have wifi 6 and 5Ghzs spectrum.

Thanks

## Comments

### mutatrum on 2025-12-03

The ESP32-C5-WROOM-1 is roughly equivalent in size, however it has a lot less pins, and also only a single core. I think it has enough pins and covers the functionality to control everything a Bitaxe needs, but not 100% sure on this. Many pins are in a different locations. so the minimal effort would be a re-routing of the board. It would then also need a custom firmware, and it's not clear if the single core on the C5 is powerful enough to run the current firmware.

However, IMO 5Ghz is not useful for a Bitaxe. There's hardly any data transfer, so speed wise 2.4Ghz is sufficient, and it has better wall penetration, especially with the tiny antenna on the device. The only use-case would be if you want to phase out all 2.4 Ghz Wi-Fi in a location, but almost all routers do both anyways.

As far as I know nobody is planning or working on this. Of course, you are free to do so, if you have experience in designing electronics. Just make sure to open-source the results!
