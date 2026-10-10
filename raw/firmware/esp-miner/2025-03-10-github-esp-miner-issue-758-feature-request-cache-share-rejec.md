# bitaxeorg/ESP-Miner issue #758: FEATURE REQUEST: Cache share rejection messages

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/758
> Collected: 2026-10-07
> Published: 2025-03-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 758
- State: closed
- Author: jtsmith0101
- Opened: 2025-03-10
- Closed: 2025-03-20
- Labels: none

## Description

Good morning,

As a home miner running my own node, I don't expect to have many stale shares.  So the rejections I get are few and far between.  I want to have a way to see my rejection reasons, with timestamps, aggregated in one place.  I'm happy if it's not formatted pretty, just log entries.  Can be a rolling log of 50 most recent rejections with times and rejection reasons (messages).

I'd like the option of getting to see this by individual bitaxe / worker, and as an aggregate on the swarm page, displaying the individual worker(s) that experienced rejected shares, what the difficulty of the submission was, etc.

Thanking you,

James

## Comments

### mutatrum on 2025-03-11

This was merges a few days ago: #746, so at least there's that. Why would you want to know when a share reject happened?

As far as I know, the main causes are stale work, which can happen when a new block has been found, or when a pool adjusts the miner difficulty and it takes a bit of a back-and-forth before agreeing on it. Both are outside of the control of the miner. Unless you've seen other reasons that I'm not aware of?

At the moment there's no mechanism at the moment to cache logs. With #746, it's possible to script it though. The reject reasons and counts are exposed through the API, so you could capture that and push the counts in an InfluxDB for example.



### jtsmith0101 on 2025-03-11

Thanks for responding.

I run my own local node and am experimenting with modifying different pool
software parameters to maximize mining efficiency. Unfortunately, to catch
the rejections in the running bitaxe log means I need to be sitting in
front of my computer with the log screen up to catch that rejection if it
occurs.  Now times that by multiple bitaxes.

Perhaps I'm an edge case for this candidate enhancement.  After all, I'm
trying to tune my  whole system (pool and miners).  Once tuned I'd probably
only occasionally give that screen a glance.

On Tue, 11 Mar 2025, 22:04 mutatrum, ***@***.***> wrote:

> This was merges a few days ago: #746
> <https://github.com/skot/ESP-Miner/pull/746>, so at least there's that.
> Why would you want to know when a share reject happened?
>
> As far as I know, the main causes are stale work, which can happen when a
> new block has been found, or when a pool adjusts the miner difficulty and
> it takes a bit of a back-and-forth before agreeing on it. Both are outside
> of the control of the miner. Unless you've seen other reasons that I'm not
> aware of?
>
> At the moment there's no mechanism at the moment to cache logs. With #746
> <https://github.com/skot/ESP-Miner/pull/746>, it's possible to script it
> though. The reject reasons and counts are exposed through the API, so you
> could capture that and push the counts in an InfluxDB for example.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/skot/ESP-Miner/issues/758#issuecomment-2713705506>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ACPVG7DCS2GPQUAAL3H4KLL2T27L7AVCNFSM6AAAAABYXNVG2OVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDOMJTG4YDKNJQGY>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
> [image: mutatrum]*mutatrum* left a comment (skot/ESP-Miner#758)
> <https://github.com/skot/ESP-Miner/issues/758#issuecomment-2713705506>
>
> This was merges a few days ago: #746
> <https://github.com/skot/ESP-Miner/pull/746>, so at least there's that.
> Why would you want to know when a share reject happened?
>
> As far as I know, the main causes are stale work, which can happen when a
> new block has been found, or when a pool adjusts the miner difficulty and
> it takes a bit of a back-and-forth before agreeing on it. Both are outside
> of the control of the miner. Unless you've seen other reasons that I'm not
> aware of?
>
> At the moment there's no mechanism at the moment to cache logs. With #746
> <https://github.com/skot/ESP-Miner/pull/746>, it's possible to script it
> though. The reject reasons and counts are exposed through the API, so you
> could capture that and push the counts in an InfluxDB for example.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/skot/ESP-Miner/issues/758#issuecomment-2713705506>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ACPVG7DCS2GPQUAAL3H4KLL2T27L7AVCNFSM6AAAAABYXNVG2OVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDOMJTG4YDKNJQGY>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


### mutatrum on 2025-03-12

There are several options you can do with the current firmware, without watching the screen. The most robust is to connect the miners with USB and capture the logs from USB to a file. I there's no machine nearby or there are too many, you can fetch the logs with something like websocat from `ws://<ip-address>/api/ws`. Another option would be to poll the info API endpoint of each miner and store the reject reasons. If you have very many machines it would make sense to capture the data and store it into some sort of database, but that might be overkill.

In all cases you need to do some script things to add timestamps. The miner doesn't have a sense of time, so it only logs time since boot.

### jtsmith0101 on 2025-03-12

Right.... forgot about embedded devices not keeping a global time.

That said, I don't think polling from another computer is the right
answer.  I mean, the bitaxe  devices already have their own logging
function that displays so many log lines to the screen before entries are
no longer available as they're aged off (an assumption / observation).
Wouldn't an easier way being sending all share rejection messages to a
similar screen as the existing logging?  Perhaps a new window below the
existing log windows?  That additional logging information may be forwarded
and displayed to the swarm?

On Wed, 12 Mar 2025, 18:53 mutatrum, ***@***.***> wrote:

> There are several options you can do with the current firmware, without
> watching the screen. The most robust is to connect the miners with USB and
> capture the logs from USB to a file. I there's no machine nearby or there
> are too many, you can fetch the logs with something like websocat from
> ws://<ip-address>/api/ws. Another option would be to poll the info API
> endpoint of each miner and store the reject reasons. If you have very many
> machines it would make sense to capture the data and store it into some
> sort of database, but that might be overkill.
>
> In all cases you need to do some script things to add timestamps. The
> miner doesn't have a sense of time, so it only logs time since boot.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/skot/ESP-Miner/issues/758#issuecomment-2716957268>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ACPVG7FL73O3SQODFII22UT2T7RYLAVCNFSM6AAAAABYXNVG2OVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDOMJWHE2TOMRWHA>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
> [image: mutatrum]*mutatrum* left a comment (skot/ESP-Miner#758)
> <https://github.com/skot/ESP-Miner/issues/758#issuecomment-2716957268>
>
> There are several options you can do with the current firmware, without
> watching the screen. The most robust is to connect the miners with USB and
> capture the logs from USB to a file. I there's no machine nearby or there
> are too many, you can fetch the logs with something like websocat from
> ws://<ip-address>/api/ws. Another option would be to poll the info API
> endpoint of each miner and store the reject reasons. If you have very many
> machines it would make sense to capture the data and store it into some
> sort of database, but that might be overkill.
>
> In all cases you need to do some script things to add timestamps. The
> miner doesn't have a sense of time, so it only logs time since boot.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/skot/ESP-Miner/issues/758#issuecomment-2716957268>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ACPVG7FL73O3SQODFII22UT2T7RYLAVCNFSM6AAAAABYXNVG2OVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDOMJWHE2TOMRWHA>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>
