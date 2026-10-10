# 256foundation/website pull request #43: Content tweaks + full em dash sweep

> Source: https://github.com/256foundation/website/pull/43
> Collected: 2026-10-07
> Published: 2026-10-03

- Repository: 256foundation/website
- Type: pull request
- Number: 43
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-03
- Closed: 2026-10-03
- Labels: none

## Description

## Summary
Small copy tweaks gathered from in-app annotations, plus a full em dash sweep across the site.

### Copy tweaks
- **Home**: correct block 881423 year to 2025; break the hero line before "Bitcoin mining stack" on narrow screens; "four unique building blocks".
- **Mission**: split the closing line at the sentence boundary.
- **Our Work**: hero reads "because a company is not incentivized to do this and a closed industry will not"; success now means anyone can "use, fork, build upon and compete"; status-quo cards sharpened (hashboard, control board, pool).
- **Projects**: em dashes removed from hero and intro.

### Em dash sweep
- Replaced " — " with commas/colons across `app/`, `components/`, `data/`, `content/` (including the MARA newsroom post).
- Normalized em dashes arriving from external feeds (Discourse forum excerpts, Substack titles, GitHub descriptions) through `decodeEntities`, so runtime content matches.

## Verification
- `npx tsc --noEmit` clean
- `npm run lint` clean
- `node --test tests` 51/51 pass
- All rendered pages return zero em dashes (`/`, `/our-work`, `/mission`, `/projects`, `/faq`, `/telehash`, `/donate`, `/newsroom`, `/contact`, `/community`, `/grants`, and newsroom articles)
- Home hero break confirmed at mobile width; mission CTA renders as two lines

No changes to the two live grant announcements' terms; drafts untouched.
