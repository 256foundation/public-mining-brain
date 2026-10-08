# 256foundation/asic-rs pull request #364: feat: add Go bindings as a supported language

> Source: https://github.com/256foundation/asic-rs/pull/364
> Collected: 2026-10-07
> Published: 2026-09-11

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 364
- State: closed
- Author: adamdecaf
- Opened: 2026-09-11
- Closed: 2026-09-15
- Labels: none

## Description

This ports [adamdecaf/asic-rs-go](https://github.com/adamdecaf/asic-rs-go) into asic-rs as an in-tree supported language, following the discussion on #351.

This PR was **AI generated** (Grok).

## What

- New workspace crate `asic-rs-ffi`: C ABI over the current asic-rs API. Complex values cross as JSON. Async work runs on an internal Tokio runtime.
- Go module `github.com/256foundation/asic-rs/go/asic_go`: factory discovery, miner telemetry/control/config, `ErrNotFound` for `Ok(None)`.
- Tests that do not need hardware (factory host lists, JSON models including `TuningTarget::Manual` / `best_share` / `operating_state`, closed handles, TEST-NET-1 `GetMiner` → `ErrNotFound`).
- CI `Go Test` job (`make -C go ffi`, `cargo test -p asic-rs-ffi`, `go test`).
- Docs: Go column/tabs in the API map, getting started, and README.

## API sketch

```go
factory := asic_go.NewFactory()
defer factory.Close()

miner, err := factory.GetMiner("192.168.1.10")
if errors.Is(err, asic_go.ErrNotFound) {
    return
}
defer miner.Close()

data, err := miner.GetData()
```

Build the native library with `make -C go ffi` (`CGO_ENABLED=1`). See `go/README.md`.

Streaming scans, `MinerListener`, and `prepare_firmware` are not wrapped yet.

## Comments

### adamdecaf on 2026-09-11

Consumer proof: [adamdecaf/hasherdash#4](https://github.com/adamdecaf/hasherdash/pull/4) switches hasherdash off `adamdecaf/asic-rs-go` onto this in-tree Go module (`github.com/256foundation/asic-rs/go/asicrs`). Until this PR merges, that hasherdash branch `replace`s to `adamdecaf/asic-rs@feat/go-bindings`.

### b-rowan on 2026-09-14

@codex review

### chatgpt-codex-connector[bot] on 2026-09-14

<!-- codex-pull-request-review-summary -->

## Codex Review Summary

This comment shows the latest Codex review activity on this pull request.

| Review | Status | Commit | Review trigger |
| --- | --- | --- | --- |
| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-09-14T16:17:37.617147Z">2026-09-14T16:17:37.617147Z</relative-time> | `e92e968` | Manual request |



<details> <summary>ℹ️ About Codex in GitHub</summary>
<br/>

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
- Open a pull request for review
- Mark a draft as ready
- Comment "@codex review" or "@codex security review".

Codex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.

</details>

### b-rowan on 2026-09-14

Seems fine to me, I don't know golang conventions but it seems pretty reasonable.  Any chance we can rename to `asic_go` or something similar?  Or at least `asic_rs`?

### adamdecaf on 2026-09-14

Renamed the Go package to `asic_go` (`github.com/256foundation/asic-rs/go/asic_go`). Also addressed the Codex notes: JSON getters now decode before returning, and `WithConcurrentLimit` clamps non-positive values so they cannot panic the scan runtime.

The hasherdash consumer at adamdecaf/hasherdash#4 will need its import/`replace` updated to the new path.

### b-rowan on 2026-09-15

Pushed a couple fixes I did up locally with codex, take a look and make sure everything is still good.  Few bugs, renamed a few things for consistency across the different bindings, etc.

### adamdecaf on 2026-09-15

Looks good!
