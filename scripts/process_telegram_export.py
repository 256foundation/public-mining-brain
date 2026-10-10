#!/usr/bin/env python3
"""Process a Telegram HTML chat export into a filtered mining-signal digest.

Part of the brain's capture layer (see automation/AGENT-PLAYBOOK.md). Community
chats are `extract` posture: service messages, bot chatter, greetings, and
banter are dropped; substantive mining knowledge is kept with attribution to
public handles; phone numbers and emails are redacted.

Usage:
    python3 scripts/process_telegram_export.py <export_dir> <out_file> \
        --title "Group Name" --source-url t.me/group --registry-id some-id \
        [--author-drop "Name1,Name2"] [--min-length 40]

Reads <export_dir>/messages.html, messages2.html, ... (Telegram desktop export,
HTML format; large chats are split across numbered files).
Writes a markdown digest grouped by month, one blockquote-cited message per
entry, suitable as a raw/ source file for the brain.
"""

from __future__ import annotations

import argparse
import html as htmllib
import re
import sys
from collections import Counter
from pathlib import Path

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}

MSG_SPLIT_RE = re.compile(r'<div class="message default clearfix( joined)?" id="message(\d+)">')
DATE_RE = re.compile(r'title="(\d{1,2}) (\w+) (\d{4}), (\d{2}:\d{2}:\d{2})"')
FROM_RE = re.compile(r'<div class="from_name">\s*(.*?)\s*</div>', re.S)
TEXT_RE = re.compile(r'<div class="text">(.*)</div>\s*</div>\s*</div>\s*$', re.S)
PHOTO_RE = re.compile(r'photos/(photo_[^"@\' ]+)')

# Messages that survive the signal filter must be >= min-length, or hit one of these
LINK_RE = re.compile(r'href="(https?://[^"]+)"')
KEYWORD_RE = re.compile(
    r"\b(TH/s|PH/s|EH/s|GH/s|J/TH|J/GH|hashboard|control board|ASIC|firmware|Mujina|Ember|Libre Board|HydraPool|"
    r"Bitaxe|ESP-Miner|AxeOS|Nerd[A-Z]\w+|stratum|Stratum|difficulty|halving|block found|solo ?min|pool|"
    r"voltage|chip|heatsink|fan|PSU|power supply|immersion|hydro|oil cooled|watt|amp|"
    r"BM1\d{3}|S17|S19|S21|T21|M5\d|M6\d|L7|L9|Avalon|Whatsminer|Seal ?Miner|Terahash|tera ?hash|"
    r"profitab|ROI|payback|electricity rate|kWh|curtail|hashprice|heat ?reus|heatpunk|"
    r"flashed|OTA|overclock|underclock|autotun|dev call|grant|telehash|hashrate)\b",
    re.IGNORECASE)

# --strict: heat-reuse vocabulary, unit-bearing numbers, and resource domains worth keeping bare
HEAT_KEYWORD_RE = re.compile(
    r"\b(heater|heating|HVAC|furnace|boiler|radiator|hot water|water heater|dry ?cooler|heat exchanger|HX|"
    r"plate exchanger|glycol|coolant|dielectric|mineral oil|duct|baffle|shroud|plenum|CFM|static pressure|"
    r"thermostat|Home Assistant|setpoint|BTU|COP|heat pump|radiant|floor heat|pool heat|hot tub|greenhouse|"
    r"sauna|grain dry|noise|dB|decibel|quiet|240 ?v|220 ?v|120 ?v|110 ?v|breaker|circuit|amps?|"
    r"Loki|Avalon|Nano ?3|Braiins|BOS|Vnish|LuxOS|Ocean|DATUM|tune|tuning|undervolt|power target|"
    r"waterblock|water ?block|cold ?plate|pump|reservoir|tank|gallon|liter|"
    r"heat\w*|hot|cold|warm|temps?|temperature|cool\w*|oil|canola|water|dehydrat\w*|dry\w*|insulat\w*|"
    r"j/t|API|(?:S9|S17|S19|S21|M3\d|M5\d|M6\d)\w*|whatsminers?|antminers?|"
    r"efficien\w*|sats?/TH|sat/th/day|FPPS|PPLNS|fee|mount\w*|inspector|code|permit|insurance)\b",
    re.IGNORECASE)
