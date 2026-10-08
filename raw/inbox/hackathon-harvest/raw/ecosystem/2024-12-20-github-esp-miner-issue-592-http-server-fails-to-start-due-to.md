# bitaxeorg/ESP-Miner issue #592: HTTP server fails to start due to default config max_open_sockets> 7 (supra 401)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/592
> Collected: 2026-10-07
> Published: 2024-12-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 592
- State: closed
- Author: adammwest
- Opened: 2024-12-20
- Closed: 2024-12-21
- Labels: none

## Description

**Describe the bug**
http server fails to start 
api/AXEos works is not accessable
ping works 

log lines from USB
I (1753) http_server: Starting HTTP Server[0m
E (1753) httpd: Config option max_open_sockets is too large (max allowed 7, 3 sockets used by HTTP server internally)
	Either decrease this or configure LWIP_MAX_SOCKETS to a larger value[0m
E (1770) http_server: start_rest_server(701): Start server failed[0m


**Expected behavior**
api/AXEos works is accessable

**Hardware**
ESP-ROM:esp32s3-20210327
401 Supra
 - Bitaxe HW vendor: Dcentral 
 - ESP-Miner FW version: 052b8bfda6b93e2c840cbc6245c82d1bcb60af2b
 - Hash Frequency: NA
 - Voltage: NA
 - Pool URL, Port, User: NA,NA,NA


**fix** 
http_server.c
```
config.max_open_sockets = 7;
```

## Comments

### eandersson on 2024-12-20

Did you build this firmware yourself? If so you need to delete the generated `sdkconfig` and rebuild the firmware.

### eandersson on 2024-12-21

Basically we updated the `sdkconfig`, but you need to manually delete the old sdk configuration otherwise the new settings won't be applied. In this case we increased the number of sockets the ESP32 is allowed to use, but we have also made other changes that are likely not reflected when you are building the firmware locally without occasionally cleaning the `sdkconfig`; e.g. lv (display), wifi and cpu frequency.
