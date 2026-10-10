# 256foundation/website pull request #26: style(footer): restructure footer, separate supplemental pages

> Source: https://github.com/256foundation/website/pull/26
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 26
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

## Summary
Restructures the footer so supplemental pages are no longer tacked onto the primary Foundation links, and evens out the link-column spacing.

- **New "Resources" column** for supplemental on-site pages: `Announcements` (`/grants/announcements`), `Telehash`, `FAQ`. Uses an outlined section marker so it reads as secondary.
- **Adds the previously missing** `/grants/announcements` link.
- **Donate promoted** to a standalone filled CTA under the logo/tagline in the brand column (kept out of the link lists).
- **Removes the social icon row** — X, GitHub, Group Chat, and Nostr were fully duplicated by the external link column.
- **Renames the external column** "Community" → "Elsewhere", distinguishing it from the on-site `/community` page link.
- **Even spacing** across the three link columns: shortens the long "Funding announcements" footer label to "Announcements" and uses an equal-width subgrid so the visual gaps stay consistent.
- Updates `docs/ui-work-log.md`.

## Layout
Four columns on `lg` (brand + three link columns), stacks cleanly on mobile.

## Verification
- `npm run lint` — 0 errors (7 pre-existing `<img>` warnings)
- `npm test` — 44/44 pass
- `npm run build` — green, all routes prerender

## Note
This branch is based off `main` plus the `docs/session-context.md` handoff commit (`ebd2ba0`), which was never merged from `ui/edits-round5`. It is included here so the context lands with this work.
