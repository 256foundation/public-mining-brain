# bitaxeorg/ESP-Miner issue #1291: i2c_master_transmit_receive(1206): i2c handle not initialized

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1291
> Collected: 2026-10-07
> Published: 2025-10-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1291
- State: closed
- Author: benjamin-wilson
- Opened: 2025-10-25
- Closed: 2025-11-05
- Labels: wontfix

## Description

Going from firmware 2.7.1 to 2.8.0 on 601/602 Gammas seems to cause some sort of race condition. It does not happen on all devices but when it does happen, on 2.8.0 and later, the gamma will not boot unless reset/power cycled. On 2.7.1 and earlier the Gamma faults and automatically resets itself, avoiding getting stuck in this loop. 

Logs from 602 Gamma 2.9.0 

```
len 0002E460 (185 KiB): RAM
I (902) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM
I (909) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (915) heap_init: At 600FE11C len 00001ECC (7 KiB): RTCRAM
I (921) esp_psram: Adding pool of 8192K of PSRAM memory to heap allocator
I (929) spi_flash: detected chip: generic
I (933) spi_flash: flash io: dio
I (938) sleep_gpio: Configure to isolate all GPIO pins in sleep state
I (944) sleep_gpio: Enable automatic switching of GPIO sleep configuration
I (952) main_task: Started on CPU0
I (956) esp_psram: Reserving pool of 32K of internal memory for DMA/internal allocations
I (965) main_task: Calling app_main()
I (969) bitaxe: Welcome to the bitaxe - FOSS || GTFO!
I (975) bitaxe: I2C initialized successfully
I (1080) adc: calibration scheme version is Curve Fitting
I (1080) adc: Calibration Success
I (1095) device_config: Device Model: Gamma
I (1096) device_config: Board Version: 602
I (1096) device_config: ASIC: 1x BM1370 (128 cores)
I (1103) system: Initial overheat_mode value: 0
I (1106) pp: pp rom version: e7ae62f
I (1109) net80211: net80211 rom version: e7ae62f
I (1116) wifi:wifi driver task: 3fccd9e4, prio:23, stack:6656, core=0
I (1126) wifi:wifi firmware version: 79fa3f41ba
I (1126) wifi:wifi certification version: v7.0
I (1129) wifi:config NVS flash: enabled
I (1133) wifi:config nano formatting: disabled
I (1137) wifi:Init data frame dynamic rx buffer num: 32
I (1142) wifi:Init static rx mgmt buffer num: 5
I (1146) wifi:Init management short buffer num: 32
I (1150) wifi:Init dynamic tx buffer num: 32
I (1154) wifi:Init static tx FG buffer num: 2
I (1159) wifi:Init static rx buffer size: 1600
I (1163) wifi:Init static rx buffer num: 10
I (1167) wifi:Init dynamic rx buffer num: 32
I (1171) wifi_init: rx ba win: 6
I (1174) wifi_init: accept mbox: 6
I (1179) wifi_init: tcpip mbox: 32
I (1183) wifi_init: udp mbox: 6
I (1186) wifi_init: tcp mbox: 6
I (1190) wifi_init: tcp tx win: 5760
I (1194) wifi_init: tcp rx win: 5760
I (1199) wifi_init: tcp mss: 1440
I (1203) wifi_init: WiFi IRAM OP enabled
I (1207) wifi_init: WiFi RX IRAM OP enabled
I (1216) connect: No WiFi SSID provided, skipping connection
I (1219) phy_init: phy_version 700,8582a7fd,Feb 10 2025,20:13:11
I (1258) wifi:mode : sta (30:ed:a0:a6:8d:0c) + softAP (30:ed:a0:a6:8d:0d)
I (1259) wifi:enable tsf
I (1259) wifi:Total power save buffer number: 16
I (1260) wifi:Init max length of beacon: 752/752
I (1265) wifi:Init max length of beacon: 752/752
I (1269) connect: Connecting...
I (1273) connect: Configuration Access Point enabled
I (1279) wifi:Set ps type: 0, coexist: 0
I (1279) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1

I (1292) TPS546: Initializing the core voltage regulator
I (1298) TPS546: Device ID: ff ff ff ff ff ff
E (1302) TPS546: Cannot find TPS546 regulator - Device ID mismatch
E (1309) vcore: VCORE_init(59): TPS546 init failed!
E (1315) system: SYSTEM_init_peripherals(104): VCORE init failed!
I (1322) power_management: Starting
I (1445) http_server: Partition size: total: 2884241, used: 702298
I (1452) http_server: AxeOS version: v2.9.0
I (1452) http_server: Starting HTTP Server
I (1454) dns_server: Socket created
I (1455) dns_server: Socket bound, port 53
I (1459) dns_server: Waiting for data
I (1826) power_management: ASIC Frequency: 525.00MHz
E (1828) i2c.master: i2c_master_transmit_receive(1206): i2c handle not initialized
E (1829) i2c_bitaxe: Unknown device
E (1833) EMC2101: Failed to read fan speed LSB: ESP_ERR_INVALID_ARG
W (1841) power_management: AP mode with invalid temperature reading: -1.0°C - Setting fan to 70%
E (1850) i2c.master: i2c_master_transmit(1195): i2c handle not initialized
E (1858) i2c_bitaxe: Unknown device
E (1862) EMC2101: EMC2101_set_fan_speed(73): Failed to set fan speed
I (1869) power_management: setting new vcore voltage to 1150mV
I (1875) vcore: Set ASIC voltage = 1.150V
I (1880) TPS546: Vout changed to 1.15 V
E (3686) i2c.master: i2c_master_transmit_receive(1206): i2c handle not initialized
E (3687) i2c_bitaxe: Unknown device
E (3688) EMC2101: Failed to read fan speed LSB: ESP_ERR_INVALID_ARG
W (3696) power_management: AP mode with invalid temperature reading: -1.0°C - Setting fan to 70%
E (3705) i2c.master: i2c_master_transmit(1195): i2c handle not initialized
E (3712) i2c_bitaxe: Unknown device
E (3716) EMC2101: EMC2101_set_fan_speed(73): Failed to set fan speed
E (5525) i2c.master: i2c_master_transmit_receive(1206): i2c handle not initialized
E (5526) i2c_bitaxe: Unknown device
E (5527) EMC2101: Failed to read fan speed LSB: ESP_ERR_INVALID_ARG
W (5535) power_management: AP mode with invalid temperature reading: -1.0°C - Setting fan to 70%
E (5543) i2c.master: i2c_master_transmit(1195): i2c handle not initialized
E (5551) i2c_bitaxe: Unknown device
```

## Comments

### benjamin-wilson on 2025-10-26

Also happens on gamma 601.
I've tried the easy stuff, lowering baud, adding a timeout. no dice
I2C channels look square-enough, doesn't look like a hardware problem 

### benjamin-wilson on 2025-10-26

Seems to be a problem specifically with the S variant of the TPS546
