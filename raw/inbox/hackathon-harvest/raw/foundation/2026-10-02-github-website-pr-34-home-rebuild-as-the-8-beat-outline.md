# 256foundation/website pull request #34: Home: rebuild as the 8-beat outline

> Source: https://github.com/256foundation/website/pull/34
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 34
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

Rebuilds the homepage from the 8-beat outline into a tighter, live page. Copy answers why/who; destination pages answer how.

## Beats
1. **Hero** — thesis is the H1 ("Bitcoin mining will be open-source, or Bitcoin remains permissioned."), full-bleed Development Kit shot (`public/home-hero.webp`, mirrored so the hardware sits right), static PCB texture, no rotating tagline, header logo only, scroll cue.
2. **Problem** — two centered statements → `/mission`.
3. **Stack** — four layer cards → `/projects#slug`, "Together, the four form the Development Kit." → `/projects`.
4. **Proof** — giant `881423` + block copy beside the existing block-find video → `/our-work`.
5. **Funding** — compact tinted band + grants CTA (not a full screen).
6. **Community** — full-bleed photo + live forum and GitHub strips → `/community`.
7. **Latest** — one live card each from newsroom, POD256, Substack → `/newsroom`.
8. **Closer** — shared `PageCTA`; keeps `id="contact"` so old `/#contact` links land.

## Also
- New client utilities: `Reveal` (one-time fade, readable with motion off) and `ScrollProgress` (purple line in the header, no easing under reduced motion), plus `lib/useReducedMotion.ts`.
- Beat destination links use the shared `Button`/`TextLink` primitives.
- Removed from home: contact form, mission essay, ecosystem essays, supporters wall, FAQ, hashrate leaderboard, duplicate project essays; ten now-dead `components/home` files deleted (`HashrateLeaderboard` stays for `/donate`).
- Zero em dashes, ban-list clean, ~5.9 desktop screens.

## Checks
- `npm run lint`: 0 errors (5 pre-existing `<img>` warnings)
- `npm test`: 50/50
- `npm run build`: green

Stacked on `ui/edits-round13` (#33) and `ui/edits-round12` (#32); merge those first.

## Open asset ask
Optional landscape crop of the Development Kit shot; the current square `public/home-hero.webp` works with the scrim.
