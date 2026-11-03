#!/bin/bash
# Explicit publication command. Build and validate locally before running.
set -euo pipefail
REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
"$REPO_DIR/build_pelican.sh"
"$REPO_DIR/.venv/bin/python" "$REPO_DIR/scripts/check_site.py" "$REPO_DIR/output"
bash "$REPO_DIR/scripts/check_secrets.sh"
cd "$REPO_DIR"
"$REPO_DIR/.venv/bin/ghp-import" -n -p -b gh-pages output
echo "Published to gh-pages: https://www.bistaumanga.com.np"
