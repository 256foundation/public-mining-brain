# bitaxeorg/ESP-Miner issue #20: Save "Best Difficulty" scores into NVS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/20
> Collected: 2026-10-07
> Published: 2023-08-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 20
- State: closed
- Author: johnny9
- Opened: 2023-08-30
- Closed: 2023-10-19
- Labels: enhancement, good first issue

## Description

We currently output the device's Best Difficulty (BD) to the OLED screen so users can see their best hash. As a lottery miner, its quite exciting when you hit those big numbers. However, after rebooting the score resets. The goal of this enhancement would be to write our best score into the NVS on the esp.

References:
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/nvs_flash.html?highlight=non%20volatile%20storage
Current nvs storage methods:
https://github.com/skot/ESP-Miner/blob/master/main/nvs_config.h

## Comments

### skot on 2023-08-31

The trick here is to write to flash as infrequently as possible so as not to wear out the flash.

(Flash endurance is related to the number of erase cycles, but you have to erase a block of flash before you can write)
