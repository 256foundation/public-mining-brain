# dvb-WarpPool — open-source solo mining pool written in Rust (Umbrel / macOS / Windows / Linux)

> Source: https://osmu.xyz/t/dvb-warppool-open-source-solo-mining-pool-written-in-rust-umbrel-macos-windows-linux/39
> Collected: 2026-10-10
> Published: 2026-06-10
> Registry ID: osmu-forum

dvb-projekt | 2026-06-10 21:21:47 UTC | #1

**dvb-WarpPool — open-source solo mining pool written in Rust (Umbrel / macOS / Windows / Linux)**

I’d like to introduce dvb-WarpPool, a Bitcoin solo pool written from scratch in Rust, made for self-hosting. The idea: if you’re chasing the lottery block with a NerdMiner, Bitaxe, NerdQaxe or Avalon Q, you don’t have to send your shares to a public solo pool — your own node builds the block templates, and when a block hits, the coinbase output already carries your wallet address. No middleman, no pool fee, no sign-up.

Under the hood: Stratum V1 (plain + TLS) and Stratum V2 with NOISE handshake, persistent VarDiff, getblocktemplate + ZMQ for millisecond job refresh, hardware detection with profile recommendation, and a SvelteKit PWA dashboard with live updates in 8 languages — now with freely sortable and collapsible cards (drag & drop, optionally saved as the default for all visitors). Plus block-found alerts via Telegram/Discord/ntfy/Slack/email/web push, and energy tracking including PV integration (Anker Solix, Home Assistant): on solar surplus the electricity price automatically drops to 0, and the kWh history splits solar and grid shares.

Easiest install is the Umbrel Community App Store (your own Bitcoin node required); alternatively signed packages for macOS/Windows/Linux or a multi-arch Docker image. Security: 2FA, Argon2, audit log, security audit, reproducible builds, Cosign-signed artifacts with SLSA attestation, currently 860+ tests.

