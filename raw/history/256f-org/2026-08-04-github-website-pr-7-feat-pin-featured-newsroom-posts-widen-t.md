# 256foundation/website pull request #7: feat: pin featured newsroom posts; widen the category union

> Source: https://github.com/256foundation/website/pull/7
> Collected: 2026-10-07
> Published: 2026-08-04

- Repository: 256foundation/website
- Type: pull request
- Number: 7
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-04
- Closed: 2026-08-05
- Labels: none

## Description

Two structural gaps in the newsroom: a post you want to keep visible sinks the moment anything newer publishes, and there are only four categories to publish under.

## What changed

| File | Change |
|---|---|
| [`types/index.ts`](types/index.ts) | Widen `NewsroomPost.category` with `'grant'` and `'manifesto'`; add optional `featured?: boolean` |
| [`lib/newsroom.ts`](lib/newsroom.ts) | New `comparePosts()` — featured first, then date descending. `getAllPosts()` sorts by it; `getLatestPost()` prefers a featured post and falls back to the newest. `toPost()` normalises the frontmatter flag to a boolean |
| [`components/newsroom/PostCard.tsx`](components/newsroom/PostCard.tsx) | Labels for the two new categories — `Record<category, string>` makes this a typecheck error otherwise |
| [`app/newsroom/page.tsx`](app/newsroom/page.tsx) | Render a featured post in its own bordered `FEATURED` block above a `RECENT` grid |

**With no featured post, `/newsroom` falls back to exactly the previous markup**, including the large treatment on the first card. That's the important property — the feature is inert until a post opts in.

## Tests

[`tests/newsroom-featured.test.mjs`](tests/newsroom-featured.test.mjs), 10 cases: no-featured ordering unchanged · a featured post beats a newer one · multiple featured stay date-sorted above the rest · `featured: false` behaves as absent · `getLatestPost` preference and fallback · empty newsroom · removing the flag restores the old result.

Node 20 can't import the TypeScript source and the repo takes no new dependencies, so the comparator is **mirrored** from `lib/newsroom.ts`, following the convention already used in `photo-carousel-distance.test.mjs`. Both sides carry a pointer to the other. Worth knowing this is weaker than testing the real function — if the source comparator changes, the mirror must change with it.

Two cases are **not** mirrors: they read the real MDX frontmatter off disk and assert every `category` is in the union and at most one post is featured. That guards the one failure a mirror can't see — a typo'd category silently falls back to `'announcement'` in `toPost()`.

## Verification

Verified with a temporary post dated **older** than the MARA release and marked featured, so pinning had to beat date order to pass:

- pinned into the `FEATURED` slot above the newer post
- took the home-page `LATEST ANNOUNCEMENT` slot (`getLatestPost()`)
- rendered its `GRANT` category label
- deleting it restored the previous `/newsroom` layout and home slot exactly

Checked in light and dark mode, no console errors. Temp post removed — `content/` is unchanged by this PR.

`npm test` 21/21 (11 existing + 10 new) · `npm run build` clean, 19 routes.

`npm run lint` can't run on `main` yet (no ESLint config — see #6), so the four changed files were linted with a temporary flat config importing `eslint-config-next`: **exit 0**. Merging #6 first makes that workaround unnecessary. No file overlap between the two branches, so they merge cleanly in either order.

## One open question for the reviewer

The spec for this item referenced an approved mock for the `/newsroom` featured layout. **That mock doesn't exist in the source document** — I checked. So the layout here is built to the written description (a bordered `FEATURED` block above a `RECENT` list) using the existing purple accent-bar section idiom. If a different layout was intended, this is the piece to redirect.

Roadmap item 6 (`website-roadmap-2026-Q3.md`, `organization-spec`).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-08-04

[vc]: #hXW3DLAXaYLcTmFiAX5GaUATXhCfguFuxtzaWpHt1Lo=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLTI1Ni1mIiwicHJvamVjdElkIjoicHJqX3h4bkVLbGJrM2RYdlFMbTF2N25JUUN3UkVmT1YiLCJpbnNwZWN0b3JVcmwiOiJodHRwczovL3ZlcmNlbC5jb20vdHlsZXJrc3RldmVucy1wcm9qZWN0cy93ZWJzaXRlLTI1Ni1mL0hUUHE0RTdwUHBHODRrTmI2TDhER0hRQWFVRVgiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS0yNTYtZi1naXQtZmVhdC1uZXdzcm9vbS1mZWF0dXJlZC10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQiLCJsaXZlRmVlZGJhY2siOnsicmVzb2x2ZWQiOjAsInVucmVzb2x2ZWQiOjAsInRvdGFsIjowLCJsaW5rIjoid2Vic2l0ZS0yNTYtZi1naXQtZmVhdC1uZXdzcm9vbS1mZWF0dXJlZC10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAifSwicm9vdERpcmVjdG9yeSI6bnVsbH0seyJuYW1lIjoid2Vic2l0ZSIsInByb2plY3RJZCI6InByal9Ec09RanhuVUtmMGxpQ2pwV3dGRFR3OTRJYXhXIiwicm9vdERpcmVjdG9yeSI6bnVsbCwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtZ2l0LWZlYXQtbmV3c3Jvb20tZmVhdHVyZWQtMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn0sImluc3BlY3RvclVybCI6Imh0dHBzOi8vdmVyY2VsLmNvbS8yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzL3dlYnNpdGUvMm5LYUtkY3JQOXFXRHNEdHo4ZXZXUjhybnRSQiIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWdpdC1mZWF0LW5ld3Nyb29tLWZlYXR1cmVkLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJERVBMT1lFRCJ9XX0=
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| <a href="https://vercel.com/256-foundation-s-projects/website"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_DsOQjxnUKf0liCjpWwFDTw94IaxW&teamId=team_pgQ2VCG6sqTl2vTEjklW5VIp&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website](https://vercel.com/256-foundation-s-projects/website) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website/2nKaKdcrP9qWDsDtz8evWR8rntRB) | [Preview](https://website-git-feat-newsroom-featured-256-foundation-s-projects.vercel.app) | Aug 4, 2026 10:23pm |
| <a href="https://vercel.com/tylerkstevens-projects/website-256-f"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_xxnEKlbk3dXvQLm1v7nIQCwREfOV&teamId=team_pgQ2VCG6sqTl2vTEjklW5VIp&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website-256-f](https://vercel.com/tylerkstevens-projects/website-256-f) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/tylerkstevens-projects/website-256-f/HTPq4E7pPpG84kNb6L8DGHQAaUEX) | [Preview](https://website-256-f-git-feat-newsroom-featured-tylerkstevens-projects.vercel.app) | Aug 4, 2026 10:23pm |
