# 256foundation/mujina pull request #55: Make non-glibc Linux cross-compilation work

> Source: https://github.com/256foundation/mujina/pull/55
> Collected: 2026-10-07
> Published: 2026-05-04

- Repository: 256foundation/mujina
- Type: pull request
- Number: 55
- State: open
- Author: Schnitzel
- Opened: 2026-05-04
- Closed: n/a
- Labels: none

## Description

## Summary

Three small changes that let `mujina-miner` cross-compile for `aarch64-unknown-linux-musl` (and other non-glibc Linux targets), so it can be deployed onto mining hardware that ships with musl userspace — concretely, the Amlogic A113D control board found on Antminer S19 series miners.

- **Switch `reqwest` to `rustls-tls`.** The default features pull in `native-tls`, which transitively requires `openssl-sys`. Cross-building `openssl-sys` to musl is painful (sysroot, pkg-config wrapper, vendored OpenSSL or a sysroot install) and unnecessary when reqwest can use rustls directly.
- **Gate `udev` and `tracing-journald` to `target_env = "gnu"`.** Both link against glibc-only system libraries (`libudev`, `libsystemd`) that have no good musl story. The existing fallback `mod platform` in `src/transport/usb.rs` already covers the no-udev case as a stub for unsupported platforms (Windows, etc.), so musl Linux now falls into that same path — fine for the CPU backend and any non-USB hashboard.
- **Same `cfg` change in `src/tracing.rs`** so the journald init mod follows the same gate as its dependency.

Net diff: 4 files, +7 / -7 lines.

## Test plan

- [x] `cargo build --release` on macOS (aarch64-apple-darwin) — unchanged, still builds.
- [x] `cargo build --release --target aarch64-unknown-linux-musl --bin mujina-minerd` from macOS — now succeeds (previously failed at `openssl-sys` and `udev`).
- [x] Resulting 17 MB statically-linked aarch64 ELF transferred to an Antminer S19j Pro control board (LuxOS base, kernel aarch64 / userspace armhf — the static aarch64 binary runs fine via the 64-bit kernel).
- [x] `MUJINA_CPUMINER_THREADS=1 MUJINA_CPUMINER_DUTY=50 MUJINA_USB_DISABLE=1 MUJINA_API_LISTEN=0.0.0.0:7785 ./mujina-minerd` — comes up cleanly, CPU board attached, dummy job source, REST API responds at `/swagger-ui`, mining-status log line ticks at 30s.

## Build steps on macOS

```sh
rustup target add aarch64-unknown-linux-musl
brew install messense/macos-cross-toolchains/aarch64-unknown-linux-musl

CARGO_TARGET_AARCH64_UNKNOWN_LINUX_MUSL_LINKER=aarch64-unknown-linux-musl-gcc \
CC_aarch64_unknown_linux_musl=aarch64-unknown-linux-musl-gcc \
  cargo build --release --target aarch64-unknown-linux-musl --bin mujina-minerd
```

## Notes / open questions

