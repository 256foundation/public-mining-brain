# bitaxeorg/legitlist release notes (4 releases)

> Source: https://github.com/bitaxeorg/legitlist/releases
> Collected: 2026-10-07
> Published: Unknown

## v1.2.1 (v1.2.1)

- Published: 2026-06-04
- Link: https://github.com/bitaxeorg/legitlist/releases/tag/v1.2.1
- Prerelease: False

﻿## What's Changed
- Added PR metadata validation for vendor submissions.
- Improved validation workflow coverage for validation tooling changes.
- Skips vendor metadata checks for maintenance PRs that do not touch `vendors/` or `logos/`.
- Removal/deactivation PRs no longer require vendor confirmation rows.
- Documented accepted vendor PR title prefixes.


## v1.2.0 (v1.2.0)

- Published: 2026-03-20
- Link: https://github.com/bitaxeorg/legitlist/releases/tag/v1.2.0
- Prerelease: False

## Highlights
- Added TikTok and Nostr social support across schema, validation, and Framer sync.
- Simplified vendor JSON by removing the logo field; logo is now inferred from slug via logos/slug.png, logos/slug.jpg, or logos/slug.webp.
- Tightened slug and filename rules to lowercase single-hyphen format to prevent case-mismatch failures.

## Reliability and Validation
- Unified CI and local validation so both run the same repository validator.
- Hardened validator handling for malformed JSON input.
- Improved sync resilience with validation preflight before Framer writes.
- Prevented disconnect errors from masking primary sync failures.
- Made sync/validation path resolution repo-root safe to avoid CWD-dependent ENOENT issues.

## Documentation and Onboarding
- Updated vendor and maintainer docs to reflect approval criteria and current validation behavior.
- Clarified first-time submission guidance and social-key constraints in the PR template.

## Data Hygiene
- Removed test/mock vendor data and reset to a clean baseline before reintroducing production entries.


## v1.1.0 (v1.1.0)

- Published: 2026-03-12
- Link: https://github.com/bitaxeorg/legitlist/releases/tag/v1.1.0
- Prerelease: False

## legitlist v1.1.0

This release stabilizes legitlist for public end-to-end testing and hardens the vendor review/sync pipeline.

### Highlights
- Switched Framer sync to soft-sync mode (no automatic stale-item deletion)
- Visibility model standardized around vendor active status
- Vendor filename guardrails strengthened in local + CI validation
- HTTPS-only validation enforced for website and social URLs
- Workflow hardening with read-only token permissions and updated Actions runtime
- Mock data reset to 15 vendors covering all supported regions
- Mock logos updated to distinct monochrome assets for better visual QA
- Logo CDN URLs pinned to commit SHA to avoid stale cache artifacts

### Current status
- Validation checks are green
- Sync workflow is stable across repeated runs
- Ready for full public-flow E2E testing

## v1.0.0 (v1.0.0)

- Published: 2026-03-12
- Link: https://github.com/bitaxeorg/legitlist/releases/tag/v1.0.0
- Prerelease: False

## legitlist v1.0.0

`legitlist` is the community-verified list of trusted Bitaxe vendors.

Open-source hardware needs open-source trust. This release defines the public process for getting listed, reviewing vendors in the open, and keeping the directory transparent, auditable, and community-driven.

## What legitlist is

- a public registry of trusted Bitaxe sellers
- a transparent review process run through GitHub
- a structured vendor data system with automatic validation
- an automated sync from approved listings to Framer CMS

## What ships in v1.0.0

### Public vendor listing workflow
- step-by-step vendor onboarding guide for non-technical users
- browser-only submission flow
- structured pull request form for vendor details and community context

### Validation and data integrity
- standard vendor listing format in `vendors/{slug}.json`
- vendor logo support in `logos/{slug}.{ext}`
- automatic validation for required fields, naming consistency, and logo size
- matching local and CI validation

### Sync and publishing automation
- automatic sync to Framer CMS after merge to `main`
- managed collection upsert by vendor slug
- publish/deploy flow with retries and diagnostics
- changed-path detection to avoid unnecessary publishes
- workflow concurrency protection

### Open review and accountability
- public discussion on every listing through pull requests
- community reporting flow for concerns
- support for listing updates, deactivation, and removal in the open
