# sv2-apps release v0.7.0

> Source: https://github.com/stratum-mining/sv2-apps/releases/tag/v0.7.0
> Collected: 2026-10-10
> Published: 2026-07-24
> Registry ID: sv2-repo

TAG: v0.7.0 | PUBLISHED: 2026-07-24T09:17:01Z
## General release information

Highlights of this release:

This release focuses on Job Declaration stability, Bitcoin Core integration improvements, Translator Proxy correctness, and runtime reliability across the Sv2 application stack.

Notable highlights include:
- The **Job Declarator Server (JDS)** now isolates `DownstreamState`, improving internal state management and reducing coupling between downstream connections.
- The **Job Declarator Client (JDC)** received a fix for a `RequestTransactionData` race condition, improving reliability during transaction retrieval and template construction.
- `bitcoin_core_sv2` improved template distribution responsiveness by eliminating unintended `min_interval` delays during chain-tip updates, resulting in faster propagation of new templates. It also cleans up outdated `TemplateData` associated with `CoinbaseOutputConstraints`.
- Translation Proxy payout verification was fixed to correctly handle split coinbase `scriptSig`s, and `UserIdentity` TLVs are now only constructed when extension `0x0002` has been successfully negotiated, ensuring full protocol compliance.
- Downstream share validation now verifies shares against the advertised power-of-two difficulty, improving correctness and compatibility with Stratum V1 miners.
- Mining infrastructure can now automatically discover ASIC telemetry endpoints using the miner username and port, simplifying deployment and monitoring.
- Pool runtime shutdown handling was centralized, while channel-management internals were simplified through removal of obsolete reset methods and unnecessary open-channel request forwarding.
- `stratum-apps` introduced the `SharedSet` synchronization wrapper and continued internal refactoring, documentation improvements, and dependency updates to keep the application stack aligned with the latest `stratum-core` release.

## What's Changed
* fix `release-apps.yaml` due to new dependency relationship between `stratum-apps` and `bitcoin_core_sv2` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/608
* Fix broken intra-doc links and clean up comments by @nulllpc in https://github.com/stratum-mining/sv2-apps/pull/546
* Fix payout verification for split coinbase scriptSig by @GitGab19 in https://github.com/stratum-mining/sv2-apps/pull/614
* introduce shared modules to `bitcoin_core_sv2` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/602
* Shutdown centralized in Pool runtime flow by @Shourya742 in https://github.com/stratum-mining/sv2-apps/pull/613
* JDS isolates `DownstreamState` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/592
* Remove send open channel request to mining handler by @Shourya742 in https://github.com/stratum-mining/sv2-apps/pull/627
* `bitcoin_core_sv2`: clean up outdated `TemplateData` on `CoinbaseOutputConstraints` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/612
* discover ASIC telemetry by miner's username and port  by @GitGab19 in https://github.com/stratum-mining/sv2-apps/pull/615
* fix `bitcoin_core_sv2` unintentional `min_interval` delays on chain-tip updates by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/632
* Validate downstream shares against the advertised pow2 difficulty by @ckolivas in https://github.com/stratum-mining/sv2-apps/pull/630
* stratum-apps: add `SharedSet` synchronization wrapper by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/640
* fix JDC `RequestTransactionData` race by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/628
* Remove reset methods by @Shourya742 in https://github.com/stratum-mining/sv2-apps/pull/636
* revert shared modules on `bitcoin_core_sv2` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/642
* chore(deps): update stratum-core to c1a7991 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/643
* tProxy: build `UserIdentity` TLV only when extension `0x0002` is negotiated inside ChannelManager by @GitGab19 in https://github.com/stratum-mining/sv2-apps/pull/624

## New Contributors
* @ckolivas made their first contribution in https://github.com/stratum-mining/sv2-apps/pull/630

**Full Changelog**: https://github.com/stratum-mining/sv2-apps/compare/v0.6.0...v0.7.0
