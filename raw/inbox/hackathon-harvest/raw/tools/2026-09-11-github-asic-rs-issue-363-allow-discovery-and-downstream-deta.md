# 256foundation/asic-rs issue #363: Allow discovery and downstream detail requests to share one concurrency budget

> Source: https://github.com/256foundation/asic-rs/issues/363
> Collected: 2026-10-07
> Published: 2026-09-11

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 363
- State: open
- Author: cfilipescu
- Opened: 2026-09-11
- Closed: n/a
- Labels: none

## Description

## Problem

`MinerFactory::scan_stream_with_ip()` lets callers begin processing miners as discovery completes, but its discovery concurrency is managed internally. A downstream caller that immediately runs `Miner::get_data()` cannot share that same concurrency budget.

Today, a caller has two practical choices:

1. Give discovery and detail collection independent limits, which can exceed the configured connection budget.
2. Statically divide the budget between discovery and details, which leaves capacity idle when the subnet is sparse or the workload is unbalanced.

For example, a total budget of 128 may be divided into 96 discovery operations and 32 detail operations. This keeps load bounded, but discovery can use only 96 slots even when no miners have been found and all 32 detail slots are idle.

This comes up in [umc-utils#911](https://github.com/EPIC-BLOCKCHAIN/umc-utils/issues/911) and [umc-utils#917](https://github.com/EPIC-BLOCKCHAIN/umc-utils/pull/917), where device records need to be emitted before a large subnet scan completes.

## Requested capability

Please provide an opt-in way for discovery and caller-owned follow-up work such as `Miner::get_data()` to draw from one dynamic concurrency budget.

The exact API is open for discussion. Possible designs include:

- accepting a caller-supplied shared limiter;
- yielding an owned permit with each identified miner so the caller can retain it through detail collection; or
- providing a combinator that runs caller-supplied async follow-up work under the factory's limiter.

The key behavior is that unused capacity should automatically be available to either stage. A sparse scan could use the full budget for discovery, while a dense scan would naturally shift some capacity to detail collection.

## Desired semantics

- The total in-flight discovery and follow-up operations never exceeds the configured budget.
- Detail collection can begin before discovery of the full range finishes.
- A concurrency limit of 1 alternates safely without deadlocking.
- Backpressure prevents an unbounded task or miner queue.
- Dropping the stream/future cancels remaining work and releases all permits.
- Failed and unsupported addresses release capacity normally.
- Existing `scan()`, `scan_stream()`, and `scan_stream_with_ip()` APIs and behavior remain unchanged.
- Completion-order streaming remains available.

This would let downstream applications optimize time to first result and total scan time without guessing a fixed discovery/detail split.
