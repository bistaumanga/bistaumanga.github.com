#!/bin/bash
set -euo pipefail
REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"
if ! command -v uv >/dev/null 2>&1; then
    echo "Install uv from https://docs.astral.sh/uv/getting-started/installation/ and rerun ./setup.sh"
    exit 1
fi
uv sync --frozen
echo "Setup complete. Run ./build_pelican.sh or see README.md for preview instructions."
