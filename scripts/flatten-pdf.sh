#!/bin/bash
set -euo pipefail

[[ -z "${1:-}" ]] && { echo "Usage: flatten-pdf <file.pdf>" >&2; exit 1; }
[[ ! -f "$1" ]] && { echo "File not found: $1" >&2; exit 1; }

tmp=$(mktemp --suffix=.pdf)
trap "rm -f '$tmp'" EXIT

pdftocairo -pdf "$1" "$tmp"
mv "$tmp" "$1"
