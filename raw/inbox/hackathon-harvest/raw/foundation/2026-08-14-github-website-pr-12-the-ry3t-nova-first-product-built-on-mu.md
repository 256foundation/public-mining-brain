# 256foundation/website pull request #12: The RY3T Nova: first product built on Mujina

> Source: https://github.com/256foundation/website/pull/12
> Collected: 2026-10-07
> Published: 2026-08-14

- Repository: 256foundation/website
- Type: pull request
- Number: 12
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-14
- Closed: 2026-08-14
- Labels: none

## Description

Publishes the newsroom announcement for the RY3T Nova, the first commercial product built on Mujina. Reviewed and approved by RY3T (via Schnitzel) prior to publication.

## Content

- Adds `content/newsroom/ry3t-nova.mdx`, restructured around the community proof-point: RY3T took the GPLv3 code and shipped a product without needing permission.
- Neutral treatment of the closed-firmware landscape rather than competitor call-outs.
- Foundation mission lands at the end as payoff, after the technical proof.
- Marked `featured: true`, so it takes the home-page slot.
- All RY3T links point at `https://nova.ry3t.com/en/` per RY3T's one requested change.

## Assets

- Hero photo, plus both of Schnitzel's demo screenshots.
- Custom OG image compositing RY3T's original with the Mujina mark set in Bridge Officer, the project's real brand typeface.

## Site changes

- Post covers now render at their own aspect ratio instead of a fixed `h-64` box with `object-contain`, which letterboxed anything that didn't match. Cover art varies widely (3:1 banner vs 3:2 photo), so no single fixed box works.
- New `lib/imageSize.ts` reads intrinsic dimensions from PNG/JPEG/WebP headers at build time. No new dependencies; returns `null` on anything unreadable and the page falls back to the previous fixed box.
- Newsroom index drops the featured hero and the Featured/Recent headings; every post renders in one uniform grid. `featured` now only pins to the home page.

## Verification

- `npm test` 21/21, `npm run lint` 0 errors, `npm run build` compiles and prerenders `/newsroom/ry3t-nova`.
- Image parser checked against all five real assets plus missing-file and relative-path cases.
- Both post pages confirmed in-browser: covers full-width and uncropped, all images 200, OG meta resolving to the new composite.
- All four RY3T links verified resolving (200).

## Known issue, not addressed here

Post dates render one day early for viewers west of UTC (`formatPostDate` parses date-only strings as UTC midnight, then formats in local time). This article will display "August 6, 2026" despite its `2026-08-07` frontmatter. Pre-existing and affects every post; tracked separately.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-08-14

[vc]: #qUmyk8IQ7yQJT0AdbTfjVbJfYpFMmC3l7utdTfDRfJE=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLTI1Ni1mIiwicHJvamVjdElkIjoicHJqX3h4bkVLbGJrM2RYdlFMbTF2N25JUUN3UkVmT1YiLCJpbnNwZWN0b3JVcmwiOiJodHRwczovL3ZlcmNlbC5jb20vdHlsZXJrc3RldmVucy1wcm9qZWN0cy93ZWJzaXRlLTI1Ni1mL2RSRkZxa3Y3Sms2YzQ4d2NuODlxekpEOTNSMlEiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS0yNTYtZi1naXQtY29udGVudC1yeTN0LW5vdmEtdHlsZXJrc3RldmVucy1wcm9qZWN0cy52ZXJjZWwuYXBwIiwibmV4dENvbW1pdFN0YXR1cyI6IkRFUExPWUVEIiwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtMjU2LWYtZ2l0LWNvbnRlbnQtcnkzdC1ub3ZhLXR5bGVya3N0ZXZlbnMtcHJvamVjdHMudmVyY2VsLmFwcCJ9LCJyb290RGlyZWN0b3J5IjpudWxsfSx7Im5hbWUiOiJ3ZWJzaXRlIiwicHJvamVjdElkIjoicHJqX0RzT1FqeG5VS2YwbGlDanBXd0ZEVHc5NElheFciLCJyb290RGlyZWN0b3J5IjpudWxsLCJsaXZlRmVlZGJhY2siOnsicmVzb2x2ZWQiOjAsInVucmVzb2x2ZWQiOjAsInRvdGFsIjowLCJsaW5rIjoid2Vic2l0ZS1naXQtY29udGVudC1yeTN0LW5vdmEtMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn0sImluc3BlY3RvclVybCI6Imh0dHBzOi8vdmVyY2VsLmNvbS8yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzL3dlYnNpdGUvRkY4a01EWnA3c0FlZTdjOG9VMXJTZHphYmN1aSIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWdpdC1jb250ZW50LXJ5M3Qtbm92YS0yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQifV19
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| <a href="https://vercel.com/256-foundation-s-projects/website"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_DsOQjxnUKf0liCjpWwFDTw94IaxW&teamId=team_4m4Hz1Tn7d5LJFeztgvbd2CS&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website](https://vercel.com/256-foundation-s-projects/website) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website/FF8kMDZp7sAee7c8oU1rSdzabcui) | [Preview](https://website-git-content-ry3t-nova-256-foundation-s-projects.vercel.app) | Aug 14, 2026 8:39pm |
| <a href="https://vercel.com/tylerkstevens-projects/website-256-f"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_xxnEKlbk3dXvQLm1v7nIQCwREfOV&teamId=team_4m4Hz1Tn7d5LJFeztgvbd2CS&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website-256-f](https://vercel.com/tylerkstevens-projects/website-256-f) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/tylerkstevens-projects/website-256-f/dRFFqkv7Jk6c48wcn89qzJD93R2Q) | [Preview](https://website-256-f-git-content-ry3t-nova-tylerkstevens-projects.vercel.app) | Aug 14, 2026 8:39pm |
