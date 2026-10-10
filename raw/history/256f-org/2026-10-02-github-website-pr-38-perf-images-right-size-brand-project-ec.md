# 256foundation/website pull request #38: perf(images): right-size brand, project, ecosystem and supporter art

> Source: https://github.com/256foundation/website/pull/38
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 38
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

Cuts shipped raster weight ~13 MB -> ~1.5 MB with no visual change.

**Why:** project marks, ecosystem logos, supporter logos and the logo set are served through raw `<img>`/`<picture>`, so every original byte was downloaded and then scaled down to a ~48-80px render. Some project marks were 2 MB and ecosystem logos 1.7 MB.

**What:**
- New `scripts/optimize-art.mjs` (the existing newsroom pass only covered `public/newsroom`) converts rasters under `public/projects`, `public/ecosystem`, `public/supporters` above 40 KB to WebP (max 800px, q82) and rewrites references.
- Re-encoded `public/logos/*` and `public/og/256F-OG.png` to compressed palette PNG (same paths/format, so no code changes).

Sizes: projects/ecosystem/supporters 10.1 MB -> 1.2 MB, logos+OG 3.2 MB -> 0.56 MB.

Verified: header/footer logo, project marks on home + `/projects`, and ecosystem logos on `/community` all render correctly (transparency intact); `npm run lint` 0 errors, `npm test` 50/50, `npm run build` clean.
