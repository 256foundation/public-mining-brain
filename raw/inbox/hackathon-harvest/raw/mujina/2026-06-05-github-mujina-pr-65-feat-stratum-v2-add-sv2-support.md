# 256foundation/mujina pull request #65: feat(stratum_v2): add SV2 support

> Source: https://github.com/256foundation/mujina/pull/65
> Collected: 2026-10-07
> Published: 2026-06-05

- Repository: 256foundation/mujina
- Type: pull request
- Number: 65
- State: open
- Author: jayrmotta
- Opened: 2026-06-05
- Closed: n/a
- Labels: none

## Description

# Summary

This pull request introduces Stratum V2 support to Mujina, it's the result of #54 with guidance from Ryan and Plebhash. 

The SV2 team has great crates like channels_sv2, sv2-apps, and so on, which made possible for Mujina to reuse the same APIs, behaviors, and patterns used to build their proxies, pools, and so on which will be Mujina's counterparties. In other words, we abstract away a big part of the stratum-related code like the Noise handshake, frame processing, state machine, and so on.

We ended up with a lot less domain-specific protocol code, and more dealing with the intricacies of a firmware like being shutdown-safe, having safe defaults and checks, interfacing and providing feedback to the user.

This pull request is in draft and open for comments, suggestions, etc. I will continue to edit it as I prepare it for a final review.

# Steps to try it out

Assuming you have Mujina cloned and checked out this pull request's branch.

Export the variables as we normally do for SV1 servers, but using the `stratum2+tcp://` scheme and suffixing it with the authority key `9auqWEzQDVyd2oe1JVGFLMLHZtCo2FFqZwtKA5gd9xbuEu7PH72` as described in SV2 spec.

```bash
$ export MUJINA_POOL_URL="stratum2+tcp://75.119.150.111:3333/9auqWEzQDVyd2oe1JVGFLMLHZtCo2FFqZwtKA5gd9xbuEu7PH72"
$ export MUJINA_POOL_USER="<bitcoin payout address>.<worker name>"
```

Then you can try with regular log level or run it with debug, that would help if you see any problems as you test.

```
$ RUST_LOG=mujina_miner=debug cargo run
```
# Features

- Support for SV2 extended channels. There is a theoretical limit of 280TH/s for standard channels HOM (header only mining), and given that Mujina intends on powering high hashrate devices it seemed reasonable to start supporting extended channels, but remaining open to adding standard channels later if a good reasoning/argument is presented.
- Adapted the exponential backoff reconnect strategy to be used both by SV1 and SV2. It was also introduced a distinction of errors that might be temporary and can be retried like reconnections in contrast to errors that are fatal and require intervention.
- Introduces a set of integration tests using `integration_tests_sv2` harness and its sniffer for assertions in behavior focused tests meant to enforce protocol compliance.
- Made several improvements to accomodate a second protocol and the "wiring" required to switch depending on the protocol scheme in the provided URL.

# Notes

1. I had a challenge around building a merkle root as the terminology currently used is SV1-specific but the data structure is/should be generic/agnostic. For example SV2 doesn't use the term `extranonce2` anymore, which conflicts with `MerkleRootTemplate` and `Extranonce2`, both important to keep SV1 and SV2 functionality.
2. If you run long enough with debug logs enabled, you'll see reports of duplicate shares found and dropped by the client. I elaborated more on this below as a comment, I think this should be handled in its own pull request, which I'm happy to work next if nobody else does.

## Comments

### jayrmotta on 2026-06-05

My recent test session pointing to the SRI pool had 100% shares accepted, and that's expected as we use the same `validate_share` function used by the pool (tested against the SRI pool). Some shares do however fail the validation and report errors, as far as I could observe all related to duplicate shares.

I did some investigations and I suspect we suffer from the same issues that led to https://github.com/bitaxeorg/ESP-Miner/pull/420 which was also triggered by esp-miner's implementation of SV2 support. Something for a separate discussion and implementation, but I believe has to happen given that allowing for higher hashrate is something that matters more for Mujina then it does for ESP-Miner.

