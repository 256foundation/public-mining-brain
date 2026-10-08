# 256foundation/website pull request #32: Design-system continuity pass (round 12)

> Source: https://github.com/256foundation/website/pull/32
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 32
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

Follow-up to the round-12 design audit. Consolidates drifted UI patterns into shared primitives and tokens; page layouts are unchanged.

## What changed
- **New primitives:** `Eyebrow` (single kicker), `TextLink` (single inline `→` link), `Panel` (hero header/body/footer box). New `lib/tokens.ts` surface tokens.
- **Kickers** unified to `Eyebrow` everywhere (SectionHeader label, local SectionKickers, inline kickers).
- **Buttons:** added `onDark` / `onDarkOutlined`; replaced ~15 hardcoded CTAs; fixed low-contrast outlined buttons on photo heroes.
- **Closers:** one `PageCTA` with `align`/`extra`/`footnote`; our-work and projects now use it.
- **Panels:** donate/telehash/faq heroes render the shared `Panel`.
- **Badges:** new states; telehash/grants pills route through `Badge`.
- **Surfaces:** dark card values collapsed; `Card` carries tokens.
- **Spacing:** named `SectionWrapper` size scale.
- **Accent:** purple is the brand accent; green reserved for live/active/hashrate.

## Checks
- `npm test` 50/50
- `npm run lint` 0 errors (7 pre-existing `<img>` warnings)
- `npm run build` green

Branched off `ui/edits-round11` (#31, now merged); merges cleanly into `main`.
