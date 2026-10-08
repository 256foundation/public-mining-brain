# 256foundation/asic-rs pull request #124: fix: improve miner discovery

> Source: https://github.com/256foundation/asic-rs/pull/124
> Collected: 2026-10-07
> Published: 2026-01-08

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 124
- State: closed
- Author: glitchpixelz
- Opened: 2026-01-08
- Closed: 2026-01-09
- Labels: none

## Description

This change prevents miner discovery from returning None when the identification timeout triggers after a valid Stock match was already found (e.g., Bitaxe). We keep the first successful identification as a fallback and, if time runs out, return that best effort result rather than discarding it. Non stock firmware results still take priority and can override Stock when detected. Remaining discovery tasks are aborted once a final decision is made.

Before

- Stock devices could be correctly identified early but still not returned if other probes didn’t complete before the timeout.
- Bitaxe could disappear from scans despite successful AxeOS web detection.

After

- If any valid identification was found before timeout, the best known result is returned.
- Bitaxe is consistently discovered again.
- Non stock firmware remains preferred when detected.
