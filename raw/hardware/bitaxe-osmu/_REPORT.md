# Capture report — bitaxe-osmu, capture-loop A2 (2026-10-10)

## Files written (9 + this report)

1. `2026-10-10-github-bitaxegamma-603-tag-diff.md` — gamma-603 release record (verbatim no-notes body), Gamma-602...gamma-603 compare (11 commits, 24 files), component-count deltas computed from both tags, verbatim patch excerpts, and the full readme.md at gamma-603.
2. `2026-10-10-github-legitlist-vendor-pr-index.md` — all 49 legitlist PRs (state=all) as a metadata table + signal notes.
3. `2026-10-10-github-legitlist-pr-12-clarify-vendor-approval-criteria.md` — approval criteria + maintainer review checklist (policy).
4. `2026-10-10-github-legitlist-pr-13-tiktok-nostr-social-slug-validation.md` — vendor schema change: social keys + strict slug regex.
5. `2026-10-10-github-legitlist-pr-14-harden-validation-workflow-parser-resilience.md` — CI switched to repo validator; 92-line inline shell validator deleted.
6. `2026-10-10-github-legitlist-pr-45-add-pr-metadata-validation.md` — new scripts/validate-pr.mjs (title prefixes, placeholders, confirmation rows); #44 was its closed-unmerged predecessor.
7. `2026-10-10-github-legitlist-pr-20-add-vendor-bitaxe-de.md` — full vendor application incl. complete bitaxe-de.json + skot/DerekLoadout review comments (later deactivated — see #54).
8. `2026-10-10-github-legitlist-pr-54-deactivate-vendor-bitaxe-de.md` — first soft-deactivation; `"active": false`; rationale cites legitlist #38 "factual trust questions", explicitly not a scam finding.
9. `2025-03-06-github-bitaxe-web-flasher-pr-17-bump-next-from-13-4-12-to-14.md` — dependabot major bump next 13.4.12 → 14.2.21, merged same day; package.json patch verbatim, lockfile summarized.

Skipped legitlist PRs (deliberately): pure one-line vendor adds without specs (#5–#10, #18–#49 vendor forms), #15/#16 (minor guide/workflow polish), #44 (superseded by #45), #52 (noted inside #54 capture).

## One-line findings on the 603 question

- The official `gamma-603` tag IS the ECO'd hardware: commit 4bcb769 (2025-04-29) bumps rev to 603 together with the ECO fixes — NRSTO/NRSTI pulldowns (#36), pullups for #25, USB ID pulldowns (#37: R27/R28 5.6k, R29/R30 5.1k on esp32 sheet), J3 partno fix (#28), mounting-hole cleanup (#32) — plus bm1370-sheet resistors R17–R21/R26 (10k/1k/1k/1k/2k/10k), so there is no separate "official 603 ≠ ECO-603" sch/pcb content; the 602→603 net delta is +10 resistor footprints (131→137), −J7 unused fan header, +6 vias (300→306).
- The 2026-02-17 release published that April-2025 hardware state plus June-2025 cleanup (fan header, silkscreen/DRC by Ben) and Feb-2026 cosmetics (3d models, worksheet); its body is only the auto-generated Full Changelog link (the "no release notes" fact), and the tag ships NO gerbers/BOM — the Manufacturing Files dir was deleted, not regenerated, while readme.md (unchanged in the diff) still points to the now-missing `Manufacturing Files` dir.
- Nothing spec-sheet-related changed: no README/KiCad-project electrical spec edits in the diff at all — the only load-bearing 603 deltas are the ten added 0402 pulldown/pullup resistors and the deleted fan header.
