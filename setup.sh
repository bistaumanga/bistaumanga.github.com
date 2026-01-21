#!/bin/bash
# First-time setup script for Pelican website

echo "========================================="
echo "Pelican Website Setup"
echo "========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source .venv/bin/activate

# Install requirements
echo ""
echo "Installing Python packages..."
pip install --upgrade pip uv
uv sync

echo ""
echo "========================================="
echo "✅ Setup Complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Preview the site locally:"
echo "   cd bistaumanga.github.com"
echo "   source ../.venv/bin/activate"
echo "   pelican --listen"
echo "   Then open http://localhost:8000"
echo ""
echo "2. Build for production:"
echo "   ./build_pelican.sh"
echo ""
echo "3. Deploy to GitHub Pages:"
echo "   ./deploy.sh"
echo ""
echo "For more information, see MIGRATION_SUMMARY.md"
echo ""
