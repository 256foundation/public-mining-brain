# Community Channels

> Sources: Telegram Bot API read of public groups, collected 2026-10-07; Primal cache API (256 Foundation Nostr profile), collected 2026-10-07; Open Source Miners United (@osmu_global) on X, 2024-09-13 to 2026-09-27, collected 2026-10-07; forum.heatpunks.org (about.json and latest.json), collected 2026-10-07
> Raw: [Telegram public groups](../../raw/ecosystem/2026-10-07-telegram-public-groups.md); [Nostr profile npub1p0d256](../../raw/foundation/2026-10-07-nostr-256foundation-profile.md); [X archive: @osmu_global](../../raw/inbox/2026-10-07-x-osmu-global.md); [forum.heatpunks.org latest](../../raw/foundation/2026-10-07-forum-heatpunks-latest.md)
> Updated: 2026-10-07

## Overview

The open-source mining community meets in several places: Telegram groups, Nostr, Discord, forums and X. This article lists the public channels the sources measured on 2026-10-07 and what is known about each. The numbers are counts of members and posts. No chat messages were collected from Telegram or Nostr, so nothing here describes what people say there.

## Channels at a glance

| Channel | Run by | Size, as measured |
|---------|--------|-------------------|
| Telegram group @the256foundation | 256 Foundation | 211 members on 2026-10-07 |
| Telegram group @heatpunks | Hashrate Heatpunks | 175 members on 2026-10-07 |
| Nostr profile "256 FOUNDATION" | 256 Foundation | 223 followers, 46 notes |
| OSMU Discord | Open Source Miners United | passed the 5K Member milestone, per a post on 2024-12-14 |
| forum.heatpunks.org | Hashrate Heatpunks | 137 users, 118 topics, 678 posts |

## Telegram

### 256 Foundation group

The group @the256foundation is a supergroup titled 256 FOUNDATION. Its description reads:

> Public group chat for the 256 Foundation. Our mission is simple: build the open-source Bitcoin mining ecosystem. If that stokes your 🔥 then get in here.

- Members on 2026-10-07: 211, with 24 online at that moment.
- Members in an earlier read on 2026-09-05: 208.

### Heatpunks group

The group @heatpunks had 175 members on 2026-10-07, up from 171 on 2026-09-05. Details are in [Heatpunks Channels](heatpunks-channels.md).

### What the Telegram read can and cannot show

The counts come from a bot, foundation_community_bot, and from the public web preview pages. The bot was added after the groups already existed. It can only see messages sent after it joined that are still in its queue, and this pull found none. The web preview shows the title, description and counts, but no message history, because these are groups and not broadcast channels. The source is explicit that an empty queue is not evidence that the groups are quiet. An earlier scan on 2026-09-17 hit the same limit.

## Nostr

The foundation's Nostr profile is named 256 FOUNDATION and lists 256foundation.org as its website. Its bio reads "501(c)(3) public charity on a mission to dismantle the proprietary mining empire." The npub begins with the characters `npub1p0d256`.

Counts from the Primal cache on 2026-10-07:

- follows 6, followers 223
- notes 46, replies 0, long-form notes 0
- relays 9
- total zap count 19, total sats zapped 306183
- media count 36

The account's join time is recorded as `2024-06-04T16:32:33Z`. The current profile event was created on 2025-11-28.

The pull did not copy the text of the 46 notes. Two feed queries returned no notes for this account. The source warns against reading that as silence, since the count says the notes exist.

## Discord and the Discourse idea

OSMU's main home is its Discord. The archive of the OSMU X account calls Discord the primary OSMU surface. On 2024-12-14 the account said the Discord had passed the 5K Member milestone.

On 2026-05-09 the same account raised a concern. It said Discord is a good tool for connecting people and sharing knowledge, but it leaves out everyone who is not on it. It said OSMU had found Discourse and asked followers for their view. A reply that day said Discourse would run alongside Discord and might replace it in the future, and that Discord alone might be gatekeeping. The archive does not record a decision. See [OSMU on X](osmu-on-x.md).

## Forums

Hashrate Heatpunks runs a Discourse forum at forum.heatpunks.org. On 2026-10-07 it had 137 users, 118 topics and 678 posts, with 7 active users in the last 30 days. See [Heatpunks Channels](heatpunks-channels.md).

The 256 Foundation has its own forum, covered in [256 Foundation Forum](../foundation/forum.md).

## X

Most of what this wiki knows about day-to-day community talk comes from X archives. Those are covered by account:

- [Skot on Bitaxe and Copyleft](skot-on-bitaxe-and-copyleft.md)
- [OSMU on X](osmu-on-x.md)
- [Public Pool on X](public-pool-on-x.md)
- [Open Mining Voices on X](open-mining-voices-on-x.md)

## See Also

- [Heatpunks Channels](heatpunks-channels.md)
- [Donate and Get Involved](../foundation/donate-and-get-involved.md)
- [256 Foundation Forum](../foundation/forum.md)
- [Bitaxe and Open Source Miners United](bitaxe-and-osmu.md)
- [OSMU on X](osmu-on-x.md)
