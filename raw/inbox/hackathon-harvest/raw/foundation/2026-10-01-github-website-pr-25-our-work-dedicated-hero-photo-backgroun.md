# 256foundation/website pull request #25: Our Work: dedicated hero photo background

> Source: https://github.com/256foundation/website/pull/25
> Collected: 2026-10-07
> Published: 2026-10-01

- Repository: 256foundation/website
- Type: pull request
- Number: 25
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-01
- Closed: 2026-10-01
- Labels: none

## Description

Follow-up to #24 (merged). Adds the dedicated hero image for `/our-work`.

- Converted the supplied `our-work-hero.jpg` (5712×4284) to a 1920px WebP (`public/our-work-hero.webp`, ~406 KB) to match the other hero assets.
- Pointed the `/our-work` hero at it (was reusing `mission-background.webp`).
- Work log updated.

## Verification

`npm run lint` (0 errors) · `npm run build` green.
