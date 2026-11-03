# Quick reference

Run from the repository root:

| Task | Command |
| --- | --- |
| Install locked dependencies | `./setup.sh` |
| Build production output | `./build_pelican.sh` |
| Check generated pages | `.venv/bin/python scripts/check_site.py` |
| Preview production output | `.venv/bin/python -m http.server 8000 --bind 127.0.0.1 --directory output` |
| Rebuild and preview while editing | `.venv/bin/pelican -lr -s bistaumanga.github.com/pelicanconf.py -b 127.0.0.1` |
| Publish reviewed changes | `./deploy.sh` |

Open <http://127.0.0.1:8000> after starting a preview. Stop it with Ctrl-C.

Edit Markdown under `bistaumanga.github.com/content/`, templates under `bistaumanga.github.com/themes/personal/templates/`, and CSS under `bistaumanga.github.com/themes/personal/static/css/`. Do not edit generated `output/` files.

For setup problems, rerun `./setup.sh`. See [README.md](README.md) for the full workflow.
