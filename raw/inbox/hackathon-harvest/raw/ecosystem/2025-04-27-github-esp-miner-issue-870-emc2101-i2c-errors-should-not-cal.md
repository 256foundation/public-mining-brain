# bitaxeorg/ESP-Miner issue #870: EMC2101 I2C errors should not call abort()

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/870
> Collected: 2026-10-07
> Published: 2025-04-27

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 870
- State: closed
- Author: skot
- Opened: 2025-04-27
- Closed: 2025-05-16
- Labels: bug

## Description

Several of the I2C functions in EMC2101.c are wrapped in ESP_ERROR_CHECK() which calls esp-idf abort() on failure. Theis bascially just restarts the ESP32, potentially in a loop. These I2C commands should prolly be wrapped in ESP_RETURN_ON_ERROR() with a nice error message for the log.

https://github.com/bitaxeorg/ESP-Miner/blob/e31043b8b4330063a9886cdc8931515ce053aaa1/main/thermal/EMC2101.c#L16-L28
