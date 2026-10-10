# 256foundation/hydrapool issue #43: Build Payout Plugin System

> Source: https://github.com/256foundation/hydrapool/issues/43
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/hydrapool
- Type: issue
- Number: 43
- State: open
- Author: pool2win
- Opened: 2026-03-19
- Closed: n/a
- Labels: none

## Description

This is highly motivated by this PR https://github.com/256foundation/hydrapool/pull/42 and others including @rkuester requesting ways to modify payout and accounting mechanisms.

The goals of the Plugin system are:

1. Users should be able to write independent crates in Rust to handle accounting and/or payouts.
2. Users should be able to point their payout/accounting crate in Cargo.toml or drop .so file in plugins/ directory. Then activate the plugin in hydrapool's config.toml.
3. Users should have access to well defined and well documented traits to make it clear what they need to do to implement in their plugins. The API should include both accounting parts - like `fill_distribution_from_shares` and building coinbase - like `build_coinbase_transaction`.
4. Users should get access to read/write to rocksdb that hydrapool is using to save shares, read back shares etc. We need a clean API for this - cleaner than what we have, with a limited subset exposed to plugin authors. Some plugins might not need access to this store at all.
5. We should write a score based pplns payout as a plugin and make it the default for hydrapool. We should also move the existing simple_pplns crate into a plugin. This lets us dog food our plugin system with this.
6. We should also provide an implementation of the system @keegreil is using in the above mentioned PR, so he can easily switch. Least we can do for him showing us the way!
