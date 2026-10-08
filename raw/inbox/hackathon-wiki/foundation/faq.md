# 256 Foundation FAQ

> Sources: 256 Foundation (FAQ page), collected 2026-10-07
> Raw: [256foundation.org FAQ](../../raw/foundation/256foundation-org-faq.md)
> Updated: 2026-10-07

## Overview

The foundation's own FAQ page answers the questions it gets most: what it does, how to donate, how grants work, how the four core projects fit together, and why open-source mining matters. This article distills those answers. The foundation asks people with other questions to email contact@256foundation.org or post on the community forum.

## About the foundation

- **What it is.** A 501(c)(3) public charity (EIN: 99-1662333) that funds free and open-source Bitcoin mining work and provides education on Bitcoin and freedom tech.
- **Who founded it.** @bitkite and @econoalchemist, in February 2024.
- **What it sees as the problem.** Three kinds of centralization:
  - Hardware and firmware: one Chinese company with ~90% market dominance.
  - Pools: ~90% of global hashrate controlled by four pool operators and their proxies.
  - Rewards: ~40% of mining rewards going to a single custodian.
- **What a donation funds.** Core contributors building Mujina, Libre Board, Hydrapool and Ember One. No board member is compensated.
- **Best way to reach it.** Email.

## Donations

- **Tax status.** Donations are tax-deductible as allowed by law. No products or services are exchanged for a donation. The FAQ suggests asking a tax professional about your own case.
- **Two ways to give.** Money (Bitcoin on-chain, Lightning, or credit/debit card through the Zaprite donation page) or hashrate.
- **Payment methods.** Bitcoin and cards only. No other cryptocurrencies.
- **Hashrate donation.** Point a miner at the foundation's Hydrapool instance at `pool.256foundation.org:3333`. If a block is found, the whole block reward goes to the foundation. Contributions show up live on Hashdash.
- **TeleHash.** The occasional in-person, livestreamed event where the pool runs in solo mode and the community points hashrate at it.

Details on each route are in [Donate and Get Involved](donate-and-get-involved.md).

## Grants

- **How funds are prioritized.** The four core projects come first. When there is funding beyond those commitments, the board opens the General Grant Program for community-submitted projects.
- **Selection.** Applicants go through an evaluation and interview process and are awarded fair-market value for their work.
- **Bitcoin or fiat.** The recipient chooses. Exact amounts paid to individuals are kept confidential for security reasons. Annual tax disclosures are available for public inspection, as the IRS requires.
- **Grants for nyms.** The foundation respects pseudonymous work but must collect taxpayer information from grantees. Its suggested workaround is for the grantee to form a Wyoming LLC and share that entity's details instead of personal ones.
- **Who can apply.** Any developer, hardware engineer or researcher working on open-source Bitcoin mining. All funded work must use a recognized open-source license: OSI for software, OSHWA for hardware.
- **Core versus General.** In the Core Projects Program the foundation scopes the work and picks developers. In the General Grant Program the applicant scopes it.
- **Application contents.** Project description, technical approach, requested funding, timeline, milestone plan, and links to prior work.

The programs are covered in more depth in [Grants and Funding](grants-and-funding.md).

## Projects and ecosystem

The four core projects are layers of one stack:

| Project | Layer |
|---|---|
| [Ember One](../hardware/ember-one.md) | Hash board, the compute layer |
| [Libre Board](../hardware/libre-board.md) | Control board that connects the hash board to the network |
| [Mujina](../mujina/mujina-firmware.md) | Firmware that runs on Libre Board and manages the mining operation |
| [Hydrapool](../hydrapool/hydrapool.md) | The pool the miner connects to |

Any combination can be used on its own. Together they make a fully open-source mining system.

The FAQ also describes two communities in the foundation's ecosystem:

- **Open Source Miners United (OSMU).** Developers and builders behind projects like Bitaxe, NerdAxe and AxeOS. See [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md).
- **Hashrate Heatpunks.** A community built on the idea that mining heat is a product, not a problem. See [Hashrate Heatpunks](hashrate-heatpunks.md).

## Technical

- **Open-source hardware.** The foundation follows the Open Source Hardware Association definition. All design files (schematics, PCB layouts, BOMs, firmware) must be public under a license that allows study, modification, distribution and manufacture.
- **Why it matters.** Bitcoin's security depends on decentralized mining. A single proprietary vendor can block miners from certain pools, enforce software updates, or deny competitors access to hardware. Open-source mining removes those single points of control.

## See Also

- [256 Foundation: Mission and Organization](mission-and-organization.md)
- [Grants and Funding](grants-and-funding.md)
- [Donate and Get Involved](donate-and-get-involved.md)
- [Nonprofit Record and Legal Status](nonprofit-record.md)
