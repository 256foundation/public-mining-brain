---
name: public-mining-brain
description: "Use when ingesting bitcoin-mining sources into this wiki, querying the brain, linting wiki quality, or exporting the knowledge pack. Triggers: 'ingest', 'add to the brain', 'what does the brain know about', 'lint the wiki', 'update the registry', or any bitcoin-mining knowledge question aimed at this repo."
---

# Public Mining Brain

Build and maintain a public knowledge base on **bitcoin mining** using the LLM-wiki method. You manage two directories: `raw/` (immutable source material) and `wiki/` (compiled knowledge articles). Sources go into `raw/`, you compile them into `wiki/` articles, and the wiki compounds over time.

Core ideas from Karpathy:
- "The LLM writes and maintains the wiki; the human reads and asks questions."
- "The wiki is a persistent, compounding artifact."

Adapted for bitcoin mining from [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) (MIT).

## Architecture

Three layers, all under the repo root:

**`raw/`** — Immutable source material. You read, never modify (once committed). Organized by topic subdirectories matching the topic map below. Sources are ingested **verbatim by default** (manufacturer manuals, spec sheets, documentation) with attribution — see [CONTRIBUTING.md](CONTRIBUTING.md). New files land in `raw/inbox/` and are moved to their topic directory during triage.

**`wiki/`** — Compiled knowledge articles. You have full ownership. One level of topic subdirectories only: `wiki/<topic>/<article>.md`. Contains two special files:
- `wiki/index.md` — Global index. One row per article, grouped by topic, with link + summary + Updated date.
- `wiki/log.md` — Append-only operation log.

**`SKILL.md`** (this file) — Schema layer. Templates and procedures live in `references/`.

### The Grounding Invariant

Every load-bearing fact in `wiki/` — numbers, dates, direct quotes — exists verbatim in the `raw/` files linked by that article's Raw field. Compile *establishes* this (locate every value before you write it); lint *verifies* it (`scripts/lint_wiki.py` greps high-signal literals in the linked raws). Because `raw/` is immutable, a verified article stays verified.

### The Volatility Rule (mining-specific)

Bitcoin mining facts rot at different speeds. Every claim that changes over time — firmware versions, pool fees and payout schemes, hardware prices, profitability figures, hashrate/difficulty stats, market cap tables — must carry an explicit **`> As-Of: YYYY-MM-DD`** stamp in the article header. Articles in `firmware/`, `pools/`, `economics/`, and `hashrate-market/` always require an As-Of stamp. Never present a volatile value as timeless.

### The Contradiction Rule (mining-specific)

Specs disagree — manufacturer spec sheet vs user manual vs reseller listing vs field reports. When sources conflict, do not average or guess. Record the conflict:

```
> **Status: Disputed**
> {Claim A, source attribution. Claim B, source attribution. Current best assessment and why.}
```

Never silently replace one number with another. Outdated facts that were once correct get:

```
> **Status: Outdated** (YYYY-MM-DD)
> {What changed, and the current understanding, with source attribution.}
```

### Canonical Units and Naming

- **Hashrate**: TH/s for per-machine; PH/s or EH/s for farms and network. Write the unit the source used — never convert silently.
- **Efficiency**: J/TH. **Power**: W (kW/MW for sites). **Temperature**: °C. **Money**: USD with the unit the source used.
- **Model names**: full canonical form — "Antminer S21 XP Hyd", "Whatsminer M66S+", "Avalon A15Pro", "SEALMINER A2 Pro". Article files kebab-case: `antminer-s21-xp-hyd.md`.
- **One article per ASIC model**, linked from the manufacturer's overview article. Firmware articles carry a supported-models table.
- Firmware version claims name the exact version string as published (e.g., `Braiins OS 23.09`, not "recent Braiins").

### Topic Map

