# 256foundation/mujina-website pull request #4: Redirect mujina.org to the source repository

> Source: https://github.com/256foundation/mujina-website/pull/4
> Collected: 2026-10-07
> Published: 2026-07-07

- Repository: 256foundation/mujina-website
- Type: pull request
- Number: 4
- State: closed
- Author: rkuester
- Opened: 2026-07-07
- Closed: 2026-07-08
- Labels: none

## Description

mujina.org still shows the original grant proposal and it's well out of date. Mujina will want a proper user-facing site eventually, but until then pointing at the source repo beats pointing at a stale page. This PR turns the site into a straight redirect to https://github.com/256foundation/mujina.

GitHub Pages can't do server-side redirects, so index.html and 404.html use an instant meta refresh instead (search engines treat that about the same as a 301). The 404 page catches old deep links. The CNAME stays as-is so the domain and cert keep working, and .nojekyll skips the Jekyll build since there's nothing left to render. The old page, the Jekyll config, and the lander image are gone from the tree but still in git history.

No DNS changes needed; the domain already points at Pages, and Pages folds www into the apex on its own.
