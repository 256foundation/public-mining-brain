# bitaxeorg/ESP-Miner issue #1756: wifi connection

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1756
> Collected: 2026-10-07
> Published: 2026-06-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1756
- State: open
- Author: skleptik
- Opened: 2026-06-06
- Closed: n/a
- Labels: question

## Description


Device Model | Gamma
Board Version | 601
ASIC Type | BM1370
-- | --
MAC Address | AC:A7:04:E4:8D:30
Free Heap Memory | 8.09 MB
• Internal | 103 kB
• Spiram | 8.02 MB
Firmware Version | v2.14.0
AxeOS Version | v2.14.0
ESP-IDF Version | v5.5.1


Constantly disconnects and reconnects, sometimes it can't connect to Wi-Fi

Downgraded to version 2.12 and now it works without any disconnect.

Log from router:
[syslog-WR1500-2026-06-06.txt](https://github.com/user-attachments/files/28668092/syslog-WR1500-2026-06-06.txt)




## Comments

### ghost on 2026-06-11

Hi !

ESP-IDF Version  v5.5.1  ??

Something not right there, it should be v5.5.3 after flashing the v2.14.0 firmware (www.bin and esp-miner.bin).

<img width="243" height="84" alt="Image" src="https://github.com/user-attachments/assets/e1de5b7b-65ea-4f90-b734-8096798e8c58" />

Can you provide a clear / clean photo of the ESP32 chip that is on this Gamma 601 so the text on it is readable.
