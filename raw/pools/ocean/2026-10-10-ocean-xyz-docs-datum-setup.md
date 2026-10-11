# OCEAN docs — DATUM Setup Guide

> Source: https://ocean.xyz/docs/datum-setup
> Collected: 2026-10-10
> Published: 2024-10-18
> Registry ID: ocean-pool

---

How To Install DATUM and set up a DATUM Gateway

## Overview

DATUM (Decentralized Alternative Templates for Universal Mining) is a brand new bitcoin mining protocol that allows anyone to create their own block templates using their own Bitcoin node. They can mine on pools that offer Datum support or solo mine without needing a third party to set up a server for them.

DATUM is currently in public beta. To download source code or install binaries click here.

## Pre-setup

You will need to be running a bitcoin node with performant enough hardware to download and validate new blocks as quickly as possible. The Bitcoin node is the heaviest part of the setup.

## Setup

- Step 1: Set up the Bitcoin node that will become your DATUM Host Node (DHN) and sync it with the entire blockchain.

*NOTE: We recommend setting up your Bitcoin Node with Bitcoin Knots as it has more template controls than CORE.*

- Step 2: Configure your DHN host node to make the blocks you want your miners to mine.
- Step 3: Ensure your DHN is network accessible by your miners.
- Step 4: Install and configure the DATUM Gateway.
- Step 5: Configure your miners with the following settings:
- Username should be the same as if mining on OCEAN without DATUM, your Bitcoin payout address with an optional worker name appended after a dot.
- Password should be “x” or blank or anything short. It is ignored.
- Point your miners hash to stratum+tcp://your_datum_node_ip:23334

If you need any additional support, please don't hesitate to reach out to mining@ocean.xyz, Jason (@wk057) or Leo (@leo_haf) on X or Nostr.

---

> Capture note: "click here" (public beta downloads) links to https://github.com/OCEAN-xyz/datum_gateway/releases/latest — the DATUM Gateway repo with source and prebuilt binaries.
