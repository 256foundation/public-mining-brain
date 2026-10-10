# bitaxeorg/bitaxe-raw pull request #17: build: pin esp toolchain to 1.93.0.0 to avoid LLVM 21 miscompile

> Source: https://github.com/bitaxeorg/bitaxe-raw/pull/17
> Collected: 2026-10-07
> Published: 2026-07-02

- Repository: bitaxeorg/bitaxe-raw
- Type: pull request
- Number: 17
- State: closed
- Author: rkuester
- Opened: 2026-07-02
- Closed: 2026-09-26
- Labels: none

## Description

esp toolchains 1.94.x and 1.95.x ship LLVM 21, which fails to compile
release builds for the Xtensa target. `cargo build --release` aborts with
`rustc-LLVM ERROR: Cannot select ... XtensaISD::PCREL_WRAPPER`. Version
1.93.0.0, the last release on LLVM 20, builds correctly. See #16 for the
full writeup and upstream references (esp-rs/rust#277, candidate fix
espressif/llvm-project@39a5993).

Two commits, to be reverted once a fixed LLVM 21 toolchain is confirmed:

- `docs(readme)`: pin the espup install step to 1.93.0.0 and note the
  reason.
- `build`: check the bundled LLVM version in the build script and stop the
  build with install instructions when it is 21 or newer, catching an
  accidental toolchain update.


## Comments

### joebnb on 2026-09-16

will  this be able to merge？im also facing this

### rkuester on 2026-09-26

Hi @joebnb, I've moved Bitaxe Gamma firmware to https://github.com/256foundation/rhapd-bitaxe-gamma, and it builds without this fix. The mujina.org how-to shows the steps: https://mujina.org/howto/set-up-a-bitaxe-gamma

Related changes: #19 retires this branch, and https://github.com/256foundation/mujina/pull/112 updates Mujina's docs. Closing this one.
