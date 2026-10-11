# Heatpunks forum capture report (capture-loop A1)

> Registry ID: heatpunks-forum
> Collected: 2026-10-10

- Upstream: 119 topics per about.json (682 posts, 138 users, 624 likes); **101 topics publicly listed** via `/latest.json` (2 pages, no `more_topics_url` past page 1). The 18-topic delta is staff-only/unlisted/system topics not visible anonymously.
- Captured: **81 topics** (all posts each, incl. a second `posts.json` fetch for t/55 posts 18-24 which Discourse paginates).
- Census: `2026-10-10-forum-heatpunks-census.md` (full 101-topic table with id/created/last-posted/posts/title).

## Skipped (20) — one-line reasons

- 5 Welcome to Hashrate Heatpunks! — intro/welcome boilerplate.
- 97 50 million infrastructure for 2.4 billion project — speculative chatter, no technical content.
- 100 Bitaxe btc address — basic support Q&A (stratum user field), no signal.
- 113 BTChel expo in Finland — event announcement, no content.
- 119 TIDES vs FPPS Payouts — 1-post question; superseded by captured experiment thread 140.
- 122 ATL BitLab hackathon June 2025 — event announcement.
- 129 Home Assistant dashboards — dashboard show-and-tell chatter; HA integrations covered in 244.
- 131 Nostr NIP-05 heatpunks.org — community meta/npub list.
- 170 Looking for work — job-seeking post (per skip rules).
- 195 September 9, 2025 significant day — personal musing.
- 203 Summit Landing Page is Live — summit logistics announcement.
- 208 Heatpunk Movement Mentioned in Forbes — one-post press link drop.
- 218 Heatpunks Telegram Group Chat Now Public — community meta.
- 220 Call for Heating Industry Professionals to attend HPS — event logistics.
- 229 BACnet integration — one-post open question, no replies, no content beyond a link.
- 264 Hashin' for heat with solar — support testimonial, no technical content.
- 267 Exergy HA Office Hours — bare event widget (1 post).
- 276 2027 Summit Waitlist Open — waitlist logistics.
- 279 Updated event info recurring HA office hours — bare event widget (1 post).
- 282 PizzAxe pizza bag warmer — one-post show-and-tell, no discussion.

## Fetch notes

- Initial parallel fetch batch hit nginx 429s; all retried OK with serial backoff. No topic 404s.
- t/55 (24 posts) required `/t/55/posts.json?post_ids[]=` follow-up for posts 18-24 (Discourse chunks long topics); merged.
- All 81 captures verified: 4 header lines present, all upstream posts present, separator count == posts-1.
