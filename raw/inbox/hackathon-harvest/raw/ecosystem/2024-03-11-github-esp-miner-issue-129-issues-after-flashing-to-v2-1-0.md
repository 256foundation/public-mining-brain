# bitaxeorg/ESP-Miner issue #129: Issues after flashing to v2.1.0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/129
> Collected: 2026-10-07
> Published: 2024-03-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 129
- State: closed
- Author: thalpius
- Opened: 2024-03-11
- Closed: 2024-03-11
- Labels: none

## Description

After I flashed my 201 BitAxe the screen turned off and I can't get it back to life. When I connect the BitAxe I got an error once, but now I don't see any logs coming in. I used bitaxe-web-flasher to flash it back to an older firmware version, but I can't seem to get it fully working since I can't access the Bitaxe anymore. Anyone any idea?

Here is the log I got after flashing to v2.1.0.

`E (847) SPIFFS: mount failed, -10025
E (857) http_server: Failed to mount or format filesystem
SP_ERROR_CHECK failed: esp_err_t 0xffffffff (ESP_FAIL) at 0x4200d854
file: "./main/http_server/http_server.c" line 529
func: start_rest_server
expression: init_fs()`

## Comments

### thalpius on 2024-03-11

Got it working again after flashing a few times using the web-flasher. Upgrading to v2.1.0 now does seem to work.
