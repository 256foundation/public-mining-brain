# bitaxeorg/ESP-Miner issue #821: Feat: Disable CORS policy by default, add enable in swarm tab

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/821
> Collected: 2026-10-07
> Published: 2025-04-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 821
- State: open
- Author: benjamin-wilson
- Opened: 2025-04-04
- Closed: n/a
- Labels: none

## Description

I've run across multiple misconfigured private networks with IP ranges outside of the private network range. This does not allow the users to use the device. 

Proposed fix:

Disable all CORS policies ("Access-Control-Allow-Origin", "*") by default. Under the swarm area, everything should be hidden with the option to 'enable swarm' with a short explanation of CORS and disclaimer about the ip ranges. This should show all the existing swarm info and another button to disable.

Looking for feedback from @skot @WantClue @eandersson on the idea.

## Comments

### seepv on 2025-04-14

Is this hard to implement or okayish?

Due to [security issues (Source)](https://github.com/bitaxeorg/ESP-Miner/issues/820) - CORS as an option would be great.

### skot on 2025-04-14

This would make anyone using AxeOS swarm on their network vulnerable to CORS attacks?

### seepv on 2025-04-14

With some simple Javascript, that’s already the case - please [see issue 820](https://github.com/bitaxeorg/ESP-Miner/issues/820).

### skot on 2025-04-14

AFAIK that is not an issue with esp-miner as we only allow requests from local IP addresses. Please lmk if that's not the case?

The issue is then that AxeOS breaks if someone is not using local IP addresses.

### seepv on 2025-04-14

For my understanding, with CORS enabled, it’s possible to access a private IP from an public IP, which would be an major security issue.

Please have a look [here](https://github.com/arendst/Tasmota/issues/6767) for Tasmota Devices with local IPs:

PROBLEM DESCRIPTION

A clear and concise description of what the problem is.

Tasmota has CORS HTTP headers enabled by default. This is a major security issue that could easily be exploited by any website with some simple Javascript, especially since Tasmota does not require a web password by default.
…

TO REPRODUCE

Steps to reproduce the behavior:

1. Make any HTTP request to a Tasmota device (i.e. curl --user username:password --head 192.168.1.100
2. See that Access-Control-Allow-Origin: * CORS header is included as an HTTP response header
3. Go to Tasmota Device Locator
4. See that TDL is able to make arbitrary HTTP requests to every Tasmota device on my network

EXPECTED BEHAVIOUR

A clear and concise description of what you expected to happen.

1. CORS is disabled by default
2. Any public Internet website should not be able to query/enumerate Tasmota devices on my local network

…

ADDITIONAL CONTEXT

Add any other context about the problem here.

It would be very easy to create a script could be dropped into any web page that would:

1. Enumerate every IP in common subnets (192.168.1.x, 192.168.0.x, 10.0.0.x, etc) to discover Tasmota devices
2. Once Tasmota devices have been identified, if they are password protected the script could attempt to bruteforce the password
3. Once a password is discovered, or if the device isn't password protected (default), the site has complete control of the Tasmota device. They can reflash the firmware.
4. By replacing the firmware a malicious actor could:


      i. Setup a proxy server to enable arbitrary access to any local network device (not just Tasmota)
     ii. Push malicious payloads (hacked IP webcam firmware, etc) to local network devices
    iii. Contact a command-and-control service to wait for further instructions

This attack vector could largely be mitigated by making CORS configurable (disabled by default), and requiring a web password to be set when first configuring the wifi. Those that prefer to control their Tasmota devices using HTTP requests could still use that method by using an HTTP password and/or enabling CORS.

### skot on 2025-04-14

We don't use the Tasmota firmware.. Currently we need to have CORS enabled for the Swarm feature to work. To prevent CSRF attacks we only allow requests from the local network; see [is_network_allowed()](https://github.com/bitaxeorg/ESP-Miner/blob/ee6bf8d29623e59773e5ceae5843dc5dc8e8c3fb/main/http_server/http_server.c#L162)  in http_server.c. 

### seepv on 2025-04-14

Similarities between ESP-Miner and Tasmota:

      i. Private IP - both
     ii. No passwords - No PW possible / PW disabled by default
    iii. CORS HTTP headers - always enabled / disabled by default

Would it that bad - to make CORS optional, e.g. enabled / instaed of disabled by default ?
Maybe this CORS issue is beyond my payroll ! - I close issue [820](https://github.com/bitaxeorg/ESP-Miner/issues/820).

### seepv on 2025-04-17

@skot @benjamin-wilson Would it be OK to make CORS configurable, with default —> set to enable ?

In my network - all Sensors, IOTs, Solar and the Bitaxe are in one
PrivatIPSubnet (192.168.x.x) and another PrivatIPSubnet are
for the Phone and a PC.
 
Forwarding ports is possible up to version v2.5.0.

With CORS enabled and v2.5.0 the Bitaxe-Homepage is read only.
(Tasmota Devices are also read only.)

To update the Bitaxe or Tasmota-Firmware I have to switch Networks.

Versions greater v2.5.0 does not allow forwarding between PrivatNetworks anymore.

‘CORS as an option’ would help very much.

### skot on 2025-04-17

it's my understanding that this should work on AxeOS.. what is the IP range of your Phone and a PC subnet?

### seepv on 2025-04-17

That’s great news - yes with v2.6.5 Port-Forwarding is working again -
with v2.5.1 it does not - I should have tested it with v2.6.5 beforehead.
Thanks for your reply and the Bitaxe.

### skot on 2025-04-18

#853 is related to this

### snotrauk on 2025-04-30

@seepv -   @skot is correct. The CORS issue is mitigated on esp-miner because it checks the origin header in the cross site request to ensure it comes from a private IP. 

All websites can use JavaScript (or simple forms) to make cross site requests, this is the basis of Cross-Site Request Forgery (CSRF) attacks. The difference with an overly permissive CORS configuration is that this allows the JavaScript to read the response, So if often more impactful as an attacker can also extract sensitive information.  

But esp-miner checks the origin header which mitigates both CSRF and CORS issues, as the request is denied. Technically it is still vulnerable to malicious code hosted on a webserver on your internal network, but that would be a very strange situation and the current fix is easiest option that doesn’t require adding some sort of authentication. 

This makes be suspect that Tasmota is vulnerable to CSRF attacks similar to https://nvd.nist.gov/vuln/detail/CVE-2025-27579 if they also don’t use authentication and don't check the origin header or have some other form of CSRF protection.
