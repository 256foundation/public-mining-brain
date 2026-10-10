# 256foundation/website pull request #4: chore: allow the dev server to pick a free port

> Source: https://github.com/256foundation/website/pull/4
> Collected: 2026-10-07
> Published: 2026-08-04

- Repository: 256foundation/website
- Type: pull request
- Number: 4
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-04
- Closed: 2026-08-04
- Labels: none

## Description

Adds `"autoPort": true` to the Next.js Dev launch config so the preview falls back to another port when 3000 is occupied, instead of failing to start.

Verified: config still parses, server boots clean on 3000 when free, `/` and `/api/hashdash` both return 200.

Local tooling only — no application code, no site behavior change.

## Comments

### vercel[bot] on 2026-08-04

[vc]: #MI2GRYVeXfRcD/KdeUDMqd9S8eE9CaXx5FKsjONStHM=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLTI1Ni1mIiwicHJvamVjdElkIjoicHJqX3h4bkVLbGJrM2RYdlFMbTF2N25JUUN3UkVmT1YiLCJpbnNwZWN0b3JVcmwiOiJodHRwczovL3ZlcmNlbC5jb20vdHlsZXJrc3RldmVucy1wcm9qZWN0cy93ZWJzaXRlLTI1Ni1mL0hHWTRRYk1vUTRuUTNhN3N2NHFCS2dpZ0ZYdUwiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS0yNTYtZi1naXQtY2hvcmUtbGF1bmNoLWpzLTZkMTc4Ni10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQiLCJsaXZlRmVlZGJhY2siOnsicmVzb2x2ZWQiOjAsInVucmVzb2x2ZWQiOjAsInRvdGFsIjowLCJsaW5rIjoid2Vic2l0ZS0yNTYtZi1naXQtY2hvcmUtbGF1bmNoLWpzLTZkMTc4Ni10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAifSwicm9vdERpcmVjdG9yeSI6bnVsbH0seyJuYW1lIjoid2Vic2l0ZSIsInByb2plY3RJZCI6InByal9Ec09RanhuVUtmMGxpQ2pwV3dGRFR3OTRJYXhXIiwicm9vdERpcmVjdG9yeSI6bnVsbCwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtZ2l0LWNob3JlLWxhdW5jaC1qc29uLWMyY2E1ZS0yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzLnZlcmNlbC5hcHAifSwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tLzI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMvd2Vic2l0ZS9BanlyMXVkWWdiMWR3QVhkbURoVjhzWnFqY3E5IiwicHJldmlld1VybCI6IndlYnNpdGUtZ2l0LWNob3JlLWxhdW5jaC1qc29uLWMyY2E1ZS0yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQifV19
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| <a href="https://vercel.com/256-foundation-s-projects/website"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_DsOQjxnUKf0liCjpWwFDTw94IaxW&teamId=team_pgQ2VCG6sqTl2vTEjklW5VIp&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website](https://vercel.com/256-foundation-s-projects/website) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website/Ajyr1udYgb1dwAXdmDhV8sZqjcq9) | [Preview](https://website-git-chore-launch-json-c2ca5e-256-foundation-s-projects.vercel.app) | Aug 4, 2026 6:23pm |
| <a href="https://vercel.com/tylerkstevens-projects/website-256-f"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_xxnEKlbk3dXvQLm1v7nIQCwREfOV&teamId=team_pgQ2VCG6sqTl2vTEjklW5VIp&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website-256-f](https://vercel.com/tylerkstevens-projects/website-256-f) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/tylerkstevens-projects/website-256-f/HGY4QbMoQ4nQ3a7sv4qBKgigFXuL) | [Preview](https://website-256-f-git-chore-launch-js-6d1786-tylerkstevens-projects.vercel.app) | Aug 4, 2026 6:23pm |
