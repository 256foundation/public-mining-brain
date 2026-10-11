# OCEAN docs — TIDES Technical Documentation

> Source: https://ocean.xyz/docs/tides
> Collected: 2026-10-10
> Published: 2024-02-29
> Registry ID: ocean-pool

---

T.I.D.E.S.
Transparent Index of Distinct Extended Shares
A Fair Bitcoin Mining Pool Reward System

## Abstract

TIDES is a Bitcoin mining pool payout system which reduces payout variance as low as possible without the pool operator needing to hold and buffer the Bitcoin rewards as a custodian. In practice, TIDES trends towards the maximum payout possible over time, and is auditable such that miners can confirm they’re getting their fair share. Additionally, TIDES can be implemented in a non-custodial fashion.

This writeup assumes at least a basic understanding of how Bitcoin mining works in general, and is about TIDES, the pooled mining reward system. While TIDES was designed for the OCEAN Bitcoin Mining Pool, much of this document is not specific to this or any other pool’s specific implementation of TIDES. It is instead a general description of the reward system itself.

Pool-specific aspects will usually be noted as such. Pools can also adjust parameters of the TIDES reward system to fit their particular needs.

## Introduction

In the world of Bitcoin mining, achieving fairness, low variance, and transparency in reward distribution for miners is crucial. Traditional pooled mining approaches often struggle with issues like payout variance, lack of transparency in the actual reward split, and full pool operator custodial risk. TIDES introduces a solution to address these challenges.

Originally designed for the OCEAN Bitcoin Mining Pool, TIDES optimizes block reward distribution, ensuring miners receive their fair share in a provably accurate fashion. This document delves into the mechanics of TIDES, offering insights into its benefits over conventional systems and its implementation in a non-custodial fashion.

## Definitions

## TIDES-Specific and General

Generation Transaction: The first transaction in a block, created by a miner. This transaction includes the coinbase (sometimes it is also referred to as the “coinbase transaction”) and awards the block’s reward (newly created bitcoins plus transaction fees).

Luck: In context, refers to how much work was expected to be required to find a block (or series of blocks) vs how much work was done. “Bad luck” being more work needed to find block(s) than expected. “Good luck” being less work required to find the block(s) than expected. “100% luck” would be expected work equaling work.

Network Difficulty: A measure of how much work is required, on average, for each block found. The Bitcoin network adjusts the difficulty every 2016 blocks to maintain a 10-minute average block discovery time.

Payout Variance: The fluctuation in mining rewards over time due to the probabilistic nature of block discovery. High variance can significantly affect miners’ earnings stability. Lower variance is generally desirable. The variance of Bitcoin mining without a pool involved is typically very high and can be compared to a lottery.

Share / Proof (used interchangeably): A proof of work that a miner was working on data that is verified to be work towards what the pool expects. Each share has a target, which is the amount of work on average that would be performed by the miner for that share.

Share log: A record of all valid proofs submitted to the pool.

Share log window: The most recent proofs (“top”) of the share log, containing the latest 8 blocks worth of work (8 × network_difficulty).

Target difficulty: The difficulty that a proof must beat before being treated as valid pool share. Also, can be the difficulty a proof must beat for a miner/pool to find a block.

Satoshi: Smallest Bitcoin unit, 0.00000001 BTC.

## What does T.I.D.E.S. mean?

Transparent - TIDES is as transparent as possible and allows miners to calculate their split of the block reward on their own to verify that what they earned matches what’s expected.

Index - Every share is tracked within the current window, and indexed in order. No order is lost.

(of)

Distinct - Every share is stored and tracked individually with order retained. There are no “shifts” or other aggregations/averages/etc that reduce the resolution of rewards. They remain distinct.

Extended - The TIDES share log is vast. It tracks eight (8) blocks worth of work at the current Bitcoin network difficulty for current rewards. This lowers variance to an acceptable level while balancing the time needed to onboard newer miners. Older shares are not discarded even when not in the current window, either, in case they’re needed back in the window after future difficulty increases.

Shares (Proofs) - As defined above, each submitted proof of work received by the pool is stored in the share log. Historically, Bitcoin mining pools refer to these as a “share”, however “proof” is less ambiguous and is used interchangeably in this document.

## How TIDES Works

