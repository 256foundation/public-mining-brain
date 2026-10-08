#!/usr/bin/env python3
"""Lint the public-mining-brain wiki.

Checks index integrity, header completeness, link integrity, raw references,
volatility stamps, orphans, unreferenced raws, log format, and evidence
grounding (high-signal literals greppable in the linked raw files).

Safe fixes (index rows, unique-name link repairs) are applied unless --no-fix.
Report-only checks never auto-fix.

Usage:
    python3 scripts/lint_wiki.py [--root PATH] [--strict] [--no-fix] [--json]

Exit codes: 0 = clean (or only warnings outside --strict), 1 = errors (or
warnings under --strict), 2 = structural failure (wiki not initialized).
Stdlib only; no third-party dependencies.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
INDEX = WIKI / "index.md"
LOG = WIKI / "log.md"

TOPIC_DESCRIPTIONS = {
    "getting-started": "Newcomer path: what mining is, choosing hardware, first run, joining a pool.",
    "hardware": "ASIC manufacturers and models, components, cooling, repair, DIY builds.",
    "firmware": "Stock, open-source, and commercial ASIC firmware; feature matrices; tuning.",
    "mining-software": "Farm management, monitoring, node tooling, marketplaces.",
    "pools": "Per-pool pages, payout schemes, fees, decentralization.",
    "protocols": "Stratum V1/V2, getblocktemplate, job negotiation, template distribution.",
    "economics": "Profitability math, hashprice, difficulty, electricity, curtailment, heat reuse.",
    "history": "Mining eras, key events, companies, geographic shifts.",
    "industry": "Farms, public miners, hosting, colocation, energy interplay.",
    "hashrate-market": "Hashrate derivatives, indexes, forwards, hosting markets.",
    "meta": "How the brain works, data dictionary.",
}
VOLATILE_TOPICS = {"firmware", "pools", "economics", "hashrate-market"}

HEADER_RE = re.compile(r"^>\s*([A-Za-z][A-Za-z-]*):\s*(.*)$")
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+\.md)\)")
INDEX_ROW_RE = re.compile(r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(.*?)\s*\|\s*([0-9]{4}-[0-9]{2}-[0-9]{2})\s*\|")
LOG_ENTRY_RE = re.compile(r"^##\s*\[\d{4}-\d{2}-\d{2}\]\s+\w+")

EVIDENCE_RES = [
    re.compile(r"\d[\d,]*(?:\.\d+)?\s*(?:TH/s|PH/s|EH/s|GH/s|MH/s|J/TH|J/T\b|kW|MW|GW|W\b|BTC\b|sats?\b|USD\b|°C)",
               re.IGNORECASE),
    re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?"),
    re.compile(r"\d{4}-\d{2}-\d{2}"),
    re.compile(r"\bv?\d+\.\d+(?:\.\d+)+\b"),
    re.compile(r'"([^"]{20,})"'),
]

issues: list[dict] = []
fixes = 0


def issue(level: str, kind: str, path: str, msg: str) -> None:
    issues.append({"level": level, "kind": kind, "path": path, "msg": msg})


def parse_header(text: str) -> dict[str, str]:
    header: dict[str, str] = {}
    for line in text.splitlines():
        m = HEADER_RE.match(line)
        if m:
            header[m.group(1)] = m.group(2).strip()
    return header


def split_body(text: str) -> tuple[str, str]:
    """Return (header_block, body) where header_block is the leading > blockquote region."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == "" or lines[i].startswith("# ")):
        i += 1
    return "\n".join(lines[:i]), "\n".join(lines[i:])


def norm_num(s: str) -> str:
    return s.replace(",", "").replace(" ", "")


def load_articles() -> list[dict]:
    articles = []
    if not WIKI.is_dir():
        return articles
    for path in sorted(WIKI.glob("*/*.md")):
        if path.name in ("index.md", "log.md"):
            continue
        text = path.read_text(encoding="utf-8")
        header = parse_header(text)
        _, body = split_body(text)
        tm = TITLE_RE.search(text)
        articles.append({
            "path": path,
            "rel": str(path.relative_to(WIKI)),
            "topic": path.parent.name,
            "title": tm.group(1).strip() if tm else path.stem,
            "header": header,
            "body": body,
            "archive": "Archived" in header,
            "raw_links": [lnk.strip() for lnk in header.get("Raw", "").split(";") if lnk.strip()],
        })
    return articles


def resolve_link(link: str, base: Path) -> Path | None:
    link = link.split("#")[0].strip()
    if not link:
        return None
    target = (base / link).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return None
    return target


def parse_index() -> tuple[list[dict], list[str]]:
    rows, lines = [], []
    if INDEX.exists():
        lines = INDEX.read_text(encoding="utf-8").splitlines()
    for line in lines:
        m = INDEX_ROW_RE.match(line)
        if m:
            rows.append({"title": m.group(1), "target": m.group(2), "summary": m.group(3), "updated": m.group(4)})
    return rows, lines


def find_unique(name: str, candidates: list[Path]) -> Path | None:
    matches = [c for c in candidates if c.name == name]
    return matches[0] if len(matches) == 1 else None


