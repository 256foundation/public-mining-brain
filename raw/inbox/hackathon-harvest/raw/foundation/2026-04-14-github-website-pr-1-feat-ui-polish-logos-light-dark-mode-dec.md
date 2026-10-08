# 256foundation/website pull request #1: feat: UI polish — logos, light/dark mode, decorative backgrounds, res…

> Source: https://github.com/256foundation/website/pull/1
> Collected: 2026-10-07
> Published: 2026-04-14

- Repository: 256foundation/website
- Type: pull request
- Number: 1
- State: closed
- Author: tylerkstevens
- Opened: 2026-04-14
- Closed: 2026-04-14
- Labels: none

## Description

…ponsive footer

## Logo system
- Add Logo component with picture/source media for native light/dark switching
- Organize all logo assets into public/logos/ (horizontal, square, vertical, rounded — black & white variants)
- Add Hydrapool and Mujina project assets to public/projects/
- Update types/index.ts and data/projects.ts to support per-project logo config
- Render project logos on [slug] page in a two-column hero layout

## Light / dark mode (system preference)
- Switch globals.css to use @custom-variant dark (@media (prefers-color-scheme: dark))
- Replace pitch-black #0a0a0a backgrounds with dark grey #1a1a1a sitewide
- Elevate secondary surface color from #111111 to #242424 for proper depth hierarchy
- Apply consistent dark:/light patterns across all 40+ components and pages

## Decorative backgrounds
- Create DecorativeBg component (PCB grid + purple radial glow + vignette fade)
- Add decorative prop to SectionWrapper (adds relative overflow-hidden context)
- Apply DecorativeBg to hero sections on /donate, /grants, /faq, /telehash
- Apply DecorativeBg to contact section on home page (glow from bottom-center)
- Apply DecorativeBg to ApplySection with vignette disabled (bg mismatch prevention)

## Mobile responsiveness
- Fix hero logo cutoff: swap to square variant on small screens
- Fix mobile hero padding/spacing to prevent CTA buttons being off-screen
- Fix EcosystemSection card layout: logo stacks above text on mobile, side-by-side on sm+
- Fix HeroSection alignment: justify-center on mobile, justify-end on desktop

## Footer
- Fix 2-column broken layout on tablet by changing sm:grid-cols-2 → md:grid-cols-3
- Now renders: 1 column (mobile) → 3 columns (tablet+) → 12-col grid (desktop)
