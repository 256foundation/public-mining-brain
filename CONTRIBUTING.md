# Contributing to public-mining-brain

Open source, open data, open PRs. This brain is maintained by LLM agents under human review — you can contribute the same way humans do: PRs and issues.

## Ground rules

1. **`raw/` is immutable.** Never edit or delete committed source files. Corrections happen by ingesting a new source and updating the wiki pages it feeds.
2. **Every load-bearing fact cites its source.** Numbers, dates, and quotes must exist verbatim in the `raw/` files linked from the article's `Raw:` header.
3. **Volatile facts carry an As-Of stamp.** Anything that changes over time (fees, firmware versions, prices, stats) gets `> As-Of: YYYY-MM-DD` in the article header.
4. **Conflicts are recorded, not erased.** Disagreements between sources become `Status: Disputed` blocks. Superseded facts become `Status: Outdated` blocks.
5. **Lint must pass.** Run `python3 scripts/lint_wiki.py` before opening a PR; CI runs it too. `--strict` mode fails on errors.
6. **No large binaries.** Nothing over 5 MB in git. Store the extracted text in `raw/` and link the original file.

## Ways to contribute

### Suggest a source

Open an issue with the **"suggest a source"** template. Maintainers review, add it to [`sources/registry.md`](sources/registry.md) with a refresh cadence, and an ingest agent picks it up.

### Ingest a source yourself

1. Save the source (verbatim where licensing allows) to `raw/inbox/YYYY-MM-DD-slug.md` with the metadata header from `references/raw-template.md`.
2. Follow the Ingest procedure in [SKILL.md](SKILL.md) — or let an agent do it.
3. Update `wiki/index.md` and `wiki/log.md`.
4. Run lint. Open a PR.

### Fix or improve a wiki page

PRs directly against the page. Keep the grounding rule: if you add or change a number, the raw source backing it must be in `raw/` and linked. Changes to facts about fast-moving things (fees, firmware) update the As-Of stamp.

### Improve the tooling

`scripts/`, `automation/`, and the `references/` procedures are normal open-source code and docs — PRs welcome.

## Review process

- Automated: lint on every PR.
- Human: a maintainer reviews grounding, structure, and registry impact before merge.
- Agents (scheduled update loops) always deliver work as PRs — never direct pushes to `main`.

## Style

- Markdown only. Relative links. One topic directory deep.
- Units as found in sources (TH/s, J/TH, W, USD) — never silently converted.
- Full canonical hardware model names ("Antminer S21 XP Hyd", not "s21xp").
- Article files kebab-case, named after the concept or model, not the raw file.
