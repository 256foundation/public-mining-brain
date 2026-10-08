# bitaxeorg/ESP-Miner issue #263: Add IPv6 support to AxeOS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/263
> Collected: 2026-10-07
> Published: 2024-07-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 263
- State: closed
- Author: ffrediani
- Opened: 2024-07-29
- Closed: 2025-10-01
- Labels: enhancement, help wanted, good first issue

## Description

Noticed that AxeOS is not compiled with IPv6 support and as such doesn't get an IPv6 address even when the LAN has full IPv6 support.

IPv6 is already the default Internet Protocol corresponding in some countries to over 40 - 50% of peak traffic in some countries according to several statistics specialist websites. IPv4 is legacy and several Internet Broadband Services Providers don't issue a Public IPv4 address to users anymore forcing the usage of CGNAT which makes the connecting have to pass through extra equipment, adding extra delay which may make a difference when finding a block.

Having a native IPv6 connection not only aligns it to use the newer and more modern Internet Protocol, but gives benefits in terms of network performance, resiliency to IPv4 and in some cases can be an alternative for some network filters.

ESP32 has enough space for IPv6 LWIP network stack along with IPv4 and is supported for quiet a while since ESP-IDF V2.1. Tasmota firmware which is very well know, widely used and produces a bigger binary has IPv6 enabled by default for ESP32.

Verified this by trying to connect to solo6.ckpool.org which has IPv6 support and got the following on the logs:
```
₿ (21536) stratum_task: Socket unable to connect to solo6.ckpool.org:3333 (errno 113)
₿ (26536) stratum_task: Get IP for URL: solo6.ckpool.org
```

Other known solo mining pools like public-poo.io and vkbit.com also support IPv6 on their FQDNs.

References:
[1] - https://tasmota.github.io/docs/IPv6/

## Comments

### ffrediani on 2024-08-15

Check if the appropriate arts of the code lack IPv6 related variables such as AF_INET6, PF_INET6, IPPROTO_IPV6, IPPROTO_ICMPV6, etc.

FreeRTOS also have information about IPv6 which is said to come enabled by default - https://www.freertos.org/Documentation/03-Libraries/02-FreeRTOS-plus/02-FreeRTOS-plus-TCP/03-Multiple-interface/02-IPv6-functionality

EspressIf IPv6 documentation can be found here - https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/lwip.html#ipv6-support

It is said that disabling IPv6 will save about 39 KB of firmware size and 7 KB of RAM which is nothing to concern about.

Here a good overview about what should be taken in consideration when running ESP32 with IPv6 support - https://github.com/espressif/arduino-esp32/discussions/9009

### abdullahozcelik on 2024-12-27

Latency is significantly better with IPv6 in my case, but indeed, it's not working :-( (Bitaxe 601 Gamma)

`₿ (102610) stratum_task: Socket unable to connect to solo6.ckpool.org:3333 (errno 113: Software caused connection abort)`

### abdullahozcelik on 2025-01-13

@skot any ETA for this enhancement? Thanks!

### skot on 2025-01-13

No ETA, but I do agree this would be nice to have if it’s well supported by esp-idf

### petrkr on 2025-04-28

It is supported by esp-idf, I am using IPv6 on ESP32 for long time, because of lack public IPv4 and I need connect from server to M-Bus ESP32 bridge.
