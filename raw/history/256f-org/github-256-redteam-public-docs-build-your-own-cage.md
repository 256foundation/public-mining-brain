# 256foundation/256-RedTeam-Public: docs/build-your-own-cage.md

> Source: https://github.com/256foundation/256-RedTeam-Public/blob/HEAD/docs/build-your-own-cage.md
> Collected: 2026-10-07
> Published: Unknown

# Build your own red-team cage

A practical build guide for humans **and their agents** who want to audit Bitcoin-mining
firmware the way the 256 Red Team does: on real hardware, in an isolated, fully observed
environment. Written 2026-09-13 from our live deployment — everything in sections 1–2 and
4 is what we actually run (the deployed state is infrastructure-as-code in our internal
lab repo; the inline configs below are taken from it verbatim). Anything we have *not*
yet deployed ourselves is explicitly marked **RECOMMENDED**.

The core idea, in one line:

> **The miner is the untrusted device.** Treat every miner in the cage like a malware
> detonation box: it can do anything it wants *except* reach the real internet unobserved,
> and you must be able to cut its power without touching it.

---

## 0. Design principles (read this before buying anything)

1. **Isolation with a choke point.** One router sits between the miners and everything
   else. Every packet, DNS query, and NTP request crosses it — or a box you control.
2. **Total observability.** Full-payload packet capture, DNS query logging, and
   protocol-level share accounting. "Trust but verify" is useless here: only verify.
3. **Remote power control.** kW-class heaters that can be switched off from your desk,
   per-outlet, with power metering. You will need this more often than you think.
4. **Reach-in without exposure.** You can reach the cage from anywhere; the cage can
   reach nothing of yours, and nothing of yours is exposed to the internet to make it
   happen.
5. **Agents analyze, humans touch hardware.** A safety policy that splits every operation
   into *always safe* (read-only, offline) and *attended-only* (anything that can change
   fans, clocks, voltage, flash, or process state) is not bureaucracy — miners are 3 kW
   space heaters with network services, and a bad automated action is a fire or a brick.

---

## 1. Separate the cage from your existing network

### 1.1 Why a hard separation

- Miners run closed-source firmware that phones home, auto-updates, and (as our findings
  show) contains default credentials, unauthenticated APIs, and anti-tamper mechanisms.
  You do not want that on the LAN with your laptops, NAS, and cameras.
- Your test tools (hostile pools, fake update servers, fuzzers) are attacks on the *DUT*.
  You equally do not want them leaking toward production devices — including other
  miners you own.
- Mining firmware behaves differently depending on what it can see. A cage gives you a
  reproducible network environment: same DNS, same NTP, same egress policy every run.

Do **not** just put the miners on a guest SSID or an existing VLAN and call it a day. You
need a router *you fully control at the OS level*, because the whole point is MITM and
traffic manipulation on the miner's path.

### 1.2 What router: a general-purpose Linux box, not a consumer router

**What we use: a Raspberry Pi Compute Module 5 (CM5)** on its IO board, running Debian 13
(trixie), two NICs:

- `eth0` — onboard CM5 NIC → **cage LAN**, static `10.66.0.1/24`
- `eth1` — USB3 Gigabit Ethernet adapter → **uplink**, DHCP from an isolated VLAN on the
  existing home router (UniFi UDR7). This is the *management* path; we never reconfigure it.

Why a Linux box beats a consumer/prosumer router for this job:

| Capability | Why it matters | Consumer router |
|---|---|---|
| Full shell, install anything (mitmproxy, Zeek, tcpdump, custom responders) | The router is also the **inline MITM/capture point** | limited/no packages |
| dnsmasq DNS + DHCP with full query logging | DNS logs are the cheapest beacon detector there is | closed UI, weak logs |
| nftables you can generate from templates | Egress policy flips (`allow` ↔ `restricted`) per test | CLI/UX per vendor |
| Infrastructure-as-code (Ansible) | Idempotent re-config between tests; auditable; agents can operate it safely | config in a web UI |
| Can run the VPN/subnet-router itself | One box = router + VPN entry + capture | needs extra devices |

