# 256foundation/website pull request #33: Round 13: mission narrative rework, footer logo + link order, shared hero scrim

> Source: https://github.com/256foundation/website/pull/33
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 33
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

Round-13 UI pass. Mission-page narrative rebuilt, footer logo/order fixes, and hero dimming unified.

## What changed
- **Mission hero:** added the new photo as a full-bleed hero behind the mission statement, matching other main pages.
- **Mission narrative:** dropped the standalone photo band; recast the intro as four numbered, bolded story beats that lead into the Vision.
- **Mission vision:** now two large display statements (hero-scale type); removed the blockquote frame and sub-paragraphs.
- **Hero dimming:** extracted one shared `HeroScrim` and applied it to mission / our-work / grants / projects / community so the treatment is identical everywhere.
- **Footer:** brand logo now uses the same `secondary` 256F lockup as the header; reordered the Elsewhere links (GitHub, Forum, Group Chat, Events, Hashdash, POD256, Newsletter, X / Twitter, Nostr).

## Checks
- `npm run lint` 0 errors (7 pre-existing `<img>` warnings)

Branched off `ui/edits-round12` (#32, open), so this PR includes those commits until #32 merges.
