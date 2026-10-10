# 256foundation/asic-rs issue #318: Antminer: identified S19 Pro is dropped when miner_type.cgi returns 404

> Source: https://github.com/256foundation/asic-rs/issues/318
> Collected: 2026-10-07
> Published: 2026-07-29

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 318
- State: closed
- Author: DanNicolau
- Opened: 2026-07-29
- Closed: 2026-08-10
- Labels: none

## Description

## Summary

`MinerFactory::scan_stream_with_ip()` drops some stock Antminer S19 Pro devices even though firmware discovery successfully identifies them as Antminers.

The affected devices run older stock firmware where `/cgi-bin/miner_type.cgi` is unavailable and returns HTTP 404. Discovery succeeds from both the HTTP Digest challenge and the RPC `version` response, but `AntMinerStockFirmware::build_miner()` subsequently requires `miner_type.cgi`. Model extraction fails, construction returns an error, and the scan result is reduced to `(ip, None)`.

## Reproduction

For an affected device:

1. `GET http://<ip>/` returns:

   ```text
   HTTP/1.1 401 Unauthorized
   WWW-Authenticate: Digest realm="antMiner Configuration", ...
   Server: lighttpd/1.4.32
   ```

2. RPC `version` on port 4028 returns a successful response containing:

   ```json
   {
     "VERSION": [{
       "Type": "Antminer S19 Pro",
       "CompileTime": "Mon Apr 19 16:36:50 CST 2021"
     }]
   }
   ```

3. An authenticated request to `/cgi-bin/miner_type.cgi` returns:

   ```text
   HTTP 404 Not Found
   ```

4. Scanning the address individually with a 15-second identification timeout still returns no miner.

This was reproduced consistently across nine devices with the same response pattern.

## Current behavior

`AntMinerStockFirmware::get_model_with_auth()` unconditionally requests:

```rust
http://{ip}/cgi-bin/miner_type.cgi
```

It then requires the response to decode as JSON containing `miner_type`. A 404 HTML response produces `ModelSelectionError::UnexpectedModelResponse`.

`build_miner()` propagates that error. The factory streaming path converts the error with `.ok().flatten()`, making an already-identified device indistinguishable from an unidentified/nonresponsive host.

Relevant paths:

- `asic-rs-firmwares/antminer/src/firmware.rs::get_model_with_auth`
- `asic-rs-firmwares/antminer/src/firmware.rs::build_miner`
- `src/factory.rs::scan_stream_with_ip`

Observed with revision `da56c59014682870a88ed87603223bcfcaa23a83`; the same construction behavior is present on current master.

## Expected behavior

A device that has already been positively identified as an Antminer should not disappear from scan results solely because `miner_type.cgi` is unavailable.

Possible approaches:

- derive/fall back to the model reported by RPC `version` (the response already contains `Antminer S19 Pro`);
- try an endpoint supported by older stock firmware;
- construct an unknown-model Antminer when positive firmware identification succeeds but model enrichment fails; or
- otherwise preserve an “identified but construction failed” result instead of returning `None`.

The `AntMinerModel` registry already includes the `ANTMINER S19 PRO` alias, so the failure is endpoint/model retrieval rather than absence of an S19 Pro model variant.


## Comments

### b-rowan on 2026-07-29

This feels like a regression.  Usually we request `get_system_info.cgi`, which returns something like the contents of https://github.com/256foundation/asic-rs/blob/master/asic-rs-firmwares/antminer/src/test/json/v2020/system_info.json

Not sure if we should just fall back to that, or always just prefer to use it, but the solution is just to make use of that endpoint.
