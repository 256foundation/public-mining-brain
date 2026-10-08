# Donate and Get Involved

> Sources: 256 Foundation (donate page), collected 2026-10-07; 256 Foundation (community page), collected 2026-10-07; 256 Foundation (contact page), collected 2026-10-07; 256 Foundation (home page), collected 2026-10-07; 256 Foundation (Hashdash), collected 2026-10-07; 256 Foundation GitHub (grants README), collected 2026-10-07; 256 Foundation GitHub (News README), collected 2026-10-07
> Raw: [donate page](../../raw/foundation/256foundation-org-donate.md); [community page](../../raw/foundation/256foundation-org-community.md); [contact page](../../raw/foundation/256foundation-org-contact.md); [home page](../../raw/foundation/256foundation-org-home.md); [Hashdash](../../raw/foundation/dash-256f-org-home.md); [grants README](../../raw/foundation/github-256foundation-grants.md); [News README](../../raw/foundation/github-256foundation-news.md)
> Updated: 2026-10-07

## Overview

There are three ways to support the 256 Foundation: give money, give hashrate, or give time. Money goes through Zaprite or straight to a Bitcoin or Lightning address. Hashrate goes to the foundation's Hydrapool instance and is tracked on the Hashdash dashboard. Time goes into the forum, the group chat and the project repos. The foundation also hosts two sub-communities, OSMU and Hashrate Heatpunks, and stewards a donation fund for each.

## Donating money

- **Through a processor.** The donate page links to a Zaprite page that takes Bitcoin or fiat.
- **Directly.** The donate page lists an on-chain address, `bc1qce93hy5rhg02s6aeu7mfdvxg76x66pqqtrvzs3`, and a Lightning address, `256foundation@strike.me`. Hashdash shows the same on-chain address and a different Lightning address, `donate@256f.org`.
- **Privately.** The grants README on GitHub also offers a PayNym.
- **Large or unusual gifts.** The donate page asks you to get in touch first.

The grants README says 100% of General Fund donations go to the people working on the funded initiatives, and that these grants are meant as long-term support, "not touch-and-go projects".

## Donating hashrate

If the pool finds a block, all proceeds go to the foundation. The donate page puts the cost plainly: it costs you only electricity.

1. Set the pool URL to `stratum+tcp://pool.256foundation.org:3333`.
2. Set the stratum username to `username.workername`. Both parts can be anything.
3. Save and restart the miner.
4. Watch for your miner on the live leaderboard at dash.256f.org. It appears within a few minutes.

Hashdash lists three username choices that give you an identity on the leaderboard: a Nostr npub, an X handle such as `@256foundation`, or a website written like `256foundation_dot_com`. The worker name is appended after a dot, for example `@256foundation.bitaxe-1`.

During [Telehash](telehash.md) events the whole community points hashrate at the pool together.

## Hashdash

Hashdash is the pool dashboard at dash.256f.org. Its overview shows hashrate over 5 minutes, average hashrate over 1 hour, active users and active workers. It has a hashrate history chart, a miner share chart, and two leaderboards: a Difficulty Leaderboard by user and worker, and a Loyalty Leaderboard by hashes per user.

## Where the community lives

The community page describes several doors into one community:

- **Forum.** Public conversation, project questions, support and dev-call threads. See [256 Foundation Forum](forum.md).
- **Group chat.** The home page says the group chat is where work starts and the forum is where it gets argued out.
- **Repos.** "The forum is where it starts. The repos are where it lands."
- **Newsroom, newsletter and podcast.** The three channels where the work gets explained.

For anything else, the contact page offers a form and the address contact@256foundation.org. It invites questions about a grant, a donation, or a project that might belong in the open stack.

## The newsletter

The newsletter is called Assembling Freedom. The News repo on GitHub hosts PDF copies and says all issues are published under the CC0 1.0 license. It describes the newsletter as weekly. The archive there starts with "January 2025 - A Spark of Defiance", runs monthly through 2025 with titled issues, and then picks up numbered issues, ending at Assembling Freedom #27.

> **Status: Disputed**
> The News README dates Assembling Freedom #27 as May 27, 2026. The foundation's home page lists the same issue under May 28, 2026.

## Sub-communities the foundation hosts

The foundation does not run or direct these groups. It gives them infrastructure, a nonprofit home, and a dedicated donation fund. The community directs the work, the board approves every allocation, and donations go to the community's own priorities.

- **Open Source Miners United (OSMU).** An informal network of developers behind Bitaxe, NerdAxe, AxeOS, Qaxe, Piaxe and more. It has no membership and needs no permission. See [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md).
- **Hashrate Heatpunks.** Home and business miners who treat miner heat as a product. See [Hashrate Heatpunks](hashrate-heatpunks.md).

The older grants README adds detail on the OSMU Fund: 100% of donations to it support open-source mining developers, the Discord server, bug bounties, legal matters and other community support. The same README, under a "coming soon" heading, says the foundation planned to team up with OSMU and make Bitaxe an official project supported through its grant programs.

## Applying for a grant

The grants README says all grant application periods were closed when it was written, with openings announced on Twitter. It still invites people to introduce themselves and apply. Current rules are in [Grants and Funding](grants-and-funding.md) and the [256 Foundation FAQ](faq.md).

## See Also

- [256 Foundation FAQ](faq.md)
- [Telehash](telehash.md)
- [256 Foundation Forum](forum.md)
- [Hydrapool](../hydrapool/hydrapool.md)