| Directory | Covers |
|---|---|
| `getting-started/` | Newcomer path: what mining is → choosing hardware → first run → joining a pool → safety |
| `hardware/` | ASIC manufacturers and models, chip generations, PSUs, control boards, cooling (air/hydro/immersion), hosting readiness, repair and diagnostics, DIY builds |
| `firmware/` | Stock firmware (Bitmain, MicroBT), open source (cgminer, BFGMiner, Braiins OS), closed commercial (LuxOS, Vnish), feature matrices, tuning, dev/reverse-engineering |
| `mining-software/` | Farm management and monitoring (Foreman, Braiins Manager, Luxor Commander, Awesome Miner), node tooling, marketplaces |
| `pools/` | Per-pool articles, payout schemes (FPPS, PPS+, SOLO, FIRC), fee structures, decentralization |
| `protocols/` | Stratum V1, Stratum V2, getblocktemplate (BIP 22/23), job negotiation, template distribution, BetterHash |
| `economics/` | Profitability math, hashprice, difficulty, electricity costs, curtailment/demand response, heat reuse, flared gas, financing |
| `history/` | CPU → GPU → FPGA → ASIC eras, key events (China ban, halvings), companies, geographic shifts |
| `industry/` | Mining farms, public miners and filings, hosting/colocation, energy interplay |
| `hashrate-market/` | Hashrate derivatives, indexes, forwards, hosting markets |
| `meta/` | How this brain works, data dictionary, operating guides |

---

## Ingest

Fetch a source into `raw/`, then compile it into `wiki/` — unless the source adds nothing new. Always fetch; whether to compile depends on triage.

### Fetch (raw/)

1. Get the source content with whatever web or file tools your environment provides. If nothing can reach it, ask the user to paste it.

2. New material lands in `raw/inbox/` first. During triage, move it to its topic directory (`raw/<topic>/`). Reuse an existing topic directory when the topic is close enough; create one only for genuinely distinct topics.

3. Save as `raw/<topic>/YYYY-MM-DD-descriptive-slug.md`:
   - Slug from source title, kebab-case, max 60 chars. Unknown publish date → omit date prefix, set Published to `Unknown`.
   - Name collision → append numeric suffix (`-2.md`).
   - Metadata header: source URL, collected date, published date, **source id from `sources/registry.md` when the source is registered**.
   - Preserve original text verbatim; clean formatting noise only. Never rewrite opinions or meaning.
   - **Binary limit**: no binaries in git over 5 MB. Extract the text, store the extraction, link the original.

   Format: `references/raw-template.md`.

### Triage

After saving the raw file and before editing `wiki/`, search the wiki for the source's key entities and synonyms, then state the disposition:

- **New** — creates one or more new articles.
- **Update** — merges into existing article(s).
- **Disputed** — contradicts existing content; may combine with New or Update (Contradiction Rule).
- **No material** — adds nothing beyond what the wiki holds. Keep the raw file, log it, stop. Never force an article out of a thin source.

### Compile (wiki/)

- **Same core thesis as an existing article** → merge into it; add the source to Sources/Raw; update affected sections and the As-Of stamp.
- **New concept** → new article in the most relevant topic directory, named after the concept (not the raw file).
- **Spans multiple topics** → place in the most relevant directory; add See Also cross-references to the others.

**Source fidelity.** Every number, date, and direct quote must be located in the raw file (grep or read) *before* it is written; write values exactly as found — if the source says 17.5 J/TH, write 17.5 J/TH, not 17.50 or "about 17.5". Derived values (sums, deltas, computed profitability) must show their components so each component is findable in `raw/`. If you cannot locate a value, do not write its exact form.

**Volatile values.** A number that was true at collection (pool fee, price, firmware version) is written with its As-Of date in the article header and, when the page mixes vintages, inline next to the value.

Format: `references/article-template.md`. Key points:
- `> Sources:` author/publication + date, semicolon-separated.
- `> Raw:` markdown links to raw/ files, semicolon-separated.
- `> Updated:` date the knowledge content last changed.
- `> As-Of:` required per the Volatility Rule.
- Relative paths from `wiki/<topic>/` use `../../raw/<topic>/<file>.md`.

### Cascade Updates

After the primary article, search the full wiki for the source's key entities, aliases, and claims it touches; update every article materially affected, refreshing its Updated date. Superseded claims get a Status block (Outdated/Disputed) — never silently rewrite history.

### Post-Ingest

Update `wiki/index.md` (add/update rows for every touched article) and append to `wiki/log.md`:

