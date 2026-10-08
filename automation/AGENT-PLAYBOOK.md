# Agent Playbook — Scheduled Update Loops

The SOP for any scheduled agent (buzz relay automation or otherwise) that keeps the brain current. The repo is self-describing: everything an agent needs lives in `SKILL.md`, `references/`, and `sources/registry.md`.

**Agents never push to `main`.** All work lands as PRs. Humans review and merge.

## Preconditions

The runner environment needs:

1. A clean checkout of this repo (and push rights to open PRs).
2. Python 3 for `scripts/lint_wiki.py`.
3. An LLM session with `SKILL.md` loaded (Agent Skills-compatible, or manually attached).
4. Web/file access for fetching sources.

## Cadences

| Loop | Cadence | Scope |
|---|---|---|
| **Freshness scan** | Weekly | Registry sources with cadence `weekly`/`event`; volatile topics (`firmware/`, `pools/`, `economics/`, `hashrate-market/`) |
| **Deep sweep** | Monthly | Full registry; lint judgment pass; orphan/backlog cleanup |
| **Event-driven** | On trigger | Breaking changes: new firmware releases, pool policy changes, difficulty epochs, major industry news |

## Freshness scan SOP

1. **Sync**: `git checkout main && git pull --ff-only`.
2. **Scan**: read `sources/registry.md`. For each `active` row whose cadence matches this loop, fetch the URL and diff against what the wiki already holds (grep key entities). Note rows that fail to fetch → plan a registry status change.
3. **Triage** each changed source per `SKILL.md` → Ingest: New / Update / Disputed / No material. New raw files go to `raw/inbox/`, then move to topic dirs during triage.
4. **Compile** one source at a time (index/log are shared state). Follow `references/ingest.md` exactly — locate every value before writing, apply Volatility + Contradiction rules.
5. **Cascade**: update affected cross-referenced articles.
6. **Register**: add/update `sources/registry.md` rows for newly durable sources; mark dead sources `dormant` (never delete rows).
7. **Lint**: `python3 scripts/lint_wiki.py` — resolve errors, note warnings. Then append the post-lint entry to `wiki/log.md`.
8. **Branch + commit**: one branch per loop run:
   - `bot/scan-YYYY-MM-DD` (freshness), `bot/sweep-YYYY-MM-DD` (deep sweep), `bot/event-<slug>` (event-driven)
   - Commit style: `wiki: <summary>`, `raw: ingest <registry-id>`, `registry: <change>`, `lint: <summary>`
9. **Open PR** using `.github/PULL_REQUEST_TEMPLATE.md` with: sources ingested (registry ids), articles created/updated, dispositions, lint result, and anything needing human judgment.

## Deep sweep additions

After step 7 above, also run the **judgment pass** from `references/lint.md` (contradictions, missing cross-refs, orphan pages, concepts lacking pages, stale As-Of stamps) and include findings + proposed fixes in the PR description.

## Guardrails

- Never edit or delete committed `raw/` files. Never force-push. Never push `main`.
- Never hand-edit `export/` (build artifact; Phase 3 tooling regenerates it).
- Compilation is serial; fetching/searching may be parallel.
- If a source is paywalled/unreachable, respect its registry Posture (`extract`/`link-only`) — do not fabricate.
- If a merge conflict appears in `wiki/index.md` or `wiki/log.md`, rebase onto fresh `main` and replay; these files are append-mostly.
- Max PR size guidance: one loop run per PR; split if the diff exceeds ~50 files.
- Anything uncertain that a human should decide goes in the PR description under "Needs human judgment" — do not guess on licensing or contested facts.

## Escalation

- Registry source dead twice in a row → mark `dormant`, note in PR.
- Contradiction the agent cannot assess → Disputed block + flag in PR.
- Structural changes (new topic directory, taxonomy moves) → open an issue for human approval instead of a PR.
