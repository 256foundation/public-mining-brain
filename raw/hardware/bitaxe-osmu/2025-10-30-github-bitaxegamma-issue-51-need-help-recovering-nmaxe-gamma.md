# bitaxeorg/bitaxeGamma issue #51: Need help recovering NMAxe Gamma BM1370 after wrong firmware flash

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/51
> Collected: 2026-10-07
> Published: 2025-10-30

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 51
- State: closed
- Author: antoniocantinebellini-collab
- Opened: 2025-10-30
- Closed: 2025-10-30
- Labels: none

## Description

Hi everyone,
I accidentally flashed my NMAxe Gamma BM1370 (ESP32-S3) miner using ESPHome, and since then the OLED screen and Wi-Fi stopped working.

I can still access the board in bootloader mode (shows up as USB Serial Device (COM3) with VID:PID 303A:1001) and I’ve tried flashing several firmware and spiffs files from v2.9.21, but the device still boots to a black screen and no Wi-Fi.

Could someone please share or confirm the correct display-enabled firmware and spiffs offsets for my board?

I’ve already used esptool to erase the flash and can reflash both .bin files manually, I just need to make sure I’m using the proper images.

Thanks a lot for your help — I really appreciate the amazing work you all do with NMAxe!

## Comments

### skot on 2025-10-30

This is not the NMAxe project, sorry!