Licensed MIT/Apache-2.0 — feedback and issues welcome on GitHub: [GitHub - dvb-projekt/dvb-WarpPool: Rust Bitcoin Solo Mining Pool — Stratum V1+V2, PWA operator UI, signed multi-arch releases · GitHub](https://github.com/dvb-projekt/dvb-WarpPool)

-------------------------

dvb-projekt | 2026-06-12 23:31:00 UTC | #2

**dvb-WarpPool — a solo mining pool that treats your hardware like it knows it**

**dvb-WarpPool is an open-source, self-hosted solo Bitcoin pool in Rust** — one binary in front of your own Bitcoin Core, from a single Bitaxe to a 1,000-miner shed. 100% of a found block goes to the address your miner authorizes with. No custody, no payout ledger, no account.

**The heart of it is VarDiff that actually knows mining hardware.** The pool reads your miner’s user agent and starts every device in the right league — eight classes from Antminer-grade iron down to a NerdMiner V2, which gets sub-1 difficulty *from the first second* instead of starving at diff 1, plus deliberately lazy retargeting so its display isn’t constantly reset. Difficulty survives reconnects **and pool restarts** (persisted per worker), converges with an EMA plus hysteresis instead of jumping around, and never moves more than 4× per step. Your miner gets a say too: `suggest_difficulty` seeds the session, `d=8192` in the password pins it — both safely clamped to the device class. And if a worker goes quiet because its difficulty ended up too high, a guarded idle decay walks it back down instead of stranding it forever — built by someone who filed the downward-crush bug against another pool and made that failure mode structurally impossible here.

**Speaks everything your fleet does.** Stratum V1, V1 over TLS (working out of the box, with a guided Let’s Encrypt setup for friends mining from outside), and Stratum V2 with the current 2024 handshake spec — verified live against the Bitaxe and NerdQAxe families, with share responses around 15 ms.

**Built to stay up.** Multiple Bitcoin Core nodes via `[[node.backup]]`: sub-second failover when the primary dies, automatic return when it’s back, block events taken from whichever node reports first — and a found block is submitted to **all** nodes in parallel, because that’s the one moment a dead node could cost real money. In load tests, 1,000 concurrent miners ran against the daemon at under 50 MB RAM and about a third of one CPU core.

**Nice to live with.** A PWA dashboard in 8 languages with background push to your phone, block alerts your whole friends group can subscribe to (one shared ntfy topic — no accounts), per-device telemetry for Bitaxe/Antminer/Avalon/Whatsminer, energy and solar tracking, and an admin cockpit instead of config-file archaeology. Install from the Umbrel app store, a signed-checksums release (.dmg, .msi, .deb/.rpm, AppImage) or multi-arch Docker — reproducible builds with SBOM included. 900+ tests run before every release.

**The honest part:** solo mining is a lottery — this pool makes the ticket-buying pleasant, not the odds better. The project is young; no mainnet block found yet (that’s how solo works at home scale). macOS/Windows binaries aren’t store-signed yet. Everything else is in the open: code, tests, benchmarks, and a handbook that documents the limitations too.

:link: [GitHub - dvb-projekt/dvb-WarpPool: Rust Bitcoin Solo Mining Pool — Stratum V1+V2, PWA operator UI, signed multi-arch releases · GitHub](http://github.com/dvb-projekt/dvb-WarpPool) · Handbook: [Introduction - dvb-WarpPool](http://dvb-projekt.github.io/dvb-WarpPool)

-------------------------

dvb-projekt | 2026-06-15 17:02:58 UTC | #5

**dvb-WarpPool — update: hardening & operations (v1.4.0)**

*New here?* dvb-WarpPool is an open-source, self-hosted Bitcoin **solo** mining pool — written in Rust, with a full operator web UI (PWA, 8 languages), built for mixed home hardware: NerdMiner next to Bitaxe next to Avalon. Stratum V1/V2/TLS, device telemetry, energy & solar tracking, signed builds for macOS/Windows/Linux/Docker/Umbrel.

This update shifts the focus from *breadth* to *operations* — what a solo pool needs to run continuously, and occasionally exposed to the open internet:

**One profile switches the whole pool.** Small/Medium/Large/Enterprise now apply everything *live*: VarDiff range, connection cap, data retention, poll intervals, rate limits. No restart — and the Hardware table honestly marks each value as live, restart-only, or advisory.

**Abuse protection that leaves your home network alone.** Internet scanners that hammer the connect limit are now auto-banned — escalating (5 min → doubling → up to 1 h), before the TLS handshake even happens. Loopback and LAN are *never* banned, so your NerdMiner can reconnect in a loop. Plus a manual block list (admin API + UI) and per-IP limits on connect, auth, and the HTTP API.

**Strong miners get the right difficulty.** Avalon Q, S19, Whatsminer & co. used to be capped artificially; now each hashrate class gets its proper range — stable difficulty, less waste.

**Monitoring out of the box.** The Prometheus `/metrics` endpoint now also exports the aggregate pool figures — pool and network hashrate, best share, active wallets, active bans — ready for Grafana, with recipes in the handbook.

**Under the hood:** a fuzz-hardened Stratum parser, 939 tests before every release, signed and reproducible artifacts.

Still honest: no mainnet block yet — the project is young.

-------------------------

dvb-projekt | 2026-06-18 01:27:51 UTC | #6

**dvb-WarpPool v1.4.2 — the setup wizard now speaks your language**

This one is deliberately small — polish where newcomers look first:

**The first-run wizard is now fully bilingual (DE/EN).** A few cards — hardware detection, the Bitcoin Core health check and its warnings, the connectivity overview — still slipped through in German even with the UI set to English. They’re now fully translated, switching the language updates every card live, and `?lang=de` / `?lang=en` lets you deep-link straight into a locale.

**One-click update works again.** `dvb-warppool-cli download-update` and the “Install update” button in the admin area used to fetch the wrong asset names and fail every time. They now recognise the real release packages, extract the daemon binary from the tarball and swap it in cleanly — with the signature verified against `SHA256SUMS`.

**Otherwise as solid as before:** one profile switches the whole pool live, auto-ban against internet scanners (your LAN is spared), Prometheus `/metrics` for Grafana, a fuzz-hardened parser, 952 tests before every release, signed and reproducible artifacts.

Still honest: no mainnet block yet — the project is young.

-------------------------

dvb-projekt | 2026-06-18 01:29:06 UTC | #7

**dvb-WarpPool v1.4.3 — the all-time best-shares board now shows the real top hits, and the wizard speaks 8 languages**

**The “All-time” best-shares board now shows the absolute top hits.** Until now every miner was capped at 10 entries in the shared table — so a single strong miner could never hold more than 10 of the 50 leaderboard slots, even when it genuinely produced the highest shares. The all-time view now reads from a dedicated, globally-ranked table with no per-worker cap, reflecting the true ranking: if one miner holds the top 50, that’s exactly what you see. The “Per-worker” view (one row per miner) and the best-share overlay on the hashrate chart stay unchanged on purpose. Existing best shares are carried over automatically on upgrade.

**The setup wizard now speaks all 8 languages.** After going bilingual in v1.4.2, it now adds Spanish, Portuguese (BR), French, Italian, Japanese and Chinese — the same language set as the dashboard. The picker is a clean dropdown (flag + native name, like the dashboard) rather than a row of buttons, the browser language is auto-detected, and `?lang=<code>` deep-links straight into any locale.

**Otherwise as solid as before:** one profile switches the whole pool live, auto-ban against internet scanners (your LAN is spared), Prometheus `/metrics` for Grafana, a fuzz-hardened parser, 956 tests before every release, signed and reproducible artifacts.

Still honest: no mainnet block yet — the project is young.

-------------------------

dvb-projekt | 2026-06-18 04:01:04 UTC | #8

**dvb-WarpPool v1.4.5 — the setup wizard now opens with an animated intro**

- **Animated warp intro on first-run setup.** The wizard opens with a short vortex clip, then fades into setup (respects reduced-motion).
- **Calmer dashboard.** The “API unreachable” notice no longer flashes on a brief network blip — it only shows after repeated failures.

Already on board: an 8-language setup wizard with a dropdown picker, an all-time best-shares board showing the real top hits, live profiles, auto-ban against internet scanners, Prometheus `/metrics`. No mainnet block yet (the project is young).

-------------------------

dvb-projekt | 2026-06-18 08:10:24 UTC | #9

**dvb-WarpPool v1.5.0 — a full-screen screensaver turns any always-on monitor into a pool dashboard**

- **New full-screen screensaver for wall & kiosk displays.** After a configurable idle time the dashboard fades into a seamlessly looping WarpPool clip with a live stat bar: best share (plus the worker that found it), hashrate, active miners, blocks found, and version/update status — with a “LIVE” badge and a ticking uptime. Any input (mouse/key/touch) brings the dashboard back.
- **Configurable per device** via a new “Display” menu in the top bar: on/off, idle timeout (5/10/15/30 min), stats overlay. Off by default, respects reduced-motion (a static still instead of video).

Already on board: an animated setup intro, an 8-language setup wizard with a dropdown picker, an all-time best-shares board showing the real top hits, live profiles, auto-ban against internet scanners, Prometheus `/metrics`. No mainnet block yet (the project is young).

-------------------------

skot | 2026-06-18 22:24:10 UTC | #10

This sounds wild! I assume vibe coded? How long did it take you? I’m impressed by the feature list

-------------------------

dvb-projekt | 2026-06-19 04:44:45 UTC | #11

Hi skot,

thank you very much for your feedback.

It’s been about four weeks of intensive work with Claude to implement all my ideas for WarpPool.

The goal was to create the best and most secure BTC solo pool available today—one that eliminates the drawbacks and limitations of existing pools and provides users with maximum support during setup and operation.

The pool was designed primarily for home mining, but also includes an extension for the commercial sector.

I think Claude and I have succeeded quite well in this. The performance metrics speak for themselves.

-------------------------

dvb-projekt | 2026-06-19 06:28:18 UTC | #12

**dvb-WarpPool v1.6.0 — a clear license (AGPLv3) + an optional legal notice for public operators**

- **New license: AGPLv3** (previously MIT/Apache). For self-hosters **nothing changes** — running your own pool stays free. The switch just keeps improvements open and stops anyone from closing off a proprietary commercial fork. A separate commercial license is available for proprietary use.
- **Optional Terms/Privacy footer for public & commercial operators.** If you run a pool for others, you can configure your own Terms-of-Use and Privacy-Policy links — the dashboard then shows a “By connecting … you agree …” notice. **Off by default** (solo setups don’t need it).

Already on board: a full-screen screensaver for wall displays, an animated setup intro, an 8-language wizard with a dropdown, an all-time best-shares board, live profiles, auto-ban against internet scanners, Prometheus `/metrics`, Stratum V2/TLS. No mainnet block yet (the project is young).

-------------------------

dvb-projekt | 2026-06-19 09:49:48 UTC | #13

**dvb-WarpPool v1.7.0 — outbound webhooks + read-only API tokens for your own add-ons & automations**

- **Outbound webhooks.** The pool can now POST pool events (block found, health, …) as JSON to your own URL — wire it into a script, a custom backend, or a no-code tool (Zapier etc.). HMAC-signed for verification, off by default. A push complement to the existing SSE live stream.
- **Read-only API tokens.** Hand an add-on or dashboard a read-only token — even if it’s compromised, it can’t reconfigure the pool (least privilege).
- **Add-on handbook chapter.** Covers the clean sidecar boundary (a separate process, not linked-in code), the stable interface contract, and the API-stability promise — for anyone building their own extensions.

Already on board: AGPLv3 + commercial option, optional legal footer, full-screen screensaver, animated setup intro, 8-language wizard, all-time best-shares board, auto-ban, Prometheus, Stratum V2/TLS. No mainnet block yet (the project is young).

-------------------------

dvb-projekt | 2026-06-20 10:44:18 UTC | #14

**dvb-WarpPool v1.8.0 — fewer false rejects: a VarDiff grace window for Stratum V1 + V2**

- **VarDiff grace window.** When the pool raises a miner’s difficulty, shares the device had already computed against the old (looser) target were briefly “in flight” — and were wrongly rejected as “low difficulty”, adding up to a few percent “rejected” / “shares above target” on busier miners. The pool now keeps accepting those in-flight shares for a short transition window. **Fixed on both protocols — Stratum V1 and V2.**
- **Honest reject stats.** The dashboard’s rejected-shares total now reflects the real rate instead of always showing 0 — and is now tracked for Stratum V2 too (previously not at all).
- **`download-update --tag`.** Self-update can now target a specific release — pin to a known-good version or roll back off a bad one.

For context: your **solo block chances were never affected** — block candidates are checked against the network target, not the pool target. This was about share accounting, VarDiff accuracy and the miner-side reject display. No mainnet block yet (the project is young).

Already on board: outbound webhooks + read-only API tokens, AGPLv3 + commercial option, legal footer, full-screen screensaver, 8-language wizard, all-time best-shares board, auto-ban, Prometheus, Stratum V2/TLS.

-------------------------

dvb-projekt | 2026-06-20 17:52:21 UTC | #15

**dvb-WarpPool v1.8.1 — smoother VarDiff: no more difficulty overshoot after a reconnect**

- **VarDiff overshoot fixed.** After a reconnect the pool’s difficulty estimate lagged and chained big jumps far past the optimum while ramping up, then swung back — visible as a wildly jittering hashrate curve on the miner display plus a short burst of rejects. The estimate now recalibrates at *every* step and lands straight on the optimum: calm display, fewer reconnect rejects, one stable difficulty instead of constant oscillation.
- Under the hood: the share-interval EMA is scaled by the difficulty ratio at each retarget (standard VarDiff practice) — applies to **Stratum V1 and V2** at once, since both share the same VarDiff engine. Live-verified: the same config that overshot to ~10× the optimum now settles cleanly.

For context: your **block chances were never affected** — this was purely difficulty stability, display and share accounting. Builds on v1.8.0 (which removed the grace-window rejects at difficulty changes); together VarDiff now runs smooth. No mainnet block yet (the project is young).

Already on board: VarDiff grace window (v1.8.0), outbound webhooks + read-only API tokens, AGPLv3 + commercial option, full-screen screensaver, 8-language wizard, all-time best-shares board, auto-ban, Prometheus, Stratum V2/TLS.

-------------------------

dvb-projekt | 2026-06-21 14:34:38 UTC | #16

**dvb-WarpPool v1.9.0 — best-share trail on the chart: a continuous peak line across the full 24 hours**

- **Best-share dots over time.** The amber dots on the hashrate curve now show the highest real share difficulty in each time slice — a continuous trail across the whole 24-hour window. Previously the overlay drew from the best-share leaderboard table (per-worker top-N), which ages out of the 24 h window for established workers — so it ran nearly empty, showing only the small fresh personal-bests of the weakest devices. Now your strong miners stay visible the whole way, in the real G/T range (the behaviour goPool’s chart already had). The best-share **list** is unchanged.
- Under the hood: each 1-minute bucket records its highest *actual* hash difficulty (not the VarDiff plateau) and serves it via the hashrate API; the frontend draws the dots from that (downsampled to 160, highest per slice). Also drops one API call per dashboard refresh.
- **Also:** the right-hand axis labels no longer get clipped on narrow phone screens.

For context: a display/UI feature only — the mining path and your block chances are untouched. After updating, the trail fills in over the first ~24 h, since the peak data is recorded going forward. No mainnet block yet (the project is young).

Already on board: smooth VarDiff with no reconnect overshoot (v1.8.0/v1.8.1), outbound webhooks + read-only API tokens, AGPLv3 + commercial option, full-screen screensaver, 8-language wizard, all-time best-shares board, auto-ban, Prometheus, Stratum V2/TLS.

-------------------------

dvb-projekt | 2026-06-22 10:53:28 UTC | #17

**dvb-WarpPool v1.10.0 — standards-compliant block construction, BIP-54-ready ahead of activation**

- **BIP-54-forward-compatible coinbase.** The coinbase now carries an enforced block-height timelock (`nLockTime = height-1`, `nSequence = 0xfffffffe`) — exactly what the upcoming **Consensus Cleanup soft fork (BIP-54)** will require. The block stays valid under **today’s** rules (the lock is always already satisfied when mining `height`) and is **ready for activation** at the same time. Future-proof, nothing to configure.
- This rounds out the already **standards-compliant** block construction: BIP-34 coinbase height, SegWit witness commitment, BIP-310 version-rolling (overt ASICBoost). Those three are table stakes for any serious pool — being **BIP-54-forward-compatible** is (as far as I can tell) not yet common.
- Applies to **Stratum V1 and Sv2** alike (shared coinbase build). **Verified end-to-end against a regtest block** accepted by Bitcoin Core.

For context: a correctness / future-proofing feature only — your block chances are unchanged. No mainnet block yet (the project is young).

Already on board: best-share peak trail on the chart (v1.9.0), smooth VarDiff with no reconnect overshoot (v1.8.x), energy + solar tracking, outbound webhooks + read-only API tokens, AGPLv3 + commercial option, full-screen screensaver, 8-language wizard, per-miner telemetry, Stratum V2/TLS.

-------------------------

dvb-projekt | 2026-06-23 07:01:13 UTC | #18

**dvb-WarpPool v1.11.0 — a calmer VarDiff: less difficulty flapping for mixed home hardware**

This release targets one concrete home-mining annoyance: the constant `set_difficulty` churn that makes ESP32 miner displays (NerdMiner et al.) flicker.

- **Poisson significance gate (on by default).** VarDiff now re-targets only when the deviation is **statistically significant** for the number of shares seen, instead of reacting to every excursion past a fixed band. A low-rate miner’s observed share-rate is Poisson-noisy (~1/√N); a fixed hysteresis band reads that noise as a real hashrate change. The gate holds until the change is real — a genuine hashrate change still clears the band promptly. Opt out with `significance_gate = false`.
- **`suggest_difficulty` is a starting hint again, not continuous control.** Devices (NerdMiner/NerdNOS) that re-send the same below-floor request every ~90 s used to trigger a `set_difficulty` each time. No more.
- **Avalon Q detection fix.** An Avalon Q reports the generic `cgminer` user-agent, so it was misclassified as Bitaxe and capped ~5× too low; detection now consults the worker name.

**Verified live** on an 8-miner Box: NerdMiner ~17 → **0** re-targets/h, 6 of 7 device classes **−46…−88 %**, **0 rejects**.

Honest framing: this is **display calm / smoothness**, not a hashrate or earnings difference. Versus ckpool/public-pool/mkpool, those run a **fixed hysteresis band** rather than a significance test, and on none of them does the converged difficulty survive a **pool restart** — on dvb-WarpPool it does (source-checked). Other pools (e.g. goPool) do have Poisson-aware VarDiff too — no superiority claimed there.

-------------------------

dvb-projekt | 2026-06-23 13:29:23 UTC | #19

**dvb-WarpPool v1.12.0 — Stratum V2 miners reach VarDiff parity with V1, plus a robustness pass**

This release implements the full VarDiff/robustness backlog from the last review — three thrusts:

- **Stratum V2 miners get full VarDiff parity.** Direct Sv2 miners used to run a hard-coded default VarDiff. They now use the same engine as V1: your `[vardiff]` operator config, the same **idle-decay** walk-down when a miner goes quiet, and their **best-/lucky-share** stats recorded for the leaderboard. One shared VarDiff engine for both protocols — no second code path lagging behind.
- **Robustness pass.** Share writes are now **atomic** (one transaction per share instead of ~14 separate fsyncs → consistent tables, less I/O). The config is **validated at startup** (no sub-60s retention TTLs, no `hysteresis_ticks = 0`). The worker table is protected against **unbounded growth** via client-controlled worker names (idle workers are evicted after the TTL, block-finders are kept forever). And the **ntime lower bound** from the block template is now enforced — it was dead (hard-coded 0), so only the upper bound applied.
- **Admin saves preserve your comments.** Editing the config from the UI no longer strips the hand-written comments/formatting from your `config.toml` (via `toml_edit`).

Honest framing: this is **feature parity, data integrity and convenience** — not a hashrate or earnings difference. V1-only operators mainly feel the hardening (atomic writes, startup validation); operators with direct Sv2 miners now get the same VarDiff quality they had on V1. Hot-path regtest-smoke-tested, 1018 tests green, reproducible build as always.

-------------------------

dvb-projekt | 2026-06-24 16:29:53 UTC | #20

**dvb-WarpPool v1.12.1 — Stratum V2 miners mine reject-free: the stale-share bug is gone**

One concrete bug in direct Stratum V2 miners — and its clean fix:

- **The problem.** A solo pool pushes a fresh mining job roughly every 30s to fold in new mempool transactions (same previous block, just a better template). A direct Sv2 miner (NerdQAxe family, NerdAxeGamma, or a Bitaxe over Sv2) submits a share in the brief window right after such a refresh — still on the job that was current when it started hashing it — which is valid work. But the Sv2 server only remembered the **single newest** job and rejected everything else as “stale”. V1 never had this: it always kept a short history of recent jobs. The Sv2 path was missing exactly that.
- **The fix.** The Sv2 server now keeps a short rolling **job history** (like V1). Every submitted share is validated — proof-of-work reconstruction included — against **the exact job it was built on**, not just the newest one. A genuine new block is still detected (via the previous-block-hash change) and correctly purges the old jobs, so truly stale shares after a block change are still rejected.
- **The result, measured live.** On the test box a NerdAxeGamma went from **~13% rejected shares to 0%** — over a 10-minute window, pool and firmware counters in lockstep (+37 accepted / 0 rejected each). As a side effect the **VarDiff starvation** stops: previously the wrongly-rejected shares were dragging the miner’s difficulty into free-fall.

Plus three small things: an **ntime acceptance window** on the Sv2 path (a share’s timestamp is checked against a sane window), a retention-config fix, and a bit of UI polish (the “LIVE” indicator no longer flickers on every event — 3s debounce).

Honest framing: this is a **correctness fix for direct Sv2 miners**, not a hashrate gain. Your miner always did the same work — what’s new is that its valid shares get **credited** again instead of thrown away, the accepted/rejected counters are accurate, and VarDiff stays stable. V1-only operators are unaffected (V1 always did this right). If you run NerdQAxe-/Bitaxe-class hardware over Stratum V2, this is the release to take. Hot-path regtest-smoke-tested, 1020 tests green, reproducible build as always.

-------------------------

dvb-projekt | 2026-06-24 19:39:58 UTC | #21

**dvb-WarpPool v1.12.2 — the energy dashboard stays fast even after months of solar data**

A small, honest performance patch — relevant if you run your **solar/PV system** alongside the pool:

- **The problem.** With solar tracking enabled, the energy dashboard splits consumed energy into “solar” vs. “grid”. The query behind it joined a per-minute solar table to the miner telemetry on a *computed* key — which SQLite could only resolve as a nested-loop full scan. After a few months of PV history that took **several seconds per call**, and the dashboard runs it on a ~30s cadence → the log filled with “slow statement” warnings.
- **The fix.** The split now runs as a **correlated per-bucket query**, driven off the telemetry and backed by the solar table’s primary-key index. Result: **hundreds of times faster** (the hourly daily-rebuild ~2000×), and the computed kWh figures are **byte-identical** — only the speed changes, not a single number.

Honest framing: a pure **performance fix for solar pools** — no new feature, no hashrate or earnings effect, no behaviour or config change. If you **don’t** use solar tracking you were never affected and see nothing change (the solar table is empty). If you do run PV, your energy dashboard is snappy again and your log is quiet. 1021 tests green, reproducible build as always.

-------------------------

dvb-projekt | 2026-06-25 16:22:57 UTC | #22

**dvb-WarpPool v1.13.0 — access controls for your Stratum endpoint, built-in backups, and explorer links**

This release is all about **operations & hardening** — every piece optional and off by default:

- **Decide who may mine.** Four new, individually toggleable gates: a **payout-address allowlist** (only your own addresses may mine), an **IP allow/deny gate** over CIDR ranges, a **per-IP connection limit**, and an **automatic ban** for a worker that keeps sending rejected shares. Your local network and the pool UI are never affected. Nothing changes for solo-at-home use — these gates are for anyone opening their pool to others, or who just wants one more layer of defense.
- **Built-in scheduled backups.** The pool can now write its own periodic backups on a schedule (with a retention count) — no external cron, no script needed. Off by default; enable it under `[backup]`.
- **One-click block lookups.** Found-block hashes and heights now link straight to a block explorer (mempool.space by default, fully configurable) — one click instead of copy-pasting into a search bar.

Honest framing: a pure **operations & hardening** release. None of these features touch your hashrate or your block chances, and none is on by default — change nothing and you have exactly the pool you had before. 1037 tests green, reproducible build as always.

-------------------------

dvb-projekt | 2026-06-29 09:15:11 UTC | #23

**dvb-WarpPool v1.14.0 — finally see WHY shares get rejected (per worker, V1 + V2)**

A small but practical release: **per-worker reject reasons.**

- **The problem.** Until now you only saw a bare number per miner: “X rejected shares”. Whether those came from stale shares at block/job changes, from a too-high difficulty, from ntime drift, or from a real misconfiguration — invisible. A reject rate without the reason is a black box.
- **What’s new.** `/api/workers` now returns a per-worker **breakdown by reason** (`stale-share`, `low-difficulty`, `invalid-ntime`, `duplicate-share`, … including the Sv2 pre-checks like `job-not-found`), sorted by frequency — for **both** protocols, Stratum V1 and V2. In-memory and additive: the share-validation logic itself is **unchanged**; it only **labels** the reject that was already counted.
- **Why it helps.** The trigger was a concrete case: a NerdAxe (Sv2) showed “over 5% rejects” in its miner software. Measured, pool and miner counters were in exact lockstep (no discrepancy), and the rate was a decaying **reconnect effect** after box updates — no bug, no money impact. Telling exactly that apart — a benign reconnect blip vs. a real misconfiguration — is what the reason breakdown now makes obvious at a glance.

Also in this release: a faster multi-arch Docker image build (cross-compile instead of arm64 emulation) and a batch of dependency updates (bitcoin, mdns-sd, anyhow, sysinfo + UI).

Honest framing: this is a **diagnostics/transparency feature**, not a hashrate gain and not a correctness fix — payouts and share scoring are unchanged. It just makes operations more **legible**: a noisy miner is immediately attributable instead of guessed. 1039 tests green, svelte-check clean, reproducible build as always.

-------------------------

dvb-projekt | 2026-06-30 07:20:29 UTC | #24

**dvb-WarpPool v1.14.1 — no more false “low difficulty” rejects for small miners (V1 + V2)**

A small but targeted patch — triggered by a real measurement on a NerdAxe over Stratum V2.

- **The problem.** Pools continuously adapt per-miner difficulty (VarDiff). So that a share a miner computed against the *slightly older, lower* difficulty isn’t lost when the difficulty steps up, there’s a short “grace window” in which the previous target still counts. That window used to hold only **one** previous target. On small miners the share rate fluctuates a lot statistically (Poisson), and VarDiff then steps up several times in quick succession — a share against a **two-steps-old** target slipped through and was wrongly counted as a “low difficulty” reject.
- **New.** The grace window now keeps a **ring of the last eight targets**. If an incoming share meets any of them (within the 60-second window), it’s accepted instead of rejected. Applies to **both** protocols, Stratum V1 and V2. Purely additive — with a single retarget everything behaves exactly as before.
- **Honest framing.** This is **not** a hashrate gain and **not** a money matter: **block chance is unchanged** (found blocks are checked against the network difficulty, entirely separate from this pool-target window), and payouts are untouched. It’s a **correctness/robustness** improvement: small miners’ reject rate becomes honest again, and the operator isn’t chasing a phantom problem.

How did we find it? We actually measured the cause: a new **opt-in diagnostic log** (enabled only via `RUST_LOG`, zero overhead in normal operation) breaks down, per rejected share, how far it was below the current target and whether it would have met a recently valid target. That made it immediately clear these were retarget slip-throughs — not broken hashes.

1044 tests green (including new regression tests “share against a two-steps-old target is accepted” for V1 and V2), svelte-check clean, reproducible build as always.

-------------------------

dvb-projekt | 2026-07-01 07:47:37 UTC | #25

[dvb-WarpPool](https://dvb-projekt.github.io/dvb-WarpPool/umbrel-guide.html)

![image](https://osmu.xyz/uploads/default/optimized/1X/962c48d3fed66a040381ac769cf7260cc3ea5c99_2_690x362.jpeg)

### [dvb-WarpPool — Umbrel User Manual](https://dvb-projekt.github.io/dvb-WarpPool/umbrel-guide.html)

Install and run your own Bitcoin solo-mining pool on Umbrel — a step-by-step guide with screenshots. Free PDF.

-------------------------

dvb-projekt | 2026-07-02 18:31:51 UTC | #27

**dvb-WarpPool v1.15.0 — internal security audit (25 findings, all fixed) + a hardened block-submit path**

This release is the result of a full internal security and correctness audit: **25 confirmed findings, all fixed** — and then re-checked by a deliberately skeptical second review pass (which caught three more real touch-ups). The highlights, framed honestly:

- **The big one: the block-submit path.** When a miner with version-rolling enabled (overt ASICBoost — practically every modern ASIC, plus NerdAxe/NerdQaxe) finds a block, the header used to be reassembled with the **un-rolled** version. Result: the submitted hash no longer matched the proof-of-work, Bitcoin Core would reject the block as `high-hash`, and the block reward would be lost. Now the block-found event carries the **exact rolled** version and reconstructs the block from **the exact job it was mined on**. For **V1 and V2**. **Honest:** this was a **latent** bug — a solo pool rarely finds a block, and **there hasn’t been a mainnet block yet** — so it was found proactively via the audit and fixed **before** it could ever bite. It changes nothing about hashrate or block chance; it makes sure a block you *do* find reliably reaches the chain.
- **New & user-facing: dismissable health warnings (GitHub** #76**).** The “Bitcoin Core is pruned” notice (and any other node warning) used to come back on every reload. Now each warning in the banner has a **“Hide permanently”** button (when logged in as admin), and a new **Admin → Health** page lists what you’ve hidden so you can bring it back. Precise: hiding `bitcoin_pruned` silences **only** that notice — new/other warnings still show. Also seedable via `config.toml`.
- **Further hardening from the audit** (operator-relevant): 2FA can no longer be reset without a valid code; a read-only API token can no longer read the node’s RPC password; the LAN miner scan now requires admin auth and stays within private IP ranges; transient RPC errors at block-submit time are now retried instead of being wrongly discarded as an auth error. Plus various smaller robustness fixes (atomic energy accounting, notification escaping, reconnect behavior).

All purely additive, no breaking changes. **1083 tests green** (including new regression tests for the version-rolling fix, end-to-end and per protocol), svelte-check clean, reproducible build as always. No “battle-tested” claim, **no mainnet block yet**.

-------------------------

dvb-projekt | 2026-07-09 09:43:43 UTC | #30

**dvb-WarpPool has moved: own forge, own registry — [git.warppool.org](http://git.warppool.org)**

*New here?* dvb-WarpPool is an open-source self-hosted Bitcoin **solo** mining pool (Rust, full operator web UI/PWA in 8 languages, for NerdMiner alongside Bitaxe alongside Avalon Q). Stratum V1/V2/TLS, signed & reproducible builds, AGPL.

The short version: **GitHub permanently suspended our account — the project lives on, now on its own infrastructure.**

What happened, factually: GitHub’s abuse review classified the project’s CI usage as “incentivized activities / general computing” — the boilerplate applied to crypto-adjacent projects. For context: our CI only ever built and tested software (Rust builds, docs, signed releases). **No mining ever ran in CI.** The appeal was finally rejected; repos, issues, releases and Docker images went offline from one moment to the next. That’s GitHub’s prerogative on their platform — but it’s also exactly the risk this project has always preached about *mining*: **if you build on someone else’s infrastructure, you can lose it.**

So we did what we preach and self-hosted:

- **New home: [git.warppool.org/dvb-projekt/dvb-WarpPool](https://git.warppool.org/dvb-projekt/dvb-WarpPool)** — a self-hosted Forgejo instance (open-source forge, EU server) with code, releases and its own Docker registry. No third-party host left that can switch the project off via a classifier.
- **Nothing was lost:** the complete git history (all branches, all 50 release tags) moved 1:1. You can verify that yourself — git is content-addressed, **the commit hashes are identical** to before.
- **Docker images** now come from `git.warppool.org/dvb-projekt/dvb-warppool` (multi-arch amd64+arm64, cosign-signed). The old `ghcr.io` paths are dead.
- **Umbrel users — one-time switch required:** already-running pools keep running untouched. But the Community Store itself was fetched from GitHub — the old entry can no longer deliver updates or fresh installs. Re-add it once: App Store → three-dot menu → **Community App Stores** → remove the old dvb-projekt entry ([github.com](http://github.com)…) → add the new URL: `https://git.warppool.org/dvb-projekt/dvb-projekt-Umbrel-Community-App-Store.git` — everything works as before afterwards.
- **Homepage:** [warppool.org](https://warppool.org) — overview, features and all downloads in one place.
- **Docs:** [docs.warppool.org](https://docs.warppool.org)
- **Bugs & feedback:** file an issue at [git.warppool.org/dvb-projekt/dvb-WarpPool/issues](https://git.warppool.org/dvb-projekt/dvb-WarpPool/issues) — registration is open, new accounts get a quick manual approval (spam protection for a small instance). No account wanted? Email [dvbprojekt@gmx.de](mailto:dvbprojekt@gmx.de) works too.

What does **not** change: the license (AGPL + commercial option), signed & reproducible builds (now with a project-held cosign key instead of the GitHub-bound keyless flow — the public key lives in the repo), the release cadence, and the code itself. Honest as always: the move cost us the GitHub metadata (old issues/PRs) and the pending PR for the official Umbrel store — we’ll rebuild both as needed. No “battle-tested” claim, **no mainnet block yet** — a server move doesn’t change that. :wink:

A Bitcoin project that takes self-sovereignty seriously should run its own forge. Now it does.

Homepage: [warppool.org](http://warppool.org) · Code: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](http://git.warppool.org/dvb-projekt/dvb-WarpPool) · Docs: [docs.warppool.org](http://docs.warppool.org)

-------------------------

dvb-projekt | 2026-07-10 04:32:18 UTC | #31

**dvb-WarpPool v1.16.0: block templates straight from Bitcoin Core — over its IPC interface**

New in v1.16.0 — one for the plumbing enthusiasts:

**The pool can now pull its block templates directly from Bitcoin Core via Core’s IPC mining interface.** Until now (and still, by default) it goes the classic route: `getblocktemplate` over JSON-RPC plus a ZMQ notification when a new block arrives. That works well — but it’s a detour, and Core’s ZMQ queue can lag noticeably under load.

Bitcoin Core v31 ships a native **IPC interface** (Cap’n Proto) for exactly this. dvb-WarpPool now optionally speaks it directly instead of RPC+ZMQ. In our own benchmark the pool fetches a fresh template in **~5–12 ms** that way versus **~90–100 ms** over GBT+ZMQ (the gap is mostly the ZMQ queue lag). For a solo pool that means: after a new block on the network you switch to fresh work a touch sooner — i.e. slightly fewer wasted hashes on a stale template right after a block change. Not a hashrate boost, just cleaner plumbing.

Honest context:

- **Off by default.** Existing setups keep using GBT unchanged — nothing to do. A clean, shared `TemplateSource` trait keeps both paths interchangeable.
- **Requires Bitcoin Core v31.0.** Still on v30? You keep using GBT — perfectly fine.
- **Switching is explicit:** Admin → Bitcoin Core has a live GBT ⇄ IPC toggle that **probes the socket first** and falls back to GBT automatically if it isn’t reachable — no shot in the dark.
- **Umbrel:** the Bitcoin app has exposed the IPC socket since **v1.3.0** (settings toggle “IPC Mining Interface”). The pool mounts Core’s data dir read-only to reach the socket — the store app brings that automatically. Don’t want the IPC exposure at all? Just leave the switch on GBT.

Everything else as usual: same license (AGPL + commercial option), signed & reproducible builds, 1098 tests gating every release in CI. No “battle-tested” claim, **no mainnet block yet** — still saying that out loud. :wink:

Full comparison against ckpool/public-pool/mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Code & releases: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

-------------------------

dvb-projekt | 2026-07-11 04:59:00 UTC | #32

**dvb-WarpPool v1.16.1 + v1.16.2 — the IPC switch is now easy to find, and the Umbrel status is correct**

*New here?* dvb-WarpPool is an open-source self-hosted Bitcoin **solo** mining pool (Rust, full operator web UI/PWA in 8 languages, Stratum V1/V2/TLS, signed & reproducible builds, AGPL). Since the move it runs entirely on its own infrastructure ([git.warppool.org](http://git.warppool.org) / [docs.warppool.org](http://docs.warppool.org)).

Two small follow-ups to the optional IPC template backend introduced in **v1.16.0** (block templates straight from Bitcoin Core over its IPC interface, Core v31):

**v1.16.1 — the switch is now in the navigation.** The **Admin → Bitcoin Core** page (with the GBT ⇄ IPC toggle and the bitcoin.conf editor) existed, but wasn’t linked in the admin navigation — you could only reach it by typing the URL. It now has a **“Bitcoin Core” tab** (in all 8 UI languages), one click away.

**v1.16.2 — the stale “IPC is off” warning on Umbrel clears.** If you enabled the IPC toggle after the fact, Umbrel sometimes kept showing “:warning: the Umbrel Bitcoin app reports: IPC mining interface is OFF” — even though IPC was live. Reason: Umbrel sets that variable **at container start**, so toggling later left the banner stale. It’s now gated on the **actual socket test**: the moment the test returns OK, the warning is gone. (On older builds, restarting the WarpPool app fixed it.)

Plus a **docs-accuracy pass** across the whole documentation (cleanly caught up after the move to our own forge).

None of this changes behaviour, protocol, or the API — the test suite is unchanged (1098). Honest as always: no “battle-tested”, **no mainnet block yet**. :wink:

Full comparison vs ckpool/public-pool/mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Code & releases: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

-------------------------

dvb-projekt | 2026-07-11 17:30:41 UTC | #33

**dvb-WarpPool v1.16.3 — switch the language and literally EVERYTHING is translated now (8 languages)**

*New here?* dvb-WarpPool is an open-source self-hosted Bitcoin **solo** mining pool (Rust, full operator web UI/PWA, Stratum V1/V2/TLS, signed & reproducible builds, AGPL). Your miners point at your own host instead of a public pool — find a block and the full reward goes straight to your Bitcoin address. It runs entirely on its own infrastructure ([git.warppool.org](http://git.warppool.org) / [docs.warppool.org](http://docs.warppool.org)).

The interface has been available in 8 languages for a while — **but** three admin pages (**API Tokens**, **Audit Log**, **Notifications**) and the relative timestamps (“just now” / “5m ago”) stubbornly stayed German no matter which language you picked. If you run the pool in Spanish, French, Japanese, Chinese, etc., that was a jarring break.

**v1.16.3 cleans that up completely:**

- **The last German strings are translated.** Those three pages, the relative times, various fallback texts, the device auto-scan labels and a handful of status/error messages now all route through the translation system — with real translations in **all 8 languages** (DE/EN/ES/FR/IT/JA/PT-BR/ZH). Switching language now means the **entire** interface follows (~130 new strings × 8 languages).
- **A CI guard keeps it that way.** A new automated check fails the build if (a) the 8 language files don’t share the exact same set of strings, (b) a UI string is added without a translation, or (c) hardcoded German creeps back into the source. So this gap simply can’t return.
- **Both end-user manuals** (Umbrel + general) were updated accordingly (the “this page is in German” notes are gone, since it’s English now) and given richer screenshots.

None of this changes behaviour, protocol, or the API — pure interface polish, test suite unchanged (1098). Honest as always: no “battle-tested”, **no mainnet block yet**. :wink:

Full comparison vs ckpool/public-pool/mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Code & releases: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

-------------------------

dvb-projekt | 2026-07-13 12:31:01 UTC | #34

**dvb-WarpPool v1.17 — turn your solo setup into a public 0%-fee pool where every miner keeps their own coins**

For newcomers: dvb-WarpPool is a self-hosted Bitcoin **solo** mining pool written in Rust. Your

node, your block, your reward — the payout flows to your wallet **directly via the coinbase**,

with no accounts, no custody, no operator in between. Built for lottery miners running a

NerdMiner next to a Bitaxe next to an Avalon Q on their own node.

**New in v1.17: per-worker mode.** One config switch —

`[mining] payout_mode = "per_worker"` — turns your private solo pool into a **public pool you

can open to other miners without ever holding their coins:**

- **Everyone mines to their own address.** The BTC address is taken straight from the Stratum

  login (`address.rig`). Whoever finds the block gets the **full** reward in a single coinbase

  output — **0 % pool fee**, non-custodial. An invalid or wrong-network address is rejected (no

  silent fallback to an operator address). The pool never holds funds.
- **The default single-address mode is unchanged** — byte-for-byte. Nothing changes unless you

  deliberately turn per-worker on.
- **Shareable per-wallet dashboard** at `/users/<address>`: hashrate windows (1m/5m/1h/1d/7d),

  best share, estimated time to next block, per-rig list. The JSON at the same path is

  **ckpool-compatible** (firmware / ckstats). *(v1.17.1 + v1.17.2 polish this page: it now

  loads correctly on direct link / bookmark and its stats view is robust in every case.)*
- **Optional ownership proof:** a miner can verify their address with a signed message (BIP-137,

  no coins moved) to unlock — for themselves only — a privacy toggle (hide the address) and

  notifications (ntfy / webhook on block-found or a rig going offline). Default: public, no

  account.
- **Self-hostable & spreadable:** per-worker works on Stratum V1 **and** V2; anyone can run their

  own instance on their own domain. AGPL-3.0.

Keeping it honest: tested and proven on regtest **and signet against a real Bitcoin Core**

(consensus E2E: per-worker block accepted, correct address attribution, no cross-pay) — a

**mainnet** block is still to come.

Source: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison vs. ckpool / public-pool / mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Project page: https://warppool.org

-------------------------

dvb-projekt | 2026-07-13 17:44:55 UTC | #35

**dvb-WarpPool v1.18.0 — your public pool now shows only as much as you want**

Quick intro for newcomers: dvb-WarpPool is a self-hosted Rust Bitcoin **solo** mining pool. With

`payout_mode = "per_worker"` it becomes a **public, non-custodial 0%-fee pool** where every miner

mines to their own address — full block reward, no fee, no custodian.

**New in v1.18.0: control over what your pool exposes publicly.** Until now the Workers page was a

fully browsable directory of *every* miner’s address plus its per-rig breakdown — more open than

what the established solo pools do. So there’s now a new `[privacy]` section with two toggles:

- **`wallet_directory_public = false`** — the browsable wallet directory disappears for anonymous

  visitors (like `solo.ckpool.org`, which has no public directory at all). Every address keeps its

  shareable `/users/<address>` page — reachable by **direct link**, but nobody can enumerate all

  addresses anymore. The logged-in operator still sees everything.
- **`leaderboard_addresses_public = false`** — the BTC address in the public best-shares

  leaderboard is masked server-side (`bc1qsx…dvng`), like AtlasPool. The operator sees full

  addresses.

Both toggles **default to the previous open behaviour** — existing installs don’t change on

upgrade. And they’re independent of the existing **per-miner opt-out** (a miner can verify their

address with a signed message and hide themselves) — one is operator-wide, the other is per-miner.

Small, but it closes a gap: running a public mainnet pool without handing strangers a ready-made

list of every miner’s address and rig setup. Payouts and block construction are untouched.

Honest is honest: proven on regtest **and signet against real Bitcoin Core** — a **mainnet** block

is still to come.

Source: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison vs ckpool / public-pool / mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Project site: https://warppool.org

-------------------------

dvb-projekt | 2026-07-14 13:01:25 UTC | #36

**dvb-WarpPool v1.19.0 — donations for public 0% pools, and a wizard that sets the public mode up for you**

Quick intro for newcomers: dvb-WarpPool is a self-hosted Rust Bitcoin **solo** mining pool. With

`payout_mode = "per_worker"` it becomes a **public, non-custodial 0%-fee pool** where every miner

mines to their own address — full block reward, no fee, no custodian.

That left a gap: a pool that takes **0%** has no built-in funding. Running one publicly means paying

for hosting out of pocket. **New in v1.19.0: voluntary donations — cleanly built into the UI, but only

when you’re a public pool.**

- **Admin → Donations** — a new admin page (shown in the menu **only in per-worker mode**) where you

  set an optional **on-chain Bitcoin address** and/or a **Lightning address** (LN address / LNURL /

  BOLT12). The on-chain value is validated on save; either field may be left blank.
- **“Support this pool” card** — as soon as at least one address is set, a donation card appears at the

  bottom of the public dashboard with copy buttons and **QR codes** (the on-chain QR is a `bitcoin:`

  URI a wallet opens directly).

Important: the addresses are **pure operator metadata** — they’re never mixed into coinbase

construction. So the hard rule stays intact: a per-worker pool pays the finder the **full** reward; a

donation is something a visitor chooses to send to a displayed address. Stored as a pool setting (no

restart, no `config.toml` edit).

**Plus a friendlier setup wizard.** The Mining card now offers a **“Private solo pool” ⟷ “Public 0%

pool”** choice. Pick public, and the wizard writes `payout_mode = "per_worker"` for you, hides the

(unused) pool-wide payout address, and forces the fee to 0 — no hand-editing of `config.toml`. In all

8 wizard languages.

Nothing changes for private solo pools: the donation menu and card never appear there.

Honest is honest: proven on regtest **and signet against real Bitcoin Core** — a **mainnet** block is

still to come.

Source: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison vs ckpool / public-pool / mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Project site: https://warppool.org

-------------------------

dvb-projekt | 2026-07-16 15:47:36 UTC | #37

**dvb-WarpPool v1.19.1 + v1.20.0 — hardening after the first public mainnet run, and 2FA that can’t lock you out**

Quick intro for newcomers: dvb-WarpPool is a self-hosted Rust Bitcoin **solo** mining pool. Privately

you mine to your own address; one switch turns it into a **public, non-custodial 0%-fee pool** where

every miner mines to **their own** address — full block reward, no fee, no custodian.

Since mid-July `pool.warppool.org` has been running **publicly on mainnet** with real miners. That

live run is exactly what drove two hardening releases — both summarised here.

**v1.19.1 — the privacy hole the live run exposed.** Three read endpoints ignored the `[privacy]`

toggles: they hid the nav tabs, but the data still sat one request away. Most importantly,

**`/api/workers` served every miner’s full payout address to any visitor** — even with the wallet

directory hidden.

- **Leaderboard / worker addresses are now masked server-side** (`bc1qtg…eqz0.bitaxe602`) — the **rig

  label is kept** so you can still tell your own machines apart. The logged-in operator still sees

  everything in full.
- **`/api/hardware`** (OS/kernel/CPU/RAM) and **`/api/miners`** (LAN devices) are now genuinely closed

  to anonymous visitors, not just hidden from the menu.
- **Stratum V2 miners show their hardware again.** The pool synthesises an identity from the Sv2

  handshake but was dropping it on the Sv2 path — fixed.
- **New header badge “IPC / GBT”** — tells you at a glance whether block templates come over Bitcoin

  Core’s IPC interface or polled RPC. (Core’s own IPC is still experimental — I deliberately don’t call

  it “proven”.)

**v1.20.0 — 2FA that can’t lock you out.** Until now, losing the phone with your authenticator meant

losing access to the admin area. Now, enabling 2FA hands you **10 one-time recovery codes** (shown

once, then stored only as an Argon2 hash):

- If you lose your authenticator, enter **one of these codes instead of the app code** at login — each

  works exactly once.
- The 2FA page shows **how many codes remain**, warns when few are left, and can generate a **fresh

  set** with your current app code (the old ones then stop working).

Also fixed: **address ownership verification could get stuck.** One typo when signing the message (or

signing with the wrong wallet) used to consume the challenge — and every retry failed forever. Now a

failed attempt keeps the challenge; only a successful check consumes it. And the admin toggle that was

mislabelled “Miners tab” now correctly controls the **“Devices” tab**.

Honest is honest: the pool runs **publicly on mainnet** but has **not found a block yet** — the full

block path (per-worker coinbase → real Bitcoin Core accepts the block) is proven end-to-end on regtest

and signet; the mainnet proof is still outstanding. All open source (AGPL), 1164 CI-gated + signed,

reproducible builds.

Source: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison vs ckpool / public-pool / mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Public pool + operator manual: [dvb-WarpPool — Public 0% Solo Pool Operator Manual (free PDF)](https://docs.warppool.org/public-pool-guide.html)

Project site: https://warppool.org

-------------------------

dvb-projekt | 2026-07-16 16:22:21 UTC | #38

**[pool.warppool.org](http://pool.warppool.org) is live — a public 0% solo pool that knows what a Bitaxe is**

Quick intro: dvb-WarpPool is an open-source (AGPL) Rust Bitcoin **solo** pool. It now runs at

`pool.warppool.org` as a **public, non-custodial 0% pool** on mainnet: every miner mines to **their

own address**, taken straight from the Stratum login. If your rig finds the block, the coinbase pays

**you** the full reward. No fee, no custodian, no account. (The daemon **refuses to start** if a fee

is configured in this mode.)

But other public solo pools do that too. The reason to try this one is different.

**Your Bitaxe doesn’t start at difficulty 100,000 here.**

Most public solo pools start every miner at a fixed difficulty of 100,000 — and **don’t remember

it**. For a Bitaxe Gamma (~1.2 TH/s) that’s one share every **six minutes**. Your hashrate readout

is guesswork, the graph jitters, short sessions show nothing. And every time your wifi blips or the

pool restarts, it all starts over.

dvb-WarpPool reads your miner’s user agent and starts it in the right league — and the difficulty

**survives reconnects and pool restarts** (persisted per worker). Instead of EMA jitter there’s a

Poisson significance gate: it only retargets when the share rate genuinely clears a confidence band,

not on every outlier. And a worker that goes quiet because its difficulty ended up too high gets

walked back down by a guarded idle decay instead of being stranded.

**Not a paper figure — this is [pool.warppool.org](http://pool.warppool.org) right now:** a Bitaxe Gamma (~1.2 TH/s) running here

lands a share every **~30 seconds** thanks to VarDiff. At a fixed 100,000 that exact same hardware

would wait **six minutes** for a single one. And the extreme case shows how absurd a fixed 100,000

is: a KH/s-class NerdMiner V2 would, by the math, get one share every **~59 years** at 100,000 —

here it checks in every couple of minutes.

**What else is different:**

- **Stratum V2 and TLS** — your Bitaxe/NerdQaxe speaks V2; most pools don’t offer it. Here

  `:3333` (V1), `:3334` (V1 over TLS) and `:3336` (Sv2) are all listening.
- **Templates ~90 ms sooner.** Block templates come straight over Bitcoin Core’s **IPC interface**

  (Cap’n Proto, Core ≥ 31) instead of polled RPC — measured ~5–12 ms vs ~89–101 ms. For you: after

  every network block you get fresh work sooner and spend less time hashing on a block that’s

  already gone. (Core’s own IPC is still marked experimental — it runs here, but I won’t call it

  proven.)
- **Your address isn’t in a browsable list.** The wallet directory is off and leaderboard addresses

  are masked. Your page at `/users/<your-address>` stays reachable by direct link — and serves

  **ckpool-compatible JSON**, so your firmware and ckstats keep working. If you want more, verify

  your address with a signed message to unlock block-found and rig-offline alerts — no account.

**Connecting:**

```auto
stratum+tcp://pool.warppool.org:3333      (V1)
stratum+tcp://pool.warppool.org:3334      (V1 over TLS)
                pool.warppool.org:3336    (Stratum V2)

User: <your-bitcoin-address>.<rig-name>
Pass: anything
```

An invalid address is rejected outright. There’s no fallback that could silently pay someone else.

**The honest part:** the project is young. This pool has **not found a mainnet block yet** —

established pools like [solo.ckpool.org](http://solo.ckpool.org) have a track record, I don’t. Solo mining is a lottery anyway;

this pool makes buying the ticket nicer, not the odds better. The full block path is proven against

real Bitcoin Core on regtest and signet (correct per-worker coinbase and witness commitment

included) — the mainnet proof is still outstanding. If that’s not for you, ckpool is a fine choice;

my own comparison page says so.

Source: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison vs ckpool / public-pool / mkpool (source-verified): [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Pool: https://pool.warppool.org

https://www.facebook.com/100001354454108/videos/3246396338894836/

-------------------------

dvb-projekt | 2026-07-17 08:17:51 UTC | #39

*dvb-WarpPool v1.20.1 — the fix that came from the Bitaxe group: Sv2 miners get their own difficulty back**

Quick intro for newcomers: dvb-WarpPool is a self-hosted Rust Bitcoin **solo** mining pool. Privately you

mine to your own address; one switch turns it into a **public, non-custodial 0%-fee pool** where every

miner mines to **their own** address — full block reward, no fee, no custodian.

This release is small and came straight out of real operation: a miner reported that his **Bitaxes on

Stratum V2 were all stuck on the same frozen difficulty** — while the same machines on Stratum V1 spread

out normally, and his Qaxe++ weren’t affected at all. That exact combination is what pinned the bug down.

**Why it happened.** Stratum V2 has two channel types: **Standard** channels (which a Bitaxe opens) and

**Extended** channels (which e.g. NerdQAxe opens). Adaptive difficulty (VarDiff) was only wired into the

Extended path. A Standard channel got its difficulty **once**, derived from the hashrate the miner

advertises, and never adjusted again. Identical Bitaxes advertise the same hashrate, so they all landed

on the same value — and it never moved, leaving them frozen together. On V1 each miner adjusts

independently on its own (noisy) share stream, which is why V1 looked fine.

**What v1.20.1 does.** Standard channels now seed the same VarDiff as Extended — including the

miner-class tuning (a Bitaxe targets a shorter share cadence, for instance) and restoring the settled

difficulty after a reconnect. Every Sv2 miner adapts on its own share stream again, exactly like on V1.

Thanks to **John11** for the genuinely good bug report: “V1 fine, only the Bitaxes affected, Qaxe++ not”

was the clue that isolated the cause immediately.

Honest is honest: the pool runs **publicly on mainnet** but has **not found a block yet** — the full

block path (per-worker coinbase → real Bitcoin Core accepts the block) is proven end-to-end on regtest

and signet; the mainnet proof is still outstanding. All open source (AGPL), 1166 CI-gated + signed,

reproducible builds.

Source: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison vs ckpool / public-pool / mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Public pool + operator manual: [dvb-WarpPool — Public 0% Solo Pool Operator Manual (free PDF)](https://docs.warppool.org/public-pool-guide.html)

Project site: https://warppool.org

-------------------------

dvb-projekt | 2026-07-17 09:23:38 UTC | #40

**dvb-WarpPool — why updating a self-hosted solo pool doesn’t hurt**

Quick intro for newcomers: dvb-WarpPool is a self-hosted Rust Bitcoin **solo** mining pool. Privately you

mine to your own address; one switch turns it into a **public, non-custodial 0%-fee pool** where every

miner mines to **their own** address — full reward, no fee, no custodian.

This week I rolled a fix out to the public mainnet pool and actually timed how long it was gone. Result:

**under one second** during which the pool wasn’t accepting stratum connections. I’m not posting that as

a shop-window number — I’m posting it because it shows what operating this thing feels like, and why it’s

no accident given the design:

- **The new image is pulled while the old pool keeps serving.** There’s no window where something is

  “building/loading” and nothing is running — the swap only happens once the image is ready.
- **The swap itself is a fraction of a second.** The Rust daemon cold-starts and binds every listener

  (Stratum V1, V1-TLS, V2) in roughly 300 ms. No JIT warmup, no 30-second boot.
- **There’s nothing to reconcile.** Because every miner mines solo to their own address, the pool keeps

  no balance ledger that a restart would have to hold consistent. At most a few in-flight shares are lost

  — the same consequence as a brief network blip.
- **Only the pool restarts, not the node.** Bitcoin Core and the TLS proxy stay up — no chainstate

  interruption, no re-sync, no certificate reload.

Framed honestly: this is a **fast restart, not “zero downtime”.** The TCP connections drop, and each

miner reconnects on its own timer — a few seconds depending on firmware. “Pool unreachable” was under

1 s; “miner back on” is single-digit seconds per device. My ~6 live miners saw only a brief reconnect.

Behind that is the rest of the operations story I care about: **reproducible, signed builds** (you can

rebuild and confirm the published binary comes from exactly this source), a built-in **auto-updater** for

the desktop app, and a **one-container deploy** for server/Umbrel that leaves the node alone. Self-hosting

shouldn’t feel like a second job.

Honest is honest: the pool runs **publicly on mainnet** but has **not found a block yet** — the full

block path (per-worker coinbase → real Bitcoin Core accepts the block) is proven end-to-end on regtest

and signet. All open source (AGPL).

Source: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison vs ckpool / public-pool / mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Public pool + operator manual: [dvb-WarpPool — Public 0% Solo Pool Operator Manual (free PDF)](https://docs.warppool.org/public-pool-guide.html)

Project site: https://warppool.org

-------------------------

dvb-projekt | 2026-07-18 10:58:37 UTC | #41

**Closer to home: WarpPool now runs from Germany :germany:**

We’ve moved our Bitcoin solo pool from Helsinki to a datacenter in Nuremberg — right into the DE/EU community that actually uses it.

And the difference is measurable. From an ordinary German home line:

- **Ping: ~32 ms → ~16 ms**
- **Stratum handshake: ~65 ms → ~37 ms**

Roughly halved.

To be straight with you: latency isn’t an efficiency factor in solo mining — it only really matters at the moment a new block lands. We did it anyway. A quick response time is a good sign of a healthy pool, and we’d rather sit close to the people we’re building this for.

Best part: you don’t have to take our word for it. **Measure it yourself** — with an independent open-source tool:

```auto
python3 stratum_test.py pool.warppool.org 3333 --runs 3
```

-> [GitHub - mweinberg/stratum-speed-test: A simple script to test latency, stratum handshake speed, and TLS+stratum connection speed to Bitcoin mining pool stratum servers. · GitHub](http://github.com/mweinberg/stratum-speed-test)

WarpPool stays what it is: a from-scratch Rust solo pool, non-custodial, 0 % fee — now just a little closer to you. :high_voltage:

-------------------------

dvb-projekt | 2026-07-20 13:42:07 UTC | #43

**Tell your miners something — without the detour through Discord**

Briefly, for anyone new: **dvb-WarpPool** is a from-scratch Rust Bitcoin **solo** pool you host

yourself. Privately you mine to your own address; one switch turns it into a **public, non-custodial

0%-fee pool** where every miner mines to **their own** address — full reward, no fee, nothing held.

If you run one publicly, you know the problem: you want to resync the node on Sunday and really should

tell your miners first. Not everyone reads Discord, and until now there was no way to put anything on

the pool page itself.

**v1.21.0 turns that into a twenty-second job.** Under **Admin → Banner** you type your notice, pick how

long it should run (minutes, hours or days) and hit Start. The text scrolls along the top of the pool

page for every visitor, and **disappears by itself** when the time is up. A Stop button ends it early.

A few details that matter in day-to-day operation:

- **It expires, you don’t have to remember.** The expiry is stored, so there’s no scheduler and no

  mental note — and a forgotten maintenance banner doesn’t hang around for weeks. A pool restart

  doesn’t change it either.
- **Readable even when it’s long.** Pointing at it, or reaching it with the keyboard, pauses the

  scrolling. Visitors who ask for reduced motion get the text static instead of moving.
- **Plain text, never HTML.** What you type is shown literally — the input box isn’t an invitation for

  markup on your public page.
- **Gone on time.** The page hides it at the exact expiry moment rather than waiting for the next

  refresh cycle.

Honest as always: the pool runs publicly on mainnet but has **not found a block yet** — the block path

is proven end-to-end on regtest and signet against a real Bitcoin Core. The project is young; ckpool has

been running since 2014.

As of v1.21.0: **1170 Rust tests** gating every release in CI, signed and reproducible builds, Stratum

V1 + V2, TLS for miners, an operator PWA in 8 languages.

-------------------------

dvb-projekt | 2026-07-21 08:00:55 UTC | #44

**What an independent speed test says about WarpPool — and the one latency that actually matters**

There’s a small open-source tool solo miners use to measure their pool’s response time: mweinberg’s Stratum speed-test. We ran WarpPool through it, against 20 other well-known solo pools, from an ordinary German home line.

The result, honestly: WarpPool lands in the top group (~18 ms ping, ~37 ms handshake), in the same tight band as the leading German pools. Solid. But here’s the framing that matters more to us than the ranking:

**This miner-to-pool ping barely matters in solo mining.** It only really counts at one moment — the block change. And that’s exactly where we put the work: not into the ping these tests measure, but into the latency that actually does something.

**The block change, tightened.** The instant a new block appears on the network, the pool has to build a fresh template and push new work to miners — the faster it does, the less time you waste on the old block. WarpPool can pull its template straight from Bitcoin Core’s (experimental) IPC interface. Roughly the pool-controlled path from block to fresh work at the miner (rounded, same location assumed):

- **WarpPool (IPC):** ~10 ms to fetch the template + ~8 ms to deliver ≈ **~20 ms**
- **The classic way (GBT+ZMQ):** ~95 ms to fetch + ~8 ms to deliver ≈ **~105 ms**

The entire lead (~80 ms) sits in the template step — the miner ping is the same for both and can’t close it. It’s opt-in and needs Core 31, and **none of the usual self-hosted solo pools offer it at all**. Honestly framed: in absolute terms that’s milliseconds every ten minutes — measurable, but no earnings miracle.

And more honestly still: the template step is only *one* part. How fast a pool reacts to a block change *overall* depends mostly on how quickly its node hears about the new block — a question of network connectivity, where large, widely-peered nodes lead. IPC is the part *we* do cleanly, not a claim to react first.

And what actually makes a solo pool good, no ping can measure:

- **0 % fee, non-custodial** — you mine to your own address, full reward, nothing held.
- **Built for small miners** — sub-1 difficulty from the very first share (NerdMiner class), and difficulty that survives even a pool restart.
- **Reproducible, not just claimed** — signed, reproducible releases; you can verify the binary came from exactly this source.

You can check both yourself — the ping with the tool, the builds with our signatures:

```auto
python3 stratum_test.py pool.warppool.org 3333 --runs 3
```

-> [GitHub - mweinberg/stratum-speed-test: A simple script to test latency, stratum handshake speed, and TLS+stratum connection speed to Bitcoin mining pool stratum servers. · GitHub](http://github.com/mweinberg/stratum-speed-test)

Honest stays honest: the pool runs publicly on mainnet but has **not found a block yet** — the project is young. WarpPool is a from-scratch Rust solo pool, non-custodial, 0 % fee, self-hostable. :high_voltage:

-------------------------

dvb-projekt | 2026-07-21 10:55:47 UTC | #45

**A certificate renewed itself and nobody noticed — which is the whole point**

Quick intro for anyone new: dvb-WarpPool is a from-scratch Rust **solo** Bitcoin mining pool you

host yourself. The block reward goes straight to your wallet through the coinbase — the pool never

holds, forwards or settles anything. Run publicly, every visiting miner mines to **their own**

address (0 % fee, non-custodial).

**v1.22.0** is a polish release. Two small things, both from actually running the thing.

**Certificates now renew quietly in the background.** If you serve your stratum port with a real

certificate — because some miner firmware only trusts public CAs — you used to have an invisible

expiry date in your calendar. The daemon read the certificate and key exactly once at startup, so

after the next Let’s Encrypt renewal it kept serving the old one, and when that finally expired,

TLS broke for every miner at once. The workaround was a restart, and our own guide carried it as a

reminder in the cheat sheet.

That is gone. The pool now checks whether the two files changed and puts a renewed certificate into

service on its own. Connections that are already open keep the certificate they negotiated, so **a

renewal costs nobody a reconnect**. And if the reload catches a half-written file mid-renewal, the

old certificate stays in service and the next check tries again, rather than dropping the listener.

**The donation card was rewritten too.** It used to open with “Support the pool” — a request made

before the reader had decided they liked anything. It now leads with a question and then gives the

reason: the pool takes no fee, so donations are what cover the server.

Going through it turned up something mildly embarrassing: four of the eight languages had been

asking for a **tip** in the waiter sense for months — `propina`, `pourboire`, `mancia`, `打赏`. All

four came from the English word “tip” in the original copy. Chinese was the worst of them: `打赏`

is a gratuity to a *person*, while the admin side of the same application already said `捐赠`, so

the public page and the admin UI were using different words for the same thing. This time each

language was written on its own terms instead of translated.

Being straight about it: the pool runs publicly on mainnet but has **not found a block yet**. The

full block path is proven end-to-end against a real Bitcoin Core on regtest and signet. 1174 tests

gate every release, and builds are signed and reproducible.

Repo: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Compared with ckpool / public-pool / mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

-------------------------

dvb-projekt | 2026-07-24 08:10:53 UTC | #46

**The pool that tells you the truth about your odds — and celebrates the moments**

A quick intro to dvb-WarpPool for anyone new: a Bitcoin **solo** mining pool written from scratch in

Rust that you host yourself. The block reward goes straight to your wallet through the coinbase — the

pool holds, routes and settles nothing. In public mode every visiting miner mines to **their own**

address (0 % fee, non-custodial).

**v1.23.0** ships two things you feel immediately as a miner.

**Honest block odds instead of a number that reads as “never”.** Each miner’s public page

(`/users/<address>`) used to show a single “estimated time to block” tile. For a home rig it said

“~12,000 years” — the mean of an exponential distribution dressed up as a forecast. It reads like

“forget it” and hides the one property that makes solo mining make sense at all: the process is

**memoryless**. Every second is a fresh draw; there is no queue, no progress bar, nothing getting

closer.

In its place is the real picture: your **chance in the next 24 hours** and **within one year** (long

odds as “1 in N”, e.g. “1 in 6.3 million”; percentages rounded down so they never overstate), the

**50/50 point** (the median — when it becomes more likely than not, not the average), and your **luck

so far**: how many blocks your accepted work “should” have produced (almost always well under 1), how

many you actually found, and — if none yet — what percentage of miners with exactly your history would

also still be empty-handed. Under it, the honest core in one line: no amount of waiting makes a block

more likely; only more hashrate or a lower difficulty. Everything is computed server-side and also

exposed as an `odds` object on `/api/users/<address>`, so third-party tools get identical numbers.

**And the pool now celebrates the moments.** Solo mining lives on three of them: your new personal-best

share, entering the pool’s all-time top 100, and the block. Until now the pool pushed only the block.

If you have verified your payout address and set a notification target (ntfy or webhook), you now also

get a ping when you set a **new personal-best share** (across all your rigs, not per device) and when

you **first enter the all-time top 100** — a genuine entry, not merely climbing higher. Each kind has

its own cooldown so a good run doesn’t become a stream of messages, and a found block sends a single

headline rather than three overlapping alerts. No new configuration — it rides the existing,

signature-verified notification target.

Honest stays honest: the pool runs publicly on mainnet but has **not yet found a block** — the full

block path is proven end-to-end on regtest and signet against a real Bitcoin Core. Bitcoin mining is

inherently probabilistic; nothing here promises a reward.

Repo: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool) · Docs: https://docs.warppool.org ·

Comparison: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

-------------------------

dvb-projekt | 2026-07-24 13:33:58 UTC | #47

**Taproot wallets can now prove the address is theirs**

Quick intro for newcomers: dvb-WarpPool is a self-hosted Bitcoin **solo** mining pool written in Rust.

The block reward goes straight to your wallet through the coinbase — no middleman. In public mode every

visiting miner mines to **their own** address (0 % fee, non-custodial).

Each miner’s public page (`/users/<address>`) has an owner area: prove an address is yours — by signing

a short challenge in your wallet, **no account, no funds moved** — and you unlock privacy (hide the

address from the public list) and notifications (ntfy/webhook: block, a new personal-best share,

entering the all-time top 100, a rig going offline).

That ownership proof only had a format for legacy and SegWit addresses (BIP-137). **Taproot (`bc1p`)

had no signed-message format — so it stayed locked out, even though Taproot addresses have always been

able to mine.** **v1.24.0** fixes that: Taproot now verifies via **BIP-322** (the format Sparrow

produces for Taproot). It feels identical to you — open the wallet, “Sign message”, paste, sign, done;

the wallet picks the right format itself.

For context, source-verified (I read the others’ code before writing sentences like this): of ckpool,

public-pool and mkpool, **none** ties privacy or notifications to any proof that the address is yours —

this “prove the address is yours, and the control over it is yours too” exists only on dvb-WarpPool as

of today. Other pools do things we don’t; this is one we’re alone on.

Honest framing: the pool runs publicly on mainnet but has **not yet found a block** (the full block

path is proven end-to-end on regtest and signet against a real Bitcoin Core). Bitcoin mining is

inherently probabilistic; nothing here promises a reward.

Repo: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool) · Docs: https://docs.warppool.org ·

Comparison: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

-------------------------

dvb-projekt | 2026-07-31 07:42:13 UTC | #48

**dvb-WarpPool v1.25.1 — when two Sv2 miners don’t give you twice the coverage**

Briefly, what dvb-WarpPool is: a solo mining pool written in Rust that you run on your

own hardware next to your Bitcoin node. The block reward goes straight to the finder’s

address through the coinbase — the pool never holds coins, no accounts, no payouts.

Stratum V1 and V2, web interface in 8 languages, reproducible signed builds. AGPLv3.

**The bug.** A user (John11) reported that several of his Sv2 miners kept showing the

same best share, and that the colliding pair changed over time — most recently two

devices with a 3.5× difference in hash rate. His suspicion: they are being given

identical work.

He was right. The extranonce prefix counter was a field on the channel registry, and

that registry is rebuilt per connection. So the first channel of every connection got

`00 00 00 00`, and all directly connected Sv2 miners searched the same extranonce space.

Stratum V1 was never affected — there the counter is an `AtomicU64` on the shared server

state. That contrast was the evidence.

**What it means in practice:** no shares were lost and nothing was unsafe, the work was

real. But two miners were not giving you twice the coverage. This affects every operator

running more than one directly connected Sv2 miner, silently.

**The fix** allocates prefixes process-wide, with the mode explicit in the type. The

decisive new test deliberately sits on the listener’s live constructors rather than on

the data structure — the old test opened two channels in one registry and could not see

the failure axis at all. Verified by removing the fix: red; putting it back: green.

**Second change: standard or extended channel?** That was the most common follow-up

question about Sv2, and the connect dialog — the one place you look while setting a

miner up — said nothing. It now recommends **extended** when you connect to a pool you

do not run yourself. On an extended channel the pool sends the coinbase halves and the

merkle path, so your miner can check for itself what it is hashing and that the reward

output is the one you configured. On a standard channel it receives a finished merkle

root and has to take the pool’s word for it. AxeOS gives the same advice in its own

tooltip. The honest counter-argument is in there too: extended costs bigger jobs and a

little merkle work on the device.

**From v1.25.0** comes the way back out of the interface to the project site — “Powered

by dvb-WarpPool” in the footer plus one line in the connect dialog for newcomers.

Status: 1206 tests + 4 ignored, clippy clean, svelte-check with no errors.

**Staying honest:** this pool has **not found a mainnet block** yet. The consensus path

is verified end to end on regtest and signet, but the first mainnet block is still

outstanding. Nothing here is “battle-tested”.

**v1.25.2, half a day later:** the connect dialog never had a scroll area of its own. On

a phone it therefore ran off the top and the bottom at once — you saw the middle and

could not reach the username or the password. Fixed; nothing changes on a desktop.

Source: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison with ckpool / public-pool / mkpool: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

-------------------------

dvb-projekt | 2026-08-02 09:20:09 UTC | #50

**Why my Sv2 miners sat at 2–4% rejects — a bug hunt in three acts**

dvb-WarpPool is a solo mining pool written in Rust that you run yourself: on an Umbrel box,

a server, a Raspberry Pi or on macOS. It speaks Stratum V1 and V2, has a PWA interface, and

sends the full block reward straight to your own wallet through the coinbase — the pool

never holds coins, there are no accounts and nothing to pay out.

**Act 1: the find nobody was looking for (v1.25.3/v1.25.4)**

The starting point was the question of why my Stratum V2 miners lost 2–4% of their shares as

“low difficulty” while V1 devices with the same chip sat at 0.2%. While I was measuring,

something else surfaced first: when a V2 miner connects, it negotiates how many bytes of the coinbase

it may vary itself. The pool took the requested size at face value — for a NerdQAxe that

stuffed ten bytes into an eight-byte gap. Harmless for shares, since miner and pool compute

identically. But the coinbase came out two bytes longer than its own length field allows:

Bitcoin Core’s decoderawtransaction rejects those exact bytes. A found block would have been

lost. It had been there since v1.0.0.

The first fix went wrong: v1.25.3 widened the miner’s part for both protocols — but V1

firmware generates its part itself and ignores what the pool announces. The result: every V1

share discarded as malformed. Twenty minutes after it hit my pool, the release was withdrawn

(marked as a pre-release, store rolled back). v1.25.4 splits the gap per protocol: V1 gets

exactly the four bytes its firmware sends anyway; the pool’s own part absorbs the growth.

The lesson became a rule: wire changes are now measured against real miners before tagging —

all 1215 tests were green even on the broken version, because every one of them used the one

size that happened to fit.

**Act 2: the actual answer (v1.25.5)**

With better diagnostics, the pattern emerged: every reject sat within 90 seconds of a

block change — 60 out of 60 in the measurement window, median 16 seconds, zero in between.

The cause was a subtlety of the V2 spec: a job with min_ntime set means “mine immediately” —

against the prev hash the miner knows at that moment. On a block change, that is the old

one. The pool sent every job that way, so spec-compliant firmware hashed against the wrong

chain after every block until the next update arrived. V1 does not have this problem,

because mining.notify carries the prev hash inside the job.

Now a block change sends a future job that SetNewPrevHash activates; a template refresh

sends an immediately active job with no SetNewPrevHash. During the rework it turned out the

built-in V1<->V2 translator relied on the same wrong assumption — caught in analysis this

time, not in production.

And a second find: V2 connections kept dropping with an encryption error at irregular

intervals — anywhere from minutes to hours apart. That was a concurrency bug in the pool —

the frame read could be interrupted by other events and lost cipher state when it was. The

reader is now cancellation-safe.

**The measurement**

Before: 9.6 lost shares per block change on average (36 out of 36 changes affected), five

connection drops in 68 minutes. After, on the same miners: 26 consecutive block changes with

zero rejects, and over three hours without a single drop. Only after that measurement was

the release tagged.

**Who should update:** everyone running Stratum V2 miners; if you grabbed v1.25.3,

definitely. Nothing to configure. To be straight about it: this pool has not found a block

on mainnet yet — the full block path is verified end to end on regtest and signet, but “not

yet” is “not yet”.

Repo: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison with other solo pools: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

-------------------------

dvb-projekt | 2026-08-10 12:45:45 UTC | #51

**Our pool dashboard shows fewer workers as of today — and that’s the actual update.**

Since dvb-WarpPool got listed on a public pool-comparison site, its measurement probes have been connecting to our Stratum port around the clock — each check with a freshly generated throwaway address that never submits a single share. Perfectly legitimate (that’s how you measure pools independently), but our dashboard dutifully counted every one of those addresses as a “worker”. Result: 203 workers on display, 31 of them actually mining.

With v1.25.6 the public worker and wallet totals only count miners that submitted at least one accepted share. A new retention rule additionally clears rows that never submitted any share from the database after 7 days (configurable; a real miner stops qualifying within seconds, and a misconfigured miner whose shares get rejected stays visible for debugging).

Also in v1.25.6: if you run your pool behind a CA-signed TLS certificate (e.g. Let’s Encrypt), the connect dialog now says so — firmware verifies it against its built-in CA store, no extra file needed. Previously the dialog always warned about “self-signed” and effectively pointed miners at the unencrypted port. Self-signed setups (the usual case on a home network) keep the familiar warning and certificate download.

A small release, but one we care about: a solo pool lives on its numbers being true — even when the honest number is smaller than the impressive one. As always: non-custodial, 0% fee, every miner mines to their own address. The pool has not found a mainnet block yet — solo mining remains a lottery ticket.

Repo: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison with other pools: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

-------------------------

dvb-projekt | 2026-08-14 13:07:42 UTC | #52

**Someone read our source and found a real weakness — v1.25.7 closes it. Thank you, Distortions.**

This is open source working as intended: the operator of StratumStats/M45Core read our code and reported that a hostile client could overwhelm the pool just by submitting invalid shares — every rejected share spawned its own unbounded background write to the database, and share submission had no rate limit. He was right.

As of v1.25.7 a rejected share costs two in-memory counter bumps; a single loop flushes the coalesced totals to the database every two seconds — on both Stratum V1 and V2. Junk traffic has nowhere left to pile up. Also fixed: a timing clash between the pool and Bitcoin Core that wrote hundreds of harmless but noisy warnings per day into the log.

The report is credited by name in the changelog. If you run the pool yourself: update recommended — this is hardening, not a feature release. As always: non-custodial, 0% fee, every miner mines to their own address, and we still honestly have “not yet” found a mainnet block.

Repo: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

-------------------------

dvb-projekt | 2026-09-07 12:56:28 UTC | #53

**v1.26.0: We measured every millisecond between “new block” and “new job” — and removed three of them.**

How fast a solo pool hands its miners fresh work after a new block is decided almost entirely by the Bitcoin node behind it, not by the pool software. We took the chain apart with microsecond timestamps on our reference box and on an Umbrel Home: hearing the block, reconstructing the compact block, validating, building the template, pushing the job. The result is now a handbook page, “Node Tuning for Block Latency” — numbers, not opinions.

What v1.26.0 does with it:

• **Latency as a metric.** Every installation now sees its own chain: three new Prometheus gauges, fields in the API, and one “tip → job” log line per new block.

• **A warning when ZMQ goes silent.** A node with ZMQ configured but not delivering used to drop the pool silently onto the poll tick — new blocks arrived up to 90 seconds late. The pool now counts those and warns in the dashboard.

• **A node recommendation from the measurement.** The setup wizard suggests `blockreconstructionextratxn=1000`: with it, one block in three needed no round trip to a peer on our box, and reconstruction fell from 90–150 ms to a 60 ms median.

• **IPC template source, automatically.** `template_source = "auto"` probes the Bitcoin Core 31 socket at start and takes the fast path when it is there — on Umbrel via an environment variable, no config editing.

• **Clean shutdown on SIGTERM.** `docker stop` used to kill the daemon outright. Share buffers are now flushed and sessions closed properly.

• **Restart without a gap, optional.** With `reuse_port` a new daemon can take over the ports while the old one still serves.

• **For developers:** the Sv2 handshake logs every stage with concrete hints (someone got their own pool talking to ours with them last week), Sv2 shares the rate limiter with V1, and both protocol parsers now run against fuzz tests in the regular test suite.

And a small invitation: our node accepts peering from other pools (`91.98.76.244:8333`). One manual peer to a node on a fast relay took us from hearing blocks 12 ms after to 17 ms before a relay-connected pool’s job — trustless, one line in bitcoin.conf. The peering page in the docs shows how to measure it.

As always: non-custodial, 0% fee, every miner mines to their own address, and we still honestly have “not yet” found a mainnet block.

Repo: [dvb-projekt/dvb-WarpPool: Bitcoin solo/pool mining server — Stratum V1 + V2 - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

Node tuning: [Node Tuning for Block Latency - dvb-WarpPool](https://docs.warppool.org/node-tuning.html)

-------------------------

dvb-projekt | 2026-09-10 10:06:51 UTC | #54

dvb-WarpPool v1.27.0 — a small one, all about keeping the node behind the pool in view:

• Opt-in Bitcoin Core release check: once a day the pool fetches the Core release list and warns in the dashboard when a newer release exists on your node’s own line (31.1 → 31.2 style bug-fix/security releases). Newer major lines are only shown, never nagged about. Off by default; the pool never updates Core itself.

• Admin → Health now starts with a node card: Core version + newest release, chain, height, peers, pruned/txindex, ZMQ, template source.

• Fix for an Umbrel race: after a Bitcoin app update both apps restart together, and the pool’s `template_source = "auto"` probe ran before bitcoind bound its IPC socket, so the pool silently stayed on GBT. It now keeps probing and tells you to restart once the socket answers.

• Quieter V1 log on port-scanner hangups, and a `noise_probe` example for anyone writing an Sv2 client against us (found the swapped-cipher bug in an external client in minutes last week).

Changelog: [v1.27.0 - dvb-projekt/dvb-WarpPool - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool/releases/tag/v1.27.0)

-------------------------

dvb-projekt | 2026-09-11 16:43:59 UTC | #55

**v1.30.0: the pool now knows whether your mining power came off the roof, out of the house battery, or from the grid — and deliberately does not flatter itself.**

dvb-WarpPool is my non-custodial Bitcoin solo pool: 0 % fee, every miner mines straight to its own address, Stratum V1 and V2, an interface in eight languages, as an Umbrel app or native.

This one started in my own basement. The pool used to show two sources for the kilowatt-hours it consumed: solar or grid. In the evening it said grid. Except that wasn’t true — in the evening the house battery carries the house here, and what’s in it is solar from midday. The meter shows nothing of that; it simply shows no import. What booked it as grid was the old check, which only compared PV production against house load: sun gone, production zero, therefore grid.

As of v1.30.0 there are three shares: **direct solar, battery, grid.** Battery means solar stored during the day and consumed later. It counts as self-supplied and costs accordingly nothing — only what actually came from the grid is priced.

The more interesting part is how you attribute that, and there I went with the less flattering option. The obvious approach is the house average: if the house runs 75 % on battery, credit the miners with 75 % battery. That reads nicely and is wrong. An example: in the evening, 200 W from the grid and 600 W from the battery, 300 W of which is miners. The average would credit the miners with 75 % battery. But unplug the miners and the grid draw drops to zero — so those 200 W were on their account, not the house’s.

So the pool attributes **marginally**: the miners are the last consumer switched on, and their load is charged against the sources in the order those would fall away if you unplugged them — grid import first, then battery, then direct PV. In the example that’s 200 W grid plus 100 W battery, two thirds to one third. With the grid at zero it’s a full 100 % battery, which is the case this whole thing exists for. It stays proportional rather than all-or-nothing: a minute whose marginal load spans two sources is booked exactly that way.

Where the data comes from: if you use the Anker bridge, there is nothing to do — it reports charge, discharge, grid import and feed-in, and it always had those values, the pool simply never read them. For Home Assistant there are five optional sensors, entered in the setup wizard or the admin area. One thing matters there: positive watts, one sensor per direction. Many HA integrations expose *one* signed value for charging and discharging; that does not work here and has to be split into two template sensors first.

Without a battery nothing changes: two shares as before, and the third bar only appears once your system has actually contributed a battery kilowatt-hour. Fixed along the way: the week, month and year view had priced every kilowatt-hour at the grid tariff, self-generated ones included — the energy card had long had this right, the overview didn’t follow.

All open source, AGPL, in the same repo as the pool.

Repo: [dvb-projekt/dvb-WarpPool: Rust Bitcoin solo mining pool — Stratum V1 + V2, PWA operator UI, signed reproducible builds - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

-------------------------

dvb-projekt | 2026-09-15 07:23:32 UTC | #56

dvb-WarpPool v1.30.1 is a security patch for Umbrel installs from our community store. If you run 1.28.0, 1.29.0 or 1.30.0 there, please update.

What was wrong: 1.28.0 added a second host port (18335) so a LAN sidecar could read `/api/workers` and `/api/energy` without the app login. That port was mapped straight onto the pool’s main API port, which also carries the first-run setup wizard and the initial admin setup. So between installing the app and finishing the wizard, anyone on your LAN could have reached both without the Umbrel login. Once the wizard and the admin account were done, the window was closed; the port then only served the same anonymous reads the public pool serves.

The fix: the port now maps to a separate read-only listener inside the daemon (`[server].api_readonly_listen`). It answers GETs, accepts the token-guarded WarpTune snapshot push, and refuses everything under `/api/auth` and `/api/admin` outright. The setup wizard never binds it. Verified over real sockets before tagging.

Not affected: native installs (.deb/.rpm/AppImage/.dmg) and Docker setups without that port mapping, and the official-store package (which never had the port). Nothing in the pool’s own login, tokens or Stratum paths changed.

Changelog: [v1.30.1 - dvb-projekt/dvb-WarpPool - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool/releases/tag/v1.30.1)

-------------------------

dvb-projekt | 2026-09-17 07:40:29 UTC | #57

dvb-WarpPool v1.31.0 — mostly dvb-WarpTune, the auto-clock sidecar:

• Avalon Q over the cgminer API: the three work modes are the ladder, `ascset workmode` is the only write, steps judged on the 15-minute hashrate (the since-boot average lags for hours after a mode switch).

• Any ASIC the NerdOS firmware knows: ladder from the board’s own option list, expected hashrate from the reported small-core count. BM1373 boards should work without a code change; first unit test pending.

• Fan-target clamp, learned the hard way: a target below the firmware’s fan target + 2 °C made the fan PID slow the fan on every step down, so the chip never cooled and the regulator walked a Gamma 640 → 500 MHz in 13 minutes (every write verified, restore clean). Now clamped in every mode instead of only warned.

• Point changes made outside the regulator (AxeOS UI, Avalon mode switch) restart settle/judge instead of being taken back.

• The sidecar binary ships in all release formats now (was source-only through 1.30.0).

• Pool: Admin → Health header count and IBD flag were read once at start and drifted; fixed. rustls bump for RUSTSEC-2026-0285.

Changelog: [v1.31.0 - dvb-projekt/dvb-WarpPool - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool/releases/tag/v1.31.0)

-------------------------

dvb-projekt | 2026-09-18 07:18:47 UTC | #58

**v1.28.0 → v1.31.0: An auto-clock for Bitaxe and friends that respects your hand tuning — as an open sidecar next to the pool.**

dvb-WarpPool is my non-custodial Bitcoin solo pool: 0 % fee, every miner mines straight to its own address, Stratum V1 and V2, a UI in eight languages, as an Umbrel app or native. v1.28.0 adds something I have wanted for a long time and no firmware ships: **dvb-WarpTune**, an auto-clock for AxeOS miners with guardrails.

What it does: WarpTune holds each miner at a temperature target by stepping frequency and core voltage along the board’s own ladder. NerdOS devices bring their ladder with them; Bitaxe and BitForge Nano get the vendor table. One decision every 30 seconds, 25 MHz steps, hysteresis, settle time after each step.

What it does not do: wreck your tuning. The point a miner runs at when WarpTune starts is the ceiling for its voltage. If you set your Gamma to 640 MHz at 1140 mV, WarpTune will never hand it 1200 mV, table or no table. On shutdown, or after the miner reboots, it puts exactly that point back and reads it back to prove it.

The guardrails the firmware lacks:

• A power budget per board from the measured cooling resistance, so a step up is computed before the temperature has to stop it.

• A reject guard that knows reasons: stale and low-difficulty do not count as instability. The counters come from the pool, not the firmware, because ESP-Miner resets them on every reconnect.

• Step memory: a step that produced rejects is off limits for an hour.

• Every write is verified by reading it back. Twelve writes per hour is the cap, three failures in a row switch live control off, and the regulator keeps going as a proposal engine.

• Limits for VR temperature, input voltage and current, all taken from what the firmware reports about itself.

Then the pool coupling: WarpTune reads the electricity picture from the pool, tariff and solar surplus, and in energy mode switches miners between Eco, Balanced and Max with a minimum hold against cloud gaps. The other way round, the Devices tab shows a badge per miner: mode, frequency, state, last decision. The pool only displays; it never writes to a miner.

Two switches for live: one on the command line, one per miner in the config. Without both it is a dry run, and dry run is the default. On my side five devices on three firmwares ran 48 hours dry; all stayed on their hand-tuned points and the regulator agreed with every one. The Gamma then ran live for a week against acceptance criteria written down beforehand; the numbers are below.

Open source, AGPL, in the same repo as the pool, installed on macOS as a launchd service with one script. Umbrel users get a second API port without the login with this update, so a sidecar on the LAN can read along.

**Addendum v1.29.0:** Two things that were obviously missing the moment it was built. First, a switch in the admin area so a home pool turns the coupling on without editing a file, and it applies at once, no restart. Second, the public pool: your miners sit in your home networks, which the pool cannot reach. So the sidecar sends its state itself, with a token you create in the owner area of your wallet page after proving ownership with a signature. The badge then shows per rig on your own wallet page, to visitors only if you want it. The pool accepts only states that belong to your wallet, at most every ten seconds, and never writes anything back to a miner. The live switch stays where it belongs: with you, on the machine the sidecar runs on.

**One week live on the Gamma:** 7 days live on the Gamma (2026-09-11 → 09-18, 991 samples): 0 interventions, hashrate avg 1306.8 GH/s against the 1305.6 GH/s baseline, 60.0–62.5 °C, 22.8 W, 17.5 J/TH, 4 stale shares in total, no reboot (15.8 days uptime). The only writes were a supervised thermal test on day 5, which is where the fan-target clamp in v1.31.0 comes from.

**v1.31.0** (Avalon Q over the cgminer API, any ASIC NerdOS knows, the fan-target clamp, manual changes respected) is one post up in this thread.

Energy mode is in its first dry run on my Octaxe and Avalon Q this week. Day one already taught me something: the pool’s surplus flag flips on the first watt, so the governor needs a margin before it lifts a miner that would draw 850 W more — that lands in v1.32.0.

Repo: [dvb-projekt/dvb-WarpPool: Rust Bitcoin solo mining pool — Stratum V1 + V2, PWA operator UI, signed reproducible builds - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool)

Comparison: [Comparison (ckpool / public-pool / mkpool) - dvb-WarpPool](https://docs.warppool.org/comparison.html)

-------------------------

dvb-projekt | 2026-09-19 18:28:20 UTC | #59

**v1.32.0 — a field note on solar surplus**

Short one. Yesterday was the first day without the EV charging, so I could finally look at the energy mode properly, and the numbers showed a mistake on the pool side rather than in the tuner.

The pool’s surplus flag required PV to exceed the house load by the miners’ power plus a buffer. That rule is right for a sub-meter that sits in front of the miners only. My Anker measures the whole house, miners included, so they were counted twice. Miners on PV for about four hours, flag on for six minutes, and dvb-WarpTune saw only two short Max windows.

v1.32.0 adds `consumption_includes_pool` (default true, because that is what a house meter reports) and keeps the old rule behind `false`. On the tuner side the energy mode now has a surplus margin per miner (the extra watts that Max draws over Eco, 900 W on an Avalon Q, 30 W on an Octaxe) and an exit debounce, so a cloud passing over does not flip the mode every hold period.

Still dry-run on the Octaxe and Avalon here; the Gamma stays live. The BM1373 board arrives Monday, that will be v1.33.0.

Repo: [dvb-projekt/dvb-WarpPool: Rust Bitcoin solo mining pool — Stratum V1 + V2, PWA operator UI, signed reproducible builds - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool) · Changelog in the repo.

-------------------------

dvb-projekt | 2026-09-24 08:57:15 UTC | #60

**v1.33.0 — the first day with a NerdAxe Gaia, and what it taught the tuner**

The BM1373 board arrived Monday. It is a NerdAxe Gaia on NerdOS, one chip, 6860 small cores, factory point 350 MHz at 940 mV. dvb-WarpPool knows it as its own vendor now, and the AxeOS probe takes the board name from the firmware, so a board that takes over another one’s address shows up as what it is (mine sat on the old Gamma’s IP and was labelled Gamma for an hour).

I let dvb-WarpTune regulate it from the first minute, with the 300–440 MHz and 900–1040 mV window the firmware offers and no vendor table. Ten minutes later it stood at 440 MHz with a core voltage of 0 mV, 5 W on the meter, no fault flag, and the API still reported the nominal hashrate. The regulator sat in its judge window and waited, because everything it looked at said “fine”. I wrote the factory point by hand.

Three things came out of that day. A step the tuner has never seen hashing in full is judged for ten minutes before the next one is taken, so the first climb on a new board is slow on purpose. A chip that reports 0 mV or 0 hashrate for three decisions, or a draw far below what the point should pull, goes back to the last point that ran and the board is rebooted. And the regulator’s memory is bound to the device, not to the address: the Gaia had inherited the Gamma’s 640 MHz voltage entry, a point that does not exist in its window.

Smaller: an automatic fan with reserve keeps the thermal budget (an Octaxe spent an afternoon of surplus at 650 MHz because the fixed-fan rule saw 61 °C, not 61 % fan), Eco gets its own ladder top, the voltage trial takes the pool’s share counter as a second vote against a firmware reading that drifts ±5 %, and the surplus margin of the energy mode is an entry condition only.

On the pool side a fix I owe to a six-minute link outage: shares after a VarDiff retarget were booked at the new difficulty while the miner still worked the old job, and the reconnect burst drew a 65 TH/s peak into a 17 TH/s pool. V1 now books at the difficulty its job went out with, Sv2 at the target the share actually met.

The Gaia runs at 400 MHz today, on the tuner, live. 420 is a question for the data, not for me. Still no mainnet block.

Repo: [dvb-projekt/dvb-WarpPool: Rust Bitcoin solo mining pool — Stratum V1 + V2, PWA operator UI, signed reproducible builds - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool) · Changelog in the repo.

-------------------------

WantClue | 2026-09-27 07:27:29 UTC | #61

keep on mining! Can’t wait for more updates

-------------------------

dvb-projekt | 2026-09-27 12:23:08 UTC | #62

**v1.34.0 — shares that arrive after the block, and a tuner that waits for enough of them**

Two things this release, both about counting honestly.

When a new block arrives, a miner gets a fresh job with clean_jobs set, but the chips are still finishing the work they hold, and those results reach the pool a few seconds later. dvb-WarpPool used to drop the old jobs at that moment, so each late share came back as “stale share”: one or two per block change, a steady 1–3 % that looked like a network or firmware problem and was neither. Both Stratum V1 and Sv2 now keep the jobs from before the block for 60 seconds and book those shares like any other, at the difficulty their job went out with. A block solution on such a job still goes to the node, which decides between the two blocks. After 60 seconds the job is stale as before. The duplicate check no longer resets on a block change, so a share sent before and after it still counts once.

On the tuner side the voltage trial now waits for 200 accepted pool shares before it calls a voltage good or short. The first version of that rule looked back 30 minutes, and VarDiff keeps every miner near four shares a minute, so the window never held 200 and the trial waited forever. It reaches back until it has them now. My NerdAxe Gaia at 420 MHz, over a day: 960 mV good at 101 % of the expected rate over 200 shares, 950 mV short twice at 82 %, 940 mV short at 53 %. The firmware read 102–105 % the whole time; only the pool saw the difference. There is a new `yield` command that prints this per operating point from the pool’s shares.

The Avalon Q went live on the energy mode this week and the first real work-mode switch was refused by the firmware: the command needs a `set` verb that the dry runs never exercised. Fixed, and today it went Eco, Standard, Super on PV surplus and back to Eco on the tariff. Without the pool’s energy feed the mode now holds Eco rather than Balanced, which had let the Q climb to Standard in the three minutes a restart took to get the first reading.

Still no mainnet block.

Repo: [dvb-projekt/dvb-WarpPool: Rust Bitcoin solo mining pool — Stratum V1 + V2, PWA operator UI, signed reproducible builds - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool) · Changelog in the repo.

-------------------------

dvb-projekt | 2026-10-03 06:53:45 UTC | #63

**v1.36.0 — calibration by button, and what it found on my Octaxe**

The headline of this release is a button. For those running dvb-WarpTune next to the pool, every miner under live control now has *Start calibration* on the devices page. It finds the lowest core voltage each of the miner’s two steps (Eco and Max) still hashes cleanly at, and it judges by the pool’s accepted shares, not by the miner’s own counters: the reference voltage first, then 10 mV less at a time, 200 shares each, until a step falls short. That takes a few hours; the miner keeps mining. At the end the card shows the voltage found per step and asks you to apply or discard it.

Two rules shaped it. It only ever lowers the voltage below your hand-tuned point at the same frequency, so a calibrated miner never draws more power than before. And it errs on the safe side: the result is the lowest voltage that passed above the highest one that failed, plus a 20 mV reserve, and in operation a step gets 10 mV more whenever the shares fall short there later. A 200-share window still varies by several percent, so now and then a good voltage fails — calibration then keeps more voltage, never less.

Testing it on my own NerdOctaxe was instructive. The board’s floor came out at the hand-tuned 1210 mV, no saving. Per-chip counters showed why: one of the eight chips has weak domains that switch off below about 1210 mV and stay off until the voltage comes back up, a quiet 1.5–3 % loss the pool’s shares barely see. The other seven chips hold 1180 mV. Calibration settled where the weakest chip still hashes, which is the honest answer for that board; spotting such a domain directly is next.

Smaller: the voltage search line on each device now says what it checked and why a miner sits above WarpTune’s table voltage (“needs 960 mV (table 940) · at 950 mV too many chip errors”).

Still no mainnet block.

Repo: [dvb-projekt/dvb-WarpPool: Rust Bitcoin solo mining pool — Stratum V1 + V2, PWA operator UI, signed reproducible builds - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool) · Changelog in the repo.

-------------------------

dvb-projekt | 2026-10-07 16:51:07 UTC | #64

**v1.37.0 + v1.37.1 — the first real savings from calibration, what the clock search taught me, and Stratum V2 for small miners**

Last release added calibration by button; this one makes it worth pressing. On my BitForge Nano the Max step (650 MHz) came down from the hand-tuned 1160 mV to 1050 mV including a 20 mV reserve: 52.1 W → 43.7 W, −16 %, with the pool’s hashrate unchanged. The per-chip error rate stayed flat under 0.5 % down to 1050 mV and jumped to 2.9 % at 1020 — exactly where calibration said no. On a Bitaxe Gamma the Max step (640 MHz) went 1140 → 1050 mV, 23.6 → 20.7 W, −12 %.

New is an opt-in clock search: before each voltage stage it looks for the best clock, judged over 30 minutes on fan, temperatures, core current, power, the draw on the power supply (kept under 80 % of its rating) and the pool’s shares. On the Nano it stopped right at my hand-tuned point: with the lid on and a 60 °C fan target the fan needed 95–100 % at 1160 mV. That is the rule doing its job — at 1050 mV the same chip needs 58 %, so a later version can search the clock at the calibrated voltage (already there as an option).

Running it live taught me three things, all fixed in this release. Chip domains that silently drop out (1–3 % of hashrate, too little for the shares to show) are now caught from the firmware’s per-chip counters, and a short bump to the hand-tuned voltage brings them back. The in-operation raise of a calibrated voltage reacted to share luck; it now needs a clear shortfall or a second sign, at most twice a day, and steps back after six good hours. And a NerdAxe Gaia showed that a power budget isn’t enough: one step up from 380 to 400 MHz drew 32 A against its regulator’s ~33 A limit and tripped it. Every step up and every restore is now held under a per-board share of that limit, predicted from what the miner actually drew there before.

v1.37.1 is a small follow-up for tiny miners on Stratum V2: a recognised NerdMiner-class device now opens its Sv2 channel at the same small difficulty it gets over V1 instead of a fixed 4096. Tested with WarpAxe on a LilyGO T-Display-S3 (~290 kH/s): start 0.0064, 4 of 4 shares valid in 12 minutes. Unrecognised miners keep the 4096 floor.

Still no mainnet block.

Repo: [dvb-projekt/dvb-WarpPool: Rust Bitcoin solo mining pool — Stratum V1 + V2, PWA operator UI, signed reproducible builds - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool) · Changelog in the repo

-------------------------

dvb-projekt | 2026-10-09 15:07:48 UTC | #65

**v1.38.0 — hashrate per watt instead of the lowest stable voltage, a quick check, and what a chip domain on my Octaxe taught me**

Calibration used to take the lowest voltage that passed 200 pool shares. Looking at the journal, that wasn’t always the best choice: on my Bitaxe Gamma at 640 MHz, 1030 mV passed, but with 6.3 % chip errors; 1040 mV had 1.9 %. Since the pool only books what the chips get right, the errors are real loss — a NerdAxe Gaia with ~6 % chip errors showed ~6 % less hashrate at the pool over 24 hours, next to a Gamma at 100 %. So v1.38 picks the voltage with the most hashrate per watt among the ones that pass, and the card says why (“1040 mV instead of the stable 1030 mV — x % more hashrate per watt”).

The same data made a faster calibration possible. Over 88 voltage verdicts from the last month, the chip error rate predicted the 200-share verdict 86–95 % of the time, and unlike the shares it rises smoothly as the voltage drops. The new quick check walks down by the error counters, about 10 minutes per step, and only the final candidate gets the full share verdict, with a 30 mV reserve. It’s meant to take about 1.5–2 hours per stage instead of 6–13; I haven’t run it on all miners yet. A re-check 28 days after you apply runs on its own on Max miners and only ever suggests.

The Octaxe gave me a lesson today. After a firmware update (a warm reboot) one of its 32 chip domains stayed off. WarpTune now switches the chain off and on in that case — confirmed off, 15 seconds, on, ready, at most three an hour and only once the miner is steady — but four tries didn’t bring that domain back. Switching the power supply off for a few seconds did. So WarpTune now gives up on a domain after two failed tries and the card says exactly that: power-cycle it, and if it still drops out, it’s a margin question for you.

Also new: Admin → Workers to remove idle workers (old test names in the leaderboard), and NerdMiner-class miners no longer triple their difficulty after a few lucky shares.

Still no mainnet block.

Repo: [dvb-projekt/dvb-WarpPool: Rust Bitcoin solo mining pool — Stratum V1 + V2, PWA operator UI, signed reproducible builds - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool) · Changelog in the repo.

-------------------------

dvb-projekt | 2026-10-10 09:19:10 UTC | #66

**v1.38.1 — clearer cards, and what yesterday’s quick check said**

A small follow-up to v1.38, mostly about saying things more clearly.

The calibration card used to show the voltage it found, with an arrow that looked like the miner would go there. Apply actually sets the found voltage plus a reserve. The card now points to what Apply sets and says the rest underneath, e.g. “found 1030 mV + 20 mV reserve · reserve capped at the starting voltage”. That cap is new information too: the reserve never takes a miner above the voltage it started from. A quick check is titled as such, and visitors who aren’t logged in are told how to apply instead of wondering where the buttons went.

WarpTune also checks voltages on its own while it runs. The card called that “Calibrating”, which made people (me included) think a calibration was running. It now says “Voltage check”, and at the voltage floor, where it keeps counting past its 200-share target, it says so instead of showing “405/200”.

The first real quick check ran yesterday on my BitForge Nano: both stages in 1 h 50 min instead of most of a night. At 650 MHz the chip errors went 0.45 → 0.52 → 0.96 % from 1050 down to 1030 mV and jumped to 3.1 % at 1020 mV, so it confirmed 1030 mV on 201 shares, the same voltage the full calibration had found a few days earlier.

Two smaller things: Admin → Workers shortens the address so the worker name stays readable, and a device added as NerdNOS that now runs WarpAxe no longer shows “HTTP 404”. The WarpTune guide has a Linux/systemd section now (someone asked whether it’s Mac only, it isn’t).

Still no mainnet block.

Repo: [dvb-projekt/dvb-WarpPool: Rust Bitcoin solo mining pool — Stratum V1 + V2, PWA operator UI, signed reproducible builds - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool) · Changelog in the repo.

-------------------------

dvb-projekt | 2026-10-10 20:44:37 UTC | #67

**v1.39.0 — WarpTune vs. the hand point, and a ratchet I had missed**

The device page now shows what the tuner gives you: per miner and in sum, what Eco saves in watts and what Max adds in hashrate, each against the miner’s hand point — the clock and voltage it would run without WarpTune. I went back and forth on the reference: the factory setting gives bigger and more comparable numbers, but for anyone who tuned by hand it would credit their own work to the tool, and on most of my miners it would have been an estimate. The hand point is the honest “without”, it is the factory setting for people who never changed it, and every miner has really run there, so it can be measured.

Measured means the pool’s accepted shares and the miner’s own power over the last week, a point counting from 200 shares and 30 minutes, with the share noise shown as ±. On my BitForge Nano the Max point (650 MHz) runs 8.2 W below its hand point at the same hashrate, the Bitaxe Gamma at 640 MHz 2.9 W below.

Building that turned up a bug. My NerdQAxe++ at its Eco clock had crept from 1140 to 1240 mV in three days, in 10 mV steps, while its chip error rate sat flat at 0.2 %. Each raise came from a 400-share vote at about 95 % of expected — inside the noise, but just under the bar — and the chip errors weren’t consulted because the error trigger was off. Now a near miss with flat chip errors counts as noise, not as a deficit, and such raises walk back down.

Still no mainnet block.

Repo: [dvb-projekt/dvb-WarpPool: Rust Bitcoin solo mining pool — Stratum V1 + V2, PWA operator UI, signed reproducible builds - Forgejo: Beyond coding. We forge.](https://git.warppool.org/dvb-projekt/dvb-WarpPool) · Changelog in the repo.
