# sv2-apps release v0.8.0

> Source: https://github.com/stratum-mining/sv2-apps/releases/tag/v0.8.0
> Collected: 2026-10-10
> Published: 2026-09-17
> Registry ID: sv2-repo

TAG: v0.8.0 | PUBLISHED: 2026-09-17T14:20:53Z
## General release information

Highlights of this release:

This release focuses on security hardening across the whole Sv2 application stack, driven by the findings of the Loupe audit, together with a deep Translator Proxy overhaul, structured runtime lifecycles for every application, and a simpler configuration story for containerized deployments.

Notable highlights include:
- The **Translator Proxy (tProxy)** Sv1 session and channel lifecycle was extensively hardened. Handshake completion is now idempotent, job notifications start only after both `mining.subscribe` and `mining.authorize` complete, `mining.extranonce.subscribe` is honored, extranonce prefix changes are applied without recreating channels, and malformed notifications no longer panic. Late Sv1 shares are validated against the target and extranonce of their own job, with standard Sv1 rejection errors for missing jobs, duplicates and low-difficulty shares.
- tProxy aggregated-mode channel handling now rejects channel opens when no extranonce space or channel ID is available, prevents downstream IDs from colliding with the aggregated channel, and isolates failures to the affected miner. Difficulty failures on one downstream no longer affect the others, and failed channel-open requests are cleaned up correctly.
- tProxy now supports the **BIP323 version rolling mask**, with a matching `invalid-non-rollable-version-bit` share rejection code exposed through the monitoring API.
- The **Job Declarator Client (JDC)** and tProxy now run on typestate-based runtime machines (`JdcRuntime`, `TranslatorRuntime`) that manage bootstrap, component lifecycles and graceful shutdown without `unwrap`/`expect`. `PoolRuntime` was aligned with the same pattern, and SIGINT handling was fixed across all applications.
- **Pool** and **JDC** no longer exhaust their extranonce allocators, handle the new `SeenSharesBudgetExhausted` share-validation error from `channels_sv2`, and the Pool's past-jobs cap is now configurable via `max_past_jobs`. JDC also rejects unknown `mode` values in its configuration, orders cached shares by target rather than raw hash bytes, and handles malformed Template Provider transactions without panicking.
- Protocol compliance was tightened across Pool, JDS, JDC and tProxy: `SetupConnection` version ranges are enforced, non-setup responses during the handshake are rejected, and the applications incorporate the `noise_sv2`, codec/framing and `channels_sv2` hardening work landed in `stratum-core`.
- `bitcoin_core_sv2` hardens the JDP `handle_declare_mining_job` path against untrusted `DeclareMiningJob` inputs and fixes a `u32` overflow in `coinbase_weight`. The crate was bumped to `0.6.0` and its README now documents JDP alongside TDP.
- Every configuration option can now be set through **environment variables**, removing the need for `envsubst` in containerized deployments. tProxy and JDC also try every DNS address of an upstream instead of only the first.
- Internals were simplified by replacing the custom mutex with shared synchronization primitives across the Translator, JDS and integration tests, and all workspaces moved to Rust edition 2024.
- Development workflow improvements: integration tests run faster, version bumps are now enforced by CI, and `AGENTS.md` plus `scripts/cross-repo.sh` document the cross-repo workflow with `stratum`.
- The application stack is aligned with the latest `stratum-core` `0.6.0` release.

