# SRI release v1.10.0

> Source: https://github.com/stratum-mining/stratum/releases/tag/v1.10.0
> Collected: 2026-10-10
> Published: 2026-06-03
> Registry ID: sv2-repo

TAG: v1.10.0 | PUBLISHED: 2026-06-03T14:30:32Z
## General release information
This release focuses on share accounting improvements, channel-management API refinements, and protocol/specification alignment.

Notable highlights include:
- `channels_sv2::server::share_accounting` now tracks rejected shares alongside accepted shares, while share-work accounting has been updated to use `u64` where appropriate for improved correctness and scalability.
- `channels_sv2::server` added a `stable_hashrate` flag, providing additional control over hashrate stability behavior.
- Standardized `error_code` constants were introduced across the protocol implementation.
- `channels_sv2` replaced reference-based getters with accessor APIs, simplifying the public API and improving encapsulation.
- Custom-work mining received stability improvements, fixing a share-validation panic after `SetNewPrevHash` and correcting chain-tip transition handling for custom mining jobs.
- Specification compatibility was improved through protocol-alignment fixes, ensuring closer adherence to the latest Stratum V2 specifications.

## Crate changes
`stratum-core`
crate version was bumped from `0.3.0` to `0.4.0`

`channels_sv2` 
crate version was bumped from `5.0.0` to `5.1.0`

`mining_sv2` 
crate version was bumped from `9.0.0` to `10.0.0`

`job_declaration_sv2` 
crate version was bumped from `7.0.0` to `8.0.0`

`template_distribution_sv2`
crate version was bumped from `5.0.0` to `5.1.0`

`common_messages_sv2` 
crate version was bumped from `7.1.0` to `7.2.0`

`parsers_sv2`
crate version was bumped from `0.3.0` to `0.4.0`

`handlers_sv2`
crate version was bumped from `0.3.0` to `0.4.0`

`stratum_translation`
crate version was bumped from `0.2.0` to `0.3.0`

## What's Changed
* add `stable_hashrate` flag to `channels_sv2::server` by @plebhash in https://github.com/stratum-mining/stratum/pull/2152
* add `error_code` constants by @plebhash in https://github.com/stratum-mining/stratum/pull/2151
* represent share work as `u64` (where appropriate) by @plebhash in https://github.com/stratum-mining/stratum/pull/2138
* `channels_sv2::server::share_accounting` keeps track of rejected shares by @plebhash in https://github.com/stratum-mining/stratum/pull/2149
* refine `CONTRIBUTING.md` with versioning exception to `stratum-core` by @plebhash in https://github.com/stratum-mining/stratum/pull/2158
* fix validate_share panic after on_set_new_prev_hash in custom-work mode by @rx18-eng in https://github.com/stratum-mining/stratum/pull/2156
* add `ERROR_CODE_OPEN_MINING_CHANNEL_EXTENDED_CHANNELS_NOT_SUPPORTED_FOR_STANDARD_JOBS` by @plebhash in https://github.com/stratum-mining/stratum/pull/2162
* Revert "refine `CONTRIBUTING.md` with versioning exception to `stratum-core`" by @plebhash in https://github.com/stratum-mining/stratum/pull/2160
* fix specs incompatibilities by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2165
* Fix custom mining job chain-tip transitions by @0xjc65eth in https://github.com/stratum-mining/stratum/pull/2164
* `channels_sv2`: replace ref getters with accessor APIs by @plebhash in https://github.com/stratum-mining/stratum/pull/2161

## New Contributors
* @rx18-eng made their first contribution in https://github.com/stratum-mining/stratum/pull/2156
* @0xjc65eth made their first contribution in https://github.com/stratum-mining/stratum/pull/2164

**Full Changelog**: https://github.com/stratum-mining/stratum/compare/v1.9.0...v1.10.0

(release notes truncated to signal by capture agent; full notes at https://github.com/stratum-mining/stratum/releases/tag/v1.10.0)
