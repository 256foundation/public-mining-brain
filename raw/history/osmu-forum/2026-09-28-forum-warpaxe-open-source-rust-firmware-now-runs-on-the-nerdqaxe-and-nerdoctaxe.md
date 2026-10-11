# WarpAxe: open-source Rust firmware now runs on the NerdQAxe++ and NerdOctaxe

> Source: https://osmu.xyz/t/warpaxe-open-source-rust-firmware-now-runs-on-the-nerdqaxe-and-nerdoctaxe/102
> Collected: 2026-10-10
> Published: 2026-09-28
> Registry ID: osmu-forum

dvb-projekt | 2026-09-28 22:32:58 UTC | #1

Hi everyone,

WarpAxe is an open-source firmware for BM1370 miners, written from scratch in Rust (GPLv3). It started on the Bitaxe Gamma; with v0.1.7 it now also mines on two Nerd boards:

- **NerdQAxe++ Rev 6.1**: 24/7 since 25 September, on Stratum V2.
- **NerdOctaxe  Rev 3.1** (6-phase TPS53667): since 28 September. At 700 MHz / 1210 mV about 11.2 TH/s at 213 W (19 J/TH), on par with NerdOS at the same point.

It speaks the NerdOS/AxeOS HTTP API (including /api/v2/settings), so tuners and dashboards keep working. On the first start it takes Wi-Fi, pools, clock and voltage, fan settings, temperature limits and display orientation from NerdOS. The board itself you pick once in the web UI, because the NerdQAxe++ and NerdOctaxe look alike on the bus.

What’s different: signed online updates, one image for all supported boards, a web UI in 8 languages with a Swarm page for your whole LAN, and a “link the fans” option for cases where all fans run on Y-cables.

**Honest status:** early. The 4-phase Octaxe variant, NerdQX and NerdQAxe++ Rev 7 have profiles but haven’t run yet. The first install needs USB (web flasher at [WarpAxe Flasher](http://warppool.org/warpaxe) ). Please take a full backup first; going back to NerdOS is one flash.

Source and comparison with NerdOS/AxeOS: [dvb-projekt/dvb-WarpAxe: Open-source firmware for the Bitaxe Gamma and NerdQAxe++, written in Rust: AxeOS-compatible API, Stratum V1 + V2, signed online updates, one image for all boards. - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe)

Feedback and bug reports very welcome, especially from other Nerd boards.

![1-octaxe-dashboard](https://osmu.xyz/uploads/default/original/1X/ce604874ffdfdeff14e3d74ffc09ebda033baeb7.png)

![web-swarm](https://osmu.xyz/uploads/default/original/1X/7bd136ea3fef77eb2ab627b76239d0c04dc0d3da.jpeg)

![2-octaxe-lcd](https://osmu.xyz/uploads/default/original/1X/a36ff85fc0262b79575b5640910cbf19cee03dd9.png)

-------------------------

dvb-projekt | 2026-09-29 05:10:05 UTC | #2

Update: v0.1.8 decodes every job’s coinbase like AxeOS and shows your share of a found block, the coinbase value and all outputs (Stratum V1 and V2). Also a new dashboard and a calmer history chart. Notes: [Releases - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases)

![2-dashboard](https://osmu.xyz/uploads/default/original/1X/6089b5bb8766ba791c61236c01b7eebaa1023dfa.jpeg)

![3-dashboard-gamma](https://osmu.xyz/uploads/default/original/1X/b8282416a12f97cf779b82a882416fd980853b00.jpeg)

![1-pool-payout](https://osmu.xyz/uploads/default/original/1X/4e9bd1fecdef8562fc44cf74a1bd3a1e671f7eed.jpeg)

-------------------------

dvb-projekt | 2026-09-30 00:12:37 UTC | #3

WarpAxe v0.1.9 is out :rocket: Correction to what I said before: the NerdOctaxe was ~8 % behind NerdOS (new work only every ~22 s). Fixed – work every 500 ms like NerdOS, now 11.59 vs 11.71 TH/s at the pool. Also new: NerdAxe Gaia and BitForge Nano run (Nano on Standard: 2.19 vs 2.10 TH/s on ForgeOS). [WarpAxe v0.1.9 - dvb-projekt/dvb-WarpAxe - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpAxe/releases/tag/v0.1.9)

![1-gaia-dashboard](https://osmu.xyz/uploads/default/original/1X/0d4a38797493d88bb639fed00cfe86c4aa1f0a73.jpeg)

![2-nano-dashboard](https://osmu.xyz/uploads/default/original/1X/64702966a635d61783699514bea720474d9a6d7a.jpeg)
