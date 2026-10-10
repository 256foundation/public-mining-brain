# 256foundation/asic-rs issue #309: Elphapex DG1 and DG1+ models are not discovered during network scan

> Source: https://github.com/256foundation/asic-rs/issues/309
> Collected: 2026-10-07
> Published: 2026-07-09

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 309
- State: closed
- Author: Kraitcer
- Opened: 2026-07-09
- Closed: 2026-07-27
- Labels: none

## Description

Hi there 👋

I was testing asic-rs (running it through a Python wrapper) and ran into a small problem while scanning the network.

When I use MinerFactory to scan my network, the library doesn't seem to pick up my Elphapex DG1 and DG1+ miners. They're definitely online and reachable, but the scan just skips right over them.

To double-check, I ran the same scan using an older Python-based pyasic library, and it found both devices without any issues. So it looks like the problem is specific to how asic-rs is trying to discover them.

If it helps, I can share raw scan output (logs, packet captures, or whatever you need) – just let me know what format would be most useful.

Thanks!

## Comments

### b-rowan on 2026-07-09

They're not supported (yet), but I can work on adding them.

Supported models list is here - https://256foundation.github.io/asic-rs/supported-devices/#support-matrix

### Kraitcer on 2026-07-09

Could you please give an approximate estimate for when this feature might be available? I understand if it’s hard to predict, just trying to plan ahead. Thank you for your work!

### b-rowan on 2026-07-09

> Could you please give an approximate estimate for when this feature might be available? I understand if it’s hard to predict, just trying to plan ahead. Thank you for your work!

Shouldn't take too long, should hopefully have a PR up today that can be tested/reviewed.

### b-rowan on 2026-07-09

PR up, you should be able to install from my branch (`pip install git+https://github.com/b-rowan/asic-rs.git@elphapex-support`), but you may need a local rust toolchain to build it from source.
