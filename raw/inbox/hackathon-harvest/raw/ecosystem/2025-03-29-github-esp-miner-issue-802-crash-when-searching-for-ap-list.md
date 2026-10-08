# bitaxeorg/ESP-Miner issue #802: crash when searching for AP list in setup mode

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/802
> Collected: 2026-10-07
> Published: 2025-03-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 802
- State: closed
- Author: skot
- Opened: 2025-03-29
- Closed: 2025-04-05
- Labels: bug, help wanted, critical

## Description

- dev-latest 4fc925a
- Bitaxe 601

```
I (119170) wifi_station: Could not connect to 'myssid' [rssi -128]: reason 201
I (119170) wifi_station: Retrying Wi-Fi connection...
I (119210) http_server: Redirecting to root
I (119350) http_server: File sending complete
I (119910) http_server: File sending complete
I (119980) http_server: Redirecting to root
I (119980) http_server: File sending complete
I (120080) http_server: File sending complete
I (120230) example_dns_redirect_server: Received 31 bytes from 192.168.4.2 | DNS reply with len: 47
I (120230) example_dns_redirect_server: Waiting for data
IP address: 1.4.168.192
I (120230) example_dns_redirect_server: Received 31 bytes from 192.168.4.2 | DNS reply with len: 47
I (120240) example_dns_redirect_server: Waiting for data
I (120810) wifi:<ba-add>idx:3 (ifx:1, b2:73:34:dc:71:39), tid:1, ssn:2, winSize:64
E (122080) httpd: Failed to post esp_http_server event: ESP_ERR_TIMEOUT
E (124080) httpd: Failed to post esp_http_server event: ESP_ERR_TIMEOUT
I (124180) wifi_station: Could not connect to 'myssid' [rssi -128]: reason 201
I (124180) wifi_station: Retrying Wi-Fi connection...
E (129170) esp_netif_lwip: ip lost timer: failed to post lost ip event (107)
I (129190) wifi_station: Could not connect to 'myssid' [rssi -128]: reason 201
I (129190) wifi_station: Retrying Wi-Fi connection...
I (129490) http_server: File sending complete
I (129920) http_server: File sending complete
I (129920) CORS: Device in AP mode. Allowing CORS.
W (129930) wifi:Haven't to connect to a suitable AP now!
E (131940) httpd: Failed to post esp_http_server event: ESP_ERR_TIMEOUT
E (133940) httpd: Failed to post esp_http_server event: ESP_ERR_TIMEOUT
I (134190) wifi_station: Could not connect to 'myssid' [rssi -128]: reason 201
I (134190) wifi_station: Retrying Wi-Fi connection...
I (134240) CORS: Device in AP mode. Allowing CORS.
W (134240) wifi:Haven't to connect to a suitable AP now!
I (134410) http_server: File sending complete
I (137010) http_server: File sending complete
I (137080) http_server: Redirecting to root
I (139190) wifi_station: Could not connect to 'myssid' [rssi -128]: reason 201
I (139190) wifi_station: Retrying Wi-Fi connection...
I (140650) wifi_station: Starting Wi-Fi scan!
W (140650) wifi:Haven't to connect to a suitable AP now!
I (140650) wifi_station: Forcing disconnect so that we can scan!
I (144480) wifi_station: Wi-Fi Scan Done

assert failed: xQueueSemaphoreTake queue.c:1709 (( pxQueue ))


Backtrace: 0x40375f75:0x3fcba040 0x4037f101:0x3fcba060 0x403873c9:0x3fcba080 0x4037f9c6:0x3fcba1a0 0x42021043:0x3fcba1e0 0x42043286:0x3fcba200 0x420432d5:0x3fcba230 0x4037fc0d:0x3fcba250
--- 0x40375f75: panic_abort at /Users/skot/esp/v5.4/esp-idf/components/esp_system/panic.c:454
0x4037f101: esp_system_abort at /Users/skot/esp/v5.4/esp-idf/components/esp_system/port/esp_system_chip.c:92
0x403873c9: __assert_func at /Users/skot/esp/v5.4/esp-idf/components/newlib/assert.c:80
0x4037f9c6: xQueueSemaphoreTake at /Users/skot/esp/v5.4/esp-idf/components/freertos/FreeRTOS-Kernel/queue.c:1709 (discriminator 1)
0x42021043: lvgl_port_tick_increment at /Users/skot/Bitcoin/ESP-Miner/ESP-Miner/managed_components/espressif__esp_lvgl_port/src/lvgl9/esp_lvgl_port.c:294
0x42043286: timer_process_alarm at /Users/skot/esp/v5.4/esp-idf/components/esp_timer/src/esp_timer.c:435
0x420432d5: timer_task at /Users/skot/esp/v5.4/esp-idf/components/esp_timer/src/esp_timer.c:461 (discriminator 1)
0x4037fc0d: vPortTaskWrapper at /Users/skot/esp/v5.4/esp-idf/components/freertos/FreeRTOS-Kernel/portable/xtensa/port.c:139





ELF file SHA256: e50c0fa58

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375eb5
--- 0x40375eb5: esp_restart_noos at /Users/skot/esp/v5.4/esp-idf/components/esp_system/port/soc/esp32s3/system_internal.c:160

SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce2810,len:0x15a0
load:0x403c8700,len:0x4
load:0x403c8704,len:0xd20
load:0x403cb700,len:0x2ee4
entry 0x403c8928
```

## Comments

### skot on 2025-03-31

This is happening to me every time. Here are my steps;
1. update bitaxe 401 or 601 to v2.6.1
2. use bitaxetool to reset nvs to defaults. (use the example config files in esp-miner repo)
3. leave USB connected to view logs
4. run through selftest. press reset button to boot esp-miner
5. join setup wifi from my iPhone
6. in captive portal click on the magnifying glass 
7. watch in USB logs as esp-miner kernel panics

### mutatrum on 2025-04-02

Where is `myssid` coming from? That has been removed from the configs, default value is empty string.
