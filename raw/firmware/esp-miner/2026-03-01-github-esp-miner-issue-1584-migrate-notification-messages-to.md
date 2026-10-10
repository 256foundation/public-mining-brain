# bitaxeorg/ESP-Miner issue #1584: Migrate notification messages to backend

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1584
> Collected: 2026-10-07
> Published: 2026-03-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1584
- State: open
- Author: mutatrum
- Opened: 2026-03-01
- Closed: n/a
- Labels: none

## Description

Currently the logic for dashboard notifications is done in the front-end. The system would be cleaner if this logic is done in the backend, and the messages are just exposed as a list with type, text, severity, dismissible, timestamp.

F.e. this would allow way easier exposing of #1565 to the front-end, and support a general version of #1465.
