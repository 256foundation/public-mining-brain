# bitaxeorg/bitaxe-raw issue #3: Flashing via the instructions in README.md fails in boot mode

> Source: https://github.com/bitaxeorg/bitaxe-raw/issues/3
> Collected: 2026-10-07
> Published: 2025-04-19

- Repository: bitaxeorg/bitaxe-raw
- Type: issue
- Number: 3
- State: open
- Author: rkuester
- Opened: 2025-04-19
- Closed: n/a
- Labels: bug

## Description

When reflashing bitaxe-raw, after powering up in boot mode by holding the `BOOT` button while connecting power, attempts to flash via the commands in the README consistently fail with the error:
```
leda » cargo flash --release --chip esp32s3
    Finished release profile [optimized] target(s) in 0.19s
    Flashing /home/rkuester/mujina/bitaxe-raw/target/xtensa-esp32s3-none-elf/release/bitaxe-raw
thread 'main' panicked at /home/rkuester/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/probe-rs-0.27.0/src/f
lashing/loader.rs:414:53:
called Result::unwrap() on an Err value: CoreDisabled(1)
```

The command in the README *does* work if the Bitaxe is running esp-miner. In fact, my current workaround is to reflash esp-miner according to its README and then reflash bitaxe-raw.

## Comments

### skot on 2025-04-21

@korbin we talked a little bit about this.. But I was surprised that `cargo flash` doesn't work with the Bitaxe ESP32 in the bootloader already?

### korbin on 2025-04-22

I am unable to reproduce this issue on a Bitaxe/ESP32S3 Devkit. `cargo flash` uses `probe-rs` - which isn't perfect for Espressif devices but seems to work.

When booting with the BOOT button held, the device enumerates as: `Espressif USB JTAG/serial debug unit` - `probe-rs`, `cargo-flash`, and `espflash` work from this state.

Try `espflash` if you are continuing to have issues:

```espflash target/xtensa-esp32s3-none-elf/release/bitaxe-raw```

### rkuester on 2025-04-22

Weird, it's annoyingly consistent here. I'll try a few more permutations of my environment and report back.

Thanks for trying to reproduce.

### rkuester on 2025-04-28

This issue persists despite the these permutations of my environment:

- A brand-new Bitaxe Gamma
- An entirely different development machine: a fresh toolchain on an Apple silicon MacBook Air (original was x86-64 with Debian testing)
- Supplying a pristine 5V from a quality bench supply

`espflash` is working reliably. I'll stick with that. 🤷‍♂
