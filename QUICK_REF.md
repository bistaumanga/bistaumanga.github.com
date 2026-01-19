# Quick Reference - Pelican Commands

## Daily Usage

### Preview Locally
```bash
cd bistaumanga.github.com
source ../.venv/bin/activate
pelican --listen
```
Visit: http://localhost:8000

### Build Site
```bash
./build_pelican.sh
```

### Deploy to GitHub Pages
```bash
./deploy.sh
```

## Adding Content

### New Blog Post
```bash
cd bistaumanga.github.com/content
nano my-new-post.md
```

Template:
```markdown
Title: My Post Title
Date: 2024-01-20 10:00
Tags: python, data-science, machine-learning
Slug: my-post-slug

Your content in Markdown here...
```

### New Page
```bash
cd bistaumanga.github.com/content/pages
nano about.md
```

## File Locations

- **Blog posts**: `bistaumanga.github.com/content/*.md`
- **Pages**: `bistaumanga.github.com/content/pages/*.md`
- **Images**: `bistaumanga.github.com/content/images/`
- **Files (PDFs, etc)**: `bistaumanga.github.com/content/files/`
- **CSS**: `bistaumanga.github.com/content/extra/css/`
- **Config**: `bistaumanga.github.com/pelicanconf.py`
- **Output**: `output/` (generated, don't edit)

## Troubleshooting

### "Command not found: pelican"
```bash
source .venv/bin/activate
```

### CSS/Images missing after build
Check files are in:
- `content/extra/css/`
- `content/images/`
Then rebuild.

### Deploy fails
```bash
source .venv/bin/activate
pip install ghp-import
./deploy.sh
```

## Helpful Pelican Commands

```bash
# Build with different config
pelican content -s publishconf.py

# Clean output directory
pelican content -d

# Auto-reload on changes
pelican --listen --autoreload

# Verbose output for debugging
pelican content -v
```

## GitHub Branches

- **main**: Pelican source files (this is what you edit)
- **gh-pages**: Generated HTML (created by `deploy.sh`)

## More Help

See: [MIGRATION_SUMMARY.md](MIGRATION_SUMMARY.md)
