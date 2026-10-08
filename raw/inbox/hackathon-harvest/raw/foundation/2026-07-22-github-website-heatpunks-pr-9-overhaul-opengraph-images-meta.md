# 256foundation/website-heatpunks pull request #9: Overhaul OpenGraph images + metadata; add llms.txt (AEO)

> Source: https://github.com/256foundation/website-heatpunks/pull/9
> Collected: 2026-10-07
> Published: 2026-07-22

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 9
- State: closed
- Author: tylerkstevens
- Opened: 2026-07-22
- Closed: 2026-07-22
- Labels: none

## Description

## Summary

Overhauls the site's social-share (OpenGraph) images and text metadata, and makes the site agent-ready (AEO). Full plan in [`SPEC-og-metadata.md`](SPEC-og-metadata.md).

### OG images
- `/api/og` rebuilt as a **terminal-window** template in bundled **JetBrains Mono** — HRHP logo + traffic-light dots in the title bar, `~/heatpunks $` prompt, a bespoke command per page, flame-gradient wordmark, green `//` comments, corner flame glow, static cursor. Replaces the generic black-bg template that read as AI-generated.
- Fonts bundled in-repo (OFL) — no external runtime dependency.

### Text / SEO
- Clean, SEO-conventional titles + descriptions for every route; descriptive home title, `Page | Hashrate Heatpunks` template.
- Every page now emits a matching **Twitter/X card + image alt text** (previously only the root layout defined a Twitter card).
- **Canonical URLs** on all pages.

### Architecture
- Content-as-data: new `data/pages.ts` inventory drives page metadata, the OG route, the sitemap, and llms.txt via a new `pageMetadata()` helper (`lib/metadata.ts`) — one source of truth.
- Removed stale `getSummitStatus()` date logic (hardcoded to 2026) and the large embedded base64 logo.

### AEO + fixes
- New **`/llms.txt`** (llmstxt.org format) generated from the inventory + site config.
- `sitemap.ts` iterates the inventory and now includes the previously-missing **`/summit/2026`**.
- JSON-LD Twitter handle reconciled to `x.com`.

## Verification
- `npm run lint` clean · `npm run test` 30/30 pass · production `npm run build` green (15 routes).
- Rendered and visually verified all 8 OG card variants (home, mission, education, summit, schedule, 2025, 2026, archive fallback).
- Verified rendered `<head>` tags (title, description, canonical, og:*, twitter:*, alt) plus `/llms.txt` and `/sitemap.xml` output.

## Notes / out of scope
- Satori can't render the site's `feTurbulence` noise / scanlines, so cards use the flame glow only (texture-free).
- Title-bar logo is the full wide HRHP badge; a square glyph mark would read cleaner at favicon size.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-07-22

[vc]: #CuXz/NqodsyvBCG3n3SOElkY5HZfuBoHHVasi/ZDHsI=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLWhlYXRwdW5rcyIsInByb2plY3RJZCI6InByal9JM0FDajFucFFjb013UjdrcGcySlJRUENteVZQIiwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tLzI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMvd2Vic2l0ZS1oZWF0cHVua3MvN1lYSjVwa1RXemY0Vm85ekt2QUxVVVBmSDRkRSIsInByZXZpZXdVcmwiOiIiLCJuZXh0Q29tbWl0U3RhdHVzIjoiRkFJTEVEIiwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IiJ9LCJyb290RGlyZWN0b3J5IjpudWxsfV19
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| [website-heatpunks](https://vercel.com/256-foundation-s-projects/website-heatpunks) | ![Error](https://vercel.com/static/status/error.svg) [Error](https://vercel.com/256-foundation-s-projects/website-heatpunks/7YXJ5pkTWzf4Vo9zKvALUUPfH4dE) |  | Jul 22, 2026 3:48pm |
