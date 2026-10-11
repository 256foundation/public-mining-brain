# _REPORT — Phase A9: LuxOS Firmware (luxos-docs + luxos-video-demo)

Collected: 2026-10-10. Agent: fetch subagent. Cap target ~12 files; delivered 13 captures + this report (features section is multi-page, and the raw `.vtt` is retained as transcript provenance).

## Files captured (14 total, all under raw/firmware/luxos/)

| # | File | Registry ID | Posture |
|---|------|-------------|---------|
| 1 | 2026-10-10-luxos-docs-introduction-to-firmware.md | luxos-docs | verbatim |
| 2 | 2026-10-10-luxos-docs-compatible-miners.md | luxos-docs | verbatim |
| 3 | 2026-10-10-luxos-docs-getting-started.md | luxos-docs | verbatim |
| 4 | 2026-10-10-luxos-docs-features-advanced-features.md | luxos-docs | verbatim |
| 5 | 2026-10-10-luxos-docs-features-atm.md | luxos-docs | verbatim |
| 6 | 2026-10-10-luxos-docs-features-autotuner.md | luxos-docs | verbatim |
| 7 | 2026-10-10-luxos-docs-features-critical-temp-sensor-behavior.md | luxos-docs | verbatim |
| 8 | 2026-10-10-luxos-docs-features-power-targeting.md | luxos-docs | verbatim |
| 9 | 2026-10-10-luxos-docs-features-temperature-and-fans.md | luxos-docs | verbatim |
| 10 | 2026-10-10-luxos-docs-api-intro.md | luxos-docs | verbatim |
| 11 | 2026-10-10-luxos-video-demo-watch-metadata.md | luxos-video-demo | extract (SSR metadata; description verbatim) |
| 12 | 2026-10-10-luxos-walkthrough-transcript.md | luxos-video-demo | extract (auto-caption transcript) |
| 13 | luxos-walkthrough.en.vtt | luxos-video-demo | raw source (unmodified yt-dlp VTT, kept for provenance) |
| 14 | _REPORT.md | — | — |

Docs captures are verbatim page bodies split out of `llms-full.txt` by page-delimiter headers (`# Title (url)`); Mintlify Markdown escapes (e.g. `\~25W`) and JSX components (`<Tabs>`, `<Callout>`) are preserved as they appear in the source file.

## HTTP / fetch statuses

| Target | Status |
|---|---|
| https://docs.luxor.tech/llms-full.txt (browser UA, --compressed) | **HTTP 200**, 316,293 bytes — proven capture path confirmed |
| https://www.youtube.com/watch?v=ivHBlP3duRg SSR (browser UA) | **HTTP 200**, 333,345 bytes |
| yt-dlp auto-subs (`--write-auto-subs --sub-lang en --sub-format vtt`) | exit 0, 185.63 KiB VTT |

## Transcript status

- 3,755 words, 47 paragraphs, English (`en`, single caption track, ASR auto-captions — not human subtitles).
- Single narrator; the walkthrough's own description names him "Trey, one of our Luxor Firmware Engineers" (recorded in provenance only — no speaker labels in transcript body).
- ASR quirks left verbatim: "Luxos"/"Lux OS", "the minor" (for "miner"), "hash board".
- `pip install --user yt-dlp` failed (PEP 668 externally-managed environment, macOS Homebrew Python) → worked around with an isolated scratch venv (yt-dlp 2026.08.19); nothing installed system-wide, nothing outside raw/firmware/luxos/ written in the repo.

## Key facts (exact literal quotes → file)

