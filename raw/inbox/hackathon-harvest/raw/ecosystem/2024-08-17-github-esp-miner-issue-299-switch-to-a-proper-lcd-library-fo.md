# bitaxeorg/ESP-Miner issue #299: Switch to a proper LCD library for the OLED

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/299
> Collected: 2026-10-07
> Published: 2024-08-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 299
- State: closed
- Author: skot
- Opened: 2024-08-17
- Closed: 2024-12-27
- Labels: enhancement

## Description

Espressif has a ESP-IDF library for LCD that's supports the I2C SSD1306 that we use on the Bitaxe. https://docs.espressif.com/projects/esp-idf/en/v5.2.2/esp32s3/api-reference/peripherals/lcd.html

Example for the I2C SSD1306
https://github.com/espressif/esp-idf/tree/v5.2.2/examples/peripherals/lcd/i2c_oled

## Comments

### mutatrum on 2024-10-23

LVGL?

### mutatrum on 2024-12-12

Fixed with #539
