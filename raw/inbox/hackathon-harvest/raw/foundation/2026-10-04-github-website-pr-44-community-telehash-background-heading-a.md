# 256foundation/website pull request #44: Community: Telehash background, heading, and nav tweaks

> Source: https://github.com/256foundation/website/pull/44
> Collected: 2026-10-07
> Published: 2026-10-04

- Repository: 256foundation/website
- Type: pull request
- Number: 44
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-04
- Closed: 2026-10-04
- Labels: none

## Description

## Summary
Community-page review annotations, plus the mobile-menu Donate tweak.

## Changes
- **Telehash card** now uses the livestream frame (`hero-03`) as its background; frame removed from the hero carousel. Whole card links to `/telehash`.
- **Connect heading** reads "Where the 256 Community lives".
- **Hashdash** card described as "Our donation pool and gamified dashboard."
- **MobileNav** Donate button loses the lightning bolt.

## Verification
- `npx tsc --noEmit` clean, `npm run lint` clean, `node --test tests` 51/51 pass
- Desktop + mobile renders checked
