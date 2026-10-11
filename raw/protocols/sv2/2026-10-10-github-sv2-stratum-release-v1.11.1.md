# SRI release v1.11.1

> Source: https://github.com/stratum-mining/stratum/releases/tag/v1.11.1
> Collected: 2026-10-10
> Published: 2026-07-22
> Registry ID: sv2-repo

TAG: v1.11.1 | PUBLISHED: 2026-07-22T15:45:19Z
## General release information

Highlights of this release:

This patch release focuses on improving Stratum V1 difficulty conversion correctness and maintaining crate version consistency.

Notable highlights include:
- `stratum_translation` no longer rounds up Stratum V1 difficulty values during conversion, ensuring more accurate target calculations and better compatibility with existing Stratum V1 implementations.
- `stratum-core` received a patch version bump to maintain version consistency across the workspace following the bug fix.

## Crate changes
`stratum-core`
crate version was bumped from `0.5.0` to `0.5.1`

`stratum_translation`
crate version was bumped from `0.4.0` to `0.4.1`

## What's Changed
* Do not round up SV1 difficulties by @ckolivas in https://github.com/stratum-mining/stratum/pull/2227
* bump PATCH of `stratum-core` by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2230

## New Contributors
* @ckolivas made their first contribution in https://github.com/stratum-mining/stratum/pull/2227

**Full Changelog**: https://github.com/stratum-mining/stratum/compare/v1.11.0...v1.11.1

(release notes truncated to signal by capture agent; full notes at https://github.com/stratum-mining/stratum/releases/tag/v1.11.1)
