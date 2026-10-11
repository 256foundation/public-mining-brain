# LuxOS (Luxor Firmware)

> Sources: LuxOS docs (docs.luxor.tech, verbatim via the llms-full.txt route — every docs page split out); LuxOS full-walkthrough video transcript (YouTube ivHBlP3duRg, auto-captions via yt-dlp, machine-transcript rules applied)
> Raw: [Introduction to firmware](../../raw/firmware/luxos/2026-10-10-luxos-docs-introduction-to-firmware.md); [Compatible miners](../../raw/firmware/luxos/2026-10-10-luxos-docs-compatible-miners.md); [Getting started](../../raw/firmware/luxos/2026-10-10-luxos-docs-getting-started.md); [Advanced features](../../raw/firmware/luxos/2026-10-10-luxos-docs-features-advanced-features.md); [ATM](../../raw/firmware/luxos/2026-10-10-luxos-docs-features-atm.md); [AutoTuner](../../raw/firmware/luxos/2026-10-10-luxos-docs-features-autotuner.md); [Critical temp sensor behavior](../../raw/firmware/luxos/2026-10-10-luxos-docs-features-critical-temp-sensor-behavior.md); [Power targeting](../../raw/firmware/luxos/2026-10-10-luxos-docs-features-power-targeting.md); [Temperature and fans](../../raw/firmware/luxos/2026-10-10-luxos-docs-features-temperature-and-fans.md); [API intro](../../raw/firmware/luxos/2026-10-10-luxos-docs-api-intro.md); [Video metadata](../../raw/firmware/luxos/2026-10-10-luxos-video-demo-watch-metadata.md); [Walkthrough transcript](../../raw/firmware/luxos/2026-10-10-luxos-walkthrough-transcript.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10 (docs carry no publish dates; video published 2025-07-24)
> Status: Draft

## Overview

LuxOS is Luxor's ASIC firmware for Bitmain and MicroBT machines: "LuxOS is the first and only Bitcoin ASIC firmware developed, owned, and maintained by a US-based company and the first-ever firmware to achieve SOC 2 Type 2 certification." Fee: "LuxOS firmware operates on a 2.8% fee structure. However, when using our mining pool, users benefit from free pool usage." Its thermal-management analog to Braiins DPS is **ATM**; its power analog is **Power Targeting**. Field experience from the heat-miner community lives in [Heater Firmware & Power Control](heater-firmware-and-power-control.md).

## ATM (Advanced Thermal Management)

- "Advanced Thermal Management (ATM) is a system engineered to dynamically adjust a miner's operating parameters, such as frequency and voltage, based on environmental conditions and user-defined settings."
- Continuous behavior, no config plumbing: "In high-temperature environments, ATM smoothly underclocks the miner as temperatures rise, preventing shutdowns. As the ambient temperature drops, especially during cooler evenings, ATM automatically restores the miner to its default settings, or even overclocks it if configured by the user." — "This entire process operates without the need for integrations, triggers, or manual intervention."
- The docs' contrast with Bitmain's Low Power Mode: "ATM might underclock a miner by 3% between 10 AM and 11 AM, then by 5% until 12 PM, 10% until 4 PM, reduce to 5% until 6 PM, and finally return to stock settings afterward. In contrast, Bitmain's LPM results in a constant 25% underclock from start to finish."
- Sensor fusion: "ATM reads temperature from every sensor available on the miner and factors all of them into its decisions" — hashboard temp is "the core input on all supported miners", chip temps where real on-die sensors exist, water inlet on hydro units.
- Temperature Buffer default: 8C.
- Escalation chain at the power floor: `POWER_MINIMUM_REACHED` stops underclocking; if heat keeps climbing, `EARLY_SHUTDOWN_PENDING` arms a staggered shutdown timer, then `EARLY_SHUTDOWN_TRIGGERED`.

## Temperature and fan behavior

- Three user-customizable thresholds per board: "Target Temperature" (fan algorithm), "Hot Temperature" (drives ATM steps), "Dangerous Temperature" ("the hashboard will be shutdown to prevent damage").
- Defaults — Bitmain: Target 55C, Hot 65C, Dangerous 70C (dangerous max 75C on fiber-glass boards, 72C on aluminium); Whatsminer M50/M60 family: Target 80°C, Hot 83°C, Dangerous 93°C, Chip Hot 115°C, Chip Panic 120°C.
- Sensor counts: "Bitmain Antminers typically have 4 temperature sensors per hashboard, though some models ship with 2. MicroBT Whatsminers have 1 temperature sensor per hashboard."
- Chip-temp honesty: on most S19-series Antminers, stock and aftermarket firmware display chip temps "estimated by adding" ~15°C to the hashboard sensor reading; "LuxOS does not surface them" (the offset the community measures cross-firmware — see [Heater Firmware & Power Control](heater-firmware-and-power-control.md)).
- Fail-safes: "If the miner is curtailed, fans will be set to 20%."; with no readable temps: "fans will be set to 100% for safety reasons."; hydro water-sensor failure "always reboots the affected board".
- Curtailment speed: "Drop power consumption to \~25W in under 5 seconds" / "Restore power consumption to normal levels in under 10 seconds".

## Power Targeting and AutoTuner

- "With power targeting, you tell the miner exactly how much power to consume. LuxOS continuously adjusts frequency and voltage to hold the miner at your chosen wattage." While active, "manual frequency and voltage changes are rejected."
- AutoTuner: "achieving the ideal hashrate and power consumption within \~1 hour", applying new settings "at a minimum rate of every 3 minutes"; "AutoTuner does not work on custom profiles."
- Profile ladder (docs, via [_REPORT](../../raw/firmware/luxos/_REPORT.md)): "LuxOS auto-generates 16 steps of underclocking profiles and 4 steps of overclocking profiles… Including the default profile, there are 21 built-in profiles in total for each miner."

> **Status: Disputed** — overclock profile count, video vs docs
> The walkthrough transcript (auto-captions) says "We pre-built out 16 underclock profiles and eight overclock profiles." while the docs say 16 + 4 = 21 total. ASR or presenter slip; both recorded verbatim; the docs figure is the referenceable one.

## Supported miners and install

- "LuxOS supports select models from both Bitmain and MicroBT." Bitmain: S19/T19/S19a/S19 Pro/S19j family through "S19 XP", "S19 XP+", "S19j XP" (Hydro variants included), "S21", "S21 Pro", "S21 XP", "S21+", "T21" plus Hydro variants, and Z15 Pro (Equihash). MicroBT: M50_VK40; M50S_VK20/VK30/VK80; M50S+_VK10/VK20/VK30; M50S++_VK50; M60_VK20; M60S_VK20 — all H616 boards, all with Power Targeting and on-die chip temps.
- Install constraint: "Remote Install" is required for CVITEK control boards and any machine on Bitmain firmware dated March 2024 or newer ([_REPORT](../../raw/firmware/luxos/_REPORT.md)).
- Deployment: "LuxOS is deployed with [Luxor Commander](/platform/commander/getting-started), Luxor's fleet management platform" — the free Commander Lite plan suffices; miners "must be running stock Bitmain or MicroBT firmware to install LuxOS."

## API

- Two surfaces: a raw TCP CGMiner-style API "on port 4028" (non-HTTP) plus an HTTP layer on port 8080 (`POST /api`). This is the integration surface the heater-controller community actually drives (pyasic, hass-miner — see [Home Assistant Heater Control](../mining-software/home-assistant-heater-control.md)).

## The walkthrough video (provenance)

- "LuxOS Firmware Full Demo: Install, Optimize, and Manage Your Bitcoin ASICs with Ease", Luxor Technology, published 2025-07-24, 21:37 runtime. Auto-caption transcript: 3,755 words, 47 paragraphs, single narrator — the description names him "Trey, one of our Luxor Firmware Engineers" (provenance only; no speaker labels in the transcript body, per machine-transcript rules the walkthrough "shows"/"demos").
- Demo deltas vs docs: fans to 100% "at 45°" is the demo machine's configured target, not the documented 55C default; "autotuner does not work on custom profiles" matches the docs.
- Scale framing from the description: "Whether you're running 1 or 100,000 machines, LuxOS helps you lower downtime, reduce manual overhead, and maximize hashrate and profitability."

## See Also

- [Braiins OS](braiins-os.md) — the DPS rival; fee 2.8% vs 2-2.5%
- [Vnish → HashCore](vnish-hashcore.md) — the third closed firmware
- [Farm Management Overview](../mining-software/farm-management-overview.md) — Commander plans/pricing and the MMS landscape (A11)
- [Heater Firmware & Power Control](heater-firmware-and-power-control.md) — field comparisons (ATM vs DPS for heaters)
- [Mining Firmware Security](../industry/mining-firmware-security.md)
