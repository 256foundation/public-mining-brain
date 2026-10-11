# What is the Bitaxe? — A beginner's intro to open-source Bitcoin mining

> Source: https://osmu.xyz/t/what-is-the-bitaxe-a-beginners-intro-to-open-source-bitcoin-mining/27
> Collected: 2026-10-10
> Published: 2026-05-30
> Registry ID: osmu-forum

WantClue | 2026-05-30 08:14:27 UTC | #1

## What is the Bitaxe? :orange_square:

Welcome to OSMU! If you’ve landed here wondering *“what actually is a Bitaxe?”* — this thread is for you. Ask anything in the replies, no question is too basic.

### The short version

The **Bitaxe** is an **open-source, standalone Bitcoin miner**. It’s a small single-board device, about the size of your hand, that hashes the SHA256 algorithm just like the big industrial miners — only quieter, cooler, and built entirely in the open.

Every part of it is open: the schematics, the PCB, the firmware (AxeOS), the bill of materials. Anyone can build one, modify one, or improve the design. That’s the whole point.

### How it works under the hood

A Bitaxe has two main brains:

- :brain: **An ASIC chip** — a specialized Bitmain chip (BM1370 in the newest Gamma) designed to do one thing extremely well: SHA256 hashing.
- :satellite_antenna: **An ESP32-S3** — a tiny Wi-Fi-enabled microcontroller that runs **AxeOS**, manages the ASIC, talks to your mining pool, and serves the web UI.

You plug it in, connect it to Wi-Fi via its built-in web interface, point it at a pool (or solo mine via something like Public Pool), and it starts hashing.

### What about hashrate?

Hashrate depends on which model you have. The original Bitaxe sat in the **250–500 GH/s** range using around 15W, but newer generations have pushed performance significantly higher:

| Model | Chip | Approx. Hashrate |
|---|---|---|
| 100 / Max | BM1397 | ~400 GH/s |
| 200 / Ultra | BM1366 | ~500 GH/s |
| 400 / Supra | BM1368 | ~700 GH/s |
| 600 / Gamma | BM1370 | ~1.2 TH/s |
| 650 / Gamma Duo | 2× BM1370 | ~2.4 TH/s |
| 801 / Gamma Turbo | BM1370 (tuned) | higher still |

It’s a tiny fraction of what an Antminer S21 puts out — but that’s not really the point.

### So why run one?

A Bitaxe isn’t about out-hashing industrial farms. People run them for reasons like:

- :slot_machine: **Solo lottery mining** — extremely long odds, but if you hit a block solo, the full reward is yours.
- :shield: **Network decentralization** — every independent miner makes Bitcoin a little more resilient.
- :mechanic: **Learning & tinkering** — it’s a fantastic way to understand how mining actually works, end to end.
- :unlocked: **Supporting open-source hardware** — voting with your wallet for transparent, hackable kit.
- :house: **Heat reuse / fun factor** — quiet enough to sit on your desk, warm enough to take the chill off.

### Getting started

A few useful starting points:

- :open_book: [Bitaxe overview (OSMU Wiki)](https://osmu.wiki/bitaxe/about)
- :page_facing_up: [Quick setup PDF](https://osmu.wiki/doc-assets/bitaxe/Bitaxe-Instructions.pdf)
- :laptop: [Bitaxe GitHub](https://github.com/bitaxeorg/)
- :open_book: [AxeOS firmware](https://osmu.wiki/axeos/about)
- :speech_balloon: [OSMU Discord](https://discord.gg/osmu)

### Got questions?

Drop them below :backhand_index_pointing_down: — whether it’s “which model should I buy first?”, “how much electricity does it use?”, “can I actually win a block?”, or “what’s the difference between solo and pool mining?” — this is the place to ask.

Happy hashing! :pick:
