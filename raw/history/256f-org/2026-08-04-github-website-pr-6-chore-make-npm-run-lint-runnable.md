# 256foundation/website pull request #6: chore: make npm run lint runnable

> Source: https://github.com/256foundation/website/pull/6
> Collected: 2026-10-07
> Published: 2026-08-04

- Repository: 256foundation/website
- Type: pull request
- Number: 6
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-04
- Closed: 2026-08-05
- Labels: none

## Description

`npm run lint` has never been able to complete in this repo. There is no ESLint config file, so `next lint` drops into its interactive *"How would you like to configure ESLint?"* setup prompt and hangs. Reproduced on a clean tree, so this is pre-existing — not a regression from any branch.

Consequence: the pre-PR check of lint + build + test could not pass, and lint has effectively never run locally or in CI.

## The fix

- Add [`eslint.config.mjs`](eslint.config.mjs) — flat config (ESLint 9), spreading the array `eslint-config-next` already exports. It ships its own ignores for `.next/`, `out/`, `build/` and `next-env.d.ts`, so those aren't repeated.
- Switch the `lint` script from `next lint` to `eslint .`. `next lint` is deprecated and is **removed entirely in Next 16**, so this is needed regardless.

No new dependencies — `eslint` and `eslint-config-next` were already in `devDependencies`.

## What lint then found

4 errors from 3 root causes, all pre-existing:

| Issue | Resolution |
|---|---|
| [`AnnouncementBanner.tsx`](components/layout/AnnouncementBanner.tsx) declared its `LinkOrA` wrapper **inside** the render | **Real bug** — the component got a new identity on every render, remounting the banner contents and resetting their state. Hoisted to module scope as `BannerLink`. |
| `AnnouncementBanner` and [`CountdownTimer.tsx`](components/telehash/CountdownTimer.tsx) call `setState` in a mount effect | Both are deliberate hydration guards — `localStorage` and the client clock don't exist during SSR. Each gets a targeted `eslint-disable-next-line` with the reason inline. **The rule stays at error strength for new code.** |
| [`Logo.tsx`](components/ui/Logo.tsx) carried a disable for a rule that no longer fires | Stale — `<img>` inside `<picture>` isn't flagged. Removed. |

7 `@next/next/no-img-element` **warnings** remain and do not fail the run. Several are intentional (remote Nostr avatars, supporter logos); converting them to `next/image` is a separate decision.

## Verification

`npm run lint && npm run build && npm test` now passes end to end — first time that's true in this repo.

- lint exit 0 (7 warnings, 0 errors) · build clean, 19 routes · tests 11/11
- `tsc` caught a mistake lint missed: the first pass replaced the `LinkOrA` usages but left the dead definition behind. Lint stayed green, the build failed. Fixed and re-verified.
- Both touched components render from `null` data (`activeAnnouncement` and `nextEventDate` are both `null`), so neither is reachable as shipped. I temporarily activated each rather than assume they were fine: internal **and** external banner branches (external correctly gets `target="_blank"` + `rel="noopener noreferrer"`), dismiss writes `localStorage` and hides the banner, and the countdown ticks after hydration. Both temp edits reverted — `data/` is untouched.

Recommend merging this before the other open branches so they inherit a working lint.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-08-04

[vc]: #r4mRAiFonU16EyKDbj500xf4KKUY7RopTeMCSlCnfbQ=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLTI1Ni1mIiwicHJvamVjdElkIjoicHJqX3h4bkVLbGJrM2RYdlFMbTF2N25JUUN3UkVmT1YiLCJpbnNwZWN0b3JVcmwiOiJodHRwczovL3ZlcmNlbC5jb20vdHlsZXJrc3RldmVucy1wcm9qZWN0cy93ZWJzaXRlLTI1Ni1mL0U5cVhSbjNUVXNRWkhDVmVESlFXUUtBUFpnNmQiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS0yNTYtZi1naXQtY2hvcmUtZXNsaW50LWZsLWU2ZTFlNi10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQiLCJsaXZlRmVlZGJhY2siOnsicmVzb2x2ZWQiOjAsInVucmVzb2x2ZWQiOjAsInRvdGFsIjowLCJsaW5rIjoid2Vic2l0ZS0yNTYtZi1naXQtY2hvcmUtZXNsaW50LWZsLWU2ZTFlNi10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAifSwicm9vdERpcmVjdG9yeSI6bnVsbH0seyJuYW1lIjoid2Vic2l0ZSIsInByb2plY3RJZCI6InByal9Ec09RanhuVUtmMGxpQ2pwV3dGRFR3OTRJYXhXIiwicm9vdERpcmVjdG9yeSI6bnVsbCwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtZ2l0LWNob3JlLWVzbGludC1mbGF0LWNvbmZpZy0yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzLnZlcmNlbC5hcHAifSwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tLzI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMvd2Vic2l0ZS8zV3Z2MkN4MlpMaXlVeHZoR2FtdTFSRTd4QW8yIiwicHJldmlld1VybCI6IndlYnNpdGUtZ2l0LWNob3JlLWVzbGludC1mbGF0LWNvbmZpZy0yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQifV19
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| <a href="https://vercel.com/256-foundation-s-projects/website"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_DsOQjxnUKf0liCjpWwFDTw94IaxW&teamId=team_pgQ2VCG6sqTl2vTEjklW5VIp&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website](https://vercel.com/256-foundation-s-projects/website) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website/3Wvv2Cx2ZLiyUxvhGamu1RE7xAo2) | [Preview](https://website-git-chore-eslint-flat-config-256-foundation-s-projects.vercel.app) | Aug 4, 2026 10:22pm |
| <a href="https://vercel.com/tylerkstevens-projects/website-256-f"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_xxnEKlbk3dXvQLm1v7nIQCwREfOV&teamId=team_pgQ2VCG6sqTl2vTEjklW5VIp&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website-256-f](https://vercel.com/tylerkstevens-projects/website-256-f) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/tylerkstevens-projects/website-256-f/E9qXRn3TUsQZHCVeDJQWQKAPZg6d) | [Preview](https://website-256-f-git-chore-eslint-fl-e6e1e6-tylerkstevens-projects.vercel.app) | Aug 4, 2026 10:22pm |