### ATM (Advanced Thermal Management) behavior
- "Advanced Thermal Management (ATM) is a system engineered to dynamically adjust a miner's operating parameters, such as frequency and voltage, based on environmental conditions and user-defined settings." → 2026-10-10-luxos-docs-features-atm.md
- "In high-temperature environments, ATM smoothly underclocks the miner as temperatures rise, preventing shutdowns. As the ambient temperature drops, especially during cooler evenings, ATM automatically restores the miner to its default settings, or even overclocks it if configured by the user." → features-atm.md
- "This entire process operates without the need for integrations, triggers, or manual intervention." → features-atm.md
- vs Bitmain LPM: "For example, ATM might underclock a miner by 3% between 10 AM and 11 AM, then by 5% until 12 PM, 10% until 4 PM, reduce to 5% until 6 PM, and finally return to stock settings afterward. In contrast, Bitmain's LPM results in a constant 25% underclock from start to finish." → features-atm.md (near-identical example also in introduction-to-firmware.md)
- "ATM reads temperature from every sensor available on the miner and factors all of them into its decisions." — hashboard temp is "the core input on all supported miners"; chip temps on miners with real on-die sensors; water inlet on hydro units. → features-atm.md
- Temperature Buffer: "The default and [recommended](../kb/recommended-settings) value is 8C." → features-atm.md
- Intro framing: "When deployed correctly ATM leads to much higher uptime of machines." and "LuxOS ATM can underclock as much as needed to keep a miner hashing in high ambient temperatures." → introduction-to-firmware.md
- Power-targeting interaction: "If the ATM reaches the configured power minimum while temperatures are still rising, the firmware emits a `POWER_MINIMUM_REACHED` event and stops underclocking further. If the heat keeps climbing past the early-shutdown threshold while sitting at the minimum, the firmware arms a staggered shutdown timer (`EARLY_SHUTDOWN_PENDING`) and, if conditions don't improve, eventually shuts the miner down (`EARLY_SHUTDOWN_TRIGGERED`)." → features-power-targeting.md

### Temperature / power management
- Three user-customizable temps: "Target Temperature: Used for the fan algorithm…", "Hot Temperature: Used by [ATM…] to drive steps up and steps down…", "Dangerous Temperature: When any of the board sensor temperatures reaches this temperature the hashboard will be shutdown to prevent damage." Plus chip and water-inlet equivalents. → features-temperature-and-fans.md
- Bitmain defaults: "Target Temperature 55C / Hot Temperature 65C / Dangerous Temperature 70C"; dangerous "Maximum of 75C, ideally a 8C buffer from your Hot Temperature" (fiber-glass boards) or "Maximum of 72C" (aluminium boards). → features-temperature-and-fans.md
- Whatsminer M50/M60 family defaults: Target 80°C, Hot 83°C, Dangerous 93°C, Chip Hot 115°C, Chip Panic 120°C (M50S+_VK20 target is 74°C). → features-temperature-and-fans.md
- Sensor counts: "Bitmain Antminers typically have 4 temperature sensors per hashboard, though some models ship with 2. MicroBT Whatsminers have 1 temperature sensor per hashboard." → features-temperature-and-fans.md
- Chip-temp honesty: "On most S19-series Antminers, stock firmware and other aftermarket firmwares display chip temperatures that are estimated by adding ~15°C to the hashboard sensor reading… LuxOS does not surface them." → features-temperature-and-fans.md
- Critical-sensor logic: "Hydro water-sensor failure always reboots the affected board, regardless of `min_per_board` or die-temp coverage." / "The miner only shuts itself down when `min_per_board == 0` and no critical board sensors, no die-temp coverage, and no working water sensors remain anywhere." → features-critical-temp-sensor-behavior.md
- Fan rules: "If the miner is curtailed, fans will be set to 20%." / no readable temps + PSU enabled + ≥1 hashboard → "fans will be set to 100% for safety reasons." → features-advanced-features.md / features-temperature-and-fans.md
- Power Targeting: "With power targeting, you tell the miner exactly how much power to consume. LuxOS continuously adjusts frequency and voltage to hold the miner at your chosen wattage." / "While power targeting is active, manual frequency and voltage changes are rejected." → features-power-targeting.md
- AutoTuner: "achieving the ideal hashrate and power consumption within ~1 hour"; intro page: AutoTuner "applies new settings at a minimum rate of every 3 minutes". → features-autotuner.md / introduction-to-firmware.md
- Curtailment: "Drop power consumption to ~25W in under 5 seconds." / "Restore power consumption to normal levels in under 10 seconds." → introduction-to-firmware.md
- Profiles: "LuxOS auto-generates 16 steps of underclocking profiles and 4 steps of overclocking profiles… Including the default profile, there are 21 built-in profiles in total for each miner." (25 MHz / 0.15 V steps) → features section quoted via introduction-to-firmware; profile mechanics in presetprofiles page (not captured — see Parks).

