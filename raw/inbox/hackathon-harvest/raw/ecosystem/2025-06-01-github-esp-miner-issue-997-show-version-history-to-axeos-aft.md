# bitaxeorg/ESP-Miner issue #997: Show version history to AxeOS after an upgrade

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/997
> Collected: 2026-10-07
> Published: 2025-06-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 997
- State: closed
- Author: mutatrum
- Opened: 2025-06-01
- Closed: 2025-06-27
- Labels: none

## Description

Have a new page in AxeOS, 'Version History' which pops up after a firmware upgrade.

To achieve this, we should start writing the current version to NVS. On opening AxeOS, we can then see if we are now running a new version and navigate to this 'Version History' page. With a callback button back to the backend we can then write the new version to NVS, so we show this only once.

## Comments

### skot on 2025-06-02

What is the benefit of having this version history?

### mutatrum on 2025-06-02

People look at AxeOS more than they look at GitHub. If we add breaking changes and new features to the Version history there, people do not need to read about then on GitHub.

### skot on 2025-06-02

What about just a link to the github release page with the release notes? This could probably be auto generated.

Somewhat related, I think a AxeOS version number to make it very clear that someone forgot to update www.bin (or it failed and they didn't notice) would be great.

### mutatrum on 2025-06-02

Unified binary would solve that issue. Not sure if that's possible without overhauling the partition table though.

### skot on 2025-06-02

A couple have looked into a unified binary, and it's non-trivial.. mostly because the partitions are not contiguous.

### WantClue on 2025-06-27

fixed by #1006