def add_index_row(rows: list[dict], lines: list[str], art: dict) -> None:
    """Append a row for art under its topic section, creating the section if needed."""
    global fixes
    fixes += 1
    row = f"| [{art['title']}]({art['rel']}) | (no summary) | {art['header'].get('Updated', '')} |"
    rows.append({"title": art["title"], "target": art["rel"], "summary": "(no summary)",
                 "updated": art["header"].get("Updated", "")})
    sec_re = re.compile(rf"^##\s+{re.escape(art['topic'])}\s*$")
    for i, line in enumerate(lines):
        if sec_re.match(line):
            # find end of this section's table (last table row before next ## or EOF)
            j = i + 1
            last_table = None
            while j < len(lines) and not lines[j].startswith("## "):
                if lines[j].startswith("|"):
                    last_table = j
                j += 1
            lines.insert((last_table + 1) if last_table is not None else (i + 2), row)
            return
    # section missing entirely
    lines += ["", f"## {art['topic']}", "", TOPIC_DESCRIPTIONS.get(art["topic"], ""), "",
              "| Article | Summary | Updated |", "|---------|---------|---------|", row]


def lint(root_override: Path | None, do_fix: bool, strict: bool, as_json: bool) -> int:
    global fixes
    root = root_override or ROOT
    if root_override:
        globals()["ROOT"], wiki, raw = root_override, root_override / "wiki", root_override / "raw"
        globals()["WIKI"], globals()["RAW"], globals()["INDEX"], globals()["LOG"] = wiki, raw, wiki / "index.md", wiki / "log.md"

    if not WIKI.is_dir() or not RAW.is_dir() or not INDEX.exists() or not LOG.exists():
        print("Wiki structure incomplete (need wiki/, raw/, wiki/index.md, wiki/log.md). Run an ingest first.")
        return 2

    articles = load_articles()
    index_rows, index_lines = parse_index()
    raw_files = [p for p in RAW.glob("*/*") if p.is_file() and p.name != ".gitkeep"]

    # ---- per-article checks ------------------------------------------------
    raw_referenced: set[Path] = set()
    linked_articles: set[Path] = set()

    for art in articles:
        rel = art["rel"]
        h = art["header"]

        if not art["archive"]:
            if "Sources" not in h:
                issue("error", "header", rel, "missing `> Sources:` line")
            if "Raw" not in h or not art["raw_links"]:
                issue("error", "header", rel, "missing `> Raw:` line (non-archive article)")
            if "Updated" not in h:
                issue("error", "header", rel, "missing `> Updated:` line")
        else:
            if "Archived" not in h:
                issue("error", "header", rel, "archive page missing `> Archived:` line")

        if art["topic"] in VOLATILE_TOPICS and "As-Of" not in h:
            issue("warn", "volatility", rel, f"volatile topic `{art['topic']}` missing `> As-Of:` stamp")

        # Raw reference resolution
        resolved_raws: list[Path] = []
        for link in art["raw_links"]:
            m = re.match(r"\[.*?\]\((.+?)\)$", link)
            target_link = m.group(1) if m else link
            target = resolve_link(target_link, art["path"].parent)
            if target is None or not str(target).startswith(str(RAW.resolve())):
                issue("error", "raw-ref", rel, f"Raw link `{target_link}` missing or escapes raw/")
                continue
            if not target.exists():
                fix = find_unique(Path(target_link).name, raw_files) if do_fix else None
                if fix:
                    new_link = f"[{Path(target_link).stem}](../../raw/{fix.parent.name}/{fix.name})"
                    text = art["path"].read_text(encoding="utf-8")
                    text = text.replace(f"]({target_link})", f"]({new_link.split('](', 1)[1]}", 1)
                    art["path"].write_text(text, encoding="utf-8")
                    globals()["fixes"] += 1
                    resolved_raws.append(fix)
                else:
                    issue("error", "raw-ref", rel, f"Raw link `{target_link}` does not exist")
                    continue
            resolved_raws.append(target)
            raw_referenced.add(target)

        # Body link resolution
        for link in MD_LINK_RE.findall(art["body"]):
            target = resolve_link(link, art["path"].parent)
            if target is None:
                continue
            if str(target).startswith(str(WIKI.resolve())) and target.name not in ("index.md", "log.md"):
                linked_articles.add(target)
            if not target.exists():
                fix = find_unique(Path(link).name, [a["path"] for a in articles]) if do_fix else None
                if fix:
                    newrel = Path("link")  # placeholder, replaced below
                    newrel = Path.relpath(fix, art["path"].parent)
                    text = art["path"].read_text(encoding="utf-8")
                    text = text.replace(f"]({link})", f"]({newrel})", 1)
                    art["path"].write_text(text, encoding="utf-8")
                    globals()["fixes"] += 1
                else:
                    issue("error", "link", rel, f"broken link `{link}`")

        # Evidence grounding
        if not art["archive"] and resolved_raws:
            raw_text = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in resolved_raws)
            raw_norm = norm_num(raw_text)
            meta_dates = {h.get("Updated", ""), h.get("As-Of", "")}
            misses = []
            for rex in EVIDENCE_RES:
                for lit in rex.findall(art["body"]):
                    lit = lit if isinstance(lit, str) else lit
                    if lit in meta_dates:
                        continue
                    if lit in raw_text or norm_num(lit) in raw_norm:
                        continue
                    misses.append(lit)
            if misses:
                uniq = list(dict.fromkeys(misses))[:8]
                issue("warn", "evidence", rel, "literals not found in linked raws (candidates): " + ", ".join(f"`{m}`" for m in uniq))

        # As-Of staleness
        if "As-Of" in h and resolved_raws:
            collected = []
            for p in resolved_raws:
                ch = parse_header(p.read_text(encoding="utf-8", errors="replace"))
                if "Collected" in ch:
                    collected.append(ch["Collected"])
            if collected and h["As-Of"] < max(collected):
                issue("warn", "volatility", rel, f"As-Of {h['As-Of']} older than newest raw Collected {max(collected)}")

    # ---- index consistency -------------------------------------------------
    by_rel = {a["rel"]: a for a in articles}
    indexed_rels = set()
    for row in index_rows:
        target = row["target"]
        if target not in by_rel:
            fix = find_unique(Path(target).name, [a["path"] for a in articles]) if do_fix else None
            if fix:
                newrel = str(fix.relative_to(WIKI))
                text = INDEX.read_text(encoding="utf-8")
                text = text.replace(f"]({target})", f"]({newrel})", 1)
                INDEX.write_text(text, encoding="utf-8")
                globals()["fixes"] += 1
                indexed_rels.add(newrel)
            elif "[MISSING]" in row["summary"]:
                issue("warn", "index", "wiki/index.md", f"entry `{target}` still marked MISSING — awaiting human decision")
            else:
                if do_fix:
                    text = INDEX.read_text(encoding="utf-8")
                    old_row = f"| [{row['title']}]({target}) | {row['summary']} | {row['updated']} |"
                    new_row = f"| [{row['title']}]({target}) | [MISSING] {row['summary']} | {row['updated']} |"
                    if old_row in text:
                        INDEX.write_text(text.replace(old_row, new_row, 1), encoding="utf-8")
                        globals()["fixes"] += 1
                issue("warn", "index", "wiki/index.md", f"entry `{target}` points to a nonexistent file — marked [MISSING]")
        else:
            indexed_rels.add(target)
            art = by_rel[target]
            expected = art["header"].get("Updated", "")
            if expected and row["updated"] != expected and do_fix:
                text = INDEX.read_text(encoding="utf-8")
                old_row = f"| [{row['title']}]({row['target']}) | {row['summary']} | {row['updated']} |"
                new_row = f"| [{row['title']}]({row['target']}) | {row['summary']} | {expected} |"
                text = text.replace(old_row, new_row, 1)
                INDEX.write_text(text, encoding="utf-8")
                globals()["fixes"] += 1
            elif expected and row["updated"] != expected:
                issue("warn", "index", "wiki/index.md", f"Updated mismatch for `{target}`: index {row['updated']} vs article {expected}")

    for art in articles:
        if art["rel"] not in indexed_rels:
            if do_fix:
                _, index_lines = parse_index()
                add_index_row(index_rows, index_lines, art)
                INDEX.write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
            else:
                issue("warn", "index", art["rel"], "article missing from index")

    # ---- orphans & unreferenced raws ---------------------------------------
    for art in articles:
        if art["path"] not in linked_articles:
            issue("info", "orphan", art["rel"], "no inbound links from other wiki articles")

    for p in raw_files:
        if p not in raw_referenced and p.parent.name != "inbox":
            issue("info", "raw-backlog", str(p.relative_to(ROOT)), "raw file not referenced by any article")

    # ---- log format ---------------------------------------------------------
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if line.startswith("## [") and not LOG_ENTRY_RE.match(line):
            issue("warn", "log", "wiki/log.md", f"malformed log entry: {line[:60]}")

    # ---- report -------------------------------------------------------------
    errors = [i for i in issues if i["level"] == "error"]
    warns = [i for i in issues if i["level"] == "warn"]
    infos = [i for i in issues if i["level"] == "info"]

    if as_json:
        print(json.dumps({"errors": errors, "warnings": warns, "info": infos, "fixes_applied": fixes}, indent=2))
    else:
        for level, group in (("ERROR", errors), ("WARN", warns), ("INFO", infos)):
            for i in group:
                print(f"{level:5} [{i['kind']}] {i['path']}: {i['msg']}")
        print(f"\n{len(errors)} errors, {len(warns)} warnings, {len(infos)} info | {fixes} auto-fixes applied")

    if errors:
        return 1
    if strict and warns:
        return 1
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=None, help="project root (default: repo root)")
    ap.add_argument("--strict", action="store_true", help="exit 1 on warnings too (CI mode)")
    ap.add_argument("--no-fix", action="store_true", help="report only; apply no auto-fixes")
    ap.add_argument("--json", action="store_true", help="JSON output")
    args = ap.parse_args()
    return lint(args.root, not args.no_fix, args.strict, args.json)


if __name__ == "__main__":
    sys.exit(main())
