# 256foundation/website pull request #42: content(grants): Ember One first grant announcement + funding-timeline consistency

> Source: https://github.com/256foundation/website/pull/42
> Collected: 2026-10-07
> Published: 2026-10-03

- Repository: 256foundation/website
- Type: pull request
- Number: 42
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-03
- Closed: 2026-10-03
- Labels: none

## Description

## Summary

Adds the Ember One first-grant article, and regularizes how grant timelines are communicated across the two live grant announcements.

### New article
- `content/newsroom/ember-one-first-grant.mdx` — backfilled `grant-announcement` post. Frontmatter matches the newsroom schema (title, seoTitle, date `2024-11-18`, category, project, program, term, excerpt, cover/og). Draft-only keys, H1, HTML comment and editor notes dropped; em dashes removed.
- `public/newsroom/ember-one-first-grant/cover.webp` — provided cover art, resized to 1440px via `scripts/optimize-images.mjs` (3.6 MB → 77 KB).

### Timeline consistency
- `content/newsroom/libre-board-funding.mdx` — now states the actual timeline: the 2026 term was set in April and ran through December, contingent on funding; funding ran short and the work paused; the September–December reactivation is four months and contingent. `excerpt` updated to carry the same on the grants-log card.
- Standardized the `term` format to `<Duration>, <Month Year> to <Month Year>` (aligns the Libre post, which had drifted from the documented format; Ember already matched).
- `tests/grant-announcements.test.mjs` — updated the Libre assertion and added a test enforcing the term format on every `grant-announcement`.
- `README.md` / `CLAUDE.md` — documented the term format next to the frontmatter spec.

## Notes
- Ember is dated 2024-11-18 (backfill), so it sorts below the live 2026 posts and has `featured: false`.
- Surfaces at `/newsroom/ember-one-first-grant`, in `/newsroom`, and in the `/grants` funding log.

## Verification
- Page, cover, `/newsroom` list, and `/grants` log all render.
- `node --test tests` 51/51 pass; `npm run lint` clean.