Acceptable alternatives if you don't want a Pi:

- **OPNsense/pfSense on any 2-NIC mini-PC** — best firewall UX, packages for capture.
- **OpenWrt on decent x86 or an aging AP** — same Linux flexibility, smaller footprint.
- Any **managed switch with a SPAN/mirror port** on the cage side so a separate capture
  host can see all traffic without being inline.

The Pi CM5 has been plenty for a cage of ~10 devices at line-rate capture with a ring
buffer; it also sips power and has no moving parts.

### 1.3 The services the cage router must provide

Our checklist (all implemented in our Ansible `lab_router` role):

- **DHCP** for the cage, with a dynamic pool (we use `10.66.0.50–200`) and **static
  reservations per device MAC** — every miner, Shelly, and AP keeps a stable IP forever.
  Stable IPs are what make packet filters, logs, and agent playbooks readable.
- **DNS** — the router resolves *all* cage DNS first, logs every query
  (`log-queries` → `/var/log/dnsmasq-lab.log`), then forwards upstream. Unexpected
  domains in that log are your cheapest compromise/beacon signal. Block outbound 53/853
  to anything else in restricted mode.
- **NTP** — the router serves time (`dhcp-option=option:ntp-server,<router>`). Miners are
  fanatical about NTP; a time server you don't expect showing up in pcaps is a finding.
- **Firewall + NAT (nftables)** — forward policy `drop` by default; explicit allow for
  LAN→WAN (open mode) or a tight allowlist (restricted mode); tailnet interface → LAN
  allowed for reach-in (see §4).
- **Gateway-only LAN side**: the cage LAN interface serves DHCP/DNS/NTP; the WAN side is
  never touched by configuration tooling.

Our dnsmasq cage config, abridged (this is our actual template):

```ini
# bind to the cage LAN only; the uplink never sees DHCP from here
interface=eth0
bind-dynamic
no-dhcp-interface=eth1

# all cage DNS resolves here first — that's the point — then forwards upstream
no-resolv
server=192.168.3.1        # upstream resolver on the uplink VLAN
domain=cage.256rt
local=/cage.256rt/

dhcp-range=10.66.0.50,10.66.0.200,255.255.255.0,12h
dhcp-option=option:router,10.66.0.1
dhcp-option=option:dns-server,10.66.0.1
dhcp-option=option:ntp-server,10.66.0.1
dhcp-authoritative

# red-team observability: every DNS query + DHCP transaction logged
log-queries
log-dhcp
log-facility=/var/log/dnsmasq-lab.log
```

Egress policy is a single Ansible variable, which is what makes per-test lockdown cheap:

```bash
# lock the cage to DNS + one pool's stratum/API ports
ansible-playbook site.yml -e egress_policy=restricted \
  -e '{"restricted_allow": ["tcp dport { 3333, 4028 }"]}'
```

### 1.4 Topology

```
 Internet ── home router (VLAN-capable, e.g. UniFi UDR7)
                │  isolated VLAN for the lab uplink (no route to your main LAN)
                ▼
        [WAN/eth1, DHCP 192.168.3.10]
        cage router — Raspberry Pi CM5, Debian
          · dnsmasq DHCP+DNS+spoofing hooks (query/DHCP logging)
          · nftables firewall + NAT, egress policy switch
          · Tailscale subnet router (reach-in, §4)
          · optional inline MITM/redirect (§5.3)
        [LAN/eth0, 10.66.0.1/24]
                │
        cage switch (managed, SPAN if possible)
        ├── miners / bare control boards   10.66.0.50+
        ├── Shelly power devices           10.66.0.119/143/161
        └── WiFi AP (bridged, no DHCP)     10.66.0.164
```

### 1.5 WiFi inside the cage

