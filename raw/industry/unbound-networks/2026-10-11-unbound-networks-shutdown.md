# Unbound Networks — shutdown record (was legit, shut down)

> Registry ID: unbound-networks
> Source: unboundnetworks.com (domain probe) + repo-captured evidence inventory
> Collected: 2026-10-11
> Method: domain probe + Wayback CDX query, curl/browser UA; Tyler confirmation in session same day
> Published: company active ~2023–2025; shut down before 2026-10-11
> Posture: extract
> As-Of: 2026-10-11

Tyler (2026-10-11, session): "unbound networks was legit. but it shut down." — this memo converts the A15 skip decision into a dormant registry row, DesiweMiner-style.

## 1. Domain probe (2026-10-11)

| URL | Result |
|---|---|
| https://unboundnetworks.com | HTTP 200, 114 bytes — registrar JS stub: `window.location.href="/lander"` (parked domain) |
| https://unbound256.com | DNS failure (000) |
| X handle | @UnBound256 (bio: "Unbound Networks") — not captured |

## 2. Wayback Machine

- CDX for `unboundnetworks.com`: snapshots 2013-06-25 → 2018-08-07 (an unrelated prior "Unbound Networks") plus one bitcoin-era capture, 2025-07-14 08:28:47 — which is already the parked `/lander` stub. The live site the Undermine 2025 audience referenced ("I didn't know your website was live until like yesterday") is unrecoverable from public archives as of 2026-10-11.

## 3. Evidence inventory (anchors already captured in this repo)

**Book (print anchor).** raw/books/braiins-heat-reuse/04-successful-case-studies.md — `Unbound Networks: "reuses industrial miner hashboards, pre-modifying the machines for easy home use and quiet operation." (p. 57)`

**Undermine 2025 panel** (raw/history/heatpunks-summit/20251111-undermine-2025-small-scale-bitcoin-mining-panel.md):
- "what we're doing on Unbound is we're trying to take the uh old generation, three or four generations removed hardware. We're trying to make super cheap um form factor fitting type space heaters" [00:02:42]
- "We have a little over a pahash of them out there in people's homes out out in Montana. My business partner Clay is out there building that network." [00:16:39]
- "go to Unbound Network, get yourself a space heater" [00:31:40]

**Undermine 2025 challenges panel** (raw/history/heatpunks-summit/20251111-undermine-2025-what-are-the-challenges-ahead-for-hashrate-heading.md): intro identifies "Zack Bombster … the guy who did all this … Cloud Line and … the Loki boards and he's … the guy behind Unbound" [00:02:11–02:43]; Clay tells the founding story (rentals → miner → heating systems).

**Telegram provenance** (#549 · 2024-03-22 · Zack Bomsta, in raw/history/2026-10-08-256f-telegram-signal.md and wiki/hardware/asic-thermals-and-heat-reuse.md): Braiins designed/built several hundred Marathon rigs (Bitmain S17/BM1397 on aluminum PCB, custom firmware, 110 °C dangerous-temp default) and "donated them to Unbound hoping we could find a use for them" — the aluminum-PCB + 7nm high-temp platform finding.

**Press (pointer, bot-walled — not captured).** ABC4 Utah / NerdWallet, "Replace Your HVAC with BTC? These Innovators Are Doing it" — Unbound Networks in Provo, Utah; radiant-floor-heat pilot.

**End state.** LinkedIn (Jack Ball, project engineer): "Unbound Networks. Nov 2023 - Aug 2025 … Missoula, Montana … Sold ASIC-based heating systems that repurpose Bitcoin mining" — employment records end 2025-08. Domain parked by 2026-10-11 (and already at the 2025-07-14 capture). Tyler confirms shut down.

## 4. Registry outcome

`unbound-networks` added to Heat-Reuse & Home-Mining Companies as `dormant`, cadence `static`, posture `extract` — real company, print + summit + press anchors, no live surface to monitor.
