# SRI issue #1791 — New Translator Proxy (closed, 30 comments)

> Source: https://github.com/stratum-mining/stratum/issues/1791
> Collected: 2026-10-10
> Published: see body
> Registry ID: sv2-repo

NUM: 1791 STATE: closed CREATED: 2025-07-05T17:39:32Z CLOSED: 2025-09-24T12:48:24Z COMMENTS: 30
TITLE: New Translator Proxy 
LABELS: 

This PR replace the current Translator Proxy with a new one, which is able to:
- run in `Aggregated` or `Non-aggregated` mode (it can open one single extended channel which is shared by every downstream or an individual extended channel for every of them)
- reject stale shares by doing a first check as soon as it gets a sv1 share from the sv1 miner
- fallback to a secondary upstream when the first upstream is not responding or it closes the channel

This new Translator Proxy is also more modular, clean, and easy to extend with future functionalities than the previous one.

It's also based on the newer client-channel APIs introduced by https://github.com/stratum-mining/stratum/pull/1724.

@Shourya742 also did a great work wrt tasks management for which we never noticed any ghost processes during our testings.

Closes stratum-mining/stratum#1623 
Closes stratum-mining/stratum#1562 
Closes stratum-mining/stratum#1582 
Closes stratum-mining/stratum#1675 
Closes stratum-mining/stratum#1632
