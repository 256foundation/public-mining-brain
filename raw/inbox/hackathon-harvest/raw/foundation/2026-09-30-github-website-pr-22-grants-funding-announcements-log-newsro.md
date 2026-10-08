# 256foundation/website pull request #22: Grants funding announcements log + newsroom category taxonomy

> Source: https://github.com/256foundation/website/pull/22
> Collected: 2026-10-07
> Published: 2026-09-30

- Repository: 256foundation/website
- Type: pull request
- Number: 22
- State: closed
- Author: tylerkstevens
- Opened: 2026-09-30
- Closed: 2026-09-30
- Labels: none

## Description

Adds the grants-page funding-announcements log (replacing "Stay Informed"), a `/grants/announcements` archive, and the newsroom category work that feeds it. Also ships the first announcement article and a newsroom category filter.

## What's in it

**Taxonomy**
- Replaces the six newsroom categories (five unused) with five: `perspective`, `foundation-news`, `project-update`, `highlight`, `grant-announcement`.
- Remaps the four existing posts (Presidio -> Perspective; HRF + MARA -> Foundation News; RY3T Nova -> Highlight).
- `category` is now validated in `toPost` instead of cast; a typo can no longer silently drop a post into the log.

**Grants log**
- New `FundingAnnouncements` + `GrantAnnouncementCard`. Newest-first, max 6, "View all ->" when there are more. Card shows date, project, program chip, term, and the excerpt. No amounts. Intentional empty state (sub-line link suppressed when empty).
- Hero card relabeled "Funding announcements" and linked to `#funding-announcements`.
- New `/grants/announcements` archive.
- General Grant "Apply for a Grant" button wired to the Typeform form.
- The old newsletter / POD256 / social links leave `/grants` as agreed.

**Newsroom**
- Category filter (All + per-category chips with counts; only populated categories show).
- Fix: `/newsroom` and the home Updates column now run strict newest-first (`getAllPostsByDate`); `featured` no longer reorders either feed.
- Split fs-free helpers into `lib/newsroomMeta.ts` so client components can import them (importing `lib/newsroom.ts` into a client bundle failed on `fs`).

**Article:** `content/newsroom/libre-board-funding.mdx` + cover photo.

## Reviewer notes

- **Two pre-publish items still open** (recorded in `docs/ui-work-log.md`): Schnitzel's consent to being named/linked, and verifying "revision three" against the repo before publishing.
- **The article's "What the Funding Covers" and "What's Next" sections** are inferred from the scope line plus the existing Libre Board specs. Worth a close read.
- **`featured: false`** on the new post, so it doesn't disturb the home slot while that's worked on separately.
- Copy rules enforced by `tests/grant-announcements.test.mjs`: no cycle/wave/round, no amounts, no pillar/retainer/adoption-phase, no retired program names, no em dashes.

## Test plan

- `npm run build` (20 routes, both new routes prerendered), `npm run lint` (0 errors), `npm test` (35 pass).
- Manually verified: log renders + links, archive renders, empty state renders when the article is removed, filter chips filter and reset, newsroom + home order newest-first, Typeform button targets the form in a new tab.