## What's Changed
* Replace custom mutex with shared primitives in IT by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/639
* Replace custom mutex/dashmap with shared primitves in JDS by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/641
* expose all config options as environment variables by @based64god in https://github.com/stratum-mining/sv2-apps/pull/585
* chore: Update rust edition to 2024 in Cargo.toml by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/651
* chore(deps): update stratum-core to 9e18d11 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/652
* chore(deps): update stratum-core to 68c5bf6 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/653
* chore(deps): update stratum-core to 408a6fd by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/654
* Use sort-unstable-by instead of sort-by by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/657
* chore(deps): update stratum-core to 0fdc873 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/660
* binary inner split sv2-app fallout by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/616
* chore(deps): update stratum-core to 35af62e by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/662
* `CONTRIBUTING.md`: anchor dev calls on UTC instead of CET by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/659
* chore(deps): update stratum-core to 30ca82a by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/663
* Use assoc error type from sv1 crate in translator by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/664
* `translator_sv2`: BIP323 version rolling mask by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/656
* `monitoring`: add `invalid-non-rollable-version-bit` to `SHARE_REJECTION_CODES` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/655
* revert logging Sv2 messages with `Display` instead of `Debug` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/680
* chore(deps): update stratum-core to b13195e by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/684
* chore(deps): update stratum-core to 1e947c8 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/686
* chore(deps): update stratum-core to f1d40a0 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/687
* chore(deps): update stratum-core to 281c58f by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/690
* chore(deps): update stratum-core to fa55e05 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/692
* fix: remove useless conversion after `stratum-core` bump by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/691
* chore(deps): update stratum-core to 8afee88 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/696
* chore(deps): update stratum-core to 0f282bb by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/697
* Migrate translator to shared synchronous primitive by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/530
* `bitcoin-core-sv2`: fix `u32` overflow in `coinbase_weight` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/678
* Refactor(jd-client): replace monolithic start loop with JdcRuntime typestate machine by @nulllpc in https://github.com/stratum-mining/sv2-apps/pull/633
* chore(deps): update stratum-core to 812acb5 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/699
* chore(deps): update stratum-core to 416a723 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/700
* chore(deps): update stratum-core to 646eb72 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/701
* `miner-apps`: adapt to `channels_sv2` `on_share_rejection` taking `&str` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/693
* chore(deps): update stratum-core to a11bf7a by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/703
* chore(deps): update stratum-core to 7f4838a by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/704
* chore(deps): update stratum-core to 2680220 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/705
* `PoolRuntime` startup and shutdown gaps, aligned with #633 by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/685
* JDC: propagate `GroupChannel::set_full_extranonce_size` error by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/658
* fix bad SIGINT patterns by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/689
* speed up integration tests by @GitGab19 in https://github.com/stratum-mining/sv2-apps/pull/698
* enforce `SetupConnection` version ranges by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/695
* chore(deps): update stratum-core to 91d4c36 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/712
* Fix tproxy open channel lifecycle by @GitGab19 in https://github.com/stratum-mining/sv2-apps/pull/710
* chore(deps): update stratum-core to 9f105cc by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/713
* fix(translator): isolate downstream difficulty failures by @GitGab19 in https://github.com/stratum-mining/sv2-apps/pull/709
* chore(deps): update stratum-core to 905cf73 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/727
* Reject non setup handshake responses by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/720
* Reject unknown JDC mode values in config by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/722
* Handle malformed template provider transactions without panic by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/724
* Order cached shares by target, not raw hash bytes by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/726
* Bye Bye custom mutex by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/728
* chore(deps): update stratum-core to 6e30341 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/732
* chore(deps): update stratum-core to d1808b1 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/736
* chore(deps): update stratum-core to 59a3e3e by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/737
* Noise-sv2 hardening  by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/706
* chore(deps): update stratum-core to aa24270 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/739
* fix tProxy channel safety in aggregated-mode by @GitGab19 in https://github.com/stratum-mining/sv2-apps/pull/729
* `bitcoin-core-sv2`: harden JDP `handle_declare_mining_job` against untrusted `DeclareMiningJob` inputs by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/677
* Fix extranonce allocator exhaustion in Pool and JDC by @GitGab19 in https://github.com/stratum-mining/sv2-apps/pull/740
* refactor(translator): replace monolithic start loop with TranslatorRuntime typestate machine by @nulllpc in https://github.com/stratum-mining/sv2-apps/pull/644
* chore(deps): update stratum-core to 3f5076e by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/804
* Pool+JDC: handle new `SeenSharesBudgetExhausted `error variant from `channels_sv2` share validation by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/733
* chore(deps): update stratum-core to cfb848e by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/822
* chore(deps): update stratum-core to ca3cc83 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/824
* chore(deps): update stratum-core to 941d004 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/825
* JDC: document `user_identity` in `README.md` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/827
* apps: pass `max_past_jobs` to channel constructors by @gimballock in https://github.com/stratum-mining/sv2-apps/pull/735
* chore(deps): update stratum-core to a79e780 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/841
* add `AGENTS.md` + `cross-repo.sh` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/840
* chore(deps): update stratum-core to fea42ee by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/842
* chore(deps): update stratum-core to 682136e by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/843
* `channels_sv2` hardening companion by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/826
* chore(deps): update stratum-core to b468c5f by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/844
* tProxy+JDC: try every DNS address of an upstream, not just the first by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/847
* chore(deps): update stratum-core to d30a0e2 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/849
* Fix tProxy issues found by Loupe by @GitGab19 in https://github.com/stratum-mining/sv2-apps/pull/741
* Codec and framing refactor fallout by @bit-aloo in https://github.com/stratum-mining/sv2-apps/pull/806
* harden tProxy Sv1 session and channel lifecycle by @GitGab19 in https://github.com/stratum-mining/sv2-apps/pull/823
* chore(deps): update stratum-core to ccd21c0 by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/863
* chore(deps): update stratum-core to fb5b43e by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/864
* refine `AGENTS.md` with issue drafting guidelines by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/860
* chore(deps): update stratum-core to e11881b by @SV2-bot in https://github.com/stratum-mining/sv2-apps/pull/866
* chore: bump `bitcoin_core_sv2` to `0.6.0` by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/865
* enforce versioning rules via CI by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/868
* docs(bitcoin-core-sv2): cover JDP alongside TDP by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/869
* ci: run the version bump check only on pull requests by @plebhash in https://github.com/stratum-mining/sv2-apps/pull/871

## New Contributors
* @based64god made their first contribution in https://github.com/stratum-mining/sv2-apps/pull/585

**Full Changelog**: https://github.com/stratum-mining/sv2-apps/compare/v0.7.0...v0.8.0
