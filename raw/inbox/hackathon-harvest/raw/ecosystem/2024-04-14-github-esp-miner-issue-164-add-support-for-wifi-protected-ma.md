# bitaxeorg/ESP-Miner issue #164: Add support for WiFi Protected Management Frames

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/164
> Collected: 2026-10-07
> Published: 2024-04-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 164
- State: closed
- Author: skot
- Opened: 2024-04-14
- Closed: 2026-06-02
- Labels: enhancement

## Description

There are some reports that WiFi Protected Management Frames (PMF) cause the ESP32-S3 to reset. It sounds like ESP-IDF supports PMF if configured? https://docs.espressif.com/projects/esp-idf/en/v5.2.1/esp32s3/api-guides/wifi-security.html

## Comments

### skot on 2024-04-14

https://x.com/_17410742_/status/1779399722634973642?s=46&t=8isHpCQqCFogL4byGwt7DA

### mutatrum on 2024-04-17

I didn't have any luck with disabling PMF, but disabling RSSI on my Asus AP got me to an uptime of 2 hours now. (BitAxe 400). I haven't done cross-testing yet, so currently both are disabled.

https://njump.me/nevent1qqsx60c5cms4yvnjzq99frp0hqx8g73u8zqqan5t3tngs4telm8kszszypftfgrkhjammsap4marwdvpdnm5nya3hrdjq2cpezputzl8ltvt6ft3kjk

### mutatrum on 2024-04-17

Searching on ESP32 wifi disconnects, also took me here: https://community.home-assistant.io/t/esp32-disconnects/370258/3

So maybe it's a combination of things. I couldn't find in ESP-Miner what power_save_mode is set to on the Espessif.

### mutatrum on 2024-04-17

With both PMF and RSSI disabled, I get a reconnect every 2 - 3 hours. Definitely an improvement, but not stable yet.

### mutatrum on 2024-04-18

I've captured api/system/info every minute, this is the uptime:

![chart (8)](https://github.com/skot/ESP-Miner/assets/56344102/bc8ec46a-d646-4725-8e1c-fe5421e88851)

No idea why it restarts more often that can be related to the wifi signal, other than that it's the start of the evening here, and maybe more signals are around from 5 p.m.? I wasn't even in the room.

HTH. If there are other things I can plot/capture, please let me know.

### mutatrum on 2026-06-02

I think this was fixed by #365
