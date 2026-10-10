# 256foundation/website-heatpunks pull request #1: Move grants to the 256 Foundation; dedupe homepage CTAs

> Source: https://github.com/256foundation/website-heatpunks/pull/1
> Collected: 2026-10-07
> Published: 2026-07-20

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 1
- State: closed
- Author: tylerkstevens
- Opened: 2026-07-20
- Closed: 2026-07-21
- Labels: none

## Description

## Summary

Hashrate Heatpunks no longer runs its own grant program. Grants are run by the parent **256 Foundation**, so the site now *describes* that program and links out to it instead of hosting its own. This deepens Heatpunks' integration into the Foundation and avoids running two competing grant programs.

Full rationale and decisions in [`SPEC-grants-256foundation.md`](SPEC-grants-256foundation.md).

## What changed

**Removed the Heatpunks grant program** (net −1,100+ lines)
- Deleted the `/grants` page, all 8 `components/grants/*`, `/api/grants`, `data/grants.ts`, `types/grants.ts`, `sendGrantApplication` in `lib/email.ts`, and the `siteConfig.grants.open` flag.

**Navigation**
- Replaced the `Grants` item with an outlined external **256 Foundation** button (→ `256foundation.org` homepage, new tab).
- Removed the standalone **Donate** nav button.
- New order: Home · Mission · Education · Summit · [Forum] · [Group Chat] · [256 Foundation].

**Donate**
- Repointed every donate link sitewide to `https://www.256foundation.org/donate` (via `foundation.donate`); retired the direct Zaprite URL constant.

**Redirect**
- Added a 308 redirect `/grants` → `https://www.256foundation.org/grants` in `next.config.js` so old links/bookmarks don't dead-end.

**Re-framed grants mentions** (homepage, education, mission)
- Bridge framing: the 256 Foundation funds open-source Bitcoin mining & decentralization, and hashrate heating fits within that mission.
- Explicit **open-source-only** requirement: anything a grant produces (code, docs, or education) must be released publicly.
- Links to the Foundation grants page.

**Deduped homepage CTAs** (follow-up to review feedback)
- Donate/grants CTAs were each appearing ~3×. Now each section has one job: grants section keeps only `SEE THE GRANT PROGRAM ↗`; donate section button relabeled `DONATE ↗`. Net: donate 3×→2× (hero + donate section), grants 3×→1×.

**Docs**
- Updated `CLAUDE.md`; added `SPEC-grants-256foundation.md`. Historical `SPEC.md`/`ARCHITECTURE.md` left untouched.

## Test plan

- [x] `npm run lint` — clean (only pre-existing OG image warnings)
- [x] `npm run build` — succeeds; route list no longer includes `/grants` or `/api/grants`
- [x] `npm run test` — 30/30 pass
- [x] `/grants` returns **308 → www.256foundation.org/grants** (verified via curl)
- [x] Nav renders correctly (Donate removed, 256 Foundation outlined external button)
- [x] Homepage/education/mission re-framed copy + button targets verified via live DOM
- [x] Footer NAVIGATE column drops GRANTS
- [x] No stale references to `grants.open`, `@/data/grants`, `@/types/grants`, `sendGrantApplication`, `DONATE_URL`, or `pay.zaprite`
- [x] Zero console errors across home → education → mission on a clean tab; server logs clean

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-07-20

[vc]: #kLQ3D2ZjYhn33bBAbPXMkVDuP4rAwDsinTjbSHhZH78=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLWhlYXRwdW5rcyIsInByb2plY3RJZCI6InByal9JM0FDajFucFFjb013UjdrcGcySlJRUENteVZQIiwibGl2ZUZlZWRiYWNrIjp7InJlc29sdmVkIjowLCJ1bnJlc29sdmVkIjowLCJ0b3RhbCI6MCwibGluayI6IndlYnNpdGUtaGVhdHB1bmtzLWdpdC1ncmFudHMtdC0xNGE1OTktMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIn0sImluc3BlY3RvclVybCI6Imh0dHBzOi8vdmVyY2VsLmNvbS8yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzL3dlYnNpdGUtaGVhdHB1bmtzL0pCSjVCWDNCMktGdGprTDdZUDRGbnZQWWR2YjQiLCJwcmV2aWV3VXJsIjoid2Vic2l0ZS1oZWF0cHVua3MtZ2l0LWdyYW50cy10LTE0YTU5OS0yNTYtZm91bmRhdGlvbi1zLXByb2plY3RzLnZlcmNlbC5hcHAiLCJuZXh0Q29tbWl0U3RhdHVzIjoiREVQTE9ZRUQifV19
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| [website-heatpunks](https://vercel.com/256-foundation-s-projects/website-heatpunks) | ![Ready](https://vercel.com/static/status/ready.svg) [Ready](https://vercel.com/256-foundation-s-projects/website-heatpunks/JBJ5BX3B2KFtjkL7YP4FnvPYdvb4) | [Preview](https://website-heatpunks-git-grants-t-14a599-256-foundation-s-projects.vercel.app), [Comment](https://vercel.live/open-feedback/website-heatpunks-git-grants-t-14a599-256-foundation-s-projects.vercel.app?via=pr-comment-feedback-link) | Jul 20, 2026 10:37pm |