UNIT_NUM_RE = re.compile(r"\d[\d,.]*\s?(?:TH|PH|EH|GH|J/TH|W|kW|kWh|V|A|°[CF]|C\b|F\b|CFM|BTU|gal|L\b|dB|%|¢|c/kWh|cents)",
                         re.IGNORECASE)
RESOURCE_DOMAINS = ("github.com", "heatpunks.org", "gitlab.com", "youtube.com", "youtu.be")
NOISE_DOMAINS = ("meet.jit.si", "cornychat.com", "zoom.us", "t.me/+")

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
# boundaries keep long digit runs inside URLs/ids (tweet ids, block hashes) intact
PHONE_RE = re.compile(r"(?<![\w/=._-])(\+\d{1,3}[- ]?)?(\(?\d{3}\)?[- .]?\d{3}[- .]?\d{4})(?![\w/])")


def clean_text(raw: str) -> str:
    t = raw
    t = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f"{m.group(2)} ({m.group(1)})" if m.group(2).strip()
               and m.group(2).strip() not in m.group(1) else m.group(1), t, flags=re.S)
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = re.sub(r"</?(strong|b|em|i|code|pre|span)[^>]*>", "", t)
    t = re.sub(r"<[^>]+>", "", t)  # any remaining tags
    t = htmllib.unescape(t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def redact(t: str) -> str:
    t = EMAIL_RE.sub("[email]", t)
    t = PHONE_RE.sub(lambda m: "[phone]" if len(re.sub(r"\D", "", m.group(0))) >= 10 else m.group(0), t)
    return t


def parse(html: str, author: str = "(unknown)") -> tuple[list[dict], str]:
    msgs: list[dict] = []
    matches = list(MSG_SPLIT_RE.finditer(html))
    for i, m in enumerate(matches):
        joined = bool(m.group(1))
        mid = int(m.group(2))
        chunk = html[m.end(): matches[i + 1].start()] if i + 1 < len(matches) else html[m.end():]
        chunk = chunk[:20000]  # safety bound
        dm = DATE_RE.search(chunk)
        if not dm:
            continue
        day, mon, year, time = int(dm.group(1)), dm.group(2), int(dm.group(3)), dm.group(4)
        month = MONTHS.get(mon)
        if not month:
            continue
        fm = FROM_RE.search(chunk)
        if fm:
            author = re.sub(r"<[^>]+>", "", fm.group(1)).strip()
        if not joined:
            author = author  # new block: author refreshed above if present
        text = ""
        tm = TEXT_RE.search(chunk)
        if tm:
            text = redact(clean_text(tm.group(1)))
        photos = PHOTO_RE.findall(chunk)
        msgs.append({
            "id": mid, "date": f"{year:04d}-{month:02d}-{day:02d}", "time": time,
            "author": author, "text": text,
            "photos": photos[:1], "links": LINK_RE.findall(chunk),
        })
    return msgs, author


def export_files(export_dir: Path) -> list[Path]:
    def num(p: Path) -> int:
        d = re.sub(r"\D", "", p.stem)
        return int(d) if d else 1
    return sorted(export_dir.glob("messages*.html"), key=num)


def keep(m: dict, min_length: int, dropped_authors: set[str]) -> bool:
    if m["author"] in dropped_authors:
        return False
    if not m["text"] and not m["photos"]:
        return False
    t = m["text"]
    if len(t) >= min_length:
        return True
    if m["links"] or m["photos"]:
        return True
    if KEYWORD_RE.search(t):
        return True
    return False


def keep_strict(m: dict, dropped_authors: set[str]) -> bool:
    """Signal-only filter: substance over chatter. Bare links survive only for
    resource domains; photo-only, meeting links, and short banter are dropped."""
    if m["author"] in dropped_authors or not m["text"]:
        return False
    t = m["text"]
    prose = re.sub(r"\(?https?://\S+\)?", "", t).strip()
    links = m["links"]
    if links and all(any(d in u for d in NOISE_DOMAINS) for u in links) and len(prose) < 120:
        return False
    if len(prose) < 25:
        return bool(links) and any(any(d in u for d in RESOURCE_DOMAINS) for u in links)
    technical = KEYWORD_RE.search(t) or HEAT_KEYWORD_RE.search(t) or UNIT_NUM_RE.search(t)
    if technical and len(prose) >= 40:
        return True
    return len(prose) >= 160


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("export_dir")
    ap.add_argument("out_file")
    ap.add_argument("--author-drop", default="Group Help", help="comma-separated author names to drop (bots)")
    ap.add_argument("--min-length", type=int, default=60)
    ap.add_argument("--title", default="256 Foundation Telegram")
    ap.add_argument("--source-url", default="t.me/the256foundation")
    ap.add_argument("--registry-id", default="256f-telegram")
    ap.add_argument("--collected", default="2026-10-08")
    ap.add_argument("--strict", action="store_true",
                    help="signal-only filter (drops banter, bare non-resource links, photo-only, meeting links)")
    args = ap.parse_args()

    msgs: list[dict] = []
    author = "(unknown)"
    for f in export_files(Path(args.export_dir)):
        part, author = parse(f.read_text(encoding="utf-8"), author)
        msgs.extend(part)
    dropped = {a.strip() for a in args.author_drop.split(",") if a.strip()}
    if args.strict:
        kept = [m for m in msgs if keep_strict(m, dropped)]
    else:
        kept = [m for m in msgs if keep(m, args.min_length, dropped)]

    out = Path(args.out_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append(f"# {args.title} — Mining Signal Digest")
    lines.append("")
    lines.append(f"> Source: Telegram export ({args.source_url}), HTML format")
    lines.append(f"> Registry ID: {args.registry_id}")
    lines.append(f"> Collected: {args.collected}")
    lines.append(f"> Published: {msgs[0]['date']} → {msgs[-1]['date']} (chat range)")
    filt = "strict signal filter" if args.strict else "default filter"
    lines.append(f"> Posture: extract ({filt}) — service/bot/noise messages dropped; phones/emails redacted; public handles retained; photos referenced by filename only (not committed)")
    lines.append(f"> Chat stats: {len(msgs)} messages total, {len(kept)} kept in digest, {len({m['author'] for m in msgs})} authors")
    lines.append("")
    lines.append("Signals of interest for compilation: field reports, hardware/firmware decisions,")
    lines.append("profitability and electricity data, pool behavior, events, technical Q&A with answers,")
    lines.append("and links to external resources.")
    lines.append("")

    cur_month = None
    for m in kept:
        ym = m["date"][:7]
        if ym != cur_month:
            cur_month = ym
            lines.append(f"## {ym}")
            lines.append("")
        photo_note = f" — photo: `{m['photos'][0]}`" if m["photos"] else ""
        lines.append(f"**[#{m['id']} · {m['date']} {m['time'][:5]} · {m['author']}]{photo_note}**")
        lines.append("")
        if m["text"]:
            lines.append(m["text"])
            lines.append("")
        elif m["photos"]:
            lines.append("_(photo only)_")
            lines.append("")

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # stats
    print(f"parsed {len(msgs)} messages; kept {len(kept)} in digest -> {out}")
    print(f"digest size: {out.stat().st_size/1024:.0f} KB")
    authors = Counter(m["author"] for m in kept)
    print("top signal authors:", ", ".join(f"{a}({n})" for a, n in authors.most_common(8)))
    domains = Counter()
    for m in kept:
        for u in m["links"]:
            d = re.sub(r"^https?://(www\.)?", "", u).split("/")[0]
            domains[d] += 1
    print("top shared domains:", ", ".join(f"{d}({n})" for d, n in domains.most_common(12)))
    years = Counter(m["date"][:4] for m in kept)
    print("per year:", dict(sorted(years.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
