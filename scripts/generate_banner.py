"""mkdocs hook: expose fork-preview banner data to templates via config.extra.

On by default (we assume any build without further signal is a dev/fork build).
Set PROD=TRUE at build time to suppress it. Only a real production deploy
(which lives outside this repo, in peeringdb/docs) should ever set PROD=TRUE.

Uses on_pre_build rather than on_config: resolve_site_url()'s local-serve
detection depends on config.site_url already being overwritten with the dev
server address, which mkdocs's own serve.py only does *after* on_config has
run (see site_url.py's docstring) but *before* on_pre_build.
"""
from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_url import PROD_SITE_URL, origin_repo_url, resolve_site_url

log = logging.getLogger("mkdocs.hooks.banner")

PROD_REPO_URL = "https://github.com/peeringdb/docs"


def on_pre_build(config, **kwargs):
    if os.environ.get("PROD") == "TRUE":
        return

    repo_root = Path(config["config_file_path"]).resolve().parent
    fork_repo_url = origin_repo_url(repo_root)
    if fork_repo_url is None:
        log.warning("Could not resolve origin remote; skipping fork-preview banner")
        return

    live_url = resolve_site_url(config.get("site_url"))

    config["extra"]["fork_banner"] = {
        "fork_repo_url": fork_repo_url,
        "fork_repo_label": urlparse(fork_repo_url).path.strip("/"),
        "live_url": live_url,
        "live_label": urlparse(live_url).hostname or live_url,
        "prod_site_url": PROD_SITE_URL,
        "prod_site_label": urlparse(PROD_SITE_URL).hostname,
        "prod_repo_url": PROD_REPO_URL,
        "prod_repo_label": urlparse(PROD_REPO_URL).path.strip("/"),
    }
