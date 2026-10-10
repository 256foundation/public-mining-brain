# Home Assistant Heater Control

> Sources: Hashrate Heatpunks Telegram group, 2024-08-02 → 2026-10-08
> Raw: [Hashrate Heatpunks Telegram signal digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

A hashrate heater is only a heater if something decides when it runs and how hard. The Heatpunks community converged on a layered control stack: miner firmware exposes an API, an abstraction library (pyasic, later also asic-rs) speaks every vendor's dialect, and Home Assistant (HA) via Schnitzel's hass-miner integration ties miners to thermostats, room sensors, smart plugs and electricity-rate data [#1752 · 2024-10-30 · Brett Rowan] [#1426 · 2024-10-08 · Brett Rowan] [#7666 · 2025-11-13 · Tyler Stevens]. Two control philosophies coexist: simple bang-bang on/off from a thermostat (pause/resume the miner, wide deadband) and dynamic power scaling that tracks heat demand (firmware DPS/ATM or HA automations) [#8077 · 2025-12-02 · Travis Bitkle] [#4766 · 2025-03-23 · Toine Heat Reuse]. The recurring pain points are slow retune/restart on power changes, Whatsminer API access, and miners that stop heating when the internet drops. None of this is mandatory — analog thermostats, cron jobs and direct API scripts all work — but HA wins on ecosystem: its community already integrates thermostats and sensors [#1123 · 2024-09-13 · R D] [#7783 · 2025-11-16 · Tyler Stevens] [#7754 · 2025-11-15 · Tyler Stevens].

## Rules of thumb

- **Prefer pausing over cutting power.** With HA and hass-miner you don't need to cut physical power: put miners in standby so boards are ready to turn back on; quick on/off reactivity requires miners to stay powered [#2388 · 2024-12-02 · R D] [#1038 · 2024-09-04 · R D] [#1130 · 2024-09-14 · Jonathan Y]. Caveat: firmware sleep still consumes power, so some builders still add a Wi-Fi PDU/contactor for a true off [#255 · 2024-08-02 · Toine Heat Reuse] [#257 · 2024-08-02 · Toine Heat Reuse].
- **Widen the deadband.** Pause and resume the miner from the thermostat rather than scaling power, and use e.g. 69F/73F instead of 70F/72F so it cycles less [#8077 · 2025-12-02 · Travis Bitkle] [#8079 · 2025-12-02 · Travis Bitkle].
- **Duty-cycle at an efficient wattage rather than running very low.** For 600W of need, run 1200W half the time if thermal mass allows cycles >20 minutes; efficiency tanks exponentially below 700-800W on an S19 [#1082 · 2024-09-07 · Zack Bomsta] [#1079 · 2024-09-07 · Zack Bomsta].
- **Control from an external sensor.** A room/house target (e.g. 72F) read by HA is likely the best total option for home heating; for a single ASIC a board temp target is the simple option [#2233 · 2024-11-29 · Jonathan Y] [#2234 · 2024-11-29 · Jonathan Y] [#1726 · 2024-10-28 · Tyler Stevens].
- **Never switch a miner with a bare relay or cheap plug at full power.** Use a smart switch driving a contactor; relays are not safe at this power [#203 · 2024-08-02 · Toine Heat Reuse].
- **Configure an internet-outage fallback** (Braiins `drain://` as the last pool) or the house gets cold when the ISP drops [#2897 · 2024-12-23 · Toine Heat Reuse] [#3216 · 2025-01-08 · Brett Rowan].
- **Expect churn.** pyasic and hass-miner change quickly (pyasic first, then hass-miner), so expect edge cases after upgrades [#3466 · 2025-01-15 · Brett Rowan].

## The control stack

Brett Rowan's layering, from bottom to top [#1752 · 2024-10-30 · Brett Rowan] [#1753 · 2024-10-30 · Brett Rowan] [#1754 · 2024-10-30 · Brett Rowan]:

1. **Firmware** — stock, Braiins OS, LuxOS, Vnish, ePIC, etc. The firmware, not the hardware, provides the API [#1766 · 2024-10-30 · Brett Rowan].
2. **API / SSH / Web API** — what Foreman, BTCTools and pyasic use to read data and write settings.
3. **Abstraction** — pyasic or Foreman's pickaxe. pyasic is "a union of all the miner APIs": the same fault_light_on call runs a gRPC command on Braiins, posts to /cg-bin/set_conf.cgi on Antminer stock, and calls RPC led on Whatsminer [#1753 · 2024-10-30 · Brett Rowan]. A few public companies use pyasic in-house, and AIPro built AIProMap on it [#1395 · 2024-10-08 · Brett Rowan]. In December 2025 asic-rs (256 Foundation, Rust, Python bindings done) was offered as a newer abstraction [#8421 · 2025-12-24 · Dan Sokil] [#8425 · 2025-12-24 · Brett Rowan].
4. **User-facing apps** — Foreman cloud, BTCTools, hass-miner/Home Assistant.

The mining pool is another layer of the stack [#1124 · 2024-09-13 · Bob]. A typical home architecture is "ESP32 --> HA --> MinerAPI": HA is the central brain and talks to miners via hass-miner, and one HA server can handle many ESPHome nodes and many miners [#2642 · 2024-12-08 · Michael Schmid @Schnitzel] [#2677 · 2024-12-09 · Michael Schmid @Schnitzel].

Alternatives to HA are legitimate: one system ran months on stock firmware + analog controls, then Braiins + analog, then Braiins + Home Assistant [#1123 · 2024-09-13 · R D]; scripts can talk to the miner API directly and Node red also works [#7783 · 2025-11-16 · Tyler Stevens]; a cron job sleeping a LuxOS water heater during peak hours and overnight was preferred over HA for simplicity [#5118 · 2025-03-29 · Josh]; and an earlier DIY approach used a Pi 4 with temp probes running commands when pool water left a range, but needed paid custom scripts [#2250 · 2024-11-29 · Jonathan Y]. The counterweight: HA adds complexity that makes deployment at scale in "normie homes" harder, and the HA server requirement is a pain [#1371 · 2024-10-08 · Zack Bomsta] [#1374 · 2024-10-08 · Cody Harris].

## Home Assistant + hass-miner

### Basic setup

- hass-miner (github.com/Schnitzel/hass-miner) uses pyasic to build the HA UI, and adds miner commands as entities from just an IP address [#1426 · 2024-10-08 · Brett Rowan] [#7666 · 2025-11-13 · Tyler Stevens]. Paired with a smart-thermostat integration you get variables for miner on/off, miner power limit and thermostat temp, linked with GUI automations [#7666 · 2025-11-13 · Tyler Stevens] [#7767 · 2025-11-16 · Josh].
- HA's built-in generic heater (thermostat) works with miners: add the miners as a heating device plus a room temp sensor and it cycles them on and off. The thermostat card is on/off only; adjusting power needs a custom automation [#2363 · 2024-12-02 · R D] [#2365 · 2024-12-02 · R D] [#2372 · 2024-12-02 · R D].
- Schedules can be set in HA as well [#2388 · 2024-12-02 · R D]. Common pattern: wifi plugs + hass-miner + temperature sensors around the house to ramp miners up/down or off based on home temperature and power rates [#3679 · 2025-01-20 · Dylan Seib].
- Field verdicts: works well after months of use (October 2024) [#1367 · 2024-10-08 · Mark | @satstackingpleb] [#1390 · 2024-10-08 · R D]; "rock solid" for K Pros on Braiins (January 2025) [#3465 · 2025-01-15 · R D]; by September 2025 "99% of all other miners" were described as very easy with HASS-miner [#7323 · 2025-09-09 · Dylan Seib].
- hass-miner avoids the password workaround on Whatsminers that other monitoring systems need [#2392 · 2024-12-02 · Brett Rowan] (but see the Whatsminer dispute below).
- Install/upgrade tips: remove and re-add miners after upgrades so all entities are created — they're tracked by MAC so they'll be seen as the same device [#3470 · 2025-01-15 · Brett Rowan]. Discovery in pyasic: `MinerNetwork.from_subnet("192.168.1.50/24")` then `await network.scan()` returns the correct miner types [#2255 · 2024-11-29 · Brett Rowan].

### Known issues over time

- 2024-10: latest HASS wouldn't install pre-release packages that pyasic required; advice was to hold off updating [#1403 · 2024-10-08 · Brett Rowan].
- 2024-12: pyasic lacked set_power_limit for vnish/luxos, so the hass-miner power slider couldn't control them; Wilfred Allyn was adding it (branch noted as "vnish set power limit") [#2413 · 2024-12-02 · Wilfred Allyn] [#2361 · 2024-12-02 · Wilfred Allyn] [#2364 · 2024-12-02 · Brett Rowan]. Adding more than one Nano 3 created extra devices with no entities [#2396 · 2024-12-02 · Jason] [#2402 · 2024-12-02 · Jason].
- 2025-01: a bug with Braiins and DPS — avoid relying on default values in newer versions; low power mode on a stock Antminer J Pro didn't respond in HA (GitHub issue #424) [#3468 · 2025-01-15 · Brett Rowan] [#3467 · 2025-01-15 · R D].
- 2025-03/04: HA did not work with Luxor for at least one builder, though it worked with Braiins [#5590 · 2025-04-17 · Josh] [#5118 · 2025-03-29 · Josh]. HA showed "miner temp" and chip temp as significantly different values — firmware readings may not be accurate [#5122 · 2025-03-29 · Josh] [#5124 · 2025-03-29 · Cody Harris].
- 2025-08 → 2025-11: Whatsminer M64 — see the API section below.
- Feature requests: letting hass-miner modify miner temp targets (Brett "thinking about this a bit") [#2246 · 2024-11-29 · Brett Rowan]; with Braiins you have SSH access, so control logic could in principle run on the device [#2249 · 2024-11-29 · Brett Rowan].

## Control strategies

### Bang-bang (on/off) thermostat

- Simplest firmware-side mode: two settings only — low power in Spring/Fall, full power in winter, with regular heat covering higher demand [#940 · 2024-09-04 · Jonathan Y].
- Whatsminer furnaces control heat like a resistive heater: on or off. One builder prefers more miners on low power mode to limit power cycles; Whatsminers start quickly so sleep vs off hasn't mattered [#3167 · 2025-01-08 · Patrick Patel] [#3178 · 2025-01-08 · Patrick Patel]. Thermostat bang-bang on Whatsminers: hashing in under a minute, PSU capacitors give a soft shutdown, no negative effects seen [#5204 · 2025-03-31 · Patrick Patel] [#5205 · 2025-03-31 · Patrick Patel].
- Hardware-only versions: a $10 wifi thermometer plus a smart switch/contactor scheduling the miner at preset temps [#203 · 2024-08-02 · Toine Heat Reuse] [#942 · 2024-09-04 · Toine Heat Reuse]; an Inkbird ITC-308 thermostat switch toggling the Vonets wifi bridge [#1125 · 2024-09-13 · Karl]; Braiins DPS plus a bang bang 220V timer switch for a water heater [#4911 · 2025-03-27 · Cody Harris].
- Late-2025 forced-air example: a 240V wifi relay switch turns the miner on and off, paired in HA with a Venstar T7900 local-API smart thermostat [#7877 · 2025-11-23 · Tyler Stevens]. At the Exergy office a Canaan Avalon Q is connected wirelessly to "Stage 1" of a Venstar T7900 via HA, while Stage 2 is hard-wired to the furnace (January 2026) [#8895 · 2026-01-27 · Heatpunk Forum].

### Dynamic power scaling

- Firmware-native: Braiins OS+ DPS — find chip temp at max power at 25c ambient and set DPS to downclock just below it (example: downclock by 300w at 70c chip temp, plus a wifi thermometer/switch for on/off) [#250 · 2024-08-02 · Toine Heat Reuse] [#243 · 2024-08-02 · Toine Heat Reuse]. DPS won't scale back up after downscaling; HA can handle the upscale [#382 · 2024-08-04 · Cody Harris]. LuxOS ATM was called "much better" than DPS for space heaters [#1357 · 2024-10-08 · Zack Bomsta]. Full detail in [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md).
- HA-driven: scaling in 250w increments cost only ~10 seconds downtime per step (October 2024) [#1374 · 2024-10-08 · Cody Harris] — but changing power target can stop and restart mining; live scaling only works in certain ranges on Braiins OS [#1418 · 2024-10-08 · R D] [#1419 · 2024-10-08 · Brett Rowan].
- Evolution: by December 2024 the same builder saw hass-miner scaling events go from 10 seconds back to 2 min restarts after updating BOS (and probably HA) [#2382 · 2024-12-02 · Cody Harris]. Brett said BOS+ shouldn't restart if the change is small enough and Braiins told him they added this via gRPC on X19s, though "maybe it doesnt work or they changed it" [#2376 · 2024-12-02 · Brett Rowan] [#2381 · 2024-12-02 · Brett Rowan].
- Why restarts matter for closed loops: with a miner scaling on Boiler Fluid Temp, a long restart lets the fluid cool further and triggers a deeper, unneeded scaling event [#2383 · 2024-12-02 · Cody Harris].
- Whatsminers always re-tune after a power-limit change; "Adjust Upfreq Speed" still takes minutes, and the heating view is that hitting the wattage fast beats optimal tuning — WM tuning time "seems to kill the point" [#6989 · 2025-08-12 · Jarno] [#6997 · 2025-08-12 · Jarno] [#6999 · 2025-08-12 · Tyler Stevens] [#6993 · 2025-08-12 · Tyler Stevens].
- Next step proposed (December 2025): PID control to autoscale power limits to hold room temperature [#8075 · 2025-12-02 · Dylan Seib].
- Profit/heat modes: controls in development (March 2025) flip between "Mining profitable" (max output) and "Mining not profitable" (just heat), and auto-adjust to a service limit (e.g. 160A on a 200A service) [#4837 · 2025-03-23 · Cade] [#4842 · 2025-03-23 · Cade]. Heat demand types: types 3 and 4 need a heat dump, types 1 and 2 need variable output management, and a user can become type 3 based on hashprice [#5066 · 2025-03-28 · Cade] [#5067 · 2025-03-28 · Cade].

> **Status: Disputed**
> Ramping vs on/off for hardware longevity. Tyler Stevens noted there was no data yet on whether bang-bang or ATM/DPS ramping is better for machine longevity [#4765 · 2025-03-23 · Tyler Stevens]. Toine argued for ramping: exploit downclocking efficiency and keep hashboards at more consistent temps [#4766 · 2025-03-23 · Toine Heat Reuse] [#4768 · 2025-03-23 · Toine Heat Reuse]. Patrick Patel saw no negative effects from bang-bang on Whatsminers [#5205 · 2025-03-31 · Patrick Patel], and Travis Bitkle's intuition is that air-cooled Whatsminers don't tolerate power scaling the way Antminers do with BraiinsOS DPS — frequency fiddling may have killed some old units [#8076 · 2025-12-02 · Travis Bitkle]. Heat-reuse duty also adds chip stress through bigger heat swings [#3500 · 2025-01-16 · Brett Rowan]. Best assessment as of 2026-10-09: unresolved; the practical consensus is DPS/ATM ramping on Antminers with aftermarket firmware, pause/resume with a wide deadband on Whatsminers.

> **Status: Disputed**
> Whatsminer responsiveness for demand response. Pat Kelly (Fog Hashing) described Whatsminers as not as quick to come back online, possibly older units with outdated firmware [#5202 · 2025-03-31 · Pat Kelly | Fog Hashing - Director of Sales, Global] [#5206 · 2025-03-31 · Pat Kelly | Fog Hashing - Director of Sales, Global]; Patrick Patel reports hashing in under a minute [#5205 · 2025-03-31 · Patrick Patel]. Travis later noted the M64's upfreq time is shorter than his air-cooled Whatsminers' [#8080 · 2025-12-02 · Travis Bitkle]. Best assessment: model- and firmware-dependent.

## Sensors, plugs and actuators

### ESPHome and local IoT

- ESPHome is firmware for ESP32 from the Home Assistant people; ESP32s are configured in YAML with no code and flashed [#2629 · 2024-12-08 · R D] [#2677 · 2024-12-09 · Michael Schmid @Schnitzel]. ESPHome runs on the ESP independently and can connect to HA or another web service [#2634 · 2024-12-08 · R D].
- You need ESPHome (or similar) for temp sensors and actuators like valves; time-based on/off of miners needs only HA [#2677 · 2024-12-09 · Michael Schmid @Schnitzel]. Talking to miners directly from an ESP32 would take a lot of code because pyasic is Python and nobody has built it [#2645 · 2024-12-08 · Michael Schmid @Schnitzel].
- Tips: buy ESPs in 6 packs; breakout boards and 3D-printed din rail mounts help [#2639 · 2024-12-08 · R D].
- Local vs cloud (February 2026): many HA sensors need third-party servers while ESPHome gives total local control; Zigbee, Zwave, Matter, Thread and Wifi solve slightly different problems [#8990 · 2026-02-02 · Dylan Seib]. Binding a Zigbee ecosystem to local HA is "bulletproof almost" [#9127 · 2026-02-12 · Reckless Apotheosis]. A whole-home guide used Canaan Avalon Mini 3s, zigbee temp sensors and an HA smart thermostat [#7210 · 2025-08-28 · Tyler Stevens].

### Smart plugs, relays and PDUs

- Tuya smart plugs handled S9s at 800w, but a couple burned out above 1000w [#3669 · 2025-01-20 · Dylan Seib].
- Sonoff gear uses the eWeLink app [#224 · 2024-08-02 · Toine Heat Reuse]; Sonoff S31 plugs measure power and can be flashed with Tasmota to run fully local [#7487 · 2025-10-29 · Heatpunk Forum].
- A Wi-Fi PDU switch between the mainline breaker and the PDU switches the system from temperature sensors or other triggers, or manually from anywhere [#1273 · 2024-10-05 · Trevor Bello]. PDUs with individually controlled outlets can also switch dry coolers, valves or pumps from a temperature signal [#8321 · 2025-12-17 · Dane O].
- Contactor hygiene: size with a 20% buffer (a 30 amp load * 1.2 = 36 amp, so a 40 amp contactor) and add a fuse or breaker in the contactor box [#1700 · 2024-10-24 · Dane O] [#1525 · 2024-10-12 · Toine Heat Reuse]. Contactor coils (24vac in one install) can fail repeatedly; check amp rating versus load [#2154 · 2024-11-24 · R D] [#2162 · 2024-11-25 · R D] [#2153 · 2024-11-24 · Dane O]. See [Heater Electrical and 120V Builds](../hardware/heater-electrical-and-120v-builds.md).
- Controller boards: DIN-mountable LILYGO T-Connect Pro (Ethernet touchscreen, 10amp relay, esp32) for $70 as of March 2025; Shelly1 preferred by another builder [#4412 · 2025-03-06 · Dane O] [#4416 · 2025-03-06 · Cody Harris].
- Thermostat accessories: Inkbird WiFi ITC-308 for temperature-triggered fan or outlet control; pair the fan's controller with a smart outlet so it doesn't run during curtailment [#3677 · 2025-01-20 · Toine Heat Reuse] [#3683 · 2025-01-20 · Travis Bitkle]. An electric damper recirculating air on temperature has worked well [#3670 · 2025-01-20 · Toine Heat Reuse]. A hydro install put the circulator on a smart plug so stopping flow hands off to the dry cooler at the HS05 controller's threshold [#8460 · 2025-12-26 · Britton].
- Off switch UX (November 2025): cutting ethernet instead of power is probably gentler on hardware, but fans keep running with no heat and confuse the household; smart plugs give a manual button [#7856 · 2025-11-23 · Jarno] [#7857 · 2025-11-23 · Josh].

### Power metering

- Clamp meter at the breaker or a permanently installed CT integrated into HA [#4573 · 2025-03-19 · Travis Bitkle] [#4574 · 2025-03-19 · Dev 🇳🇿]; HA can alert at a demand threshold (e.g. a 10kw demand limit) [#5209 · 2025-03-31 · Karl] [#5217 · 2025-03-31 · Dylan Seib].
- Iotawatt Wi-Fi ESP32 devices with CT ports monitor panels [#9002 · 2026-02-02 · Barnminer Barnmyna]. Farm-scale pattern: Sonoff sensors push mqtt every 30s into influxDB with on/off controls in grafana [#8538 · 2026-01-04 · Gianluca L].

## Miner APIs by vendor

| Firmware / vendor | API notes | Anchors |
|---|---|---|
| CGMiner-style (most modern miners, e.g. Whatsminer) | RPC API, json payloads via binary stream; a device with port 4028 open in an IP scanner is always a miner | [#2265 · 2024-11-29 · Brett Rowan] [#3724 · 2025-01-21 · Karl] |
| Braiins OS | CGMiner-style API for reads; settings need the gRPC API or the REST API built on it (openapi schema on up-to-date installs) | [#8424 · 2025-12-24 · Brett Rowan] [#8431 · 2025-12-24 · Brett Rowan] [#8433 · 2025-12-24 · Brett Rowan] |
| LuxOS | "way better with api integration"; Luxor was "first to market with a complete API, including pool features"; cannot shut individual boards via API while ATM runs | [#2586 · 2024-12-05 · Cade] [#8418 · 2025-12-24 · Nicolas Drouin-Audet] [#5118 · 2025-03-29 · Josh] |
| ePIC UMC | "a really good API", but a web API on port 4028 — a different protocol that conflicts in mixed fleets | [#2263 · 2024-11-29 · Brett Rowan] [#2265 · 2024-11-29 · Brett Rowan] |
| Whatsminer (BTMiner / MBT) | Docs hard to use, sample file out of date; MBT API v3.0.0 has a dynamic power set usable for PV tracking; full access requires dealing with the password setting | [#3169 · 2025-01-08 · Patrick Patel] [#5257 · 2025-04-02 · Sam] [#6995 · 2025-08-12 · Jarno] |
| Canaan Avalon (Mini3, Q, Nano3) | Mini3/Q API docs useful for HA automations — "Easy. Just API calls"; nano3 source reveals undocumented commands | [#7151 · 2025-08-21 · Heatpunk Forum] [#7323 · 2025-09-09 · Dylan Seib] [#6816 · 2025-07-24 · Brett Rowan] |

Products built on these APIs: a pool-heater product automates via LuxOS APIs and "It works really well" [#2499 · 2024-12-05 · Nicolas Drouin-Audet]; 100acresranch's controller talks to the control board via the LuxOS API [#1344 · 2024-10-08 · Mark | @satstackingpleb]. Miner discovery can also listen for UDP broadcasts on ports 14235 and 8888 (Upstream Data snippet, Apache 2.0) [#3721 · 2025-01-21 · Brett Rowan].

### Whatsminer and the M64: an evolving story

> **Status: Disputed**
> Brett Rowan said pyasic should work with Whatsminers without changing the default password [#3170 · 2025-01-08 · Brett Rowan]; Patrick Patel still had to change it [#3173 · 2025-01-08 · Patrick Patel], and in August 2025 Jarno said full API access requires dealing with the password setting [#6995 · 2025-08-12 · Jarno]. Best assessment: read-only monitoring may work without it; commands generally need the password/API-key step.

- January 2025: pyasic called "a game changer" versus the BTMiner docs; there is no drain-like option for Whatsminers [#3169 · 2025-01-08 · Patrick Patel] [#3217 · 2025-01-08 · Patrick Patel].
- August 2025: M64 power modes were believed to be only High/Med/Low, but the API has a custom power-limit variable [#6983 · 2025-08-12 · Heatpunk Forum]; the M64 wasn't reacting to HASS-miner mode-change commands [#7006 · 2025-08-12 · Dylan Seib]; pyasic's btminer RPC implementation was the reference for commands [#6996 · 2025-08-12 · Brett Rowan].
- November 2025: the M64 initially didn't work with pyasic; with HASS-miner it "mostly works" — sensors populate but commands don't, the hurdle being generating the API key [#7668 · 2025-11-13 · Tyler Stevens] [#7780 · 2025-11-16 · Dylan Seib]. Travis got a Whatsminer working through HA talking directly to the miner API, with a schedule [#7845 · 2025-11-22 · Travis Bitkle] [#7880 · 2025-11-23 · Travis Bitkle]. Reference thread: https://heatpunks.org/t/whatsminer-api-documentation/202 [#7885 · 2025-11-23 · Tyler Stevens].
- Whatsminers also had trouble with Braiins Manager scheduled curtailment [#8074 · 2025-12-02 · Travis Bitkle]. See [Whatsminer M64 Hydro Heaters](../hardware/whatsminer-m64-hydro-heaters.md).

## Curtailment around appliances, rates and solar

- Use case: curtail miners while a central furnace or AC compressor runs, then resume [#2351 · 2024-12-02 · Cade] [#2353 · 2024-12-02 · Cade]. Options: current sensors on big appliances signal HA, which turns off Wi-Fi relays [#2386 · 2024-12-02 · Dev 🇳🇿]; a Wi-Fi PDU switch curtailing on sensors [#2377 · 2024-12-02 · Toine Heat Reuse]; or transfer switches so hashrate heating runs only when e.g. the dryer is off [#2375 · 2024-12-02 · Dane O]. A related concept is a PDU that plugs into an existing Nema 14-50 outlet with the appliance plugged back through it [#5348 · 2025-04-07 · Dane O] [#5352 · 2025-04-07 · Dane O].
- Solar soak: hass-miner auto-adjusting power to excess solar was a goal from December 2024 [#2412 · 2024-12-02 · Wilfred Allyn]; CT clamps on the back feed can tune miners to absorb surplus [#8378 · 2025-12-22 · Dane O]; Edge Mining prototyped HA reading inverter data and controlling miners via hass-miner, being rebuilt as a modular system [#8377 · 2025-12-22 · gitgab] [#8380 · 2025-12-22 · gitgab]; in Mossel Bay, miners on hass-miner respond to inverter battery charge levels [#8556 · 2026-01-06 · Jason].

## Internet-outage failure modes

- The classic gotcha: the internet went out, miners stopped hashing and blew cold air, and the house got cold [#2897 · 2024-12-23 · Toine Heat Reuse].
- Braiins fix: a `drain://` pool URL wastes hashrate locally when no pool is reachable [#3216 · 2025-01-08 · Brett Rowan] [#4024 · 2025-02-13 · Cody Harris]. Example: `drain://mine.ocean.xyz.3334`; any string after `drain://` is believed to work [#3235 · 2025-01-10 · Cody Harris] [#3236 · 2025-01-10 · Brett Rowan]. Recommended heater pool order: Pool 1 DATUM, Pool 2 Ocean, Pool 3 drain:// [#4012 · 2025-02-12 · Cody Harris].
- Earlier (September–December 2024) the community was less sure: a backup pool on BOS kept a miner working [#1041 · 2024-09-04 · Jonathan Y] [#1043 · 2024-09-04 · Brett Rowan]; a "fake" last-pool trick was reported to work on BOS but not on Lux [#2932 · 2024-12-24 · Cade] [#2939 · 2024-12-24 · Nicolas Drouin-Audet].
- By November 2025 this was called "limp mode": Braiins drain:// for non-technical homes, with Epic UMC OS and Luxor having similar settings; a past LuxOS bug that kept mining on network loss has since been fixed [#7931 · 2025-11-24 · Heatpunk Forum] [#7857 · 2025-11-23 · Josh]. Hashing without network matters most when the miner is the main heat source [#7860 · 2025-11-23 · Dane O].
- Whatsminers have no drain equivalent; a Raspberry Pi local proxy was harder than expected [#4013 · 2025-02-12 · Patrick Patel] [#4020 · 2025-02-12 · Patrick Patel]. One furnace builder's pyasic-based control unit restarts miners on errors and restarts the router when the internet drops [#3152 · 2025-01-08 · Patrick Patel].

> **Status: Disputed**
> Vnish offline hashing. In a September 2024 test Vnish did not keep hashing offline, suggesting a Braiins-specific behavior [#1073 · 2024-09-06 · Karl]; others argued pool handling should be the same across firmware [#1074 · 2024-09-06 · Brett Rowan] [#1094 · 2024-09-07 · Toine Heat Reuse]. Not retested in the digest; verify on your firmware before relying on it.

## Networking

- VONETS Wi-Fi bridges accept 5-15v and can be powered from the control board, the PSU, or the IX Tech adapter (12v stepped to 5v; check with a volt meter before splicing) [#1929 · 2024-11-13 · Mark | @satstackingpleb] [#1923 · 2024-11-12 · Trevor Bello] [#1926 · 2024-11-12 · PizzAndy].
- VONETS gotchas: a clock stuck in 1969 made miners report the last share as 20000 days ago; occasional factory resets needed [#2845 · 2024-12-20 · Dane O] [#2847 · 2024-12-20 · PizzAndy]. A Loki on a Vonets pointing at the DATUM port fell back to OCEAN because the miner must be on the same network as the DATUM gateway [#7306 · 2025-09-08 · Trevor Bello] [#7311 · 2025-09-08 · Mourad D.].
- Remote sites: a 4g/5g modem plus an ethernet-to-wifi bridge, or a spare phone hotspot plus a Vonets bridge as the cheapest start [#3685 · 2025-01-21 · R D] [#3688 · 2025-01-21 · Karl].

## Revenue and hashprice data

- Braiins Insights endpoints: `https://insights.braiins.com/api/v1.0/hashrate-stats` returns only the live reading; `https://insights.braiins.com/api/v1.0/hashrate-value-history` returns history [#3863 · 2025-02-05 · Tyler Stevens] [#3866 · 2025-02-05 · Dylan Seib]. Tyler's scripts take TH/s and a start date and sum daily hashprice (fiat) or hashvalue (sats) [#3872 · 2025-02-05 · Tyler Stevens].
- Hashrateindex has an ASIC price index API [#5402 · 2025-04-10 · Wilfred Allyn]; an Ocean Mining Pool API repo was shared as a base for monitoring apps [#8509 · 2026-01-03 · Heatpunk Forum].
- Planned HA automation (October 2025): pull real-time hashprice, enter electric rate, TOU and solar, and run the miner only when profitable — meant for summer, when you want profit rather than heat [#7450 · 2025-10-23 · Tyler Stevens]. Calculators that feed this thinking are covered in [Hashrate Heating Economics](../economics/hashrate-heating-economics.md).

## Projects and resources (as of 2026-10-09)

- Exergy HA integrations (HACS-installable, January 2026): miners — Canaan Avalon Home, Bitaxe, Stealthminer, Whatsminer (Old Firmware); pools — OCEAN, DATUM, Public Pool [#8896 · 2026-01-27 · Heatpunk Forum]. Weekly Exergy HA office hours run Wednesdays 10am Mountain [#9482 · 2026-03-02 · Dylan Seib] [#9933 · 2026-04-22 · Heatpunk Forum].
- Thermine (thermine.xyz): Raspberry Pi platform for zero-knowledge users — app setpoint control, GPIO sensors, chip-frequency presets, Ocean payout views [#7750 · 2025-11-14 · Gianluca L] [#7761 · 2025-11-15 · Gianluca L] [#8443 · 2025-12-26 · Gianluca L].
- Open-source space-heater app: https://github.com/heatpunk/hashboard [#10297 · 2026-07-01 · MΛRCUS]. HA SV2 add-ons seeking testers: https://github.com/EthnTuttle/ha-sv2-addons [#9461 · 2026-02-28 · Deleted Account].
- StartOS 0.4.0 Alpha 12 includes Home Assistant [#7659 · 2025-11-13 · Tyler Stevens].
- Nicolas Drouin-Audet's heater-control mobile app supports only Bitmain via the Luxor API [#8418 · 2025-12-24 · Nicolas Drouin-Audet]. Lincoin pool offers an agent for notifications and remote control [#7438 · 2025-10-19 · Karl].
- Videos: HA heating setups explained on YouTube @nakamotoheatingsolutions [#3052 · 2025-01-03 · Michael Schmid @Schnitzel]. Radiant zone control alternative: Taco Controllers, though Dylan leans toward HA [#6380 · 2025-06-04 · Heatpunk Forum].

## See Also

- [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md)
- [asic-rs](asic-rs.md)
- [Air-Cooled Hashrate Heating](../hardware/air-cooled-hashrate-heating.md)
- [Heater Electrical and 120V Builds](../hardware/heater-electrical-and-120v-builds.md)
- [Hydronic Heat Reuse](../hardware/hydronic-heat-reuse.md)
- [Whatsminer M64 Hydro Heaters](../hardware/whatsminer-m64-hydro-heaters.md)
- [Pool Choice for Heat Miners](../pools/pool-choice-for-heat-miners.md)
- [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)
- [Hashrate Heating Products and Installs](../industry/hashrate-heating-products-and-installs.md)
- [Mujina](../firmware/mujina.md)
- [Community Workshop Wisdom](../getting-started/community-workshop-wisdom.md)
