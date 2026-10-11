#!/usr/bin/env python3
"""Build the machine-readable knowledge pack from wiki/.

Produces the single interface between this content repo and external consumers
(256-wiki front end, REST API, other agents):

    export/knowledge-pack.json   schema-versioned pack (meta, topics, pages)
    export/MANIFEST.md           human-readable build manifest

The pack is a build artifact — never hand-edit it; regenerate. The contentHash
covers every topic and page field, so consumers can pin and verify the exact
content version they rendered or answered from (provenance contract).

Schema v1:

{
  "meta": { "version": 1, "generated": "ISO-8601", "contentHash": "sha256:…",
            "sourceCommit": "abc1234|null", "pageCount": N, "topicCount": N },
  "topics": [ { "id": "hardware", "name": "Hardware", "description": "…" } ],
  "pages": [ {
    "slug": "antminer-s21-xp-hyd", "topic": "hardware",
    "title": "Antminer S21 XP Hyd", "summary": "…",
    "updated": "2026-10-10", "asOf": "2026-10-10",
    "statuses": ["draft", "disputed"],         // header Status + body **Status:** blocks
    "sources": ["…"], "rawLinks": ["raw/…"],   // rawLinks are repo-root-relative
    "backlinks": ["antminer-s23-xp-hyd"],      // slugs of pages linking here
    "body": "markdown verbatim"
  } ]
}

Usage:
    python3 scripts/build_export.py [--root PATH] [--out PATH] [--check]

Exit codes: 0 = built (or --check found a fresh pack), 1 = build errors
(or --check found a stale pack), 2 = structural failure (wiki not initialized).
Stdlib only; no third-party dependencies.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
INDEX = WIKI / "index.md"

SCHEMA_VERSION = 1
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
HEADER_RE = re.compile(r"^>\s*([A-Za-z][A-Za-z-]*):\s*(.*)$")
INDEX_ROW_RE = re.compile(
    r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|"
)
RAW_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+\.md)\)")
BODY_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+\.md)\)")
BODY_STATUS_RE = re.compile(r"^>\s*\*\*Status:\s*([^*]+?)\*\*")
SPECIAL_PAGES = {"index.md", "log.md"}

# Keep in sync with TOPIC_DESCRIPTIONS in scripts/lint_wiki.py (duplicated so
# this script stays standalone, like every script in this repo).
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

errors: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def parse_header(text: str) -> dict[str, str]:
    header: dict[str, str] = {}
    for line in text.splitlines():
        m = HEADER_RE.match(line)
        if m:
            header[m.group(1)] = m.group(2).strip()
    return header


def split_body(text: str) -> tuple[str, str]:
    """Return (header_block, body); header_block is the leading > blockquote region."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == "" or lines[i].startswith("# ")):
        i += 1
    return "\n".join(lines[:i]), "\n".join(lines[i:])


def parse_summaries() -> dict[tuple[str, str], str]:
    """Map (topic, filename) → summary from wiki/index.md rows."""
    summaries: dict[tuple[str, str], str] = {}
    if not INDEX.exists():
        return summaries
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        m = INDEX_ROW_RE.match(line)
        if not m:
            continue
        parts = m.group(2).strip().split("/")
        if len(parts) != 2:
            continue
        summaries[(parts[0], parts[1])] = m.group(3).strip()
    return summaries


def parse_as_of(value: str) -> str | None:
    """Leading YYYY-MM-DD from an As-Of stamp; annotations after the date are dropped."""
    m = re.match(r"(\d{4}-\d{2}-\d{2})", value)
    return m.group(1) if m else None


def parse_statuses(text: str, header: dict[str, str]) -> list[str]:
    """Header Status plus every body `**Status: X**` marker, lowercased, deduped."""
    found: list[str] = []
    if header.get("Status"):
        found.append(header["Status"])
    for line in text.splitlines():
        m = re.match(r"^>\s*\*\*Status:\s*([^*]+?)\*\*", line)
        if m:
            found.append(m.group(1))
    out: list[str] = []
    for s in found:
        s = re.sub(r"\s+", " ", s).strip(" :—-").strip().lower()
        if s and s not in out:
            out.append(s)
    return out


