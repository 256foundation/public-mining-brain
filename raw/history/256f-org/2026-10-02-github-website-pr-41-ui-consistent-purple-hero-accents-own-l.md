# 256foundation/website pull request #41: ui: consistent purple hero accents, own-line emphasis, drop hero periods

> Source: https://github.com/256foundation/website/pull/41
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 41
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

Hero-heading consistency pass across the main pages.

- **Home**: "open-source" gets its own line and a purple accent.
- **Mission**: purple on "decentralize", "open-source", and "mining stack".
- **Grants**: accent moves to "Funding"; "open-source" stays white.
- **Community**: "build" highlighted purple (headline is now a `ReactNode`).
- **Our Work**: "Bitcoin mining stack" on its own line, purple (from the first commit).
- Removed the trailing period from every main-page hero header (home, mission, our-work, community, donate) so they match.

Merged current `main` in so this sits on top of #40 (lint clean, no `<img>` warnings). Verified all six heroes render; `npm test` 50/50, `npm run build` clean.
