# Joining a New Pool

> Source: https://forum.heatpunks.org/t/joining-a-new-pool/231
> Collected: 2026-10-10
> Published: 2025-12-08
> Registry ID: heatpunks-forum

Cardiac | 2025-12-08 02:30:01 UTC | #1

What do heatpunk users want from pools that they’re not seeing with current offerings?

[https://parasite.space/](https://parasite.space/) is doing novel payout structures where the winning share is awarded and entire bitcoin from the payout.

[https://dmnd.work](https://dmnd.work) is using Stratum v2 but it seems like they want KYC and companies signing up. Sad.

What features of a pool would make it optimal for hashrate heating?

-------------------------

tylerkstevens | 2025-12-09 16:00:14 UTC | #2

Share windows are important when your hashrate comes from small, intermittent machines that are constantly adjusting power (heating) and cycling on and off. I’m particularly interested in learning more how e-hash handles this. I think payout methods like tides from Ocean might not be ideal.

Thoughts?

-------------------------

Cardiac | 2025-12-31 14:47:05 UTC | #3

Ehash uses a database (like all other pools) since it’s Cashu based. The window for shares is whatever you want. It seems useful for infrequent miners. Have you examined the various payout schemas? You can see vnprc’s talk about it here: [https://www.youtube.com/watch?v=F2p_V0svDTo&t=11730s](https://www.youtube.com/watch?v=F2p_V0svDTo&t=11730s) (timestamped). The simplest accounting is called Proportional and it’s just # of ehash/# of sats once a payout occurs.

TIDES is nice but doesn’t account for fees. PPLNS-JD (aka [SLICE](https://blog.dmnd.work/understanding-slice-pplns-jd/)) is promising since it accounts for fees in different templates.

-------------------------

Cardiac | 2025-12-31 15:59:32 UTC | #4

[webuyhash.com](https://webuyhash.com/)

### [webuyhash.com](https://webuyhash.com/)

Pool revenue calculator. :thinking:
