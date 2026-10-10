# bitaxeorg/ESP-Miner issue #218: No connection to wifis with SSID length of 32 bytes

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/218
> Collected: 2026-10-07
> Published: 2024-06-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 218
- State: closed
- Author: kisenberg
- Opened: 2024-06-12
- Closed: 2024-12-01
- Labels: none

## Description

**Describe the bug**
If a wifi has a SSID with a length of 32 bytes, Bitaxe is not able to connect. Only connections to wifis with SSID up to a length of 31 bytes are possible.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to AxeOS settings.
2. Enter 32 bytes long SSID into field of "WiFi SSID".
3. Click "Save".
4. Click "Restart".
5. Bitaxe displays try to connect the wifi forever.

**Expected behavior**
A connection to wifis with SSID of 32 bytes length should be possible, because an SSID can be 32 bytes long.

**Screenshots & Photos**
n/a

**Hardware (please complete the following information):**
 - Bitaxe HW version: Supra 400
 - Bitaxe HW vendor: D-Central
 - ESP-Miner FW version: 2.1.8
 - Hash Frequency: 490 MhZ
 - Voltage: 1166mV
 - Pool URL, Port, User:

**Additional context**
n/a


## Comments

### tommywatson on 2024-06-12

Unfortunately it looks like we are limited to 31 characters by the esp-idf wifi libraries, the structure defined the ssid attribute as

`uint8_t ssid[32];                         /**< SSID of target AP. */`

Including the null terminator that limits the SSID to 31 characters.

https://github.com/espressif/esp-idf/blob/8760e6d2a7e19913bc40675dd71f374bcd51b0ae/components/esp_wifi/include/esp_wifi_types_generic.h#L354


### kisenberg on 2024-07-11

So, there will be no chance to change that from 32 bytes to 33 bytes with the null terminator?
