# bitaxeorg/ESP-Miner issue #1780: reduce sv2 minimum extranonce size to match sv1

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1780
> Collected: 2026-10-07
> Published: 2026-06-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1780
- State: closed
- Author: 0xf0xx0
- Opened: 2026-06-21
- Closed: 2026-07-18
- Labels: question

## Description

The bitaxe on sv2 requests a minimum extranonce size of 6 bytes, while the sv1 side has no minimum. should we set the minimum at 0 and rely on the sv2 pool to provide enough nonce space for its job interval?

## Comments

### cbyam on 2026-06-22

I support this. The 6-byte minimum is arbitrary and inconsistent with SV1, which just takes whatever the pool assigns.

To be clear on the upside: this isn't a hashrate change. The device hashes at the same rate regardless of extranonce width. The real benefit is freeing extranonce budget for the pool's `extranonce_prefix` (which matters for pools and proxies addressing many connections) and better interop with pools that want a larger prefix.

One caveat: the extended path relies on the extranonce today. In `create_jobs_task.c`, the work loop re-sends jobs between pool updates and counts on the incrementing extranonce to make each one unique. If a pool grants `extranonce_size = 0`, every re-sent job is identical and you get duplicate shares, the same failure the SV2 standard branch avoids by not re-feeding work.

Sizing-wise the need is tiny: the counter advances once per ASIC job interval (single-digit ms), so 2 bytes covers ~a minute, 3 bytes covers hours. 6 (2^48) is pure overkill that just shrinks the pool's prefix budget.

So I'd suggest lowering the request rather than zeroing it. One line in `stratum_v2_task.c`:

```c
// hash_rate, 6  ->  hash_rate, 2
sv2_build_open_extended_mining_channel(frame_buf, sizeof(frame_buf),
                                       1, user ? user : "", hash_rate, 2);
```

Going all the way to 0 also works, but only if the loop is taught to stop re-sending when the granted size is 0 (or when the counter overflows a small size), otherwise it compiles and connects but silently duplicates shares. Happy to test against a pool that hands out a small or zero extranonce.

### 0xf0xx0 on 2026-06-23

im down for a minimum of 2, @mutatrum what do you think?

### mutatrum on 2026-07-05

Can you verify using extranonce size 2 and 0 againt #1731? As even if `extranonce_size == 0` , shouldn't `extranonce_2` take this over? If a pool sends the same job, that'll be ignored (assuming they play nice with the jobID), incrementing `extranonce_2` creates new work.

I don't think there's a reason it wouldn't work with 0. And of course, 0 is the best constant, as then there is no constant.

If you could open a pool connection for me to test against with extranonce_size of 0, I can test it from all the models. Especially the BM1397 could be tricky.

Oh and sorry for the late reply.

### cbyam on 2026-07-05

the counter does keep incrementing, but with a 0-byte grant there's nowhere to encode it. the rollable field's length comes straight from the pool's grant:

```c
// create_jobs_task.c, generate_work_sv2_ext()
uint8_t extranonce_2_len = conn->extranonce_size;   // 0 if pool grants 0
uint8_t extranonce_2[32];
memset(extranonce_2, 0, sizeof(extranonce_2));
for (int i = extranonce_2_len - 1; i >= 0 && extranonce_2_counter > 0; i--) {
    extranonce_2[i] = (uint8_t)(extranonce_2_counter & 0xFF);
    extranonce_2_counter >>= 8;
}
```

with `extranonce_2_len == 0` that loop never runs, extranonce_2 is a zero-length field in the coinbase, and every counter value produces a byte-identical coinbase, merkle root, and job. we also don't roll ntime on extended channels, so extranonce is the only uniqueness source.

that's why #1731 makes the 0-byte case worse, not better. the jobID dedup is a sane optimization when the local roll is actually producing distinct work in between. stack it on a 0-byte grant and you get the worst of both: pool resends are correctly suppressed, and our own self-generated "new" jobs are indistinguishable duplicates too. the chip spends long stretches re-grinding a haystack it already emptied, and nothing in the pipeline flags it as stale because nothing changed to flag.

size 2 is a fix, not a band-aid: 65,536 distinct extranonce2 values per pool job means 65,536 distinct coinbases/merkle roots/headers, ~2.8e14 hashes of genuinely unique space hanging off a single upstream job. that comfortably outlasts the interval between real pool updates for anything in this hashrate class. and it composes fine with #1731, since the dedup is keyed to the pool's jobID, not our local roll: 65k locally-varied headers under one jobID never trip the check, because they're no longer byte-identical.

as for testing the 0-byte case on hardware: no known pool actually grants 0. SRI's downstream `min_extranonce2_size` config has a hard floor of 2 (max 16), so SRI-based pools and proxies can't even be configured to hand out less, and braiins always reserves rollable space on extended channels. 0 is spec-legal but only reachable with a purpose-built test harness, and the outcome is already determined by the code above. worth noting SRI's floor being exactly 2 independently corroborates that as the right minimum for us to request.


### cbyam on 2026-07-05

quick correction to my SRI claim, since I went back to the source. the "floor of 2" I cited is a comment in the old translator config examples (min_extranonce2_size in tproxy-config: "Min value: 2 ... Max value: 16"), and nothing in the code enforces it. that knob also governs what the proxy hands its downstream sv1 miners, not what a pool grants an sv2 extended channel. after the roles split into sv2-apps it was renamed downstream_extranonce2_size, still with no enforced floor.

the accurate version of the point is stronger though: the current SRI pool hardcodes CLIENT_SEARCH_SPACE_BYTES = 16 ([channel_manager/mod.rs#L62](https://github.com/stratum-mining/sv2-apps/blob/453e853f96735d6f824649d98b2f95fda6938f2f/pool-apps/pool/src/lib/channel_manager/mod.rs#L62)) and grants every extended channel the full 16 rollable bytes regardless of what min it requested (a request only fails if it exceeds 16). so an SRI pool can't be configured to grant 0, or anything under 16 for that matter. "no known pool grants 0" stands.

that also means I shouldn't lean on SRI to corroborate 2 specifically. the case for 2 is the wrap-time math: it's the smallest request where the extranonce2 counter can't wrap within a job's lifetime. and it's not hypothetical, some pools grant exactly what's requested rather than 16 (mine does), so a bitaxe asking for 2 will really run with 2 bytes.
