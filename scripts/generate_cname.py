"""mkdocs hook: regenerate docs/CNAME before every build.

Derives the GitHub Pages custom domain from SITE_URL_OVERRIDE (if set --
used by non-production deploys, e.g. this fork's dev preview) or falls
back to mkdocs.yml's site_url (correct for a real production deploy with
no override set, so this is safe by default if this branch is ever
merged upstream -- no manual CNAME edit required).
"""
from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import urlparse


def on_pre_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    site_url = os.environ.get("SITE_URL_OVERRIDE") or config.get("site_url")
    if not site_url:
        return
    domain = urlparse(site_url).hostname
    if not domain:
        return
    (docs_dir / "CNAME").write_text(domain + "\n", encoding="utf-8")
