# 256foundation/website pull request #8: copy: adopt "Core Contributor" terminology (roadmap item 2)

> Source: https://github.com/256foundation/website/pull/8
> Collected: 2026-10-07
> Published: 2026-08-05

- Repository: 256foundation/website
- Type: pull request
- Number: 8
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-05
- Closed: 2026-08-05
- Labels: none

## Description

Replaces "Lead Engineer" with core-contributor language across the site, and gives the board cards their actual offices. Roadmap item 2 in `website-roadmap-2026-Q3.md`.

## What changed

**Pillar project role labels** — `data/projects.ts`: the four `role: 'Lead Engineer'` entries are now `role: 'Core Contributor'`. "Core Contributor" is standard open-source usage and signals primary-developer status without implying employment, which the funding relationship is not. The four `'Project Manager'` entries are unchanged.

**Board cards** — `data/team.ts`: board roles are now the offices held — Tyler Stevens President, Skot Secretary, Joe Wood Treasurer. These cards describe board positions only, so Skot's card no longer doubles as a project role; his bio keeps the Ember One work without a role label.

**Prose** — the Bitaxe passage on `/projects/ember-one` and the P2Pool V2 passage on `/projects/hydrapool` now describe Skot and Jungly as core contributors. In `content/newsroom/mara-foundation-tier1-supporter.mdx`, Schnitzel is "a core contributor on Libre Board" — narrowed from the previous foundation-wide phrasing, which named the project rather than implying the foundation has engineers.

Type keys (`team.leadEngineer`, `TeamMember`) are internal and not user-visible, so they are deliberately left alone; renaming them is tracked as optional cleanup elsewhere.

## Verification

- `grep -rn "Lead Engineer\|lead engineer" app components data types content lib tests` returns nothing.
- `npm run lint` — 0 errors, 7 known `@next/next/no-img-element` warnings.
- `npm run build` — clean, 19 routes prerendered. `npm test` — 21/21 pass.
- Fetched all four pillar routes and counted occurrences: each renders "Core Contributor", zero "Lead Engineer".
- Screenshotted in both light and dark mode: all four pillar team sections, the `/mission` board cards with the three offices, both reworded prose passages, and the DOOMAXE paragraph in the MARA release.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-08-05

[vc]: #+4XAoFCE/siDcSMOkpy/gtA/9Twwm5KsslHxNE5nYTU=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLTI1Ni1mIiwicHJvamVjdElkIjoicHJqX3h4bkVLbGJrM2RYdlFMbTF2N25JUUN3UkVmT1YiLCJpbnNwZWN0b3JVcmwiOiJodHRwczovL3ZlcmNlbC5jb20vdHlsZXJrc3RldmVucy1wcm9qZWN0cy93ZWJzaXRlLTI1Ni1mLzRnQTFHZTl6aXhFc1N3ZTFYU2tpZmpDbXR6a1giLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS0yNTYtZi1naXQtY29weS1jb3JlLWNvbnRyLTkzMGRkOS10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQiLCJsaXZlRmVlZGJhY2siOnsicmVzb2x2ZWQiOjAsInVucmVzb2x2ZWQiOjAsInRvdGFsIjowLCJsaW5rIjoid2Vic2l0ZS0yNTYtZi1naXQtY29weS1jb3JlLWNvbnRyLTkzMGRkOS10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAifSwicm9vdERpcmVjdG9yeSI6bnVsbH0seyJuYW1lIjoid2Vic2l0ZSIsInByb2plY3RJZCI6InByal9Ec09RanhuVUtmMGxpQ2pwV3dGRFR3OTRJYXhXIiwicm9vdERpcmVjdG9yeSI6bnVsbCwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtZ2l0LWNvcHktY29yZS1jb250cmlidS02MDNhZGUtMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn0sImluc3BlY3RvclVybCI6Imh0dHBzOi8vdmVyY2VsLmNvbS8yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzL3dlYnNpdGUvSFR3UTcyb3FUMTl2Z1NyTXlLUmd0SlFwUUhReiIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWdpdC1jb3B5LWNvcmUtY29udHJpYnUtNjAzYWRlLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJERVBMT1lFRCJ9XX0=
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| <a href="https://vercel.com/256-foundation-s-projects/website"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_DsOQjxnUKf0liCjpWwFDTw94IaxW&teamId=team_pgQ2VCG6sqTl2vTEjklW5VIp&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website](https://vercel.com/256-foundation-s-projects/website) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website/HTwQ72oqT19vgSrMyKRgtJQpQHQz) | [Preview](https://website-git-copy-core-contribu-603ade-256-foundation-s-projects.vercel.app) | Aug 5, 2026 8:30pm |
| <a href="https://vercel.com/tylerkstevens-projects/website-256-f"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_xxnEKlbk3dXvQLm1v7nIQCwREfOV&teamId=team_pgQ2VCG6sqTl2vTEjklW5VIp&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website-256-f](https://vercel.com/tylerkstevens-projects/website-256-f) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/tylerkstevens-projects/website-256-f/4gA1Ge9zixEsSwe1XSkifjCmtzkX) | [Preview](https://website-256-f-git-copy-core-contr-930dd9-tylerkstevens-projects.vercel.app) | Aug 5, 2026 8:30pm |