TIDES handles how proof of work submissions to a Bitcoin mining pool are tracked and rewarded to miners. The basics can be broken up into a few distinct steps.
Pooled Mining Software

TIDES gets accepted proofs of work from the mining pool’s software, the actual server that accepts connection from remote mining hardware and organizes those efforts.

TIDES is agnostic to the software and protocol in use. While at the time of this writing this is dominated by the Stratum protocol, TIDES only needs the proof of work to track valid shares for the purposes of pooled mining rewards. Where these shares come from can be any software capable of hosting the pool itself, provided that the work is valid.
Share Acceptance

Proofs that are valid and accepted by the pool software are added to the top of the share log in the order they are received. Each proof counts as a number of shares in the share log equal to the proof’s target difficulty. This means the share log is effectively a measure of the number of hashes the miner has done for the pool.

Shares are continuously added to the top of the share log, in order, as miners work to find the next block.

Shares are never removed from the share log. The main consideration is that the shares are in order.
Block Solving and the Share Log Window

When a block is found by any miner of the pool, that block’s network difficulty is used to calculate the share log window size (share_log_window, unit: difficulty 1 shares). Up until that point, the window can only be an estimate, since we can not predict exactly when a block will be found nor its difficulty (though it only changes approximately every 2 weeks).

share_log_window is eight times the block’s difficulty worth of shares. A pool can set this to a different value, depending on the amount of variance tolerated.

At eight blocks worth of work, this ensures that all shares submitted have a 99.9665% chance of being rewarded at least once. On average shares will be rewarded eight times.

The total block reward (subsidy plus transaction fees) is used as the basis for calculating the split of earnings (current_block_reward, unit: satoshis).

Each miner’s shares within the share log window are tallied, starting at the share at the top of share log and working backwards through the log until share_log_window shares have been tallied such that a count of each miner’s shares in the window is available and stored (miner_shares_in_window[...], unit: difficulty 1 shares).

The reward is then split up proportionally based on their percentage of the shares in the top of the share log window. Rewards are rounded down to the nearest satoshi.

shares w = shares_in_window
shares m = miner_shares_in_window
r = current_block_reward

∑i miner_shares_in_window[i] = share_log_window ∑i sharesm [i] = sharesw

∑i ( miner_shares_in_window[i] share_log_window ×current_block_reward ) = current_block_reward ∑i ( sharesm [i] sharesw × r ) = r

The above shows rewards calculated without a pool fee. Pool fees can be calculated many ways with TIDES. Generally the share itself is tagged with a flag that represents how its fee is calculated when handling rewards. Specific implementations on fee structures are beyond the scope of this document. (See *Pool Fees* section.)

Assuming a uniform pool fee (pool_fee_percentage) across all shares rewarded, the calculation looks like this for finding the pool’s total fee collected (pool_fee, unit: satoshis):

f sum = pool_fee
f % = pool_fee_percentage

( current_block_reward -pool_fee) =
∑i ( miner_shares_in_window[i] × ( 1-pool_fee_percentage ) share_log_window × current_block_reward )

(r-fsum)= ∑i(sharesm[i]×(1-f%)sharesw×r)

While this is idealistic, actual implementations will round the pool fee down to the nearest satoshi, per miner, when calculating rewards.

Note: Again, shares are never removed from the share log. As a result, individual shares are generally expected to be rewarded many times (8 times on average) while they are within the window at the top of the share log. An average of eight times when the window is sized as noted in this document to eight times the network difficulty.

Technical note: The top of the share log window is determined based on where the top of the share log was when the work was actually issued to the miner who found the block. It is not the moment in time the block is actually found. (Prevents cheating. See Edge Cases section.)
Simplified Example

Let's say a miner represents 5% of the total work in the share log window at the time a block is discovered. If the total block reward is 6.25 BTC, the miner's share of the reward would be 6.25 BTC × 5% = 0.3125 BTC. Pretty simple. If there’s an additional 1 BTC in transaction fees to claim, for a total of 7.25 BTC block reward, this example miner receives 7.25 BTC × 5% = 0.3625 BTC.
General Summary

As blocks are found, miners receive their fair split of the block reward. The result is that the total reward trends towards the maximum possible reward at 100% “luck”. There is always going to be some variance, but due to the large window size the average trends towards 100% “luck” over time.

