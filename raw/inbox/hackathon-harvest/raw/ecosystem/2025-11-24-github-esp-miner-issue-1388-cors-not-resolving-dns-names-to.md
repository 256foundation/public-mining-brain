# bitaxeorg/ESP-Miner issue #1388: CORS not resolving DNS names to IPs

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1388
> Collected: 2026-10-07
> Published: 2025-11-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1388
- State: closed
- Author: opacey
- Opened: 2025-11-24
- Closed: 2026-06-22
- Labels: none

## Description

**Describe the bug**
On v2.10.0 and v2.11.0 (at least), AxeOS WebUI is not permitting any config changes when accessed via the devices sub-domain name (e.g. bitaxe.mydomain.net), and yields the following error in the console log (but not in the WebUI):

```
W (1568683) CORS: IP address string is too long: bitaxe.mydomain.net
I (1568684) CORS: Client is NOT in the private ip ranges or same range as server.
W (1568688) httpd_txrx: httpd_resp_send_err: 401 Unauthorized - Unauthorized
```

**To Reproduce**
Steps to reproduce the behavior:
1. Run local DNS and DHCP servers
2. Assign an IPv4 and hostname combo to the bitaxe
3. Access the device via that name: e.g. http://bitaxe.mydomain.net
4. Attempt to edit and save any setting
5. Receive the "401 Unauthorised" error

**Expected behavior**
For the settings changes to be accepted and saved.

**Hardware (please complete the following information):**
 - Bitaxe HW version: BitAxe Gamma 601
 - Bitaxe HW vendor: https://www.thesolomining.co
 - ESP-Miner FW version: v2.11.0, v2.10.0 (tested both)
 - Hash Frequency: Defaults (varies by firmware version)
 - Voltage: 5.1v
 - Pool URL, Port, User: n/a

## Comments

### mutatrum on 2025-11-24

For now it's expected behavior, unfortunately, as we've seen attempts in the wild to update the pool setting through a malicious website, that's why it's locked down to only allow local IP addresses.

The local hostname _can_ work, but that's very dependent on the router, so it's not a proper solution, in some environments it works, and some it doesn't. There's a PR in the works to support mDNS: #1131, which needs to be updated and further tested, but it's definitely on the near future roadmap.

### opacey on 2025-11-24

Oh, I see, thanks for the response. My domainname resolves to a local IP address though, so it should remain compatible shouldn't it? Or do you mean it is internally configured to not try to resolve domain names to IPs?

Either way, would you guys consider making error messages int he GUI more verbose? I had to connect to the USB console via screen to get any more depth than just '401 unauthorised'. I noticed v.2.10.0 has slightly more detail than v2.11.0 has, oddly.

### mutatrum on 2025-11-24

> Oh, I see, thanks for the response. My domainname resolves to a local IP address though, so it should remain compatible shouldn't it? Or do you mean it is internally configured to not try to resolve domain names to IPs?

The second indeed. You have a router that can do it for the device, so do I, but on other router brands that doesn't work. IIIRC it's also dependent on which browser/OS you're accessing the device. The way to solve it is if the Bitaxe firmware itself knows how to do DNS stuff.

> Either way, would you guys consider making error messages int he GUI more verbose? I had to connect to the USB console via screen to get any more depth than just '401 unauthorised'. I noticed v.2.10.0 has slightly more detail than v2.11.0 has, oddly.

Can't remember how it was on v2.10, what extra information would be useful?

### opacey on 2025-11-25

My preference is:
```
Could not save settings. Http failure response for http://bitaxe.mydomain.net/api/system: 401 Unauthorized
> CORS: IP address string is too long: bitaxe.mydomain.net
> CORS: Client is NOT in the private ip ranges or same range as server.
> httpd_txrx: httpd_resp_send_err: 401 Unauthorized - Unauthorized"
```

If that is too much text for the GUI widget perhaps there could be a 'copy error to clipboard' link on the widget which includes the full error text or stack trace?

The error in v2.11.0:
```Could not save settings. Http failure response for http://bitaxe.mydomain.net/api/system: 401 Unauthorized```
...which is pretty ambiguous.


I just loaded up v.2.9.0 and v2.10.0 and they have the same error text - I must have hallucinated the more verbose error in v2.10.0 - sorry.

### Fudmottin on 2025-11-27

I believe I have a similar issue. My router doesn't seem to resolve local hostnames provided to the BitAxe during setup. So
when I try to access the administrative interfaces via Safari, it fails to locate the BitAxes unless I just use the IP which works fine. I tried to work around this problem by adding entries into my /etc/hosts file:

```bash
192.168.0.25   bitaxe1 bitaxe1.local
192.168.0.101  bitaxe2 bitaxe2.local
192.168.0.161  bitaxe3 bitaxe3.local
192.168.0.100  bitaxe4 bitaxe4.local
```

This allows me to pull up the admin page in my browser. The first thing I noticed was the swarm page no longer displayed any of my BitAxes. Scanning wouldn't work. I didn't try any other actions besides checking for firmware updates. I updated from 2.8 to 2.11. No change in behavior.

Am I experiencing a related or the same issue?

### mutatrum on 2025-11-27

You can only access by IP at the moment, when accessing on hostname several things may or may not work, until we have mDNS implemented.

### mutatrum on 2026-06-22

Fixed by #1240
