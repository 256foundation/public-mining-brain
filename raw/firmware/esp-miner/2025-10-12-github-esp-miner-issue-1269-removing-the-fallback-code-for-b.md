# bitaxeorg/ESP-Miner issue #1269: Removing the fallback code for best(Session)Diff

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1269
> Collected: 2026-10-07
> Published: 2025-10-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1269
- State: closed
- Author: duckaxe
- Opened: 2025-10-12
- Closed: 2026-06-02
- Labels: none

## Description

Related to https://github.com/bitaxeorg/ESP-Miner/pull/1202

The output of `bestDiff` and `bestSessionDiff` values includes a [check](https://github.com/duckaxe/ESP-Miner-Bitaxe/blob/078ea5e7bb8502aa55b20f93b4cdfc032fd9b5fe/main/http_server/axe-os/src/app/components/swarm/swarm.component.ts#L345) to see if the value is a string, in order to convert it into a number. This legacy code can be removed once NerdAxe provides a numerical value for `best(Session)Diff`.



## Comments

### mutatrum on 2025-10-13

> This legacy code can be removed once NerdAxe provides a numerical value for `best(Session)Diff`

... and sufficient time has elapsed for people to upgrade.

It could be cleaned up with #1265 and by integrating it into the `fallbackDeviceModel` (which should be renamed then), so all backwards compatibility code is in a single function.

### mutatrum on 2026-06-02

Fixed as part of #1524
