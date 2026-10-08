# Telehash 4

> Sources: 256 Foundation forum (TELEHASH #4 - May 19th @ Bitcoin Park Austin), 2026-04-26; 256 Foundation forum (TELEHASH TALKING POINTS - What are you building!?), 2026-05-08; 256 Foundation forum (TELEHASH #4 Performance Metrics), 2026-05-21; 256 Foundation forum (event calendar), collected 2026-10-07; 256 Foundation (telehash page), collected 2026-10-07
> Raw: [forum: Telehash 4 announcement](../../raw/foundation/2026-04-26-forum-telehash-4-may-19th-bitcoin-park-austin.md); [forum: Telehash talking points](../../raw/foundation/2026-05-08-forum-telehash-talking-points-what-are-you-building.md); [forum: Telehash 4 performance metrics](../../raw/foundation/2026-05-21-forum-telehash-4-performance-metrics.md); [forum event calendar](../../raw/foundation/256-foundation-forum-event-calendar.md); [256foundation.org telehash](../../raw/foundation/256foundation-org-telehash.md)
> Updated: 2026-10-07

## Overview

Telehash 4 was the fourth of the 256 Foundation's hashrate fundraisers, held live at Bitcoin Park Austin on May 19, 2026, alongside TEMS 2026. No solo block was found. The community still pointed a peak of about 2.49 EH/s at the pool and contributed about 30.81 ZH of total work from 59 unique users. Afterward the foundation posted a full set of pool and dashboard metrics on its forum. This article covers that event in detail. For how Telehash works and the earlier events, see [Telehash](telehash.md).

## Announcement

The foundation announced the event on its forum on 2026-04-26 under the name "TELEHASH #4 - Live at Bitcoin Park Austin for TEMS 2026". People could join in person or online. In-person RSVPs went through the Bitcoin Park Austin meetup page, and hashrate instructions were on the Hashdash dashboard at dash.256f.org.

The forum event was scheduled from 2026-05-19 18:00 to 2026-05-20 01:00.

> **Status: Disputed**
> The forum announcement and the forum event calendar both schedule the event from 18:00 to 01:00 the next day. The foundation's telehash page describes it as a "6.5-hour event". The first is a scheduled window and the second may be the measured running time, but the sources do not say so.

## Community talking points

On 2026-05-08 the foundation opened a forum thread asking the community what it was building, so that projects could be featured on the stream. The team asked for pictures and video walk-throughs, with no deadline other than before going live.

One community member offered Proof Of Print, a printer and filament bed prototype heated by mining, and shared a project site and two videos. The team said it would cover it on stream.

## Performance metrics

The foundation posted these figures on the forum after the event.

### Hashrate and work

| Metric | Value |
|---|---|
| Total work | `3.0808e22` hashes, about 30.81 ZH |
| Average hashrate | `1.3166e18 H/s`, about 1.32 EH/s |
| Peak hashrate | `2.4946e18 H/s`, about 2.49 EH/s |
| Best share | 5,641,087,619,091 |

### Participation

| Metric | Value |
|---|---|
| Unique users | 59 |
| Unique workers seen during the event | 2231 |
| Peak users, dashboard-style | 53 |
| Peak active workers, dashboard-style | 2217 |

### Shares

| Metric | Value |
|---|---|
| Accepted shares | 20,754,816 |
| Rejected shares | 41,377 |
| Reject rate | 0.199% |

### Dashboard and infrastructure load

| Metric | Value |
|---|---|
| Total API requests | 452,062 |
| Peak API rate | 32.7 req/s |
| Overall API cache hit rate | 77.43% |
| Query/query_range cache hit rate | 78.30% |
| Peak nginx active connections | 5,625 |
| Total stream connections | 157,937 |

The telehash page adds context for the load numbers. Hashdash was stress-tested live with thousands of concurrent users, and the team made caching fixes in the first 30 minutes.

## Who contributed

The metrics post ranks all 59 users by hashes. Work was very concentrated at the top.

| Rank | User (Nostr name or pool username) | Share of total work |
|---|---|---|
| 1 | Elektron | 73.5959% |
| 2 | NiceHash | 8.9372% |
| 3 | Schnitzel | 7.2802% |
| 4 | FutureBit | 2.8661% |
| 5 | Megawatt | 2.1143% |
| 6 | Dylan | 1.6390% |
| 7 | RiglyBlockPartyTelehash | 1.1050% |

Everyone from rank 8 down contributed less than one percent each. The list mixes company names, meetups and individuals, and includes a Hashrate Heatpunks entry.

## What else happened

According to the telehash page, the event included updates on all four core projects. Representatives from major mining companies attended and shared what they most need from an open-source mining stack. The page calls it the foundation's biggest event yet.

## See Also

- [Telehash](telehash.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [Events and Calendar](events-and-calendar.md)
- [Donate and Get Involved](donate-and-get-involved.md)
