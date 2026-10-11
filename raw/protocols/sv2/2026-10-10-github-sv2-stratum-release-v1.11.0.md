# SRI release v1.11.0

> Source: https://github.com/stratum-mining/stratum/releases/tag/v1.11.0
> Collected: 2026-10-10
> Published: 2026-07-08
> Registry ID: sv2-repo

TAG: v1.11.0 | PUBLISHED: 2026-07-08T16:00:16Z
## General release information

Highlights of this release:

This release focuses on `binary_sv2` reliability and cleanup, safer Sv1 parsing and conversion APIs, improved Sv1 difficulty handling, and expanded fuzz-testing coverage.

Notable highlights include:

* `binary_sv2` received several reliability and maintainability improvements, including absolute paths in procedural macro expansions, proper compile-time errors from proc macros, restored `std` build support, and broad cleanup of unused code and internal APIs.
* `sv1_api` parsing and conversion paths were made safer by removing several `unwrap` calls, introducing the `BadBytesConvert` parsing error, and using `bitcoin::hashes::hex` for hexadecimal conversions.
* `HexBytes` and `HexU32Be` now rely on their standard serialization and deserialization implementations instead of custom `serde` implementations, simplifying the Sv1 API and reducing duplicated conversion logic.
* `stratum-translation` added integer power-of-two Sv1 difficulty conversion, improving difficulty and target conversion behavior between Stratum V1 and Stratum V2.
* `sv1_api` gained dedicated fuzz targets, expanding automated coverage of parsing and protocol-handling edge cases.
* `channels_sv2::server::jobs::job_store::JobStore` has been deprecated as part of the ongoing refinement and simplification of channel-management APIs.
* CI execution was accelerated by adopting `cargo binstall` for tool installation.

## Crate changes
`binary_sv2`
crate version was bumped from `5.0.0` to `6.0.0`

`parsers_sv2`
crate version was bumped from `0.4.0` to `0.5.0`

`sv1_api`
crate version was bumped from `4.0.0` to `5.0.0`

`stratum-core`
crate version was bumped from `0.4.0` to `0.5.0`

`stratum_translation`
crate version was bumped from `0.3.0` to `0.4.0`

`channels_sv2`
crate version was bumped from `6.0.0` to `7.0.0`

`codec_sv2`
crate version was bumped from `5.0.0` to `6.0.0`

`extensions_sv2`
crate version was bumped from `0.1.0` to `0.2.0`

`framing_sv2`
crate version was bumped from `6.0.1` to `7.0.0`

`handlers_sv2`
crate version was bumped from `0.4.0` to `0.5.0`

`common_messages_sv2`
crate version was bumped from `7.2.0` to `8.0.0`

`job_declaration_sv2`
crate version was bumped from `8.0.0` to `9.0.0`

`mining_sv2`
crate version was bumped from `10.0.0` to `11.0.0`

`template_distribution_sv2`
crate version was bumped from `5.1.0` to `6.0.0`

`derive_codec_sv2`
crate version was bumped from `1.1.2` to `1.1.3`

## What's Changed
* Add absolute path in binary sv2 proc macro by @Shourya742 in https://github.com/stratum-mining/stratum/pull/2185
* Fix binary_sv2 std build by @Shourya742 in https://github.com/stratum-mining/stratum/pull/2187
* Remove unused entities in `binary_sv2` + `common_messages_sv2` + `template_distribution_sv2` by @Shourya742 in https://github.com/stratum-mining/stratum/pull/2189
* Use compile error in proc macro by @Shourya742 in https://github.com/stratum-mining/stratum/pull/2186
* deprecate `channels_sv2::server::jobs::job_store::JobStore` by @plebhash in https://github.com/stratum-mining/stratum/pull/2190
* remove unwrap from `sv1_api::Subscribe::TryFrom` by @lucasbalieiro in https://github.com/stratum-mining/stratum/pull/2198
* adjust hex conversion on sv1 to use `bitcoin::hashes::hex` by @lucasbalieiro in https://github.com/stratum-mining/stratum/pull/2205
* add `BadBytesConvert` to `ParsingMethodError` in `sv1_api` by @lucasbalieiro in https://github.com/stratum-mining/stratum/pull/2207
* add integer power-of-two Sv1 difficulty conversion in `stratum-translation` by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2210
* accelerate CI via `cargo binstall` by @plebhash in https://github.com/stratum-mining/stratum/pull/2209
* remove custom impls of `serde::Deserialize` and `serde::Serialize` for HexBytes and HexU32Be by @lucasbalieiro in https://github.com/stratum-mining/stratum/pull/2212
* remove `unwrap` calls when using `as_u64` by @lucasbalieiro in https://github.com/stratum-mining/stratum/pull/2219
* Binary sv2 cleanup by @Shourya742 in https://github.com/stratum-mining/stratum/pull/2200
* add fuzz targets for sv1 crate by @lucasbalieiro in https://github.com/stratum-mining/stratum/pull/2220


**Full Changelog**: https://github.com/stratum-mining/stratum/compare/v1.10.0...v1.11.0

(release notes truncated to signal by capture agent; full notes at https://github.com/stratum-mining/stratum/releases/tag/v1.11.0)
