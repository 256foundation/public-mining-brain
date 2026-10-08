# 256foundation/website pull request #24: Community page, Our Work stub, nav consolidation, and site copy polish

> Source: https://github.com/256foundation/website/pull/24
> Collected: 2026-10-07
> Published: 2026-10-01

- Repository: 256foundation/website
- Type: pull request
- Number: 24
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-01
- Closed: 2026-10-01
- Labels: none

## Description

Consolidates the Ecosystem and Community nav dropdowns into one `/community` page, adds a light `/our-work` stub, moves the supporter showcase to `/donate`, and sweeps retired canon vocabulary site-wide. This PR supersedes the earlier #23 with the full set of follow-up work included.

## What's here

### New pages
- **`/community`** — one narrative: photo-carousel hero (real community photos), Connect (six channel cards), Community projects (community-directed funds: OSMU + Hashrate Heatpunks, with full descriptions; projects we serve: Bitaxe, Jua Kali, ASIC-rs, HashScope), a featured **Telehash** block linking `/telehash`, Listen and learn (live Substack + POD256 cards + newsletter signup), Get involved (Conversation + Code/GitHub blocks).
- **`/our-work`** — real-but-light first pass covering all agreed outline sections (thesis, status quo, vision, proof of work, how we work, programs, close). Added to nav, footer, and sitemap.

### Nav / structure
- Both dropdowns removed. Header and footer order: `Mission · Our Work · Mining Stack · Grants · Community · Newsroom`.
- Mobile nav is now flat links; footer "Open Mining Stack" renamed "Mining Stack".
- **Supporters** — `SupporterShowcase` (logo tiers + live hashrate leaderboard) moved off the home page onto `/donate`.

### Carousel
- Full-bleed hero crossfade with dot nav and subtle arrows flanking the dots, swipe on touch, pause on hover, reduced-motion static.
- Any manual move resets the autoplay timer.

### Copy / canon sweep
- Retired vocabulary replaced across FAQ, home ApplySection/ProjectsSection/EcosystemSection, and telehash copy.
- Hero and section copy revised per review; Telehash block corrected (block height 881423).

### Layout fixes
- Centered the `/projects` closing CTA block and the `/our-work` close.
- `/our-work` programs use a numbered list so the five items never leave an orphan row.

### Tests
- `tests/community.test.mjs` guards channel/project sets, nav order, sitemap coverage, and banned vocabulary.

## Notes for review

- `/our-work` copy is a first pass (commented as such) and reuses `mission-background.webp` as its hero; dial in later.
- Home still has its old Community/Ecosystem sections (language-scrubbed); its full overhaul comes after this and Our Work.
- Community hero photos live in `public/community/hero-0*.webp` (1920px WebP); reorder or swap via `communityHeroPhotos` in `data/community.ts`.

## Verification

`npm test` (44 pass) · `npm run lint` (0 errors, 7 pre-existing `<img>` warnings) · `npm run build` green — `/community` and `/our-work` prerender static.
