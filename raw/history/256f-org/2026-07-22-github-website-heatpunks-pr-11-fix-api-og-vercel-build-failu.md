# 256foundation/website-heatpunks pull request #11: Fix /api/og Vercel build failure: move off Edge runtime

> Source: https://github.com/256foundation/website-heatpunks/pull/11
> Collected: 2026-10-07
> Published: 2026-07-22

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 11
- State: closed
- Author: tylerkstevens
- Opened: 2026-07-22
- Closed: 2026-07-22
- Labels: none

## Description

## Summary

Since the OG/metadata overhaul (#9) merged, **every production build has actually been failing on Vercel**, so the live site kept silently serving the old pre-overhaul build. The error:

> **Build Failed:** The Edge Function "api/og" size is 1.03 MB and your plan size limit is 1 MB.

- `@vercel/og`'s own Satori/Resvg WASM core is already close to 1 MB before any custom fonts are added — bundling two JetBrains Mono TTFs (~530 KB) plus the logo pushed `/api/og` over Vercel's **Edge** Function size cap.
- Fix: drop `export const runtime = 'edge'` (Node.js Serverless Functions have a far larger size ceiling, and `next/og`'s `ImageResponse` has supported the Node.js runtime since Next 14).
- The Edge-only `fetch(new URL(..., import.meta.url))` asset-loading pattern doesn't resolve under Node, so it's swapped for `fs.readFileSync(join(process.cwd(), ...))`, read once at module scope (a bonus: no longer re-reads/re-fetches fonts on every request).
- Updated `SPEC-og-metadata.md` with a correction note documenting this.

## Test plan
- [x] `npm run lint` clean
- [x] Production build's own file trace (`route.js.nft.json`) shows a ~3.1 MB bundle for `/api/og` — comfortably inside Node's function size limit (vs. Edge's 1 MB)
- [x] Rendered `/api/og?card=summit` locally post-fix and screenshotted — pixel-identical to the pre-fix Edge-runtime render, no console/server errors

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-07-22

[vc]: #CMm8cHuL/zsM3PwEKkUHys3QOh2romP8eIbNMKUcJwo=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLWhlYXRwdW5rcyIsInByb2plY3RJZCI6InByal9JM0FDajFucFFjb013UjdrcGcySlJRUENteVZQIiwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tLzI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMvd2Vic2l0ZS1oZWF0cHVua3MvRTJqTHJhR2lBVzJ6VzJ1a2pBV2VXZjdwNG5aNiIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWhlYXRwdW5rcy1naXQtZml4LW9nLWUtYWNjZDQ2LTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJQRU5ESU5HIiwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtaGVhdHB1bmtzLWdpdC1maXgtb2ctZS1hY2NkNDYtMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn19XX0=
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| [website-heatpunks](https://vercel.com/256-foundation-s-projects/website-heatpunks) | ![Building](https://vercel.com/static/status/building.svg) [Building](https://vercel.com/256-foundation-s-projects/website-heatpunks/E2jLraGiAW2zW2ukjAWeWf7p4nZ6) | [Preview](https://website-heatpunks-git-fix-og-e-accd46-256-foundation-s-projects.vercel.app), [Comment](https://vercel.live/open-feedback/website-heatpunks-git-fix-og-e-accd46-256-foundation-s-projects.vercel.app?via=pr-comment-feedback-link) | Jul 22, 2026 4:29pm |
