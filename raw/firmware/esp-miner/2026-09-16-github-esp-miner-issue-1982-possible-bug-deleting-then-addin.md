# bitaxeorg/ESP-Miner issue #1982: Possible bug: deleting then adding a pool before Save can delete the replacement

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1982
> Collected: 2026-10-07
> Published: 2026-09-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1982
- State: open
- Author: plastardhippo
- Opened: 2026-09-16
- Closed: n/a
- Labels: none

## Description

## Describe the bug

An AI-assisted source review of ESP-Miner v2.15.1 found a possible pool-editor ordering issue. Deleting a spare pool and adding a replacement before saving appears to reuse the deleted pool's ID while retaining a deferred DELETE for that same ID. Saving then appears to write the replacement before deleting it.

This is a source-level finding and has not been reproduced on hardware or in an Angular/backend integration test. Could a maintainer confirm whether another path prevents this sequence?

## To reproduce — proposed, not executed

1. Start with primary and fallback pools plus a spare pool, for example ID 2.
2. Delete the spare pool in AxeOS, without saving yet.
3. Add a replacement pool. The first available ID is now 2.
4. Keep the replacement unselected as primary/fallback and click Save.
5. Reload the pool list and check whether the replacement survived. In an isolated integration test, also inspect the settings PATCH followed by the DELETE for ID 2.

## Expected behavior

The final saved pool list should match the editor: the old spare pool is replaced by the new one. A pending deletion should not delete a newly created pool using the same ID.

## Source evidence

Reviewed release: v2.15.1, commit `78a03e3b5e7600aa8691a7c319ccb4efce72719b`.
The same relevant sequence is present in development commit `43e9b97ef6053bec44543fccb91f5d020e69be4d`, checked September 16, 2026:

- [ID allocation](https://github.com/bitaxeorg/ESP-Miner/blob/43e9b97ef6053bec44543fccb91f5d020e69be4d/main/http_server/axe-os/src/app/components/pool/pool.component.ts#L242-L249) considers the visible controls, without reserving pending deletion IDs.
- [Deletion](https://github.com/bitaxeorg/ESP-Miner/blob/43e9b97ef6053bec44543fccb91f5d020e69be4d/main/http_server/axe-os/src/app/components/pool/pool.component.ts#L298-L310) removes the control and queues its ID in `pendingDeletePoolIds`.
- [Save ordering](https://github.com/bitaxeorg/ESP-Miner/blob/43e9b97ef6053bec44543fccb91f5d020e69be4d/main/http_server/axe-os/src/app/components/pool/pool.component.ts#L326-L346) updates the settings before issuing pending DELETEs.
- [Backend deletion](https://github.com/bitaxeorg/ESP-Miner/blob/43e9b97ef6053bec44543fccb91f5d020e69be4d/main/http_server/http_server.c#L1351-L1389) protects selected primary/fallback IDs but allows an unselected spare to be cleared.

A small standalone ordering model reproduced the ID collision, but that is not a runtime reproduction of the application.

## Hardware / context

Initial review context: Bitaxe Gamma 602 from Solo Satoshi, ESP-Miner v2.15.1. Frequency, voltage and actual pool credentials are not involved in this source-level finding. No device settings were changed to investigate it. Searches for the pending deletion identifier and pool-ID reuse did not locate an exact existing report; happy to link a duplicate if one was missed.
