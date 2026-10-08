# 256foundation/website pull request #23: Community page: consolidate Ecosystem + Community, add Our Work stub

> Source: https://github.com/256foundation/website/pull/23
> Collected: 2026-10-07
> Published: 2026-09-30

- Repository: 256foundation/website
- Type: pull request
- Number: 23
- State: closed
- Author: tylerkstevens
- Opened: 2026-09-30
- Closed: 2026-10-01
- Labels: none

## Description

Consolidates the Ecosystem and Community nav dropdowns into a single `/community` page, adds a light `/our-work` stub, moves the supporter showcase to `/donate`, and sweeps retired canon vocabulary site-wide.

## What's here

- **`/community`** — one narrative: photo-carousel hero (single CTA: Join the forum), Connect (six channel cards), Community projects (community-directed funds: OSMU + Hashrate Heatpunks; projects we serve: Bitaxe, Jua Kali, ASIC-rs, HashScope), a featured **Telehash** block linking `/telehash`, Listen and learn (live Substack + POD256 cards + newsletter signup), Get involved (Conversation + Code/GitHub).
- **`/our-work`** — real-but-light first pass covering all 8 agreed outline sections. Added to nav, footer, and sitemap.
- **Nav** — both dropdowns removed. `Mission · Our Work · Mining Stack · Grants · Newsroom · Community`. Mobile nav is now flat links.
- **Supporters** — `SupporterShowcase` (logo tiers + live hashrate leaderboard) moved off the home page onto `/donate`.
- **Canon sweep** — FAQ, home ApplySection/ProjectsSection/EcosystemSection, and telehash copy updated to core-projects / program-name vocabulary.
- **Tests** — `tests/community.test.mjs` guards channel/project sets, nav, sitemap, and banned vocabulary.

## Notes for review

- `public/community/hero-0*.jpg` are **placeholder** copies of the TeleHash photos. Drop real community shots there and swap `communityHeroPhotos` in `data/community.ts`.
- `/our-work` copy is a first pass (commented as such) and reuses `mission-background.webp` as its hero; dial in later.
- Home still has its old Community/Ecosystem sections (language-scrubbed); its full overhaul comes after this and Our Work.

## Verification

`npm test` (44 pass) · `npm run lint` (0 errors, 7 pre-existing `<img>` warnings) · `npm run build` green — `/community` and `/our-work` prerender static.

## Comments

### tylerkstevens on 2026-10-01

Superseded by a new PR with an updated description covering the follow-up work (real hero photos, manual carousel controls, copy revisions, nav reorder, layout fixes).
