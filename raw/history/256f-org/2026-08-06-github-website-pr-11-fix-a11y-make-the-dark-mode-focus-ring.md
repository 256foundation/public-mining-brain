# 256foundation/website pull request #11: fix(a11y): make the dark-mode focus ring visible

> Source: https://github.com/256foundation/website/pull/11
> Collected: 2026-10-07
> Published: 2026-08-06

- Repository: 256foundation/website
- Type: pull request
- Number: 11
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-06
- Closed: 2026-08-06
- Labels: none

## Description

## Problem

The sitewide keyboard focus ring is effectively invisible in dark mode — about
**1.4:1** contrast (`#3b1445` on the `#1a1a1a` page background). Dark mode is
the site's primary experience, so this affects most keyboard users on every
focusable element: nav links, buttons, form fields, everything.

## Cause

`app/globals.css` sets the base ring to `#3b1445`, and the only color override
lives inside the **light-mode** block:

```css
:focus-visible { outline: 2px solid #3b1445; outline-offset: 2px; }

@media (prefers-color-scheme: light) {
  :focus-visible { outline-color: #5c2070; }   /* light gets the readable one */
}
```

Light mode is fine. Dark mode has no override, so it falls through to the base
`#3b1445`.

Worth noting for anyone who tries to patch this at the component level: the base
rule is **unlayered**, and unlayered CSS beats every `@layer`. Tailwind
utilities live in `@layer utilities`, so a `dark:focus-visible:outline-*` class
on an element silently does nothing. The fix has to happen here.

## Fix

Adds a dark-mode override next to the base rule, using the design system's
dark accent `#c084d8`. Light mode is untouched. Also comments why the rule is
unlayered so the next person doesn't "clean it up" into a layer.

3 lines of CSS plus comments.

## Verification

Browser, both color schemes, checking computed `outline-color` after the
`transition-colors` animation settles:

| Element | Dark | Light |
|---|---|---|
| `a` (nav link) | `#c084d8` | `#5c2070` |
| `button` | `#c084d8` | — |
| `input[type=text]` | `#c084d8` | — |
| `input[type=email]` | `#c084d8` | — |
| `textarea` | `#c084d8` | — |
| `summary` | `#c084d8` | — |

Reached by real keyboard Tab with `:focus-visible` active, not just
programmatic focus.

`npm run lint` — 0 errors, 7 known `no-img-element` warnings ·
`npm run build` — compiles clean · `npm test` — 21/21 pass

## Comments

### vercel[bot] on 2026-08-06

[vc]: #GlrgDbIWottrNmQDtRJogBTKvbmcabnVhQPoSLXTIPE=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLTI1Ni1mIiwicHJvamVjdElkIjoicHJqX3h4bkVLbGJrM2RYdlFMbTF2N25JUUN3UkVmT1YiLCJpbnNwZWN0b3JVcmwiOiJodHRwczovL3ZlcmNlbC5jb20vdHlsZXJrc3RldmVucy1wcm9qZWN0cy93ZWJzaXRlLTI1Ni1mLzVURWZHdFU4SmV6am1TajluRktrMWpxR1J5OHoiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS0yNTYtZi1naXQtZml4LWRhcmstZm9jdXMtcmluZy10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQiLCJsaXZlRmVlZGJhY2siOnsicmVzb2x2ZWQiOjAsInVucmVzb2x2ZWQiOjAsInRvdGFsIjowLCJsaW5rIjoid2Vic2l0ZS0yNTYtZi1naXQtZml4LWRhcmstZm9jdXMtcmluZy10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAifSwicm9vdERpcmVjdG9yeSI6bnVsbH0seyJuYW1lIjoid2Vic2l0ZSIsInByb2plY3RJZCI6InByal9Ec09RanhuVUtmMGxpQ2pwV3dGRFR3OTRJYXhXIiwicm9vdERpcmVjdG9yeSI6bnVsbCwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtZ2l0LWZpeC1kYXJrLWZvY3VzLXJpbmctMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn0sImluc3BlY3RvclVybCI6Imh0dHBzOi8vdmVyY2VsLmNvbS8yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzL3dlYnNpdGUvNno4WW1qOWtLaHhxVDZ1OW52ODNtY3pQOTNNNyIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWdpdC1maXgtZGFyay1mb2N1cy1yaW5nLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJERVBMT1lFRCJ9XX0=
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| <a href="https://vercel.com/256-foundation-s-projects/website"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_DsOQjxnUKf0liCjpWwFDTw94IaxW&teamId=team_4m4Hz1Tn7d5LJFeztgvbd2CS&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website](https://vercel.com/256-foundation-s-projects/website) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website/6z8Ymj9kKhxqT6u9nv83mczP93M7) | [Preview](https://website-git-fix-dark-focus-ring-256-foundation-s-projects.vercel.app) | Aug 6, 2026 8:40pm |
| <a href="https://vercel.com/tylerkstevens-projects/website-256-f"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_xxnEKlbk3dXvQLm1v7nIQCwREfOV&teamId=team_4m4Hz1Tn7d5LJFeztgvbd2CS&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website-256-f](https://vercel.com/tylerkstevens-projects/website-256-f) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/tylerkstevens-projects/website-256-f/5TEfGtU8JezjmSj9nFKk1jqGRy8z) | [Preview](https://website-256-f-git-fix-dark-focus-ring-tylerkstevens-projects.vercel.app) | Aug 6, 2026 8:40pm |
