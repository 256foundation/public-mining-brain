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
| **Capture layer** | Continuous | Telegram/Discord/X watchers and GitHub monitors feed `raw/inbox/` (see below) |

## Capture Layer (community & social sources)

Chat and social sources are captured by dedicated bots/watchers (run on the automation infrastructure — e.g., buzz relay), which feed this repo through the same PR-only contract:

1. **History exports** — one-time dumps (Telegram chat export, Discord server export, X archive) land in `raw/inbox/` as dated archive files, then get triaged like any source.
2. **Live watchers** — Telegram bots (256F, Heatpunks groups), the X scraper (follows + tags of `256f-x` / `heatpunks-x`), and GitHub monitors (commits/PRs/issues/discussions of every repo in the registry's Open-Source Projects section) append incremental captures to `raw/inbox/`:
   - `raw/inbox/YYYY-MM-DD-<source-id>-digest.md` — periodic digests (recommended: daily or weekly batch per source)
   - `raw/inbox/YYYY-MM-DD-<source-id>-<slug>.md` — individual high-signal captures (release notes, major announcements, block found, significant threads)
3. **Posture per registry**: Discourse forums and X are public → `verbatim` allowed. Telegram/Discord are gated communities → `extract` by default (knowledge extracted with attribution to public handles; personal details, wallet info, and private matters stripped). Tyler can flip any specific source to `verbatim`.
4. Watchers open PRs on the same loop cadence (batched — one PR per loop run, not per message).
5. **Signal triage**: most chat volume is noise. The watcher (or the ingest agent on scan) extracts *knowledge claims, decisions, field reports, links, and community consensus* — not transcripts. A claim that matters gets compiled into a wiki article per the normal Ingest flow; chatter that adds nothing gets logged as No material with the digest kept in raw/.


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
