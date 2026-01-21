#!/bin/bash
# Deploy script for GitHub Pages
# This publishes the content from output/ directory to GitHub Pages

set -e

echo "Building site with production config..."
cd bistaumanga.github.com
source ../.venv/bin/activate
pelican content -s publishconf.py
cd ..

echo "Publishing to GitHub Pages..."

# Install ghp-import if not already installed

# Push the output directory to gh-pages branch
# The -n adds a .nojekyll file to tell GitHub Pages not to process with Jekyll
# The -p pushes to GitHub
# The -f forces the push
ghp-import -n -p -f output

echo "Deployment complete! Your site should be live at https://bistaumanga.com.np"
echo "Note: It may take a few minutes for changes to appear."
