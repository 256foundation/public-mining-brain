# bitaxeorg/ESP-Miner issue #773: Webserver Crash When Using AxeOS via Mobile Browser

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/773
> Collected: 2026-10-07
> Published: 2025-03-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 773
- State: open
- Author: LisBerndt
- Opened: 2025-03-14
- Closed: n/a
- Labels: none

## Description

When operating the AxeOS via a mobile browser (in this case, Yandex), the web server crashes after a few actions (viewing logs, opening the dashboard, change settings etc.). The API gets unreachable and in some cases, the device even becomes unreachable via ping. As a test, I used the OS exclusively through a desktop browser (Chrome) for an entire day—without any issues.

Bitaxe Gamma BM1370
AxeOS 2.5.1


## Comments

### Uefi1 on 2025-03-17

Yeah, I also noticed that the web interface sometimes disconnects. I have to turn off the ASIC, wait for it to cool down, and then turn it back on.









### NotAnotherHelloWorld on 2025-03-17

I experience similar issues. Web frontend worked fine for a week without issues, but as soon as I started collecting stats using curl on API endpoint, the webserver becomes unresponsive after a few hours. Ping works fine even when web is down. WiFi deauth and letting it reconnect solves this, without having to reboot the device. I'll try to see if I can gather something useful from the logs when I have the time, maybe it's not closing sessions correctly.

### Uefi1 on 2025-03-17

> I experience similar issues. Web frontend worked fine for a week without issues, but as soon as I started collecting stats using curl on API endpoint, the webserver becomes unresponsive after a few hours. Ping works fine even when web is down. WiFi deauth and letting it reconnect solves this, without having to reboot the device. I'll try to see if I can gather something useful from the logs when I have the time, maybe it's not closing sessions correctly.

I have some suspicions that the ESP32 chip is overheating because it's located near the heatsink, where the fan blows out hot air. Some of that hot air might be hitting the ESP32, which could be why the web interface stops responding.

BitAxe is probably poorly designed—it would have been better to solder the ESP32 chip on the back of the board rather than placing it next to the processor's cooling system.

















### LisBerndt on 2025-03-17

> > I experience similar issues. Web frontend worked fine for a week without issues, but as soon as I started collecting stats using curl on API endpoint, the webserver becomes unresponsive after a few hours. Ping works fine even when web is down. WiFi deauth and letting it reconnect solves this, without having to reboot the device. I'll try to see if I can gather something useful from the logs when I have the time, maybe it's not closing sessions correctly.
> 
> I have some suspicions that the ESP32 chip is overheating because it's located near the heatsink, where the fan blows out hot air. Some of that hot air might be hitting the ESP32, which could be why the web interface stops responding.
> 
> BitAxe is probably poorly designed—it would have been better to solder the ESP32 chip on the back of the board rather than placing it next to the processor's cooling system.

I don't think it's a heating issue. This behavior first appeared about two hours in under default settings in a cool room, and as I mentioned, only when using a mobile user. In the last few days, while overclocking the device (with manual settings and additional cooling) and using only a desktop browser, the system has been running stably.



### skot on 2025-03-17

> I experience similar issues. Web frontend worked fine for a week without issues, but as soon as I started collecting stats using curl on API endpoint, the webserver becomes unresponsive after a few hours. Ping works fine even when web is down. WiFi deauth and letting it reconnect solves this, without having to reboot the device. I'll try to see if I can gather something useful from the logs when I have the time, maybe it's not closing sessions correctly.

this is interesting. We were having problems running out of sockets but I thought #571 would have helped there. @WantClue do you know what release #571 made it into?

### Uefi1 on 2025-03-17

