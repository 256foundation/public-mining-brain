# 256foundation/website pull request #15: feat(home): rebalance News & Updates into three equal columns

> Source: https://github.com/256foundation/website/pull/15
> Collected: 2026-10-07
> Published: 2026-09-07

- Repository: 256foundation/website
- Type: pull request
- Number: 15
- State: closed
- Author: tylerkstevens
- Opened: 2026-09-07
- Closed: 2026-09-07
- Labels: none

## Description

News & Updates was two-thirds newsletter: the newsroom got a single strip, the podcast a static blurb with no episodes at all. Newsletters have slowed down while podcasts and newsroom posts have not, so the section now gives all three equal billing.

## What changed

**Three peer columns** — Updates, Podcast, Newsletter — each showing its two most recent items, the leading one with a preview image.

**Podcast episodes are now live data.** pod256.org publishes through Podhome and links its RSS feed; `lib/pod256.ts` reads that feed on the same hourly revalidate as the other fetchers and fails soft to an empty list the way they do. Cards show `EP 124 · 1h 05m · August 17, 2026`; the duplicated `124.` prefix is stripped from feed titles.

**The inline newsletter signup box is gone**, replaced by an "All Newsletters →" link plus a subscribe note, matching the other two column footers. `components/shared/NewsletterSignup.tsx` now has no callers — left in place rather than deleted, since it is the only email-capture UI in the codebase.

**Bug fix: feed text rendered raw HTML entities.** `HydraPool&#8217;s Record Stress Test` appeared literally on the page. Tag-stripping left entities behind and React escapes on output, so decoding has to happen at parse time — new `lib/html.ts`. This was pre-existing and also affected the old Substack cards.

## Layout notes

- Columns stack below `lg` and go three across at `lg`. No two-across `md` step: with three columns it strands the third on a row of its own.
- Only the lead card in each column carries artwork. Six images turned the section into a wall of pictures rather than a scannable summary.
- POD256 art is a round logo on its own ground, so it uses `object-contain`; `object-cover` cut off the circle. The wide newsroom and Substack covers still use `object-cover`. `assets.podhome.fm` joins the `next/image` remote patterns.

## Verified

- `npm test` — 26/26 pass
- `npm run build` — clean
- `npm run lint` — 0 errors
- Rendered at 375px, 768px and desktop, light and dark: 1/1/1 stacked below `lg`, 3-across at `lg`, no horizontal overflow, all images loading
- Desktop section height down from ~1180px to 865px

## Known open items

- The Updates column footer still reads "All Announcements →" rather than matching its heading.
- Every POD256 episode reuses the same show logo, so that lead image will not change as new episodes land.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