This gives miners both a provably fair split of every block reward for every single block, and that reward is the maximum possible reward.

See *Life of Shares* section for some examples of how this plays out in practice.
Implementation Notes

Implementations of TIDES must never lose resolution within the share log. Every valid proof submission must be tracked individually, and in a way that preserves order and amount of work performed. Unlike other reward systems that tend to just count submissions within a small time frame and aggregate those, TIDES is accurate down to a single share at all times. There are no “shifts” or similar losses of contribution resolution with TIDES.

This is, however, quite resource intensive, especially if rewards must be continuously calculated for performing actions such as direct generation payouts. While there are optimizations that can be done to keep this process as resource-efficient as possible, it’s a significant amount of data that must be accurately tracked for every miner.

The Bitcoin network difficulty is currently 132,716,002,350,731. With a window of network_difficulty × 8, that means TIDES must continuously calculate rewards for 1,061,728,018,805,849 shares.

Any optimization performed must never lose resolution on the amount of work a miner has in the window at any given time, nor the order of miner work submissions.

Additionally, since the size of the window can change with changes in network difficulty, a TIDES implementation may never fully discard shares, even when they’re no longer in the share log window. The judgment of a pool administrator can be used regarding resources and may archive older portions of the share log that are increasingly *unlikely* to become relevant, but these should not be fully discarded.

## Additional Technical Details
Pool Fees

Pools generally must collect a fee to cover expenses. Pool fees are intended to be handled at the individual share level. Every share is tagged with its fee rate flag at the time it is mined. Any time that share is rewarded when a block is found (as in, it’s in the top of the share log within the share log window at that time), the pool’s fee is deducted from that share’s total based on the fee rate for that particular fee rate flag.

Shares can have different fee rates, depending on the rules of the pool at the time the share was mined. The share will retain the fee rate flag forever once mined, unless a pool’s policy causes a change at a later date.

A miner may have shares in the share log with different fee rates depending on how they were mined and the pool’s specific rules. For example, a pool may offer a discount for using a specific template or type of miner. A pool may charge an additional fee for using a specific node or implementation. This is entirely up to the pool.

Technical note: As shares are tallied in the share log window, shares with different fee rates are tallied alongside the full tally per miner in their own buckets. The fee is then deducted from the aggregate by the appropriate percentage for each of the shares-with-fee tallies, rounded down to the nearest satoshi.
Difficulty Changes

As the network difficulty changes, the size of the share log window to be rewarded when a block is found changes.

If the network difficulty goes up, the size of the window increases. Older shares end up being in the window again, despite having “slid out” before the difficulty change.

If the network difficulty goes down, the size of the window decreases. Older shares end up no longer being in the window, despite having been in the window before the difficulty change.

Miners who have continuously mined with the pool through the entire current share log window will see no real change to their reward-per-block, since their proportion of the share log window isn’t going to change much at a difficulty change.

This ensures the lowest variance possible and consistent rewards per unit of work across difficulty change boundaries.

Keep in mind the window doesn’t exist as anything other than an estimate until a block is found. It can only be estimated based on the current difficulty and top of the share log.
Subsidy Halving, Large Transaction Fees, Etc.

TIDES is completely agnostic to the value of the block reward (subsidy plus transaction fees, current_block_reward).

No matter how much the block reward, miners are simply awarded their fair split of that reward at the time a block is found. Since shares in the share log are counted based on the amount of work done, not some pre-calculated amount of Bitcoin, the *percentage* of the reward split doesn’t change due to changes in the block reward. The miner’s portion is whatever their portion of the top of the share log is. It doesn’t matter if the change in block reward is due to high/low transaction fees, subsidy halvings, etc. The amount of work in the share log is what matters.
Workers

Workers do not matter to TIDES. Rewards are calculated per user, not per worker. The sum of all work submitted by a user’s workers is what is used for reward calculations.

Implementations of TIDES and relevant optimizations *may* be used to produce stats per worker, and can generate these per block to estimate earnings per worker. *However*, an individual worker’s portion of the block reward will tend to be estimated less accurately, only to within +/- one satoshi. With a significant number of workers, this can lead to stats errors.

