# 256foundation/asic-rs pull request #382: feat(discovery): add DiscoveryCommand with explicit port field

> Source: https://github.com/256foundation/asic-rs/pull/382
> Collected: 2026-10-07
> Published: 2026-09-16

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 382
- State: closed
- Author: nkatha23
- Opened: 2026-09-16
- Closed: 2026-09-16
- Labels: none

## Description

Fixes https://github.com/256foundation/asic-rs/issues/370

Replaces `Vec<MinerCommand>` in `get_discovery_commands()` with`Vec<DiscoveryCommand>`, a new type that carries an explicit `port: u16` alongside each command. Discovery probes now fire on the port declared by each firmware entry rather than hardcoded constants in `util.rs`.
Existing `send_rpc_command` / `send_web_command` signatures are unchanged and  backend data-collection call sites as well.
