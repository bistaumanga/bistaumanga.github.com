# Website review and changes

## How the site works

Pelican reads Markdown from `bistaumanga.github.com/content/` and renders the local Jinja theme into `output/`. GitHub Pages serves the generated branch, with `CNAME` selecting the custom domain. The homepage is a page saved at `/`; writing lives at `/blog/`. The existing article keeps its published `/001_visual_search.html` URL.

## Findings addressed

| Finding | Change |
| --- | --- |
| Homepage read as a job history and omitted current research interests | Rewrote it from the supplied CV, with a short professional overview, education, selected research, patents, and service. |
| Publication title and conference name errors | Corrected the comparative summarisation title and identified WSDM as Web Search and Data Mining. |
| No visible path from the profile to the existing project | Added a generated projects/writing section and clearer writing navigation. |
| The active default theme did not load the configured dark-mode override | Added a self-contained theme with responsive layout, automatic light/dark CSS, code styling, focus indicators, skip link, and semantic headings. Removed the unused override. |
| Incomplete page metadata and crawl support | Added descriptions, canonical and Open Graph metadata, a sitemap, robots declaration, and a custom 404 page. |
| Development SITEURL omitted a URL scheme | Development now uses local relative URLs; canonical metadata always identifies the production domain. |
| Build scripts depended on the caller's current directory and forwarded arguments without quoting | Anchored scripts to their repository directory and quoted forwarded arguments. |
| Makefile generated output in a different directory | Unified generated output at the repository root. |
| Legacy Make/Invoke deployment paths targeted `main` | Routed publication through the checked deployment script targeting `gh-pages`; removed unconditional force pushing. |
| Setup continued after errors and referenced missing documentation | Setup now fails on errors and installs from the lockfile; rewrote README and command reference. |
| Existing Python environment pointed to a missing interpreter | Restored it with `uv sync --frozen`. |
| Visual-search article named SigLIP 3 while using SigLIP 2 | Corrected title, removed duplicate main heading, added a summary and distinct slug while preserving the URL. |
| USearch example used an incorrect top-level import | Changed to `from usearch.index import Index` and an explicit supported storage dtype. |
| Unqualified precision/hardware statements | Made precision guidance conditional on the actual model/backend and added primary documentation links. |
| Article images lacked intrinsic dimensions | Added measured dimensions and lazy loading; CSS scales images to the reading width. |

## Content sources and limits

- The supplied August 2026 CV informed the professional overview, interests, education, and teaching/service. Detailed responsibilities and the phone number were not copied into the site. The supplied PDF was not uploaded or substituted for the existing downloadable file.
- [Google Scholar](https://scholar.google.com/citations?user=zfNw5-8AAAAJ&hl=en) was opened directly in the browser. It confirmed the selected papers and the embedding-model patent's 2025 grant; Contextual Query Rewriting is described as an application. No citation metrics were copied, so the homepage does not need citation-count maintenance.
- [LinkedIn](https://au.linkedin.com/in/bistaumanga) exposed limited indexed public information; direct browsing reached its sign-in wall. The CV supplies the specific role description.
- [ACL Anthology](https://aclanthology.org/2020.findings-emnlp.367/) and the [AAAI proceedings](https://ojs.aaai.org/index.php/AAAI/article/download/3764/3642) support publication corrections.
- Article API references: [SigLIP 2 model card](https://huggingface.co/google/siglip2-base-patch16-naflex) and [USearch](https://github.com/unum-cloud/usearch).

## Verification

- Production Pelican build succeeds.
- Generated-site checker validates all 13 HTML pages for local links, fragments, a single main heading, essential metadata, stylesheet links, and image alt text. It also checks sitemap destinations and required output files.
- Browser review at desktop size and a 390-pixel mobile viewport covered the homepage, writing index, article navigation, code layout, and both loaded demo images. The mobile article's document width matches its viewport.
- Shell scripts pass syntax checks. Source changes pass `git diff --check`.

External service availability, authenticated LinkedIn details, and execution of the ML examples are outside these checks. The reviewed changes were subsequently published to GitHub Pages. The configured `www.bistaumanga.com.np` host serves the new site over HTTPS; the bare domain failed TLS hostname verification during the deployment checks. Canonical URLs and the sitemap use the working `www` host. The explicit `./deploy.sh` command rebuilds and validates before publishing.

## Future content maintenance

Keep the short professional overview current as your role changes. Add substantive project notes as new public work becomes available; the homepage automatically lists the three newest articles. Review any older downloadable CV before deciding to promote it from the homepage.
