"""mkdocs hook: regenerate docs/release_notes/atom.xml from
docs/release_notes/index.md before every build."""
from __future__ import annotations

import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from markdown.extensions.toc import slugify

sys.path.insert(0, str(Path(__file__).resolve().parent))
from atom_common import build_feed, dedupe_published
from site_url import resolve_site_url

log = logging.getLogger("mkdocs.hooks.release_notes_atom")

MAX_ENTRIES = 20
RELEASE_HEADING_RE = re.compile(r"^## Release (?P<version>\d[\w.]*)\s*$")
DATE_RE = re.compile(r"^(?:Release|Beta Announcement) Date:\s*(?P<date>.+)$")
DATE_FORMATS = ("%d %b %Y", "%d %B %Y")


def _parse_date(text: str) -> datetime | None:
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text.strip(), fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def on_pre_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    site_url = resolve_site_url(config.get("site_url"))
    if not site_url.endswith("/"):
        site_url += "/"

    index_path = docs_dir / "release_notes" / "index.md"
    sections: list[dict] = []
    current = None
    for line in index_path.read_text(encoding="utf-8").splitlines():
        heading_m = RELEASE_HEADING_RE.match(line)
        if heading_m:
            current = {
                "version": heading_m.group("version"),
                "release_date": None,
                "beta_date": None,
                "issue_count": 0,
            }
            sections.append(current)
            continue
        if current is None:
            continue
        date_m = DATE_RE.match(line)
        if date_m:
            parsed = _parse_date(date_m.group("date"))
            key = "release_date" if line.startswith("Release Date:") else "beta_date"
            current[key] = parsed
            continue
        if line.strip().startswith("| ["):
            current["issue_count"] += 1

    entries = []
    for s in sections:
        published = s["release_date"] or s["beta_date"]
        if published is None:
            log.warning(f"release_notes/index.md: Release {s['version']} has no parseable date, skipping")
            continue
        title = f"Release {s['version']}"
        n = s["issue_count"]
        entries.append({
            "title": title,
            "entry_url": site_url + "release_notes/#" + slugify(title, "-"),
            "published": published,
            "summary": f"{n} GitHub issue{'s' if n != 1 else ''} addressed in this release." if n else "",
            "path": s["version"],  # dedupe_published's tiebreak key
        })

    dedupe_published(entries)
    entries.sort(key=lambda e: e["published"], reverse=True)
    entries = entries[:MAX_ENTRIES]

    feed_bytes = build_feed(
        title="PeeringDB Release Notes",
        site_url=site_url,
        self_path="release_notes/atom.xml",
        entries=entries,
    )
    (docs_dir / "release_notes" / "atom.xml").write_bytes(feed_bytes)
    log.info(f"Generated docs/release_notes/atom.xml with {len(entries)} entries")
