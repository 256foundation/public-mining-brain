# FAQ: Braiins OS Licensing (Braiins Academy)

> Registry ID: braiins-os
> Source: https://academy.braiins.com/braiins-os/faqs/license (markdown captured via /braiins-os/faqs/license.md llms route)
> Collected: 2026-10-10
> Published: n/d (docs site build 2026-10-02, sitemap lastmod 2026-10-04)
> Posture: verbatim
> As-Of: 2026-10-10

# FAQ: Braiins OS Licensing

## Braiins OS Licensing

### Is Braiins OS usage subject to a license?

Yes, it is. License agreement is available [here](https://braiins.com/os/plus/license).

### How can I determine the version of Braiins OS I am using?

To determine the version of Braiins OS you're using, you have multiple options. You can check the software version information provided in the user interface of the software.

Additionally, you can pull this information via Braiins API, see [here](https://github.com/braiins/bos-plus-api), or use other tools such as Braiins Toolbox, see [here](https://braiins.com/toolbox/), to access the version information.

### Where can I find the detailed terms of the Braiins OS license?

Detailed terms and conditions for the Braiins OS license can be found on our official [website](https://braiins.com/os/plus/license).

It's recommended to review these terms before using Braiins OS.

### How does the new licensing of Braiins OS (version 23.04 and newer) work?

The new licensing system for Braiins OS version 23.04 and newer operates as follows:

Before mining operations begin, each mining device undergoes a process of license acquisition. This involves the device contacting a **license server**, which is responsible for generating a time-limited license based on the provided device information. Once the device successfully obtains the license, it gains authorization to initiate mining activities.

During the mining process, the appropriate dev fee is credited to Braiins. Licenses obtained by devices are automatically renewed every **60 minutes**. This system benefits from geographically distributed license servers, enhancing reliability and minimizing latency for miners.

In cases of connection interruptions or any unforeseen issues with our infrastructure, it's important to note that the acquired licenses remain valid for a duration of 12 hours. This ensures uninterrupted mining operations throughout this extended period, despite potential disruptions.

However, should a situation arise where a license becomes invalid or fails to be acquired initially, the mining device will trigger a penalty mechanism. This penalty involves the device's **hashrate being reduced by an x%**, as outlined in the license agreement. This mechanism aims to incentivize consistent connectivity and compliance with the licensing requirements while maintaining a fair balance between the interests of miners and Braiins.

### What is the fee for the license?

The fee is defined in the [license agreement's](https://braiins.com/os/plus/license) section 5.

### What is the licensing server?

The licensing server is a dedicated server infrastructure that operates on specific URLs, which are determined based on geolocation. Its primary function is to generate time-limited licenses for **Braiins OS version 23.04 and newer**.

Once a mining device acquires a license from the licensing server, it is then authorized to commence mining operations, with the appropriate development fee credited to Braiins. To connect to the licensing server and obtain a license, miners need to establish connections to URLs following the `*.braiins.com` pattern.

It's important to note that the licensing server pertains exclusively to licenses for Braiins OS versions 23.04 and newer.

### What are the common issues related to Braiins OS licensing?

There are typically two types of problems that users might encounter with Braiins OS licensing:

#### 1. Connection and URL Access Issues

It's important to ensure that both your miners and the Braiins Farm Proxy (if used) can reach URLs with the mask `*.braiins.com`. Furthermore, ensure that port `3336` is allowed for both license and developer fee connections. If you're setting up with a Farm Proxy, additional ports `443` and `3338` need to be allowed as well.

If you continue to experience problems with Braiins OS licensing after checking these factors, please don't hesitate to reach out to our [support team](https://help.braiins.com/en/support/tickets/new) for further assistance.

### What happens if the miner(s) can't connect to the licensing server to obtain the license?

If the license is not acquired, mining will commence without the license. However, it's important to note that in this scenario, the miner will incur a penalty in the form of hashrate reduction, as defined by the [license agreement](https://braiins.com/os/plus/license).

### What happens if a miner with an obtained license loses connection to the licensing server?

In the event that a miner with a valid license experiences a connection interruption or encounters issues with our infrastructure.

It's important to note that the licenses for **Braiins OS version 23.04** and newer remain valid for a duration of **12 hours**.

This ensures uninterrupted mining operations during this specified timeframe.

However, if a license becomes invalid, the mining device will start to incur a reduction in hash rate, as defined in the [license agreement](https://braiins.com/os/plus/license).


---

Was this helpful?

Yes, thanks!Sort of, thanks!Not really

Talk to us!
