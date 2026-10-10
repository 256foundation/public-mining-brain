# 256foundation/website pull request #35: Docs: sync project docs to the round 14 home

> Source: https://github.com/256foundation/website/pull/35
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 35
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

Follow-up to #34 (already merged). Its docs commit landed after the merge, so this carries just that commit.

Updates the docs a fresh session reads so nothing lives only in chat:

- **CLAUDE.md** — route map (home is an 8-beat page; adds `/community`, `/our-work`, `/contact`; corrects `/mission`), home component list, data table (`data/community.ts`, `data/ourWork.ts`, `stats` now unused), and the "Current UI state" section (8-beat home, `Reveal`/`ScrollProgress`/`useReducedMotion`, `HeroScrim` hero pattern, nav order).
- **README.md** — component tree (new `home/*` and `ui/*` primitives incl. `Eyebrow`/`TextLink`/`Panel`/`HeroScrim`/`Reveal`), newsroom "newest post" wording, "add a project" recipe (`data/projects.ts` + `data/community.ts`), and a note that `data/stats.ts` is currently unused.
- **docs/session-context.md** — current open/merged PR state, home overhaul marked done, lint baseline (5 `<img>` warnings), mission/home hero asset paths.
- **ARCHITECTURE.md** — banner notes that the home/mission sections are superseded.

No code changes. `npm run lint` 0 errors, `npm test` 50/50.
