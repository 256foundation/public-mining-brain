#!/usr/bin/env python3
"""Ingest ledger: per-source rollup of raw/ captures vs wiki citations.

Answers: which upstream sources have we captured from, how much of each
reached the wiki, and where the gaps are. Output is a LOCAL tracking doc
(.agent/ingest-ledger.md, gitignored) — never wiki content.

Mechanical sections are regenerated on every run. The hand-maintained
"## Audit verdicts" section between AUDIT markers is preserved.

Usage: python3 scripts/ingest_ledger.py [--write]
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW = REPO_ROOT / "raw"
WIKI = REPO_ROOT / "wiki"
LEDGER = REPO_ROOT / ".agent" / "ingest-ledger.md"

AUDIT_BEGIN = "<!-- audit-begin (hand-maintained; preserved by regen) -->"
AUDIT_END = "<!-- audit-end -->"

# github-<repo-token>[-site] -> (canonical slug, registry ID)
GITHUB_REPOS = {
    "esp-miner": ("bitaxeorg/ESP-Miner", "esp-miner"),
    "ultrahex": ("bitaxeorg/UltraHex", "bitaxe-hw"),
    "bitaxegamma": ("bitaxeorg/BitaxeGamma", "bitaxe-hw"),
    "bitaxegammahex": ("bitaxeorg/BitaxeGammaHex", "bitaxe-hw"),
    "bitaxemax": ("bitaxeorg/BitaxeMax", "bitaxe-hw"),
    "bitaxesupra": ("bitaxeorg/BitaxeSupra", "bitaxe-hw"),
    "bitaxeultra": ("bitaxeorg/BitaxeUltra", "bitaxe-hw"),
    "bitaxegt": ("bitaxeorg/BitaxeGT", "bitaxe-hw"),
    "bitaxebonanza": ("bitaxeorg/BitaxeBonanza", "bitaxe-hw"),
    "bitaxe-web-flasher": ("bitaxeorg/bitaxe-web-flasher", "esp-miner"),
    "bitaxe-raw": ("bitaxeorg/bitaxe-raw", "rhapd-bitaxe"),
    "foss-miner-list": ("bitaxeorg/foss-miner-list", "osmu-projects"),
    "mujina": ("256foundation/mujina", "mujina"),
    "mujina-website": ("mujina website repo", "mujina"),
    "asic-rs": ("256foundation/asic-rs", "asic-rs"),
    "hashscope": ("256foundation/hashscope", "hashscope"),
    "website": ("256foundation/website", "256f-site"),
    "block-watcher-website": ("256f block-watcher site", "btc-toolkit"),
    "hydrapool": ("256foundation/hydrapool", "hydrapool"),
}

DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-")
GITHUB_RE = re.compile(r"(?:^|-)github-([a-z0-9-]+?)(?:-(?:issue|pr)-\d+(?:-|$)|$)")
ISSUE_RE = re.compile(r"-(?:issue|pr)-(\d+)")

# non-github source keys -> registry IDs
REGISTRY_MAP = {
    "POD256 episode pages": "pod256",
    "POD256 full transcripts (e067-e127)": "pod256",
    "osmu.wiki": "osmu-wiki",
    "256F Discourse forum": "256f-forum",
    "256F newsletter (Assembling Freedom)": "256f-substack",
    "256F org site + website repo": "256f-site",
    "256F hardware docs (Ember/PCB/BZM2)": "emberone-00-pcb",
    "256F research docs": "256f-site",
    "256foundation/hydrapool": "hydrapool",
    "bitaxe.org": "esp-miner",
    "mujina.org": "mujina",
    "Telegram history digests": "256f-telegram",
    "Bitcoin BIP texts": "rhap-spec",
    "github/bitaxeorg/BitaxeBIRDS": "emberone-01-pcb",
}


def classify(path: Path) -> tuple[str, str]:
    """Return (source_key, kind). kind: capture | digest | draft."""
    rel = path.relative_to(REPO_ROOT).as_posix()
    name = path.name.removesuffix(".md")

    if rel.startswith("raw/inbox/hackathon-wiki/"):
        return "sprint drafts (leads, not sources)", "draft"
    if rel.startswith("raw/inbox/"):
        return "inbox (staged/untriaged)", "capture"

    if "pod256/transcripts" in rel:
        return "POD256 full transcripts (e067-e127)", "capture"
    if "/pod256/" in rel:
        return "POD256 episode pages", "capture"
    if "256f-newsletter" in rel:
        return "256F newsletter (Assembling Freedom)", "capture"
    if "256f-research" in rel:
        return "256F research docs", "capture"
    if "256f-org" in rel:
        if "forum" in name:
            return "256F Discourse forum", "capture"
        return "256F org site + website repo", "capture"
    if "256f-hardware" in rel:
        return "256F hardware docs (Ember/PCB/BZM2)", "capture"
    if "hydrapool" in rel:
        return "256foundation/hydrapool", "capture"
    if "telegram" in name:
        return "Telegram history digests", "digest"
    if "harvest" in rel and "/protocols/" in rel:
        return "Bitcoin BIP texts", "capture"

    if name.startswith("osmu-wiki-"):
        return "osmu.wiki", "capture"
    if name.startswith("bitaxe-org-"):
        return "bitaxe.org", "capture"
    if name.startswith("mujina-org-"):
        return "mujina.org", "capture"
    if "telegram-public-groups" in name:
        return "Telegram public groups scan", "capture"

    if name.startswith("forum-"):
        return "256F Discourse forum", "capture"
    if name.startswith("bitaxe-") and "pod256" not in name:
        return "Bitaxe project docs (readmes/licenses)", "capture"

    m = GITHUB_RE.search(name)
    if m:
        token = m.group(1)
        for known, (slug, reg) in GITHUB_REPOS.items():
            if token == known or token.startswith(known):
                return f"github/{slug}", "capture"
        return f"github/{token}", "capture"

    return f"other/{path.parent.relative_to(RAW).as_posix()}", "capture"


def cited_paths() -> set[str]:
    """All raw/ paths referenced by any wiki article (relative, no anchor)."""
    out = set()
    pat = re.compile(r"\]\((?:\.\./)+raw/([^)#\s]+)")
    for md in WIKI.rglob("*.md"):
        for m in pat.findall(md.read_text(encoding="utf-8")):
            out.add(("raw/" + m.strip()).rstrip("/"))
    return out


def main() -> None:
    all_raw = sorted(p for p in RAW.rglob("*.md"))
    cited = cited_paths()

    stats: dict[str, dict] = defaultdict(
        lambda: {"n": 0, "cited": 0, "dates": [], "max_issue": 0,
                 "unref_sample": [], "kinds": defaultdict(int)}
    )
    for p in all_raw:
        rel = p.relative_to(REPO_ROOT).as_posix()
        key, kind = classify(p)
        s = stats[key]
        s["n"] += 1
        s["kinds"][kind] += 1
        if rel in cited:
            s["cited"] += 1
        elif len(s["unref_sample"]) < 3:
            s["unref_sample"].append(rel.replace("raw/", "", 1))
        dm = DATE_RE.match(p.name)
        if dm:
            s["dates"].append(dm.group(1))
        im = ISSUE_RE.search(p.name)
        if im:
            s["max_issue"] = max(s["max_issue"], int(im.group(1)))

    lines = [
        "# Ingest Ledger (LOCAL — gitignored)",
        "",
        f"Generated {date.today().isoformat()} by `scripts/ingest_ledger.py`. "
        "Mechanical sections regenerate; verdicts below the audit marker are hand-maintained.",
        "",
        "Per upstream source: captures on disk, how many are cited by wiki articles,",
        "capture span, and (audit pass) upstream totals + quality verdict.",
        "",
        "## Sources",
        "",
        "| Source | Registry ID | Captures | Cited | Unreferenced | Span | Max item# |",
        "|---|---|---|---|---|---|---|",
    ]
    total = cited_total = 0
    for key in sorted(stats):
        s = stats[key]
        total += s["n"]
        cited_total += s["cited"]
        span = ""
        if s["dates"]:
            span = f"{min(s['dates'])} → {max(s['dates'])}"
        reg = REGISTRY_MAP.get(key, "")
        if not reg:
            for known, (slug, rid) in GITHUB_REPOS.items():
                if key == f"github/{slug}":
                    reg = rid
        lines.append(
            f"| {key} | {reg or '—'} | {s['n']} | {s['cited']} | {s['n'] - s['cited']} | {span} |"
        )
    lines += [
        "",
        f"**Totals:** {total} raw files, {cited_total} cited by ≥1 wiki article, "
        f"{total - cited_total} unreferenced.",
        "",
        "## Unreferenced samples (per source, up to 3)",
        "",
    ]
    for key in sorted(stats):
        s = stats[key]
        if s["unref_sample"]:
            lines.append(f"- **{key}** ({s['n'] - s['cited']} unref): "
                         + "; ".join(s["unref_sample"]))
    lines += [
        "",
        "## Upstream completeness (audit pass fills)",
        "",
        "| Source | Upstream total | Captured | Coverage | How checked |",
        "|---|---|---|---|---|",
    ]
    for key in sorted(stats):
        s = stats[key]
        mi = f" (issues/PRs seen up to #{s['max_issue']})" if s["max_issue"] else ""
        lines.append(f"| {key} | TODO | {s['n']}{mi} | TODO | TODO |")
    lines += ["", AUDIT_BEGIN, ""]

    # preserve hand-maintained verdicts on regeneration
    if LEDGER.exists():
        old = LEDGER.read_text(encoding="utf-8")
        if AUDIT_BEGIN in old and AUDIT_END in old:
            kept = old.split(AUDIT_BEGIN, 1)[1].split(AUDIT_END, 1)[0]
            lines += [kept.lstrip("\n"), AUDIT_END, ""]
        else:
            lines += ["## Audit verdicts (hand-maintained)", "", "<!-- per source: verdict / keep-drop / next action -->", "", AUDIT_END, ""]
    else:
        lines += ["## Audit verdicts (hand-maintained)", "",
                  "<!-- per source: verdict / keep-drop / next action -->", "", AUDIT_END, ""]

    out = "\n".join(lines)
    if "--stdout" in sys.argv:
        print(out)
    else:
        LEDGER.parent.mkdir(exist_ok=True)
        LEDGER.write_text(out, encoding="utf-8")
        print(f"wrote {LEDGER.relative_to(REPO_ROOT)} "
              f"({total} raw files, {len(stats)} sources, {cited_total} cited)")


if __name__ == "__main__":
    main()
