# bitaxeorg/bitaxe-raw pull request #13: Fixes for bitaxeBonanza raw

> Source: https://github.com/bitaxeorg/bitaxe-raw/pull/13
> Collected: 2026-10-07
> Published: 2026-05-31

- Repository: bitaxeorg/bitaxe-raw
- Type: pull request
- Number: 13
- State: closed
- Author: johnny9
- Opened: 2026-05-31
- Closed: 2026-07-25
- Labels: none

## Description

1. Renamed the product to BitaxeBonanza so it appears different to the normal Bitaxe

2. Adjusted the UART default and setting CDC baud so data to the asic can be sent/read properly.

3. Added gpio pins for the VR on the esp32 side
   - 0x04 = VR_EN get/set, ESP32 GPIO10
   - 0x05 = VR_PGOOD get, ESP32 GPIO11



## Comments

### johnny9 on 2026-07-25

Superseded by #18, which includes these changes plus Bonanza Bridge protocol 1 safety-lease ownership, compatibility handling, and validation with BIRDS `bzmd` on attached hardware.
