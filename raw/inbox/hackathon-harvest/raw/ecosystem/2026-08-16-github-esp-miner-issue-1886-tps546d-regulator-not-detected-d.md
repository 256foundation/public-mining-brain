# bitaxeorg/ESP-Miner issue #1886: TPS546D regulator not detected - Device ID mismatch on Bitaxe Gamma (Board v601)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1886
> Collected: 2026-10-07
> Published: 2026-08-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1886
- State: open
- Author: arcsin3x
- Opened: 2026-08-16
- Closed: n/a
- Labels: none

## Description

**Describe the bug**
On my Bitaxe Gamma (Board Version 601) running firmware v2.14.2, the TPS546D core voltage regulator fails to initialize during boot. 

**Background Information**

 The original TPS546D24A on this board was damaged and replaced with a new genuine unit. After replacement, the device fails to recognize it with the same "Device ID mismatch" error. The new chip appears to be a different silicon revision, as the ID read from it (54 49 54 60 00 00) is identical to what the previous chip reported before failure. I have verified solder joints, orientation, and surrounding components—all appear correct. This suggests the firmware's Device ID validation may be too strict and does not accommodate all valid TPS546D24A ID variants.
**My logs**
[0;32mI (1051) bitaxe: Welcome to the bitaxe - FOSS || GTFO![0m
[0;32mI (1054) bitaxe: I2C initialized successfully[0m
[0;32mI (1058) bitaxe: RST pin initialized to low[0m
[0;32mI (1163) adc: calibration scheme version is Curve Fitting[0m
[0;32mI (1163) adc: Calibration Success[0m
[0;32mI (1188) nvs_config: Used entries: 214[0m
[0;32mI (1189) nvs_config: Free entries: 542[0m
[0;32mI (1189) nvs_config: Available entries: 416[0m
[0;32mI (1191) nvs_config: Total entries: 756[0m
[0;32mI (1204) device_config: Device Model: Gamma[0m
[0;32mI (1204) device_config: Board Version: 601[0m
[0;32mI (1205) device_config: ASIC: 1x BM1370 (128 cores)[0m
[0;32mI (1211) system: Initial overheat_mode value: 0[0m
[0;32mI (1218) pp: pp rom version: e7ae62f[0m
[0;32mI (1221) net80211: net80211 rom version: e7ae62f[0m
I (1227) wifi:wifi driver task: 3fcbe2b0, prio:23, stack:6656, core=0
I (1242) wifi:wifi firmware version: 4df78f2
I (1242) wifi:wifi certification version: v7.0
I (1242) wifi:config NVS flash: enabled
I (1244) wifi:config nano formatting: disabled
I (1248) wifi:Init data frame dynamic rx buffer num: 32
I (1253) wifi:Init static rx mgmt buffer num: 5
I (1257) wifi:Init management short buffer num: 32
I (1262) wifi:Init static tx buffer num: 16
I (1266) wifi:Init tx cache buffer num: 32
I (1269) wifi:Init static tx FG buffer num: 2
I (1273) wifi:Init static rx buffer size: 1600
I (1278) wifi:Init static rx buffer num: 16
I (1281) wifi:Init dynamic rx buffer num: 32
[0;32mI (1286) wifi_init: rx ba win: 16[0m
[0;32mI (1289) wifi_init: accept mbox: 6[0m
[0;32mI (1293) wifi_init: tcpip mbox: 32[0m
[0;32mI (1298) wifi_init: udp mbox: 6[0m
[0;32mI (1301) wifi_init: tcp mbox: 6[0m
[0;32mI (1305) wifi_init: tcp tx win: 5760[0m
[0;32mI (1309) wifi_init: tcp rx win: 5760[0m
[0;32mI (1314) wifi_init: tcp mss: 1440[0m
[0;32mI (1318) wifi_init: WiFi/LWIP prefer SPIRAM[0m
[0;32mI (1323) wifi_init: WiFi IRAM OP enabled[0m
[0;32mI (1327) wifi_init: WiFi RX IRAM OP enabled[0m
[0;32mI (1336) connect: ESP_WIFI_MODE_STA[0m
[0;32mI (1337) connect: Wi-Fi Password provided, using WPA2[0m
[0;32mI (1342) connect: wifi_init_sta finished.[0m
I (1347) wifi:Set ps type: 0, coexist: 0

[0;32mI (1351) connect: ESP_WIFI setting hostname to: bitaxe[0m
[0;32mI (1356) phy_init: phy_version 711,97bcf0a2,Aug 25 2025,19:04:10[0m
I (1405) wifi:mode : sta (44:b1:76:d2:97:c8) + softAP (44:b1:76:d2:97:c9)
I (1406) wifi:enable tsf
I (1407) wifi:Total power save buffer number: 8
I (1408) wifi:Init max length of beacon: 752/752
I (1412) wifi:Init max length of beacon: 752/752
[0;32mI (1417) connect: Connecting...[0m
[0;32mI (1421) connect: wifi_init_sta finished.[0m
[0;32mI (1422) connect: Configuration Access Point enabled[0m
[0;32mI (1431) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1[0m
[0;32mI (1432) display: SSD1306 (128x32)[0m
[0;32mI (1444) display: Install panel IO[0m
[0;32mI (1448) display: Install panel driver[0m
[0;32mI (1454) display: Initialize LVGL[0m
[0;32mI (1457) LVGL: Starting LVGL task[0m
[0;32mI (1476) display: Rotation: 0[0m
[0;32mI (1578) display: Display init success![0m
[0;32mI (1578) input: Install button driver[0m
[0;32mI (1655) system: Existing overheat_mode value: 0[0m
[0;32mI (1784) filesystem: Partition size: total: 2884241, used: 756012[0m
[0;32mI (1784) TPS546: Initializing the core voltage regulator[0m
[0;32mI (1819) TPS546: Device ID: 54 49 54 60 00 00[0m
[0;31mE (1819) TPS546: Cannot find TPS546 regulator - Device ID mismatch[0m
[0;31mE (1820) vcore: VCORE_init(96): TPS546 init failed![0m
[0;31mE (1825) system: VCORE init failed[0m
[0;31mE (1829) bitaxe: Critical peripheral initialization failure (ESP_OK). Entering degraded mode.[0m
[0;32mI (1838) http_server: Starting HTTP Server[0m
[0;32mI (1847) websocket_log: websocket_log_task starting[0m
[0;32mI (1849) websocket_api: websocket_api_task starting[0m
[0;32mI (1855) dns_server: Socket created[0m
[0;32mI (1859) dns_server: Socket bound, port 53[0m
[0;32mI (1863) dns_server: Waiting for data[0m
[0;32mI (1869) system: Firmware Version: v2.14.2[0m
[0;32mI (1872) system: AxeOS Version: v2.14.2[0m
[0;32mI (1877) BAP: Initializing BAP system[0m
[0;32mI (1883) BAP: BAP system initialized successfully[0m
I (4258) wifi:ap channel adjust o:1,1 n:11,2
I (4259) wifi:new:<11,2>, old:<1,1>, ap:<11,2>, sta:<11,2>, prof:1, snd_ch_cfg:0x0
I (4260) wifi:state: init -> auth (0xb0)
I (4267) wifi:state: auth -> assoc (0x0)
I (4273) wifi:state: assoc -> run (0x10)
I (4281) wifi:<ba-add>idx:0 (ifx:0, 6a:db:54:6d:8e:8e), tid:5, ssn:0, winSize:64
I (4377) wifi:connected with PDCN, aid = 3, channel 11, 40D, bssid = 6a:db:54:6d:8e:8e
I (4378) wifi:security: WPA2-PSK, phy: bgn, rssi: -43
I (4385) wifi:pm start, type: 0

I (4386) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us
I (4390) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
E (4398) wifi:sta is connecting, cannot set config
[0;32mI (4403) connect: Acquiring IP...[0m
I (4465) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (4868) wifi:new:<11,2>, old:<11,2>, ap:<11,2>, sta:<11,2>, prof:1, snd_ch_cfg:0x0
I (4869) wifi:station: a8:93:4a:e0:e6:fd join, AID=1, bgn, 40D
[0;32mI (4905) esp_netif_lwip: DHCP server assigned IP to a client, IP is: 192.168.4.2[0m
I (4983) wifi:<ba-add>idx:2 (ifx:1, a8:93:4a:e0:e6:fd), tid:0, ssn:17, winSize:64
[0;32mI (5086) http_server: Redirecting to root[0m
[0;32mI (5631) http_server: Redirecting to root[0m
[0;32mI (5711) http_server: File sending complete[0m
[0;32mI (6028) http_server: Redirecting to root[0m
I (6387) wifi:<ba-add>idx:1 (ifx:0, 6a:db:54:6d:8e:8e), tid:0, ssn:2, winSize:64
[0;32mI (6468) http_server: Redirecting to root[0m
[0;32mI (8226) http_server: Redirecting to root[0m
[0;32mI (8350) http_server: Redirecting to root[0m
[0;32mI (8357) CORS: Device in AP mode. Allowing CORS.[0m
[0;32mI (8357) websocket: Added WebSocket api client, fd: 45, slot: 0[0m
[0;32mI (9206) connect: IPv4 Address: 192.168.123.44[0m
[0;32mI (9206) connect: Connected to SSID: PDCN[0m
I (9207) wifi:station: a8:93:4a:e0:e6:fd leave, AID = 1, reason = 2, bss_flags is 33786979, bss:0x3c2373a0
I (9214) wifi:new:<11,2>, old:<11,2>, ap:<11,2>, sta:<11,2>, prof:1, snd_ch_cfg:0x0
I (9222) wifi:<ba-del>idx:2, tid:0
I (9225) wifi:new:<11,2>, old:<11,2>, ap:<11,2>, sta:<11,2>, prof:1, snd_ch_cfg:0x0
I (9232) wifi:mode : sta (44:b1:76:d2:97:c8)
[0;32mI (9237) protocol_coordinator: Protocol coordinator started (primary: SV1, fallback: SV1, state: 1)[0m
[0;32mI (9239) esp_netif_handlers: sta ip: 192.168.123.44, mask: 255.255.255.0, gw: 192.168.123.2[0m
[0;32mI (9238) stratum_v1_task: Opening connection to pool: public-pool.io:3333[0m
[0;32mI (9255) connect: Configuration Access Point disabled[0m
[0;32mI (9239) main_task: Returned from app_main()[0m
[0;33mW (9270) httpd_txrx: httpd_sock_err: error in recv : 113[0m
[0;33mW (9280) httpd_txrx: httpd_sock_err: error in recv : 113[0m
[0;33mW (9285) httpd_txrx: httpd_sock_err: error in recv : 113[0m
[0;33mW (9291) httpd_ws: httpd_ws_recv_frame: WS frame is not properly masked.[0m
[0;32mI (9299) websocket: Removed WebSocket api client, fd: 45, slot: 0[0m
[0;33mW (9306) httpd_txrx: httpd_sock_err: error in recv : 113[0m
[0;32mI (11218) connect: IPv6 Address: FE80::46B1:76FF:FED2:97C8[0m
[0;32mI (19265) http_server: File sending complete[0m
[0;32mI (30333) http_server: File sending complete[0m
[0;32mI (30429) http_server: File sending complete[0m
[0;32mI (30461) http_server: File sending complete[0m
[0;32mI (31870) http_server: File sending complete[0m
[0;32mI (32027) http_server: File sending complete[0m
[0;32mI (32175) http_server: File sending complete[0m
[0;32mI (32376) http_server: File sending complete[0m
[0;32mI (32393) websocket: Added WebSocket api client, fd: 47, slot: 0[0m
[0;32mI (32628) http_server: File sending complete[0m
[0;32mI (43736) websocket: Added WebSocket log client, fd: 48, slot: 1[0m


**Hardware Context (Important)**
The original TPS546D24A regulator on this board was damaged and has been replaced with a new, genuine unit (same part number). After soldering the replacement chip, the device now fails to recognize it with the "Device ID mismatch" error shown in the logs.

The replacement chip was purchased from a reputable supplier and is confirmed to be a genuine TPS546D24A. It was installed with proper ESD precautions and reflow soldering.

<img width="1024" height="1820" alt="Image" src="https://github.com/user-attachments/assets/26aa4966-7f76-4d76-bae3-85420baabeef" />

**I have verified:**

✅ The chip orientation is correct

✅ All surrounding passive components are intact

✅ No shorts or bridges are visible on the pins

✅ I2C pull-up resistors are present and functional

This suggests the issue may not be a hardware defect on the new chip, but rather:

A different silicon revision with a slightly modified Device ID,

An I2C communication issue (bus capacitance, timing, or solder joint quality),

Or an overly strict Device ID validation in the firmware that does not account for all valid ID variants of this regulator.

**Steps to Reproduce**
Flash firmware v2.14.2 (AxeOS v2.14.2) on Bitaxe Gamma (board v601)

Power on the device

Observe serial monitor output during boot

**Expected Behavior**
The TPS546D24A regulator should be successfully detected and initialized, allowing proper core voltage regulation for the BM1370 ASIC.

**Actual Behavior**
The boot log shows:

TPS546 initialization attempt fails with Device ID mismatch

VCORE initialization fails

System enters "degraded mode"

Device continues to boot but with compromised power regulation


**Hardware (please complete the following information):**

Device Model | Gamma
Board Version | 601
ASIC | 1x BM1370 (128 cores)
Firmware Version | v2.14.2
AxeOS Version | v2.14.2
Display | SSD1306 (128x32)
Wi-Fi | Connected (RSSI: -43dBm)


**Additional context**
I2C bus is successfully initialized prior to TPS546 check

Other peripherals (ADC, display, buttons, NVS) initialize correctly

The ID read from the chip is 54 49 54 60 00 00 — this may actually be a valid ID for certain silicon revisions, but the driver validation logic rejects it

System continues in degraded mode — ASIC may not receive stable core voltage

## Comments

### WantClue on 2026-08-16

I'm wondering why is the ID all 00 at the end? where did you get this TPS from ? 

### arcsin3x on 2026-08-16

> I'm wondering why is the ID all 00 at the end? where did you get this TPS from ?

I don't know why, but the chip I bought online had this issue from the previous seller, so I switched to another one, and it still gives the same error. I also noticed that the silkscreen markings on the chips from both sellers are exactly the same.

### arcsin3x on 2026-08-17

**I tried using the code below to flash into the ESP32 device to directly read the TPS ID, but it couldn't scan any devices on the I2C bus.** 
```c
#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"
#include "driver/i2c_master.h"

#define I2C_MASTER_NUM 0
#define I2C_MASTER_FREQ_HZ 100000

typedef struct {
    int sda;
    int scl;
    const char *name;
} i2c_pin_t;

static const i2c_pin_t pin_configs[] = {
    {4, 5, "GPIO4/GPIO5 (Bitaxe default)"},
    {8, 9, "GPIO8/GPIO9 (Your original)"},
    {21, 22, "GPIO21/GPIO22 (Common)"},
    {18, 19, "GPIO18/GPIO19"},
    {33, 32, "GPIO33/GPIO32"},
};

static const char *TAG = "I2C_SCANNER";


static bool probe_device(i2c_master_bus_handle_t bus_handle, uint8_t addr) {
    i2c_device_config_t dev_config = {
        .dev_addr_length = I2C_ADDR_BIT_LEN_7,
        .device_address = addr,
        .scl_speed_hz = I2C_MASTER_FREQ_HZ,
    };
    
    i2c_master_dev_handle_t dev;
    esp_err_t ret = i2c_master_bus_add_device(bus_handle, &dev_config, &dev);
    if (ret != ESP_OK) return false;
    

    uint8_t test_byte = 0x00;
    ret = i2c_master_transmit(dev, &test_byte, 1, 100);
    i2c_master_bus_rm_device(dev);
    
    return (ret == ESP_OK);
}


static int scan_pins(int sda, int scl) {
    ESP_LOGI(TAG, "\n=== Testing SDA=GPIO%d, SCL=GPIO%d ===", sda, scl);
    
    i2c_master_bus_config_t bus_config = {
        .clk_source = I2C_CLK_SRC_DEFAULT,
        .i2c_port = I2C_MASTER_NUM,
        .scl_io_num = scl,
        .sda_io_num = sda,
        .glitch_ignore_cnt = 7,
        .flags.enable_internal_pullup = true,
    };
    
    i2c_master_bus_handle_t bus_handle;
    esp_err_t ret = i2c_new_master_bus(&bus_config, &bus_handle);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "  Bus init failed: %s", esp_err_to_name(ret));
        return 0;
    }
    
    vTaskDelay(pdMS_TO_TICKS(50));
    
    int found = 0;
    for (uint8_t addr = 0x01; addr < 0x7F; addr++) {
        if (probe_device(bus_handle, addr)) {
            const char *name = "Unknown";
            if (addr == 0x24) name = "TPS546";
            else if (addr == 0x3C) name = "OLED";
            else if (addr == 0x4C) name = "EMC2101";
            else if (addr == 0x40) name = "INA260";
            ESP_LOGI(TAG, "  ✅ Found 0x%02X (%s)", addr, name);
            found++;
        }
        if (addr % 16 == 0) vTaskDelay(pdMS_TO_TICKS(2));
    }
    
    ESP_LOGI(TAG, "  Total: %d device(s)", found);
    

    i2c_del_master_bus(bus_handle);
    vTaskDelay(pdMS_TO_TICKS(100));
    
    return found;
}

void app_main(void) {
    ESP_LOGI(TAG, "=== Bitaxe I2C Pin Scanner ===");
    ESP_LOGI(TAG, "This will test multiple pin combinations");
    ESP_LOGI(TAG, "Make sure DC power is connected to Bitaxe!");
    
    vTaskDelay(pdMS_TO_TICKS(2000));
    
    int total_configs = sizeof(pin_configs) / sizeof(pin_configs[0]);
    int best_found = 0;
    const char *best_name = NULL;
    
    for (int i = 0; i < total_configs; i++) {
        int found = scan_pins(pin_configs[i].sda, pin_configs[i].scl);
        if (found > best_found) {
            best_found = found;
            best_name = pin_configs[i].name;
        }
        vTaskDelay(pdMS_TO_TICKS(500));
    }
    
    ESP_LOGI(TAG, "\n=== Summary ===");
    if (best_found > 0) {
        ESP_LOGI(TAG, "✅ Best result: %s with %d device(s)", best_name, best_found);
        ESP_LOGI(TAG, "Use these pins in your main code");
    } else {
        ESP_LOGE(TAG, "❌ No I2C devices found on any pin combination!");
        ESP_LOGE(TAG, "\nPlease check:");
        ESP_LOGE(TAG, "1. DC power is connected to Bitaxe (12V or 24V)");
        ESP_LOGE(TAG, "2. Both USB and DC are plugged in");
        ESP_LOGE(TAG, "3. The device is powered on");
    }
    
    while (1) {
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
``` 
**I tried modifying ESP-Miner to read the TPS device ID block by block, and eventually confirmed that the device ID is indeed 54 49 54 60 00 00. It might be a custom chip or due to other reasons. I added this device ID into the matching code, but it still didn't get the chip to start up. Below are the logs from the 601.**

`I (24) boot: ESP-IDF v6.0.2-dirty 2nd stage bootloader
I (24) boot: compile time Aug 17 2026 10:09:09
I (24) boot: Multicore bootloader
I (25) boot: chip revision: v0.2
I (28) boot: efuse block revision: v1.4
I (31) boot.esp32s3: Boot SPI Speed : 80MHz
I (35) boot.esp32s3: SPI Mode       : DIO
I (39) boot.esp32s3: SPI Flash Size : 16MB
I (43) boot: Enabling RNG early entropy source...
I (47) boot: Partition Table:
I (50) boot: ## Label            Usage          Type ST Offset   Length
I (56) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (63) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (69) boot:  2 factory          factory app      00 00 00010000 00400000
I (76) boot:  3 www              Unknown data     01 82 00410000 00300000
I (82) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (89) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (95) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (102) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (108) boot: End of partition table
I (112) boot: Defaulting to factory image
I (115) esp_image: segment 0: paddr=00010020 vaddr=3c160020 size=f50e4h (1003748) map
I (291) esp_image: segment 1: paddr=0010510c vaddr=3fc9f100 size=06620h ( 26144) load
I (296) esp_image: segment 2: paddr=0010b734 vaddr=40374000 size=048e4h ( 18660) load
I (300) esp_image: segment 3: paddr=00110020 vaddr=42000020 size=157194h (1405332) map
I (538) esp_image: segment 4: paddr=002671bc vaddr=403788e4 size=1679ch ( 92060) load
I (556) esp_image: segment 5: paddr=0027d960 vaddr=50000000 size=00024h (    36) load
I (568) boot: Loaded app from partition at offset 0x10000
I (568) boot: Disabling RNG early entropy source...
I (578) octal_psram: vendor id    : 0x0d (AP)
I (578) octal_psram: dev id       : 0x02 (generation 3)
I (578) octal_psram: density      : 0x03 (64 Mbit)
I (583) octal_psram: good-die     : 0x01 (Pass)
I (588) octal_psram: Latency      : 0x01 (Fixed)
I (594) octal_psram: VCC          : 0x01 (3V)
I (599) octal_psram: SRF          : 0x01 (Fast Refresh)
I (605) octal_psram: BurstType    : 0x01 (Hybrid Wrap)
I (610) octal_psram: BurstLen     : 0x01 (32 Byte)
I (616) octal_psram: Readlatency  : 0x02 (10 cycles@Fixed)
I (622) octal_psram: DriveStrength: 0x00 (1/1)
I (627) MSPI Timing: Enter psram timing tuning
I (633) esp_psram: Found 8MB PSRAM device
I (637) esp_psram: Speed: 80MHz
I (641) cpu_start: Multicore app
I (1046) esp_psram: SPI SRAM memory test OK
I (1054) cpu_start: GPIO 44 and 43 are used as console UART I/O pins
I (1055) cpu_start: Pro cpu start user code
I (1055) cpu_start: cpu freq: 240000000 Hz
I (1060) app_init: Application information:
I (1065) app_init: Project name:     esp-miner
I (1070) app_init: App version:      v2.14.0-56-g26bac19-dirty
I (1076) app_init: Compile time:     Aug 17 2026 10:07:20
I (1082) app_init: ELF file SHA256:  32d8bfa4f...
I (1088) app_init: ESP-IDF:          v6.0.2-dirty
I (1093) efuse_init: Min chip rev:     v0.0
I (1098) efuse_init: Max chip rev:     v0.99
I (1103) efuse_init: Chip rev:         v0.2
I (1108) heap_init: Initializing. RAM available for dynamic allocation:
I (1115) heap_init: At 3FCAB130 len 0003E5E0 (249 KiB): RAM
I (1122) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM
I (1128) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (1134) heap_init: At 600FE000 len 00001FE8 (7 KiB): RTCRAM
I (1141) esp_psram: Adding pool of 7664K of PSRAM memory to heap allocator
I (1149) spi_flash: detected chip: generic
I (1153) spi_flash: flash io: dio
I (1157) sleep_gpio: Configure to isolate all GPIO pins in sleep state
I (1164) sleep_gpio: Enable automatic switching of GPIO sleep configuration
I (1182) main_task: Started on CPU0
I (1186) esp_psram: Reserving pool of 32K of internal memory for DMA/internal allocations
I (1195) main_task: Calling app_main()
I (1199) log_buffer: Soft reboot detected, 61604 bytes of logs preserved
I (1206) bitaxe: Welcome to the bitaxe - FOSS || GTFO!
I (1213) bitaxe: I2C initialized successfully
I (1217) bitaxe: RST pin initialized to low
I (1322) adc: calibration scheme version is Curve Fitting
I (1322) adc: Calibration Success
I (1350) nvs_config: Used entries: 244
I (1351) nvs_config: Free entries: 512
I (1351) nvs_config: Available entries: 386
I (1353) nvs_config: Total entries: 756
I (1366) device_config: Device Model: Gamma
I (1367) device_config: Board Version: 601
I (1367) device_config: ASIC: 1x BM1370 (128 cores)
I (1375) system: Initial overheat_mode value: 0
I (1380) pp: pp rom version: e7ae62f
I (1383) net80211: net80211 rom version: e7ae62f
I (1389) wifi:wifi driver task: 3fcbbdf0, prio:23, stack:6656, core=0
I (1405) wifi:wifi firmware version: 00ad238
I (1405) wifi:wifi certification version: v7.0
I (1405) wifi:config NVS flash: enabled
I (1406) wifi:config nano formatting: disabled
I (1410) wifi:Init data frame dynamic rx buffer num: 32
I (1415) wifi:Init static rx mgmt buffer num: 5
I (1419) wifi:Init management short buffer num: 32
I (1424) wifi:Init static tx buffer num: 16
I (1428) wifi:Init tx cache buffer num: 32
I (1431) wifi:Init static tx FG buffer num: 2
I (1436) wifi:Init static rx buffer size: 1600
I (1440) wifi:Init static rx buffer num: 16
I (1443) wifi:Init dynamic rx buffer num: 32
I (1448) wifi_init: rx ba win: 16
I (1452) wifi_init: accept mbox: 6
I (1456) wifi_init: tcpip mbox: 32
I (1460) wifi_init: udp mbox: 6
I (1463) wifi_init: tcp mbox: 6
I (1467) wifi_init: tcp tx win: 5760
I (1472) wifi_init: tcp rx win: 5760
I (1476) wifi_init: tcp mss: 1440
I (1480) wifi_init: WiFi/LWIP prefer SPIRAM
I (1485) wifi_init: WiFi IRAM OP enabled
I (1489) wifi_init: WiFi RX IRAM OP enabled
I (1501) connect: ESP_WIFI_MODE_STA
I (1502) connect: Wi-Fi Password provided, using WPA2
I (1505) connect: wifi_init_sta finished.
I (1509) wifi:Set ps type: 0, coexist: 0

I (1513) connect: ESP_WIFI setting hostname to: bitaxe
I (1519) phy_init: phy_version 712,87e8c20e,Apr 13 2026,18:51:10
I (1563) wifi:mode : sta (44:b1:76:d2:97:c8) + softAP (44:b1:76:d2:97:c9)
I (1564) wifi:enable tsf
I (1564) wifi:Total power save buffer number: 8
I (1565) wifi:Init max length of beacon: 752/752
I (1570) wifi:Init max length of beacon: 752/752
I (1574) connect: Connecting...
I (1579) connect: wifi_init_sta finished.
I (1580) connect: Configuration Access Point enabled
I (1589) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (1589) display: SSD1306 (128x32)
I (1601) display: Install panel IO
I (1605) display: Install panel driver
I (1611) display: Initialize LVGL
I (1615) LVGL: Starting LVGL task
I (1634) display: Rotation: 0
I (1736) display: Display init success!
I (1736) input: Install button driver
I (1818) system: Existing overheat_mode value: 0
I (1819) system: Custom WWW disabled; skipping SPIFFS filesystem initialization
I (1821) TPS546: Initializing the core voltage regulator
I (1848) TPS546: Attempting direct read of Device ID...
I (1849) TPS546: Direct read attempt 1: 06 54 49 54 60 00
I (1854) TPS546: Direct read attempt 2: 06 54 49 54 60 00
I (1860) TPS546: Direct read attempt 3: 06 54 49 54 60 00
I (1866) TPS546: Attempting 7-byte read (with length prefix)...
I (1868) TPS546: 7-byte read attempt 1: 06 54 49 54 60 00 00
I (1874) TPS546: Parsed as SMBus block (len=0x06)
I (1879) TPS546: Device ID matched via 7-byte read!
I (1885) TPS546: Final Device ID: 54 49 54 60 00 00
I (1891) TPS546: Power config-OPERATION: 00
I (1896) TPS546: Power config-ON_OFF_CONFIG: 08
I (1901) TPS546: Reading MFR info
I (1905) TPS546: MFR_ID: 03 00 00
I (1908) TPS546: MFR_MODEL: 03 00 00
I (1913) TPS546: MFR_REVISION: 03 00 00
I (1917) TPS546: Writing new config values
I (1922) TPS546: VOUT_MODE: 94
I (1926) TPS546: ---Writing new config values to TPS546---
I (1932) TPS546: Setting ON_OFF_CONFIG: 08
I (1937) TPS546: Setting STACK_CONFIG: 0000
I (1942) TPS546: Setting SYNC_CONFIG: 10
I (1946) TPS546: Setting PHASE: 00
I (1950) TPS546: Setting FREQUENCY: 650MHz
I (1955) TPS546: Setting VIN_ON: 4.80V
I (1960) TPS546: Setting VIN_OFF: 4.50V
I (1964) TPS546: Setting VIN_OV_FAULT_LIMIT: 6.50V
E (2021) i2c_bitaxe: FATAL: [TPS546] (0x24) failed all 5 retries.
I (2021) TPS546: Setting VIN_OV_FAULT_RESPONSE: B7
E (2073) i2c_bitaxe: FATAL: [TPS546] (0x24) failed all 5 retries.
I (2073) TPS546: Setting VOUT SCALE: 0.25
E (2124) i2c_bitaxe: FATAL: [TPS546] (0x24) failed all 5 retries.
I (2124) TPS546: Setting VOUT_COMMAND: 1.20V
I (2125) TPS546: Setting VOUT_MAX: 2.00V
I (2130) TPS546: Setting VOUT_MIN: 1.00V
I (2134) TPS546: Setting VOUT_OV_FAULT_LIMIT: 1.25
I (2140) TPS546: Setting VOUT_OV_WARN_LIMIT: 1.16
I (2145) TPS546: Setting VOUT_MARGIN_HIGH: 1.10
I (2151) TPS546: Setting VOUT_MARGIN_LOW: 0.90
I (2156) TPS546: Setting VOUT_UV_WARN_LIMIT: 0.90
I (2161) TPS546: Setting VOUT_UV_FAULT_LIMIT: 0.75
I (2167) TPS546: ----- IOUT
I (2169) TPS546: Setting IOUT_OC_WARN_LIMIT: 25.00A
I (2175) TPS546: Setting IOUT_OC_FAULT_LIMIT: 30.00A
I (2181) TPS546: Setting IOUT_OC_FAULT_RESPONSE: c0
I (2186) TPS546: ----- TEMPERATURE
I (2190) TPS546: Setting OT_WARN_LIMIT: 105C
I (2195) TPS546: Setting OT_FAULT_LIMIT: 145C
I (2200) TPS546: Setting OT_FAULT_RESPONSE: ff
I (2205) TPS546: ----- TIMING
I (2209) TPS546: Setting TON_DELAY: 0ms
I (2214) TPS546: Setting TON_RISE: 3ms
I (2218) TPS546: Setting TON_MAX_FAULT_LIMIT: 0ms
I (2223) TPS546: Setting TON_MAX_FAULT_RESPONSE: 3b
I (2229) TPS546: Setting TOFF_DELAY: 0ms
I (2234) TPS546: Setting TOFF_FALL: 0ms
I (2238) TPS546: Setting PIN_DETECT_OVERRIDE
I (2243) TPS546: -----------VOLTAGE---------------------
I (2249) TPS546: read VIN_ON: 4.80V
I (2254) TPS546: read VIN_OFF: 4.50V
I (2258) TPS546: read VIN_OV_FAULT_LIMIT: 21.00V
I (2263) TPS546: read VIN_UV_WARN_LIMIT: 3.25V
I (2268) TPS546: read VIN_OV_FAULT_RESPONSE: 3C
I (2274) TPS546: read VOUT_MAX: 2.00V
I (2278) TPS546: read VOUT_OV_FAULT_LIMIT: 1.50V
I (2283) TPS546: read VOUT_OV_WARN_LIMIT: 1.39V
I (2288) TPS546: read VOUT_MARGIN_HIGH: 1.32V
I (2294) TPS546: read VOUT_COMMAND: 1.20V
I (2298) TPS546: read VOUT_MARGIN_LOW: 1.08V
I (2303) TPS546: read VOUT_UV_WARN_LIMIT: 1.08V
I (2308) TPS546: read VOUT_UV_FAULT_LIMIT: 0.90V
I (2331) TPS546: read VOUT_MIN: 1.00 V
I (2332) TPS546: read STATUS_WORD: 8823
I (2332) TPS546: -----------VOLTAGE/CURRENT---------------------
I (2336) TPS546: read READ_VIN: 0.00V
I (2341) TPS546: read READ_IOUT: -0.19A
I (2345) TPS546: read READ_VOUT: 0.10V
I (2366) TPS546: -----------TIMING---------------------
I (2368) TPS546: read TON_DELAY: 0ms
I (2369) TPS546: read TON_RISE: 3ms
I (2390) TPS546: read TON_MAX_FAULT_LIMIT: 0ms
I (2395) TPS546: read TON_MAX_FAULT_RESPONSE: 3b
I (2397) TPS546: read TOFF_DELAY: 0ms
I (2398) TPS546: read TOFF_FALL: 0ms
I (2399) TPS546: ---------CONFIG--------------------
I (2411) TPS546: read PHASE: 00
I (2412) TPS546: read STACK_CONFIG: 0000
I (2413) TPS546: read SYNC_CONFIG: 10
I (2418) TPS546: read INTERLEAVE: 0020
I (2422) TPS546: read CAPABILITY: d0
I (2426) TPS546: ---------OPERATION------------------
I (2432) TPS546: read OPERATION: 00
I (2436) TPS546: read ON_OFF_CONFIG: 08
I (2441) TPS546: read COMPENSATION CONFIG
I (2445) TPS546: 05 12 20 84 21
I (2449) TPS546: Clearing faults
I (2460) TPS546: Turning on output...
I (2482) TPS546: OPERATION after set: 0x80 (expected 0x80)
I (2483) TPS546: STATUS_WORD after power on: 8861
I (2483) TPS546: VOUT after power on: 0.097V
I (2488) EMC2101: Initializing EMC2101 (Temperature offset: 0° C)
I (2512) thermal: EMC2101 configuration: Ideality Factor: 24, Beta Compensation: 00
I (2513) power_management: Starting
I (2514) power_management: ASIC Frequency: 525 MHz, Expected hashrate: 1.07GH/s
I (2531) fan_controller: Starting
I (2532) fan_controller: Set to Startup mode, fan speed: 70.0%
I (2536) system: Firmware Version: v2.14.0-56-g26bac19-dirty
I (2539) system: AxeOS Version: Unified
I (2543) http_server: Starting HTTP Server
I (2552) websocket_log: websocket_log_task starting
I (2554) websocket_api: websocket_api_task starting
I (2568) dns_server: Socket created
I (2569) dns_server: Socket bound, port 53
I (2570) dns_server: Waiting for data
I (2574) BAP: Initializing BAP system
I (2580) BAP: BAP system initialized successfully
I (3023) power_management: setting new vcore voltage to 1250mV
I (3024) vcore: Set ASIC voltage = 1.250V
I (3025) TPS546: Vout changed to 1.25 V
E (3131) TPS546: Status: 0x8861
E (3131) TPS546: The voltage regulator is turned off
E (3131) TPS546: An output overvoltage fault has occurred
E (3136) TPS546: VOUT Status: C0
E (3139) TPS546: VOUT Overvoltage Fault
E (3144) TPS546: VOUT Undervoltage Warning
E (3149) TPS546: The output voltage is NOT within the regulation window. PGOOD pin is asserted.
I (4423) wifi:ap channel adjust o:1,1 n:13,2
I (4423) wifi:new:<13,0>, old:<1,1>, ap:<13,2>, sta:<13,0>, prof:1, snd_ch_cfg:0x0
I (4424) wifi:state: init -> auth (0xb0)
I (4433) wifi:state: auth -> assoc (0x0)
I (4441) wifi:state: assoc -> run (0x10)
I (4450) wifi:<ba-add>idx:0 (ifx:0, ee:b9:70:81:7a:f0), tid:5, ssn:0, winSize:64
I (4550) wifi:<ba-add>idx:1 (ifx:0, ee:b9:70:81:7a:f0), tid:0, ssn:2, winSize:64
I (4555) wifi:connected with YYGLGG, aid = 5, channel 13, BW20, bssid = ee:b9:70:81:7a:f0
I (4555) wifi:security: WPA2-PSK, phy: bgn, rssi: -45, cipher(pairwise:0x3, group:0x3), pmf:0
I (4565) wifi:pm start, type: 0

I (4565) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us
I (4574) wifi:set rx beacon pti, rx_bcn_pti: 14, bcn_timeout: 25000, mt_pti: 14, mt_time: 10000
E (4582) wifi:sta is connecting, cannot set config
I (4587) connect: Acquiring IP...
I (4651) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (6105) connect: IPv4 Address: 192.168.1.70
I (6105) connect: Connected to SSID: YYGLGG
I (6106) wifi:mode : sta (44:b1:76:d2:97:c8)
I (6111) esp_netif_handlers: sta ip: 192.168.1.70, mask: 255.255.255.0, gw: 192.168.1.1
I (6117) connect: Configuration Access Point disabled
I (6125) mdns_mem: mDNS task will be created from internal RAM
I (6129) connect: mDNS/Avahi initialized successfully - device discoverable on network
I (6191) BTC_PRICE: Price update task started
I (6191) BTC_PRICE: BTC price task initialized successfully
I (6191) asic_init: Starting ASIC initialization (cold boot mode)
I (6398) asic_init: Performing full UART initialization
I (6398) serial: Initializing serial
I (6399) asic_init: Detecting ASIC chips...
I (6402) asic: Initializing 1x BM1370
I (7226) connect: mDNS hostname set to: bitaxe.local
I (7226) connect: Access device at: http://bitaxe.local
I (7227) connect: mDNS HTTP service registered: _http._tcp port 80
I (7233) connect: Discover with: avahi-browse _http._tcp
I (7239) connect: mDNS instance: Bitaxe Gamma 601 (97C8)
I (7246) connect: mDNS AxeOS subtype registered: _axeos._sub._http._tcp
I (7253) connect: Discover AxeOS devices with: avahi-browse _axeos._sub._http._tcp
I (7262) connect: mDNS TXT records added: board=601, family=Gamma, asic=BM1370, asic_count=1, fw_version=v2.14.0-56-g26bac19-dirty
I (7273) connect: mDNS/Avahi setup complete - device ready for network discovery
I (7380) connect: IPv6 Address: FE80::46B1:76FF:FED2:97C8
E (7406) common: 0 chip(s) detected on the chain, expected 1
E (7406) common: ASIC 0 not found
E (7406) asic_init: ASIC initialization failed - chip chain detection failed
I (7413) main_task: Returned from app_main()
I (16192) websocket: Added WebSocket api client, fd: 44, slot: 0, type_count: 1
I (21191) BTC_PRICE: Fetching price from Binance...
I (21364) BTC_PRICE: Raw response: {"symbol":"BTCUSDT","price":"63283.66000000"}
I (21364) BTC_PRICE: Price updated: 63283.66000000
I (21367) BTC_PRICE: HTTP status: 200`
