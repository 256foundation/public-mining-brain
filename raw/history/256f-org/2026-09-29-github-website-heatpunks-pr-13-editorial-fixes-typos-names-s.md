# 256foundation/website-heatpunks pull request #13: Editorial fixes: typos, names, stale docs, X handle

> Source: https://github.com/256foundation/website-heatpunks/pull/13
> Collected: 2026-10-07
> Published: 2026-09-29

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 13
- State: open
- Author: average-gary
- Opened: 2026-09-29
- Closed: n/a
- Labels: none

## Description

Copy and docs cleanup from an editorial pass plus an external link check.

**Each fix is its own commit** so any change you don't want can be dropped independently (revert or drop it in a rebase) without touching the rest.

## What's included
- **Schedule/video copy:** grammar fixes ("heating element is", "Guests Dip", "rotate"), punctuation (stray period in the pool payout panel, missing final periods), and name spellings (BACnet, IoT, ASICs, Anti-Corruption Foundation, Undermine).
- **Components:** footer label `[256.ORG]` → `[256FOUNDATION.ORG]` (the link already points to 256foundation.org), "HEATPUNK SUMMIT 2026" heading, and an em dash in the grants copy.
- **Education page:** lowercase "donations" mid-sentence.
- **README/CLAUDE.md:** removed the stale "Heatpunk Grant Program" / `grants.open` toggle text (grants are run by the 256 Foundation), corrected where the featured video appears (`/summit/2026`), and corrected how the forum feed behaves when `DISCOURSE_URL` is unset or the forum is unreachable.
- **X handle:** `@HashHeatpunks` → `@heatpunks` (the social link, Twitter card tags, and JSON-LD `sameAs`).

## Link check
All external links and all 38 YouTube IDs resolve. Only the X link needed a change.

## Follow-up decisions (also separate commits)
- The 2026 award is now called "Heatpunk Innovation Award" everywhere (it was also called "Heatpunk Hardware Award").
- `/summit/schedule` now has an `[ARCHIVE]` line under the header. The 2026 descriptions keep their original wording.
- `/summit/schedule` no longer has the "add all to calendar" button or the per-session calendar buttons, since they would add past dates. `AddToCalendar` and `lib/calendar.ts` are kept for reuse on 2027.
- The donate section item is renamed "256 FOUNDATION GRANTS" so it doesn't read as a Heatpunks program.
- "Join Ocean Mining" is left as-is on purpose.

Apart from the archive note and removing the calendar buttons, only text strings changed; the YAML still parses. Lint was not run locally.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
