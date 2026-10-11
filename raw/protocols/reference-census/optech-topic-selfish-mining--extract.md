# Bitcoin Optech topic page — Selfish mining (extract)

> Registry ID: optech (unregistered, handoff-approved)
> Source: https://bitcoinops.org/en/topics/selfish-mining/
> Collected: 2026-10-10
> Published: n/d (continuously updated topic page; latest newsletter mention 2026-09-18)
> Posture: extract
> As-Of: 2026-10-10

## Capture note

Second of Optech's two mining-related topic pages (no generic `/en/topics/mining/` page exists — see pooled-mining capture for the index findings). Static-rendered page (~3.4KB, full text in HTML — no JS shell). Text below extracted verbatim from the article body.

# Selfish mining

Selfish mining allows a miner (or cartel of miners) controlling less than a majority of hashrate to keep more block reward per unit of work than the majority of honest miners. This effectively allows the sub-majority to dictate block inclusion policy, including censoring transactions.

The attack was first publicly described in 2010. It later obtained its name selfish mining from a 2013 paper. In the form of attack requiring the fewest assumptions, the math shows that a miner with 1/3 of total network hashrate can obtain marginally more block reward per unit of work than the other 2/3 of honest miners. As the selfish miner increases hashrate towards 1/2 of the network total, their block reward ratio increases. If they consistently obtain more than 1/2 of the network total hashrate, they can prevent other miners from keeping any blocks on the best chain, allowing them to obtain all block reward and censor any transaction.

There is no known practical solution to selfish mining for Bitcoin, beyond attempting to ensure no miner or cartel of miners obtains 1/3 or more of total hashrate.

It is possible for selfish mining to occur accidentally, such as when several large hashrate miners have low-latency connections to each other but high-latency connections to the rest of the network. There were indications that such accidental selfish mining occasionally occurred in 2015 when significant Bitcoin mining was located in China and that country's firewall contributed significant latency to block propagation. Mitigating this concern, as well as addressing other problems, inspired the development of centralized block relay solutions (such as FIBRE and FALCON) and decentralized block relay improvements (such as compact block relay).

## Primary code and documentation

- Mining Cartel Attack (2010)
- Majority is not Enough (2013)

## Optech newsletter and website mentions (6 entries, 2023–2026, newest first)

- 2026-09-18 — BIPs #2241 adds BIP332 for opt-in stale tip relay
- 2026-08-07 — Draft BIP for stale tip relay
- 2025-06-13 — Calculating the selfish mining danger threshold
- 2025-05-30 — Selfish mining still possible despite centralized and decentralized block relay improvements
- 2024-04-24 — Discussion about weak block relay and unintentional selfish mining
- 2023-03-29 — Bitcoin Core #27278 improves logging that could indicate a selfish mining attack or other concerns

## Parks

- Other mining-adjacent Optech topic pages not captured (out of the 1–2 file mission scope): block-withholding, asicboost, difficulty-adjustment-algorithms, time-warp, signet.
- No Stratum V2 topic page exists on bitcoinops.org (confirmed against the full 158-topic index); Stratum V2 coverage lives on the pooled-mining topic page (captured separately).
