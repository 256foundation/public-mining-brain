# 256foundation/website pull request #10: feat(projects): Fund This Project CTA on pillar pages (roadmap item 4)

> Source: https://github.com/256foundation/website/pull/10
> Collected: 2026-10-07
> Published: 2026-08-06

- Repository: 256foundation/website
- Type: pull request
- Number: 10
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-06
- Closed: 2026-08-06
- Labels: none

## Description

## What

Adds a `Fund This Project →` button to the hero of all four pillar detail pages
(`/projects/ember-one`, `/projects/mujina`, `/projects/libre-board`,
`/projects/hydrapool`). It is the first item in the hero button row, ahead of
GitHub and Forum, and links to `/donate`.

Roadmap item 4.

## Why

The pillar pages had no donate CTA in the page body — the only path was the
global `Donate` button in the site header. This is a conversion fix: someone
reading about a project now has a direct next step without scrolling back up.

**Scope note:** this is a plain link to the existing `/donate` page. It does not
carry any per-project identifier and does not attribute donations to a project.
How to track per-project funding is a separate decision and will be handled as
its own change.

## How

Uses the existing `components/ui/Button` primitive (`variant="primary"`,
`size="md"`) rather than hand-rolled classes. That variant already matches the
design system — square corners, purple `#3b1445`, Space Mono — and its `md`
padding (`px-5 py-2.5`) is identical to the neighboring GitHub/Forum buttons, so
the row stays aligned. Label uses `&rarr;`, not a chevron.

Diff is 4 added lines plus the import.

## Verification

- `npm run lint` — 0 errors, 7 known `no-img-element` warnings
- `npm run build` — compiles clean, all 4 slugs prerender
- `npm test` — 21/21 pass
- Browser: button confirmed present and first-in-row on all four pages, in both
  light and dark mode; keyboard-reachable via Tab with `:focus-visible` active;
  click navigates to `/donate`

## Known issue, not introduced here

`app/globals.css:150` sets `:focus-visible { outline: 2px solid #3b1445 }`
unlayered, so it overrides every Tailwind focus utility sitewide. The matching
`#5c2070` override at `app/globals.css:274` is inside a
`@media (prefers-color-scheme: light)` block, so dark mode falls through to
`#3b1445` on a `#1a1a1a` background — a near-invisible focus ring on every
focusable element on the site.

This button inherits that behavior; it does not cause it. Left alone here to
keep the branch scoped — worth its own change.

## Comments

### vercel[bot] on 2026-08-06

[vc]: #hzmXVDepbt65PHKLth0o9VCgzvwGsZoYpfuTQoEGo3M=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLTI1Ni1mIiwicHJvamVjdElkIjoicHJqX3h4bkVLbGJrM2RYdlFMbTF2N25JUUN3UkVmT1YiLCJsaXZlRmVlZGJhY2siOnsicmVzb2x2ZWQiOjAsInVucmVzb2x2ZWQiOjAsInRvdGFsIjowLCJsaW5rIjoid2Vic2l0ZS0yNTYtZi1naXQtZmVhdC1waWxsYXItZG9uYXRlLWN0YS10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAifSwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tL3R5bGVya3N0ZXZlbnMtcHJvamVjdHMvd2Vic2l0ZS0yNTYtZi82M2VNVXFlMkc2V1dCZEVjR29hektQb0tLaHZkIiwicHJldmlld1VybCI6IndlYnNpdGUtMjU2LWYtZ2l0LWZlYXQtcGlsbGFyLWRvbmF0ZS1jdGEtdHlsZXJrc3RldmVucy1wcm9qZWN0cy52ZXJjZWwuYXBwIiwibmV4dENvbW1pdFN0YXR1cyI6IkRFUExPWUVEIn1dfQ==
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| <a href="https://vercel.com/tylerkstevens-projects/website-256-f"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_xxnEKlbk3dXvQLm1v7nIQCwREfOV&teamId=team_pgQ2VCG6sqTl2vTEjklW5VIp&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website-256-f](https://vercel.com/tylerkstevens-projects/website-256-f) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/tylerkstevens-projects/website-256-f/63eMUqe2G6WWBdEcGoazKPoKKhvd) | [Preview](https://website-256-f-git-feat-pillar-donate-cta-tylerkstevens-projects.vercel.app) | Aug 6, 2026 8:32pm |
