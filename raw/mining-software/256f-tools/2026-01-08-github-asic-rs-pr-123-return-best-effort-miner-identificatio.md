# 256foundation/asic-rs pull request #123: Return best-effort miner identification on timeout (don’t drop Stock matches)

> Source: https://github.com/256foundation/asic-rs/pull/123
> Collected: 2026-10-07
> Published: 2026-01-08

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 123
- State: closed
- Author: glitchpixelz
- Opened: 2026-01-08
- Closed: 2026-01-08
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

## Comments

### b-rowan on 2026-01-08

I think this needs to be rebased or something?

### glitchpixelz on 2026-01-08

Not a rebase, the identification logic tried to wait for a better match, a non stock firmware, and could hit the overall identification timeout before all probes finished. When the timeout fired, the function returned None instead of stock. I noticed this thankfully of a bitaxe that I had scanned.

### b-rowan on 2026-01-08

> Not a rebase, the identification logic tried to wait for a better match, a non stock firmware, and could hit the overall identification timeout before all probes finished. When the timeout fired, the function returned None instead of stock. I noticed this thankfully of a bitaxe that I had scanned.

I get that but the commit history compared to the master branch is messed up it seems like, since some of these are already on master?

### glitchpixelz on 2026-01-08

Yes that is correct. I committed this to the same branch that was previously merged.

### b-rowan on 2026-01-08

> Yes that is correct. I committed this to the same branch that was previously merged.

Can you update your master, make a new branch from it, and cherry pick the needed commits?
