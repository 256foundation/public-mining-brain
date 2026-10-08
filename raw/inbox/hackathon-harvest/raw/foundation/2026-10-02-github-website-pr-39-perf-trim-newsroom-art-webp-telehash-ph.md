# 256foundation/website pull request #39: perf: trim newsroom art, webp telehash photos, lazy-mount community hero

> Source: https://github.com/256foundation/website/pull/39
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 39
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

Second image/perf pass, no visual change.

- Re-ran the existing newsroom optimizer (`npm run optimize:images`): the one remaining oversized original (`libre-board-funding/cover.jpeg`, 311 KB) is now WebP, plus marginal re-encodes of new art.
- Extended `scripts/optimize-art.mjs` with per-directory caps and added `public/telehash`, whose five full-width carousel photos were still JPEG (2.2 MB -> 0.8 MB WebP).
- `CommunityHeroCarousel` rendered all 8 full-width hero `next/image`s at once; it now mounts only the current frame and its two neighbours, so `/community` loads 3 hero images instead of 8 (crossfade and reduced-motion behaviour unchanged).

`public/` 9.4 MB -> 7.8 MB. Verified `/telehash` carousel and `/community` hero render; `npm run lint` 0 errors, `npm test` 50/50, `npm run build` clean.
