# Foundation Progress Timeline, 2026

> Sources: 256 Foundation (Assembling Freedom #13), 2026-01-14; 256 Foundation (Assembling Freedom #14), 2026-01-30; 256 Foundation (POD256 Episode 103 newsletter), 2026-02-05; 256 Foundation (Assembling Freedom #16), 2026-02-11; 256 Foundation (Assembling Freedom #17), 2026-02-19; 256 Foundation (Assembling Freedom #18), 2026-03-04; 256 Foundation (Assembling Freedom #19), 2026-03-11; 256 Foundation (POD256 Episode 108 newsletter), 2026-03-18; 256 Foundation (Assembling Freedom #21), 2026-03-25; 256 Foundation (Assembling Freedom #22), 2026-04-05; 256 Foundation (Assembling Freedom #23), 2026-04-11; 256 Foundation (Assembling Freedom #24), 2026-04-15; 256 Foundation (Assembling Freedom #25), 2026-04-22; 256 Foundation (Assembling Freedom #26), 2026-05-13; 256 Foundation (Assembling Freedom #27), 2026-05-28; 256 Foundation (newsletter #9, September 2025), 2025-09-25
> Raw: [Assembling Freedom #13](../../raw/newsletter/2026-01-14-assembling-freedom-13.md); [Assembling Freedom #14](../../raw/newsletter/2026-01-30-assembling-freedom-14.md); [POD256 Episode 103 newsletter](../../raw/newsletter/2026-02-05-unlocking-decentralized-mining-deep-dive-into-pod256-episode.md); [Assembling Freedom #16](../../raw/newsletter/2026-02-11-assembling-freedom-16-ai-open-source-bitcoin-mining-and-batt.md); [Assembling Freedom #17](../../raw/newsletter/2026-02-19-assembling-freedom-17-unpacking-pod256-episode-105-chips-cha.md); [Assembling Freedom #18](../../raw/newsletter/2026-03-04-assembling-freedom-18-high-signal-in-the-hashtub-workshops-o.md); [Assembling Freedom #19](../../raw/newsletter/2026-03-11-assembling-freedom-19-revolutionizing-bitcoin-mining-hacking.md); [POD256 Episode 108 newsletter](../../raw/newsletter/2026-03-18-pod256-episode-108-breakdown-from-mixers-to-miners-why-samou.md); [Assembling Freedom #21](../../raw/newsletter/2026-03-25-assembling-freedom-21.md); [Assembling Freedom #22](../../raw/newsletter/2026-04-05-pod256-episode-110-newsletter-april-fools-real-progress-open.md); [Assembling Freedom #23](../../raw/newsletter/2026-04-11-assembling-freedom-23.md); [Assembling Freedom #24](../../raw/newsletter/2026-04-15-assembling-freedom-24-bitcoin-mining-renaissance-stratum-v2.md); [Assembling Freedom #25](../../raw/newsletter/2026-04-22-assembling-freedom-25.md); [Assembling Freedom #26](../../raw/newsletter/2026-05-13-assembling-freedom-26.md); [Assembling Freedom #27](../../raw/newsletter/2026-05-28-assembling-freedom-27.md); [Newsletter September 2025](../../raw/newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md)
> Updated: 2026-10-07

## Overview

In 2026 the Assembling Freedom newsletter became weekly. Each issue is now a written recap of one POD256 podcast episode, usually hosted by econoalchemist, Skot and Tyler Stevens. The fifteen issues from January to May 2026 follow the foundation from Telehash #3, where the whole open stack ran together, through Mujina running on stock Antminers, a second round of grants, a $100k grant from the MARA Foundation, and a record Hydra Pool stress test at Telehash #4. Read these issues with care. Several say they were generated from show notes, and issue #13 labels much of its text as extrapolation. Their tables and images did not survive into the saved text, so some figures are missing.

## How the 2026 issues differ

- Each issue covers one episode instead of one month. There is no grant-by-grant status report as in [2025](foundation-progress-2025.md).
- The style is promotional. Issue #13 sorts each topic into importance, extrapolations and implications. The extrapolations are guesses about what the episode implies, not reports of what was built.
- Two issues carry no Assembling Freedom number in their title: the Episode 103 issue and the Episode 108 issue. They sit between #14 and #16, and between #19 and #21.
- Later issues are published under the CC0 1.0 license.

## Issue by issue

| Issue | Episode | Date given in the issue | Main subject |
|---|---|---|---|
| #13 | 101 | January 14, 2026 | Hydra Pool, HashDash, TeleDash and the Telehash playbook |
| #14 | 102 | not given | Telehash #3 debrief with Mujina's lead developer |
| unnumbered | 103 | February 04, 2026 | The case against closed-source mining |
| #16 | 104 | not given | AI, open mining and surveillance |
| #17 | 105 | not given | Ember One bug fix, chip design, immersion cooling |
| #18 | 106 | March 4, 2026 | Heatpunk Summit debrief |
| #19 | 107 | not given | Mujina on stock Antminer S19 control boards |
| unnumbered | 108 | March 18, 2026 | Samourai Wallet, with guest Lauren Rodriguez |
| #21 | 109 | March 25, 2026 | Hashrate heat and home sovereignty |
| #22 | 110 | April 1, 2026 | Renewed grants, Bitaxe Bonanza |
| #23 | 111 | April 8, 2026 | Mujina progress, solo blocks, LibreBoard v3 |
| #24 | 112 | April 15, 2026 | Stratum V2 and the return of home mining |
| #25 | 113 | April 22, 2026 | Touchscreen miner, thermostats, Doom |
| #26 | 114 | May 13, 2026 | Bitcoin 2026 recap, MARA grant, Telehash #4 preview |
| #27 | 115 | not given | Hydra Pool stress test at Telehash #4 |

## January: Telehash #3 and the dashboards

Issue #13 covers [Hydra Pool](../hydrapool/hydrapool.md) and two new dashboards built with guest developer d++. HashDash shows pool metrics such as total hash rate, active workers and share distribution. TeleDash adds stream overlays and a jumbotron view for fundraisers, with block height, BTC price, donation messages, the odds of finding a block and leaderboards. The episode discussed scalability testing to handle 10,000 workers, monitored with Prometheus. The issue also says Hydra Pool can pay up to 100 addresses per block.

The issue tells readers how to join a [Telehash](../foundation/telehash.md): point miners at the foundation pool with a valid BTC address as the username and any worker name. It recalls that Telehash #1 found block 881423.

> **Status: Disputed**
> Issue #13 gives two different ports for the Telehash pool. The instructions say `pool.256foundation.org:33303`. Two paragraphs later the same issue refers to a port-specific join on 3333. The existing [Telehash](../foundation/telehash.md) article, from the foundation website, gives port 3333.

Issue #14 is the debrief of Telehash #3. It describes an eight-hour live stream held after NEMS, the North East Mining Summit. The centrepiece was a sous vide miner: three [Ember One](../hardware/ember-one.md) hash boards with custom water blocks, run by a [Libre Board](../hardware/libre-board.md) prototype on [Mujina](../mujina/mujina-firmware.md), pointed at Hydra Pool and mining on mainnet while the water cooked ribeyes. The issue says the water reached 131°F.

> **Status: Disputed**
> Issue #14 says the water temperature hit 131°F. The existing [Telehash](../foundation/telehash.md) article, from the foundation website, says Mujina held a temperature probe at 101°F. The two may describe different measurements. Neither source explains the gap.

The same issue reports interest from ASIC makers at NEMS, lays out a Mujina roadmap (REST APIs, multipool failover and power targets), and mentions HashScope, a tool for checking shares. It says the foundation has allocated $400k+ in grants. Issue #13 puts the figure at $400k, and issue #22 says over $400k in prior grants.

## February: the case for the open stack

- **Episode 103.** The argument is that closed firmware and hardware block innovation, safety certification and planning. Makers are moving to hydro-only designs and three-phase power and dropping 240V options, which leaves home and small business miners behind. The issue praises Tether for open-sourcing its MOS fleet platform. It describes pointing hashrate at the foundation's Hydra Pool as a donation. Skot and Joe Nakamoto called in from the Plan B conference in El Salvador.
- **Issue #16.** Recorded at Bitcoin Park in Nashville. It says the largest difficulty drop since the 2021 China ban made home mining viable again. It also says competitive open-source ASICs are still out of reach and that FPGAs are useful for learning. The hosts warn about data leaks from closed AI models and recommend local agents.
- **Issue #17.** Ryan, the Mujina developer, found a voltage domain bug in the Ember One. It was fixed at the desk, and the board then ran at about 2 TH/s against a target of 3.6 TH/s with proper cooling. The issue also mentions solo-block wins on the foundation's Hydra Pool and preparation for the Heat Punk Summit.

> **Status: Disputed**
> The newsletters describe the Ember One differently. The September 2025 issue says it is built around Bitmain BM1362AC chips and makes roughly 3.5Th/s. Issue #17 calls it a rig with Intel boards and 12 chips targeting 3.6 TH/s. Issue #23 says Ember One hash boards are about 100W and 2-4 TH/s per board. Issue #14 says the design is based on the BM1362AC with Intel BZM2 support to come.

## March: Mujina on stock Antminers

- **Heatpunk Summit.** Issue #18 is a debrief of Heatpunk Summit 2026, held Feb 27–28 at The Space in Denver. The foundation showed its full stack there. Details are in [Hashrate Heat Reuse and the Heatpunk Summit](hashrate-heat-reuse.md).
- **Issue #19.** Mujina was flashed onto stock Bitmain Antminer S19 control boards over Ethernet or USB using LuxOS, with no SD card. Drivers were added for temperature sensors, fans and the undocumented APW12 power supply. The result removes developer fees and allows single-board operation and immersion setups without fan spoofers. The issue warns that poor fan control can overheat boards and trip breakers. Skot is quoted: "I essentially vibe coded S19j Pro support into Mujina firmware in a few hours." HashScope is described here as a Stratum MITM proxy for debugging traffic between miner and pool.
- **Episode 108.** A live episode from Denver on the Samourai Wallet prison sentences. See [Samourai Wallet Case and Developer Liability](samourai-wallet-case.md).
- **Issue #21.** Tyler and Eco demo a customer dashboard for heat reuse. The issue describes the 256 Foundation as a 501(c)3.

## April: second grant round

Issue #22 reports renewed grants for the four projects: Mujina, Libre Board, Ember One and Hydra Pool. It says the foundation runs an all-Bitcoin treasury experiment and pays developers in sats pegged to cost basis. It quotes a foundation post dated Apr 2, 2026: "Funding for our second round of grants begins today." The quoted part of that post names Mujina, Hydra Pool and Libre Board. The quote is abridged, so it does not show whether Ember One was listed. See [Grants and Funding](../foundation/grants-and-funding.md).

Other points from April:

- **Mujina.** Work was under way to unlock Bitmain control boards and port Mujina to Amlogic-based Antminers. A community fork got Mujina running on the Braiins BCB100 control board, which widens support for Antminer S19 models. Issue #23 lists PWM frequency changes for fan control, a workaround for missing RPM data, and a universal Bitmain-chip driver as the April goal.
- **Hydra Pool.** The April roadmap adds difficulty and hashrate hints in the password field and better logging. Issue #22 lists a plugin architecture, a gamified dashboard and Lightning payouts as roadmap items.
- **LibreBoard v3.** Power delivery upgrades for Ember One hash boards. Issue #23 also mentions Ember One v6.1 reliability.
- **Bitaxe Bonanza.** Skot showed a prototype built around the donated Intel BZM2 chips, targeting about 1.2 TH/s per unit. The issue notes that early designs had scaling problems.
- **Ampminer.** Issue #25 describes Skot's first working prototype: a stock S19j Pro running Mujina with a touchscreen from the Bitaxe GT Touch, Wi-Fi through a hidden USB port, and native support for AC Infinity duct fans.
- **LibreDOOMAxe.** Schnitzel ran Doom on a Libre Board paired with a Bitaxe hash board through bitaxe-raw. The Libre Board article has more on [DOOMAXE](../hardware/libre-board.md).
- **Thermostats.** The crew prototyped the Libre Board as a bridge between standard 24V home thermostats and miners.
- **Recognition.** OpenSats published an Open Hardware Impact Report that highlights Bitaxe and the 256 Foundation.

> **Status: Disputed**
> The newsletters disagree on Mujina's pool protocol. The September 2025 issue says the pool client is stratum v1 only for now. Issue #19 lists Stratum V1 support. Issue #22 calls Mujina Stratum V2 native. Issue #14 mentions contributors adding Stratum v2 patches. The [Mujina Firmware](../mujina/mujina-firmware.md) article tracks a similar disputed feature list.

## May: Las Vegas and Telehash #4

Issue #26 recaps the Bitcoin 2026 conference in Las Vegas.

- **MARA Foundation grant.** The 256 Foundation won the MARA Foundation's inaugural community-vote grant of $100k. The money extends the runway for the four core projects plus documentation, storytelling and community work.
- **DoomAxe.** Schnitzel's battery-powered portable miner that also plays Doom drew attention on the floor. It ran Mujina, hashed to Hydra Pool and was hooked into Proto Fleet on the spot.
- **Open hardware debate.** The hosts' position: ASIC chips may stay closed at the silicon level, but open design of everything around them is what counts.
- **Side event.** A Mario Kart tournament filled a 3,000,000-sat prize pot.
- **Foundation updates.** A revamped website, a self-hosted Discourse forum at `forum.256foundation.org`, and regular Mujina developer calls.
- **Telehash #4 preview.** Set for May 19 at Bitcoin Park in Austin. New for this event: hashrate donations through HashDash at `dash.256f.org`, a Block Party event for pre-buying solo hash, and a loyalty leaderboard that tracks total hashes contributed, credited to d++ and jungly.

Issue #27 reports on the event itself as a Hydra Pool stress test.

- The live test ran for 6.5-hour.
- Rejected shares stayed under 2%.
- The server held more than 2,000 simultaneous connections at about 1% CPU.
- Miners of very different sizes shared one pool. Stratum suggest-difficulty and two password parameters, `d=` for starting difficulty and `h=` for a hashrate hint, set each miner's difficulty automatically.
- The issue gives a sense of scale: 1 EH/s is about 1.4 million Bitaxe Supra units.
- Looking ahead, it mentions Telehash #5, more gamification, and a call for ASIC makers and large miners to adopt open standards.

The stress test table in issue #27 was lost when the text was saved. The [Telehash](../foundation/telehash.md) article has the event's headline figures from the foundation website.

## See Also

- [Foundation Progress Timeline, 2025](foundation-progress-2025.md)
- [Hashrate Heat Reuse and the Heatpunk Summit](hashrate-heat-reuse.md)
- [Samourai Wallet Case and Developer Liability](samourai-wallet-case.md)
- [Open Mining Ecosystem News, 2025 to 2026](open-mining-ecosystem-news.md)
- [Telehash](../foundation/telehash.md)
- [Grants and Funding](../foundation/grants-and-funding.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [Libre Board](../hardware/libre-board.md)
- [Ember One](../hardware/ember-one.md)
