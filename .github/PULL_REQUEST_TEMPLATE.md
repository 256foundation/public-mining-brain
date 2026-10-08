# Summary

<!-- One or two sentences: what changed and why. -->

## Type of change

- [ ] Ingest (new source(s) into `raw/` + compiled into `wiki/`)
- [ ] Wiki update (merge/cascade into existing article(s))
- [ ] Lint fixes
- [ ] Registry update (`sources/registry.md`)
- [ ] Tooling / docs (`scripts/`, `automation/`, `references/`)

## Sources ingested

<!-- Registry IDs from sources/registry.md, or `unregistered`. -->

## Articles created / updated

<!-- Paths + disposition per article: New / Update / Disputed / No material -->

## Lint

- [ ] `python3 scripts/lint_wiki.py` run — result: <!-- N errors, N warnings -->

## Checklist

- [ ] `raw/` files are new only — nothing committed previously was edited or deleted
- [ ] Every load-bearing number/date/quote exists in the linked `raw/` files
- [ ] Volatile claims carry `> As-Of:` stamps
- [ ] Conflicts recorded as Disputed blocks (not averaged away)
- [ ] `wiki/index.md` and `wiki/log.md` updated
- [ ] No binaries over 5 MB added

## Needs human judgment

<!-- Licensing questions, contested facts, structural proposals. Or "none". -->
