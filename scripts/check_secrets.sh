#!/bin/bash
# Requires Gitleaks v8.30.1 or later. Findings are always fully redacted.
set -euo pipefail
REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
SCANNER="${GITLEAKS_BIN:-gitleaks}"
if ! command -v "$SCANNER" >/dev/null 2>&1; then
    echo "Install Gitleaks from https://github.com/gitleaks/gitleaks before publishing."
    exit 1
fi
cd "$REPO_DIR"
"$SCANNER" git --no-banner --redact=100 --ignore-gitleaks-allow --log-opts=--all .
"$SCANNER" git --no-banner --redact=100 --ignore-gitleaks-allow --pre-commit .
"$SCANNER" git --no-banner --redact=100 --ignore-gitleaks-allow --pre-commit --staged .
"$SCANNER" dir --no-banner --redact=100 --ignore-gitleaks-allow output
