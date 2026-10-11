# 256F website PR #47: Docs: session sync (rounds 16-17, OG cards, em dash rule, open items)

> Source: https://github.com/256foundation/website/pull/47
> Collected: 2026-10-10
> Published: 2026-10-10
> Registry ID: 256f-site

State: merged 2026-10-10 | Author: tylerkstevens | +80/-13 | 4 files (docs only, no code changes)

## Body

Documentation catch-up for the session that ended 2026-10-10.

- Mark PR #41 and the #42-#46 content branches merged; note all branches merged / no open PRs.
- Add round 16 (hero consistency + OG cards) and round 17 (content branches, em dash sweep) summaries.
- Record the three unanswered product questions, the branch cleanup, and the round-7 Libre Board supersede.
- Update CLAUDE.md current-state with the OG card system, no-period hero rule, and centered PageCTA default.

Docs only, no code changes.

## Files changed

==FILE== CLAUDE.md +13/-2
@@ -140,6 +140,8 @@ renders. GitHub/forum/Substack fetches use `next: { revalidate: 3600 }`.
 - [`lib/discourse.ts`](lib/discourse.ts) — Discourse forum (`forum.256foundation.org`):
   latest topics + per-project category topics; plus `forumTopicUrl` / `timeAgo` helpers.
 - [`lib/substack.ts`](lib/substack.ts) — parses the Substack RSS feed for post cards.
+- [`lib/html.ts`](lib/html.ts) — `decodeEntities()` + tag-strip for feed text; also folds
+  em dashes (named or numeric) to commas so external copy matches the site's no-em-dash rule.
 - [`lib/newsroomMeta.ts`](lib/newsroomMeta.ts) — `fs`-free slice of the newsroom module
   (category vocabulary/labels, `formatPostDate`). Client components import this, not
   `lib/newsroom.ts`, which imports Node `fs` and fails the webpack client build.
@@ -174,6 +176,9 @@ the rules that matter when writing UI:
    — **not a toggle**. The `dark:` variant is remapped to that media query via
    `@custom-variant`, so there is no `.dark` class and no theme switcher. Style both modes.
 7. Use `→` (`&rarr;`) for directional UI, not chevrons.
+8. **No em dashes in rendered copy** — use commas, colons, or parentheses. External feed
+   text is normalized to a comma in `lib/html.ts` (`decodeEntities`) so third-party posts
+   match; the only literal em dash left in source is the `mdash` entity mapping there.
 
 ---
 
@@ -210,7 +215,7 @@ avoid (Resend, Hashdash, Typeform) so they don't creep back in.
 
 ---
 
-## Current UI state (as of 2026-10-02)
+## Current UI state (as of 2026-10-10)
 
 Read [`docs/ui-work-log.md`](docs/ui-work-log.md) for the running log of UI revisions,
 decisions, and open items. Durable facts a fresh session must know:
