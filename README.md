# public-mining-brain

A public, LLM-maintained knowledge base covering **bitcoin mining end to end** — hardware and ASICs, firmware (open and closed source), pools, protocols, economics and profitability, history, and the industry.

Built as a [Karpathy-style LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): instead of re-searching raw documents on every question, an LLM agent ingests sources into `raw/`, compiles durable, citation-backed knowledge pages into `wiki/`, and keeps them cross-linked and internally consistent over time. Workflow adapted from [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki).

## Who it's for

- People getting into bitcoin mining
- People who want to build, modify, or develop bitcoin miners themselves
- Any agent, human, or application that needs grounded, citable answers about bitcoin mining

## How it works

| Operation | What it does | Spec |
|---|---|---|
| **Ingest** | Collects a source into `raw/`, triages it, compiles or updates wiki articles | [SKILL.md](SKILL.md) |
| **Query** | Answers questions with citations linking back to wiki pages | [SKILL.md](SKILL.md) |
| **Lint** | Verifies index integrity, link integrity, and evidence grounding; auto-fixes what is safe | [scripts/lint_wiki.py](scripts/lint_wiki.py) |
| **Update loop** | Scheduled agents scan the source registry and open PRs with new knowledge | [automation/AGENT-PLAYBOOK.md](automation/AGENT-PLAYBOOK.md) |

## Repository layout

```
raw/                  Immutable source material, verbatim, organized by topic
  └── inbox/          Staging area — new sources land here before triage
wiki/                 Compiled knowledge pages (the brain)
  ├── index.md        Global table of contents
  └── log.md          Append-only operation log
sources/registry.md   The persistent source registry the update loop pulls from
references/           Templates and operating procedures (ingest / query / lint)
scripts/              Lint tooling (plain Python, stdlib only)
automation/           Playbook for scheduled ingest agents
SKILL.md              The skill spec — point your agent here
```

## Using the brain

The wiki is plain markdown. Two ways to use it:

1. **Through an agent** — point Claude Code, Cursor, Codex, OpenCode, or any Agent Skills-compatible tool at this repo with `SKILL.md` loaded. Ask it questions; answers come back with citations into `wiki/`.
2. **Directly** — `grep` and read. Start at [`wiki/index.md`](wiki/index.md).

## Grounding rule

Every load-bearing fact in `wiki/` — every number, date, and quote — exists verbatim in the `raw/` files linked by that page. `raw/` is immutable. Answers are only as good as their sources, and every page shows its sources.

## Contributing

Open PRs are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). To suggest a new source for the brain to follow, open an issue using the "suggest a source" template.

## Status

v0.1 — skeleton, taxonomy, and initial source registry. Bulk ingest in progress.
