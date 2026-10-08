# 256foundation/website pull request #16: fix(feeds): retry RSS fetches so a build hiccup cannot blank a column

> Source: https://github.com/256foundation/website/pull/16
> Collected: 2026-10-07
> Published: 2026-09-07

- Repository: 256foundation/website
- Type: pull request
- Number: 16
- State: closed
- Author: tylerkstevens
- Opened: 2026-09-07
- Closed: 2026-09-07
- Labels: none

## Description

The live home page shipped saying **"No issues yet."** under Newsletter. The feed was fine — the fetch failed.

## Why it happened

`/` is statically prerendered, so its feed fetches run during the Docker build on the GitHub Actions runner. The fetchers fail soft to `[]`, so one failed fetch bakes an empty column into the image and it stays empty until the next hourly revalidation.

Substack sits behind Cloudflare, which intermittently challenges datacenter IPs. It is not user-agent filtering or rate limiting: from a normal client the feed returns 200 for every UA tried, including no UA, and for five rapid consecutive requests. The same feed populated correctly on this morning's build and failed on this afternoon's.

## The fix

**`lib/feed.ts`** — one shared `fetchFeedXml` for both feeds:
- a real `User-Agent` and `Accept`, rather than the default runtime UA
- `AbortSignal.timeout(8000)` bounding each attempt
- 3 attempts with linear backoff, retrying 429 and 5xx
- immediate give-up on 404-style responses that will not fix themselves

Applies to the POD256 feed too, which had the same exposure.

**Honest empty state** — an empty list means the fetch failed, not that no issues exist. The column now points at Substack instead of asserting there is nothing to read.

## Verified

- Retry control flow exercised against a stub server: recovers on attempt 3 after two 503s (3 hits); a 404 returns null after 1 hit with no wasted retries
- All six cards and all three lead images render locally through the new path
- `npm test` 26/26, `npm run build` clean, `npm run lint` 0 errors

Note this reduces the odds of a blank column but cannot eliminate them — if Cloudflare challenges all three attempts, the column still falls back, now with honest copy.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