Actual Bitcoin earnings accounting should be based on a per-user basis, not worker.
Generated Payouts

Implementing TIDES with payouts from the generation enhances security by ensuring miners' rewards are directly linked to their contributions without the need to trust pool operators to later distribute the earnings. This ensures the mining pool itself has minimal, if any, control over funds distributed directly to miners by the Bitcoin network itself. Miners can actively audit the block templates they are mining to ensure it rewards them the correct split.

Implementations of TIDES should be implemented with block rewards generated to miners wherever possible.

## Technical Edge Cases
Share log is too small

In two possible instances, it’s possible that when a block is found that there may not be enough shares in the share log equal to eight blocks worth of work at the current network difficulty.

The times this can happen are:

- Initial launch of a TIDES-based pool, where there simply has not been enough work submitted to total eight blocks worth of work at the current network difficulty.
- If the network difficulty rises by an extreme amount quickly and the pool has not kept up with its portion of the total network proportional to that meteoric rise in difficulty.

If this happens, rather than use the network difficulty times eight as the denominator for splitting rewards (share_log_window), TIDES uses the total work in the share log (share_log_total). This means the reward is being split across fewer than eight blocks worth of work, but each share’s individual reward ends up being larger, leading to a fair split but with more variance.
Miner's individual reward is too small

Rewards are proportional to the block reward based on the miner’s individual contributions in the share log. If the miner has not submitted enough work to earn at least one full satoshi worth of earnings at the time a block is found, those earnings are lost as TIDES itself has no concept rewards unrelated to a single block.

In practice, this isn’t an issue for any modern mining equipment working continuously on the pool, even as the pool reaches high hash rates.

This does effectively price out miners that are simply not effective at mining, such as CPU miners, since they cannot contribute enough work to earn any reward each block.
Share log window delta - block time and work time

The top of the share log is always determined by what the top of the share log was for any given work that is handed out to miners. The effect is that there is some share count latency between what the top of the share log was when the work was given and what it is determined to be at the time a block is found.

This is by design, and prevents a malicious miner from temporarily delaying submission of a block winning share for some period of time while trying to pad the top of the share log for more reward before giving the winning share to the pool.

This does not affect overall rewards. The size of the window is still the same for the block, so rewards are still calculated normally. It just ends up time shifting the window slightly into the past (in practice, usually up to 40 seconds depending on a number of factors).

While this doesn’t directly impact rewards for miners, in theory, it could cause confusing optics with some extreme examples. For example, it could mean that a brand new miner who joins the pool might not earn any reward for a block that just happens to be found within the first moments of that miner joining. While they would have shares in the top of the share log *at the time the block was found*, they might not have had any shares in the top of the share log *at the time the work that found the block was given to miners*… this holds true even if that new miner himself was the one who found the block.

This is noted for completeness, and again, doesn’t affect overall rewards.
Pool-Specific Implementations of TIDES

Due to the way TIDES works, rewards can be pre-calculated when work is given to a miner. This means a pool can use that data to pay miners directly from the block’s generation transaction without ever being responsible for the miner’s earnings.

When work is given to a miner, that work is internally tagged with the share ID of the share currently at the top of the share log when that work was issued to the miner, along with a generation transaction that would pay all miners appropriately for the block being worked on for the top of the share log at that point in time.

This can result in a block rewarding miners for a share log window a short period in the past vs the moment the actual block is found, but this makes sure the rewards in the block match actual rewards for the window and doesn’t affect overall rewards. (See *Technical Edge Cases* above.)
Rewards vs. Payouts Distinction

Earnings are rewarded every block for shares in the share log. Payouts may not necessarily coincide with every reward for various reasons. Generally, a tiny payout isn’t worthwhile, since an aggregate of dust payments are not efficient or cost effective to spend/move later.

Pools may implement alternative methods of paying out these smaller amounts, such as by accruing them until the sum exceeds a minimum threshold (see below), with Lightning integration, or other ways.

However, how the pool tracks and handles payouts is beyond the scope of TIDES itself, as TIDES is the reward system and not the payout system. TIDES does make a fair payout simpler for both the pool and miner to validate, but doesn’t handle the payout itself.
Minimum Payouts

