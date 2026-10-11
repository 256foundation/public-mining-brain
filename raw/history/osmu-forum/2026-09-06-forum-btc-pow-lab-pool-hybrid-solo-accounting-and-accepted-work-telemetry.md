# BTC PoW Lab Pool — Hybrid Solo accounting and accepted-work telemetry

> Source: https://osmu.xyz/t/btc-pow-lab-pool-hybrid-solo-accounting-and-accepted-work-telemetry/87
> Collected: 2026-10-10
> Published: 2026-09-06
> Registry ID: osmu-forum

BtcPoWLab | 2026-09-06 10:12:10 UTC | #1

Hi OSMU, I am Carlos Monzon from Power CM Software. Disclosure first: I operate BTC PoW Lab Pool.

I would like to introduce our Bitcoin pool and invite technical feedback on how we explain accepted work and reward accounting to home miners.

Our Hybrid Solo model allocates a found block reward as 85% to the finder, 10% to Community Reward and 5% to BTC PoW Lab. Community eligibility uses accepted work within a rolling seven-day window; the finder is excluded from the Community Reward for their own block. This is a conditional allocation when a block is found, not a promise of periodic income.

One measurement detail matters with Vardiff: raw share counts alone are not comparable when difficulty changes. For example, 100 accepted shares at difficulty 1 and 10 at difficulty 10 have the same summed share difficulty. That is an illustration of accounting weight, not a claim about actual pool results or a guarantee of finding a block. Hashrate estimates also need the same observation window.

[Pool status and telemetry](https://btcpowlab-pool.com/status?utm_source=osmu_forum&utm_medium=community&utm_campaign=discovery_2026_09&utm_content=pool_intro)

[Research Lab](https://www.btcpowlab.com/?utm_source=osmu_forum&utm_medium=community&utm_campaign=discovery_2026_09&utm_content=pool_intro)

Which telemetry checks do you find most useful when evaluating a pool with a small ASIC? I welcome questions about the accounting model and anything in our presentation that is unclear.

-------------------------

WantClue | 2026-10-08 15:59:46 UTC | #2

Do you have the source code open sourced ?

-------------------------

BtcPoWLab | 2026-10-09 19:18:40 UTC | #3

Hi WantClue,

Thank you for asking. The production pool code is not currently published as an open-source release.

We publish the reward rules, public telemetry and verification data, but those should not be confused with access to the pool’s source code.

The Proof Center is here:

![image](https://osmu.xyz/uploads/default/original/1X/2136b11e54de92948dc094ddb59717fa2812a73f.svg)

      [BTC PoW Lab Pool](https://btcpowlab-pool.com/proof)

![image](https://osmu.xyz/uploads/default/optimized/1X/0af4049ca9556d0b2ab800fe457d2dde1e41eb76_2_690x362.png)

### [Bitcoin Mining Proof Center](https://btcpowlab-pool.com/proof)

Verify BTC PoW Lab Pool Bitcoin templates, exact 85/10/5 coinbase economics and immutable block proof bundles.

We also have a separate public repository for Share Work Audit, our accepted-work hashrate auditing tool:

[github.com](https://github.com/monzncarlos-droid/share-work-audit)

![image](https://osmu.xyz/uploads/default/optimized/1X/86eafe9cf1a9b74afe3a0e13725347c91937a8cd_2_690x344.png)

### [GitHub - monzncarlos-droid/share-work-audit: Browser-local accepted-work hashrate audit with...](https://github.com/monzncarlos-droid/share-work-audit)

Browser-local accepted-work hashrate audit with explicit windows, CSV export and reproducible methodology. By BTC PoW Lab.

That tool is not the pool engine. I want to be clear about that distinction so readers can assess exactly what is available for independent review.

Best regards,

Carlos Monzon

Power CM Software / BTC PoW Lab
