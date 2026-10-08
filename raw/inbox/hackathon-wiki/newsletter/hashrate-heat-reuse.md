# Hashrate Heat Reuse and the Heatpunk Summit

> Sources: 256 Foundation (newsletter #5, May 2025), 2025-05-05; 256 Foundation (newsletter #6, June 2025), 2025-06-19; 256 Foundation (newsletter #7, July 2025), 2025-07-15; 256 Foundation (newsletter #8, August 2025), 2025-08-18; 256 Foundation (newsletter #9, September 2025), 2025-09-25; 256 Foundation (Assembling Freedom #10), 2025-10-28; 256 Foundation (Assembling Freedom #11), 2025-11-24; 256 Foundation (Assembling Freedom #12), 2025-12-22; 256 Foundation (Assembling Freedom #14), 2026-01-30; 256 Foundation (POD256 Episode 103 newsletter), 2026-02-05; 256 Foundation (Assembling Freedom #16), 2026-02-11; 256 Foundation (Assembling Freedom #17), 2026-02-19; 256 Foundation (Assembling Freedom #18), 2026-03-04; 256 Foundation (Assembling Freedom #21), 2026-03-25; 256 Foundation (Assembling Freedom #25), 2026-04-22; 256 Foundation (Assembling Freedom #27), 2026-05-28
> Raw: [Newsletter May 2025](../../raw/newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md); [Newsletter June 2025](../../raw/newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md); [Newsletter July 2025](../../raw/newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md); [Newsletter August 2025](../../raw/newsletter/2025-08-18-is-open-source-communism.md); [Newsletter September 2025](../../raw/newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md); [Assembling Freedom #10](../../raw/newsletter/2025-10-28-assembling-freedom-10.md); [Assembling Freedom #11](../../raw/newsletter/2025-11-24-assembling-freedom-11.md); [Assembling Freedom #12](../../raw/newsletter/2025-12-22-assembling-freedom-12.md); [Assembling Freedom #14](../../raw/newsletter/2026-01-30-assembling-freedom-14.md); [POD256 Episode 103 newsletter](../../raw/newsletter/2026-02-05-unlocking-decentralized-mining-deep-dive-into-pod256-episode.md); [Assembling Freedom #16](../../raw/newsletter/2026-02-11-assembling-freedom-16-ai-open-source-bitcoin-mining-and-batt.md); [Assembling Freedom #17](../../raw/newsletter/2026-02-19-assembling-freedom-17-unpacking-pod256-episode-105-chips-cha.md); [Assembling Freedom #18](../../raw/newsletter/2026-03-04-assembling-freedom-18-high-signal-in-the-hashtub-workshops-o.md); [Assembling Freedom #21](../../raw/newsletter/2026-03-25-assembling-freedom-21.md); [Assembling Freedom #25](../../raw/newsletter/2026-04-22-assembling-freedom-25.md); [Assembling Freedom #27](../../raw/newsletter/2026-05-28-assembling-freedom-27.md)
> Updated: 2026-10-07

## Overview

A Bitcoin miner turns nearly all of its electricity into heat. Hashrate heat reuse means putting that heat to work: warming rooms, water, floors, hot tubs and even food, while the miner earns bitcoin. The topic runs through almost every newsletter issue. In 2025 it shows up as individual builds, many of them by Tyler Stevens at The Space Denver. In 2026 it becomes a movement with its own event, the Heatpunk Summit, and the foundation's own stack is shown cooking a steak. The newsletter's steady claim is that closed mining hardware holds this field back and open hardware and firmware will speed it up.

## Why the foundation cares

- **Scale of the opportunity.** Tyler Stevens gave a talk in Alaska on July 5 arguing that heat reuse could triple current network hashrate by capturing only 1% of world-wide comfort heat. The foundation's view is that closed hardware is not suited to realizing this.
- **Decentralization.** Heat gives homes and small businesses an economic reason to mine. The newsletters argue that more hashrate in homes means more censorship resistance.
- **Open tooling.** Heat builds need the miner to take orders from a thermostat or home automation system. That means documented APIs and firmware that can be changed. Ideas raised on the podcast include firmware that targets a room temperature and a fallback that hashes dummy work to keep heat flowing during a network outage.

## Builds reported in 2025

| When | Who | What |
|---|---|---|
| April 14 | Rev.Hodl | A set of homestead builds on closed hardware: sous-vide cooking, tap water heated to 150°F, a hashing space heater and a clothes dryer converted to use miners. |
| June 21 | Softwarm LLC | An install with 30 Antminer S21 miners making over 6 Ph/s, with a radiator to shed excess heat from the immersion system. |
| June 22 | The Space Denver | Start of a new heat reuse install at the venue. |
| July 8 | Rev.Hodl | Won the energy prize at the Atlanta Bitlab Mining Hackathon by using a special clay to cool air with a miner. |
| August 22 | Tyler Stevens | Upgraded the heated floor system at The Space Denver. The miner runs whenever rooftop solar can power it. When the building gets too warm, a remote-controlled pump sends the heat to an outdoor radiator. |
| September 29 | Tyler Stevens | Heating The Space Denver with an Avalon Mini 3 and an Avalon Q. Home Assistant holds 77°F (+/- 1°F). A smart thermostat calls for natural gas heat when the miners cannot keep up. |
| October | Tyler Stevens | Basement tests with immersion-cooled S19 and S21 miners tied into radiant floor heating, with separate loops and PID controls. |

Other 2025 notes:

- On October 28 Exergy updated its Home Assistant documentation for controlling Canaan Avalon Mini 3 miners through Node-RED and direct API calls.
- Schnitzel, the Libre Board lead, also runs a heat startup called Nakamoto Heating.
- A podcast in October said about a third of Canaan's revenue came from smaller home units.
- One recipient of the donated Intel chips, PizzAndy, planned a 3D printer that mines to heat its print bed. An April 2026 issue links to a Tom's Hardware interview about it.
- The December issue points to the Heat Punks forum at `heatpunks.org` as the home of the community.

## Lessons from industrial cooling (TEMS panel)

The June 2025 issue prints a transcript of a TEMS panel, "Beating The Texas Heat", with mining operator Marshall Long. It is about large sites, but much of it applies to heat reuse.

- **Pick where the pain goes.** Long's question to anyone choosing a cooling method: "Where do you want your pain and when do you want it?" Hydro costs the most up front. Air is easy to start and painful to maintain forever. Single-phase immersion sits between them and can reuse air miners.
- **Hydro helps heat reuse.** Long described a hydro setup that preheats water at a site where beer is made. Hydro units are heavy, cost more and need three-phase power.
- **Fluid chemistry matters.** Immersion fluids differ and age. Long said that around 2018 he used plain mineral oil, which broke down, became conductive and fried a batch of S9s. A good vendor should test fluid samples regularly.
- **Closed loops.** After a West Texas site failed when its water supply turned briny, vendors now sell closed systems that need no added water. Newer hydro units accept inlet water of 65 or 75 degrees Celsius.
- **Mining leads on cooling density.** Long said high-performance computing people are amazed by flow rates like 1,700 liters a minute.
- **Vendors are opening up.** Makers used to refuse SSH access. Operators responded by finding their own ways in. Long said makers have started shipping immersion-ready models and cooperating.

## The foundation's own demos

- **Sous vide miner.** At Telehash #3 the foundation ran three [Ember One](../hardware/ember-one.md) boards with custom water blocks on a [Libre Board](../hardware/libre-board.md) prototype with [Mujina](../mujina/mujina-firmware.md), mining to [Hydra Pool](../hydrapool/hydrapool.md) while the water cooked ribeyes. Issue #14 says the water reached 131°F. The Episode 103 issue describes a sous vide heater as a reference design.
- **Thermostat bridge.** In April 2026 the crew prototyped the Libre Board as a bridge between a standard 24V home thermostat and a miner. Three control styles were compared: simple on and off heat calls, gradual ramping of chip frequency, and PID loops for precise temperature targets. Frequency tuning behaves differently under Mujina, stock firmware and LuxOS.
- **Fans.** Skot's Ampminer prototype, a stock S19j Pro running Mujina, has native support for AC Infinity duct fans. Issue #25 presents them as a quieter option.

## Heatpunk Summit 2026

Issue #18 is a debrief of the summit, held Feb 27–28 at The Space in Denver's RiNo district.

- 150+ builders attended.
- Over 20 different hashrate heating systems were running live.
- The crowd mixed HVAC professionals, hydronics engineers and home miners.
- The foundation showed its full open stack.

**The Hashtub.** The centrepiece was a cedar hot tub heated entirely by miners, a joint project of Snorkel and Hashrate House. Two S19J Pro miners, about 8 kW, heat it from cold to 104 °F / 40 °C in under 4 hours. The schematics and parts list are on GitHub under NakamotoHeating/HashTub. The issue lists two heating system models. The Pleb model is 24 J/TH at 4,395 USD. The Pro model is 16 J/TH at 5,895 USD.

**Engineering lessons.**

- Mixed metals in a plumbing loop corrode quickly. The workshop consensus was to use dielectric unions, sacrificial anodes and matched materials.
- A professional hydronics engineer critiqued the venue's boiler setup on site, and the critique turned into live upgrades.
- A regulatory track covered homeowners insurance and zoning.

**Canaan.** The Avalon maker attended and hosted a builder feedback session. The issue says Canaan signalled it would support the home mining and heat reuse market with better documentation and APIs, firmware changes for lower-power home use and a direct feedback channel. The Avalon Mini 3 is described as 37.5 TH/s @ 800 W.

**Starting point.** The episode's advice is to start small: one Avalon Mini 3, Home Assistant and a plate heat exchanger. It calls Home Assistant automation "the real unlock".

## Measuring the heat

Issue #21 describes a customer dashboard built on Home Assistant and a Venstar thermostat. It shows heat delivered by miners against natural gas use, heating stage changes, outdoor temperature and sats earned.

- The issue says miners convert about 99% of electricity into heat.
- Its rule of thumb is that a 1 kW miner gives about 3,412 BTU/hr.
- It cites a Braiins engineer who heats a house with one hydro-cooled miner and reports up to 63% cash back on electricity.

## Immersion or hydro

> **Status: Disputed**
> The 2026 issues point in different directions on cooling. Issue #17 (February 2026) presents immersion cooling as a game-changer for home setups and rates hydro as high performance with leak risks, suited to industrial sites. Issue #27 (May 2026) says immersion is declining and hydro is winning, for both home rigs and industrial fleets. The Episode 103 issue (February 2026) complains that makers moving to hydro-only designs leave home miners behind.

Issue #17 also claims that fluids like mineral oil move heat far better than air, and names the costs of immersion as the initial setup and fluid management. Issue #16 mentions heat-pump and hot-tub mining experiments.

## See Also

- [Foundation Progress Timeline, 2025](foundation-progress-2025.md)
- [Foundation Progress Timeline, 2026](foundation-progress-2026.md)
- [Open Mining Ecosystem News, 2025 to 2026](open-mining-ecosystem-news.md)
- [Libre Board](../hardware/libre-board.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Telehash](../foundation/telehash.md)