TIDES itself has no concept of a minimum payout itself. TIDES simply determines the reward split down to the satoshi. A pool may implement payouts in a way where earnings are not actually provided to a miner except under predetermined conditions, such as reaching a threshold of a preset value.

## Life of Shares

A share's life begins when a miner submits a valid proof of work to the pool. This share, and its target difficulty, is immediately recorded at the top of the share log. The top of the share log always contains the most recent share the pool has accepted from any miner.

It's also important to note that the share's value is intrinsically linked to the amount of actual work it represents - the higher the target difficulty of the share, the greater its value in the log and the more of the window it occupies.

Another way to look at it is that the share log tracks the number of useful hashes done by a miner in the most accurate way practical, and the share log window contains the proofs of hashes done by all miners in the pool, in order, so that their specific fair reward can be determined.

Upon submission, the share becomes the top share of the share log window, which contains the latest 8 blocks worth of work. The position of the share within this window is crucial as it determines its eligibility for rewards. The share is indexed in order, with older submissions below it and newer submissions above it.

Share log visualization example where the top left is the newest share and the bottom right is the oldest. Miner has one share at the top of the share log.

In the example image above, you can see that “U” has submitted their first share, and it’s now at the top of the share log. The current share log window is highlighted.

Progression of example miner’s progress in the share log.

As more shares are submitted by “U”, more of the window will have shares from “U”. Their percentage of the share log window will settle around their percentage of the pool as a whole, which ensures their split of all rewards is completely fair. It does take some period of time, depending on the pool’s network hash rate percentage, for a miner to have shares evenly distributed throughout the share log.

As new blocks are found by the pool, the share log window is recalculated based on the latest block's difficulty (red outlined shares in the example visuals). During this process, each share within the window is evaluated for its contribution towards finding the block. The total block reward is proportionally distributed among all shares in the window, with each share earning a slice based on its target difficulty relative to the total of all shares in the window. (In the visual examples here, all shares are target difficulty 1 for simplicity.)

You can look closely and see that order is preserved for all shares by all miners, even after the shares are no longer in the window at the top of the share log. New shares are never inserted anywhere except at the top.

Example miner’s new and old shares in the share log.

A unique aspect of TIDES is that shares are not removed from the share log after being rewarded. In fact, shares are never discarded and should be kept by the pool indefinitely to ensure there’s always a full share window (see notes on difficulty changes). As long as a share remains within the share log window, it remains eligible for rewards with each new block found.

This means a single share can be rewarded multiple times. A share is expected to be rewarded on average eight times, but can be rewarded more or fewer times, depending on pool luck. For a miner who mines continuously at the pool, the variance is able to iron out over more than eight blocks worth of work and end up as expected.

Looking at this another way, during a short period with “low luck”, where blocks have taken more work than average to find, a share will be rewarded fewer than eight times. In a short period of “high luck”, where blocks have taken less work than average to find, a share will be rewarded more than eight times.

Over longer periods, however, this averages out to rewards trending towards average luck. If for example, one share is rewarded 7x and another 9x, this ends up being the expected amount of work rewarded.

Example miner visualization after a difficulty increase.

If the difficulty increases, then “U” would have their older shares now back inside the share log window for blocks with the higher difficulty. Their percentage of the share log window is unchanged, however. In the example above, the network difficulty doubled, so the share log window also doubled in size.

Note: The example images are based on pseudorandom data, and have a higher variance than a real implementation due to small overall example values (difficulty and share log window size). In practice, there is hardly any delta-percentage at difficulty changes.

While the difficulty change will change the frequency of blocks found, it changes the total reward per share as it would on any pool, or effective total reward per time period with solo mining. It does not, however, change the miner’s percentage of the share log, provided they’ve been mining long enough to have older shares return to the window. Their reward per block ends up unchanged under TIDES.

In reality, the pool hash rate will fluctuate as miners come and go, equipment is upgraded, decommissioned, etc. A miner’s hash rate will not be 100% consistent, either. But TIDES works such that when the pool finds a block, you get your fair split of the reward based on your contribution, and these variables level out as much as they possibly can.
How a Share is Rewarded

As we touched on in the last section, a share is rewarded any time the following is true:

- The pool finds a block, and…
- The share is in the window at the top of the share log at that time.

