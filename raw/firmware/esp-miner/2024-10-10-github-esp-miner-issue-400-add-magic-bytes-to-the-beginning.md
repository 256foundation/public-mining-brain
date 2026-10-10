# bitaxeorg/ESP-Miner issue #400: Add magic bytes to the beginning of firmware images to properly identify them

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/400
> Collected: 2026-10-07
> Published: 2024-10-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 400
- State: closed
- Author: skot
- Opened: 2024-10-10
- Closed: 2026-07-25
- Labels: enhancement, help wanted

## Description

If we pick a couple magic bytes (I like emojis) to add to the beginning of esp-miner.bin and www.bin images then we can have AxeOS look for these bytes before loading a bad image.

## Comments

### cyphercosmo on 2025-01-18

Even though the current flow starts with the user clicking the button to check for recent updates, they still need to download the files and upload them right after.

We should then assume those files could've been tampered with by the time the user uploads them, so the options we have is either adapt the flow so those files never touch the potentially compromised space or to have a way to verify such a file is indeed what it claims to be.

When it comes to the verification process we could go a more centralized approach and simply check the calculated SHA of the file matches a known release on Github. The Bitcoin inspired approach could be for the build process to produce a digital signature and embed the public key so that once uploaded we can check the file against the hash, the signature, and the public key. The only challenge with that would be to transport the pk and the signature.

What are your thoughts @skot ? You seem to have something a lot simpler in mind.

### 0xf0xx0 on 2026-07-25

resolved by checksum in #1763