### Supported miners
- "LuxOS supports select models from both Bitmain and MicroBT." → compatible-miners.md
- Bitmain: S19/T19/S19a/S19 Pro/S19j family through S19 XP/S19 XP+/S19j XP (incl. Hydro variants), S21/S21 Pro/S21 XP/S21+/T21 + Hydro variants, Z15 Pro (Equihash) — with per-model control-board + hashboard-model tables and Power Targeting / On-die Chip Temps capability columns. → compatible-miners.md
- MicroBT (Whatsminer): M50_VK40; M50S_VK20/VK30/VK80; M50S+_VK10/VK20/VK30; M50S++_VK50; M60_VK20; M60S_VK20 — all H616 control board, all with Power Targeting ✓ and On-die Chip Temps ✓. → compatible-miners.md
- Install constraint: "Remote Install is required for: Machines with CVITEK control boards; Any machine with Bitmain Firmware dated March 2024 or newer." → compatible-miners.md
- Deployment: "LuxOS is deployed with [Luxor Commander]… You only need the free **Commander Lite** plan to deploy LuxOS." Miners "must be running stock Bitmain or MicroBT firmware to install LuxOS." → getting-started.md

### Device-count / scale claims
- Video description: "Whether you're running 1 or 100,000 machines, LuxOS helps you lower downtime, reduce manual overhead, and maximize hashrate and profitability." → watch-metadata.md
- "LuxOS is the first and only Bitcoin ASIC firmware developed, owned, and maintained by a US-based company and the first-ever firmware to achieve SOC 2 Type 2 certification." → introduction-to-firmware.md
- Fees: "LuxOS firmware operates on a 2.8% fee structure. However, when using our mining pool, users benefit from free pool usage." → introduction-to-firmware.md
- API surface: TCP (raw, non-HTTP) CGMiner-style API "on port `4028`" plus an HTTP layer on port 8080 (`POST /api`). → api-intro.md

### Video-vs-docs deltas worth flagging
- Transcript: "We pre-built out 16 underclock profiles and eight overclock profiles." — docs say 16 under + **4** over (= 21 total). ASR or presenter slip; both recorded verbatim. → transcript vs introduction-to-firmware.
- Transcript demo box: fans to 100% "at 45°", underclock "if any board sensor hits 65°", shutdown "at 70… You can increase that to 75" — 45° is the demo machine's configured target, not the documented 55C default. → transcript.
- Transcript: "autotuner does not work on custom profiles" (matches docs: "AutoTuner does not work on custom profiles.").

## Parks / not captured (cap)

- Direct docs.luxor.tech page routes were not probed this session — llms-full.txt (the proven path) returned 200 on first try; no 403 encountered.
- `pip install --user yt-dlp` failure text: "note: If you believe this is a mistake, please contact your Python installation or OS distribution provider… externally-managed-environment" (PEP 668). Resolved via scratch venv; nothing parked.
- llms-full.txt carries no per-page publish dates → docs captures use `Published: n/d`.
- Available in llms-full.txt but skipped under the file cap: `firmware/changelog` (~1,350 lines of release notes), `features/presetprofiles` (full page), `api/available_commands`, per-command API refs (`atm`, `atmset`, `powertargetset`, `tempctrlset`, …), KB pages (`remoteinstall`, `recommended-settings`, `eventstroubleshooting`), `tools_and_integrations/luxosinstaller`, `tools_and_integrations/luxos/installation` (Python `luxos` package v0.0.7). Single-file re-split can be done later from the same llms-full.txt if needed.