A key point with TIDES: Because the pool doesn’t buffer funds to artificially attempt to remove all variance, a miner can only have new earnings when the pool finds blocks.

Every time a pool finds a block, all shares in the window are rewarded. Let’s look at what that will look like for a new miner. For our examples, we’ll assume the pool has average luck and finds blocks exactly every time after network_difficulty shares are submitted. This better represents long term averages.

New miner’s earnings graph. Mining at a constant hash rate. X-axis: Pool blocks since joining; Y-axis: Earnings (unitless). Red: Sum of earnings; Blue earnings per block.

As you can see from the graph, there is an effective “ramp up” period before a miner under TIDES starts getting their full reward every block. The graph above is unitless, as it holds for any consistent hash rate, with consistent difficulty, etc, when also presuming average luck. In practice, “luck” and other factors will affect this, but the concept remains the same.

The design is to eliminate as much variance as possible. In order to do that, the share log window needs to be large. Because the window is large, it takes some time for your work to be evenly distributed throughout the window. As the pool’s overall hash rate increases with respect to the network, the time between blocks will decrease, and the total real time for gaining uniformity within the share log decreases as well.

Once there are shares in the window, they act as a buffer to iron our variance for your own earnings. If you were to stop mining temporarily or permanently for whatever reason, you would still have shares in the share log that can be rewarded by blocks until they are no longer in the window.

New miner’s earnings graph after going offline. X-axis: Pool blocks since joining; Y-axis: Earnings (unitless). Red: Sum of earnings; Blue earnings per block.

In the above example, the miner goes offline after block 24. Their shares remain in the window for some period of time (eight blocks worth of work). This is a benefit over PPS type pools, as you can continue to receive some rewards during downtime, maintenance, curtailment, etc. And once online again, build back to the stable reward level.

## FAQ

Q. *Since TIDES doesn’t require that a pool buffer funds, how does it prevent gaming the system (pool hopping, etc)?*
A. Because shares are never discarded, there’s always shares in the reward window when a block is found. A miner can’t pool hop to gain an advantage, because they’d be bunching up shares in a specific spot in the share log window, and then would have none elsewhere. So what would happen is that they hop on after a block is found (like you would when a straight proportional pool found a block to game the system), and they don’t gain anything special because shares from the previous “round” (TIDES has no concept of a “round”) are not discarded. Instead, the miner just gets their fair share for the hash rate contributed, assuming another block is found.

Q. *I heard TIDES pays less than [insert other reward system here]. Is that true?*
A. No, TIDES is provably fair. You can look at blocks found by the pool, look at the pool’s overall hash rate, and look at the shares you submitted counted by your own equipment, if desired, and confirm you’re getting your fair split of the block’s reward. Pools can expose even more detailed data via their APIs to allow validation at an even more accurate level.

Q. *Does TIDES share the transaction fees in a block? If so, how?*
A. Yes. Miners get their fair split of the transaction fees as well as the block’s subsidy. Whenever a block is found, the full reward including transaction fees is used to determine the amount split up among miners.

Q. *I mined for [some period of time] and haven’t gotten any Bitcoin! The pool must be cheating, right? Right?!*
A. Unlike hashrate-rental payout systems such as FPPS, TIDES can only reward miners with Bitcoin that is mined. As in, the only Bitcoin rewarded is from blocks found by the pool. There’s also generally a minimum payout threshold in place on the pool as well, and you will not receive a payment until a) you’re earned Bitcoin from blocks mined while you have shares in the share log, and b) you’ve earned enough Bitcoin to reach the minimum payout threshold. In short, it may take a bit of time, but you’ll earn your fair share of the rewards.

Q. *It says I’m earning so little per block! I should be getting way more! Why aren’t I?*
A. Your earnings per block depend on several factors. For example, if you’re earning 1 BTC per block while the pool’s hash rate is 1 Eh/s, if the pool’s hash rate jumped to 2 Eh/s, you’d then be earning 0.5 BTC per block… but twice as often. The earnings per block will fluctuate with the pool’s overall hash rate, but the amount of Bitcoin earned over time trends towards the expected value for your hash rate no matter how frequent or infrequent blocks are found.

