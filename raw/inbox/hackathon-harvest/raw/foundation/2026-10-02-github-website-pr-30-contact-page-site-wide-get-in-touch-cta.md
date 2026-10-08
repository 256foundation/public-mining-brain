# 256foundation/website pull request #30: Contact page, site-wide get-in-touch CTAs, and footer/Our Work copy

> Source: https://github.com/256foundation/website/pull/30
> Collected: 2026-10-07
> Published: 2026-10-02

- Repository: 256foundation/website
- Type: pull request
- Number: 30
- State: closed
- Author: tylerkstevens
- Opened: 2026-10-02
- Closed: 2026-10-02
- Labels: none

## Description

## Summary

One PR for the full round: a dedicated **`/contact`** page, a get-in-touch path on every page, and a handful of small copy edits.

### Contact page
- New `app/contact/page.tsx`: the shared `ContactForm` plus the general email **contact@256foundation.org**.
- Added to `app/sitemap.ts` and to the footer **Resources** column.
- The form posts client-side to Formspree (`formspree.io/f/xkndjepy`) — verified end-to-end (200 `{ok:true}` and the in-page success state).

### Relink
- `/#contact` → `/contact` in the header, footer, and mobile nav, and in the Libre Board article.
- The home page keeps its own `id="contact"` section and full form, so old `/#contact` links still land on a working form.

### Contextual contact links (site-wide)
- Secondary **Get in touch** action where a close already exists: `/our-work`, `/projects`, `/community`, `/telehash`, newsroom articles.
- Shared contextual `PageCTA` closer (primary Donate + secondary Get in touch, tailored copy) where there was no close: `/mission`, `/faq`, `/newsroom`, `/grants`, `/grants/announcements`, `/donate`, `/community`.

### Copy
- Footer: general email under the 501(c)(3) line; tagline → "Open-Sourcing Bitcoin Mining".
- `/our-work` close: Linux Foundation line on its own line; primary button → "Support with a Donation →".
- Contact form: label "Name / Nym", message placeholder "What's up?".

### Tests
- `tests/contact.test.mjs`: page carries the form/email, nav + footer + sitemap point at `/contact`, no `/#contact` left in nav, footer lists the email, home anchor preserved.

## Verification
- `npm test` — 50/50 pass
- `npm run lint` — 0 errors (7 pre-existing `<img>` warnings)
- `npm run build` — green
