# SRI release v1.12.0

> Source: https://github.com/stratum-mining/stratum/releases/tag/v1.12.0
> Collected: 2026-10-10
> Published: 2026-09-17
> Registry ID: sv2-repo

TAG: v1.12.0 | PUBLISHED: 2026-09-17T13:22:34Z
## General release information

Highlights of this release:

This release is dominated by a deep hardening pass over `channels_sv2`, a breaking refactor of the codec and framing layer, BIP323 adaptations across the protocol stack, and the removal of AES-256-GCM from `noise_sv2`. Every published crate that changed takes an incompatible version bump, so downstream consumers should expect to adapt.

Notable highlights include:

* `channels_sv2` received an extensive correctness and hardening pass covering share validation, job lifecycle, and coinbase construction. Share validation now enforces `min_ntime` and `nTime` bounds across all channel types, share dedup and extranonce-prefix rotation were hardened, and several coinbase defects that could yield consensus-invalid coinbases were fixed, including undersized BIP141 parts and `scriptSig` size/serialization errors.
* `channels_sv2` job storage is now bounded on every axis: future templates, past jobs, replaced group jobs, client future jobs, `rejected_shares`, and `seen_shares`. The past-jobs cap is configurable per channel with a measured default.
* `channels_sv2` fixed several panics and state-machine gaps, including chain-tip transition handling, `StandardChannel::on_new_group_channel_job` on malformed upstream coinbases, an `ExtranoncePrefix` allocation released while live jobs still referenced its bytes, and arithmetic hardened against overflow, underflow, and division by zero.
* BIP323 adaptations landed across the stack: the subprotocol crates, `sv1_api`, `stratum_translation`, and `channels_sv2`, with a supporting `EllSwiftPubKey` type alias added to `binary_sv2`.
* `codec_sv2` and `framing_sv2` were refactored: the `Frame<T, B>` enum was removed and split into `MessageFrame<T>` and `SerializedFrame<B>`, `HandShakeFrame` became `HandshakeMessage`, and a `SizeHint` enum was introduced.
* `binary_sv2` split its inner representation into owned and reference variants, added `B032` as an encodable field, made merkle-root computation return `[u8; 32]` without intermediate allocation, and bounded and redacted oversized values in error output.
* `noise_sv2` dropped its AES-256-GCM support and the `aes-gcm` dependency, leaving ChaCha20-Poly1305 as the sole cipher, alongside a broader hardening pass.
* `sv1_api` exposed all message properties, gained an associated error type on its exposed trait, and now supports typed submit errors and extranonce prefix updates together with `channels_sv2`.
* `stratum_translation` no longer produces rounded Stratum V1 difficulty targets.
* New standardized `error_code` constants were added for protocol version mismatch in `common_messages_sv2` and for channel capacity exhaustion in `mining_sv2`.
* CI now enforces version bumps of modified crates against the highest version published on crates.io, integration tests were accelerated, and a false-green skip when no companion PR is present was fixed.

## Crate changes
`stratum-core`
crate version was bumped from `0.5.1` to `0.6.0`

`channels_sv2`
crate version was bumped from `7.0.0` to `8.0.0`

`binary_sv2`
crate version was bumped from `6.0.0` to `7.0.0`

`derive_codec_sv2`
crate version was bumped from `1.1.3` to `2.0.0`

`codec_sv2`
crate version was bumped from `6.0.0` to `7.0.0`

`framing_sv2`
crate version was bumped from `7.0.0` to `8.0.0`

`noise_sv2`
crate version was bumped from `1.4.2` to `2.0.0`

`sv1_api`
crate version was bumped from `5.0.0` to `6.0.0`

`stratum_translation`
crate version was bumped from `0.4.1` to `0.5.0`

`parsers_sv2`
crate version was bumped from `0.5.0` to `0.6.0`

`handlers_sv2`
crate version was bumped from `0.5.0` to `0.6.0`

`extensions_sv2`
crate version was bumped from `0.2.0` to `0.3.0`

`common_messages_sv2`
crate version was bumped from `8.0.0` to `9.0.0`

`mining_sv2`
crate version was bumped from `11.0.0` to `12.0.0`

`job_declaration_sv2`
crate version was bumped from `9.0.0` to `10.0.0`

`template_distribution_sv2`
crate version was bumped from `6.0.0` to `7.0.0`


