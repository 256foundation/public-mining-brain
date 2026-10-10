# 256foundation/hydrapool issue #32: Better error messages are needed when debugging Bitcoin node RPC

> Source: https://github.com/256foundation/hydrapool/issues/32
> Collected: 2026-10-07
> Published: 2025-11-03

- Repository: 256foundation/hydrapool
- Type: issue
- Number: 32
- State: closed
- Author: rkuester
- Opened: 2025-11-03
- Closed: 2025-11-04
- Labels: none

## Description

403s, connection failures, and other Bitcoin node errors should result in informative error messages that help users diagnose problems in their specific context. I encountered misleading errors when setting up Hydrapool in Docker following the README.

Because Hydrapool's Docker network wasn't in an `rpcallowip` range in Bitcoin Core's bitcoin.conf (as documented in #31), bitcoind returned 403 Forbidden. Hydrapool panicked with this error:
```
thread 'tokio-runtime-worker' panicked at /usr/local/cargo/git/checkouts/p2poolv2-a1a70bd60bcd2d3a/05554b8/p2poolv2_lib/src/stratum/work/gbt.rs:105:54:
called Result::unwrap() on an Err value: Other("Failed to parse response: error decoding response body")
```

The error blamed JSON parsing when the real issue was a 403 HTTP status code. The response body was empty (because of the 403), which caused the JSON parser to fail. This made diagnosis very difficult, especially when running a pre-built Hydrapool container where modifying p2poolv2_lib's source wasn't straightforward.

I added extensive debug logging to p2poolv2/bitcoindrpc and augmented the error strings returned via BitcoindRpcError. This let me see the actual 403 status and other diagnostic information at debug log level. My changes are here: [96eebfb](https://github.com/rkuester/p2poolv2/commit/96eebfb496e93b12bbbfcd9b95f4717b41472da0?diff=unified) (for reference—not production-ready).

## Comments

### pool2win on 2025-11-04

Addressed in https://github.com/p2poolv2/p2poolv2/pull/251

We now log specific status code and message from bitcoind in case of errors. We also propagate these details in bitcoinrpcerror for clients to handle in different ways if they want to.

The error logging will address the debugging concerns. The second part is something I needed to do for a while, so did that while I was at it.

### pool2win on 2025-11-04

Merged 251, closing.
