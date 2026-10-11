# Pogolo - Local Golang pool

> Source: https://osmu.xyz/t/pogolo-local-golang-pool/28
> Collected: 2026-10-10
> Published: 2026-05-30
> Registry ID: osmu-forum

0xf0xx0 | 2026-05-30 18:28:57 UTC | #1

pogolo is a db-less solo mining pool, designed to serve your LAN swarm :3

it’s loosely based on public-pool, and is written in Go. It’s easily configurable with a well-documented TOML file. visit the [repo here](https://github.com/0xf0xx0/pogolo) for install instructions uwu

![showoff](https://osmu.xyz/uploads/default/original/1X/576e1b100672f0179d5f71959c9c3d44891f7b43.png)

-------------------------

skot | 2026-06-19 01:06:08 UTC | #2

Love to see all the open source mining pool development happening; LFG! Can you tell us more about the pros and cons of db-less?

-------------------------

0xf0xx0 | 2026-06-19 17:39:17 UTC | #3

yee! going db-less makes pogolo a lot leaner on system resources and upkeep, as theres no database to install and maintain alongside the pool and the bitcoin node. the downside is theres no long-term storage, so you can’t track your stats over time.  i dont want a hard dependency on valkey or postgres or whatever, pogolo should be a pool you can just grab and run, without extensive setup. i will be adding a prometheus endpoint eventually, for optional stats storage :3

-------------------------

0xf0xx0 | 2026-07-07 17:32:43 UTC | #4

v1.1.4 is out :3 mainly adding zmq support for faster block notifications, and lots of smaller fixes and tweaks uwu

im also requesting cpu profiles, generated with `--prof`, for optimizing future builds.

![image](https://osmu.xyz/uploads/default/original/1X/bad3e5f9ad67c1ddf145107ce7032ac1d7b22563.svg)

      [GitHub](https://github.com/0xf0xx0/pogolo/releases/tag/v1.1.4)

![image](https://osmu.xyz/uploads/default/optimized/1X/dfcfdfae2596f97a0d0ff62b1e15cbb2252b5593_2_690x345.png)

### [Release v1.1.4 · 0xf0xx0/pogolo](https://github.com/0xf0xx0/pogolo/releases/tag/v1.1.4)

New

new error when a share is submitted while the pool is switching to a new job and the client hasn't yet
zmq hashblock listener has been added for rapid block change and reorg updates
add random...

-------------------------

0xf0xx0 | 2026-07-16 03:22:23 UTC | #6

hotfix out for v1.1.4, i fucked up version validation x33

![image](https://osmu.xyz/uploads/default/original/1X/73d30203652514eb1457c5571fe576006b1da788.svg)

      [F0xf0rge: Build the world you wish to live in](https://git.0xf0xx0.eth.limo/0xf0xx0/pogolo/releases/tag/v1.1.4-hotfix)

![image](https://osmu.xyz/uploads/default/optimized/1X/95d83fc0b8e035156b657db0c1aef6627debf14a_2_690x345.png)

### [v1.1.4-hotfix - 0xf0xx0/pogolo](https://git.0xf0xx0.eth.limo/0xf0xx0/pogolo/releases/tag/v1.1.4-hotfix)

# Fix
- share version validation was incorrect, revert to validating the mask
- related, properly process mask according to bip-310

**Full Changelog**: https://git.0xf0xx0.eth.limo/0xf0xx0/pogolo/compare/v1.1.4...v1.1.4-hotfix

-------------------------

0xf0xx0 | 2026-09-02 03:26:29 UTC | #8

![aa-choo](https://osmu.xyz/uploads/default/original/1X/cc90c33d0039062a9973c1431dcd08e915a52b3e.png)

-------------------------

0xf0xx0 | 2026-09-03 19:42:59 UTC | #9

1.1.5 is out, bringing small perf improvements to keep pogolo at the top in its class :3 [Release v1.1.5 · 0xf0xx0/pogolo · GitHub](https://github.com/0xf0xx0/pogolo/releases/tag/v1.1.5)

also on umbrel, we now have a webui forked from bitcoin cores :3

![home page](https://osmu.xyz/uploads/default/original/1X/7404f7b2874b42f4b12ad49cf630428a477a7c3f.png)

**More screenshots**

![insights page](https://osmu.xyz/uploads/default/original/1X/b068e725bc63986b47af712255d6b9b0d1f91f30.png)

![gopher stats](https://osmu.xyz/uploads/default/original/1X/367b3fb0a7b9ac07c6f981783fe92a88278d39e2.png)

![settings page](https://osmu.xyz/uploads/default/original/1X/d2347a5e035a20033139ebb31bdd0e3020f98368.png)

![connection qr code](https://osmu.xyz/uploads/default/original/1X/5e3ee7a2a43e3d90c484911af5d370f68477634c.png)

-------------------------

0xf0xx0 | 2026-09-14 19:17:25 UTC | #10

and today brings 1.1.6, with native SV2 support! [Release v1.1.6 · 0xf0xx0/pogolo · GitHub](https://github.com/0xf0xx0/pogolo/releases/tag/v1.1.6)

-------------------------

WantClue | 2026-09-29 21:12:15 UTC | #11

keep us posted, maybe we can automate a notification in here for updates

-------------------------

0xf0xx0 | 2026-10-08 02:48:07 UTC | #12

automated notifs would be pretty fire ngl

![sneak peek of the next pogolo release, with a vanity sv2 authority key and backend sync waiting](https://osmu.xyz/uploads/default/original/1X/2dcb598fb53eab95fb736550e2eafb20945617f7.png)

quietly workin hard getting sv2 up to par with SRI, recently implemented a static authority key that can be generated with `pogolo --generate-authority-key`

might change the flag name and/or add shorter aliases

by default pogolo generates an ephemeral authority key on startup, as its not needed on the lan, but if wanted its there uwu

i also wrote a [vanity key grinder](https://git.0xf0xx0.eth.limo/0xf0xx0/stratumv2/src/branch/master/examples/grinder/pubkeygrinder.go), thats how i got the `9bSV2` :3

also, finally implemented a backend sync wait on startup kekeke

it didnt really matter but might as well not serve work on old blocks, non?

it waits for the backend to exit IBD and be synced to 99% before it starts the template loop, though the backend can fall out of sync later (imo, the getblockchaininfo call is too slow for the loop, i want new jobs to be fast after all :3).

for the webui side, i likely need to include a small go binary to (re)generate an authority keypair, i am *not* maintaining a second keygen impl lmfao

it has support for displaying the authority key and embedding it in the qr code, im too lazy to start the umbrel dev container rn so poke me if you want to see a screenshot i forgot i recorded a gif when i did it lol

![gif showing the connection info changing when switching between sv1 and sv2](https://osmu.xyz/uploads/default/original/1X/f84d45a8c7afb48ea35ea75d2918471d2aa59403.gif)

-------------------------

0xf0xx0 | 2026-10-08 03:11:37 UTC | #13

also forgot to link, my sv2 go module is at [0xf0xx0/stratumv2: A Golang library for the Stratum V2 Protocol - F0xf0rge: Build the world you wish to live in](https://git.0xf0xx0.eth.limo/0xf0xx0/stratumv2) and mirrored out to github, same name and repo name

if youre a go dev or know one, give it a try and tell me how it is so far uwu its very much a WIP and any tips/bug reports are welcome

-------------------------

WantClue | 2026-10-08 15:58:46 UTC | #14

Im thinking about TLS with pp e.g. you always need to reboot the process to read the new certificate but there must be a way of changing that live. Haven’t digged into it lately. But what about pogolo, do you support some native switch there e.g. with certificate managers ?

-------------------------

0xf0xx0 | 2026-10-08 17:04:35 UTC | #15

no, i consider tls to be out of scope for the lan, and currently recommend using a reverse proxy to handle it. sv2 is a better alternative for encryption imo, its grown on me as ive been implementing it and it does end up being slightly faster to process.

-------------------------

0xf0xx0 | 2026-10-08 20:00:43 UTC | #16

oh! i forgot to mention i implemented sv2 share batching :3

it batches shares into windows (by default, 15 seconds) before sending the ack. if a share comes in before the time is up, the window gets extended by half of the remaining time.

-------------------------

WantClue | 2026-10-09 11:17:01 UTC | #17

true, i just don’t know how many ppl will use sv2 in that regard. If it’s only about security tls beats an entire sv2 impl IMO

-------------------------

0xf0xx0 | 2026-10-10 18:11:08 UTC | #18

yeah im unsure, if its asked for i might look into implementing it uwu

on the other paw i dont wanna incentivize usin pogolo on the public web x3 id rather push people towards [m45core](https://github.com/M45Core/M45-goPool) for that.
