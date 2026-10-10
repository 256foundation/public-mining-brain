# bitaxeorg/ESP-Miner issue #1180: Rescan and connect for stronger WiFi signal

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1180
> Collected: 2026-10-07
> Published: 2025-08-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1180
- State: open
- Author: sz4bi
- Opened: 2025-08-05
- Closed: n/a
- Labels: bug

## Description

I have multiple wireless access points (APs) with the same SSID to provide full coverage throughout the house. AxeOS connects to the strongest AP at startup. However, if that AP is restarted, AxeOS connects to another AP with the same SSID, even if it has a weaker signal. When the nearest AP becomes available again, AxeOS does not reconnect to it.

It would be great to implement a feature that rescans the available networks and reconnects to the one with the strongest signal.

## Comments

### skot on 2025-08-19

I have seen this too in my multi-AP setup. Not sure how to do best do this however.. do we need to be constantly scanning even though we have a connection?

### sz4bi on 2025-08-20

I don't think constant scanning is needed, just do a scan like every 10-30-60 minutes. In case of a wifi disconnection, this scan is already happening, but we should run this "scan" more frequently.

### mutatrum on 2025-11-06

I'm not sure the ESP can do this without disconnecting, so it's possible you'll reconnect to the pool and lose share counts. The dashboard might also lose connection, as the reconnect logic is not 100% solid there either. Unfortunately, the ESP32-S3 doesn't have roaming capabilities.

Although there's this, so information is contradictory: https://github.com/espressif/esp-idf/tree/27baa4a2/examples/wifi/roaming/roaming_app

Addition, this looks like a better example: https://github.com/espressif/esp-idf/blob/27baa4a26138c5caf1386202746928bed5b5fe16/components/esp_wifi/wifi_apps/roaming_app/src/README.md

### WantClue on 2026-06-05

I was testing alot with the esp feature for doing AP roaming, currently I have not finalized it. It has some bugs and issues and the reconnect is not always working, but I'll try to spend some time on it again to get it working.