Q. *Is my [insert non-ASIC miner name, or old ASIC miner name here] fast enough to mine with TIDES?*
A. TIDES does not care what kind of miner you use. If you’re submitting valid shares, they’ll be added to the share log. That said, you need a miner (or group of miners in aggregate) that can make the minimum payout threshold set by the pool in a timeframe that’s acceptable to you. For things like CPU miners or scammy “hobby” miners, this will simply never happen in a person’s lifetime. Even some older ASIC-based miners may take months or years to reach the minimum payout set by a pool.

Q. *What if a pool using TIDES mines a massive transaction fee in their block, like has happened a few times with other pools? Will miners get their split of that as well? Or can the pool cheat the miners out of the reward and “return” or keep it?*
A. TIDES is intended to be implemented in a non-custodial fashion, meaning miners should be paid via the generation transaction, and already have their split of that large transaction fee without the pool ever even having control over it. TIDES doesn’t care if the transaction fees are 100 satoshi or 100 BTC. The full block reward is split with miners.

Q. *This sounds a lot like PPLNS. Is TIDES just PPLNS?*
A. TIDES is what PPLNS was originally supposed to be. TIDES is not the pseudo-PPLNS as implemented by every other “PPLNS" pool to-date where shares are either tallied in “shifts” and lose resolution (lower rewards) or the “N” used is extremely low (high variance, lost rewards), or worse. Instead, TIDES keeps track of *all* shares and rewards the latest network_difficulty × 8 shares with every block. This means your earnings are 100% fair, as high as possible, and completely verifiable with each block. In short, TIDES is not directly comparable to any current or historic PPLNS pools.

Q. *I can only mine sporadically, or at certain times of the day. Can I still mine with TIDES?*
A. Yes. In fact, with TIDES you’ll likely end up with more consistent rewards than other reward systems because of the way the share log works. You’ll end up at some average percentage of the share log based on your average hash rate over the span of a share log window, and earn rewards based on that. And, since you always have shares in the share log (as long as you eventually return), you’ll continuously get rewards. You generally won’t miss out on blocks mined while you're offline. You’re not penalized for being offline. Your shares aren’t simply discarded while they’re in the window. There will be slightly higher variance in rewards than a miner who mines continuously, but you’ll still see fairly consistent rewards even if you only mine for a short time per day.

Q. *I want to mine on a TIDES pool. What can I do to maximize my earnings?*
A. For the lowest variance and highest reward possible, you want to point your miners at the pool and keep them there. This way you constantly have the most amount of the share log filled with your shares as possible, and thus maximize your reward and minimize your variance.

Q. *Is TIDES itself decentralized?*
A. TIDES, by nature of how the share log works, cannot itself be decentralized, sadly. The amount of processing and validation required to continuously update reward calculations and other stats simply can’t be done sensibly in a decentralized way. But, TIDES is provably fair. If a pool were running TIDES and it ended up not being 100% fair, it would be immediately obvious this was the case, unlike with FPPS-type payout methods which are completely opaque and nearly impossible to accurately verify.

Q. *Is TIDES compatible with decentralized mining?*
A. TIDES is agnostic to the type of work, as long as it arrives at a valid Bitcoin pooled mining proof of work. That share can come from a traditional centralized system (pool-side template and mining, such as Stratum) or from a decentralized template pooled mining system. It matters not to TIDES.

That said, TIDES is designed to allow a pool to charge different fee rates based on several factors. Since every share is distinct in TIDES, each share can have its own fee rate tagged to it. This way a miner can use multiple methods with different fee rates on the same user and still end up with a fair split of their reward while being charged fees appropriate for their actual work with per-share resolution. This can make it easy for a pool to encourage decentralized mining by offering a lower fee for shares found using such protocols.

Q. *This all sounds so complicated. What’s the bottom line?*
A. The bottom line is you should be mining with a pool that uses TIDES to ensure you’re always getting your fair share of block rewards mined. No games, no funny math, and designed to be non-custodial. Just fair mining.

## Conclusion

TIDES revolutionizes the Bitcoin mining pool landscape by introducing a reward system rooted in fair, transparent, and simple reward distribution. Unlike traditional methods that often leave miners guessing about if what they’re earning is truly fair, TIDES provides a clear path that guarantees each participant receives their rightful reward split. This approach sets a new high standard for reward systems in Bitcoin mining.