> > I experience similar issues. Web frontend worked fine for a week without issues, but as soon as I started collecting stats using curl on API endpoint, the webserver becomes unresponsive after a few hours. Ping works fine even when web is down. WiFi deauth and letting it reconnect solves this, without having to reboot the device. I'll try to see if I can gather something useful from the logs when I have the time, maybe it's not closing sessions correctly.
> 
> this is interesting. We were having problems running out of sockets but I thought [#571](https://github.com/bitaxeorg/ESP-Miner/pull/571) would have helped there. [@WantClue](https://github.com/WantClue) do you know what release [#571](https://github.com/bitaxeorg/ESP-Miner/pull/571) made it into?

Skot, do you know when this issue occurs the most? Try refreshing the WiFi networks several times (about 5-7 times) using the magnifying glass icon to scan for signal and networks. After that, completely exit the interface and try logging in again!

By the way, there's another bug—the magnifying glass icon doesn't show all available networks, only 1-2, and sometimes none at all. It's likely that the WiFi network refresh time is too short.

### Uefi1 on 2025-03-19

> > I experience similar issues. Web frontend worked fine for a week without issues, but as soon as I started collecting stats using curl on API endpoint, the webserver becomes unresponsive after a few hours. Ping works fine even when web is down. WiFi deauth and letting it reconnect solves this, without having to reboot the device. I'll try to see if I can gather something useful from the logs when I have the time, maybe it's not closing sessions correctly.
> 
> this is interesting. We were having problems running out of sockets but I thought [#571](https://github.com/bitaxeorg/ESP-Miner/pull/571) would have helped there. [@WantClue](https://github.com/WantClue) do you know what release [#571](https://github.com/bitaxeorg/ESP-Miner/pull/571) made it into?

Skot, I finally managed to flash the Lucky Miner LV06 with your esp-miner-factory-205 firmware! I really liked the firmware—thank you so much for your hard work and contribution ! I flashed it using a USB-TTL adapter. At first, it didn’t work, but then I realized that the RXD and TXD markings were swapped.

















### NotAnotherHelloWorld on 2025-04-09

I haven't looked through all the commits for 2.6.1, but I haven't had any more issues after upgrading to this release. Been collecting stats on the API endpoint and accessing the web interface from multiple devices, with no issues for a week.

@LisBerndt have you been able to test?

### hgs-sellis on 2025-08-03

I still have this problem on 2.9.0. The web interface stops responding on my 3 miners after about a day and the only way to get it to come back seems to be a hard restart with the power cable.

### Alex71btc on 2025-08-06

I have the same problem,  web interface not reachable, mine also not shown in public pool app on umbrel after 2 days usually

### duckaxe on 2025-08-06

> I still have this problem on 2.9.0. The web interface stops responding on my 3 miners after about a day and the only way to get it to come back seems to be a hard restart with the power cable.

IP changed? Does the pool receive the shares from the miner?

### hgs-sellis on 2025-08-06

> IP changed? Does the pool receive the shares from the miner?

No, the IP has not changed. Yes, the miner is still submitting shares. It seems to be related to how much you use the web UI. If I am careful not to check on them too much, they run longer without showing the problem.



### skot on 2025-08-19

the ESP32 is a very limited-resource webserver.. but it should be able to handle a couple connections without problem. Are you just using AxeOS via one browser window? Are you running any other Bitaxe management-type tools?

### duckaxe on 2025-09-09

[v2.10.0](https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.10.0) is out. Tried it? @Alex71btc @hgs-sellis 

### Alex71btc on 2025-09-09

Thanks didn't notice, will try asap!

### Alex71btc on 2025-09-21

still same issue with v2.10.0

### hhaniel on 2025-12-10

Same issue on v2.12.0 - My BitAxe is out in the garage so bit of a pain to get to all the time so I have it plugged into a smart socket so I can power cycle it from remote. I think the API may stipp be responsive though since my prometheus/grafana setup is still getting data and plotting graphs - I may try doing a reset via API the next time it happens rather than pulling the power


### Alex71btc on 2025-12-10

Still same issue

### hhaniel on 2025-12-10

To me it feels like a momory leak - some web pages respond but the main status page does not - is there anyway to enable ssh or something to be able to look what is happening under the covers?

### vortexopenclaw on 2026-06-01

I looked at this as an issue-first explanation rather than starting from the PR.

I was able to reproduce a related WebSocket/server failure mode on current firmware using a raw `/api/ws/live` WebSocket connection followed by a masked CLOSE frame. On an intermediate cleanup revision, repeating that probe produced `Failed to acquire WebSocket client mutex` log spam and then a software reset due to exception/panic.

The code path I focused on was `main/http_server/websocket.c`. The risky behavior appears to be:

- the WebSocket registry can retain stale file descriptors after clients disconnect unexpectedly
- failed async sends only log a warning instead of removing the stale client from ESP-Miner's registry
- broadcast iterates the shared client list without the same mutex used by add/remove
- once stale clients accumulate, the small WebSocket slot pool can get consumed while the device still responds to ping
- logging while holding the WebSocket client mutex can re-enter the WebSocket log/count path, which creates a mutex re-entry failure mode

The direction I tested was:

- prune inactive WebSocket clients before counting or broadcasting
- keep registry reads/writes under the existing client mutex
- copy broadcast recipients into a short snapshot while holding the mutex
- send WebSocket frames outside the mutex
- remove failed or no-longer-WebSocket clients from ESP-Miner's registry
- avoid logging while holding the client mutex

Validation I ran on the proposed approach:

- `git diff --check`
- firmware `idf.py build`
- OTA-tested on Bitaxe Gamma
- repeated the raw `/api/ws/live` WebSocket handshake plus masked CLOSE-frame probe 5 times
- final tested commit completed the 5-iteration probe successfully
- post-probe `/api/system/info` stayed HTTP 200
- uptime continued increasing
- mining resumed around normal Gamma hashrate
- rejected shares stayed at `0`
- post-probe logs showed WebSocket connects without the mutex-acquire failure spam
- the Bitaxe Gamma was rolled back healthy afterward

Reference implementation from the closed PR, if useful for discussion: #1742
