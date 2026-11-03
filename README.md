# Umanga Bista — personal website

A Pelican static site hosted on GitHub Pages at [bistaumanga.com.np](https://bistaumanga.com.np).
The source is in `bistaumanga.github.com/`; generated files go in the repository's ignored `output/` directory.

## Setup and preview

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run:

```bash
./setup.sh
./build_pelican.sh
.venv/bin/python scripts/check_site.py
.venv/bin/python -m http.server 8000 --bind 127.0.0.1 --directory output
```

Open <http://127.0.0.1:8000>. Stop the server with Ctrl-C. The build uses the locked Python dependencies, including Python 3.13.

For automatic regeneration while editing, run this from the repository root instead of the static server:

```bash
.venv/bin/pelican -lr -s bistaumanga.github.com/pelicanconf.py -b 127.0.0.1
```

The production build uses relative links for local preview and absolute production URLs for canonical metadata, the sitemap, and Atom entries.

## Editing

- Homepage: `bistaumanga.github.com/content/pages/index.md`
- Articles: `bistaumanga.github.com/content/*.md`
- Downloads and article images: `bistaumanga.github.com/content/files/`
- Templates: `bistaumanga.github.com/themes/personal/templates/`
- Styles: `bistaumanga.github.com/themes/personal/static/css/site.css`
- Site settings: `bistaumanga.github.com/pelicanconf.py`
- Production settings: `bistaumanga.github.com/publishconf.py`

The local theme uses system fonts, semantic HTML, responsive CSS, and automatic light/dark appearance. No frontend framework, external font service, or JavaScript is required.

New article example:

```markdown
Title: My article
Date: 2026-11-04 10:00
Slug: my-article
Tags: machine-learning
Summary: A short description for listings and search previews.

Article text here. The template supplies the main heading.
```

New articles use `/blog/my-article/`. The existing visual-search article retains `/001_visual_search.html` so published links keep working.

## Checks and publication

```bash
./build_pelican.sh
.venv/bin/python scripts/check_site.py
```

The checker validates generated local links and fragments, one main heading per page, essential metadata, stylesheet links, image alt text, sitemap targets, and required output files. It does not test external services or execute code examples in articles.

To publish the reviewed result explicitly:

```bash
./deploy.sh
```

This rebuilds, runs the checker, and pushes generated files to `gh-pages`. Configure GitHub Pages to serve that branch from its root. `CNAME` preserves the custom domain. The script does not force-push. `make github` and the optional Invoke `gh-pages` task delegate to the same script; neither targets the source branch.

See [REVIEW.md](REVIEW.md) for findings and verification notes.

Content is copyrighted by its author.
