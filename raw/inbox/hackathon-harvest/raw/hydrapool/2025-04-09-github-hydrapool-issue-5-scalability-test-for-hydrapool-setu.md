# 256foundation/hydrapool issue #5: Scalability test for hydrapool setup to test up to 1000 stratum clients

> Source: https://github.com/256foundation/hydrapool/issues/5
> Collected: 2026-10-07
> Published: 2025-04-09

- Repository: 256foundation/hydrapool
- Type: issue
- Number: 5
- State: closed
- Author: pool2win
- Opened: 2025-04-09
- Closed: 2026-03-19
- Labels: testing

## Description

(no description)

## Comments

### pool2win on 2025-10-29

We need to run this again with a whole lot of accounting and payout changes.

### adamdecaf on 2025-11-04

I threw some hashrate at the test instance today from a few workers and everything seemed to perform well. The best diff was only 2.67G (when I had a bitaxe hit 3.47G), but the test seemed to be a success.

<img width="1116" height="382" alt="Image" src="https://github.com/user-attachments/assets/44773e61-2536-41b1-bb51-576ca00941f7" />
<img width="1104" height="232" alt="Image" src="https://github.com/user-attachments/assets/c9ee2a0a-9fe4-4088-baf9-1473597f8a8f" />

### pool2win on 2026-03-02

@adamdecaf  - big thanks for sharing your results 

### pool2win on 2026-03-19

Closing this as we did a fair amount of optimisations during the Jan 26 telehash. We'll revist this once we update to latest p2poolv2 libs before next telehash.
