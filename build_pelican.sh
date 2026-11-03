#!/bin/bash
set -euo pipefail
REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR/bistaumanga.github.com"
"$REPO_DIR/.venv/bin/pelican" content -s publishconf.py "$@"
echo "Build complete: $REPO_DIR/output/"
