# 256foundation/website pull request #21: Rebrand logo system, nav reorder, full-bleed stack hero

> Source: https://github.com/256foundation/website/pull/21
> Collected: 2026-10-07
> Published: 2026-09-29

- Repository: 256foundation/website
- Type: pull request
- Number: 21
- State: closed
- Author: tylerkstevens
- Opened: 2026-09-29
- Closed: 2026-09-29
- Labels: none

## Description

## What

Second UI round on top of the Open Mining Stack page (PR #20). Three things:

1. **New brand logo system** — swaps in the new assets and fixes a color-mode bug.
2. **Nav cleanup/reorder**.
3. **Full-bleed hero** on `/projects`.

> Note: branched off `ui/website-changes` (PR #20). Until that merges, this PR's diff includes its commits; after merge it will show only this round.

## Changes

### Logo
- Added the six new assets to `public/logos/` (`horizontal`/`secondary`/`vertical` × `dark`/`light`), trimmed to sane sizes; removed the old horizontal/vertical files.
- **Bug fix:** the `<picture>` logic was inverted — light mode served white artwork on a white background, making the logo invisible. `Logo.tsx` now serves dark/purple artwork in light mode and white artwork in dark mode.
- Applied sitewide: header + mobile drawer use the compact **secondary** lockup; hero + footer use the full **horizontal** wordmark.
- Regenerated `app/icon.png` (favicon) from the new 256 mark.

### Nav
- Removed the **Home** item (logo links home).
- Reordered to: **Mission · Mining Stack · Grants · Newsroom · Ecosystem · Community**.

### Hero
- `app/projects/page.tsx` hero is now a **full-bleed, responsive** background image (`fill` + `object-cover`) with gradient contrast overlays and overlaid white copy.
- Added `public/projects/open-mining-stack.webp` at 2400×2272 (399KB, down from a 3.1MB source).

## Verification

- `npm run build` — clean (18 routes)
- `npm run lint` — 0 errors (6 pre-existing warnings)
- `npm test` — 26/26 pass
- Responsive check: hero fills viewport at desktop (1436×640) and mobile (386×560); header/hero/footer logos have no overflow.

## Notes for review

- Header/mobile use the **secondary** lockup to fit the nav; hero/footer use the full wordmark. Easy to switch the header to horizontal if preferred.
- `square`/`circular` variants still point at the older files (currently unused).
