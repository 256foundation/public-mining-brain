# WarpAxe: open-source Rust firmware for the Bitaxe Gamma (early, feedback welcome)

> Source: https://osmu.xyz/t/warpaxe-open-source-rust-firmware-for-the-bitaxe-gamma-early-feedback-welcome/100
> Collected: 2026-10-10
> Published: 2026-09-28
> Registry ID: osmu-forum

dvb-projekt | 2026-09-28 12:42:33 UTC | #1

Hi everyone,

I’m building **WarpAxe**, an open-source firmware for the Bitaxe Gamma, written from scratch in Rust (GPLv3). It replaces AxeOS on the device and speaks the same HTTP API, so tuners, dashboards and fleet tools that talk to AxeOS keep working.

**What it does differently**

- **Signed online updates:** the miner fetches a new release and checks its signature before it installs it.
- **One image for all supported boards:** the board is detected on the first start; your Wi-Fi and pool settings from AxeOS are kept.
- **Stratum V1 (optional TLS) and Stratum V2**, with a fallback pool.
- **Web UI in 8 languages**, including a Swarm page that shows every miner on your LAN (AxeOS, NerdOS, ForgeOS or WarpAxe).
- **Host-tested drivers:** chip, chain and board drivers run in CI against a simulated chain and I²C bus.

**Where AxeOS is ahead:** far more boards, years of use by a large community, plus things WarpAxe doesn’t have (yet): scoreboard, themes, the BAP accessory port, Wi-Fi setup over Bluetooth. The README has a side-by-side comparison, checked against the AxeOS source; corrections welcome.

**Status:** early, v0.1.6. It mines 24/7 on my Gamma 602 (about 1.33 TH/s at 17.7 J/TH) and on a NerdQAxe++. Other boards have a profile but haven’t been tested yet. Please read the supported-boards list before you flash.

