"""mkdocs hook: regenerate docs/atom.xml from docs/blogs.md before every build."""
from __future__ import annotations

import logging
import os
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.dom import minidom
from xml.etree import ElementTree as ET

log = logging.getLogger("mkdocs.hooks.atom")

ATOM_NS = "http://www.w3.org/2005/Atom"
ENTRY_RE = re.compile(
    r"^-\s*\[(?P<title>.+?)\]\((?P<path>blog/[^)]+)\)\s*-\s*(?P<date>\w+ \d{1,2}, \d{4})\s*$"
)
MAX_ENTRIES = 20


def on_pre_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    repo_root = Path(config["config_file_path"]).resolve().parent
    site_url = os.environ.get("SITE_URL_OVERRIDE") or config.get("site_url") or "https://docs.peeringdb.com/"
    if not site_url.endswith("/"):
        site_url += "/"

    entries = []
    for lineno, line in enumerate(
        (docs_dir / "blogs.md").read_text(encoding="utf-8").splitlines(), start=1
    ):
        stripped = line.strip()
        if not stripped.startswith("- ["):
            continue
        m = ENTRY_RE.match(stripped)
        if not m:
            log.warning(f"blogs.md:{lineno}: entry doesn't match expected format, skipping: {stripped!r}")
            continue
        entries.append({
            "title": m.group("title"),
            "path": m.group("path"),
            "blogs_md_date": datetime.strptime(m.group("date"), "%B %d, %Y").replace(tzinfo=timezone.utc),
        })

    bulk_dates = _bulk_first_added_dates(repo_root, "docs/blog/")
    for e in entries:
        git_rel = "docs/" + e["path"]
        published = bulk_dates.get(git_rel)
        if published is None:
            published = _first_commit_date_follow(repo_root, git_rel)
        if published is None:
            log.warning(f"No git history found for {git_rel}, falling back to blogs.md date")
            published = e["blogs_md_date"]
        e["published"] = published

    _dedupe_published(entries)

    entries.sort(key=lambda e: e["published"], reverse=True)
    entries = entries[:MAX_ENTRIES]

    feed = ET.Element("feed", xmlns=ATOM_NS)
    ET.SubElement(feed, "title").text = "PeeringDB Blog"
    ET.SubElement(feed, "id").text = site_url
    ET.SubElement(feed, "updated").text = _isoformat(
        entries[0]["published"] if entries else datetime.now(timezone.utc)
    )
    ET.SubElement(feed, "link", href=site_url + "atom.xml", rel="self")
    ET.SubElement(feed, "link", href=site_url)
    author = ET.SubElement(feed, "author")
    ET.SubElement(author, "name").text = "PeeringDB"

    for e in entries:
        entry_url = site_url + e["path"].removesuffix(".md") + "/"
        entry = ET.SubElement(feed, "entry")
        ET.SubElement(entry, "title").text = e["title"]
        ET.SubElement(entry, "id").text = entry_url
        ET.SubElement(entry, "link", href=entry_url)
        ET.SubElement(entry, "published").text = _isoformat(e["published"])
        ET.SubElement(entry, "updated").text = _isoformat(e["published"])
        summary = _excerpt(docs_dir / e["path"])
        if summary:
            ET.SubElement(entry, "summary").text = summary

    pretty = minidom.parseString(ET.tostring(feed, encoding="utf-8")).toprettyxml(
        indent="  ", encoding="utf-8"
    )
    (docs_dir / "atom.xml").write_bytes(pretty)
    log.info(f"Generated docs/atom.xml with {len(entries)} entries")


def _bulk_first_added_dates(repo_root: Path, git_path: str) -> dict[str, datetime]:
    """One git-log pass over git_path's history; returns {path: earliest 'Added' commit date}.

    Files introduced via a rename (git classifies that transition as R, not A) won't
    appear here -- callers fall back to a per-file --follow lookup for those.
    """
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--name-only", "--format=COMMIT|%aI", "--", git_path],
            cwd=repo_root, capture_output=True, text=True, check=True, timeout=30,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as exc:
        log.warning(f"git log failed for {git_path}: {exc}")
        return {}

    first_added: dict[str, str] = {}
    current_date = None
    for line in out.splitlines():
        if line.startswith("COMMIT|"):
            current_date = line.split("|", 1)[1]
        elif line.strip():
            # Newest-first traversal: later (older-commit) lines overwrite, so the
            # value left after the full pass is each path's *earliest* Added date.
            first_added[line.strip()] = current_date
    return {k: datetime.fromisoformat(v) for k, v in first_added.items()}


def _first_commit_date_follow(repo_root: Path, git_rel_path: str) -> datetime | None:
    """Slow but rename-aware: only used as a fallback for files the bulk pass missed."""
    try:
        out = subprocess.run(
            ["git", "log", "--follow", "--format=%aI", "--", git_rel_path],
            cwd=repo_root, capture_output=True, text=True, check=True, timeout=10,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return None
    lines = [l for l in out.splitlines() if l.strip()]
    if not lines:
        return None
    return datetime.fromisoformat(lines[-1])


def _dedupe_published(entries: list[dict]) -> None:
    """Nudge apart entries sharing an identical published timestamp (e.g. two posts
    added in the same commit) by 1s increments, so atom:updated stays unique per the
    W3C Feed Validator's interoperability recommendation. Ties are broken by path for
    a deterministic, stable ordering across builds."""
    by_timestamp: dict[datetime, list[dict]] = {}
    for e in entries:
        by_timestamp.setdefault(e["published"], []).append(e)
    for group in by_timestamp.values():
        if len(group) < 2:
            continue
        group.sort(key=lambda e: e["path"])
        for offset, e in enumerate(group):
            e["published"] += timedelta(seconds=offset)


def _isoformat(dt: datetime) -> str:
    # git-derived dates carry their real commit timezone (e.g. -07:00); normalize to
    # UTC before formatting so the "Z" suffix always reflects the correct instant.
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


_SKIP_LINE_RE = re.compile(r"^(#{1,6}\s|[-*+]\s|\d+\.\s|>|!\[|<!--|```)")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_MD_EMPHASIS_RE = re.compile(r"(\*\*|__|\*|_|`)")


def _plain_text(line: str) -> str:
    """Strip inline markdown (links, bold/italic/code markers) for feed-reader display."""
    text = _MD_LINK_RE.sub(r"\1", line)
    text = _MD_EMPHASIS_RE.sub("", text)
    return text


def _excerpt(post_path: Path, max_len: int = 280) -> str:
    if not post_path.exists():
        return ""
    lines = post_path.read_text(encoding="utf-8").splitlines()
    # line 0 is the H1 title, line 1 is the italic *Month Day, Year* date line.
    # Skip blank lines and markdown block syntax (headings, lists, images, etc.)
    # to find the first genuine prose line for the summary.
    for line in lines[2:]:
        stripped = line.strip()
        if not stripped or _SKIP_LINE_RE.match(stripped):
            continue
        text = _plain_text(stripped)
        if len(text) > max_len:
            text = text[:max_len].rsplit(" ", 1)[0] + "…"
        return text
    return ""
