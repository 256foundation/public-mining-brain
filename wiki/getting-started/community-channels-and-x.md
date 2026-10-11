# Community Channels & X Presence

> Sources: Telegram Bot API read of the public groups @the256foundation and @heatpunks, collected 2026-10-07; Primal cache read of the 256 Foundation Nostr profile, collected 2026-10-07; forum.heatpunks.org about.json and latest.json, collected 2026-10-07; forum.256foundation.org welcome topic, collected 2026-10-07; 256foundation.org community page, collected 2026-10-07; X keyword-search archives for @osmu_global (2024-03-29 → 2026-09-27), @heatpunks (2026-06-01 → 2026-07-22), notable @Public_Pool_BTC posts (2025-10-25 → 2026-05-06), mixed open-source-mining accounts (2025-06-05 → 2026-10-06), and the batch method note — all collected 2026-10-07; heatpunks forum census and 81-topic capture backfill (forum.heatpunks.org), collected 2026-10-10; Hashrate Heatpunks Telegram signal digest (forum URL move), collected 2026-10-09
> Raw: [Telegram public groups](../../raw/hardware/bitaxe-osmu/2026-10-07-telegram-public-groups.md); [Nostr profile npub1p0d256](../../raw/history/256f-org/2026-10-07-nostr-256foundation-profile.md); [forum.heatpunks.org latest](../../raw/history/256f-org/2026-10-07-forum-heatpunks-latest.md); [256F forum welcome topic](../../raw/history/256f-org/2026-03-18-forum-welcome-to-the-256-foundation-wave.md); [256foundation.org community page](../../raw/history/256f-org/256foundation-org-community.md); [X archive: @osmu_global](../../raw/history/256f-research/2026-10-07-x-osmu-global.md); [X archive: @osmu_global 2024 remainder](../../raw/history/256f-research/2026-10-07-x-osmu-global-2024.md); [X archive: @osmu_global 2024 Q1 remainder](../../raw/history/256f-research/2026-10-07-x-osmu-global-2024-q1.md); [X archive: @heatpunks](../../raw/history/256f-research/2026-10-07-x-heatpunks.md); [X archive: notable @Public_Pool_BTC posts](../../raw/history/256f-research/2026-10-07-x-notable-public-pool.md); [X archive: notable open-source mining posts](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md); [X archive method, batch 1](../../raw/history/256f-research/2026-10-07-x-archive-method.md); [Heatpunks forum census 2026-10-10](../../raw/history/heatpunks-forum/2026-10-10-forum-heatpunks-census.md); [Heatpunks forum capture report](../../raw/history/heatpunks-forum/_CAPTURE-REPORT.md); [Heatpunks Telegram signal digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

The open-source mining community gathers in a small set of public surfaces: two Telegram supergroups run by the 256 Foundation and Hashrate Heatpunks, two Discourse forums (forum.heatpunks.org and forum.256foundation.org), a Nostr profile for the 256 Foundation, an OSMU Discord, and a set of X accounts (@256FOUNDATION, @osmu_global, @heatpunks, @Public_Pool_BTC, plus project-adjacent voices). The Foundation's own community page describes its setup as "Six doors, one community", with Open Source Miners United and the Hashrate Heatpunks as sub-communities it hosts and funds. Every number on this page is a point-in-time measurement taken on 2026-10-07 by bot reads and public API endpoints archived under raw/ — with the forum.heatpunks.org figures refreshed on 2026-10-10 by a capture-loop census that also backfilled 81 full topic captures. The captures contain no chat message text for Telegram or Nostr, so this page records sizes, dates and activity patterns — not what anyone said.

## Channels at a glance

| Channel | Surface | Run by | Measured signal |
|---------|---------|--------|-----------------|
| @the256foundation | Telegram supergroup | 256 Foundation | 211 members, 24 online (2026-10-07); 208 on 2026-09-05 |
| @heatpunks | Telegram supergroup | Hashrate Heatpunks | 175 members, 21 online (2026-10-07); 171 on 2026-09-05 |
| OSMU Discord | Discord | Open Source Miners United | "surpassed the 5K Member milestone" per post of 2024-12-14 |
| forum.heatpunks.org | Discourse | Hashrate Heatpunks | 119 topics, 682 posts, 138 users, 624 likes; 101 topics publicly listed (2026-10-10 census). Earlier read: 137 users, 118 topics, 678 posts (2026-10-07) |
| forum.256foundation.org | Discourse | 256 Foundation | welcome topic stamped 2026-03-18 in the capture |
| 256 FOUNDATION | Nostr | 256 Foundation | 223 followers, 46 notes (2026-10-07) |
| @osmu_global | X | Open Source Miners United | joined 2024-03-05; ~72–102 posts lifetime per public indexes |
| @heatpunks | X | Hashrate Heatpunks | created ~Mar 2025; 321 followers at collection |
| @Public_Pool_BTC | X | Public Pool | archived posts 2025-10-25 → 2026-05-06 |

## Telegram groups

Both groups were read on 2026-10-07 through the Telegram Bot API (getChat, getChatMemberCount, getChatAdministrators) plus the public web previews at t.me/s/the256foundation and t.me/s/heatpunks.

### @the256foundation — 256 FOUNDATION

- Type: supergroup. Title: 256 FOUNDATION.
- Description, from getChat: "Public group chat for the 256 Foundation. Our mission is simple: build the open-source Bitcoin mining ecosystem. If that stokes your 🔥 then get in here."
- Member count on 2026-10-07: 211. The web preview showed the same 211 members with 24 online at that moment.
- An earlier bot read on 2026-09-05 recorded 208 members.
- Administrators: creator econoalchemist (username econoalchemist); administrators Tyler (username tylerkstevens) and Rod (username rodbitkite).

### @heatpunks — Hashrate Heatpunks

- Type: supergroup. Title: Hashrate Heatpunks.
- Description, from getChat, calls it "The official Hashrate Heatpunk group chat", a community of builders working on the emerging hashrate heating industry whose mission is to "Marry the bitcoin mining and heating sectors to bring hashrate back home"; it points to heatpunks.org for HRHP resources and the forum.
- Member count on 2026-10-07: 175, with 21 online on the web preview at that moment.
- An earlier bot read on 2026-09-05 recorded 171 members.
- Administrators: creator Tyler (username tylerkstevens); administrators Dylan (username tronsington) and Cody (username codyharris86).

### What the Telegram read can and cannot show

The reading bot, foundation_community_bot, was added after the groups already existed. It sees only messages sent after it joined that are still in its update queue; this pull found a webhook not set, 0 pending updates, and getUpdates returning ok with 0 updates. An earlier Hydrapool community scan on 2026-09-17 hit the same empty getUpdates. The source is explicit that the empty queue is not evidence that the groups are quiet. Because these are groups rather than broadcast channels, the t.me/s web previews show title, description and counts but no message history. No posts were sent to either group, and no message text, dates or reply threads were captured.

## X accounts

The X archives were built by keyword search (`from:<handle>` plus date windows and `max_id` paging), with a "Limit 10 hits per query". The method note calls them inbox dumps for later wiki compile, "not an official X data download", and records that a complete dump needs the account's own X archive export. Coverage is self-declared incomplete in every file; engagement counts are as of collection on 2026-10-07. The method note lists @256FOUNDATION as the primary archive account, alongside @heatpunks and @osmu_global, with @Schnitzel, @skot9000, @Public_Pool_BTC and @tylerkstevens as notable adjacent accounts.

### @osmu_global — Open Source Miners United

- Account: @osmu_global, joined 2024-03-05, linking osmu.xyz and the OSMU Discord. The archive notes "Public indexes have listed ~72–102 posts lifetime; this file is a paged sample, not a complete dump."
- Three archive slices hold 9, 18 and 39 posts, together spanning 2024-03-29 → 2026-09-27. The files self-declare the gaps: most of 2024 Mar–Sep, sparse May–Jul 2024, much of 2025 Jan–May and Sep, and 2026 Jan–Mar. Searches for 5–28 Mar 2024 returned no hits besides a 2024-03-29 reply.
- The archive's own summary of where the community lives: "Discord is the primary OSMU surface; X is secondary."
- On 2024-12-14 the account announced "We have surpassed the 5K Member milestone on our Discord 😍🚀", linking discord.com/invite/osmu (likes=25, views=2464).
- On 2026-05-09 it opened a channel question: Discord connects people and shares knowledge but "it's leaving out everyone else", and asked followers about Discourse. A reply the same day: "Alongside and maybe replace in the future. Discord itself alone might be gatekeeping". No decision appears in the archive.
- Firmware release posts are a recurring beat: esp-miner v2.3.0 on 2024-10-17 (likes=49, views=3202), the ESP-Miner v2.15.1 release link on 2026-08-29, and on 2026-09-27 "Have you checked out ESP-Miner v2.15.3 yet? Tell us what you think" (likes=1, views=167).
- The account relays solo blocks found via Public Pool: 2025-10-23 (self-hosted on Umbrel), 2025-12-22 (another Umbrel block), 2026-04-03 (first block on the hosted instance, which it also called the first known block of a NerdOctAxe), and 2026-07-10 ("Aaand another one!").
- Tooling and ecosystem posts: welcoming the BitForge Nano to the web flasher on 2026-03-24, and on 2026-07-12 saying goodbye to @prime_ng, which had "transitioned from an open-source model to a commercial licensing structure", with a move to @tailwindcss.
- On 2024-08-11 it announced that most repositories would move to a new GitHub organization, bitaxeorg, within days or weeks. On 2024-08-26 it warned followers about impersonation and fishy links.
- The license stance recurs: "Open Source is the only option." (2026-06-28) and "Don’t get fooled. OSMU is copyleft not copyright." (2025-06-10). The 2025-06-25 buyer-beware reminder about proprietary devices using the Bitaxe name is the highest-engagement post in the main slice (likes=51, views=3181); the highest in the 2024 slices is a 2024-09-04 photo post at likes=148, views=6662.

### @heatpunks — Hashrate Heatpunks

- Bio: "A community working on the emerging hashrate heating industry. Affiliated @256Foundation." Created ~Mar 2025; 321 followers at collection.
- An account-wide `from:heatpunks` search returned only five posts, all from 2026 (2026-06-01 → 2026-07-22); a 2025 date window returned none. The archive concludes the account "appears to mostly relay forum.heatpunks.org threads".
- Four of the five posts carry forum thread links: the Fornax Heater thread (2026-06-01), a dark mode display problem (2026-07-08), the Science Direct research paper (2026-07-21), and the 2027 Heatpunk Summit waitlist (2026-07-22). The fifth, also 2026-07-22, quotes @tylerkstevens with "Waitlist now open!".
- The summit narrative lives on @tylerkstevens, whose 2026-07-22 post announcing the third Heatpunk Summit (Feb 26-27 in Denver, CO) drew likes=52, views=7520 at collection.

### @Public_Pool_BTC — Public Pool

- Two archive slices cover the account: a six-post file spanning 2025-10-25 → 2026-05-06, and four further posts inside the mixed open-source-mining archive. The file is self-declared "Not a full Public Pool timeline."
- The highest-reach post in the project-account archives announced "Block #2 on hosted Public-Pool. By a lone Bitaxe." on 2026-07-10 (likes=420, views=59319).
- On 2026-06-05 the account made a two-part operations announcement: with Stratum V2 support shipped in Bitaxe/ESP-Miner v2.14.0, the hosted pool at web.public-pool.io now supports Stratum V2; and several months of improvements merged into the main sqlite branch were pushed to the Umbrel and Start9 app stores, pending approval (likes=171, views=18136).
- Solo-mining near misses are a recurring post type: a 20T difficulty share on 2025-11-07, a target difficulty of ~120T announced 2026-02-03, and on 2026-04-04 a 59T share from a NerdOCTAXE 90 minutes after the hosted-instance block, put at 43% of the network difficulty.
- The 2026-04-03 hosted-instance block — the account's own count has it as #5 overall — reached likes=166, views=8274; the 2025-10-25 block-winner follow-up (a nerdquaxe++rev6 the operator assembled) reached likes=381, views=21574.

### Voices around the projects

The mixed archive holds 24 posts from @Schnitzel, @skot9000, @Public_Pool_BTC, @tylerkstevens and @wantclue, spanning 2025-06-05 → 2026-10-06, selected for reach rather than completeness. Its two largest posts are Michael Schmid's 2026-08-12 introduction of the 256 Red Team (likes=314, views=64950) and skot's 2025-06-05 "Bitaxe in every home" post (likes=274, views=28005). The archive lists its own gaps, including the full @skot9000 and @wantclue timelines.

The Foundation's own account, @256FOUNDATION, is the primary account in the same archive batch; its dated slices (2023 → 2026) live alongside these files in raw/history/256f-research/ and are compiled in [256F Community Timeline](../history/256f-community-timeline.md). The method note repeats that Grok-based pulls cannot produce a full timeline for the account and that a complete dump needs the account's X archive export.

## Nostr

The 256 Foundation's Nostr profile is npub1p0d256yljvn3pl82gpkmdyfqlxcmu6px63msrpmuauzha8yq4eeqprfpqe. Its kind 0 event names it "256 FOUNDATION", lists 256foundation.org as the website, and carries the bio "501(c)(3) public charity on a mission to dismantle the proprietary mining empire." The profile event was created 2025-11-28; the account's recorded join time is 2024-06-04T16:32:33Z.

Primal cache counts on 2026-10-07:

- follows 6, followers 223
- notes 46, replies 0, long-form notes 0
- relays 9
- total zap count 19, total sats zapped 306183
- media count 36

The pull did not copy the text of the 46 notes: a Primal feed query and a mega_feed_directive query returned no kind-1 events authored by the pubkey. The capture warns against treating the missing note text as the account being silent — the count says the notes exist. The Foundation's forum welcome topic lists Nostr among the places to follow it, next to X and the newsletter.

## Discourse forums

### forum.heatpunks.org

The forum's site record gives the title Hashrate Heatpunks, the description "Official Forum of the HRHP", the extended description "A community platform for sharing information, education and furthering development of the hashrate heating industry.", contact admin@heatpunks.org, and a creation time of 2025-03-31T21:51:34.836Z.

Stats from about.json on 2026-10-07:

- users 137, topics 118, posts 678, likes 624
- active users: 2 last day, 4 last 7 days, 7 last 30 days
- topics: 0 last day, 0 last 7 days, 1 last 30 days
- posts: 0 last day, 2 last 7 days, 6 last 30 days

A capture-loop census on 2026-10-10 recounted the site whole: 119 topics, 682 posts, 138 users and 624 likes, running Discourse 2026.8.0-latest.1, of which 101 topics are publicly listed via latest.json — the difference from the 119 site-wide count is staff-only/unlisted/system topics not visible anonymously. The same backfill captured 81 topics in full (every post, including a second posts.json fetch for topic 55's posts 18-24), and the census's public table runs from topic 5, 'Welcome to Hashrate Heatpunks!' (2025-03-31), to topic 291 (2026-10-10). Public topic counts by category: General 30, Control 15, Hydronics/Radiant & Water Heating 16, Forced Air/HVAC 6, Firmware & Software 4, Contractors & Tradesmen 3, Mining Pools 5, Target Markets 1, Products & Custom Systems 10, Businesses & Economics 8, ASIC Miners 1, Regulatory & Certifications 2. The forum has been live since the site record's 2025-03-31 creation; per the Heatpunks Telegram signal digest, its topic links moved to forum.heatpunks.org URLs by late January 2026 — the first digest mirror on the new domain is stamped 2026-01-30.

The latest.json pull is the first page only, not every topic. The newest topic on the page was created 2026-09-12; by the 2026-10-10 census the newest publicly listed topic was 291, 'UK numbers: running a small hashrate heater on the Ofgem price cap vs Economy 7 (free calculator)', created 2026-10-10. A sample of the page, with exact titles and post counts:

- 2026-09-12 — "PizzAxe - Bitcoin mining pizza bag warmer by PizzAndy" (1 post)
- 2026-09-01 — "Updated event information for recurring HA office hours" (1 post)
- 2026-07-22 — "2027 Heatpunk Summit Waitlist Open!" (1 post)
- 2026-07-21 — "Scientific Research Paper on Hashrate Heating Featured in Science Direct" (1 post)
- 2026-06-01 — "Introducing the Fornax Heater (DIY heater/miner with spouse-approved aesthetics!)" (11 posts)
- 2025-11-25 — a "Limp Mode" idea thread (10 posts, last posted 2026-07-02)

Long-running threads stay alive for months: the limp-mode thread ran from 2025-11-25 to 2026-07-02, and a rural-Colorado propane-replacement thread from 2025-04-23 shows a last post of 2026-03-06 on the same page.

### forum.256foundation.org

The Foundation runs its own Discourse forum. Its welcome topic — stamped 2026-03-18 in the capture, with the post header reading 2026-04-22 17:32:07 UTC — calls the forum "the home for developers, contributors, researchers, miners, and anyone who believes Bitcoin mining should be free, open, and accessible to everyone". The forum is organized around the projects the Foundation funds and develops, with categories for General, Ember One Hashboard, Mujina Firmware, Libre Control Board, Hydrapool, asic-rs and Site Feedback. The same post routes day-to-day discussion to the Telegram group at t.me/the256foundation, points followers to x.com/256FOUNDATION and Nostr, and lists admin@256foundation.org or Signal tylerkstevens.97 for moderation concerns.

## What these captures do not contain

- No Telegram message text, dates or reply threads for either group: the bot queue was empty and group history is not exposed on the web preview. An empty queue is not evidence the groups are quiet.
- No Nostr note bodies: 46 notes are counted, none copied.
- The X archives are keyword-search samples with a 10-hit query limit, not official exports, and each file lists its own coverage gaps. Engagement counts are as of collection on 2026-10-07; member and follower counts are single-day reads from the same date.
- The forum.heatpunks.org pull of 2026-10-07 covers only the first page of latest.json; nothing newer than 2026-09-12 was on it. The 2026-10-10 capture-loop census and 81-topic backfill close that gap through 2026-10-10, but both still see only what about.json and latest.json expose anonymously — staff-only and unlisted topics are counted in the 119, not readable.

## See Also

- [Community Workshop Wisdom](community-workshop-wisdom.md)
- [256F Community Timeline](../history/256f-community-timeline.md)
- [The 256 Foundation](../history/256-foundation-organization.md)
- [Hashrate Heatpunks Community Timeline](../history/heatpunks-community-timeline.md)
- [OSMU Open Miners: NerdMiner, PiAxe, QAxe & BitForge](../hardware/osmu-open-miners.md)
- [Mining Policy and Legal](../industry/mining-policy-and-legal.md)
