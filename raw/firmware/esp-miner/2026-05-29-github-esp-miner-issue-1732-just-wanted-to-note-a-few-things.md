# bitaxeorg/ESP-Miner issue #1732: Just wanted to note a few things

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1732
> Collected: 2026-10-07
> Published: 2026-05-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1732
- State: closed
- Author: mrv777
- Opened: 2026-05-29
- Closed: 2026-06-20
- Labels: Feedback

## Description

Ran a little security check and a few things got mentioned I thought I would just pass along:

- /api/theme bypasses the normal network gate and has unsafe type handling. Unlike other API handlers, it does not call is_network_allowed(). POST also accepts unvalidated JSON types and can pass NULL into string handling.
- OTAWWW erases Axe-OS before validating www.bin. A bad or zero-length upload can wipe/corrupt the UI partition before failure is detected.
- Production frontend dependencies have known high CVEs. npm audit --omit=dev reports 9 high vulnerabilities in Angular/PrimeNG packages.

## Comments

### WantClue on 2026-05-30

Thank you for letting us know, taking a look into that if any of these actually are exploitable. 

### mutatrum on 2026-05-30

> Ran a little security check and a few things got mentioned I thought I would just pass along:
> 
> * /api/theme bypasses the normal network gate and has unsafe type handling. Unlike other API handlers, it does not call is_network_allowed(). POST also accepts unvalidated JSON types and can pass NULL into string handling.

See #1637, not sure if anything is already fixed there?

> * OTAWWW erases Axe-OS before validating [www.bin](http://www.bin). A bad or zero-length upload can wipe/corrupt the UI partition before failure is detected.

Ideally we should have a 2nd partition for www as well. No idea if this is feasible.

> * Production frontend dependencies have known high CVEs. npm audit --omit=dev reports 9 high vulnerabilities in Angular/PrimeNG packages.

First step is #1651 which fixes quite a few. Idea is to keep upgrading, as Angular 19 is also EOL.

### mutatrum on 2026-06-20

First point: #1759
Second point: #1763 aka the best part is no part.
Third point: #1651
