# Braiins OS

> Sources: braiins.com/os-firmware product page (Webflow SSR, 64 KB); Braiins Academy docs (academy.braiins.com — the former docs.braiins.com — Rspress, verbatim via its llms.md route); ASIC Miner Value cross-check not applicable (firmware, not hardware); Cambridge DMIR 2025 for installed-base share
> Raw: [Braiins OS landing](../../raw/firmware/braiins-os/2026-10-10-braiinos-os-firmware-landing.md); [About](../../raw/firmware/braiins-os/2026-10-10-braiinos-about.md); [Autotuning](../../raw/firmware/braiins-os/2026-10-10-braiinos-autotuning.md); [DPS](../../raw/firmware/braiins-os/2026-10-10-braiinos-dps.md); [Configuration](../../raw/firmware/braiins-os/2026-10-10-braiinos-configuration.md); [Installation](../../raw/firmware/braiins-os/2026-10-10-braiinos-installation.md); [License FAQ](../../raw/firmware/braiins-os/2026-10-10-braiinos-faq-license.md); [DPS/Autotuning FAQ](../../raw/firmware/braiins-os/2026-10-10-braiinos-faq-dps-autotuning.md); [Technical resources + supported models](../../raw/firmware/braiins-os/2026-10-10-braiinos-technical-resources.md); [Fetch _REPORT (license quotes, platform version)](../../raw/firmware/braiins-os/_REPORT.md); [DMIR 2025 firmware mix](../../raw/economics/cambridge-report/dmir-2025-extract.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10 (docs build 2026-10-02, commit 2b65ece)
> Status: Draft

## Overview

Braiins OS is "an advanced autotuning firmware that optimizes the performance of your ASIC miners by automatically finding the optimal frequency and voltage for each individual chip, giving more work to high quality chips and less to low quality chips". It is the firmware side of the Braiins stack (pool + OS + toolbox), positioned against stock Bitmain firmware and aftermarket rivals LuxOS and Vnish/HashCore. Releases are date-versioned "YY-MM" ("a release of Braiins OS occuring in October 2021 would be named as Braiins OS 21.10" — "occuring" sic, verbatim); the current generation is 26.x. For the heat-miner field experience with DPS, see [Heater Firmware & Power Control](heater-firmware-and-power-control.md).

## Dev fee and the license server

- Pricing: "**2.5% dev fee**" (landing); FAQ: "When you use Braiins OS, we collect a 2-2.5% dev fee (depending on the hardware model) by directing that percentage of your hashing power to our pool. It’s up to you which pool you mine with for the remaining 97.5-98%."
- The fee is hashrate-directed, not exact: "the dev fee is never exactly the specified percentage of your total hashing power, as this number is always changing in real-time" — bounded by "a fixed tolerance".
- License mechanics: each device acquires a license from Braiins' license server before mining; "Licenses obtained by devices are automatically renewed every **60 minutes**"; licenses "remain valid for a duration of 12 hours" after connectivity drops. Dev-fee traffic uses port `3336` to `*.braiins.com`. (License §5.4 default where no percentage is published: "the percentage shall be 2,5 %" — comma decimal, per the [_REPORT](../../raw/firmware/braiins-os/_REPORT.md) license quote.)
- Fallback penalty (license §3.10, quoted in the license-FAQ capture): if verification fails, "the cryptocurrency mining device will only use 95 % of its processing power (so called hash rate) until the next verification procedure is successfully conducted" ([_REPORT](../../raw/firmware/braiins-os/_REPORT.md), quoting license §3.10).
- Default fee in the license (§5.4) if not otherwise indicated: "the percentage shall be 2,5 %" (comma decimal in the original).
- Pool rebate: mining on Braiins Pool with Braiins OS earns "a 0% effective pool fee rate instead of the standard 2.5%" — collected then rebated daily; a full-Braiins-OS fleet gets "a full 100% refund of the pool fee".

## Autotuning

- Per-chip calibration: "Per-chip autotuning is the process of software calibrating the frequencies and voltages on every individual chip on a hash board to achieve higher efficiency."
- Speed dispute between Braiins' own pages: docs say "Machines can be tuned in about 10 minutes", while the landing FAQ says "The tuning usually takes between 1-9 hours to complete, depending on the type of control board, power limit specified and the quality of the chips in your device." Not a contradiction so much as best-case vs full-sweep framing — both verbatim.

> **Status: Disputed** — autotune duration, Braiins docs vs Braiins landing
> "about 10 minutes" (academy autotuning page) vs "between 1-9 hours" (landing FAQ) vs "can take several hours" (docs FAQ). Best assessment: per-power-target tuning is minutes-to-hours depending on control board and chip quality; the maker's own pages disagree on the headline number.

- Profiles persist: "Once the tuning is finished, the settings "profile" is saved, and you can return to it at any time in the future and immediately apply it without waiting for the machine to re-tune."
- Expectations spread: "Some machines will be in better condition" (better cooling, higher-quality chips) — "Those machines might see a 15%+ improvement in J/TH efficiency while others will only improve by 5%".
- Hashboard power split: "Braiins OS assumes you have 3 hashboards and will take these values and apply 1/3 of the power limit to each hashboard" — even if one is disabled/damaged.
- Tuner config lives at `/etc/bosminer-autotune.json`; the mining daemon is BOSminer, Braiins' CGMiner fork — "Basic subset of the upstream CGMiner API as well as several new commands" ([_REPORT](../../raw/firmware/braiins-os/_REPORT.md)).
- New in the 2026 docs (beta): a **Continuous Tuner** — "instead of switching between fixed profiles, it keeps re-optimizing frequencies and voltages predictively every few minutes, and adapts automatically as chips degrade over time."

## DPS (Dynamic Performance Scaling)

- Definition: "DPS dynamically adjusts power and hash-rate targets based on real-time conditions, helping miners maintain the ideal balance between performance and stability."
- **Default flipped in 26.01** (docs table): new installations run "DPS is OFF by default" (25.11 and older) vs "DPS is ON by default" (26.01 and newer); upgraded machines migrate settings with On Start Target = 66%.
- Downscale trigger: "Chip temperature is greater than or equal to the HOT temperature" (3-min timeout); upscale in Normal mode at "Chip temperature is less than or equal to the TARGET temperature"; Boost mode runs until "8°C below the HOT temperature" — "this mode can increase the stress on the hardware at the cost of more hash-rate, proceed at your own risk!"
- Upscale needs both: "The miner's temperature is at least 5 degrees below the HOT limit and the fans are running below 80%."
- Profile ladder: "All profiles that are tuned by DPS are saved and do not need retuning… This way miners can tune approximately 6 - 15 targets, depending on what step size you are using."
- Anti-cycling memory: "If the miner scales up power and then quickly downscales within 30 minutes, DPS takes note of the conditions" (target, temperature, fan speed); "The DPS memory automatically clears itself after 32 hours if no triggering event occurs".
- Grid Alignment snaps on-start targets to the step grid (66% of 3500 W = 2310 W → "2300 W").
- Modes "NORMAL and BOOST"; ramping for curtailment Pause/Resume ≈ 2 s each ([_REPORT](../../raw/firmware/braiins-os/_REPORT.md)).

## Supported hardware (39 current rows)

- "Below is a table listing the devices supported by Braiins OS, including the compatible control boards, hashboard models, and power supply units (PSUs)." — 39 rows in "Current Miners" (37 Antminer variants + Braiins Mini Miner BMM 100/BMM 101) plus 10 legacy rows (S9/S9i/S9j, S17 family, T17 family).
- Boundary, verbatim: "The miners listed below are supported, but development has been discontinued. Specifically, for the X17 series , development stopped at version 23.01 , and for the S9 series, it ended at version 22.08.1" (spacing sic).
- S21-class current coverage runs through S21 XP Hyd. and "S21E XP Hyd. U3" (BM1368/BM1370 chips); S19-class through "S19 XP+ Hyd." and "S19e XP Hyd.".
- Batch install via Braiins Toolbox: "remote batch installations on all the Antminer S21 and S19 series control boards: Zynq/Xilinx, Amlogic, BeagleBone Black, and Cvitek/CV1835."
- SD-card route for S19 (Zynq/BeagleBone): MicroSD "minimum capacity of 128 MB" — "avoid using cards with capacities greater than 8 GB"; "Simple copy to SD card will not work. The SD card has to be flashed!"

## Scale, share and posture

- Maker claims: "Proven and reliable since 2018, Braiins OS has operated on hundreds of thousands of miners" and "**3 GW+** Over 3 gigawatts running Braiins OS." Note the phrasing — "hundreds of thousands", not a 1.5M-class figure (contrast [Vnish/HashCore](vnish-hashcore.md)).
- Independent share datapoint (Cambridge DMIR 2025, survey June–Sept 2024): Braiins OS 5.6% of surveyed fleet firmware vs stock 44.4% / Vnish 26.4% / custom 17.6% / LuxOS 3.3% ([DMIR extract](../../raw/economics/cambridge-report/dmir-2025-extract.md), p.53).
- Security posture: "Braiins has completed a SOC 1 Type 2 and SOC 2 Type 2 audit".
- Stratum V2: "The first firmware ever providing users the benefits of Stratum V2" (maker claim); "both Braiins OS and Braiins OS are fully backwards compatible with Stratum V1" (duplicated name in original, verbatim).
- No open-source claim appears in the 2026 docs — distribution is license-server based (since 23.04); the only GitHub link captured is `github.com/braiins/bos-plus-api`. The 2018 S9-era braiins-os repo is historic.
- Cooling modes automatic/manual/immersion; "Hot Temperature triggers Dynamic Performance Scaling (if enabled); Dangerous Temperature will stop mining" with a suggested "10° separation between those values".

## Docs platform note

docs.braiins.com now redirects to **academy.braiins.com** (Rspress v2.0.17 "Braiins Academy"). The `llms.txt` route works and every doc page has a sibling `.md` — the same agent-friendly convention as docs.luxor.tech and docs.hashcore.com. Wiki references to docs.braiins.com URLs should be updated to academy.braiins.com.

## See Also

- [LuxOS](luxos.md) — the ATM rival; per-firmware comparison in [Heater Firmware & Power Control](heater-firmware-and-power-control.md)
- [Vnish → HashCore](vnish-hashcore.md) — the rebrand and the device-count claims
- [Mining Firmware Security](../industry/mining-firmware-security.md) — license-server dependence as an attack/availability surface
- [Stratum V1 & V2 in Practice](../protocols/stratum-in-practice.md) — SV2 support context
