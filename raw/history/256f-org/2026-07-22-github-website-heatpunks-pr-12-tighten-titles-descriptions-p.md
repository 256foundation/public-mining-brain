# 256foundation/website-heatpunks pull request #12: Tighten titles/descriptions per opengraph.xyz feedback

> Source: https://github.com/256foundation/website-heatpunks/pull/12
> Collected: 2026-10-07
> Published: 2026-07-22

- Repository: 256foundation/website-heatpunks
- Type: pull request
- Number: 12
- State: closed
- Author: tylerkstevens
- Opened: 2026-07-22
- Closed: 2026-07-22
- Labels: none

## Description

## Summary

opengraph.xyz's meta-tag inspector flagged the same issue on every page after the OG overhaul went live: the shared `description` (feeds `og:description`, Twitter, and `<meta name="description">`) was 132–162 characters — past its ~125-char social-preview sweet spot and close to/over Google's ~150–160 search-snippet cutoff. Also flagged: the home title at 63 characters (target ≤60).

- Tightened all 7 page descriptions to 121–138 characters
- Shortened the home title from 63 → 50 characters (`...for Homes & Businesses` → `...for Homes`)
- Content trims: home title drops "& Businesses" (already implied by "home and business heating" in the description); summit description drops the explicit word "Bitcoin" (implied by context) to make room for the waitlist CTA

**Deliberately not acted on** (both flagged, both judgment calls to skip):
- "Image missing conversion text" (og:image) — generic nudge to bake a "Learn More" CTA into the image; that's built for marketing banners, not this site's terminal aesthetic, and the command/comment lines already serve that role
- Mission title "too short" (28 chars) — a soft "unused SERP space" nudge, not a real problem (Education's 30-char title gets no warning at all; threshold is inconsistent)

## Test plan
- [x] `npm run lint` clean, production `npm run build` green
- [x] Verified exact character counts with a script (not eyeballed) before drafting copy
- [x] Verified in the rendered `<head>` (not just source) that title/description lengths match what was drafted — home: title 50 chars, description 122 chars; summit: description 138 chars

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### vercel[bot] on 2026-07-22

[vc]: #zg6TdKWVfuMYTyTYK0UDmdyFZrVdntenNDk/1uYuyU4=:eyJpc01vbm9yZXBvIjp0cnVlLCJ0eXBlIjoiZ2l0aHViIiwicHJvamVjdHMiOlt7Im5hbWUiOiJ3ZWJzaXRlLWhlYXRwdW5rcyIsInByb2plY3RJZCI6InByal9JM0FDajFucFFjb013UjdrcGcySlJRUENteVZQIiwiaW5zcGVjdG9yVXJsIjoiaHR0cHM6Ly92ZXJjZWwuY29tLzI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMvd2Vic2l0ZS1oZWF0cHVua3MvNDJ5SHlETVZ3ZEE0d3NHSEw5TkdCakJHQUVieiIsInByZXZpZXdVcmwiOiJ3ZWJzaXRlLWhlYXRwdW5rcy1naXQtdGlnaHRlbi1iMDQ5MWItMjU2LWZvdW5kYXRpb24tcy1wcm9qZWN0cy52ZXJjZWwuYXBwIiwibmV4dENvbW1pdFN0YXR1cyI6IlBFTkRJTkciLCJsaXZlRmVlZGJhY2siOnsicmVzb2x2ZWQiOjAsInVucmVzb2x2ZWQiOjAsInRvdGFsIjowLCJsaW5rIjoid2Vic2l0ZS1oZWF0cHVua3MtZ2l0LXRpZ2h0ZW4tYjA0OTFiLTI1Ni1mb3VuZGF0aW9uLXMtcHJvamVjdHMudmVyY2VsLmFwcCJ9fV19
The latest updates on your projects. Learn more about [Vercel for GitHub](https://vercel.link/github-learn-more).

| Project | Deployment | Actions | Updated (UTC) |
| :--- | :----- | :------ | :------ |
| [website-heatpunks](https://vercel.com/256-foundation-s-projects/website-heatpunks) | ![Building](https://vercel.com/static/status/building.svg) [Building](https://vercel.com/256-foundation-s-projects/website-heatpunks/42yHyDMVwdA4wsGHL9NGBjBGAEbz) | [Preview](https://website-heatpunks-git-tighten-b0491b-256-foundation-s-projects.vercel.app), [Comment](https://vercel.live/open-feedback/website-heatpunks-git-tighten-b0491b-256-foundation-s-projects.vercel.app?via=pr-comment-feedback-link) | Jul 22, 2026 4:54pm |
