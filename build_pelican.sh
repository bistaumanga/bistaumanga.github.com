#!/bin/bash
# Build script for Pelican site

set -e

echo "Building Pelican site..."
cd bistaumanga.github.com

# Activate virtual environment
source ../.venv/bin/activate

# Build the site for production
pelican content -s publishconf.py $@

echo "Build complete! Output is in ../output/"
echo "To preview locally, run: pelican --listen"