## What's Changed
* channels_sv2: keep failed group channel additions atomic by @par1ram in https://github.com/stratum-mining/stratum/pull/2234
* channels_sv2: reject undersized BIP141 coinbase parts by @par1ram in https://github.com/stratum-mining/stratum/pull/2232
* allow access to all sv1 message props by @coleFD in https://github.com/stratum-mining/stratum/pull/2224
* `CONTRIBUTING.md`: anchor dev calls on UTC instead of CET by @plebhash in https://github.com/stratum-mining/stratum/pull/2245
* split inner to owned and ref variants by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2225
* `channels_sv2`: enforce `min_ntime` on `validate_share` (all channel types) by @plebhash in https://github.com/stratum-mining/stratum/pull/2241
* add BIP323 adaptations to `subprotocol` crates by @plebhash in https://github.com/stratum-mining/stratum/pull/2235
* Add assoc error type to sv1 exposed trait by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2268
* `sv1_api` + `stratum-translation`: BIP323 adaptations by @plebhash in https://github.com/stratum-mining/stratum/pull/2237
* `channels_sv2`: BIP323 adaptations + fix version rolling validation by @plebhash in https://github.com/stratum-mining/stratum/pull/2236
* add `Sv2` string to coinbase tag standard by @plebhash in https://github.com/stratum-mining/stratum/pull/2226
* `channels_sv2`: document why coinbase `scriptSig` length prefix is always 1 byte by @plebhash in https://github.com/stratum-mining/stratum/pull/2244
* `channels_sv2`: fix client `set_target` does not refresh targets of already-queued future jobs by @plebhash in https://github.com/stratum-mining/stratum/pull/2257
* Make merkle root from path return [u8; 32] by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2285
* `channels_sv2`: drop future job superseded by reused `template_id` by @plebhash in https://github.com/stratum-mining/stratum/pull/2267
* Dont allocate vec for concat in merkle calculation by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2286
* binary_sv2: hex encode only the displayed prefix of B016M by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2284
* Remove aes256gcm from noise_sv2 by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2270
* `channels_sv2`: harden arithmetic against overflow, underflow and division by zero by @plebhash in https://github.com/stratum-mining/stratum/pull/2239
* `channels_sv2`: bound future-job storage on client channels by @plebhash in https://github.com/stratum-mining/stratum/pull/2266
* `channels_sv2`: bound client `rejected_shares` map by @plebhash in https://github.com/stratum-mining/stratum/pull/2263
* `channels_sv2`: fix chain-tip transition correctness gaps in the job state machine by @plebhash in https://github.com/stratum-mining/stratum/pull/2255
* `channels_sv2`: fix client `StandardChannel::on_new_group_channel_job` panics on malformed upstream coinbase by @plebhash in https://github.com/stratum-mining/stratum/pull/2259
* `channels_sv2`: fix `ExtranoncePrefix` allocation released while live jobs still reference its bytes by @plebhash in https://github.com/stratum-mining/stratum/pull/2261
* `channels_sv2`: fix coinbase `scriptSig` size/serialization defects that yield consensus-invalid coinbases by @plebhash in https://github.com/stratum-mining/stratum/pull/2243
* `common_messages_sv2`: add protocol-version-mismatch `SetupConnectionError` `error_code` by @plebhash in https://github.com/stratum-mining/stratum/pull/2287
* speedup integration tests (on companion PRs) by @plebhash in https://github.com/stratum-mining/stratum/pull/2293
* fix rounded Sv1 difficulty target by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2291
* Remove vec slice encodable binary sv2 by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2295
* `channels_sv2`: bound job-storage retention (future templates, past jobs, replaced group jobs) by @plebhash in https://github.com/stratum-mining/stratum/pull/2290
* add B032 as encodable field by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2306
* return unclaimed bytes and not remove them by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2305
* Noise sv2 hardening by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2283
* add `ERROR_CODE_OPEN_MINING_CHANNEL_CHANNEL_CAPACITY_EXHAUSTED` to `mining_sv2` by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2308
* Add Size hint enum by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2294
* `channels_sv2`: enforce share `nTime` bounds, bound `seen_shares`, and fix job-ID/chain-tip/coinbase validation gaps (plus `template_distribution_sv2` docs fix)) by @plebhash in https://github.com/stratum-mining/stratum/pull/2303
* fix(ci): prevent false green IT skip when no companion is present by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2320
* binary-sv2: bound and redact the ValueExceedsMaxSize sample by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2316
* Acknowledge field and struct visibility in parser by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2328
* `channels_sv2`: make the past-jobs cap configurable w/ a 'good' default value by @gimballock in https://github.com/stratum-mining/stratum/pull/2307
* `binary_sv2`: add EllSwiftPubKey type alias by @plebhash in https://github.com/stratum-mining/stratum/pull/2351
* add `AGENTS.md` by @plebhash in https://github.com/stratum-mining/stratum/pull/2366
* `channels_sv2`: harden share dedup, extranonce-prefix rotation, BIP141 witness framing, and job/target validation by @plebhash in https://github.com/stratum-mining/stratum/pull/2336
* Reject non-finite input in hash_rate_to_target by @gimballock in https://github.com/stratum-mining/stratum/pull/2221
* Binary_sv2 combined loupe fixes by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2343
* Refactor codec and framing by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2317
* feat(channels_sv2, sv1_api): support prefix updates and typed submit errors by @GitGab19 in https://github.com/stratum-mining/stratum/pull/2319
* Add noise unauthenticated initiator docs by @bit-aloo in https://github.com/stratum-mining/stratum/pull/2392
* refine `AGENTS.md` with issue drafting guidelines by @plebhash in https://github.com/stratum-mining/stratum/pull/2389
* enforce version bumps of modified crates via CI by @plebhash in https://github.com/stratum-mining/stratum/pull/2388

## New Contributors
* @par1ram made their first contribution in https://github.com/stratum-mining/stratum/pull/2234

**Full Changelog**: https://github.com/stratum-mining/stratum/compare/v1.11.1...v1.12.0

(release notes truncated to signal by capture agent; full notes at https://github.com/stratum-mining/stratum/releases/tag/v1.12.0)
