# Presidio Bitcoin Fundraiser and the Case for Commoditizing Mining

> Sources: 256 Foundation (newsroom: It's Time to Commoditize Bitcoin Mining), collected 2026-10-07
> Raw: [newsroom: Presidio Bitcoin fundraiser](../../raw/foundation/256foundation-org-newsroom-presidio-bitcoin-fundraiser.md)
> Updated: 2026-10-07

## Overview

On Saturday, September 12, the 256 Foundation held its first private, in-person fundraiser at Presidio Bitcoin in San Francisco. Operators, donors, engineers and vendors from the mining industry heard a presentation and then joined hands-on workshops led by the Lead Maintainers of the four core projects. The foundation published the argument it made there under the title "It's Time to Commoditize Bitcoin Mining". Its thesis: Bitcoin mining will be open-source, or Bitcoin remains permissioned.

## The venue

Presidio Bitcoin is a co-working and events space for open-source Bitcoin builders, inside the Presidio at the foot of the Golden Gate Bridge. The post ties the choice to the Bay Area's open-source history: BSD at UC Berkeley, GitHub founded there in 2008, and the Linux Foundation based in the city.

## The argument

**Mature industries run on commoditized inputs.** Nobody reinvents aluminum alloy. The post cites the Hall-Héroult process: the price of aluminum fell from $4.86 a pound to 78 cents in five years, and whole industries grew on top of the metal.

**Open source is a force multiplier.** Public work can be audited, fixed, extended and reused by anyone. Closed projects cannot match that pace. Projects that reach critical mass create what the post calls "gunpowder moments you can't undo", such as the Linux kernel, TCP and HTTP.

**A company is the wrong vehicle.** A company wants to capture value from what it creates. That works for specialization. It does not work for commodities, and the post says this is a big part of why the mining stack was never commoditized.

**Bitcoin's own ethos requires it.** The white paper describes one CPU, one vote. Miners later split from nodes, and the mining part of the stack became centralized and permissioned.

**A nonprofit can break the loop.** There is little demand for an open stack because there are no open tools, and no open tools because there is little demand. The post says Linux broke the same cycle 26 years ago when serious operators adopted it. With no incentive to capture value, the foundation says it can be the steward that gets the building blocks to that point.

## The status quo it describes

A modern miner is four building blocks: a hashboard, a control board, firmware and a pool. None is commoditized.

- No datasheets, pinouts or specs for the chips.
- No open control board to start from.
- Firmware that cannot be audited. The post cites Antbleed, a remote shutdown backdoor found in Bitmain firmware in 2017.
- Pools that cannot be verified.

The post also raises the risk for an industry tied into national electric grids: what happens if a vendor is attacked, ships a critical vulnerability, or drops support.

## The vision

A miner is any device that provides issuance, settlement and record security. It could be a water heater, part of a solar and battery system, or an off-grid rig. The post's comparison: Apple does not dictate what a computer is, and miners should come in every shape too.

## Proof of work

Winning block 881423 gave the foundation its first resources. It then funded grantees who reverse engineered the whole stack and wrote down the recipes: [Ember One](../hardware/ember-one.md), [Libre Board](../hardware/libre-board.md), [Mujina](../mujina/mujina-firmware.md) and [Hydrapool](../hydrapool/hydrapool.md). Nine months after winning the block, early versions of all four ran together as one development kit.

## Breakout workshops

After the slides, attendees split into one workshop per core project, each led by its Lead Maintainer:

| Project | Lead Maintainer |
|---|---|
| Ember One | Skot |
| Libre Board | Schnitzel |
| Mujina | Ryan |
| Hydrapool | Jungly |

The sessions used direct questions, exercises and live demos on real hardware. The post's reason: getting a project into someone's hands is not the same as getting it into their head.

## What comes next

Ember One and Libre Board need their latest revisions taken through final validation. Mujina and Hydrapool remain under continuous development. The core grants program needs more funding to keep going.

The presentation closed with the programs now running:

- **Education.** Developer calls, the forum, a weekly podcast and newsletter, and in-person teaching, such as Ryan's at Bitcoin++ in Nairobi.
- **Stewardship.** A neutral home for shared projects like ASIC-rs, which the post says is now an active dependency inside a manufacturer's fleet management software.
- **Fiscal sponsorship.** For [Hashrate Heatpunks](hashrate-heatpunks.md) and Open Source Miners United, with funds earmarked for each.
- **Working groups.** To advance standards, including work on Stratum V2.
- **The 256 Red Team.** See [Red Team Program](red-team-program.md).

## The ask

The post says what the foundation needs most is fiscal support. Commoditizing an industry is long and expensive, and it wants its Core Contributors to have the stability of multi-year funding. Tyler recorded a walkthrough of the deck and posted it on X.

## See Also

- [256 Foundation: Mission and Organization](mission-and-organization.md)
- [Grants and Funding](grants-and-funding.md)
- [Events and Calendar](events-and-calendar.md)
- [Donate and Get Involved](donate-and-get-involved.md)
