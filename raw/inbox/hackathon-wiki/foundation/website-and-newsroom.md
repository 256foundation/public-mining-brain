# Website and Newsroom

> Sources: 256 Foundation GitHub (website README), collected 2026-10-07; 256 Foundation (newsroom index), collected 2026-10-07; 256 Foundation (grants announcements page), collected 2026-10-07; 256 Foundation (home page), collected 2026-10-07
> Raw: [website README](../../raw/foundation/github-256foundation-website.md); [256foundation.org newsroom](../../raw/foundation/256foundation-org-newsroom.md); [256foundation.org grants announcements](../../raw/foundation/256foundation-org-grants-announcements.md); [256foundation.org home](../../raw/foundation/256foundation-org-home.md)
> Updated: 2026-10-07

## Overview

256foundation.org is the foundation's public site. Its source is open on GitHub. The site is mostly static, pulls a little live data from GitHub, the forum, Substack and the mining pool, and keeps its content in plain data files and MDX posts so non-developers can update it. The newsroom is where the foundation publishes its own announcements, and grant announcements posted there also feed a funding log on the grants page.

## What the site says up front

The home page leads with the foundation's thesis: Bitcoin mining will be open-source, or Bitcoin remains permissioned. It then makes four points.

- A miner is four building blocks, and the foundation open-sourced all four. Together they form the Development Kit.
- The projects run. In 2025, miners around the world pointed hashrate at the foundation's pool and found Bitcoin block 881423. Nine months later the four projects ran together as a complete kit.
- It funds builders. "Money from anyone, influence from no one."
- It is a community. The forum is where work gets argued out. The group chat is where it starts.

## Pages

| Route | Purpose |
|---|---|
| `/` | Home |
| `/mission` | Mission statement, principles, founders and board |
| `/projects` | The "Open Mining Stack": hash board, control board, firmware, pool |
| `/grants` | The two grant programs and the funding announcements log |
| `/grants/announcements` | Archive of every grant announcement, newest first |
| `/donate` | Bitcoin, Lightning, card and hashrate donation |
| `/telehash` | Participation guide and event history |
| `/faq` | Categorized questions and answers |
| `/newsroom` | List of foundation-authored posts |

The top navigation also links out to ecosystem projects (Bitaxe, OSMU, Hashrate Heatpunks, Jua Kali, ASIC-rs, HashScope) and to community channels (forum, group chat, newsletter, POD256, X, Nostr, Hashdash).

## The newsroom

Posts are written by the foundation and sorted newest first. There are five categories: perspective, foundation news, project update, highlight, and grant announcement. As collected, the newsroom listed six posts.

| Post | Category | Wiki coverage |
|---|---|---|
| Additional Funding Reactivates Libre Board's 2026 Term | Grant Announcement | [Libre Board](../hardware/libre-board.md) |
| It's Time to Commoditize Bitcoin Mining | Perspective | [Presidio Bitcoin Fundraiser](presidio-bitcoin-fundraiser.md) |
| HRF Renews Support for the 256 Foundation | Foundation News | [Grants and Funding](grants-and-funding.md) |
| The RY3T Nova: The First Product Built on Mujina | Highlight | [RY3T Nova](ry3t-nova.md) |
| 256 Foundation Wins $100,000 from the MARA Foundation | Foundation News | [Grants and Funding](grants-and-funding.md) |
| Ember One: our first grant builds the miner from the chip up | Grant Announcement | [Ember One](../hardware/ember-one.md) |

The home page's "What's new" strip shows one item each from the newsroom, POD256 and the newsletter.

## The funding log

Posts in the grant announcement category also appear in a funding log on the grants page, which shows at most 6, and in the full archive. The archive listed two grants when collected:

| Project | Program | Term |
|---|---|---|
| Libre Board | Core Projects Program | Four months, September 2026 to December 2026 |
| Ember One | Core Projects Program | Six months, November 2024 to April 2025 |

The README sets rules for this log:

- It covers grants the foundation gives. Grants it receives from third parties, such as HRF and MARA, are filed as foundation news instead.
- It never shows a dollar amount.
- Every term uses one format: duration, then start month and year to end month and year.
- An automated test enforces the rules.

## How the site is built

- **Stack.** Next.js 15 with the App Router, React, TypeScript and Tailwind CSS v4. Newsroom posts are MDX files. The README says there are no other runtime dependencies.
- **Static first.** Most pages are generated at build time. The home page and the projects page refresh hourly so live data stays current.
- **One API route.** `/api/hashdash` queries the pool's Prometheus API for the top 5 workers, total hashrate and active worker count, and resolves Nostr names and avatars for npub identities. It returns `503` if the pool is unreachable.
- **Live data.** GitHub stars, forks and activity, the latest forum topics, and Substack posts. GitHub is called unauthenticated by default, and a token raises the rate limit to 5,000 req/hr.
- **Contact form.** Posts straight to Formspree from the browser. No server-side email is involved.
- **Analytics.** Umami, self-hosted and optional.
- **Hosting.** The README documents three paths: Vercel, self-hosting on Proxmox with Nginx and PM2, and platform hosts (Coolify, Netlify, Railway). The site builds and runs with no environment variables set.

One quirk the README records: the Libre Board forum category uses the slug `fibre-board`, a legacy typo.

## Design rules

- Dark mode is the primary experience and follows the operating system setting. There is no toggle.
- No rounded corners anywhere.
- Purple is the only accent color. Terminal green is reserved for live status and code text.
- Borders, not shadows, create depth.
- Headings are uppercase in Barlow Condensed. Space Mono is used for code, labels and buttons. Inter is used for body text.

## Updating content

Content lives in a `data/` folder and a `content/newsroom/` folder, so most updates need no component changes. Adding a newsroom post means adding one MDX file with a title, date, author, category and excerpt. Adding a Telehash event, a supporter logo or a team member means editing one data file.

## See Also

- [256 Foundation: Mission and Organization](mission-and-organization.md)
- [Grants and Funding](grants-and-funding.md)
- [Donate and Get Involved](donate-and-get-involved.md)
- [256 Foundation FAQ](faq.md)
