# Repair, Supply & Vendors

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07; bitaxeorg/legitlist (README, vendor and maintainer guides, releases), captured 2026-10-07; legitlist vendor-application PRs, 2026-03 → 2026-09 (index captured 2026-10-10); bitaxeorg/ESP-Miner GitHub issues, 2024-01 → 2026-09
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md); [legitlist README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-legitlist.md); [legitlist vendor guide](../../raw/hardware/bitaxe-osmu/github-legitlist-vendor-guide.md); [legitlist vendor PR index](../../raw/hardware/bitaxe-osmu/2026-10-10-github-legitlist-vendor-pr-index.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
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

## Open-source miner vendors & the legitlist

Because Bitaxe is open hardware, anyone may build and sell it — so the community keeps its own list of sellers that ship genuine, license-respecting boards. As-Of 2026-10-10.

- **What it is:** bitaxeorg/legitlist is the community-verified list of genuine Bitaxe vendors; listings sync to bitaxe.org/buy, and the pitch is "No backroom deals. No paid placements. Just miners vouching for miners." The repo itself is AGPL v3 ([legitlist README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-legitlist.md)). It replaced an older bitaxe.org page that was a curated list by Skot of sellers supporting the project ([bitaxe.org legacy list](../../raw/hardware/bitaxe-osmu/bitaxe-org-legacy-list.md)); the GitHub backend, which shows the reasoning behind each listing, went live 2026-05-06 ([X: skot](../../raw/history/256f-research/2026-10-07-x-notable-skot-bitaxe.md)).
- **How a vendor gets listed:** open a PR adding `vendors/{slug}.json` plus a square logo (400×400px recommended, max 200 KB); PR titles start with Add/Update/Remove/Deactivate vendor; the community reviews and maintainers merge. Open PRs have two weeks to address requested changes or are closed ([legitlist README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-legitlist.md); [vendor guide](../../raw/hardware/bitaxe-osmu/github-legitlist-vendor-guide.md)).
- **Approval criteria:** genuine Bitaxe hardware (not clones or unverified boards sold as Bitaxe), a live shop, community presence, no open fraud/counterfeit reports, correct "Bitaxe" spelling, real product photos, and Bitaxe product pages that link to bitaxe.org. Selling closed-source miners is fine as long as they are not Bitaxe derivatives sold in violation of the open-source license ([vendor guide](../../raw/hardware/bitaxe-osmu/github-legitlist-vendor-guide.md); [maintainer guide](../../raw/hardware/bitaxe-osmu/github-legitlist-maintainers.md)).
- **Removal:** vendors can be removed for no longer selling genuine hardware, confirmed fraud/counterfeit reports, or going dark; a soft removal sets `active` to false, and only active vendors are displayed ([maintainer guide](../../raw/hardware/bitaxe-osmu/github-legitlist-maintainers.md); [legitlist README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-legitlist.md)).
- **The application pipeline itself is built and hardened in public** (49 PRs to date, 2026-03-11 → 2026-09-20; 41 merged, 6 closed unmerged, 2 open). PR #12 (merged 2026-03-20) codified the approval criteria as a maintainer review checklist plus contributor-facing criteria, renamed the pitch from "core-team approved" to "maintainer-approved", and added "Final inclusion is always at maintainer discretion and based on community trust, listing quality, and alignment with the Bitaxe open-source ecosystem" ([PR #12](../../raw/hardware/bitaxe-osmu/2026-10-10-github-legitlist-pr-12-clarify-vendor-approval-criteria.md); [vendor PR index](../../raw/hardware/bitaxe-osmu/2026-10-10-github-legitlist-vendor-pr-index.md)). Same-day PRs #13 and #14 hardened the tooling: TikTok and Nostr social keys with slug validation tightened to "lowercase letters, numbers, and hyphens only", and CI switched from an inline validator to the repository's own `npm run validate` to remove "validation drift between local and CI checks" ([PR #13](../../raw/hardware/bitaxe-osmu/2026-10-10-github-legitlist-pr-13-tiktok-nostr-social-slug-validation.md); [PR #14](../../raw/hardware/bitaxe-osmu/2026-10-10-github-legitlist-pr-14-harden-validation-workflow-parser-resilience.md)). PR #45 (merged 2026-06-04) made CI enforce the process mechanically: PR titles must start with `Add vendor:`, `Update vendor:`, `Remove vendor:` or `Deactivate vendor:`, template placeholders must be replaced, and vendor confirmations must be answered Yes/No for add/update PRs ([PR #45](../../raw/hardware/bitaxe-osmu/2026-10-10-github-legitlist-pr-45-add-pr-metadata-validation.md)).
- **Add → deactivate lifecycle:** the list's first soft-deactivation is also its only one so far — Bitaxe.de was listed on 2026-04-25 (PR #20) and deactivated on 2026-08-19 (PR #54) by setting `"active": false`, "while the factual trust questions documented in #38 are resolved"; the PR is explicit that it "is not a finding that Bitaxe.de is a scam or has committed fraud". A hard-deletion revert (PR #52) was closed unmerged the day before for skipping the documented soft-deactivation path, and the listing "can be reconsidered through the normal public process" — one churn data point so far, handled through the documented mechanism ([PR #20](../../raw/hardware/bitaxe-osmu/2026-10-10-github-legitlist-pr-20-add-vendor-bitaxe-de.md); [PR #54](../../raw/hardware/bitaxe-osmu/2026-10-10-github-legitlist-pr-54-deactivate-vendor-bitaxe-de.md); [vendor PR index](../../raw/hardware/bitaxe-osmu/2026-10-10-github-legitlist-vendor-pr-index.md)).
- **Size and spread (snapshot 2026-10-07):** 27 vendors — 17 in Europe, 5 in North America, 2 in South America, 2 in Asia Pacific, 1 in India ([legitlist regions](../../raw/history/256f-research/2026-10-07-github-legitlist-vendor-regions.md)). legitlist releases: v1.0.0 and v1.1.0 on 2026-03-12, v1.2.0 on 2026-03-20, v1.2.1 on 2026-06-04 ([legitlist releases](../../raw/hardware/bitaxe-osmu/github-legitlist-releases.md)).
- **Trademark:** bitaxe.org states the Bitaxe name and logo are internationally trademarked by bitaxeorg ([bitaxe.org legacy list](../../raw/hardware/bitaxe-osmu/bitaxe-org-legacy-list.md)).

### Clone-support policy

- **Firmware maintainers do not support clones.** LuckyMiner devices (LV06, LV07) are not supported by ESP-Miner; maintainers call them knockoffs that turned the Bitaxe work into a closed-source product, and skot called LuckyMiner "a scam product" ([ESP-Miner #351](../../raw/firmware/esp-miner/2024-09-25-github-esp-miner-issue-351-board-version-0-11-vs-board-versi.md); [ESP-Miner #1024](../../raw/firmware/esp-miner/2025-06-10-github-esp-miner-issue-1024-vin-and-vout-error.md)). Closed-source ESP-Miner derivatives are also turned away, because their changes are unknown ([ESP-Miner #1457](../../raw/firmware/esp-miner/2025-12-15-github-esp-miner-issue-1457-open-the-password-field.md)).
- **Unreleased prototypes are not supported either:** GT board 800 prototypes were sold before the 801 release; maintainers tell owners to return the unit or ask for an 801, revert to the shipped firmware, or get firmware from the manufacturer ([ESP-Miner #1543](../../raw/firmware/esp-miner/2026-02-06-github-esp-miner-issue-1543-800xxx-support-for-lastest-firmw.md)).
- **Support routing:** GitHub issues are not customer support — buyers go to their seller, DIY builders to the OSMU Discord ([bitaxeGamma #29](../../raw/hardware/bitaxe-osmu/2025-03-14-github-bitaxegamma-issue-29-bitaxe-gamma-not-hashing.md)). Maintainer advice since 2024: buy from legit sellers, because "Bitaxe being FOSS, there are many vendors that cut corners or make other modifications" ([ESP-Miner #94](../../raw/firmware/esp-miner/2024-01-21-github-esp-miner-issue-94-about-board-version-distinction.md)).
- **Silent part swaps:** even listed hardware can ship with substituted parts — one early small batch from one vendor used ESP32-S3 modules without PSRAM, which newer firmware cannot run; that vendor fixed affected units ([ESP-Miner #1998](../../raw/firmware/esp-miner/2026-09-24-github-esp-miner-issue-1998-psram-issue-gamma-601-totally-br.md)). Model and module details: [Bitaxe Models & Open-Source Miner Family](../hardware/bitaxe-models.md).

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
- [Bitaxe Models & Open-Source Miner Family](../hardware/bitaxe-models.md)
- [Community Workshop Wisdom](../getting-started/community-workshop-wisdom.md)
- Same topic: [Hashrate Heating Products & Installs](hashrate-heating-products-and-installs.md)
