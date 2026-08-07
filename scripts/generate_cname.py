"""mkdocs hook: regenerate docs/CNAME before every build.

Domain comes from site_url.resolve_site_url() -- see that module for the
PROD=TRUE / SITE_URL_OVERRIDE / local-serve precedence.
"""
from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_url import LOOPBACK_HOSTS, resolve_site_url


def on_pre_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    domain = urlparse(resolve_site_url(config.get("site_url"))).hostname
    if not domain or domain in LOOPBACK_HOSTS:
        # A CNAME file only means anything for a real GitHub Pages deploy --
        # skip it for a local build/serve session.
        return
    (docs_dir / "CNAME").write_text(domain + "\n", encoding="utf-8")
