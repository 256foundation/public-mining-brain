#!/usr/bin/env python3
"""Archive published POD256 transcripts using Python 3.9+ and curl."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime
from email.utils import parsedate_to_datetime
import hashlib
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo


FEED_URL = "https://serve.podhome.fm/rss/c0be02f5-0e88-59a3-84cb-b76041a83264"
NS = {
    "podcast": "https://podcastindex.org/namespace/1.0",
    "itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
}
FORMATS = {"text/html": "html", "application/x-subrip": "srt", "text/vtt": "vtt"}
TIMEZONE = ZoneInfo("America/Chicago")
ROOT = Path(__file__).resolve().parents[1]


def write_bytes(path, content):
    if path.exists():
        if path.read_bytes() != content:
            raise FileExistsError(
                f"Raw snapshots are immutable: {path}. Use a new --collected date "
                "or a different --output directory."
            )
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".part")
    temporary.write_bytes(content)
    temporary.replace(path)


def write_text(path, content):
    write_bytes(path, content.encode("utf-8"))


def download(url):
    # Podhome accepts curl requests; its CDN rejects Python's default user agent.
    result = subprocess.run(
        ["curl", "--fail", "--silent", "--show-error", "--location",
         "--proto", "=https", "--proto-redir", "=https", "--retry", "3",
         "--connect-timeout", "20", "--max-time", "120", url],
        capture_output=True, check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    return result.stdout


def markdown(text):
    text = escape(text, quote=False)
    return re.sub(r"([\\`*_\[\]|])", r"\\\1", text)


class TranscriptParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.active = None
        self.buffer = []
        self.speaker = "Unknown"
        self.timestamp = None
        self.segments = []

    def handle_starttag(self, tag, attrs):
        if tag in {"cite", "time", "p"}:
            self.active, self.buffer = tag, []
        elif tag == "br" and self.active:
            self.buffer.append(" ")

    def handle_data(self, data):
        if self.active:
            self.buffer.append(data)

    def handle_endtag(self, tag):
        if tag != self.active:
            return
        text = re.sub(r"\s+", " ", "".join(self.buffer)).strip()
        if tag == "cite":
            self.speaker = text.rstrip(":") or "Unknown"
        elif tag == "time":
            if not re.fullmatch(r"\d{2,}:\d{2}:\d{2}", text):
                raise ValueError("Invalid transcript timestamp: " + text)
            self.timestamp = text
        elif tag == "p" and text:
            if self.timestamp is None:
                raise ValueError("Transcript paragraph is missing a timestamp")
            self.segments.append((self.timestamp, self.speaker, text))
        self.active, self.buffer = None, []


def parse_transcript(content):
    parser = TranscriptParser()
    parser.feed(content.decode("utf-8-sig"))
    if not parser.segments:
        raise ValueError("HTML contains no timestamped transcript paragraphs")
    previous = -1
    for timestamp, speaker, text in parser.segments:
        current = seconds(timestamp)
        if current < previous:
            raise ValueError("Transcript timestamps are out of order")
        previous = current
    return parser.segments


def seconds(timestamp):
    hours, minutes, secs = map(int, timestamp.split(":"))
    return hours * 3600 + minutes * 60 + secs


def transcript_body(segments):
    paragraphs, group = [], []

    def flush():
        timestamp, speaker, _ = group[0]
        label = "" if speaker.casefold() == "unknown" else f" {markdown(speaker)}:"
        paragraphs.append(f"**[{timestamp}]{label}** " + markdown(" ".join(s[2] for s in group)))

    for segment in segments:
        if group and (seconds(segment[0]) - seconds(group[0][0]) >= 30
                      or segment[1] != group[0][1]):
            flush()
            group = []
        group.append(segment)
    if group:
        flush()
    return "\n\n".join(paragraphs) + "\n"


def read_episodes(feed, start, end):
    root = ET.fromstring(feed)
    episodes = []
    for item in root.findall("./channel/item"):
        published = parsedate_to_datetime(item.findtext("pubDate"))
        local_date = published.astimezone(TIMEZONE).date()
        if not start <= local_date <= end:
            continue
        number = int(item.findtext("itunes:episode", namespaces=NS))
        enclosure = item.find("enclosure")
        sources = [
            {"url": t.get("url"), "type": t.get("type"), "language": t.get("language")}
            for t in item.findall("podcast:transcript", NS)
            if t.get("type") in FORMATS
        ]
        episodes.append({
            "episode": number,
            "title": item.findtext("title"),
            "guid": item.findtext("guid"),
            "published_at": published.isoformat(),
            "date": local_date.isoformat(),
            "duration": item.findtext("itunes:duration", namespaces=NS),
            "episode_url": item.findtext("link"),
            "audio_url": enclosure.get("url") if enclosure is not None else None,
            "transcript_sources": sources,
            "status": "published" if sources else "not_published",
            "markdown_path": None,
            "original_files": [],
        })
    episodes.sort(key=lambda episode: (episode["date"], episode["episode"]))
    if len({e["episode"] for e in episodes}) != len(episodes):
        raise ValueError("Duplicate episode numbers in selected feed entries")
    return episodes, len(root.findall("./channel/item"))


def archive_episode(episode, output, refresh, previous_files, collected):
    if episode["status"] == "not_published":
        return episode
    year = episode["date"][:4]
    segments = None
    for source in episode["transcript_sources"]:
        suffix = FORMATS[source["type"]]
        relative = Path("originals") / year / f"e{episode['episode']:03d}.{suffix}"
        path = output / relative
        cached = previous_files.get(relative.as_posix())
        content = path.read_bytes() if path.exists() and not refresh and cached else None
        if (content is None or cached["url"] != source["url"]
                or hashlib.sha256(content).hexdigest() != cached["sha256"]):
            content = download(source["url"])
        if suffix == "html":
            segments = parse_transcript(content)
        elif suffix == "vtt" and not content.decode("utf-8-sig").startswith("WEBVTT"):
            raise ValueError("Invalid VTT file")
        elif suffix == "srt" and b" --> " not in content:
            raise ValueError("Invalid SRT file")
        if not path.exists() or path.read_bytes() != content:
            write_bytes(path, content)
        episode["original_files"].append({
            **source, "path": relative.as_posix(),
            "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest(),
        })
    if segments is None:
        raise ValueError("A published episode has no usable HTML transcript")
    relative = Path("transcripts") / year / f"{episode['date']}-e{episode['episode']:03d}.md"
    episode["markdown_path"] = relative.as_posix()
    episode["segment_count"] = len(segments)
    episode["speakers"] = sorted({segment[1] for segment in segments})
    originals = " · ".join(
        f"[{FORMATS[f['type']].upper()}](../../{f['path']})"
        for f in episode["original_files"]
    )
    document = (
        f"# {markdown(episode['title'])}\n\n"
        f"> Source: {next(f['url'] for f in episode['original_files'] if f['type'] == 'text/html')}\n"
        f"> Collected: {collected}\n"
        f"> Published: {episode['date']}\n\n"
        f"- Episode: {episode['episode']}\n"
        f"- Published: {episode['date']} (America/Chicago)\n"
        f"- Publication timestamp: {episode['published_at']}\n"
        f"- Duration: {episode['duration']}\n"
        f"- Source: [Episode page]({episode['episode_url']})\n"
        f"- Audio: [Original episode]({episode['audio_url']})\n"
        f"- Original transcripts: {originals}\n\n"
        "This is the publisher's machine transcript. Paragraphs combine consecutive "
        "source cues into approximately 30-second passages without correcting the wording. "
        "Names and technical terms may be misspelled. Unknown speaker labels are omitted; "
        "the original files retain the source cues and labels.\n\n"
        "## Transcript\n\n" + transcript_body(segments)
    )
    write_text(output / relative, document)
    return episode


def write_index(output, manifest):
    episodes = manifest["episodes"]
    available = sum(e["status"] == "published" for e in episodes)
    lines = [
        "# POD256 transcript archive", "",
        f"> Source: {FEED_URL}",
        f"> Collected: {manifest['collected_date']}",
        "> Published: Unknown", "",
        f"Publication window: **{manifest['start_date']} through {manifest['end_date']}**, "
        "inclusive, using America/Chicago publication dates.", "",
        f"The [publisher's RSS feed]({FEED_URL}) contains **{len(episodes)} episodes** "
        f"in this window. **{available} have archived transcripts**; "
        f"**{len(episodes) - available} have no published transcript in the feed**.", "",
        "Each available episode has a readable Markdown transcript and the publisher's "
        "original HTML, SRT, and VTT files. The Markdown retains all source text and "
        "groups cues into passages of approximately 30 seconds. Transcripts are machine "
        "generated, with unverified names and speaker labels.", "",
        "[manifest.json](manifest.json) records metadata, source URLs, local paths, file "
        "sizes, and SHA-256 checksums. [feed.xml](feed.xml) is the RSS snapshot used for "
        "this inventory. Episode numbers and publication dates come from that feed; "
        "the archive makes no claim about episodes absent from it.", "",
        "## Episodes", "",
    ]
    for year in sorted({e["date"][:4] for e in episodes}, reverse=True):
        lines += [f"### {year}", "", "| Date | Episode | Title | Transcript |", "| --- | --- | --- | --- |"]
        for episode in reversed([e for e in episodes if e["date"].startswith(year)]):
            title = f"[{markdown(episode['title'])}]({episode['episode_url']})"
            status = (f"[Read]({episode['markdown_path']})" if episode["markdown_path"]
                      else "Not published")
            lines.append(f"| {episode['date']} | {episode['episode']:03d} | {title} | {status} |")
        lines.append("")
    lines += ["## Missing transcripts", "",
              "These episodes are in the selected feed window, but have no transcript "
              "links. Their audio and episode URLs remain in the manifest. No transcript "
              "has been invented or generated for them.", ""]
    for episode in episodes:
        if episode["status"] == "not_published":
            lines.append(f"- {episode['date']} — E{episode['episode']:03d}: "
                         f"[{markdown(episode['title'])}]({episode['episode_url']})")
    lines += ["", "## Reproducing this snapshot", "", "From the repository root:", "", "```sh",
              "python3 scripts/download_pod256.py --start " + manifest["start_date"]
              + " --end " + manifest["end_date"]
              + " --collected " + manifest["collected_date"]
              + " --feed-file raw/pod256/transcripts/" + manifest["collected_date"] + "/feed.xml",
              "```", "",
              "Python 3.9+ and curl are the only requirements. Existing identical files "
              "are reused. Raw snapshots are immutable: changed content is rejected "
              "instead of overwriting source material.", "",
              "## Collecting a new snapshot", "",
              "Omit the dates to select the two years ending today in America/Chicago. "
              "New collections go into `raw/pod256/transcripts/<collected-date>/`. "
              "Use a different `--output` directory for another collection on the same "
              "day. `--refresh` requests the original files again; corrected transcripts "
              "must be saved in a new snapshot. When using a custom output directory, "
              "pass it with `--output` and point `--feed-file` at that directory's "
              "`feed.xml` to reproduce it.", ""]
    write_text(output / "README.md", "\n".join(lines))


def main():
    today = datetime.now(TIMEZONE).date()
    try:
        two_years_ago = today.replace(year=today.year - 2)
    except ValueError:
        two_years_ago = today.replace(year=today.year - 2, day=28)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=date.fromisoformat, default=two_years_ago)
    parser.add_argument("--end", type=date.fromisoformat, default=today)
    parser.add_argument("--collected", type=date.fromisoformat, default=today,
                        help="Collection date and default snapshot directory name")
    parser.add_argument("--output", type=Path, help="New snapshot directory")
    parser.add_argument("--feed-file", type=Path, help="Use a saved RSS snapshot")
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    if args.start > args.end:
        parser.error("--start must be on or before --end")
    output = (args.output or ROOT / "raw" / "pod256" / "transcripts" / args.collected.isoformat()).resolve()
    feed = args.feed_file.read_bytes() if args.feed_file else download(FEED_URL)
    episodes, total = read_episodes(feed, args.start, args.end)
    if not episodes:
        raise ValueError("No feed episodes fall inside the requested date window")
    previous_files = {}
    if (output / "manifest.json").exists():
        previous = json.loads((output / "manifest.json").read_text())
        expected = {
            "start_date": args.start.isoformat(), "end_date": args.end.isoformat(),
            "collected_date": args.collected.isoformat(),
            "feed_sha256": hashlib.sha256(feed).hexdigest(),
        }
        if any(previous.get(key) != value for key, value in expected.items()):
            raise FileExistsError(
                "This raw snapshot already exists with a different feed, date window, "
                "or collection date. Use a new --collected date or --output directory."
            )
        previous_files = {f["path"]: f for e in previous["episodes"] for f in e["original_files"]}
    errors = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(archive_episode, e, output, args.refresh, previous_files,
                               args.collected.isoformat()): e
                   for e in episodes}
        for future in as_completed(futures):
            episode = futures[future]
            try:
                future.result()
                print(f"E{episode['episode']:03d}: {episode['status']}", flush=True)
            except Exception as error:
                errors.append(f"E{episode['episode']:03d}: {error}")
    if errors:
        raise RuntimeError("Archive incomplete; rerun to resume downloads:\n" + "\n".join(errors))
    manifest = {
        "schema_version": 1, "show": "POD256", "feed_url": FEED_URL,
        "start_date": args.start.isoformat(), "end_date": args.end.isoformat(),
        "collected_date": args.collected.isoformat(),
        "publication_timezone": str(TIMEZONE), "feed_episode_count": total,
        "feed_sha256": hashlib.sha256(feed).hexdigest(),
        "episode_count": len(episodes),
        "transcript_count": sum(e["status"] == "published" for e in episodes),
        "missing_transcript_count": sum(e["status"] == "not_published" for e in episodes),
        "episodes": episodes,
    }
    write_bytes(output / "feed.xml", feed)
    write_text(output / "manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    write_index(output, manifest)
    print(f"Archived {manifest['transcript_count']} transcripts across {len(episodes)} episodes in {output}")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
