# 256foundation/asic-rs issue #370: feat: make RPC and HTTP management ports configurable per MinerFactory

> Source: https://github.com/256foundation/asic-rs/issues/370
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 370
- State: closed
- Author: nkatha23
- Opened: 2026-09-15
- Closed: 2026-09-16
- Labels: none

## Description

send_rpc_command hardcodes port 4028, send_web_command hardcodes port 80. This surfaces as a  problem in two places today.

Test suite port collisions. Any test that exercises the RPC discovery path needs to bind localhost:4028. Two such tests running in parallel hit Address already in use (os error 98). PR #368 worked around this with a static tokio::sync::Mutex<()> to serialize those tests. As more tests are added this serialization bottleneck grows. If tests could request an OS-assigned port via TcpListener::bind(:0), the collision disappears entirely and tests can run in parallel without coordination.

Multi-miner hosts and remapped ports. When multiple miner processes run on a single server (the pattern used in hydrapool/mujina test infrastructure), each process needs a distinct port. asic-rs currently cannot address any instance other than the one on the default 4028/80. The same limitation affects production deployments where operators remap management ports away from defaults to reduce scanner exposure, or put miners behind reverse proxies.

_Proposed change_
Add with_rpc_port(u16) and with_web_port(u16) builder methods to MinerFactory:
```
let factory = MinerFactory::new()
    .with_rpc_port(14028)
    .with_web_port(8080);

let miner = factory.get_miner(ip).await?;
```
The ports propagate through discovery probes and data-collection backends. This requires a breaking change to FirmwareEntry::build_miner (trait signature) and the two utility functions. 

## Comments

### b-rowan on 2026-09-15

Concept seems fine, good with the base idea, but the suggested change probably will not work.  Different miners may use different ports for each of these services, so a global setter would likely cause problems.  For example, whatsminers use 4028 for the V1/V2 API, and 4433 for the V3 API.  Not sure the best way to handle this, maybe there is a way to create a custom firmware type which implements `MinerFirmware`, which can then be passed in custom discovery ports and added to the firmware registry for the factory?

Food for thought, let me know if you have other ideas.

### b-rowan on 2026-09-15

Maybe we can actually add those functions into the `MinerFirmware` trait, like `use_rpc_port` and `use_web_port` to replace them (and also use them when constructing the APIs downstream)?

### nkatha23 on 2026-09-15

> Maybe we can actually add those functions into the `MinerFirmware` trait, like `use_rpc_port` and `use_web_port` to replace them (and also use them when constructing the APIs downstream)?

Agreed. 
Proposed: add `fn rpc_port(&self) -> u16 { 4028 }` and `fn web_port(&self) -> u16 { 80 }` to `FirmwareEntry` with those defaults. 
Each firmware overrides as needed,  WhatsMiner V3 returns 4433 from `rpc_port()`. During discovery, command dispatch uses each firmware's declared ports, and `build_miner` receives those same values for backend construction.

For the reverse-proxy / port-remapping case, users create a thin newtype wrapper around the stock firmware entry that overrides the port methods and register it in the factory alongside the default. No global setter needed

also asking : commands from all firmwares are currently collected into a `HashSet<MinerCommand>` and deduped before firing. If two firmware entries declare the same command on different ports, they'd collapse into one probe. Two options:

1. Fire commands per-firmware instead of globally deduped,  more probes, correct behavior for non-standard ports
2. Only apply custom ports during `build_miner`, keep discovery on standard ports, simpler imo, works when only the management API is remapped

### nkatha23 on 2026-09-15

BUT: After tracing the discovery path, the `rpc_port()`/`web_port()` methods on `FirmwareEntry` don't reach the discovery phase as-is.

`get_miner_inner` collects commands from all firmwares into a `HashSet<MinerCommand>` and fires each unique command once,  dedup happens on command content only. `MinerCommand` has no port field, so there's nowhere to pipe a per-firmware port into the probe.

Also noting: WhatsMiner's 4433 is a `build_miner` concern, not a discovery concern. Discovery uses `RPC_DEVDETAILS` and `HTTP_WEB_ROOT` on the standard ports,  the V3 API transition happens entirely inside `build_miner`. So a factory-level port setter wouldn't conflict with that.

The cleanest fix that makes everything self-consistent is adding `port: u16` to `MinerCommand` itself:

   ```
 RPC { command: &'static str, port: u16 }
    WebAPI { command: &'static str, port: u16 }
```

Then each firmware's `get_discovery_commands()` declares its port explicitly, deduplication becomes (command, port) pairs, and the probe fires on the right port. The `rpc_port()`/`web_port()` methods still make sense as helpers that firmware entries use when constructing their commands, just not as the primary mechanism.

This also aligns with your suggestion [1](https://github.com/256foundation/asic-rs/issues/370#issuecomment-5688086933),  a custom firmware type with custom commands naturally carries its ports in the command definitions. makes sense? 


### b-rowan on 2026-09-15

I think it will be best to define a new type `DiscoveryCommand` for doing initial discovery (rather than modifying `MinerCommand` which is used in multiple places), then implementing your suggestion.  Thought this through pretty thoroughly as far as I can tell and your suggestion is the only plausible way to go about it from what I can tell.
