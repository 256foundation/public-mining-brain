# bitaxeorg/ESP-Miner issue #233: Add support for mDNS to have pretty dashboard URL

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/233
> Collected: 2026-10-07
> Published: 2024-06-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 233
- State: closed
- Author: skot
- Opened: 2024-06-19
- Closed: 2026-06-22
- Labels: enhancement

## Description

ESP-IDF apparently [supports mDNS](https://docs.espressif.com/projects/esp-idf/en/v5.2.2/esp32s3/api-reference/protocols/mdns.html) which would potentially allow us to have the the AxeOS dashboard have a URL like `bitaxeAB02.local` instead of the IP address.

I suggest using the last 4 hex digits of the WiFi MAC address appended (like we do for the setup AP SSID) so that there are not problems with multiple Bitaxe on the same network. Of course if there is a better way to do this, that would be awesome too.

## Comments

### skot on 2024-06-19

@tbd3 maybe you'd be interested in looking into this?

### mutatrum on 2024-06-20

What's the difference between this and #165? I can access the dashboard with the hostname configured.

### skot on 2024-06-20

Really? Can you access AxeOS from your browser with `http://<hostname>.local`? Or something else besides the IP?

### mutatrum on 2024-06-20

Yes, I set the hostname, restart and it works:

![image](https://github.com/skot/ESP-Miner/assets/56344102/3f9e71cd-34ed-494f-8fb1-b90cc8b3b08c)

![image](https://github.com/skot/ESP-Miner/assets/56344102/2d026d26-da82-44d9-8922-99602be0c29c)

Same for API access:

![image](https://github.com/skot/ESP-Miner/assets/56344102/e528910a-d3f4-4164-8bcd-0928ff9041e4)


### skot on 2024-06-20

🤯 what is this network magic!? Mine doesn't work like that.

### mutatrum on 2024-06-20

Always has been? I can access all my devices by their hostnames on my LAN.

Two things I can think of: my main machine is a linux machine, maybe that's better with these things? But AFAIK this also works from the Windows machines in the house, and it also works from mobile phones. Second thing I can think of is I have the router as DNS (192.168.1.1) so that will resolve locally first, and only forwards to an external DNS when that fails. But isn't that is totally standard? Do you access everything on your LAN by IP?

![image](https://github.com/skot/ESP-Miner/assets/56344102/71323be6-ae5f-4f2d-bdcb-cc4c2860f358)

### pixeldoc2000 on 2024-06-20

@skot 
The Firmware (esp) send its hostname with the DHCP Request to the Router.

If the Router DHCP Server update the DNS Server of the Router, the Hostname will be resolved to the device IP. But this depends on the Router to implement it.

![grafik](https://github.com/skot/ESP-Miner/assets/376715/384f37c0-a213-4418-8488-3e98e5d02b2a)

mDNS work independently via broadcast. Having mDNS may be nice to have, but I think there are more important issues to fix before getting into creature comfort stuff?



### skot on 2024-06-20

Ah, I did not have my router as DNS on this machine. Changed and it works! pretty cool. I did not know you could do that.

As @pixeldoc2000 says, this is not universal, so we probably can't remove the IP from the screen.

Definitely a nice-to-have feature for future. You're right there are other pressing issues.

### skot on 2024-06-20

We should prolly set the default hostname to `bitaxeXXXX` with X being the last 4 of the WiFi MAC

### KillerInk on 2025-04-21

with mdns you can report services(http) to the network you have running on that device.
so if some ask for all http services in the network that device answers too.
its also possible to create a own service.

that would also avoid to scan the full network range for the swarm page

https://github.com/bitaxeorg/ESP-Miner/blob/e31043b8b4330063a9886cdc8931515ce053aaa1/main/http_server/axe-os/src/app/components/swarm/swarm.component.ts#L109

instead of that you could just ask the network for a "bitaxe" service.
or if it reports as plain http service, it then show up too on windows networktab as a http device where you can double click it to open the webpage


its just a few lines
```

#include "mdns.h"

mdns_init();
mdns_hostname_set("BitaxeXXXX");
mdns_instance_name_set("BitaxeXXXX");
mdns_service_add("BitaxeHttp", "_http", "_tcp", 80, NULL, 0);
```

greets

### skot on 2025-04-21

> with mdns you can report services(http) to the network you have running on that device.
> so if some ask for all http services in the network that device answers too.
> its also possible to create a own service.
> 
> that would also avoid to scan the full network range for the swarm page
> 
> https://github.com/bitaxeorg/ESP-Miner/blob/e31043b8b4330063a9886cdc8931515ce053aaa1/main/http_server/axe-os/src/app/components/swarm/swarm.component.ts#L109
> 
> instead of that you could just ask the network for a "bitaxe" service.
> or if it reports as plain http service, it then show up too on windows networktab as a http device where you can double click it to open the webpage
> 
> 
> its just a few lines
> ```
> 
> #include "mdns.h"
> 
> mdns_init();
> mdns_hostname_set("BitaxeXXXX");
> mdns_instance_name_set("BitaxeXXXX");
> mdns_service_add("BitaxeHttp", "_http", "_tcp", 80, NULL, 0);
> ```
> 
> greets

This sounds amazing. Want to submit a PR? Make sure it's against the dev-latest branch. We'll need to test to make sure this doesn't break our Swarm/CORS strategy.

I'd sure love to stop showing IP addresses on the display and show a mdns hostname instead.

### KillerInk on 2025-04-22

well the c part is not the big problem^^
im not realy familiar with node/js, but i can give it a try.

also this fails if there is no dns server and network runs on fixed ips or upnp broadcast is disabled.
in that cases the try and error approach is better.
also its possible todo a reverse lookup to get the hostdns, wich is the easier approach maybe, because it only affects node.js side.
this would then happen after a bitaxe ip got found and should not break the swarm/core strategy.
except in my case where all bitaxes have the same hostname and i get routed to last one logged to the network^^


### KillerInk on 2025-05-18

after yesterdays townhall this seems obsolete^^ at least the swarm part. mdns itself is still a nice feature
