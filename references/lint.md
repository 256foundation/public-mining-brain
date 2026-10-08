# Lint Procedure

Quality checks over the whole wiki. Mechanical checks are implemented in `scripts/lint_wiki.py`; run it first, then do the judgment pass.

```
python3 scripts/lint_wiki.py            # report + safe auto-fixes
python3 scripts/lint_wiki.py --strict   # exit 1 on errors (CI mode)
```

## 1. Mechanical (script, auto-fix where safe)

| Check | Auto-fix |
|---|---|
| Article missing from `index.md` | Add row with `(no summary)` |
| Index row points to nonexistent file | Mark `[MISSING]` — do not delete; human decides |
| Index Updated ≠ article Updated | Sync index to article |
| Broken internal link, unique same-name target | Fix path |
| Broken internal link, zero/multiple targets | Report |
| Broken Raw link, unique same-name file in `raw/` | Fix path |
| Raw link escaping `raw/` (e.g., points at `wiki/`) | Report — always needs a decision |
| Dead See Also link, unique match | Fix; zero matches → remove link; multiple → report |

## 2. Mechanical (script, report-only)

- **Evidence grounding** — high-signal literals (unit-bearing numbers like `17.5 J/TH`, `961.92 EH/s`, `3,250 W`; decimals; version strings; ISO dates; long quotes) that cannot be found in the article's linked raw files. These are *candidates*: derived values, sums, and product names can false-positive. Judge each against the raw context; report only real mismatches.
- **Header completeness** — missing `Sources:` / `Updated:` lines; archive pages need `Archived:` and are exempt from `Raw:`.
- **Volatility** — articles in `firmware/`, `pools/`, `economics/`, `hashrate-market/` missing `As-Of:`; As-Of older than the newest Collected date among linked raws.
- **Unreferenced raw files** — raws not linked from any article (ingestion backlog).
- **Orphan pages** — no inbound links from other wiki articles.
- **Log format** — entries must start with `## [YYYY-MM-DD] <operation> | ...`.

## 3. Judgment (human/agent, report-only)

- Factual contradictions across articles not yet in Status blocks.
- Claims superseded by newer sources but presented as current.
- Missing cross-references between related articles (suggest; don't add silently).
- Concepts frequently mentioned across articles but lacking a dedicated page.
- Archive pages whose cited source articles have been substantially updated since archival.
- Registry drift: registered sources that went dead, or heavily-cited sources not yet registered.

## 4. Post-Lint

Append to `wiki/log.md`:

```
## [YYYY-MM-DD] lint | <N> issues found, <M> auto-fixed
```

## CI

GitHub Actions runs `scripts/lint_wiki.py --strict` on every PR. PRs failing lint are not mergeable.
