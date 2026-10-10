# 256foundation/website pull request #40: perf: next/image for remaining raw img, tighter newsroom optimizer

> Source: https://github.com/256foundation/website/pull/40
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 40
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

Clears the last image lint warnings and trims newsroom art further.

- Converted the last 5 raw `<img>` tags to `next/image` (community project logos, supporter logos, team avatars, leaderboard avatars, telehash carousel) so they get responsive AVIF/WebP and correct sizing. Leaderboard avatars use `unoptimized` because their hosts are arbitrary live-API URLs; the `onError` fallbacks are preserved. `eslint` is now **0 problems** (was 5 warnings).
- Newsroom optimizer cap 1600px/q82 -> 1440px/q78, and aligned `next.config` `deviceSizes` to 1440 (drops a 1600 upscale step). `public/newsroom` 1.9 MB -> 1.3 MB.

`public/` 7.8 MB -> 7.2 MB. Verified community/supporter/team art and the telehash carousel render; `npm test` 50/50, `npm run build` clean.
