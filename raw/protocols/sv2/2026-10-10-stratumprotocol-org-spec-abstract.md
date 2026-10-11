# Stratum V2 Specification — 0. Abstract (+ full chapter index)

> Source: https://stratumprotocol.org/specification/00-abstract/
> Collected: 2026-10-10
> Published: spec maintained in github.com/stratum-mining/sv2-spec
> Registry ID: stratum-v2

(/specification/06-job-declaration-protocol/)

 (/specification/07-template-distribution-protocol/)

 (/specification/08-message-types/)

 (/specification/09-extensions/)

 (/specification/10-discussion/)

Search pages and sections Jump to page or section  Abstract   Motivation   Design Goals   Protocol Overview   Protocol Security   Mining Protocol   Job Declaration Protocol   Template Distribution Protocol   Message Types   Extensions   Discussion

View on GitHub (https://github.com/stratum-mining/sv2-spec/blob/main/00-Abstract.md) Ask a question (https://github.com/stratum-mining/sv2-spec/discussions/new?category=q-a&title=Question%3A+Abstract&body=Question+about+the+specification%3A%0A%0Ahttps%3A%2F%2Fgithub.com%2Fstratum-mining%2Fsv2-spec%2Fblob%2Fmain%2F00-Abstract.md%0A%0A---%0A%0A)

# 0. Abstract   (#0-abstract)

The current stratum protocol (v1) is used prevalently throughout the cryptocurrency mining industry today, but it was never intended nor designed to be an industry standard.

This document proposes a new version of stratum protocol that addresses scaling and quality issues of the previous version, focusing on more efficient data transfers (i.e. distribution of mining jobs and result submissions) as well as increased security.

Additionally, the redesigned protocol includes support for transaction selection by the miners themselves, as opposed to the current version of the protocol in which only the pool operators can determine a new block’s transaction set.

There are some trade offs necessary to make the protocol scalable and relatively simple, which will be addressed in the detailed discussions below.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC2119.

We keep the name "Stratum" so that people will recognize that this is an upgrade of the widespread protocol version 1, with the hope that it will help gather support for the new version more easily.

 (/specification/01-motivation/)
