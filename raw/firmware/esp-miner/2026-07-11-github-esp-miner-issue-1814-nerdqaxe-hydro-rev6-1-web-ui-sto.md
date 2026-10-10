# bitaxeorg/ESP-Miner issue #1814: NerdQAxe++ Hydro Rev6.1 - Web UI stops working after ~48 hours while mining continues (JS files truncated)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1814
> Collected: 2026-10-07
> Published: 2026-07-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1814
- State: closed
- Author: ZwarteHenk
- Opened: 2026-07-11
- Closed: 2026-07-12
- Labels: none

## Description

Hardware:
- Black Triangle NerdQAxe++ Hydro Rev6.1 (AliExpress)
- Hydro version
- ~5 TH/s

Firmware tested:
- v1.0.36
- v1.0.37.2 LTS

Problem:

After approximately 48 hours the Web UI stops working.

Mining continues normally:
- Shares continue to submit.
- Public Pool shows normal hashrate.
- OLED display continues updating.
- ICMP ping continues working.

Only the normal Web UI fails.

Observations:

- http://IP/recovery works perfectly.
- index.html loads successfully.
- runtime.js, polyfills.js, main.js and styles.css never finish loading or are transferred incompletely.

Chrome DevTools:

Network:
- index.html = HTTP 200
- JS/CSS requests remain Pending or incomplete

Console:

Uncaught SyntaxError: Unexpected end of input

polyfills.js

Uncaught SyntaxError: Unexpected end of input

main.js

This indicates the javascript files are truncated during transfer.

Power cycling the miner immediately restores the Web UI.

After approximately another 48 hours the issue returns.

Things already tried:

- Full erase flash
- Reflash using official Web Flasher
- Keep Configuration disabled
- Browser cache cleared
- Different browser
- Phone and PC tested
- Ping verified
- Recovery page verified

The problem is completely reproducible.

It appears the HTTP file server stops serving larger static assets after long uptime while mining itself continues normally.

<img width="3072" height="4080" alt="Image" src="https://github.com/user-attachments/assets/2e1dba10-646a-4813-8ca0-f39a6da9554f" />
<img width="3072" height="4080" alt="Image" src="https://github.com/user-attachments/assets/9627a3bb-e285-4330-8870-dc3f8ef729cd" />
<img width="3072" height="4080" alt="Image" src="https://github.com/user-attachments/assets/9f997e38-59f2-4e97-acdb-28894eb4559a" />
<img width="3072" height="4080" alt="Image" src="https://github.com/user-attachments/assets/4000df14-1ff0-4d65-9ce9-b87db21c3c53" />

<img width="1080" height="2410" alt="Image" src="https://github.com/user-attachments/assets/d6b2c672-217d-493f-8ef6-7485cddfb962" />

## Comments

### ZwarteHenk on 2026-07-11

The last screenshot is after hard Reboot (unplug 12v).

### bonifacio123 on 2026-07-12

I believe issues for that device should be posted here instead:  [https://github.com/shufps/ESP-Miner-NerdQAxePlus/issues](https://github.com/shufps/ESP-Miner-NerdQAxePlus/issues).

### ZwarteHenk on 2026-07-12

Thanks I have posted it there now.  Should I delete this post?

### bonifacio123 on 2026-07-12

I think so since this area is for AxeOS issues
