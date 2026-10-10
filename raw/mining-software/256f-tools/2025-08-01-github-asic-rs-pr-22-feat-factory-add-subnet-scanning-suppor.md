# 256foundation/asic-rs pull request #22: feat(factory): Add subnet scanning support

> Source: https://github.com/256foundation/asic-rs/pull/22
> Collected: 2026-10-07
> Published: 2025-08-01

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 22
- State: closed
- Author: lurkny
- Opened: 2025-08-01
- Closed: 2025-08-04
- Labels: none

## Description

Added in the ability to scan via subnet.

Also added in some cargo options to optimize our release build, reducing binary size by 66%.



## Comments

### s0kil on 2025-08-01

Have some comments regarding scanning:

At Zetta, after much experimentation, we ended up concluding on "2 stage scanning",
During the first stage, scan the subnet, ex: `192.14.1.1-254` with low TCP timeout, 1s, or even less, 500ms.
Once 1st stage scan completes, re-scan the dead hosts, with higher TCP timeout settings, 2-5s, should be configurable.
This process helps deal with network congestion, and ensures that each network scan is consistent.

Something like this, in Scala:
```scala
    def scan2Stage(
        ipAddresses: Seq[IpAddress],
        context: AsicRadarContext
    ): Seq[(IpAddress, Option[Device])] =
        val stage1Results = scan(ipAddresses, context)
        val deadHosts = ipAddresses.filter(ip =>
            stage1Results.exists { case (scannedIp, device) => scannedIp == ip && device.isEmpty }
        )
        val stage2Results = scan(deadHosts, context)
        stage1Results ++ stage2Results
```

### b-rowan on 2025-08-01

@s0kil this is why my thought was just to use the `MinerFactory`, as we can use `with_retries`.  Then the main focus is on making the factory scan very efficient, which it already is because of the way requests are grouped.

The downside of the scan you have as I see it is that it hits the dead hosts multiple times, and guarantees that you are waiting the maximum amount of time on every scan.

### s0kil on 2025-08-01

> @s0kil this is why my thought was just to use the `MinerFactory`, as we can use `with_retries`. Then the main focus is on making the factory scan very efficient, which it already is because of the way requests are grouped.

`with_retries` would essentially be the 2nd stage scan, and we could configure how many retries and timeout config. Sounds good.

### lurkny on 2025-08-01

Changing this to a draft while I convert MinerFactory to use a builder pattern