- The `reqwest` rustls swap is mildly opinionated. If you'd prefer to keep `native-tls` as the default and offer rustls behind a feature flag instead, happy to refactor — but it'd add complexity for the cross-build path with no obvious upstream benefit.
- This is the minimal change to make the build *work*. Real S19 hashboard support (driving BM1362 chips over UART, APW12 PSU over I²C, fans, EEPROM decode, PIC sensor reads) is separate work — see [skot/amlogic-cb-tools](https://github.com/skot/amlogic-cb-tools) for the standalone hardware-validation binaries that prove out the control-board interfaces before they land in mujina.

## Comments

### rkuester on 2026-07-06

My reading of this PR is that it brings up several good issues, but doesn't completely solve any of them. What the diff actually accomplishes is making Mujina compile as a static binary. That's useful on its own, but each change raises a bigger question about Mujina's portability, and we should answer those questions deliberately. Here's my attempt at listing them:

1. The real portability question is how Mujina deploys on a board like this.

   The S19 control board runs an aarch64 kernel over an armhf userspace. There are roughly three ways to land Mujina on it: supply the whole operating system ourselves, compile against the board's existing userspace including its C library, or ship a static binary that ignores the userspace entirely. The first two seem like the first-class options, but neither is cheap here, because source for what's on the board isn't readily at hand. The kernel for this chip at this version could probably be tracked down, config and all, but that's an expedition. Compiling against the board's own libraries needs more than the .so files sitting on the box: matching headers, a sysroot built from them, and a Rust cross toolchain pointed at that sysroot, which I suspect is less well-trodden than doing the same for a C program. The static route is the fallback we reach for because it's easiest from a toolchain perspective. It's also why this PR has to touch the three dynamic C library dependencies it does: openssl (via reqwest's native-tls), libudev, and libsystemd. Whichever answer we settle on shapes everything downstream, so it's worth recording somewhere more permanent than this thread.

2. Capability selection belongs in build features, not as a byproduct of the libc.

   Whether udev or journald is available varies on its own axis, orthogonal to which C library the target uses. A glibc distro without systemd, Alpine with eudev, and this static build wanting neither are all real configurations. Gating on `target_env = "gnu"` makes those capabilities switch on and off as a byproduct of the libc choice, and the libc doesn't actually predict them. `cfg(target_os)` still has a job: it answers whether the capability can exist on the target at all. There is no udev on macOS and no journald on Windows, so those gates are correct and permanent. The mechanics work out: udev and journald become optional dependencies behind default-on features, and they can stay in their target tables, so the cfg says what's possible and the feature says what's wanted. A feature is more than an off switch, though. Turn udev off and the code that depends on it no longer compiles, which forces the real question: what does this build do instead? Maybe it enumerates serial devices by some other means, or maybe it skips discovery and takes boards from static configuration. Every feature carries that second decision about the alternative behavior.

3. The TLS swap is a good example of how a change made to compile statically can have wide consequences.

   Switching reqwest to rustls-tls changes more than how the binary links. Certificate validation moves from the system's CA store to bundled Mozilla roots, and dropping default features also loses reqwest's system-proxy support. That applies on every platform, including the glibc and macOS builds that work today. A CLI pointed at an https endpoint whose cert chains to a private CA would break silently. The OP offered the feature-flag version in the PR notes, and I think that's the right call after all: keep native-tls as the default and make rustls the static build's opt-in, the same way reqwest itself models it.

4. Features and platforms multiply the build matrix, and testing has to keep up.

   Once we have feature flags and more than one platform, the question becomes which combinations we actually build and test. Anything outside that set may quietly break, as this PR demonstrates: the emberone00 integration test module still gates on `target_os = "linux"` alone but calls udev. Those tests are ignored by default and only run when requested by hand, but `cargo test` still compiles them, so a plain `cargo test` on a musl host fails to build. CI builds a single glibc Debian configuration, so neither that breakage nor future regressions of the static build would show up. Features at least make the set of combinations something we choose and can count, so CI can build and test each one we claim to support instead of chasing an open-ended list of platforms. And a combination is more than a compile check; whatever alternative behavior it selects is what needs testing.

Concretely, I think the implementation that falls out is: udev, journald, and rustls become cargo features, with the first two default-on and rustls opt-in alongside a native-tls default. Defining each feature includes deciding what the build does with the feature off. No udev probably means boards come from static configuration instead of discovery; no journald already falls back to console logging. The cfg gates express only platform impossibility, like udev on macOS. The emberone00 integration tests, which find their board through udev, would compile only when the udev feature is on, so the tests follow the same switch as the code they exercise. CI builds and tests both with the default features and with them off. That keeps today's builds unchanged while making the static build a supported configuration instead of a byproduct of the libc.

Rather than grow this PR into all of that, I may close it and open one or more issues from the list above so the questions can be worked separately. The PR did its job by raising them.