You will want WiFi in the cage for power devices and sensors — running mains-rated
Ethernet to every outlet is unnecessary. **We use a standalone Ubiquiti UAP-AC-M**
(`10.66.0.164`), configured as a plain WPA2 / 2.4 GHz AP that **bridges clients untagged
onto the cage LAN** — the AP runs *no* DHCP of its own; the cage router hands out
addresses. Any dumb-but-solid 2.4 GHz AP in "access point / bridge" mode works. 2.4 GHz
matters: most smart-relay/sensor hardware (Shellys included) is 2.4 GHz only.

Keep the SSID and PSK cage-unique. This is not your home WiFi — it's the detonation
network's wireless edge, and the Shellys on it are the least-hardened devices in the cage.

### 1.6 Configuration discipline (this saved us repeatedly)

- **Infrastructure-as-code.** All router config is Ansible (`lab_router` + `tailscale`
  roles), idempotent, re-runnable, reviewed like code. Agents converge the box to the
  declared state instead of hand-editing.
- **Safety asserts inside the automation.** The role *refuses to run* if the LAN NIC's
  MAC doesn't match the expected onboard NIC, and asserts LAN ≠ WAN before touching
  anything. Configure the wrong interface once and you've locked yourself out of a
  remote site.
- **Never reconfigure the WAN/management path from the automation.** It is the road home.
- **Name the interface roles, not just the cables** (`lan_interface`/`wan_interface`
  variables) and pin a stable NetworkManager connection UUID for the LAN.
- Verify after every apply: `ip -br addr`, `nft list ruleset`, `tail dnsmasq-lab.log`,
  and the DHCP lease table.

---

## 2. Power: Shelly devices (metering + remote cut)

### 2.1 Exactly what we use

| Device | Model / SKU | Firmware | Role in our cage |
|---|---|---|---|
| **Shelly Pro 2PM** | `SPSW-202PE12UL` | 1.7.5 | 2-channel metered relay — switches the **PSU feed of a full miner** on channel 0, plus a test load |
| **Shelly Pro 4PM** | `SPSW-204PE16EU` | 1.7.5 | 4-channel metered relay — test-bench power for devices under test |
| **Shelly Pro 4PM** | `SPSW-204PE16EU` | 2.0.0 | 4-channel metered relay — **auxiliary power only** (never the running miners) |

Buy the same SKUs or the local-mains equivalent (Pro series comes in EU/UL variants —
check your voltage). The "Pro" DIN-rail family is what you want: per-channel **power
metering** plus per-channel **relays**, local API, no cloud dependency. If your
electrician prefers wall-outlet control, the Shelly Plus/Pro 1PM/2PM class with the same
local RPC API works per-outlet too.

### 2.2 Why Shelly

- **Local HTTP JSON-RPC (Gen2 API)** — no cloud account required, no dependency on the
  vendor's servers for anything you do in the lab:

  ```bash
  curl http://10.66.0.119/rpc/Shelly.GetDeviceInfo
  curl http://10.66.0.119/rpc/Shelly.GetStatus          # per-channel watts, volts, temps
  curl -X POST http://10.66.0.119/rpc/Switch.Set \
       -d '{"id":0,"on":false}'                          # cut channel 0
  ```

- **Per-channel power telemetry** is a test instrument: miner PSU draw, standby draw,
  inrush on boot, and the "did the firmware actually idle the boards?" question are all
  a `GetStatus` away.
- **Cheap enough to dedicate** one channel per miner PSU, one per bench supply, one for
  the cage router + AP itself.
- WiFi (2.4 GHz) — pairs with the cage AP in §1.5; reservations give them stable IPs.

**Killing the cage router's own power with a Shelly** is a deliberate trick: if you
remotely brick the router's config mid-test, you can power-cycle it without driving to
the site. Put the router + AP + switch on Shelly-fed outlets, and keep one *manual*
override path (physical switch at the cage) — never let "the network is down and so is
the power control" happen.

### 2.3 Wiring and safety notes