def normalize_raw_link(link: str) -> str | None:
    """File-relative Raw link → repo-root-relative path ('raw/<topic>/<file>.md')."""
    link = link.split("#")[0].strip()
    if not link:
        return None
    parts: list[str] = [p for p in link.split("/") if p not in ("", ".")]
    while parts and parts[0] == "..":
        parts.pop(0)  # drop the escape
        if parts and parts[0] not in ("..",):
            parts.pop(0)  # drop the topic dir being escaped
    return "raw/" + "/".join(parts) if parts else None


def build_pages() -> list[dict]:
    summaries = parse_summaries()
    pages: list[dict] = []
    for path in sorted(WIKI.glob("*/*.md")):
        if path.name in SPECIAL_PAGES:
            continue
        topic = path.parent.name
        text = path.read_text(encoding="utf-8")
        header = parse_header(text)
        _, body = split_body(text)
        tm = TITLE_RE.search(text)
        title = tm.group(1).strip() if tm else path.stem
        if title.endswith("."):
            title = title.rstrip(".")
        updated = header.get("Updated", "").strip()
        as_of = parse_as_of(header.get("As-Of", "").strip())
        if header.get("As-Of", "").strip() and not as_of:
            warn(f"{path.relative_to(ROOT)}: As-Of '{header['As-Of']}' has no YYYY-MM-DD date")
        raw_links: list[str] = []
        for link in RAW_LINK_RE.findall(header.get("Raw", "")):
            rel = normalize_raw_link(link)
            if rel and rel not in raw_links:
                raw_links.append(rel)
        pages.append({
            "slug": path.stem,
            "topic": topic,
            "title": title,
            "summary": summaries.get((topic, path.name), ""),
            "updated": updated or None,
            "asOf": as_of or None,
            "statuses": parse_statuses(text, header),
            "sources": [s.strip() for s in header.get("Sources", "").split(";") if s.strip()],
            "rawLinks": raw_links,
            "backlinks": [],  # filled after all pages load
            "body": body.strip("\n"),
        })
    return pages


def add_backlinks(pages: list[dict]) -> None:
    """A backlink of page B is any page A whose body links to B's article file."""
    by_key = {(p["topic"], p["slug"]): p for p in pages}
    for src in pages:
        seen: set[str] = set()
        for link in BODY_LINK_RE.findall(src["body"]):
            target = link.split("#")[0].strip()
            parts = [p for p in target.split("/") if p not in ("", ".")]
            if not parts or parts[-1] in SPECIAL_PAGES:
                continue
            stem = Path(parts[-1]).stem
            if len(parts) == 1:
                dst = (src["topic"], stem)                      # same-topic article link
            elif parts[0] == ".." and len(parts) == 2:
                dst = (src["topic"], stem)                      # ../<topic>/<file>.md escape
            elif len(parts) == 2:
                dst = (parts[0], stem)                          # <topic>/<file>.md from wiki root
            else:
                continue
            dst_page = by_key.get(dst)
            if dst_page is None or dst_page["slug"] == src["slug"]:
                continue
            if dst_page["slug"] not in seen:
                seen.add(dst_page["slug"])
                dst_page["backlinks"].append(src["slug"])
    for p in pages:
        p["backlinks"].sort()


def content_hash(pack: dict) -> str:
    canonical = json.dumps(
        {"topics": pack["topics"], "pages": pack["pages"]},
        sort_keys=True, ensure_ascii=False, separators=(",", ":"),
    )
    return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def git_commit(root: Path) -> str | None:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=root, capture_output=True, text=True, check=True,
        )
        return out.stdout.strip() or None
    except Exception:
        return None


