# 256foundation/website-heatpunks pull request #10: Clean up stale admin@heatpunks.org doc references

> Source: https://github.com/256foundation/website-heatpunks/pull/10
> Collected: 2026-10-07
> Published: 2026-07-22

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 10
- State: closed
- Author: tylerkstevens
- Opened: 2026-07-22
- Closed: 2026-07-22
- Labels: none

## Description

## Summary

Docs-only cleanup. Confirmed the live site has **zero** code references to `admin@heatpunks.org` — every `mailto:` in `app`/`components` resolves through `siteConfig.contact.email`, which is `tyler@256foundation.org`. The stale `@heatpunks.org` addresses only existed in design/spec docs, some of which claimed a "current"/"approved" status despite having already shipped with a different email.

- `ARCHITECTURE.md`, `SPEC.md` — added a divergence-list bullet: the `admin@`/`contact@`/`grants@`/`summit@heatpunks.org` addresses in ADR tables and `.env` examples describe the original design only.
- `SPEC-summit-2027.md` — added a status note (it previously had none) pointing to the real address and to the doc that now supersedes it.
- `SPEC-summit-2027-overhaul.md`, `SPEC-grants-256foundation.md` — these specs already shipped, so their "current"/"approved" banners were themselves stale. Updated to "shipped" and fixed the specific false-equivalence claims (e.g. "`siteConfig.contact.email`, which already equals `admin@heatpunks.org`" — it doesn't; it's `tyler@256foundation.org`).

No code changes.

## Test plan
- [x] `npm run lint` clean
- [x] Grepped repo for `admin@heatpunks.org` / `@heatpunks.org` before and after — confirmed no occurrences remain in `app/`, `components/`, `data/`, `lib/`, `types/`
- [x] Confirmed `data/site.ts` → `contact.email` and every `mailto:` call site already resolve to `tyler@256foundation.org`

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-07-22

[vc]: #SOcpumPbL81ylL8Gk+555FSgxNfVe/hfMRqyhPuPRlU=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLWhlYXRwdW5rcyIsInByb2plY3RJZCI6InByal9JM0FDajFucFFjb013UjdrcGcySlJRUENteVZQIiwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tLzI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMvd2Vic2l0ZS1oZWF0cHVua3MvNXJYTGRzZVdtbnZwMUx1b29ZcTM2NWNDaE1uaCIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWhlYXRwdW5rcy1naXQtZG9jcy1maXgtZmExNDExLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCIsIm5leHRDb21taXRTdGF0dXMiOiJQRU5ESU5HIiwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtaGVhdHB1bmtzLWdpdC1kb2NzLWZpeC1mYTE0MTEtMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn19XX0=
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| [website-heatpunks](https://vercel.com/256-foundation-s-projects/website-heatpunks) | ![Building](https://vercel.com/static/status/building.svg) [Building](https://vercel.com/256-foundation-s-projects/website-heatpunks/5rXLdseWmnvp1LuooYq365cChMnh) | [Preview](https://website-heatpunks-git-docs-fix-fa1411-256-foundation-s-projects.vercel.app), [Comment](https://vercel.live/open-feedback/website-heatpunks-git-docs-fix-fa1411-256-foundation-s-projects.vercel.app?via=pr-comment-feedback-link) | Jul 22, 2026 4:08pm |
