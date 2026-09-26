"""Shared site-URL resolution policy for all mkdocs hooks in this repo.

Precedence:
1. PROD=TRUE -- real production, full stop.
2. SITE_URL_OVERRIDE, if set.
3. The local dev-server address mkdocs itself is serving on (e.g.
   http://127.0.0.1:8000/), if `mkdocs serve` is what's actually running.
   Requires callers to be wired to on_pre_build, not on_config: mkdocs's
   serve.py only overwrites config.site_url with the dev address *after*
   on_config has already run (see commands/serve.py's `config.site_url =
   f'http://{config.dev_addr}...'`, right before it calls build()), so
   on_config never sees it.
4. LOCAL_SITE_URL ("http://localhost:8000/", mkdocs's own default
   --dev-addr) -- the fallback when none of the above apply: a plain
   `mkdocs build` with no env vars and no live dev server, e.g.
   docs-build-check.yml's CI check or a one-off local build that gets
   served separately afterward (a static server started after the build
   already finished can't be predicted at build time -- there's nothing
   to detect there). Deliberately assumes "local" rather than guessing a
   real GitHub Pages URL from `git remote get-url origin`: a real checkout
   always has an `origin` remote, so a git-remote-based guess would almost
   always "succeed" with a URL that doesn't correspond to anything actually
   being served, which is more misleading than an honest localhost default.
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path
from urllib.parse import urlparse

PROD_SITE_URL = "https://docs.peeringdb.com/"
LOCAL_SITE_URL = "http://localhost:8000/"
LOOPBACK_HOSTS = {"localhost", "127.0.0.1", "::1"}


def resolve_site_url(config_site_url: str | None = None) -> str:
    if os.environ.get("PROD") == "TRUE":
        return PROD_SITE_URL
    override = os.environ.get("SITE_URL_OVERRIDE")
    if override:
        return override
    if config_site_url and urlparse(config_site_url).hostname in LOOPBACK_HOSTS:
        return config_site_url
    return LOCAL_SITE_URL


def origin_repo_url(repo_root: Path) -> str | None:
    try:
        out = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=repo_root, capture_output=True, text=True, check=True, timeout=10,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if out.startswith("git@github.com:"):
        out = "https://github.com/" + out.removeprefix("git@github.com:")
    return out.removesuffix(".git")
