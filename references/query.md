# Query Procedure

Read-only. Queries never write files (archiving is the only exception, and only when explicitly requested).

## Steps

1. **Locate.** Read `wiki/index.md` for candidates, then full-text search `wiki/` with the question's key terms *and their synonyms* (e.g., "efficiency" and "J/TH" and "watts per terahash"; "S19" and "Antminer S19"; "FPPS" and "full pay-per-share"). Never claim the brain has nothing until both the index and full-text search come back empty — and say that you searched.

2. **Read** the articles found, including their Status blocks (Outdated/Disputed), Contradictions sections, and As-Of stamps.

3. **Synthesize.** Prefer wiki content over your own training knowledge. Where they differ, say so.

4. **Cite.** Markdown links to the wiki pages used: `[Article Title](wiki/topic/article.md)` (project-root-relative in conversation; file-relative when writing inside wiki files).

5. **Surface volatility.** For fees, versions, prices, profitability, or stats: state the As-Of date you found. If the wiki is silent or stale on a volatile fact, say so plainly.

6. **Answer in conversation.** Write no files.

## Honesty rules

- If the brain doesn't know, say "the brain doesn't cover this" — never pad with uncited training knowledge presented as brain content.
- If two wiki articles disagree, present both with their Disputed context; don't pick a winner silently.
- If the question needs data the wiki links to but doesn't synthesize (e.g., a live stat), point at the page and the source instead of inventing the number.

## Archiving (only when explicitly asked)

1. Write the answer as a new page per `references/archive-template.md` in the most relevant topic directory.
2. Never merge into existing articles — archive content is a synthesized answer.
3. Update `wiki/index.md` (Summary prefixed `[Archived]`) and append to `wiki/log.md`:

```
## [YYYY-MM-DD] query | Archived: <page title>
```
