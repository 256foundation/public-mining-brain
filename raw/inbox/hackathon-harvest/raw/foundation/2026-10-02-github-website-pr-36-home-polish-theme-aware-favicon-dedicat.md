# 256foundation/website pull request #36: Home polish: theme-aware favicon, dedicated community photo, CTA consistency

> Source: https://github.com/256foundation/website/pull/36
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 36
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

Final home-page polish pass.

- **Favicon:** uses the header `secondary` 256 mark, theme-aware (`app/icon.svg` black/white) with `app/favicon.ico` + `app/apple-icon.png` fallbacks; replaces the off-brand `app/icon.png`.
- **Community photo:** dedicated wide home crop (`public/home-community.webp`, 2048x820) instead of reusing a `/community` carousel shot; speaker centered so `object-cover` reads at any aspect ratio.
- **CTA consistency:** the Latest beat's "All updates →" (`/newsroom`) was the last bare main-page text link on home; it now uses the same outlined `Button` as every other in-content main-page destination.

Verified: `npm run lint` 0 errors, `npm test` 50/50, `npm run build` clean. Desktop + mobile checked.
