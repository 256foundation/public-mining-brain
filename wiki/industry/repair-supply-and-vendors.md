# Repair, Supply & Vendors

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md)
> Updated: 2026-10-08
> Status: Draft

## Overview

The unglamorous industrial base of mining: who repairs miners, where boards and parts come from, how much PCB fabrication really costs, and which vendors the community trusts. Recurring theme: opacity is the business model — Skot's diagnosis of paid repair courses is 'rent seeking built up on the fact that Bitcoin mining hasn't been very open' [#5155 · 2026-07-23 · Skot Bitaxe] — and the antidote is open documentation.

## ZeusBTC & the miner-repair grey market (July 2026)

- Jayr Motta was considering ZeusBTC's paid courses for S19j Pro / APW12 maintenance and debugging but found the course site 'a bit sketchy'; asked the group for references [#5146 · 2026-07-23 · Jayr Motta]
- Skot: 'Zeus always seemed sketchy to me too. Selling PDFs and knockoff bitaxe' — 'I'd be very wary of anyone selling an Antminer repair course tbh' [#5147 · 2026-07-23 · Skot Bitaxe] [#5148 · 2026-07-23 · Skot Bitaxe]
- The counter-case: Brett Rowan ordered lots of goods from Zeus, never an issue (though never a course); Julien 'Dri' F stocked an entire repair center in Russia from Zeus, including tools hard to find elsewhere [#5150 · 2026-07-23 · Brett Rowan] [#5154 · 2026-07-23 · Julien 'Dri' F ⛏️]
- Skot's structural diagnosis: Zeus is 'rent seeking built up on the fact that Bitcoin mining hasn't been very open' — the antidote is open documentation: he posted the community HashSource/Antminer-APW12-Firmware repo and floated reverse-engineering the PSU's PIC firmware for current readings ('pretty legendary') [#5155 · 2026-07-23 · Skot Bitaxe] [#5156 · 2026-07-23 · Skot Bitaxe] [#5157 · 2026-07-23 · Skot Bitaxe] [#5158 · 2026-07-23 · Skot Bitaxe]
- APW12 part-number decoding: APW121215 = an APW12 that can output between 12-15V — really what matters when powering hashboards; the letter suffix marks subtle PSU-firmware differences between variants [#5168 · 2026-07-23 · Skot Bitaxe] [#5161 · 2026-07-23 · Jayr Motta]
- Stock Bitmain PSU data is a 'ridiculous 400 Hz (yes, Hz)' protocol [#5234 · 2026-07-26 · Skot Bitaxe]; the HashSource org publishes the Antminer APW12 PSU firmware for reverse engineering [#5156 · 2026-07-23 · Skot Bitaxe]

## Hashboard schematics & peer review

- Bitcoin Mining World published Mæstro Juergen's (MinerMEDIC) reverse-engineered Antminer T17 hashboard schematics as a free PDF, and licensed his full S21/S19-series schematics exclusively [#2362 · 2025-06-05 · Scott Offord] [#2364 · 2025-06-05 · Scott Offord] [#2370 · 2025-06-06 · Scott Offord]
- Peer review caught errors: Jstefanop flagged LDOs that 'would burn up in a second'; maintainer confirmed three errata fixed in version b (0.8 V rail fed from 1.8 V confirmed correct) [#2377 · 2025-06-07 · Jstefanop] [#2379 · 2025-06-07 · Scott Offord] [#2380 · 2025-06-07 · Scott Offord] [#2391 · 2025-06-08 · Mæstro Juergen]
- Design archaeology: the T17 and all 17-series share a layout scheme with post-XP boards — how they eliminated the opamps is an open question [#2392 · 2025-06-08 · Mæstro Juergen]

## PCB fabrication & component supply

- JLCPCB's speed and price impress: 'it's insane how fast and cheap jlcpcb can make PCBs and ship to the US' [#5171 · 2026-07-23 · Skot Bitaxe]
- Why so cheap? PizzAndy wonders how much is CCP subsidy vs genuinely superior facilities; golana: subsidies are 'a big part of it', but JLC also has huge fabrication economies of scale and owns LCSC (cheap components); US-based Macrofab runs a similar automated flow with preferred components yet can't compete on price [#5174 · 2026-07-23 · PizzAndy] [#5175 · 2026-07-23 · golana]
- Bitaxe Gamma sourcing reality: no single vendor stocks the full BOM — Jayr tried the whole BOM on LCSC and came up short; DigiKey marketplace availability comes and goes; 'Stock at these places can change really fast. So it's a moving target' [#5195 · 2026-07-23 · Jayr Motta] [#5190 · 2026-07-23 · Skot Bitaxe] [#5197 · 2026-07-23 · Skot Bitaxe]
- Link-share: https://elektronics.dev [#4917 · 2026-05-30 · Michael Schmid @Schnitzel]

## GekkoScience open-source license dispute (October 2025)

- econoalchemist lost confidence in GekkoScience: they forked the Bitaxe Gamma Turbo, modified the design and distributed it without providing complete source the next developer could take and modify — 'they broke the open-source license'; the Twitter conversation 'devolved quickly' and he got blocked [#3190 · 2025-10-30 · econoalchemist]
- Reckless Apotheosis had spent months trying to sway GekkoScience on OSHW, 'clearly, not with great success' [#3192 · 2025-10-30 · Reckless Apotheosis]

## Hosting & fleet dashboards

- Hosting warning from the field: szarka's S21 Pro sat dark at Kaboomracks — 'Kaboomracks' hosting sucks ass... Never again with these guys', 'Worst hosting ever', with an almost one-month outage as the last straw, despite Foreman access being the original draw [#2054 · 2025-05-05 · szarka] [#2065 · 2025-05-05 · szarka] [#2067 · 2025-05-05 · szarka]
- Exergy (industrial heat-reuse) runs a public fleet dashboard at fleet.exergyheat.com; community-linked instance updated with new features [#4700 · 2026-04-24 · Tyler Stevens] [#4703 · 2026-04-24 · Ankit G]
- Home-builder distribution idea: orange-pill senior folks at DR Horton — 'They built 89,000 homes last year' — selling miners as household-opex reduction; custom home builders expected to come first on the residential side [#610 · 2024-03-25 · Alex Brammer] [#611 · 2024-03-25 · Barnminer Barnmyna]

## Vendor relations: Canaan

- Tyler Stevens went live on X with Canaan (2026-08-11), soliciting community questions [#5335 · 2026-08-11 · Tyler Stevens]
- Earlier back-channel: Skot's feeler to Leo Wang at Canaan got 'they'll look into it' [#3268 · 2025-11-07 · Skot Bitaxe]

## Current-sensing on the cheap

- Turn the whole bus bar into a shunt resistor (temperature-compensate copper's positive tempco) [#5128 · 2026-07-22 · Aadhi M] [#5133 · 2026-07-22 · Skot Bitaxe] [#5143 · 2026-07-22 · golana]; ACS37200 current-sensor carriers from Pololu as the practical part [#5222 · 2026-07-26 · Skot Bitaxe]; mounting (cut the bar, solder tabs, spot-weld, press-fit bus bars) still open [#5225 · 2026-07-26 · Skot Bitaxe] [#5228 · 2026-07-26 · PizzAndy] [#5229 · 2026-07-26 · golana]

## AI compute in miner form factors? (August 2025)

> **Status: Disputed**
> Mæstro Juergen: inference 'VMs running assistants' are distributable, low-bandwidth work that could ride existing miner containers + Starlink at stranded-power sites [#2939 · 2025-08-20 · Mæstro Juergen] [#2945 · 2025-08-20 · Mæstro Juergen] [#2950 · 2025-08-20 · Mæstro Juergen] [#2959 · 2025-08-20 · Mæstro Juergen]. Wilson Mining: data centers 'have a completely different set of goals than btc miners' and are too expensive to build for mining; "No fiber, no data center" [#2944 · 2025-08-20 · Wilson Mining] [#2947 · 2025-08-20 · Wilson Mining] [#2958 · 2025-08-20 · Wilson Mining]. Dimi8146's middle ground: bitcoin mines are already starting to look like datacenters-in-containers; judge AI-in-a-container by what fits over a Starlink dish — much AI traffic stays local text, though it 'immediately breaks down when you give the bots internet access & autonomy' [#2946 · 2025-08-20 · Dimi8146] [#2949 · 2025-08-20 · Dimi8146] [#2960 · 2025-08-20 · Dimi8146] [#2962 · 2025-08-20 · Dimi8146] [#2963 · 2025-08-20 · Dimi8146]. No resolution; revisit when container-AI economics firm up.

## See Also

- [Open Mining Economics](../economics/open-mining-economics.md)
- [Ember One & the BZM2 Hardware Stack](../hardware/ember-one-bzm2.md)
- [Community Workshop Wisdom](../getting-started/community-workshop-wisdom.md)
- Same topic: [Hashrate Heating Products & Installs](hashrate-heating-products-and-installs.md)
