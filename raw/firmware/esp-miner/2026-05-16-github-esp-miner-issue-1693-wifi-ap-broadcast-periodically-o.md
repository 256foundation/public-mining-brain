# bitaxeorg/ESP-Miner issue #1693: WiFi AP broadcast periodically occurs even after association

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1693
> Collected: 2026-10-07
> Published: 2026-05-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1693
- State: closed
- Author: disturbedlegend
- Opened: 2026-05-16
- Closed: 2026-06-25
- Labels: none

## Description

When tracking down the causes of nearby broadcasting APs that interfere with my own wireless, I noted that the BitAxe 601 (v2.13.1) periodically re-activates its AP mode and broadcasts its SSID. The dashboard of my wireless controller is limited, so I was not able to determine the exact time/duration/pattern of activation, only that it appears to occur at least once per day.

I confirmed that this issue still occurs after re-configuring a defaulted configuration, wiped via the web firmware tool.

Also, I confirmed that this broadcast occurs without the unit having rebooted during that window (via uptime)

Device Model: Gamma
Board Version: 601
ASIC Type: BM1370
Firmware Version: v2.13.1
AxeOS Version: v2.13.1
ESP-IDF Version: v5.5.2


## Comments

### WantClue on 2026-06-11

Do you have any usb logs that you could provide for that ? 

### WantClue on 2026-06-25

no response for over two weeks, gonna close this. If any further information is provided this issue will be reopened
