# bitaxeorg/BitaxeGT issue #10: I2C not working well sometimes on cold boot.

> Source: https://github.com/bitaxeorg/BitaxeGT/issues/10
> Collected: 2026-10-07
> Published: 2025-08-28

- Repository: bitaxeorg/BitaxeGT
- Type: issue
- Number: 10
- State: open
- Author: skot
- Opened: 2025-08-28
- Closed: n/a
- Labels: bug

## Description

When first attaching power, my bitaxeGT 800xxx sometimes will have I2C errors. The errors will persist until reset is pressed.

log snippet;
```
I (1289) connect: Configuration Access Point enabled
I (1297) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (1304) connect: ESP_WIFI setting hostname to: bitaxe601xxx
I (1310) connect: wifi_init_sta finished.
I (1315) TPS546: Initializing the core voltage regulator
I (1321) TPS546: Device ID: ff ff ff ff ff ff
E (1326) TPS546: Cannot find TPS546 regulator - Device ID mismatch
E (1333) vcore: VCORE_init(62): TPS546 init failed!
E (1338) system: SYSTEM_init_peripherals(104): VCORE init failed!
I (1345) power_management: Starting
I (1350) power_management: ASIC Frequency: 525 MHz
I (1478) http_server: Partition size: total: 2884241, used: 696023
I (1494) http_server: AxeOS version: v2.10.0b2-13-gd2de33a-dirty
I (1495) http_server: Starting HTTP Server
I (1497) websocket: websocket_task starting
I (1500) dns_server: Socket created
I (1504) dns_server: Socket bound, port 53
I (1508) dns_server: Waiting for data
I (1513) BAP: Initializing BAP system
I (1517) BAP_UART: Initializing BAP UART interface
I (1523) BAP_UART: BAP UART interface initialized successfully
I (1529) BAP_UART: UART send task created successfully
I (1535) BAP_SUBSCRIPTION: BAP mode management task started
I (1541) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B

I (1547) BAP_SUBSCRIPTION: BAP mode management task started
I (1553) BAP: BAP system initialized successfully
I (1558) bitaxe: BAP interface initialized successfully
E (1856) i2c.master: i2c_master_transmit_receive(1234): i2c handle not initialized
E (1857) i2c_bitaxe: Unknown device
E (1858) EMC2103: Failed to read fan speed LSB: ESP_ERR_INVALID_ARG
W (1866) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%
E (1875) i2c.master: i2c_master_transmit(1223): i2c handle not initialized
E (1882) i2c_bitaxe: Unknown device
E (1886) EMC2103: EMC2103_set_fan_speed(57): Failed to set fan speed
I (1895) power_management: setting new vcore voltage to 1150mV
I (1900) vcore: Set ASIC voltage = 1.150V
I (1905) TPS546: Vout changed to 1.15 V
E (3711) i2c.master: i2c_master_transmit_receive(1234): i2c handle not initialized
E (3712) i2c_bitaxe: Unknown device
E (3713) EMC2103: Failed to read fan speed LSB: ESP_ERR_INVALID_ARG
W (3721) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%
E (3730) i2c.master: i2c_master_transmit(1223): i2c handle not initialized
E (3737) i2c_bitaxe: Unknown device
E (3741) EMC2103: EMC2103_set_fan_speed(57): Failed to set fan speed
I (4121) wifi:ap channel adjust o:1,1 n:6,2
I (4121) wifi:new:<6,0>, old:<1,1>, ap:<6,2>, sta:<6,0>, prof:1, snd_ch_cfg:0x0
I (4122) wifi:state: init -> auth (0xb0)
I (4139) wifi:state: auth -> assoc (0x0)
I (4147) wifi:state: assoc -> run (0x10)
I (4163) wifi:connected with low, aid = 9, channel 6, BW20, bssid = 72:a7:41:93:8b:49
I (4164) wifi:security: WPA2-PSK, phy: bgn, rssi: -61
I (4191) wifi:pm start, type: 0

I (4191) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us
I (4192) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
E (4200) wifi:sta is connecting, cannot set config
I (4204) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (4210) connect: Connected!
I (4236) wifi:<ba-add>idx:0 (ifx:0, 72:a7:41:93:8b:49), tid:6, ssn:0, winSize:64
I (5234) connect: IP Address: 192.168.1.28
I (5234) connect: Connected to SSID: low
I (5235) wifi:mode : sta (50:78:7d:16:26:ac)
I (5238) esp_netif_handlers: sta ip: 192.168.1.28, mask: 255.255.255.0, gw: 192.168.1.1
I (5245) connect: Configuration Access Point disabled
I (5466) serial: Initializing serial
I (5466) asic: Initializing BM1370
I (5474) common: Chip 0 detected: CORE_NUM: 0x00 ADDR: 0x00
I (5474) common: Chip 1 detected: CORE_NUM: 0x00 ADDR: 0x00
E (5551) i2c.master: i2c_master_transmit_receive(1234): i2c handle not initialized
E (5552) i2c_bitaxe: Unknown device
E (5553) EMC2103: Failed to read fan speed LSB: ESP_ERR_INVALID_ARG
W (5561) power_management: Ignoring invalid temperature reading: -1.0 °C
```

## Comments

### skot on 2025-08-29

On cold boot there is a mysterious I2C write to address 0x50. this isn't present on a warm boot. 

<img width="241" height="267" alt="Image" src="https://github.com/user-attachments/assets/43894c5a-eaad-4e36-8314-68a4d681eb55" />

### skot on 2025-08-29

The mystery 0x50 on cold boot is definitely coming from the EMC2103. The EMC2103-4 has a feature to load it's configuration from a I2C EEPROM. Unless this feature is specifically disabled with the correct `SHDN_SEL` strapping resistor, the EMC2103-4 will turn into a I2C Master at power-up and send a I2C write to address 0x50, looking for the EEPROM.

Apparently this 0x50 screws up our communication with the TPS546D24.

The correct `SHDN_SEL` strapping resistor for the EMC2103-4 appears to be 10k
<img width="850" height="580" alt="Image" src="https://github.com/user-attachments/assets/0cdf5983-2a0f-4afa-a4ce-4bfc9c3b5a27" />

### skot on 2025-09-02

TL:DR; set R33 to 10k 

<img width="1310" height="625" alt="Image" src="https://github.com/user-attachments/assets/4edb8aa7-6e50-4b12-9b0b-f2398ada757b" />

<img width="925" height="749" alt="Image" src="https://github.com/user-attachments/assets/892085aa-37d5-426b-8e46-06471d89b706" />
