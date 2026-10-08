# bitaxeorg/bitaxe-raw issue #16: build: release build fails on esp toolchains 1.94.0.0+ (LLVM 21 "Cannot select" regression)

> Source: https://github.com/bitaxeorg/bitaxe-raw/issues/16
> Collected: 2026-10-07
> Published: 2026-07-02

- Repository: bitaxeorg/bitaxe-raw
- Type: issue
- Number: 16
- State: open
- Author: rkuester
- Opened: 2026-07-02
- Closed: n/a
- Labels: none

## Description

## Summary

`cargo build --release` fails during LLVM instruction selection on the
current esp Rust toolchains (1.94.0.0 through 1.95.0.0). The build aborts
before linking with:

```
rustc-LLVM ERROR: Cannot select: ... i32 = XtensaISD::PCREL_WRAPPER
  TargetConstantPool:i32<@anon... = private unnamed_addr constant
  [14 x i8] c"ADC Read Error", align 1> 0
In function: ..._usb_task_task0...poll
```

The Xtensa backend can't lower a PC-relative reference to an aggregate
constant in the constant pool. Here that's the `"ADC Read Error"` string
literal in `src/control/adc.rs`, pulled into the USB task by inlining.

## Details

- Only optimized codegen is affected. `cargo check` and `cargo clippy`
  pass; debug builds (opt-level 0) get through codegen and only fail at
  link for unrelated reasons.
- Independent of the release profile knobs: reproduces with `lto` set to
  fat, thin, or off, and at opt-level 2, 3, and s.
- Target: `xtensa-esp32s3-none-elf` (our no_std firmware).

## Toolchain bisect

| esp toolchain | bundled LLVM | result |
| --- | --- | --- |
| 1.93.0.0 | 20.1.1 | builds |
| 1.94.0.2 | 21.1.3 | fails |
| 1.95.0.0 | 21.1.3 | fails |

The regression tracks the esp-rs fork's LLVM 20 to 21 bump.

## Known upstream regression

- esp-rs/rust#277 reports the same `Cannot select XtensaISD::PCREL_WRAPPER`
  failure, also a regression in 1.94.0.0+, from the LLVM 20 to 21 bump.
  That reporter hit it on the std target with a `[2 x float]` constant and
  said it did not reproduce on no_std for them. This case shows it does
  affect no_std too, via a string (`[14 x i8]`) constant.
- A candidate fix is committed to the LLVM fork:
  espressif/llvm-project@39a59933237b749f9c5b5f3adf02384e8dfec78e,
  "[Xtensa] Fix ConstantPool lowering for aggregate constants"
  (2026-05-13). Not confirmed in a released toolchain yet.
- Two more open "Cannot select" reports against the same LLVM 21 backend:
  esp-rs/rust#275, esp-rs/rust#281.

## Workaround

Pin the esp toolchain to the last good version:

```
espup install --toolchain-version 1.93.0.0
```


## Comments

### rkuester on 2026-07-02

Anyone else hitting this on esp 1.94.x or 1.95.x?

#17 pins the toolchain to 1.93.0.0 as a temporary fix: the README install step now requests that version, and a build.rs check stops the build with install instructions if it sees LLVM 21 or newer. Happy to drop it once a fixed toolchain is released.

### winterrdog on 2026-07-05

> Anyone else hitting this on esp 1.94.x or 1.95.x?

yes, i did. i was running esp `1.95.0.0`

> Pin the esp toolchain to the last good version:
> 
> ```
> espup install --toolchain-version 1.93.0.0
> ```

this worked great
