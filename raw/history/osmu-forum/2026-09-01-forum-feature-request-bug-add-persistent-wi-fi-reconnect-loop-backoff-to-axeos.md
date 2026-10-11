# Feature Request / Bug: Add persistent Wi-Fi reconnect loop / backoff to AxeOS

> Source: https://osmu.xyz/t/feature-request-bug-add-persistent-wi-fi-reconnect-loop-backoff-to-axeos/80
> Collected: 2026-10-10
> Published: 2026-09-01
> Registry ID: osmu-forum

infotech452564 | 2026-09-01 21:10:48 UTC | #1

**Feature Request / Bug: Add persistent Wi-Fi reconnect loop / backoff to AxeOS**

**Issue description:** When there is a power outage, my Wi-Fi router takes a few minutes to fully boot up and broadcast the network again. However, the Bitaxe boots up much faster. If it doesn’t find the Wi-Fi network immediately upon startup, it gives up, gets stuck in AP mode (“host wifi”), and stops trying to connect.

Because of this, after every power flicker, the Bitaxe remains offline indefinitely until I manually hard-reset (power cycle) the device.

**Suggested Solution:** Could the ESP firmware be updated to include a continuous reconnection loop, a longer connection timeout window, or a periodic retry backoff timer (e.g., retry connecting to Wi-Fi every 30–60 seconds indefinitely) instead of permanently falling back to AP mode when the initial boot connection fails? This would make unattended deployment much more reliable after power outages.

-------------------------

WantClue | 2026-09-29 21:09:38 UTC | #2

Thank you for reporting this issue, i’ll open a github issue about it to keep track of it.
