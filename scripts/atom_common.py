"""Shared Atom 1.0 feed-building helpers for this repo's mkdocs hooks."""
from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from xml.dom import minidom
from xml.etree import ElementTree as ET

ATOM_NS = "http://www.w3.org/2005/Atom"

_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_MD_EMPHASIS_RE = re.compile(r"(\*\*|__|\*|_|`)")


def plain_text(line: str) -> str:
    """Strip inline markdown (links, bold/italic/code markers) for feed-reader display."""
    text = _MD_LINK_RE.sub(r"\1", line)
    text = _MD_EMPHASIS_RE.sub("", text)
    return text


def truncate(text: str, max_len: int = 280) -> str:
    if len(text) > max_len:
        return text[:max_len].rsplit(" ", 1)[0] + "…"
    return text


def isoformat(dt: datetime) -> str:
    # Dates may carry a real, non-UTC timezone (e.g. git-derived commit times);
    # normalize to UTC before formatting so the "Z" suffix is always correct.
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def dedupe_published(entries: list[dict], key: str = "published", tiebreak_key: str = "path") -> None:
    """Nudge apart entries sharing an identical published timestamp (e.g. two posts
    added in the same commit) by 1s increments, so atom:updated stays unique per the
    W3C Feed Validator's interoperability recommendation. Ties are broken by
    tiebreak_key for a deterministic, stable ordering across builds."""
    by_timestamp: dict[datetime, list[dict]] = {}
    for e in entries:
        by_timestamp.setdefault(e[key], []).append(e)
    for group in by_timestamp.values():
        if len(group) < 2:
            continue
        group.sort(key=lambda e: e[tiebreak_key])
        for offset, e in enumerate(group):
            e[key] += timedelta(seconds=offset)


def build_feed(*, title: str, site_url: str, self_path: str, entries: list[dict]) -> bytes:
    """entries: dicts with title, entry_url, published (tz-aware datetime), optional summary."""
    feed = ET.Element("feed", xmlns=ATOM_NS)
    ET.SubElement(feed, "title").text = title
    ET.SubElement(feed, "id").text = site_url
    ET.SubElement(feed, "updated").text = isoformat(
        entries[0]["published"] if entries else datetime.now(timezone.utc)
    )
    ET.SubElement(feed, "link", href=site_url + self_path, rel="self")
    ET.SubElement(feed, "link", href=site_url)
    author = ET.SubElement(feed, "author")
    ET.SubElement(author, "name").text = "PeeringDB"

    for e in entries:
        entry = ET.SubElement(feed, "entry")
        ET.SubElement(entry, "title").text = e["title"]
        ET.SubElement(entry, "id").text = e["entry_url"]
        ET.SubElement(entry, "link", href=e["entry_url"])
        ET.SubElement(entry, "published").text = isoformat(e["published"])
        ET.SubElement(entry, "updated").text = isoformat(e["published"])
        if e.get("summary"):
            ET.SubElement(entry, "summary").text = e["summary"]

    return minidom.parseString(ET.tostring(feed, encoding="utf-8")).toprettyxml(
        indent="  ", encoding="utf-8"
    )
