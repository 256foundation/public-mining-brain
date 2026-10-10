# 256foundation/website pull request #19: perf(newsroom): right-size article art, fix optimizer cache

> Source: https://github.com/256foundation/website/pull/19
> Collected: 2026-10-07
> Published: 2026-09-29

- Repository: 256foundation/website
- Type: pull request
- Number: 19
- State: closed
- Author: tylerkstevens
- Opened: 2026-09-29
- Closed: 2026-09-29
- Labels: none

## Description

## Why the newsroom thumbnails were slow

The site is self-hosted (Caddy → Docker container, not Vercel), so every `/_next/image` request is handled by the Next optimizer in the container. Three things compounded:

1. **The optimizer's disk cache never worked in the container.** `.next` is copied root-owned and the runner drops to the unprivileged `nextjs` user, which can't create `.next/cache/images`. Four back-to-back requests for the same image all returned `x-nextjs-cache: MISS`, and response time scaled with source size (~0.23s for a 29KB banner vs ~1.0s for a 1.5MB PNG) — i.e. it re-decoded and re-encoded from the source every time.
2. **`minimumCacheTTL` defaulted to 60s** (`cache-control: public, max-age=60, must-revalidate`), so browsers re-fetched optimized bytes a minute later.
3. **Covers were huge originals** (`deck-cover.png` 1.5MB, `og-hrf…png` 753KB, `gladstein_schnitzel_doomaxe.png` 3.2MB/5712px) and `deviceSizes` offered 2048/3840 for sources only 1376–1536px wide.

## Changes

- **`scripts/optimize-images.mjs`** (new, `npm run optimize:images`): re-encodes `public/newsroom` art to WebP (max 1600px, q82), rewrites all references, removes originals. **12.2MB → 1.8MB**; covers now 14–179KB. Idempotent.
- **`next.config.ts`**: `minimumCacheTTL: 31536000` (sources are immutable per deploy); `deviceSizes` capped at 1920 with 1600 added, dropping 2048/3840.
- **`Dockerfile`**: `mkdir -p .next/cache/images && chown -R nextjs:nodejs .next` so the optimizer can actually cache.
- **`package.json`**: pin `sharp` (already a transitive next optional dep) so it's traced into the standalone runtime.

## Verification

- Locally against a production build: first request 0.12s, **second identical request `x-nextjs-cache: HIT` in ~1.5ms**, `cache-control: public, max-age=31536000`.
- `sharp` is now present in `.next/standalone/node_modules`; built `srcset` no longer lists 2048/3840 and contains no stale `.png/.jpeg` refs.
- `npm run build`, `npm run lint` (0 errors), `npm test` (26/26) all pass.

## Notes for review

- All newsroom art is now WebP, including `ogImage`. Every major social scraper supports WebP OG; if you'd rather keep PNG for OG previews, say so and I'll emit PNG siblings for those.
- Caddy has no `Cache-Control` rule for `/_next/image` in this repo — an edge cache there would be a further win, but the container fix is what stops the re-encoding.
- Deploy will need a fresh image; merged and pushed to `main` triggers the normal build/deploy workflow.