- Mains wiring = electrician or a competent human. Dedicated circuit for the miners
  (they're 3+ kW); Shelly Pros are DIN-rail devices that belong in/beside the cage's
  distribution box or an enclosure.
- **Auth on the Shellys is off in our cage.** That is acceptable *only because* the cage
  is isolated and the WiFi is cage-unique. If you expose Shellys anywhere else, enable
  auth and updated firmware.
- **Remote power-cycling a hashing miner is attended-only** in our safety policy: cutting
  PSU power mid-write or mid-flash is brick territory, and the fans/thermal envelope are
  part of the risk. Cutting *standby* loads, bench supplies, or the router/AP is fine
  unattended.
- Log every Shelly into DHCP reservations with a name that says what it *feeds*, not
  where it sits (`shelly-pro2pm` feeds miner X's PSU on ch0 — the name should survive the
  next re-plug).

---

## 3. Eyes and ears: cameras, microphones, environmental

> **Status in our cage:** partially deployed. A standalone smoke detector in the miner
> room is **required by our safety policy and present**; networked cameras/microphones
> are **RECOMMENDED — not yet deployed in our cage** (they're on the roadmap). Everything
> in this section is recommendation + design intent, labeled as such.

Miners fail audibly and visibly long before they fail safely: a fan bearing changes its
pitch, a hashboard LED stops blinking, a PSU whines, something smells hot. Remote eyes
and ears turn "I think it died last night" into "I watched it die at 02:14."

**RECOMMENDED baseline:**

- **Camera with RTSP/streaming**, pointed at the miners' status LEDs and fans — e.g. a
  PoE IP camera (Reolink / UniFiProtect class) powered from the cage switch, or a plain
  USB webcam on the capture host. Goal is *evidence-grade* clips on state change, not a
  surveillance system: motion/sound-triggered recording, retained a few days.
  Bridge it onto the cage network (§1.5) or a dedicated monitoring VLAN; treat the camera
  itself as IoT — firmware updates, unique password, no cloud.
- **Microphone** for acoustic monitoring. The cheapest reliable pattern: a USB microphone
  on the capture host + a cron/systemd timer computing a loudness/spectrum baseline —
  fan-stop or bearing-death is a step-change in the noise floor (miners run ~75 dB, so
  *silence* is the anomaly). Alert on deviation, keep rolling audio clips.
- **Smoke detection** — non-negotiable regardless of monitoring: a smoke detector in the
  miner room (a networked one that can push an alert is a plus; a standalone one is the
  floor). Miners are 3 kW of sustained current in a box.
- **Temperature/humidity** in the cage — a Shelly Plus/BLU HT or any local temp sensor;
  ambient drift catches cooling failures before the miners do.

Two rules that keep monitoring gear from becoming its own attack surface:

1. **Monitoring devices live on the cage side** (or a separate monitoring VLAN) — never
   on the network the miners are attacking *from*. A compromised miner must not be able
   to pivot into your camera NVR.
2. **One-way visibility.** The cage must not be able to reach the camera's admin
   interface just because the camera can see the cage. ACL it.

---

## 4. Remote access: Tailscale (WireGuard mesh)

### 4.1 The pattern we run

The **cage router itself is the Tailscale node** — a *subnet router* advertising the cage
prefix. Nothing in the cage gets a tailnet identity; the tailnet simply has a route to
`10.66.0.0/24` through the router:

```
your laptop / ops server ── tailnet ──▶ redteam-cage-router (subnet router, 10.66.0.0/24)
                                          └──▶ cage devices directly
```

- Install Tailscale from its official repo, then:
  ```bash
  tailscale up --advertise-routes=10.66.0.0/24 --hostname=<cage-router-name> \
               --accept-routes=false
  ```
- **Approve the subnet route** in the Tailscale admin console (Machines → node →
  Edit route settings) unless auto-approval is on.
- The nftables ruleset allows `tailscale0 → cage LAN` explicitly, so the tunnel and the
  firewall are configured as one reviewed unit.
- **Auth keys are one-time and never committed** — passed at first bring-up from a
  gitignored secrets file, deleted after the node registers.
- Restrict with ACLs which tailnet hosts may reach `10.66.0.0/24` (in our case: the ops
  server and the operator's machines — not every node on the tailnet).

This gives you SSH, HTTP, APIs, and pcap pulls to every cage device from anywhere,
with **zero inbound ports** on your home router and no exposure of the cage to the
internet.

### 4.2 The `accept-routes` footgun (learned live)

On the cage router, keep `--accept-routes=false`. If the router *accepts* routes
advertised by other tailnet nodes — e.g. a node advertising your home/management subnet —
its return traffic can get pulled into the tunnel and you lose SSH to the very box you
manage everything through. Recovery (from another tailnet node):
`ssh -J <ops-node> <router> 'sudo tailscale set --accept-routes=false'`.

### 4.3 Joining our tailnet vs. building your own

For a team building their own cage, **create your own separate tailnet** — it's free,
takes ten minutes, and keeps your blast radius independent of ours. Connect to our
environment (if we collaborate) via **Tailscale node/app sharing** of the specific
machines that need to talk — not by merging infra. If you'd rather not depend on
Tailscale the service, a plain WireGuard tunnel from an ops box to the cage router is the
same shape with more manual config; the architectural point is *reach-in without
exposure*, not the vendor.

---

## 5. The rest of the build (what makes it a lab, not just an isolated VLAN)

### 5.1 Capture host

- A small PC (or the router itself for light duty) running a **rotating tcpdump ring
  buffer** (ours: ~200 × 100 MB) on the choke point or a
  **SPAN/mirror port** from the cage switch.
- **Zeek** on top for structured `conn`/`dns`/`ssl`/`http` logs — grep-able, agent-friendly.
- Retain pcaps per firmware-version baseline window; hash and archive with the firmware
  inventory. Compress; they get big.

### 5.2 Controlled pool infrastructure

- A **Stratum proxy that parses and logs every JSON-RPC message** (ours: HashScope, 256
  Foundation) between miner and pool — this is the primary anti-skimming instrument: any
  share not going to your configured worker is visible.
- A **local pool** (ours: HydraPool) as the pool of record; keep one test pointed at a
  real public pool with a sacrificial worker — some firmware behaves differently when it
  can't reach "real" pools.

### 5.3 MITM capability (why the router choice matters)

Because you own the router OS and the DNS path, you can — per test — redirect or
intercept nearly anything:

- **DNS redirection**: fake/controlled answers for a domain (update servers, fee pools,
  telemetry endpoints) via dnsmasq `address=`/host entries.
- **Transparent HTTP(S) interception**: mitmproxy in transparent mode, or a redsocks-style
  redirect, for vendor desktop tools and cleartext/weak-TLS channels. Several vendor
  update chains we tested do not verify signatures or pin TLS — that's exactly the kind
  of finding this setup surfaces (and it's a *finding about the vendor*, not a license to
  attack strangers).
- **Port-level redirect/rewrite** for protocol fuzzing (hostile pool ↔ miner) with the
  real service still observable in the capture.

### 5.4 Start with bare control boards, not full miners

A **full miner** (hashboards + PSU) hashes, heats, and risks; a **bare control board**
(same board, no hashboards/PSU connected) draws a few watts and is completely safe to
leave powered unattended. In our experience the majority of red-team work never needs
hashboards at all — and you can parallelize a bare-board bench across vendors and
firmware versions at a fraction of the cost, power, and risk of a rack of live miners.

**Bare control board is enough for (most of the backlog):**

- **Firmware work**: acquiring and unpacking images, binwalk/Ghidra analysis, bootloader
  and partition-layout exploration, UART/recovery boot, flash dumps. This is offline or
  board-local — nothing here cares whether hashboards exist.
- **Management-plane testing**: web UI, authentication, API/CGI endpoints, privilege
  boundaries, config backup/restore, factory-reset behavior, persistence checks.
- **OTA and update paths**: the fetch side, manifest/signature validation, downgrade
  behavior — intercepted at the router (§5.3). Several vendors' update chains fail to
  verify signatures; you find that on a bare board.
- **Network behavior**: DHCP/DNS/NTP handling, egress telemetry and hardcoded
  phone-home endpoints, port scans of the board's own listeners.
- **Pool/Stratum protocol work**: the control board runs the mining protocol — you can
  capture and fuzz subscribe/authorize handshakes against a hostile pool with no hashing
  hardware attached. (Caveat: firmware with zero hashrates attached may skip or error
  parts of the mining pipeline, and you get no share-submission traffic — see below.)

**You need real hashboards attached for (a much shorter list, attended-only):**

- **Thermal and fan behavior**: fan-curve control, temperature-sensor readings,
  missing-fan/over-temp faults, throttling. A bare board has no fans or hashboard temp
  sensors to exercise, and firmware behaves differently without them.
- **Hashboard-side RE**: the control-board↔hashboard link protocol, hashboard EEPROMs
  (I2C), and the firmware on the hashboards' own micros. None of that exists on a bench
  of bare boards.
- **Anything that only manifests under load**: watchdog resets while hashing, memory/CPU
  pressure during active mining, race conditions that need the mining pipeline hot.
- **Measured-performance and fee/skim verification**: hashrate reporting vs. actual
  work submitted, frequency/voltage/power-mode behavior, hidden-fee skimming analysis
  against a controlled pool. A bare board subscribes to the pool but submits no shares —
  measuring *shares* requires hashing.
- **Tests that need the miner to "boot happy"**: some firmware refuses to fully start
  the mining pipeline (or error-spams) without hashboards present. If your test needs a
  normally-running miner rather than a normally-running control plane, it's a full-miner
  test.

We run both: bare boards for breadth, a few full miners for thermal/load/skimming work,
with the full-miner PSU feeds on Shelly channels (§2).

### 5.5 Bench kit (for when software access ends)

3.3 V USB-UART adapters (FTDI/CP2102) + jumper leads, multimeter, SD cards + reader
(recovery boot on Amlogic/Zynq), I2C reader for hashboard EEPROMs, and — sacrificial
units only — hot-air station / NAND reader for chip-off. Rule of thumb from our playbook:
UART first, always; 3.3 V only; photograph boards before/after any rework; log every
flash dump with its SHA256.

### 5.6 Safety policy (steal ours, then enforce it with automation)

- **Always safe (unattended):** offline analysis, read-only device probes (API
  *read* groups, SSH reads, MTD dumps), passive capture, router-side firewall changes.
- **Attended-only (human within fire-extinguisher range):** anything that can change fan
  speed, clock/voltage, flash contents, or process state — fan control, frequency/voltage,
  OTA writes, config-mutating CGI/API calls, hostile-pool fuzzing, process kills, reboots.
- Required guards: thermal watch via read-only API before/during/after (abort at ≥ 80 °C
  or fans < ~3000 RPM while hashing), reversion step documented *before* the test, one
  change at a time, sacrificial unit designated in writing before flash/boot work, smoke
  detector, dedicated circuit, electrical-rated fire extinguisher.
- Learn this lesson early: **"read-only" is per-endpoint, not per-HTTP-verb.** We once
  triggered a config rewrite + reload from a *bodyless GET* on a factory CGI. Verify side
  effects from the decompile/firmware before probing, don't infer from the method.

### 5.7 Operating rules for agents (copy this into your AGENTS.md)

If an AI agent will work in your cage, make these binding for it:

1. **Read before write.** Team context (`AGENTS.md`), the safety policy, and the device
   inventory are mandatory reading every session.
2. **No live attacks without an operator instruction that names the target IP.** Agents
   analyze pcaps/images/dumps freely; they do not scan, fuzz, or poke devices on their own.
3. **Unattended-safe list only** when no human is present (see §5.6). Unsure = not safe.
4. **No exfiltration.** Firmware images, dumps, and credentials stay on your systems.
   Hashes may go to external services; full images never.
5. **Disclosure is human-gated.** Agents draft; humans verify and contact vendors.
6. **Evidence or it didn't happen.** Affected version + SHA256, repro steps, artifact
   references, confidence label (`confirmed | probable | suspected`), and `UNVERIFIED`
   tags on anything unverified.
7. **Infrastructure-as-code with safety asserts** (§1.6) is what makes it *safe* to let
   an agent reconfigure the lab network: the automation refuses wrong-interface
   changes, validates configs before applying, and converges idempotently.
8. **Update the plan and inventory** when work completes — the repo should be more
   indexed after every session than before.

---

## 6. Bill of materials — what we actually run

| Item | What we use | Notes |
|---|---|---|
| Cage router | Raspberry Pi CM5 + IO board, Debian 13 | 2nd NIC via USB3 GbE adapter; dnsmasq + nftables + Tailscale, Ansible-managed |
| Upstream router | UniFi UDR7 (existing home router) | any VLAN-capable router; lab uplink on its own VLAN |
| Cage switch | UniFi USW Flex 2.5G | any switch; managed + SPAN preferred |
| Cage WiFi AP | Ubiquiti UAP-AC-M (standalone) | WPA2 2.4 GHz, bridges untagged, no DHCP of its own |
| Power control | Shelly Pro 2PM `SPSW-202PE12UL`, 2× Shelly Pro 4PM `SPSW-204PE16EU` | per-channel metering + relays; local Gen2 HTTP API |
| DUTs | 3 full miners (S19-class: LuxOS / ePIC / Mujina+Nova) + 5 bare control boards (Mara, ePIC, stock S21, BeagleBone S19j Pro, Braiins BCB100) | bare boards = safe 24/7 targets; full miners = attended |
| Capture/ops | Dedicated ops server (Hetzner) + Mac bench | Zeek/tcpdump/Ghidra/binwalk/mitmproxy on the bench; ops server joins the tailnet |
| Remote access | Tailscale subnet router on the cage router | §4 |
| Safety | Smoke detector, electrical-rated extinguisher, dedicated circuit | non-negotiable |
| Bench | 3.3 V USB-UART adapters, multimeter, SD cards, I2C EEPROM reader | §5.5 |

(Rough, useful budgets: the entire non-miner infrastructure above is well under
$1,500 new; a single bare control board or used full miner is often the pricier part.)

## 7. Build order (checklist)

1. Pick the room: dedicated circuit, airflow plan, no carpet, extinguisher, smoke alarm.
2. Flash/prepare the router OS; install Ansible roles; **assert the MAC before applying**;
   bring up DHCP/DNS/NTP/nftables; verify from a laptop on the cage LAN.
3. Carve the lab uplink VLAN on the home router; plug the router WAN into it; confirm no
   route between main LAN and cage LAN.
4. Wire the cage switch + AP; bridge the AP untagged, no DHCP; join it to the cage.
5. Electrician wires the Shellys (miner PSU feeds, bench power, router/AP power); join
   them to the cage WiFi; DHCP-reserve each with a name that says what it *feeds*.
6. Bring up Tailscale on the router (`--advertise-routes`, `--accept-routes=false`);
   approve the route; ACL which tailnet nodes may reach the cage.
7. Add devices **one at a time**: reserve its MAC, watch its DHCP/DNS in the log, start a
   capture baseline (7 days per firmware version is our target).
8. Add pool infrastructure (Stratum-logging proxy + local pool) in the capture path.
9. Write the safety policy doc; wire the unattended/attended lists into your agents'
   instructions; only then scale to full miners.
10. Keep the whole config in git. If it isn't in the repo, it isn't real.

---

## About the 256 Red Team

The 256 Red Team audits Bitcoin-mining firmware and pool infrastructure for hidden
fees, backdoors, share-skimming, anti-tamper mechanisms, and undocumented failure
modes — mixing human expertise with AI agents under a strict safety policy. This
guide is the first public release; sanitized findings, harnesses, and agent playbooks
will follow in this repo. Deeper material (device inventory, the full safety policy,
the hardware-access playbook) lives in our internal repo and will be published here
as it is reviewed for release.
