# 256foundation/website pull request #9: feat: use Bridge Officer wordmark for Mujina; refine tagline

> Source: https://github.com/256foundation/website/pull/9
> Collected: 2026-10-07
> Published: 2026-08-06

- Repository: 256foundation/website
- Type: pull request
- Number: 9
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-06
- Closed: 2026-08-06
- Labels: none

## Description

## What changed

**Bridge Officer wordmark for Mujina**
- Adds the Bridge Officer (Iconian Fonts) typeface, self-hosted at `public/fonts/bridge-officer.woff2`, via `@font-face` + a `.font-bridge-officer` utility that falls back to `var(--font-display)`.
- New optional `titleFont` field on `PillarProject`, set only on Mujina — so this is a one-line data change if another project ever gets a brand face.
- Applied to two headers: the project detail hero `<h1>` and the pillar card `<h3>` on `/projects`. Deliberately **not** applied to small text (home `ProjectsSection` card title at 16px, grant log table, taglines, body prose).

**Tagline copy**
- "The Linux kernel **of** Bitcoin mining firmware" → "The Linux kernel **project** of Bitcoin mining firmware". Mujina isn't a kernel, but occupies the kernel project's role in the mining ecosystem. Data-driven, so it propagates to all render sites.

## Note on the lowercase rendering

The supplied woff2 is a **6-glyph subset containing only lowercase `a i j m n u`** — verified with fontTools. There is no capital `M`, so these titles render lowercase `mujina`; `uppercase` would silently fall back to Barlow Condensed for every character. Font + case selection is centralized in `lib/projectTitle.ts` with that constraint documented. Swapping in a fuller font file later is a file drop plus one line.

This means the Mujina card on `/projects` reads lowercase next to its three uppercase siblings — intentional branding, but a visible inconsistency worth a second opinion.

## Verification

- `npm run build` — clean, all 4 `/projects/[slug]` routes prerender
- `npx tsc --noEmit` — clean
- `npm run lint` — 0 errors (7 pre-existing `<img>` warnings elsewhere)
- Confirmed real glyphs in use, not fallback: `"Bridge Officer", monospace` measures 235.1px vs 173.4px for a nonexistent font on the same string
- Confirmed the other three projects still render `font-display uppercase`
- Fetched served HTML for `/`, `/projects`, `/projects/mujina`: **0** occurrences of the old tagline remain

## Licensing — needs your confirmation

Iconian fonts are distributed free for **personal** use; embedding on an organization's public site generally requires a license from Iconian. Please confirm 256 Foundation has that before this reaches production.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-08-06

[vc]: #vfm+xpkHXALiHGA4HGEtFuHKRneieJxb3pk4kilrvdc=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLTI1Ni1mIiwicHJvamVjdElkIjoicHJqX3h4bkVLbGJrM2RYdlFMbTF2N25JUUN3UkVmT1YiLCJpbnNwZWN0b3JVcmwiOiJodHRwczovL3ZlcmNlbC5jb20vdHlsZXJrc3RldmVucy1wcm9qZWN0cy93ZWJzaXRlLTI1Ni1mLzlmTFV0QW45a1NVRUh4emdBb0MyV2JtVGp4UVoiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS0yNTYtZi1naXQtc3R5bGUtZm9udC11cGRhdGVzLXR5bGVya3N0ZXZlbnMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJQRU5ESU5HIiwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtMjU2LWYtZ2l0LXN0eWxlLWZvbnQtdXBkYXRlcy10eWxlcmtzdGV2ZW5zLXByb2plY3RzLnZlcmNlbC5hcHAifX1dfQ==
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| <a href="https://vercel.com/tylerkstevens-projects/website-256-f"><sup><img src="https://vercel.com/api/www/avatar?projectId=prj_xxnEKlbk3dXvQLm1v7nIQCwREfOV&teamId=team_pgQ2VCG6sqTl2vTEjklW5VIp&s=32" width="16" height="16" align="middle" alt="" /></sup></a> [website-256-f](https://vercel.com/tylerkstevens-projects/website-256-f) | ![Building](https://vercel.com/static/status/building.svg) [Building](https://vercel.com/tylerkstevens-projects/website-256-f/9fLUtAn9kSUEHxzgAoC2WbmTjxQZ) | [Preview](https://website-256-f-git-style-font-updates-tylerkstevens-projects.vercel.app) | Aug 6, 2026 7:49pm |
