# 256foundation/hydrapool pull request #42: Custom, user defined payouts

> Source: https://github.com/256foundation/hydrapool/pull/42
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/hydrapool
- Type: pull request
- Number: 42
- State: open
- Author: keegreil
- Opened: 2026-03-19
- Closed: n/a
- Labels: none

## Description

Work In Progress PR to get an initial "vector check":

This PR aims to make two things possible:

Override the PPLNS defined coinbase payouts with a user defined payout list provided from a local file. If no local filename is given in the config file, then p2poolv2 behavior reverts to default PPLNS.

Get share information from p2poolv2, so that shares meeting a difficulty threshold can be forwarded to an external pool.

This PR is being submitted in conjunction with a PR to p2poolv2.
Every effort was made to minimize changes to the p2poolv2 repository, and to house most of the logic and modifications in Hydrapool.

Remaining tasks:
More thorough debugging and edge case testing
Documentation.



## Comments

### pool2win on 2026-03-19

Hey @keegreil, this looks really nice.

My concern is to merge changes into main.rs. Here is my thinking, let me take your lead and finally build a plugin system for hydrapool payout/accounting mechanisms. I wrote up an issue describing what we want this plugin system to do. I will then take your mechanism and convert it into a plugin and you can then own it from there. How does it sound like a plan..

The issue is here: https://github.com/256foundation/hydrapool/issues/43

### keegreil on 2026-03-19

> Hey @keegreil, this looks really nice.
> 
> My concern is to merge changes into main.rs. Here is my thinking, let me take your lead and finally build a plugin system for hydrapool payout/accounting mechanisms. I wrote up an issue describing what we want this plugin system to do. I will then take your mechanism and convert it into a plugin and you can then own it from there. How does it sound like a plan..
> 
> The issue is here: https://github.com/256foundation/hydrapool/issues/43

That sounds good to me! 

Only reason I selected merge to "main" is I couldn't figure out how to make the PR merge to a tag and I got tired of messing with it. My code was based off the latest tags on both repos, so automerge would work. 

I think the plugin system sounds great, much cleaner and more flexible than my hacked together method. 

Happy to do whatever work I need after the fact to get my stuff working.  

Thanks!
