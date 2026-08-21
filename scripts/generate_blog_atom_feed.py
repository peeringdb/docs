"""mkdocs hook: regenerate docs/blog/atom.xml from docs/blogs.md before every build."""
from __future__ import annotations

import logging
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from atom_common import build_feed, dedupe_published, plain_text, truncate
from site_url import resolve_site_url

log = logging.getLogger("mkdocs.hooks.blog_atom")

ENTRY_RE = re.compile(
    r"^-\s*\[(?P<title>.+?)\]\((?P<path>blog/[^)]+)\)\s*-\s*(?P<date>\w+ \d{1,2}, \d{4})\s*$"
)
MAX_ENTRIES = 20


def on_pre_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    repo_root = Path(config["config_file_path"]).resolve().parent
    site_url = resolve_site_url(config.get("site_url"))
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
        e["entry_url"] = site_url + e["path"].removesuffix(".md") + "/"
        e["summary"] = _excerpt(docs_dir / e["path"])

    dedupe_published(entries)

    entries.sort(key=lambda e: e["published"], reverse=True)
    entries = entries[:MAX_ENTRIES]

    feed_bytes = build_feed(
        title="PeeringDB Blog",
        site_url=site_url,
        self_path="blog/atom.xml",
        entries=entries,
    )
    (docs_dir / "blog" / "atom.xml").write_bytes(feed_bytes)
    log.info(f"Generated docs/blog/atom.xml with {len(entries)} entries")


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


_SKIP_LINE_RE = re.compile(r"^(#{1,6}\s|[-*+]\s|\d+\.\s|>|!\[|<!--|```)")


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
        return truncate(plain_text(stripped), max_len)
    return ""
