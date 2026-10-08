# Ingest Procedure

Detailed checklist for the Ingest operation. The contract is [SKILL.md](../SKILL.md); this document is the step-by-step.

## 1. Acquire

- Use the environment's web/file tools to fetch the source.
- Registered sources: check `sources/registry.md` for the source's **Posture** (`verbatim` / `extract` / `link-only`) before capture.
  - `verbatim` — copy the full text (manufacturer manuals, spec sheets, docs, openly licensed material).
  - `extract` — capture the facts, tables, and figures with attribution; keep structure of tables intact.
  - `link-only` — store metadata + link only; used for paywalled or huge sources.
- If nothing can reach the source, ask the user to paste it.
- **No binaries > 5 MB in git.** For a large PDF: extract text (and key tables), store the extraction, and put the original URL in the header.

## 2. Save to raw/

1. New files always land in `raw/inbox/` first: `raw/inbox/YYYY-MM-DD-descriptive-slug.md`.
2. Use the header from `references/raw-template.md` (Source, Registry ID, Collected, Published).
3. Verbatim content; formatting cleanup only; never rewrite meaning.
4. Name collisions get a numeric suffix (`-2.md`).

## 3. Triage

Search the wiki for the source's key entities and synonyms (grep both `wiki/` and `wiki/index.md`). State the disposition explicitly:

| Disposition | Meaning | Action |
|---|---|---|
| New | Knowledge not yet in the wiki | Create article(s) |
| Update | Extends/reinforces existing article(s) | Merge in, refresh Updated/As-Of |
| Disputed | Contradicts existing content | Update or create, add Status blocks on both sides |
| No material | Nothing new | Keep raw file, log, stop |

`New`, `Update`, and `Disputed` may combine. `No material` is exclusive. Never force an article out of a thin source.

During triage also **move the raw file** from `raw/inbox/` to its topic directory (`raw/<topic>/`) using the topic map in SKILL.md. The inbox should be empty after each ingest.

## 4. Compile

Determine placement (merge / new / split with cross-references) per SKILL.md. Before writing any value, **locate it in the raw file** — grep or read. Write values exactly as found. Derived values show their components. If a value can't be located, drop it or state it without precision.

Hardware and firmware specifics:

- One article per ASIC model. Spec numbers (TH/s, J/TH, W, voltage, temperature range) each traceable to a raw source; conflicting numbers across sources get Disputed blocks, not averaging.
- Firmware articles: version-locked claims ("Braiins OS 25.03 adds X" as of 2025-03) + a supported-models table.
- Pool articles: fee and payout scheme claims carry As-Of; payout scheme definitions (FPPS, PPS+, SOLO, FIRC) live in `pools/` concept articles, referenced from per-pool pages.
- Never compute "profitability" without showing the full inputs (hashrate, efficiency, power cost, block reward, fees, BTC price) and their As-Of dates.

Apply the Volatility Rule and the Contradiction Rule (SKILL.md). Article format: `references/article-template.md`.

## 5. Cascade

Search the full wiki for the source's key entities, aliases, and affected claims. Update every materially affected article: refresh `Updated`, add Outdated/Disputed blocks where superseded. Archive pages are never cascade-updated.

## 6. Register

If the source will be re-checked later, add it to `sources/registry.md` with cadence + posture (see the schema at the top of that file). Update the row if the source already exists.

## 7. Post-Ingest

1. `wiki/index.md` — add/update rows for every touched article (link, one-line summary, Updated date).
2. `wiki/log.md` — append the operation entry (format in SKILL.md).
3. Run `python3 scripts/lint_wiki.py` and resolve what it reports before committing.

## Parallelism rule

Searching may run in parallel; **compilation must not** — `index.md` and `log.md` are shared state. Compile one source at a time.
