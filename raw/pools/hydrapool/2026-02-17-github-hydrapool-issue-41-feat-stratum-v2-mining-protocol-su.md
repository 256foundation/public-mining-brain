# 256foundation/hydrapool issue #41: feat: Stratum v2 Mining Protocol support

> Source: https://github.com/256foundation/hydrapool/issues/41
> Collected: 2026-10-07
> Published: 2026-02-17

- Repository: 256foundation/hydrapool
- Type: issue
- Number: 41
- State: open
- Author: average-gary
- Opened: 2026-02-17
- Closed: n/a
- Labels: none

## Description

### Background

Following up on the discussion in #37 — I've put together a plan and started working toward adding native SV2 Mining Protocol support for downstream miners.

### `stratum-core` vs legacy SRI crates

The concerns raised in #37 about technical debt and tight coupling in the `*_sv2` crates are well-taken. Since that discussion, the `stratum-mining` org published [`stratum-core`](https://crates.io/crates/stratum-core) (v0.2.0), a ground-up refactor that consolidates the protocol primitives into a single crate with cleaner APIs — `Responder` for Noise handshake, `StandardChannel`/`ExtendedChannel` with built-in `validate_share()`, and all Mining Protocol message types. This plan uses `stratum-core` rather than the legacy individual crates.

### Design

**Dual-protocol:** SV1 continues on port 3333, SV2 listens on port 3334. Both feed validated shares into the existing `Emission` pipeline — PPLNS accounting, block submission, and metrics work unchanged downstream.

**Scope:** Pool-side Mining Protocol only. No Job Declaration Protocol, no Template Distribution Protocol. The pool continues to build block templates via `getblocktemplate` + ZMQ.

**Integration seam:** SV2-validated shares produce the same `Emission` struct sent through the existing `emissions_tx` channel. Everything downstream is protocol-agnostic.

**User identity:** `SetupConnection.user_identity` enforces a Bitcoin address, same convention as SV1's `mining.authorize`.

### Phases

| Phase | Summary |
|-------|---------|
| 0 — Foundation | Add `stratum-core` dependency, SV2 config section |
| 1 — Connections | Noise handshake, SetupConnection handler, connection registry |
| 2 — Channels | Standard channels, Extended channels, vardiff lifecycle |
| 3 — Jobs | GBT→SV2 template bridge, job distribution, SetNewPrevHash |
| 4 — Shares | SubmitSharesStandard/Extended, Emission bridge |
| 5 — Wiring | `main.rs` integration, Docker/packaging |
| 6 — Testing | Unit, integration, interop tests |
| 7 — Metrics | Prometheus counters, Grafana dashboards |

