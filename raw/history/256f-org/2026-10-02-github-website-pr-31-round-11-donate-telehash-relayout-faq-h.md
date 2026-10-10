# 256foundation/website pull request #31: Round 11: donate + telehash relayout, FAQ hero CTA, footer cleanup

> Source: https://github.com/256foundation/website/pull/31
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 31
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

## Summary
Round 11 focuses on the donate and telehash pages (layout + removing the dark purple/neon green styling in favor of the neutral/brand palette), plus a few site cleanups.

## Changes
### /donate
- Compact two-column hero with the Zaprite action above the fold (button + Card/On-chain/Lightning chips); button relabeled "Donate Bitcoin or Fiat".
- Folded the old money section into the hero; trimmed direct-address and hashrate copy.
- Removed the standalone 501(c)(3) section.
- Direct-donation cards widened so the on-chain address stays on one line; Lightning address updated to `256foundation@strike.me`.
- Code chips + `CopyButton` rethemed from dark purple/neon green to neutral gray/brand purple.
- Shared `ZAPRITE_URL` constant (removes hardcoded/`#`-fallback mismatch).
- Bottom PageCTA retitled "Large Gifts or Something Else".

### /telehash
- Neutralized the dark purple/green code blocks and green status badges; pool URL kept on one line.
- Reworked the hero: event status moved into a full-height right-side panel with an anchored header and a primary purple "View Events Calendar" bar; removed the separate countdown section.

### Site
- FAQ: answer email -> `contact@256foundation.org`; new hero "General Questions" panel with Get in touch (/contact) + Visit the Forum.
- Supporters heading renamed "Community Backers" -> "Foundation Backers".
- Footer: dropped redundant Contact link from Resources (large Contact button already present).

## Testing
- `npm test` 50/50, `npm run lint` 0 errors, `npm run build` green.