I was wondering if a share that fails `validate_share` should be accounted as rejected, even if the rejection came from the client itself and not the upstream server. Right now it's not being accounted, hence the 100% success.

### adammwest on 2026-06-11

Another Relavent PR https://github.com/shufps/ESP-Miner-NerdQAxePlus/pull/546

> I did some investigations and I suspect we suffer from the same issues that led to https://github.com/bitaxeorg/ESP-Miner/pull/420

I am the author of that PR, 
If you use sniffed Antminer register values, the space is smaller than the 280Th theoretical limit for header only mining.
I think first ill try to make an issue then this topic can be discussed in more detail.
https://github.com/256foundation/mujina/discussions/72

### rkuester on 2026-07-04

Rebased this atop 2f6efca, which now ensures that each commit in a multi-commit PR passes CI.

### rkuester on 2026-07-06

> > I did some investigations and I suspect we suffer from the same issues that led to [bitaxeorg/ESP-Miner#420](https://github.com/bitaxeorg/ESP-Miner/pull/420)
> 
> I am the author of that PR, If you use sniffed Antminer register values, the space is smaller than the 280Th theoretical limit for header only mining. I think first ill try to make an issue then this topic can be discussed in more detail. #72

In the course of reviewing this PR, I've gone down the search space partitioning rabbit hole (which if done incorrectly can lead to duplicate shares) and have posted a link to a draft write-up over in discussion #72. It's still a work in progress as I wrap my brain around all the work esp-miner and its derivatives have done to reverse engineer this behavior. Thanks again, @adammwest!

### jayrmotta on 2026-08-14

Hey @rkuester, I just rebased main onto this branch to keep it fresh and ready for reviews, but the CI failed because the `stratum-apps` transitively brings `json5` which uses this `ISC` license.

I'm sending this message so you can help me assess if we could accept dependencies with this license or if I have to consider alternatives so we don't depend on that.

### rkuester on 2026-08-15

> Hey @rkuester, I just rebased main onto this branch to keep it fresh and ready for reviews [...]

I owe you several beers already for your patience.

> [...] but the CI failed because the `stratum-apps` transitively brings `json5` which uses this `ISC` license.

ISC is acceptable. The initial addition missed it because it wasn't in any of our existing dependencies. For the record, it's widely used and essentially MIT, and GPL-compatible per [the FSF's guidelines](https://www.gnu.org/licenses/license-list.html#ISC).

Would you please add it to the allow list in the relevant commit?

Thank you for testing the new license check machinery! 😂

### rkuester on 2026-08-16

> Would you please add it to the allow list in the relevant commit?

@jayrmotta in order for the series to pass CI on each commit individually, that needs to get either amended into the commit that adds the dependency or reordered as its own commit before the commit that adds the dependency.

(`just ci` locally should give you the same result, hopefully. If not, please let me know, because it would be a subtle bug with `just ci` on updates to PR branches.)

### jayrmotta on 2026-08-31

Hey @rkuester, I might just go ahead and cut the `integration_tests_sv2` dependency along the tests I had written.

Perhaps in the future we can have something like that as a separate repo, but for now I think the gain we get by simplifying the changeset just seems worth.

I might also move this back to draft to invite more reviews and comments until I have finished rebasing and removing this dep.

### jayrmotta on 2026-09-14

Summary of my recent changes:

- The tests that relied on `integration_tests_sv2` were dropped as they brought many transient dependencies and added a significant number of lines. Perhaps we can think of a fuzzing approach external to the main repo;
- Implemented `SetupConnectionSuccess.flags` version rolling enforcement, a pool answering REQUIRES_FIXED_VERSION now causes a fatal FixedVersionRequired error;
- Added support for the missing `SetExtranoncePrefix` message;
- A few other minor improvements and simplifications.

I would love if you could run this branch pointing to an SV2 pool (perhaps your own if you are using SV2-ui) and then share logs, any observed behavior that seemed odd, all feedback is welcome.
