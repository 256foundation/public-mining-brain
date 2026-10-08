# 256foundation/website pull request #27: content(libre-board): reactivation framing + funding CTA

> Source: https://github.com/256foundation/website/pull/27
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 27
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

## Summary
Newsroom copy pass on the September 30 Libre Board funding announcement.

### Libre Board article
- Reframes the post as **additional funding that reactivates the existing 2026 term**, not a new term. Retitles the post, SEO title, excerpt, opening, and the "What the Funding Covers" lead.
- Updates the grants-log `term` label to `2026 term, reactivated September`.
- Adds a **"Keep It Running"** CTA: continuous donations keep grants on schedule, and larger/longer commitments give grantees an uninterrupted term and stability. Stays honest about the actual one-time rails (no recurring/subscription claim).
- No budget or grant-agreement detail added, per the team's brief.
- Fixes the grant-announcements test's frontmatter parser, which broke on the apostrophe in "Board's" (it silently treated the title as missing); updates the term assertion.

## Verification
- `npm test` — 44/44 pass
- `npm run lint` — 0 errors (7 pre-existing `<img>` warnings)
- `npm run build` — green
