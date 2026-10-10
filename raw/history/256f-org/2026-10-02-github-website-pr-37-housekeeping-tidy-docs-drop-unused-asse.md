# 256foundation/website pull request #37: Housekeeping: tidy docs, drop unused assets, non-breaking audit fix

> Source: https://github.com/256foundation/website/pull/37
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 37
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

Post-sprint cleanup. No user-visible behavior change.

- **Unused assets:** remove `public/mission-background.webp` (superseded by the mission hero) and the 67-byte unused `public/logo-white.png`.
- **Docs:** move the one-off `discourse-header-prompt.md` into `docs/` and repoint `CLAUDE.md`; refresh the asset lists to the current mission hero.
- **Dependencies:** `npm audit fix` (non-breaking) clears the babel / humanfs / browserslist / brace-expansion advisories (6 -> 3 remaining). The last `next`/`postcss` and `sharp` advisories need `--force` (majors) and are left for a separate call.

Verified: `npm run lint` 0 errors, `npm test` 50/50, `npm run build` clean.
