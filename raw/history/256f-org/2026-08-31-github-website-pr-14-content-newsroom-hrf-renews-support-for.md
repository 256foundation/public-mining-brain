# 256foundation/website pull request #14: content(newsroom): HRF renews support for the 256 Foundation

> Source: https://github.com/256foundation/website/pull/14
> Collected: 2026-10-07
> Published: 2026-08-31

- Repository: 256foundation/website
- Type: pull request
- Number: 14
- State: closed
- Author: tylerkstevens
- Opened: 2026-08-31
- Closed: 2026-08-31
- Labels: none

## Description

Adds the newsroom post announcing HRF's renewed Bitcoin Development Fund grant.

## What's here
- `content/newsroom/hrf-renews-support.mdx` — dated 2026-08-25 to match HRF's press release; takes the `featured` home-page slot from the RY3T Nova post (which flips to `featured: false`).
- Three images in `public/newsroom/hrf-renews-support/`:
  - `og-hrf-256-foundation.png` — 1200x630 banner/OG composite (Bitcoin 2026 HRF-stage panel photo + 256 Foundation and HRF marks), used as both `coverImage` and `ogImage`
  - `hrf-stage-panel-bitcoin-2026.webp`
  - `schnitzel-gladstein-bitcoin-2026.webp`
  - `gladstein-announcement-tweet.webp`
- Outbound links to HRF's press release, the Bitcoin Development Fund, the panel recording on YouTube, and Gladstein's announcement on X.

## Verified
- `npm test` — 26/26 pass
- `npm run build` — clean; `/newsroom/hrf-renews-support` prerenders
- Rendered in light and dark mode, no console errors
- All outbound links return 200

## Known open items (deliberate, not blockers)
- The RY3T conflict-of-interest disclosure (Schnitzel sits on RY3T's board) was removed during the edit pass.
- The second mining bullet attributes issuance to both the block subsidy and transaction fees; fees transfer existing bitcoin rather than issue new.
- Copy uses "Lead Maintainers" and "Core Projects" rather than the "Core Contributors" / pillar-projects convention.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
