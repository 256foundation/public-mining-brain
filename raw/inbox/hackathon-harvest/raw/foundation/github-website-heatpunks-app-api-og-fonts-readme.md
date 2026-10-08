# 256foundation/website-heatpunks: app/api/og/fonts/README.md

> Source: https://github.com/256foundation/website-heatpunks/blob/HEAD/app/api/og/fonts/README.md
> Collected: 2026-10-07
> Published: Unknown

# Bundled fonts

`JetBrainsMono-Regular.ttf` and `JetBrainsMono-Bold.ttf` are used by the OpenGraph
image generator (`app/api/og/route.tsx`) to render social-share images in the same
typeface as the site.

- **Font:** JetBrains Mono
- **Source:** https://github.com/JetBrains/JetBrainsMono
- **License:** SIL Open Font License 1.1 (OFL) — https://github.com/JetBrains/JetBrainsMono/blob/master/OFL.txt

The OFL permits bundling and redistribution of the font files with this project.
They are committed to the repo (rather than fetched from a CDN at render time) to
keep image generation self-contained with no external runtime dependency.
