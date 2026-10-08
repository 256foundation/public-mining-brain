# Buying a Bitaxe

> Sources: Bitaxe.org (buy page), collected 2026-10-07; Bitaxe.org (legacy list page), collected 2026-10-07; bitaxeorg (legitlist README), collected 2026-10-07; Bitaxe.org (home page), collected 2026-10-07; bitaxeorg (bitaxeGamma README), collected 2026-10-07
> Raw: [bitaxe.org buy](../../raw/ecosystem/bitaxe-org-buy.md); [bitaxe.org legacy list](../../raw/ecosystem/bitaxe-org-legacy-list.md); [legitlist README](../../raw/ecosystem/github-bitaxeorg-legitlist.md); [bitaxe.org home](../../raw/ecosystem/bitaxe-org-home.md); [bitaxeGamma README](../../raw/ecosystem/github-bitaxeorg-bitaxegamma.md)
> Updated: 2026-10-07

## Overview

Bitaxe designs are open, so anyone can build and sell them. That makes it hard for a buyer to know who is selling genuine hardware. The project answers this with a public vendors list on bitaxe.org, fed by a GitHub repository called legitlist. Vendors apply with a pull request, the community reviews it, and maintainers decide. An older, hand-curated list is kept as the legacy list.

## Why buy instead of build

The Bitaxe READMEs describe building a board as an advanced project. The Gamma README says that if you are not looking for a project, it might be best to buy one pre-assembled from one of the many sellers. For the build route see [Building a Bitaxe](building-a-bitaxe.md).

## The vendors list on bitaxe.org

The buy page shows vendors with a region filter. Each entry gives a region, a country and the vendor's name. In the collected snapshot the countries span Europe, North America, South America, Asia Pacific and India. Europe has the most entries. The page links to the legitlist README for anyone who wants to become a vendor.

Bitaxe.org's home page uses three labels for the miner: open source, standalone and legit.

## How legitlist works

The README calls legitlist the community-verified list of trusted Bitaxe vendors. Its main points:

- It is not a pay-to-play directory. There are no paid placements.
- It is a public trust signal that is community-reviewed and maintainer-approved.
- Final inclusion is always at maintainer discretion. It is based on community trust, listing quality and alignment with the Bitaxe open-source ecosystem.
- Only vendors marked as active should be displayed on the site.

The process is: a vendor submits a pull request, the community reviews it, maintainers merge it, and the vendor is listed on the site. The discussion happens in the pull request itself.

### What a vendor submits

Each vendor is two files:

- A JSON file with the shop's name, website, region and social accounts.
- A logo. A square image of 400×400px is recommended, with a maximum size of 200 KB.

The supported regions are Europe, North America, South America, Asia Pacific, Middle East, Africa and India. A vendor guide in the repository gives the step-by-step path.

If maintainers request changes to an open pull request, the vendor has two weeks to make them. After that the pull request is closed and has to be reopened.

### Reporting a vendor

Anyone can report a vendor that should not be listed by opening an issue. The README says every report is reviewed and every removal is transparent.

## The legacy list

Bitaxe.org also keeps a legacy list. The page describes it as a curated list by Skot of sellers who support the Bitaxe project and open source Bitcoin mining. The snapshot shows entries by region and country only. It covers Europe, North America, South America, Central America, Asia Pacific and Africa. The page footer states that the Bitaxe name and logo are internationally trademarked by bitaxeorg.

## See Also

- [Bitaxe Model Lineup](bitaxe-models.md)
- [Building a Bitaxe](building-a-bitaxe.md)
- [Bitaxe and Open Source Miners United](bitaxe-and-osmu.md)
