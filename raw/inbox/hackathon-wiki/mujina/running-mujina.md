# Running Mujina

> Sources: Mujina project (mujina.org first-run tutorial, current as of July 2026), collected 2026-10-07; Mujina project (mujina.org connect to a pool), collected 2026-10-07; Mujina project (mujina.org home page), collected 2026-10-07; 256 Foundation (mujina GitHub README), collected 2026-10-07; 256 Foundation forum (WSL issues prevents bitaxe-raw talking to Mijuna), 2026-07-01; 256 Foundation forum (Mujina Dev Call #2), 2026-05-05
> Raw: [mujina.org first run](../../raw/mujina/mujina-org-tutorial-first-run.md); [mujina.org connect to a pool](../../raw/mujina/mujina-org-howto-connect-to-a-pool.md); [mujina.org home](../../raw/mujina/mujina-org-home.md); [mujina README](../../raw/mujina/github-256foundation-mujina.md); [WSL issue thread](../../raw/mujina/2026-07-01-forum-wsl-issues-prevents-bitaxe-raw-talking-to-mijuna.md); [Dev Call 2](../../raw/mujina/2026-05-05-forum-mujina-dev-call-2.md)
> Updated: 2026-10-07

## Overview

Today [Mujina](mujina-firmware.md) is a daemon you build from source and run yourself. It is written in Rust and configured through environment variables. A CPU backend lets the whole miner run with no mining hardware and no pool account, and the mujina.org tutorial says this takes about fifteen minutes, most of it compile time. This article covers building, the first run on a CPU, connecting to a Stratum v1 pool, logging, the REST API, and what the sources say about operating systems.

## What you need

- The current stable Rust toolchain, installed with rustup.
- On Debian or Ubuntu, two build packages: `libudev-dev` and `libssl-dev`. Other Linux distributions need their equivalents.
- On macOS, the README says to install Xcode Command Line Tools. A build failure on `openssl-sys` usually means the build cannot find openssl.

## Code layout

The repository is a cargo workspace named mujina-miner. It holds several binaries, including `mujina-minerd` (the daemon) and `mujina-cli`. Build and test with `cargo build` and `cargo test`. Running needs a binary picked by name:

```
cargo run --bin mujina-minerd
```

The optional `just` tool gives shorter aliases: `just run`, `just test`, and `just checks` (fmt, lint and test in one step).

The README points to deeper documents inside the repository: an architecture overview, the REST API, CPU mining, the container image, a BM13xx chip reference, the Bitaxe-Raw control protocol, and a Bitaxe Gamma board guide. Those documents are not in `raw/`.

## First run on a CPU

Start the daemon with the CPU backend on and USB discovery off:

```
MUJINA_CPUMINER_THREADS=2 \
MUJINA_USB_DISABLE=1 \
  cargo run --release --bin mujina-minerd
```

What happens, per the tutorial:

- `MUJINA_CPUMINER_THREADS` enables the CPU backend with that many hashing threads. `MUJINA_USB_DISABLE` skips the search for USB hardware.
- With no pool set, the miner starts its built-in dummy job source, which generates synthetic work.
- A virtual "CPU Miner" board connects, the same way an ASIC board would.
- The REST API comes up.
- About every half minute the scheduler prints a status line with uptime, hashrate and share count.

A CPU does a few megahashes a second, where an ASIC does terahashes, so this is not profitable. The tutorial stresses that it is not a simulation. Every part of Mujina that would drive real hardware is running.

The README's quick start uses the same idea with one thread and also sets `MUJINA_CPUMINER_DUTY=50`. It says the run exercises job distribution, hashing, share detection, logging and the API.

Press Ctrl+C to stop. The daemon shuts down cleanly and prints a final status line.

## Connecting to a pool

Three variables point the miner at a Stratum v1 pool:

| Variable | Meaning | Default |
|----------|---------|---------|
| `MUJINA_POOL_URL` | The Stratum v1 job source | none; the dummy source is used |
| `MUJINA_POOL_USER` | Worker name, typically a payout address with a worker suffix | `mujina-testing`, a shared testing name |
| `MUJINA_POOL_PASS` | Worker password; most pools ignore it | `x` |

Only `MUJINA_POOL_URL` is strictly required. The miner negotiates version rolling with the pool automatically. A USB board needs nothing more. A CPU-only run adds the two CPU variables above.

To verify, watch the periodic status line. A rising `shares` count means the pool is accepting work. Then check the pool's dashboard for the worker.

### Testing submission at CPU speed

Pools set share difficulty for ASIC-speed miners, so a CPU would wait days for one share. `MUJINA_POOL_FORCED_RATE` forces a target in shares per minute. A value of `6` targets one share every ten seconds. The miner lowers its local share threshold to hit the rate, but the pool still applies real difficulty and is expected to reject these shares as below difficulty. The point is to test connectivity and the submission flow, not to earn rewards.

## Logging

By default Mujina logs its own entries at info level and third-party crates at warn.

- `MUJINA_LOG` filters Mujina's own modules. A bare level such as `trace` applies to all of Mujina. A named module, such as `stratum_v1=trace`, changes only that module.
- `RUST_LOG` keeps its usual Rust meaning. `MUJINA_LOG` wins where the two overlap.
- Debug shows logical stages: chip initialization, jobs received, shares submitted. Trace adds serial frames, I2C transactions and USB device events.

With debug logging, each `Share found` pair in the log is a hash thread finding a candidate nonce and the scheduler checking it against the job's share threshold.

## REST API

The daemon logs its API address at startup. The default is `127.0.0.1:7785`. Set `MUJINA_API_LISTEN` to change the address or port.

- `/api/v0/health` returns `OK`.
- `/api/v0/miner` is the full state snapshot, with subtrees at `/api/v0/boards` and `/api/v0/sources`.
- A Swagger UI is served at `/swagger-ui` from the daemon's own OpenAPI spec.

The README says the `/api/v0/` prefix signals the API is still in flux, and that authentication is on the roadmap. Persistent configuration through the REST API and CLI is planned to follow as those interfaces mature.

## Operating system support

The sources do not agree on where Mujina runs.

> **Status: Disputed**
> The mujina.org tutorial (current as of July 2026) says "Mujina runs only on Linux." The mujina GitHub README says "macOS is supported", and the Dev Call #2 summary says USB hot-plug discovery "works on Linux and macOS today" with a Windows port wanted. In a forum thread, ixtech.xyz reported running Mujina with CPU mining on a Windows machine, and on 2026-07-05 said a Bitaxe was working natively on Windows and opened pull request #76, "feat: native Windows support for Bitaxe mining". The sources do not say whether that pull request was merged.

### The WSL2 report

On 2026-07-01 ixtech.xyz reported a dead end running Mujina against a Bitaxe Gamma through WSL2 and usbipd:

- Mujina built in WSL without trouble. CPU mining and the dashboard worked.
- With bitaxe-raw flashed, Mujina discovered the device, but every control-frame write hung.
- They traced it to the control CDC ACM endpoint on the ESP32-S3 not being drained. They could push 4 KB into the ASIC UART port in 340 ms, but the same write to the control port timed out at 2 s.
- They concluded the block was inside bitaxe-raw, not Mujina, and filed bitaxe-raw issue #14. They were not sure whether it was a firmware bug or a usbipd interaction, and had not tested native Linux.
- Unknown_aadhi pointed to Mujina PR #75, which has Windows driver code. ixtech.xyz said it helped, and that more code changes and USB fixes were still needed.

Note that bitaxe-raw is now deprecated in favour of rhapd-bitaxe-gamma. See [Mujina Hardware Compatibility](hardware-compatibility.md).

## Where this is heading

The home page says the goal is Mujina OS: complete operating system images installed onto a miner's control board. The tutorial's next steps are setting up a Bitaxe Gamma, connecting to a real pool, and running in a container. Those how-to pages, and the environment variable reference, are not in `raw/`.

## See Also

- [Mujina Firmware](mujina-firmware.md)
- [Mujina Hardware Compatibility](hardware-compatibility.md)
- [Contributing and Mujina Improvement Proposals](contributing-and-mips.md)
- [Mujina Dev Calls](mujina-dev-calls.md)
- [Hydrapool](../hydrapool/hydrapool.md)