**Install / go back:** install from the browser at [WarpAxe Flasher](http://warppool.org/warpaxe) (Chrome/Edge over USB). Going back to AxeOS takes one flash with the official Bitaxe flasher.

Source, comparison and release notes: [dvb-projekt/dvb-WarpAxe: Open-source firmware for the Bitaxe Gamma and NerdQAxe++, written in Rust: AxeOS-compatible API, Stratum V1 + V2, signed online updates, one image for all boards. - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe)

I’d love to hear from people who try it, especially bug reports and results from other Gamma units.

![web-swarm](https://osmu.xyz/uploads/default/original/1X/7bd136ea3fef77eb2ab627b76239d0c04dc0d3da.jpeg)

![oled-rotation](https://osmu.xyz/uploads/default/original/1X/50413697cf0be32d4c24369b58c69a60a2c25b7e.png)

![web-dashboard-gamma](https://osmu.xyz/uploads/default/original/1X/684351f5fce6df95420830272751cc586529f2e3.png)

-------------------------

dvb-projekt | 2026-09-30 00:11:45 UTC | #2

WarpAxe v0.1.9 is out. For the Bitaxe Gamma little changes (API: core current with its limit, cause of a regulator stop, the build’s git hash). The main work went into the Nerd boards: they now pace work like NerdOS and hash on par with it (NerdOctaxe 11.59 vs 11.71 TH/s at the pool), and the NerdAxe Gaia and BitForge Nano run (Nano on its Standard preset at the pool: 2.19 TH/s vs 2.10 on ForgeOS).

Release notes: [WarpAxe v0.1.9 - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases/tag/v0.1.9)

-------------------------

dvb-projekt | 2026-09-30 05:53:00 UTC | #3

WarpAxe v0.1.10 is out, mainly for Bitaxe owners:

• Profiles for the Gamma Duo (650), Gamma Turbo (801), Naja Duo (1201) and Gamma Hex (1300), matched against AxeOS’s source (pins, regulator, EMC2103 fan chip, colour display on Naja/Hex). None has run on hardware yet; each is offered on the first start and taken only when you pick it.

• Heads-up for Gamma Duo owners: v0.1.9 took a Duo for a plain Gamma (its board version 650 lies in the Gamma’s 600 range). Please use v0.1.10 or later on a Duo.

• The regulator now shows on the Gamma’s type plate, and the dashboard marks the current as input or output as the board measures it.

If you have one of these boards and a way back to AxeOS over USB, feedback is very welcome. The web flasher already has v0.1.10.

Release notes: [WarpAxe v0.1.10 - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases/tag/v0.1.10)

-------------------------

dvb-projekt | 2026-10-01 07:00:37 UTC | #4

WarpAxe v0.1.11 and v0.1.12 are out.

For Bitaxe owners mainly: AxeOS’s hashrateMonitor is there with the same JSON (per chip total, four domains, error counter) and errorPercentage, read from the chips’ own counters once a second, plus errorPercentage1m over a minute; domain watchdogs work unchanged. The 0/1 fields (isUsingFallbackStratum, useFallbackStratum, useNTP, autofanspeed) are numbers again as in AxeOS. The Gamma Duo and Gamma Turbo profiles have now run on hardware at a user’s; Naja Duo and Hex still haven’t. The Naja Duo and Hex show the Bitaxe wordmark on the boot screen, with skot’s consent (thanks!).

Release notes: [Releases - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases)

-------------------------

dvb-projekt | 2026-10-01 12:39:22 UTC | #5

WarpAxe v0.1.13 is out. Two things that may interest BM1373 owners: the BM1373 really has eight hash-domain counters — four at 0x88–0x8B as on the BM1370 and four more at 0xAC–0xAF, each counting an eighth of the 0x8C total (found with a read-only register scan on a NerdAxe Gaia). AxeOS reads the first four and doubles them; WarpAxe now reads all eight. And on the Naja Duo, free values now go up to 600 MHz, the documented overclock (untested by me). Also fixed: replies to several register reads in a row could be cut off in the receive buffer, which is where “empty” domains came from.

Release notes: [WarpAxe v0.1.13 - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases/tag/v0.1.13)

-------------------------

dvb-projekt | 2026-10-02 08:30:38 UTC | #6

arpAxe v0.1.14 is out. Mainly for Nerd boards: the second fan output (M1) now follows the chips by default, as on NerdOS. Before, it followed the regulator temperature, and a NerdOctaxe-γ v2.2 overheated on auto because its regulator stayed cool while the chips heated up — linked fans fixed it. The fans also stay at full while the chips warm up after a start or an overheat stop. And the API now reports NerdOS’s stratum.usingFallback next to AxeOS’s isUsingFallbackStratum, so scripts for either firmware keep working. Thanks to John11 for the testing.

Release notes: [WarpAxe v0.1.14 - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases/tag/v0.1.14)

-------------------------

dvb-projekt | 2026-10-03 13:16:09 UTC | #7

arpAxe v0.1.15 is out. One finding that may matter beyond WarpAxe: the TPS546 keeps its output on through an ESP reset, so during an update restart or in ROM download mode the ASICs sit powered at their last clock with nothing controlling fans or temperature. On a BitForge Nano, three minutes in download mode gave 82 °C chip / 95 °C regulator. WarpAxe now switches the core voltage off before every restart and first thing at boot. Also new: the web flasher saves a full flash backup before installing and can restore it (in Chrome on macOS that needed small acknowledged read packets — the serial driver drops bytes of 0xFF-heavy data otherwise).

Release notes: [WarpAxe v0.1.15 - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases/tag/v0.1.15)

-------------------------

dvb-projekt | 2026-10-06 01:19:47 UTC | #8

WarpAxe v0.1.16 is out. A finding that may matter beyond WarpAxe: the TPS546 only regulates accurately (and only warns on undervoltage) between 0.25 and 0.75 V at its reference, so the clean output range is 0.25–0.75 V divided by VOUT_SCALE_LOOP — 1–3 V on the 0.25 most boards use. WarpAxe now never commands a core voltage below that and publishes the floor as regulatorMinMv. On the NerdAxe Gaia the stock firmware’s 0.25 put every voltage (800–970 mV) below the range; after a cold start the board’s own straps set 0.5, so WarpAxe uses that now (7 h at 340 MHz / 950 mV: 945 mV in every minute, 0 rejects, same power). Also new: the Wi-Fi radio no longer uses modem sleep, ping ~65 ms → ~7 ms.

Release notes: [WarpAxe v0.1.16 - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases/tag/v0.1.16)

-------------------------

dvb-projekt | 2026-10-06 02:07:21 UTC | #9

Quick follow-up: v0.1.17 lifts the clock cap on the Gamma Duo and Gamma Turbo. With ?oc the clock is free there, as on the plain Gamma and in AxeOS; core voltage stays capped at 1250 mV. Thanks to John11, who runs two Turbos at 850 MHz under AXP90 coolers.

Release notes: [WarpAxe v0.1.17 - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases/tag/v0.1.17)

-------------------------

dvb-projekt | 2026-10-07 08:58:40 UTC | #10

WarpAxe is at v0.1.20. For Bitaxe owners: the online-update bar no longer gets stuck at “Writing 100 %” on some networks (thanks John11), and GET /api/v2/dashboard now reports the hash rate and the error hash rate per chip in NerdOS’s format, so a weak chip shows up before the pool rejects anything. New and experimental: the same image also runs on a LilyGO T-Display-S3 (NerdMiner hardware) and hashes on the ESP32-S3 itself, about 290 kH/s.

Release notes: [Releases - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases)

-------------------------

dvb-projekt | 2026-10-08 15:14:39 UTC | #11

WarpAxe is at v0.1.21. For Bitaxe owners with more than one chip (Gamma Duo, Gamma Turbo): the hash counter card now has a total line, all chips’ counted hash rate and errors together (an idea from John11). On the experimental T-Display-S3 (NerdMiner hardware) the CPU really runs at 240 MHz now, about 290 kH/s, and it can mine over Stratum V2 on WarpPool.

Release notes: [Releases - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases)

-------------------------

dvb-projekt | 2026-10-08 15:19:51 UTC | #12

WarpAxe is at v0.1.22. For Bitaxe owners: an update that does not boot now rolls back to the previous version by itself (after one reinstall over USB, which writes the new bootloader; settings are kept), and pool or worker changes apply at once without a restart. New board: the NerdNOS (BM1397), at 300 MHz the pool counted about 190 GH/s with WarpAxe against 180 with its stock firmware.

Release notes: [Releases - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases)

-------------------------

dvb-projekt | 2026-10-09 15:33:20 UTC | #13

arpAxe is at v0.1.24. For Nerd board owners: the BM1370 on the NerdQAxe++, NerdOctaxe and NerdQX (Q1370) now starts with NerdOS’s chip init instead of ESP-Miner’s. ESP-Miner changed a core-clock trim in August (0x0C to 0x10), and with that my NerdOctaxe at 700 MHz sometimes came up with one hash domain at about 3 % of its rate, until a power cycle. With NerdOS’s value it came up clean 6 times out of 6. Bitaxes keep ESP-Miner’s init.

Also since my last post, v0.1.23: on every board the dashboard shows the best difficulty since the last start next to the all-time best, which survives restarts; the NerdNOS display’s device page shows the ESP32 temperature, effective rate, Wi-Fi signal and restart clock instead of dashes; and the Bitcoin whitepaper is no longer built into the image (the web UI links to the copy next to the installer), which leaves about 180 KB more room.

Release notes: [Releases - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases)
