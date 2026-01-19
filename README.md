# Personal Website and Blog

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fbistaumanga.com.np)](https://bistaumanga.com.np)

My personal website and blog hosted on [GitHub Pages](https://pages.github.com) at [bistaumanga.com.np](https://bistaumanga.com.np).

Built with [Pelican](https://getpelican.com) (Python static site generator) and [Bootstrap](https://getbootstrap.com).

---

## 🚀 Quick Start

### First-Time Setup
```bash
./setup.sh
```

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

---

## 📁 Project Structure

```
bistaumanga.github.com/
├── bistaumanga.github.com/     # Pelican source
│   ├── content/                # Markdown content
│   │   ├── pages/             # Static pages
│   │   ├── *.md               # Blog posts
│   │   ├── images/            # Images
│   │   ├── files/             # Files (PDFs, etc.)
│   │   └── extra/             # CSS, CNAME, etc.
│   ├── pelicanconf.py         # Dev config
│   └── publishconf.py         # Production config
├── output/                     # Generated site
├── build_pelican.sh            # Build script
├── deploy.sh                   # Deploy script
├── setup.sh                    # Setup script
└── requirements.txt            # Python dependencies
```

---

## 📝 Adding Content

### New Blog Post

Create `bistaumanga.github.com/content/my-post.md`:

```markdown
Title: My Post Title
Date: 2024-01-20 10:00
Tags: python, data-science
Slug: my-post-slug

Your content here...
```

Then build and deploy:
```bash
./build_pelican.sh
./deploy.sh
```

---

## 📚 Documentation

- **[QUICK_REF.md](QUICK_REF.md)** - Quick command reference

---

## 🛠️ Technology Stack

- **[Pelican](https://getpelican.com)** - Static site generator (Python)
- **[Bootstrap](https://getbootstrap.com)** - CSS framework
- **[Font Awesome](https://fontawesome.com)** - Icons
- **[GitHub Pages](https://pages.github.com)** - Hosting
- **[MathJax](https://www.mathjax.org)** - Math rendering

---

## 📜 License

Content is copyrighted. Code is open source.

---