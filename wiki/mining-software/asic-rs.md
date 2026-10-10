# asic-rs and the Fleet-Tooling Stack

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md)
> Updated: 2026-10-08
> Status: Draft

## Overview

The management layer above firmware: pyasic (the Python SDK that unified vendor APIs), its Rust successor asic-rs (a 256 Foundation project), the Home Assistant integrations built on them, and the gateway/automation tooling the community builds for home miners. In 2026 this stack crossed into industrial use: Proto's proto-fleet farm-management tool is built on asic-rs.

## pyasic origins (2024)

- hass-miner integrates pyasic into Home Assistant (Brett Rowan co-maintains it); pyasic showed ~6.7k downloads/month in February 2024, largely via hass-miner pulling it in [#148 · 2024-02-25 · Michael Schmid @Schnitzel] [#149 · 2024-02-25 · econoalchemist] [#154 · 2024-02-25 · Michael Schmid @Schnitzel]
- pyasic is a unified Python SDK across vendors/firmwares — e.g. 'stop mining' maps to the right call per firmware; features the firmware itself lacks (power limiting on Antminer stock FW) surface as clean errors [#317 · 2024-03-03 · Michael Schmid @Schnitzel]
- Home Assistant + hass-miner works for a handful of miners but won't scale to 100+; the plan was a separate large-fleet manager built on pyasic as the standardization layer [#312 · 2024-03-03 · Michael Schmid @Schnitzel]
- Field report: S21, S19 XP and S19K Pro on LuxOS monitored fine via hass-miner in a Home Assistant dashboard [#304 · 2024-03-03 · Nikos]
- Home-miner feature ideas for the pyasic/HA stack: import hourly power pricing, room temperature sensors, home automations (e.g. light flashes when Braiins finds a block) [#303 · 2024-03-03 · Blizzabler]
- Upstream Data's Foreman praised for depth but criticized for its level of data/control access; a FOSS fleet manager is seen as needed [#152 · 2024-02-25 · Barnminer Barnmyna]
- Gridless committed to open-sourcing their Whatsminer headless control interface (March 2024) and offered hashrate donations to 256F [#416 · 2024-03-05 · Erik Gridless] [#419 · 2024-03-05 · Erik Gridless]

## asic-rs (2026)

- asic-rs topic created in the 256F group; repo github.com/256foundation/asic-rs (2026-03-23) [#4633 · 2026-03-23 · econoalchemist] [#4634 · 2026-03-23 · econoalchemist]
- v0.5.0 shipped 2026-04-22: many bug fixes + a rewrite of the Python bindings for stability [#4694 · 2026-04-22 · Brett Rowan]
- Maintainership: Brett Rowan maintains both pyasic and asic-rs — pyasic is being dropped in favor of asic-rs ('asic-rs is just better'); Python bindings published as pyasic-rs on PyPI; migration help offered (2026-05-26) [#4898 · 2026-05-26 · Brett Rowan] [#4899 · 2026-05-26 · Brett Rowan] [#4902 · 2026-05-26 · Brett Rowan] [#4908 · 2026-05-26 · Brett Rowan]
- Whatsminer V3 API: asic-rs ships the reference implementation of the V3 RPC and unlocks the API automatically [#4895 · 2026-05-26 · Brett Rowan] [#4897 · 2026-05-26 · Brett Rowan]
- Adoption: Proto's proto-fleet, their open-source farm-management tool released 2026-04-24, uses asic-rs for alternate miner types/firmwares without re-implementing them [#4699 · 2026-04-24 · Brett Rowan]
- Ecosystem integration idea: use asic-rs inside sv2-ui (stratum-mining/sv2-ui issue #70) [#4681 · 2026-04-20 · plebhash]
- hass-miner roadmap: swap the backend to asic-rs bindings; plus an auto-report protocol idea where miners push themselves to a metrics server [#3123 · 2025-10-15 · Brett Rowan] [#3129 · 2025-10-15 · Brett Rowan]

## Home-automation & gateway tools (2025-2026)

- csh2000's RPi+small-screen miner gateway: Wi-Fi→Ethernet internet sharing for the miner, on-screen stats (hashrate/temp/BTC price), Telegram-based remote control, and Home Assistant preinstalled (enter the miner IP, build dashboards); LibreBoard integration groundwork; first beta promised for November 2025 [#3115 · 2025-10-15 · csh2000]
- Variable-rate automations: ComEd hourly-pricing API for hourly-rate markets [#3126 · 2025-10-15 · Blizzabler]; Spanish OMIE market on/off integration exists, landing after the first beta [#3128 · 2025-10-15 · csh2000]
- thermine.xyz: open-source app (Raspberry Pi + DS1820 sensor) for temperature monitoring, released a week prior — offered as inspiration/raw material [#3127 · 2025-10-15 · Gianluca L]
- Field report: hashprice + solar-generation automation — 'I get paid to heat my home (or just mine) at +$0.13/kWh', auto switching off or to a lower mode when solar stops or the furnace is cheaper (explained on POD256) [#3130 · 2025-10-15 · Dylan Seib]
- Home-Assistant mining help: tronsington (Dylan Seib) runs weekly HA office hours Wednesdays at 10:00 Mountain Time; docs in progress [#5026 · 2026-07-03 · Tyler Stevens] [#5027 · 2026-07-03 · Dylan Seib]

## Interim Mujina paths (2025)

- Rollout timeline (May 2025): control board ~October 2025, Mujina initial release ~December 2025; hashboards can be driven from a laptop meanwhile; feature-incomplete prereleases and open dev branches well before December [#2227 · 2025-05-22 · econoalchemist] [#2234 · 2025-05-22 · Ryan]
- Interim hardware: the control board is essentially a modified Raspberry Pi CM5 IO board — a CM5 + IO board gets you something very close today; Mujina runs on nearly any Linux machine [#2236 · 2025-05-22 · Michael Schmid @Schnitzel] [#2235 · 2025-05-22 · Ryan]
- Day-one asks from the community: pyasic support for emberOne at release [#2233 · 2025-05-22 · Reckless Apotheosis]
- Libre Board end-state: USB to all your hashboards, running Mujina OS, with an integrated node and pool — an all-in-one [#2343 · 2025-06-05 · Ryan]

## See Also

- [Mujina](../firmware/mujina.md)
- [On-Demand Hashrate](../hashrate-market/on-demand-hashrate.md)
- [Hydrapool](../pools/hydrapool.md)
- Same topic: [Home Assistant Heater Control](home-assistant-heater-control.md)