Detailed issue breakdowns and task tracking: **[Project Board](https://github.com/users/average-gary/projects/1)**

### Approach

Developing on forks of both `hydrapool` and `p2poolv2`. The SV2 code lives as a new `stratum_sv2/` module in `p2poolv2_lib` alongside the existing `stratum/` module, with minimal changes to `hydrapool` itself (config + wiring in `main.rs`). Intent is to contribute upstream as PRs.

Open to feedback on the design or phasing.

## Comments

### rkuester on 2026-02-17

+1 for Sv2 in Hydrapool. We'll be working work towards landing Sv2 in Mujina too.

### pool2win on 2026-02-18

This is so awesome! Thanks Gary for taking charge here. You know SV2 well, so it'll be great to have you build this out. The level of detail on your project is awesome too.

It is good to know the refactor is ready and stratum-core has been shipped. I'll take this opportunity to look at the relevant crates from there.

Which stratum-core crates will we need to import here? I saw in https://github.com/average-gary/hydrapool/issues/2 that we import the entire stratum-core. Curious if we can selectively import from there?

The reason is to not build all dependencies of all the other crates that we don't use. This will also make the vulnerabilities checker flag all dependencies of all the crates that we don't even use. The con of direct imports is that we have to make sure the crates we do import from stratum-core will need to have compatible versions - I think we can manage that. What do you think? 

Out of curiosity, which stratum-core crates do we need? I am just guessing a list here, so please be patient with my lack of awareness on the new crates structure.

- [ ] noise_sv2
- [ ] parsers_sv2?
- [ ] framing_sv2?
- [ ] mining_sv2?
- [ ] stratum_translation?

Also, you can leave the Prom/Grafan work out of the project. We need to do a re-write of the approach we took last year. I want to switch to open telemetrics and improve logging to Grafana too. The next telehash is in May. So I was punting that work till late March, early April.

### average-gary on 2026-02-27

Hey @pool2win  — thanks for the feedback and for looking into stratum-core. Wanted to circle back with a full status update since a lot has been built out since this was posted.

## stratum-core imports

We addressed this by forking stratum-core ([average-gary/stratum:feature-flag-subprotocols](https://github.com/average-gary/stratum/tree/feature-flag-subprotocols)) and adding feature gates on the subprotocols. 

The workspace dependency is:
`stratum-core = { git = "...", branch = "feature-flag-subprotocols", default-features = false, features = ["mining"] }`

This pulls in only the Mining Protocol subprotocol — no Job Declaration, no Template Distribution. The crates actually used at runtime are:
- `noise_sv2` — Noise NX handshake (Responder)
- `codec_sv2` — Noise encrypt/decrypt, frame encode/decode
- `framing_sv2` — SV2 frame types
- `mining_sv2` — All Mining Protocol message structs (OpenStandardMiningChannel, NewMiningJob, SubmitSharesStandard, SetNewPrevHash, SetTarget, plus the extended variants)
- `common_messages_sv2` — SetupConnection / SetupConnectionSuccess
- `parsers_sv2` — AnyMessage enum for dispatch
- `binary_sv2` — Wire format types (U256, Str0255, B064K, Seq0255, etc.)
 
These are all internal crates re-exported through stratum-core's single crate facade. With `default-features = false, features = ["mining"]`, the JD and TD subprotocol crates (and their deps) are excluded from the build entirely.

Additionally, `stratum-core` is behind an `sv2` cargo feature flag in `p2poolv2_lib`, so it's not even compiled unless you opt in:
```
[features]
sv2 = ["dep:stratum-core"]
```

## What was built
[p2pool-v2: sv2-support](https://github.com/average-gary/p2pool-v2/tree/sv2-support)
All implementation lives in `p2poolv2_lib/src/stratum_sv2/` (new module, alongside existing stratum/). The SV2 code is entirely additive. Both protocols produce the same `Emission` struct and feed into the same `emissions_tx: mpsc::Sender<Emission>` channel.


## Hydrapool changes
[hydrapool: sv2-support](https://github.com/average-gary/hydrapool/tree/sv2-support)
Hydrapool itself is minimal — just config and wiring:
- config.toml: [stratum_sv2] section (hostname, port, public/secret key)
- main.rs: ~90 lines to start the SV2 accept loop, connect it to the shared emissions_tx, and wire the template feed (Sv2NotifyBridge)
- Docker: Dockerfile.hydrapool updated, docker-compose.interop.yml for interop testing

## Testing
23 integration tests in p2poolv2_tests/src/stratum_sv2_test.rs:
- Interop testing against the SRI mining-device (https://github.com/stratum-mining/sv2-apps) (CPU miner simulator) via Docker Compose — 5-phase automated test: bitcoind regtest → hydrapool boots → mining-device connects + handshake + channel open → share submission → verification.
- Unit tests cover all modules (channels, difficulty, work/merkle, shares, setup).

## Metrics
Per your note — we closed the Prometheus/Grafana issues as "not planned." Happy to fold SV2 counters into the OpenTelemetry rewrite when that comes together.

I'll see about testing this implementation against hash on TN4 but perhaps you have a harness for testing this already? 

### average-gary on 2026-03-04

## SV2 Implementation Update — End-to-End Working on Testnet4

The SV2 Mining Protocol implementation is feature-complete and verified on testnet4 with real ASIC hardware.

### Live Test Results

**Bitaxe ASIC** → **SRI Translator Proxy** (SV1→SV2) → **Hydrapool** (SV2 pool) → **testnet4 Bitcoin node**

- 100+ shares accepted with zero rejections
- Stable through multiple GBT polling cycles and job updates
- Noise NX encrypted transport on port 3334
- SV1 continues working on port 3333

### Architecture

SV2 code lives in `p2poolv2_lib` behind an `sv2` cargo feature flag. Both SV1 and SV2 feed validated shares into the same `emissions_tx` channel — PPLNS, share chain, and block submission are protocol-agnostic.

Uses [`stratum-core`](https://crates.io/crates/stratum-core) (the consolidated SRI crate) rather than the legacy individual `*_sv2` crates, as discussed in #37.

### What's Implemented

- **Noise NX handshake** with SRI-compatible Base58Check authority keys (via `key-utils` crate)
- **Extended mining channels** (required for translator proxy compatibility)
- **Standard mining channels** with group channel management
- **Variable difficulty** with per-channel `SetTarget`
- **Job distribution** — GBT→SV2 template bridge with `NewMiningJob`, `NewExtendedMiningJob`, `SetNewPrevHash`
- **Share validation** — `SubmitSharesStandard` and `SubmitSharesExtended` with Emission bridge
- **23 integration tests** covering connection lifecycle, channel management, job distribution, share submission, and emissions pipeline
- **Interop test infrastructure** for automated testing against the SRI translator proxy

### Key Interop Discoveries

Getting the SRI translator proxy to work required matching the SRI pool's exact message semantics (not just spec compliance):

1. **Future job pattern** — SRI translator expects all jobs sent as "future" (`min_ntime = None`), then activated by `SetNewPrevHash`. Jobs with `min_ntime = Some(...)` go into `active_job` storage, but `SetNewPrevHash` only looks in `future_jobs`.
2. **Message ordering** — All `NewMiningJob`/`NewExtendedMiningJob` messages must be sent before any `SetNewPrevHash` in the same batch, even across channel types.
3. **Channel-type awareness** — Connections with only extended channels must not receive standard channel messages (`channel_id=0` broadcast `SetNewPrevHash` confuses the translator).

### Repos

- **p2pool-v2**: [`average-gary/p2pool-v2@sv2-support`](https://github.com/average-gary/p2pool-v2/tree/sv2-support) — 20+ commits, all SV2 modules + tests
- **hydrapool**: [`average-gary/hydrapool@sv2-support`](https://github.com/average-gary/hydrapool/tree/sv2-support) — feature enablement, config, Docker, testnet4 deployment configs

### Project Board

All 23 implementation issues are Done: [Project Board](https://github.com/users/average-gary/projects/1)

Open to feedback. PRs will be forthcoming after cleanup.

### average-gary on 2026-03-04

## How to Validate

You can reproduce this end-to-end on testnet4. The setup requires three components: a Bitcoin node, hydrapool, and the SRI translator proxy.

### Prerequisites

- **testnet4 Bitcoin node** with RPC and ZMQ enabled:
  ```
  bitcoin-node -testnet4 \
    -rpcuser=<your_rpc_user> \
    -rpcpassword=<your_rpc_password> \
    -rpcport=48335 \
    -zmqpubhashblock=tcp://127.0.0.1:28334
  ```
- **Rust toolchain** (stable)
- **An SV1 miner** — a Bitaxe, CPU miner, or the SRI [`mining-device`](https://github.com/stratum-mining/sv2-apps/tree/main/miner-apps/mining-device)

### 1. Build hydrapool

```bash
git clone https://github.com/average-gary/hydrapool.git
cd hydrapool
git checkout sv2-support
cargo build --release
```

### 2. Configure hydrapool

Edit `config-testnet4.toml` — update these fields for your environment:

```toml
rpc_user = "<your_rpc_user>"
rpc_password = "<your_rpc_password>"
coinbase_address = "<your_testnet4_address>"
```

The authority keys are the SRI defaults and work out of the box for testing.

### 3. Build the SRI translator proxy

The translator bridges SV1 miners to the SV2 pool. Use the `fix/extension-negotiation-race` branch ([PR #276](https://github.com/stratum-mining/sv2-apps/pull/276)) which includes a fix for long username truncation:

```bash
git clone https://github.com/stratum-mining/sv2-apps.git
cd sv2-apps
git checkout fix/extension-negotiation-race
cd miner-apps
cargo build --release -p translator_sv2
```

> **Note:** Once PR #276 is merged, building from `main` will work.

### 4. Configure the translator

Edit `translator-testnet4.toml` (included in the hydrapool repo) — update `user_identity` with your testnet4 payout address:

```toml
user_identity = "<your_testnet4_address>"
```

The `authority_pubkey` must match the key in `config-testnet4.toml` (the SRI defaults are already set in both files).

### 5. Run the stack

Start in this order:

```bash
# 1. Bitcoin node (must be synced to testnet4)

# 2. Hydrapool
./target/release/hydrapool --config config-testnet4.toml

# 3. Translator proxy
/path/to/sv2-apps/miner-apps/target/release/translator_sv2 \
  -c /path/to/hydrapool/translator-testnet4.toml

# 4. Point your SV1 miner at <hydrapool_host>:34255
```

### 6. What success looks like

**Translator log:**
```
SubmitSharesExtended: valid share, forwarding it to upstream | channel_id: 2, sequence_number: 1 ☑️
SubmitSharesSuccess(channel_id=2, last_sequence_number=1, new_submits_accepted_count=1, new_shares_sum=1) ✅
```

Share counts should increment continuously with no errors.

**Hydrapool log:**
```
SV2 extended mining channel opened downstream_id=1 channel_id=1
```

**What to watch for:**
- No `JobIdNotFound` errors in the translator log
- Translator stays connected through GBT polling cycles (job updates every ~10 seconds)
- The translator should not crash or reconnect

### Repos

| Component | Branch | Link |
|-----------|--------|------|
| hydrapool | `sv2-support` | [average-gary/hydrapool](https://github.com/average-gary/hydrapool/tree/sv2-support) |
| p2pool-v2 | `sv2-support` | [average-gary/p2pool-v2](https://github.com/average-gary/p2pool-v2/tree/sv2-support) |
| sv2-apps (translator) | `fix/extension-negotiation-race` | [PR #276](https://github.com/stratum-mining/sv2-apps/pull/276) |
