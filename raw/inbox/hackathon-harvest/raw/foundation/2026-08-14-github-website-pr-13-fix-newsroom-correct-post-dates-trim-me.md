# 256foundation/website pull request #13: fix(newsroom): correct post dates, trim meta tags, open outbound links in new tabs

> Source: https://github.com/256foundation/website/pull/13
> Collected: 2026-10-07
> Published: 2026-08-14

- Repository: 256foundation/website
- Type: pull request
- Number: 13
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-14
- Closed: 2026-08-14
- Labels: none

## Description

Three fixes to the live newsroom, following the RY3T Nova publish.

## Post dates rendered a day early

`new Date('2026-08-14')` parses a date-only string as UTC midnight, and `toLocaleDateString` then formatted it in the viewer's local zone — shifting the day back for everyone west of UTC.

This was visible in production: the RY3T Nova post showed **August 13** and the MARA post showed **April 28**, a day off from the event it describes. Fixed by formatting in UTC, which pins the authored calendar date.

`tests/newsroom-date.test.mjs` covers it: four timezones on both sides of UTC, month boundaries, malformed input, plus a check that reads the real MDX frontmatter off disk so a post can never silently publish on the wrong day.

## Meta tags over the truncation limits

Flagged by an Open Graph inspector — title 65 chars against a ~60 budget, description 200 against ~160.

Adds an optional `seoTitle` frontmatter field used only by `<title>`/`og:title`. The on-page headline stays exactly as approved ("The RY3T Nova: The First Product Built on Mujina") while search and social get a 57-char version. The excerpt drops to 144 chars, which also reads better in the two-line clamp on post cards.

## Outbound links stayed in the same tab

Posts lean on external references (project sites, GitHub, Schnitzel's X threads) and every one navigated readers away mid-article. External links now carry `target="_blank"` and `rel="noopener noreferrer"`; in-site links and `mailto:` are untouched.

## Verification

- `npm test` 26/26 (up from 21), `npm run lint` 0 errors, `npm run build` compiles.
- Browser-verified on both posts: RY3T Nova now reads "August 14, 2026", MARA reads "April 29, 2026".
- 15/15 external links open in a new tab; all 6 in-site links unchanged.
- Title 57 chars, description 144 chars, `<h1>` unchanged.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-08-14

[vc]: #YMi9LLWqB3Ndl4pN1f7ayzgnsSzUspFwyBOrUPLYOFE=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlIiwicHJvamVjdElkIjoicHJqX0RzT1FqeG5VS2YwbGlDanBXd0ZEVHc5NElheFciLCJyb290RGlyZWN0b3J5IjpudWxsLCJpbnNwZWN0b3JVcmwiOiJodHRwczovL3ZlcmNlbC5jb20vMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy93ZWJzaXRlL0dhb0VxUWZNUE44QkpBcml4NkV0bUUxTXVITmYiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS1naXQtZml4LW5ld3Nyb29tLWRhdGUtZjhlNTVlLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJERVBMT1lFRCIsImxpdmVGZWVkYmFjayI6eyJyZXNvbHZlZCI6MCwidW5yZXNvbHZlZCI6MCwidG90YWwiOjAsImxpbmsiOiJ3ZWJzaXRlLWdpdC1maXgtbmV3c3Jvb20tZGF0ZS1mOGU1NWUtMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn19LHsibmFtZSI6IndlYnNpdGUtMjU2LWYiLCJwcm9qZWN0SWQiOiJwcmpfeHhuRUtsYmszZFh2UUxtMXY3bklRQ3dSRWZPViIsImluc3BlY3RvclVybCI6Imh0dHBzOi8vdmVyY2VsLmNvbS90eWxlcmtzdGV2ZW5zLXByb2plY3RzL3dlYnNpdGUtMjU2LWYvQ1A3RWdraVpuODJEdGRWU0NVN1FYblRCRFN0NyIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLTI1Ni1mLWdpdC1maXgtbmV3c3Jvb20tZGEtYTU1M2ViLXR5bGVya3N0ZXZlbnMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJERVBMT1lFRCIsImxpdmVGZWVkYmFjayI6eyJyZXNvbHZlZCI6MCwidW5yZXNvbHZlZCI6MCwidG90YWwiOjAsImxpbmsiOiJ3ZWJzaXRlLTI1Ni1mLWdpdC1maXgtbmV3c3Jvb20tZGEtYTU1M2ViLXR5bGVya3N0ZXZlbnMtcHJvamVjdHMudmVyY2VsLmFwcCJ9LCJyb290RGlyZWN0b3J5IjpudWxsfV19
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| <a href="https://vercel.com/256-foundation-s-projects/website"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_DsOQjxnUKf0liCjpWwFDTw94IaxW&teamId=team_4m4Hz1Tn7d5LJFeztgvbd2CS&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website](https://vercel.com/256-foundation-s-projects/website) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website/GaoEqQfMPN8BJArix6EtmE1MuHNf) | [Preview](https://website-git-fix-newsroom-date-f8e55e-256-foundation-s-projects.vercel.app) | Aug 14, 2026 8:55pm |
| <a href="https://vercel.com/tylerkstevens-projects/website-256-f"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_xxnEKlbk3dXvQLm1v7nIQCwREfOV&teamId=team_4m4Hz1Tn7d5LJFeztgvbd2CS&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website-256-f](https://vercel.com/tylerkstevens-projects/website-256-f) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/tylerkstevens-projects/website-256-f/CP7EgkiZn82DtdVSCU7QXnTBDSt7) | [Preview](https://website-256-f-git-fix-newsroom-da-a553eb-tylerkstevens-projects.vercel.app) | Aug 14, 2026 8:55pm |