@@ -237,7 +242,13 @@ decisions, and open items. Durable facts a fresh session must know:
   "round", no retired program names, no em dashes. Empty state ships. Tests:
   `tests/grant-announcements.test.mjs`.
 - **Hero title accent:** the accent word in a hero H1 is `text-[#c084d8]` (e.g. "Mining
-  Stack", "Open-Source").
+  Stack", "Open-Source"). Main-page hero H1s carry **no trailing period**.
+- **OpenGraph cards:** `public/og/og-*.png` (home + every footer Foundation/Resources page),
+  regenerated with `npm run og` (`scripts/generate-og.mjs`; brand TTFs in `assets/fonts/`, the
+  script mirrors them into `~/Library/Fonts` for librsvg). `generatePageMetadata` defaults to
+  `og-home.png`; each page passes its own `ogImage`; newsroom posts use their featured image.
+- **Closers:** `components/shared/PageCTA.tsx` centers by default, so every page ends on the
+  same note.
 - **Home (`/`) is an 8-beat page** (round 14): `HomeHero` (thesis H1, full-bleed Development
   Kit shot `public/home-hero.webp`, mirrored so the hardware sits right, static PCB, no
   rotating tagline, header logo only) → `ProblemSection` → `StackSection` (four layers →
==FILE== README.md +1/-0
@@ -667,6 +667,7 @@ GitHub API is called unauthenticated by default (60 req/hr limit). Set `GITHUB_T
 5. **Dark mode is the primary experience** — optimize dark first, light is fully supported
 6. **Borders over shadows** — depth via `#1f1f1f` borders, not box shadows
 7. **Arrow symbols** — use `→` (`&rarr;`) for directional UI, not chevrons
+8. **No em dashes in copy** — use commas, colons, or parentheses; feed text is normalized in `lib/html.ts`
 
 ### Decorative Elements
 
==FILE== docs/session-context.md +18/-9
@@ -5,19 +5,17 @@ Written so a fresh session (or a different agent) can resume with zero chat hist
 Read this together with [`docs/ui-work-log.md`](./ui-work-log.md) (the running UI log)
 and the repo root [`CLAUDE.md`](../CLAUDE.md).
 
-Last updated: 2026-10-02
+Last updated: 2026-10-10
 
 ---
 
 ## TL;DR current state
 
-- **Merged to `main`:** [#32](https://github.com/256foundation/website/pull/32) (round 12
-  design-system pass), [#33](https://github.com/256foundation/website/pull/33) (round 13
-  mission/footer), [#34](https://github.com/256foundation/website/pull/34) (round 14 home
-  overhaul). The branch stack `ui/edits-round12 → round13 → round14` is merged.
-- **Open:** [#35](https://github.com/256foundation/website/pull/35) — docs sync for round 14
-  (CLAUDE/README/session-context/ARCHITECTURE), on `ui/edits-round14`.
-- Earlier merged: #20, #21, #24, #25, #26, #27, #28, #30, #31. Rounds 3 and 4 had no PR.
+- **Everything is merged; no open PRs.** Recent rounds: content/design pass #36–#41,
+  Ember One first grant announcement + funding-timeline format #42, site-wide em dash
+  sweep + copy tweaks #43, community tweaks (Telehash background, heading, Hashdash copy,
+  mobile nav) #44, grants grant-log link #45, Mujina firmware copy #46.
+- Earlier merged: #20, #21, #24–#28, #30–#35. Rounds 3 and 4 had no PR.
 - Branch the next round fresh off `main`.
 - Dev server: `npm run dev` → http://localhost:3000.
 
@@ -84,6 +82,10 @@ All five are complete and merged.
   `Working Group Program`, `Community Program`. No per-project amounts.
 - **Grant-announcement copy rules:** no "cycle" / "wave" / "round"; no "pillar" /
   "maintainer retainer" / "adoption phase"; no retired program names; **no em dashes**.
+- **No em dashes anywhere in rendered copy** (site-wide, not just grant copy). Use commas,
+  colons, or parentheses; external feed text is normalized in `lib/html.ts`.
+- **Grant `term` format:** `<Duration>, <Month Year> to <Month Year>` (e.g.
+  `Four months, September 2026 to December 2026`), enforced by a test.
 - Retired vocabulary replaced site-wide (`pillar projects` → `core projects`,
   "under our umbrella" → "we serve", etc.); `tests/community.test.mjs` guards it.
 - Telehash happens **a few times a year** (not annually/semi-annually). Use the real
@@ -102,7 +104,8 @@ All five are complete and merged.
 Crossfade (~6s), hover-pause, reduced-motion static, swipe on touch, subtle arrows
 flanking centered dots, manual nav resets the autoplay timer. Photos are real community
 shots in `public/community/hero-0*.webp` (1920px WebP), listed in `communityHeroPhotos`
-in `data/community.ts` — add or reorder there.
+in `data/community.ts` — add or reorder there. `hero-03` is held out of the rotation and
+used as the Telehash feature card background (`telehashFeaturePhoto`).
 
 ---
 
@@ -158,3 +161,9 @@ the root layout provides `<main>`, so avoid accidental `main > main`.
 - #23 Community page (superseded by #24) — closed
 - #24 Community page, Our Work stub, nav consolidation, copy polish — merged
 - #25 Our Work hero photo — merged
+- #36–#41 Home polish, image perf passes, housekeeping, docs sync — merged
+- #42 Ember One first grant announcement + funding-timeline format — merged
+- #43 Content tweaks + full em dash sweep — merged
+- #44 Community: Telehash background, heading, nav tweaks — merged
+- #45 Grants: link the funded grant log from the announcements section — merged
+- #46 Projects: tighten Mujina firmware copy — merged
==FILE== docs/ui-work-log.md +48/-2
@@ -4,7 +4,7 @@ Running log of website UI revision rounds, decisions, and open follow-ups. **Rea
 first in a fresh session** so nothing lives only in chat history. For the fuller
 round-5 pickup context, see [`docs/session-context.md`](./session-context.md).
 
-Last updated: 2026-10-02
+Last updated: 2026-10-10
 
 ---
 
@@ -31,7 +31,15 @@ Last updated: 2026-10-02
 | `chore/image-weight` | [#38](https://github.com/256foundation/website/pull/38) | Cut shipped raster weight ~13MB → ~1.5MB: convert oversized project/ecosystem/supporter art to right-sized WebP (`scripts/optimize-art.mjs`), re-encode logos + OG to compressed palette PNG | merged |
 | `chore/perf-pass` | [#39](https://github.com/256foundation/website/pull/39) | Round 2 of image/perf: re-run newsroom optimizer, convert telehash photos to WebP, and mount only 3 frames in the `/community` hero carousel instead of all 8 | merged |
 | `chore/img-nextimage` | [#40](https://github.com/256foundation/website/pull/40) | Convert the last 5 raw `<img>` tags to `next/image` (lint now clean), tighten newsroom optimizer to 1440px/q78, align `deviceSizes` to 1440 | merged |
-| `ui/our-work-hero-break` | [#41](https://github.com/256foundation/website/pull/41) | Hero-heading consistency: purple accent word(s) on the home, mission, grants, community and our-work heroes, "open-source"/"mining stack" broken to their own line where noted, trailing periods removed from all main-page hero headers; grants hero CTAs switched to the shared Button pair; our-work Vision relabeled "The Future" with a new lead line and program copy refreshed; community "Listen and Learn" shows newsroom + newsletter + podcast with the newsroom piece first, and project cards keep "Visit →" visible, with a Donate → button into each community fund (OSMU, Hashrate Heatpunks); community carousel opens on the developer-call shot; every page's closing PageCTA now defaults to centered so pages all end on the same note. **Plus:** regenerated OpenGraph share cards — one branded home card and a dedicated card per footer Foundation + Resources page (`scripts/generate-og.mjs` → `public/og/og-*.png`, brand TTFs in `assets/fonts/`), wired through `ogImage` in each page's metadata; newsroom posts still use their own featured image | PR opens now |
+| `ui/our-work-hero-break` | [#41](https://github.com/256foundation/website/pull/41) | Hero-heading consistency: purple accent word(s) on the home, mission, grants, community and our-work heroes, "open-source"/"mining stack" broken to their own line where noted, trailing periods removed from all main-page hero headers; grants hero CTAs switched to the shared Button pair; our-work Vision relabeled "The Future" with a new lead line and program copy refreshed; community "Listen and Learn" shows newsroom + newsletter + podcast with the newsroom piece first, and project cards keep "Visit →" visible, with a Donate → button into each community fund (OSMU, Hashrate Heatpunks); community carousel opens on the developer-call shot; every page's closing PageCTA now defaults to centered so pages all end on the same note. **Plus:** regenerated OpenGraph share cards — one branded home card and a dedicated card per footer Foundation + Resources page (`scripts/generate-og.mjs` → `public/og/og-*.png`, brand TTFs in `assets/fonts/`), wired through `ogImage` in each page's metadata; newsroom posts still use their own featured image | merged |
+
+| `newsroom/ember-one-first-grant` | [#42](https://github.com/256foundation/website/pull/42) | Newsroom: backfill the Ember One first grant announcement; standardize every grant-announcement `term` to `<Duration>, <Month Year> to <Month Year>` (documented in README, enforced by `tests/grant-announcements.test.mjs`); correct the Libre Board article to its April–December 2026 term with the funding-driven pause and contingent September–December reactivation | merged |
+| `content/site-tweaks` | [#43](https://github.com/256foundation/website/pull/43) | Copy tweaks (home block-`881423` year → 2025 + narrow-screen hero break, mission closing split, our-work hero/status-quo copy, projects hero/intro) and a site-wide em dash sweep across `app/`, `components/`, `data/`, `content/`, plus normalization of em dashes arriving from Discourse/feed text | merged |
+| `content/community-updates` | [#44](https://github.com/256foundation/website/pull/44) | Community: Telehash card now uses the livestream frame as its background (pulled from the hero rotation); heading "Where the 256 Community lives"; Hashdash described as the donation pool + gamified dashboard; mobile-menu Donate drops the lightning bolt | merged |
+| `content/grants-announcements-link` | [#45](https://github.com/256foundation/website/pull/45) | Grants: the funding-announcements sub-line now links the funded grant log (`/grants/announcements`) as well as the newsroom | merged |
+| `content/projects-firmware-copy` | [#46](https://github.com/256foundation/website/pull/46) | Projects: sharpen the Mujina firmware closed-problem / open-answer copy | merged |
+
+**All of the above are merged; no open PRs as of 2026-10-10.** The five `content/*` + `newsroom/*` remote branches and four stale local branches (upstream `gone`) are merged but not yet deleted.
 
 Merge order for the earlier stack was #20 → #21 → `ui/edits-round3`; all three are merged, so `ui/edits-round5` now bases on `main`.
 
@@ -292,6 +300,33 @@ already boxed buttons, but the Latest beat's "All updates →" was a bare text l
 the same `Button variant="outlined" size="sm"`, so every in-content link to a main page on the
 home page is the same control (photo overlays stay `onDark`).
 
+### Round 16 — `ui/our-work-hero-break` (PR #41, merged) — hero consistency + OG cards
+
+- **Hero headings made consistent site-wide:** the accent word in each main-page hero H1 is
+  purple (`text-[#c084d8]`) and trailing periods are gone, with "open-source" / "mining stack"
+  broken to their own lines on the home, mission, grants, community and our-work heroes.
+- **Grants hero CTAs** switched to the shared `Button` pair so they match every other hero.
+- **Our Work:** "Vision" relabeled "The Future" with a new lead line; program copy refreshed.
+- **Community:** "Listen and Learn" now surfaces newsroom + newsletter + podcast, newsroom
+  first; project cards keep "Visit →" visible and gain a Donate → button into each community
+  fund (OSMU, Hashrate Heatpunks); carousel opens on the developer-call shot.
+- **Closers:** `PageCTA` now centers by default, so every page ends on the same note.
+- **OpenGraph cards regenerated** (`scripts/generate-og.mjs`, `npm run og`): a branded home
+  card and a dedicated card per footer Foundation + Resources page, wired through `ogImage`
+  in each page's metadata; newsroom posts still use their own featured/cover image.
+
+### Round 17 — content branches (PRs #42–#46, merged)
+
+- **Ember One announcement** backfilled (`content/newsroom/ember-one-first-grant.mdx`), and the
+  funding-timeline `term` format standardized to `<Duration>, <Month Year> to <Month Year>`
+  across all grant announcements (README documents it, a test enforces it).
+- **Libre Board article corrected** to its April–December 2026 term, the funding-driven pause,
+  and a contingent September–December reactivation.
+- **Full em dash sweep** across the app, components, data and content, plus normalization of
+  em dashes arriving from Discourse and feed text (`lib/html.ts`, `lib/feed.ts`, etc.).
+- Community/grants/projects copy tweaks (Telehash feature background, "Where the 256 Community
+  lives", Hashdash description, grant-log link, Mujina firmware copy).
+
 ---
 
 ## Decisions / conventions locked
@@ -323,6 +358,17 @@ home page is the same control (photo overlays stay `onDark`).
 
 ## Open items / next steps
 
+- **Unanswered product questions** (asked during round 16, still open):
+  1. `/community` lost its signup card, so `components/shared/NewsletterSignup.tsx` is now
+     unused. Keep a subscribe form somewhere on `/community`, or delete the component?
+  2. `/our-work` vision wording: use the short "The Future" eyebrow with the lead line
+     "The future of mining should be decided by miners.", or the full phrase "The Future of
+     Mining Should be Determined by Miners"? Also confirm **decided** vs **determined**.
+  3. Home hero line "OPEN-SOURCE," leaves the comma on the purple accent line; leave or move it.
+- **Branch cleanup:** five merged `content/*`/`newsroom/*` remote branches and four stale local
+  branches (upstream `gone`) still exist; safe to delete.
+- **Round 7 Libre Board note is superseded** by round 17: the term is April–December 2026 with a
+  funding-driven pause, and the September–December reactivation is contingent.
 - **Grants "Apply for a Grant" button** (General Grant card) now links to the Typeform
   application form (`https://form.typeform.com/to/oqyJAntF`, new tab). Core Projects
   "Calls currently closed" stays inert until its window reopens. The hero "Apply for a