```
## [YYYY-MM-DD] ingest | <primary article title>
- Disposition: <New; Update; Disputed>
- Raw: <raw file path>
- Updated: <cascade-updated article title>
```

For No material:

```
## [YYYY-MM-DD] ingest | no material: <raw file path>
- Disposition: No material
```

### Research (multi-source ingest)

Use only when explicitly asked to research a topic or grow the registry. Split the topic into angles; search wide (official names, abbreviations, synonyms); for core conclusions deliberately search the opposing side (failures, criticism, debunkings). Save sources to `raw/` as usual. Searching may run in parallel; compilation must not — compile one source at a time because `index.md` and `log.md` are shared state.

### Registry Maintenance

When a source proves durable (will be re-checked), add it to `sources/registry.md` with its cadence and posture. When a registered source goes stale or dead, mark its Status `dormant`/`dead` — never delete rows.

---

## Query

Search the wiki and answer questions. Triggers: "what do I know about X", "how does Y work", "compare A and B".

1. Read `wiki/index.md`, then full-text search `wiki/` with key terms *and synonyms*. Never claim the brain knows nothing until both come back empty — and say that you searched.
2. Read the articles found; synthesize.
3. Prefer wiki content over training knowledge. Cite with markdown links: `[Article Title](wiki/topic/article.md)` (project-root-relative in conversation; file-relative inside wiki files).
4. If the wiki is silent or stale on a volatile fact, say so and state the As-Of date of what you found.
5. Answer in conversation. Write no files unless asked.

**Archiving** (only when explicitly asked): write the answer as a new page per `references/archive-template.md`, prefix the index Summary with `[Archived]`, log:

```
## [YYYY-MM-DD] query | Archived: <page title>
```

---

## Lint

Quality checks. Three authority levels. Mechanical checks run via `python3 scripts/lint_wiki.py [--strict]`.

### Safe Fixes (auto-fix)

- **Index consistency** — article missing from index → add with `(no summary)`; index entry to a nonexistent file → mark `[MISSING]`, decide later; index Updated ≠ article Updated → sync index to article.
- **Internal links** — broken target with exactly one same-name file elsewhere in `wiki/` → fix path; zero or multiple → report.
- **Raw references** — broken Raw link with exactly one same-name match in `raw/` → fix; else report.
- **See Also** — dead cross-reference with exactly one match → fix; zero matches → remove the link; multiple → report.

### Mechanical Reports (never auto-fix)

- **Evidence grounding** — high-signal literals (unit-bearing numbers, decimals, versions, ISO dates, long quotes) that cannot be found in the linked raw files. Candidates, not verdicts — judge against raw context.
- **Evidence errors** — missing Raw field, unresolvable Raw links, Raw links escaping `raw/`. Always need a decision.
- **Unreferenced raw files** — ingestion backlog.
- **Volatility** — articles in `firmware/`, `pools/`, `economics/`, `hashrate-market/` missing an As-Of stamp; or As-Of older than the newest linked raw source.

### Judgment Reports (never auto-fix)

Factual contradictions across articles; outdated claims lacking Status blocks; missing cross-references (suggest, don't add); orphan pages; frequently-mentioned concepts lacking a page; archive pages whose sources moved on.

### Post-Lint

```
## [YYYY-MM-DD] lint | <N> issues found, <M> auto-fixed
```

---

## Export

Compile `wiki/` into the machine-readable knowledge pack for external consumers (front end, API, other agents):

```
python3 scripts/build_export.py
```

Produces `export/knowledge-pack.json` (pages, index, backlinks, metadata, content hash) plus `export/MANIFEST.md`. The pack is a build artifact — never hand-edit it; regenerate. Tag releases when the pack format or content changes materially.

---

## Conventions

- Standard markdown, relative links throughout; one level of topic subdirectories.
- Today's date for log entries and Collected dates; Published from the source (`Unknown` if absent); Updated only on knowledge changes.
- In conversation, cite project-root-relative; inside wiki files, file-relative.
- Ingest updates index + log (No material: log only). Archive updates both. Lint updates log (and index only when auto-fixing). Query writes nothing.
- `raw/` is append-only. `export/` is regenerated, never hand-edited.
