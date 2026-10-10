# bitaxeorg/ESP-Miner issue #761: Deal with RGB LEDs on bitaxeMax models

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/761
> Collected: 2026-10-07
> Published: 2025-03-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 761
- State: closed
- Author: skot
- Opened: 2025-03-11
- Closed: 2025-03-18
- Labels: bug, enhancement, good first issue

## Description

The old [bitaxeMax](https://github.com/bitaxeorg/bitaxemax) models have two RGB LEDs. We never really used them, but some recent firmware change caused the `X` LED to be on a steady yellowish green. At the very least we should turn off LEDs on models that have them.

<img width="1606" alt="Image" src="https://github.com/user-attachments/assets/e559ed19-3a57-4d45-b6ac-62e6489b5ab8" />

## Comments

### skot on 2025-03-11

<img width="692" alt="Image" src="https://github.com/user-attachments/assets/5e21d945-6da0-4004-bbc9-92b78685af70" />

### skot on 2025-03-11

Bonus challenge is to make the LEDs do something cool, like flash when a share is submitted (ala the bitHalo). But make sure to properly abstract this HW-specific code in esp-miner

### WantClue on 2025-03-13

I think we removed a big portion of the code associated to the LEDs so it would be helpful to look into old commits

### skot on 2025-03-18

Well.... it looks like I used the same pins for the right LED (LEDX) that are used for Octal SPI (GPIO35, 36, 37) Which is used for PSRAM on the ESP32-S3-WROOM-1 module. It looks like the few bitaxeMax users out there are going to have to deal with the LED being on, or stay with with way old firmware from before we were using PSRAM.

<img width="698" alt="Image" src="https://github.com/user-attachments/assets/5f966123-4933-4251-ac3e-f39aa44fd464" />

<img width="680" alt="Image" src="https://github.com/user-attachments/assets/3c382b5c-602e-41ad-ac0a-0a54246f255f" />
