# 256foundation/website pull request #20: Open Mining Stack: collapse project pages into one narrative page

> Source: https://github.com/256foundation/website/pull/20
> Collected: 2026-10-07
> Published: 2026-09-29

- Repository: 256foundation/website
- Type: pull request
- Number: 20
- State: closed
- Author: tylerkstevens
- Opened: 2026-09-29
- Closed: 2026-09-29
- Labels: none

## Description

## What

Replaces the `/projects` index and the four standalone `/projects/[slug]` pages with a single narrative page at **`/projects`**: **"Open Mining Stack"**.

The page tells the stack as four layers — hash board → control board → firmware → pool — in order: **Ember One, Libre Board, Mujina, Hydrapool**.

## Why

The four core projects belong together as one stack. Each layer is either undocumented, closed, or concentrated; open one and close another and you rebuild the cage. The page frames each layer as a **closed problem → open answer** (what it does, what it teaches, what it unlocks), and closes on the collective claim: a permissionless open-source mining development kit.

## Changes

- **New page** `app/projects/page.tsx`: hero (permissioned stakes + open-origin point), commodity/recipes overview, 4-cell layer index with computing analogies, sticky layer sub-nav, four layer sections, closing CTA. Optional hero dev-kit image slot (drop `public/projects/open-mining-stack-devkit.{webp,jpg,png}` and it appears).
- **New components**: `StackSubNav`, `StackLayerSection`, `ActivityBadges` (fail-soft GitHub stars + last push / forum last reply).
- **Retired deep pages**: `/projects/{ember-one,libre-board,mujina,hydrapool}` → `308` to each project's dedicated site (`next.config.ts`).
- **Nav**: Projects dropdown removed → single `MINING STACK` top-level link; footer relabeled.
- **Removed**: Grant Log (page, `data/grants.ts`, `GrantLogTable`, `Grant`/milestone/context types) and the duplicate ecosystem grid.
- **Data/types pruned** to what the page uses; added `architect` and `whatItDoes`.
- **Internal links** (home cards, hero chips, 2 MDX posts) now point to on-page anchors.
- **Docs**: `CLAUDE.md`, `README.md`, `docs/open-mining-stack-plan.md`.

## Verification

- `npm run build` — clean (18 routes; `/projects/[slug]` gone)
- `npm run lint` — 0 errors (6 pre-existing `<img>` warnings)
- `npm test` — 26/26 pass
- Redirects: all four return `308` to the correct external site

## Notes for review

- Hero/problem copy is a first draft — worth a read at `/projects`.
- P2Pool V2 is phrased as a roadmap/path (separate project by the same maintainer), not shipped.
- No grant amounts per project; maintainers credited as "Core Architect & Lead Maintainer" to keep grantee status flexible.
