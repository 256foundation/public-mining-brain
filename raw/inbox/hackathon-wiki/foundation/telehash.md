# Telehash

> Sources: 256 Foundation (telehash page), collected 2026-10-07; 256 Foundation (our-work page), collected 2026-10-07; 256 Foundation forum (TELEHASH #4 announcement), 2026-04-26; 256 Foundation (Assembling Freedom #14), 2026-01-30
> Raw: [256foundation.org telehash](../../raw/foundation/256foundation-org-telehash.md); [256foundation.org our work](../../raw/foundation/256foundation-org-our-work.md); [Telehash 4 forum announcement](../../raw/foundation/2026-04-26-forum-telehash-4-may-19th-bitcoin-park-austin.md); [Assembling Freedom #14](../../raw/newsletter/2026-01-30-assembling-freedom-14.md)
> Updated: 2026-10-07

## Overview

Telehash is the 256 Foundation's fundraising event, held a few times a year. The team gathers in person and livestreams while miners around the world point their hashrate at the foundation's [Hydrapool](../hydrapool/hydrapool.md) instance running in solo mining mode. If a block is found during the stream, the whole block reward goes to the foundation. The first Telehash found a block and launched the organization.

## How to take part

Miners set their pool URL to `stratum+tcp://pool.256foundation.org:3333` and use any `username.workername`. A website URL, X handle or Nostr npub as the username puts a profile picture or favicon on the leaderboard.

## Past events

| Event | What happened |
|---|---|
| Telehash 1 | Over 8 hours of livestreaming. A block was found, with a 3.146 BTC block reward, raising the initial funds of about $300,000 USD that seeded the four core projects. |
| Telehash 2 | One month into development of each core project. An early Ember One hash board hashed live to an early Hydrapool instance. |
| Telehash 3 | The first time all four core projects ran together in one working system: Ember One boards driven by Libre Board, running Mujina, pointed at a self-hosted Hydrapool. The team water-cooled the rig and cooked a steak live, using Mujina to hold a temperature probe at 101°F. |
| Telehash 4 | Held at Bitcoin Park Austin on May 19, 2026. No solo block was found. The community connected a peak of 2.49 EH/s and contributed about 30.81 ZH of total work over the 6.5-hour event, with 59 unique contributors and 2,231 workers. |

> **Status: Disputed**
> The telehash page calls Telehash 4 a 6.5-hour event. The forum announcement scheduled it from 2026-05-19 18:00 to 2026-05-20 01:00, a longer window. This may be scheduled time versus actual running time; no source says so. See [Telehash 4](telehash-4.md).

> **Status: Disputed**
> The telehash page says the Telehash 3 demo held a temperature probe at exactly 101°F. Assembling Freedom #14 gives a different water temperature for the same sous vide demo. See [Foundation Progress Timeline, 2026](../newsletter/foundation-progress-2026.md).

## Telehash as a test bed

Telehash doubles as a public integration test. At Telehash 4 the Hashdash dashboard was stress-tested with thousands of concurrent users, hitting 32.7 req/s at peak, which prompted caching fixes in the first 30 minutes. Representatives from mining companies also attended and shared what they need from an open-source mining stack.

## See Also

- [Grants and Funding](grants-and-funding.md)
- [256 Foundation: Mission and Organization](mission-and-organization.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [Telehash 4](telehash-4.md)
- [Foundation Progress Timeline, 2026](../newsletter/foundation-progress-2026.md)
