# SRI release v1.9.0

> Source: https://github.com/stratum-mining/stratum/releases/tag/v1.9.0
> Collected: 2026-10-10
> Published: 2026-05-05
> Registry ID: sv2-repo

TAG: v1.9.0 | PUBLISHED: 2026-05-05T15:36:19Z
## General release information

Highlights of this release:

This release focuses on `channels_sv2` extranonce and target improvements, fallible Sv1 APIs, and stronger framing/codec validation.

Notable highlights include:
- `channels_sv2` now clamps standard and extended channel targets to the declared `max_target` during channel creation and vardiff updates, fixing low-hashrate miners getting stuck when vardiff computed an easier target than allowed.
- `channels_sv2` added `extranonce_manager`, with `ExtranonceAllocator` and typed prefixes backed by a shared bitmap. It supports pool allocation and proxy sub-allocation from upstream prefixes, prevents standard/extended prefix overlap, and frees slots when prefixes are dropped.
- Client share accounting now tracks rejected shares by upstream `error_code`, rather than only keeping a single rejected-share count.
- `sv1_api` client/server trait methods now return `Result`s across authorization, subscription, submit handling, extranonce/version-rolling state, status updates, and request-id tracking, allowing missing-state errors to propagate.
- `common_messages_sv2` added `has_declare_tx_data(flags)` for checking the Job Declaration `DECLARE_TX_DATA` setup flag.
- Framing and codec coverage improved with `quickcheck` properties for SV2 headers/frames/handshake framing, plus Criterion benchmarks for encoding, decoding, serialization, Noise paths, and buffer-pool behavior.
- Maintenance improved by committing `Cargo.lock`, dispatching `stratum/main` updates to `sv2-apps`, and documenting crate versioning rules for SemVer and public dependency exposure.

## Crate changes
`stratum-core`
crate version was bumped from `0.2.1` to `0.3.0`

`channels_sv2` 
crate version was bumped from `4.0.0` to `5.0.0`

`mining_sv2` 
crate version was bumped from `8.0.0` to `9.0.0`

`common_messages_sv2` 
crate version was bumped from `7.0.0` to `7.1.0`

`parsers_sv2`
crate version was bumped from `0.2.2` to `0.3.0`

`handlers_sv2`
crate version was bumped from `0.2.2` to `0.3.0`

`sv1_api`
crate version was bumped from `3.0.0` to `4.0.0`

`stratum_translation`
crate version was bumped from `0.1.3` to `0.2.0`

## What's Changed
* ci: dispatch stratum main updates to sv2-apps by @plebhash in https://github.com/stratum-mining/stratum/pull/2121
* Fix CI by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2127
* Add prop test to framing by @Shourya742 in https://github.com/stratum-mining/stratum/pull/2085
* contribution guidelines for crate versioning by @plebhash in https://github.com/stratum-mining/stratum/pull/2133
* Make sv1 server trait methods return results by @Shourya742 in https://github.com/stratum-mining/stratum/pull/2134
* bump sv1-api dependent crate by @Shourya742 in https://github.com/stratum-mining/stratum/pull/2137
* channels_sv2: clamp target to max_target instead of erroring by @vnprc in https://github.com/stratum-mining/stratum/pull/2118
* Add codec benches by @Shourya742 in https://github.com/stratum-mining/stratum/pull/2058
* Add `extranonce_manager` module in `channels_sv2` by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2098
* channels_sv2::client::share_accounting keeps track of `error_code` for rejected shares by @plebhash in https://github.com/stratum-mining/stratum/pull/2139
* feat(common-messages): add has_declare_tx_data helper function by @wcqy-ye in https://github.com/stratum-mining/stratum/pull/2129
* use rust 1.85 in `release-libs` workflow by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2144
* add override step to `release-libs` workflow by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2145
* update error handling in `release-libs.sh` by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2146

## New Contributors
* @wcqy-ye made their first contribution in https://github.com/stratum-mining/stratum/pull/2129

**Full Changelog**: https://github.com/stratum-mining/stratum/compare/v1.8.0...v1.9.0

(release notes truncated to signal by capture agent; full notes at https://github.com/stratum-mining/stratum/releases/tag/v1.9.0)
