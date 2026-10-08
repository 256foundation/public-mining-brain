# Open Mining Voices on X

> Sources: jungly (@jungly) on X, 2026-01-24 to 2026-09-29; WantClue (@wantclue) on X, 2026-08-25 to 2026-10-03; mixed accounts on X (notable open-source mining posts, including @Schnitzel), 2025-06-05 to 2026-10-06; all collected 2026-10-07
> Raw: [X archive: notable @jungly posts](../../raw/inbox/2026-10-07-x-notable-jungly-hydrapool.md); [X archive: notable @wantclue posts](../../raw/inbox/2026-10-07-x-notable-wantclue.md); [X archive: notable open-source mining posts](../../raw/inbox/2026-10-07-x-notable-open-source-mining.md)
> Updated: 2026-10-07

## Overview

Several people who build the open mining stack post about it on X. This article covers three of them: jungly on Hydrapool, WantClue on Bitaxe firmware, and Michael Schmid on the 256 Red Team. Each section reports what that person posted, with dates. The archives are keyword samples, not full timelines. Skot, OSMU and Public Pool have their own articles, linked at the end.

## jungly on Hydrapool

jungly (Kulpreet Singh) leads Hydrapool and P2Poolv2 and is a 256 Foundation grant recipient. See [Hydrapool](../hydrapool/hydrapool.md).

**First outing, 2026-01-24.** In a short thread jungly said Hydrapool had its first outing over the previous few days. It reached `1.4EH/s` and handled 1500 peak worker connections. The thread listed features:

- Built in Rust, with test coverage that makes it easy to extend and maintain.
- Support for Solo and PPLNS accounting, and an invitation to try a novel accounting or payout method on it.
- A web endpoint to fetch all user shares, so anyone can audit the pool.

**Telehash, 2026-05-20.** jungly said the team ran Hydrapool the day before for the 256 Foundation's Telehash. Internally Hydrapool uses P2Poolv2's stratum and accounting libraries. jungly called it rock solid, shared performance on an AMD EPYC 9R45 AWS EC2 instance as an image, and said a P2Poolv2 release was coming soon. See [Telehash 4](../foundation/telehash-4.md).

**Other posts.**

- 2026-01-24: pointed followers to Ryan Kuester's work on Mujina. See [Mujina Firmware](../mujina/mujina-firmware.md).
- 2026-02-03: agreed that centralised services are a pain, and wished Bitcoin's mascot were a hydra instead of a honeybadger.
- 2026-02-17: congratulated another pool project and asked whether it pays out from the coinbase and uses a linear chain, staying true to the original p2pool design.
- 2026-05-22: thanked people running Hydrapool instances in the wild.
- 2026-08-10: noted that in the original p2pool, miners built their own blocks using their own node.

## WantClue on Bitaxe firmware

WantClue works on ESP-Miner, the Bitaxe firmware. See [AxeOS / ESP-Miner Firmware](axeos-esp-miner-firmware.md).

- **2026-08-25.** Shared a short video as a Bitaxe teaser.
- **2026-09-25.** Said ESP-Miner 2.15.3 had landed, bringing the Bitaxe Naja Duo and the Bitaxe Gamma Hex to the family, plus fixes.
- **2026-09-27.** Said the web flasher had been reworked so it is easier to pick the right device, because many devices had been added.
- **2026-10-03.** Reported from the opening of an exhibition on money at the Münzkabinett in Dresden. WantClue said it features a Bitaxe Hex, a BitForge Nano, a NerdNOS and an original QAxe. See [PiAxe, QAxe and BitForge Nano](other-open-miners.md).

**A claim about a competitor, 2026-09-18.** WantClue quoted a post from @altair_tech. As archived, the quoted text says the Bitaxe Naja Duo and the HammerMiner Thor P2 run the same chips, and that the Naja Duo draws 43% more power at the wall than advertised. WantClue's own comment treated the test as proof that open source wins, said there are "some liars around", and called the Naja Duo the most capable open source miner yet. The quoted text and WantClue's reading of it do not obviously match. The attached image is not described in the archive, so this wiki cannot say which device the power figure belongs to.

## Michael Schmid on the 256 Red Team

On 2026-08-12 Michael Schmid (@Schnitzel) introduced the 256 Red Team in a thread. The first post had 314 likes at collection. The points below are the thread's claims. Background is in [Red Team Program](../foundation/red-team-program.md).

- **Why.** The thread says about 90% of ASICs run one vendor's closed-source firmware and almost nobody has audited it. It cites Antbleed (2017), a remote kill switch in Antminer firmware that a user found by reading strings.
- **Rules.** Hardware the team owns, an isolated lab, coordinated disclosure.
- **What was tested.** Stock Bitmain S19j Pro and S21 units; third-party firmware LuxOS, VNISH and Braiins OS; and open baselines Mujina and AxeOS/Bitaxe. Methods were static reverse engineering, live traffic capture, and share-level reconciliation.
- **Findings count.** 41 findings filed, each with evidence and a way to reproduce it. The thread lists common hygiene bugs, stock firmware included: unauthenticated factory APIs, local paths to root, fleet-default credentials, vendor SSH keys baked into images, and updates that do not verify what they install.
- **Stock Bitmain.** The thread says a full decompile of both miner daemons, plus live connection tables, found no hashrate skimming, no kill switches and no covert beacons.
- **Third-party firmware.** The thread says behavior an owner cannot see from the dashboard is concentrated there, not in stock. It gives no specifics.
- **Disclosures.** Three were submitted, to VNISH, Luxor and Braiins. Each was reported privately, with 30 days to respond before the Red Team publishes.
- **Advice to operators.** Firewall ports 6060 / 4028 / 1534, rotate default credentials, and isolate miner VLANs.
- **Next.** MicroBT Whatsminer, Canaan Avalon, and newer makers Auradine, Bitdeer (SEALMINER) and ePIC.

Follow-ups:

- 2026-08-12: a Canaan Avalon Mini 3 was donated to the team. See [Canaan Mujina Port](canaan-mujina-port.md).
- 2026-08-13: Schmid said the team found no major flaws in Mujina, only a couple of small improvements. Schmid added that there were no flashable OS images for Mujina on S19 yet and the team was working on it.
- 2026-08-17: Schmid showed the team's control-board cage, with miner control boards on a bench wired into an isolated lab network.

The thread's statements about third-party firmware are the Red Team's claims at the time of posting. The archive contains no vendor response and no published findings.

## Limits of the archive

The jungly file holds 10 posts and says it misses the 2025 grant-period posts and most P2Poolv2 engineering threads. The WantClue file holds 5 posts, all from 2026. The mixed file holds 24 posts chosen for reach. Engagement counts are as of collection.

## See Also

- [Skot on Bitaxe and Copyleft](skot-on-bitaxe-and-copyleft.md)
- [OSMU on X](osmu-on-x.md)
- [Public Pool on X](public-pool-on-x.md)
- [Canaan Mujina Port](canaan-mujina-port.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [Red Team Program](../foundation/red-team-program.md)
- [Multi-Chip Bitaxe Designs](multi-chip-bitaxe-designs.md)
