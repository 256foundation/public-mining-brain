# 256foundation/mujina pull request #105: refactor(bm13xx): merge the first part of the multi-chip driver work

> Source: https://github.com/256foundation/mujina/pull/105
> Collected: 2026-10-07
> Published: 2026-08-30

- Repository: 256foundation/mujina
- Type: pull request
- Number: 105
- State: closed
- Author: rkuester
- Opened: 2026-08-30
- Closed: 2026-08-30
- Labels: none

## Description

The first part of the multi-chip BM13xx driver work, for EmberOne, S19, and S21. It holds the refactoring of the BM13xx thread and the Bitaxe driver that the later parts build on.

The thread now operates a chain the board declares. Every register has a typed value round-trip tested against capture bytes, and the codec decodes per chip model. The Bitaxe driver shrinks to assembly and monitoring around a `BitaxeDevice`.

Fixes along the way: the JobFull length byte and domain-boundary drive strength match factory firmware, and the TPS546 no longer gates its output on the CONTROL pin. Unit tests cover the protocol, chain, and actor exit paths; `just test-bitaxe-gamma` adds hardware smoke and baseline tests, passing on a Bitaxe running suitable firmware. The later parts, board support built on this base, follow in branches stacked on this one.
