# Bitaxe Gamma (600) & the BM1370 — What you need to know

> Source: https://osmu.xyz/t/bitaxe-gamma-600-the-bm1370-what-you-need-to-know/24
> Collected: 2026-10-10
> Published: 2026-05-27
> Registry ID: osmu-forum

OSMU | 2026-05-27 20:53:32 UTC | #1

# Bitaxe Gamma (600) & the BM1370 — What you need to know

Welcome to the Bitaxe hardware corner of OSMU! :orange_square:

This thread is a starting point for anyone running, building, or just curious about the **Bitaxe Gamma (600)** — the open-source solo miner built around Bitmain’s **BM1370** ASIC. Drop your questions, mods, and benchmarks below.

## What’s the BM1370?

The BM1370 is the SHA256 mining ASIC most commonly found in the **Antminer S21 Pro**, and it’s the chip powering the Bitaxe Gamma. Like its predecessors (BM1366, BM1368), it’s officially undocumented by Bitmain — most of what we know has been reverse-engineered by this community.

A few key specs:

- **Nominal hashrate:** ~1 to 1.4 TH/s per chip
- **Efficiency:** ~15 J/TH (the best of any chip currently used in a Bitaxe)
- **Serial protocol:** UART
- **Voltage domains:** Three internal VDD rails (VDD1, VDD2, VDD3) plus 0.8V and 1.2V IO rails

For the full pinout and details, see the OSMU Lab page: [osmu.wiki/osmu-lab/bm1370](https://osmu.wiki/osmu-lab/bm1370/)

## Why the Gamma is a big deal

The Gamma is currently the most efficient single-chip Bitaxe you can build. Compared to earlier generations:

| Bitaxe | Chip | Efficiency |
|---|---|---|
| Max (100) | BM1397 | ~30+ J/TH |
| Ultra (200) | BM1366 | ~21 J/TH |
| Supra (400) | BM1368 | ~17 J/TH |
| **Gamma (600)** | **BM1370** | **~15 J/TH** |

That means more hashes per watt — better for solo lottery mining, lower heat, quieter fans, and a lower power bill running 24/7.

## Things worth discussing here

A few starter prompts — feel free to reply to any of these or start your own thread:

- :wrench: **Tuning:** What voltage/frequency combo are you running on your Gamma? What’s your sweet spot for stability vs. hashrate?
- :thermometer: **Cooling:** Stock heatsink + fan, or have you modded it? Any temp readings from the on-chip diode (TEMP_P / TEMP_N pins)?
- :high_voltage: **PSU choice:** What are you powering yours with?
- :coin: **Solo luck:** Has anyone hit a block (or come close) on a Gamma yet? Share the story!
- :hammer_and_wrench: **Builds & mods:** Custom cases, BitHalo setups, cluster builds — post pics.

## Useful links

- :open_book: [Bitaxe Gamma (600) overview](https://osmu.wiki/bitaxe/600)
- :open_book: [BM1370 details](https://osmu.wiki/osmu-lab/bm1370/)
- :open_book: [AxeOS firmware](https://osmu.wiki/axeos/about)
- :speech_balloon: [OSMU Discord](https://discord.gg/osmu)

Happy hashing — and welcome aboard. :pick:
