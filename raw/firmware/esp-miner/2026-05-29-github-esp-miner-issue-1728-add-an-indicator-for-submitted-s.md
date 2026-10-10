# bitaxeorg/ESP-Miner issue #1728: Add an indicator for submitted shares on SV2

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1728
> Collected: 2026-10-07
> Published: 2026-05-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1728
- State: closed
- Author: mutatrum
- Opened: 2026-05-29
- Closed: 2026-07-26
- Labels: none

## Description

If the SV2 pool buffers share submits, there's no visual indication on the dashboard that they have been submitted. More confusingly, in the logs it shows it submitted shares but nothing else so it looks like the pool is ignoring them.

The idea is to add an indicator or a second counter or something which shows the pending shares on the pool side.

Follow-up of #1720.

## Comments

### warioishere on 2026-05-30

I think this is cleanly doable with what SV2 already gives us. The submit side increments `conn->sequence_number`, and `SubmitShares.Success`/`.Error` carry `last_sequence_number`/`seq_num`. So pending is just:

```
pending = (last submitted seq) - (last resolved seq)
        = (conn->sequence_number - 1) - last_resolved_sequence_number   // floored at 0
```

I'd track `last_resolved_sequence_number` on `sv2_conn_t` (updated from both the Success batch ack and the Error seq), and derive `pending` from the two sequence numbers rather than keeping a separate counter, so it can't drift out of sync. Surface it as e.g. `sharesPending` in the system API (0 for SV1).

Two questions before I touch anything:
- Where/how would you want it shown, a separate "pending" counter next to accepted/rejected, or a small badge/indicator near the response time?
- Happy to put up a PR for this if you'd like, should we?

### mutatrum on 2026-05-30

Sounds good.

> Where/how would you want it shown, a separate "pending" counter next to accepted/rejected, or a small badge/indicator near the response time?

That's the biggest question, I'm not a UI designer. But as soon as it's surfaced, maybe you can play around a bit to see what makes sense?

> Happy to put up a PR for this if you'd like, should we?

Yes, please. I was genuinely confused when no shares were reported, so I'm probably not the only one here.

### warioishere on 2026-05-30

PR done