def build_pack(root: Path) -> dict:
    if not WIKI.is_dir():
        print(f"error: {WIKI} does not exist — wiki not initialized", file=sys.stderr)
        raise SystemExit(2)
    pages = build_pages()
    slugs = [p["slug"] for p in pages]
    dupes = sorted({s for s in slugs if slugs.count(s) > 1})
    if dupes:
        fail(f"duplicate article slugs across topics: {dupes} — slugs must be unique")
    add_backlinks(pages)
    topics = [
        {
            "id": tid,
            "name": tid.replace("-", " ").title(),
            "description": TOPIC_DESCRIPTIONS.get(tid, ""),
        }
        for tid in sorted({p["topic"] for p in pages})
    ]
    pages.sort(key=lambda p: (p["topic"], p["slug"]))
    pack: dict = {
        "meta": {
            "version": SCHEMA_VERSION,
            "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "contentHash": "",
            "sourceCommit": git_commit(root),
            "pageCount": len(pages),
            "topicCount": len(topics),
        },
        "topics": topics,
        "pages": pages,
    }
    pack["meta"]["contentHash"] = content_hash(pack)
    return pack


def write_manifest(pack: dict, out_dir: Path) -> None:
    counts: dict[str, int] = {}
    for p in pack["pages"]:
        counts[p["topic"]] = counts.get(p["topic"], 0) + 1
    disputed = sum(1 for p in pack["pages"] if "disputed" in p["statuses"])
    outdated = sum(1 for p in pack["pages"] if "outdated" in p["statuses"])
    lines = [
        "# Knowledge Pack Manifest",
        "",
        f"- Generated: {pack['meta']['generated']}",
        f"- Content hash: `{pack['meta']['contentHash']}`",
        f"- Source commit: {pack['meta']['sourceCommit'] or '(not a git checkout)'}",
        f"- Schema version: {pack['meta']['version']} — fields: `meta`, `topics`, `pages`",
        f"- Pages: {pack['meta']['pageCount']} across {pack['meta']['topicCount']} topics",
        f"- Pages with Disputed blocks: {disputed} · with Outdated blocks: {outdated}",
        "",
        "The pack is the single interface between this repo and its consumers",
        "(256-wiki front end, REST API, agents). Regenerate, never hand-edit:",
        "`python3 scripts/build_export.py`",
        "",
        "| Topic | Pages |",
        "|---|---|",
    ]
    for t in pack["topics"]:
        lines.append(f"| {t['id']} | {counts[t['id']]} |")
    (out_dir / "MANIFEST.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the knowledge pack from wiki/.")
    ap.add_argument("--root", type=Path, default=ROOT, help="repo root (default: script's repo)")
    ap.add_argument("--out", type=Path, default=None, help="output dir (default: <root>/export)")
    ap.add_argument("--check", action="store_true",
                    help="verify the existing pack is fresh; exit 1 if stale")
    args = ap.parse_args()
    root = args.root.resolve()
    out_dir = (args.out or root / "export").resolve()

    pack = build_pack(root)
    rendered = json.dumps(pack, ensure_ascii=False, indent=2) + "\n"

    if args.check:
        existing = out_dir / "knowledge-pack.json"
        if existing.exists() and existing.read_text(encoding="utf-8") == rendered:
            print(f"pack is fresh: {pack['meta']['contentHash']}")
            return
        print("pack is stale or missing — run scripts/build_export.py")
        raise SystemExit(1)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "knowledge-pack.json").write_text(rendered, encoding="utf-8")
    write_manifest(pack, out_dir)
    for w in warnings:
        print(f"warn: {w}")
    for e in errors:
        print(f"error: {e}")
    if errors:
        raise SystemExit(1)
    print(f"built {out_dir / 'knowledge-pack.json'} — {pack['meta']['pageCount']} pages, "
          f"{pack['meta']['topicCount']} topics, hash {pack['meta']['contentHash'][:19]}…")


if __name__ == "__main__":
    main()
