# Telegram public groups, live bot read

> Source: Telegram Bot API via @foundation_community_bot (getMe, getWebhookInfo, getUpdates, getChat, getChatMemberCount, getChatAdministrators) plus the public pages https://t.me/s/the256foundation and https://t.me/s/heatpunks
> Collected: 2026-10-07
> Published: Unknown

The bot was added after the groups already existed. It can see new messages from the time it was added, and only if they are still in the update queue. This pull found no queued messages. It is not a history export. Do not treat the empty queue as "the groups are quiet."

## Bot

- Username: foundation_community_bot
- Webhook: not set
- Pending updates: 0
- Allowed updates: message, edited_message, channel_post, my_chat_member, chat_member
- getUpdates: ok, 0 updates

A 2026-09-17 Hydrapool community scan in the 256-community workspace also recorded an empty getUpdates. Same limit, not a new finding about conversation volume.

## @the256foundation

- Public page: https://t.me/the256foundation
- Web preview checked: https://t.me/s/the256foundation
- Type: supergroup
- Title: 256 FOUNDATION
- Description, from getChat: "Public group chat for the 256 Foundation. Our mission is simple: build the open-source Bitcoin mining ecosystem. If that stokes your 🔥 then get in here."
- Member count, getChatMemberCount, 2026-10-07: 211
- Same moment on https://t.me/s/the256foundation: 211 members, 24 online
- The web preview showed the title, description, and counts. It did not show message history. These are groups, not broadcast channels, so t.me/s does not list posts.
- Administrators, getChatAdministrators:
  - creator: econoalchemist (username econoalchemist)
  - administrator: Tyler (username tylerkstevens)
  - administrator: Rod (username rodbitkite)
- Earlier count from the 2026-09-05 community inventory pull: 208 members. That figure is a prior bot read, not a message archive.

## @heatpunks

- Public page: https://t.me/heatpunks
- Web preview checked: https://t.me/s/heatpunks
- Type: supergroup
- Title: Hashrate Heatpunks
- Description, from getChat: "The official Hashrate Heatpunk group chat. A community of builders working on the emerging hashrate heating industry. Mission: Marry the bitcoin mining and heating sectors to bring hashrate back home. HRHP Resources & Forum: https://heatpunks.org"
- Member count, getChatMemberCount, 2026-10-07: 175
- Same moment on https://t.me/s/heatpunks: 175 members, 21 online
- Web preview showed no message history.
- Administrators, getChatAdministrators:
  - creator: Tyler (username tylerkstevens)
  - administrator: Dylan (username tronsington)
  - administrator: Cody (username codyharris86)
- Earlier count from the 2026-09-05 community inventory pull: 171 members.

## What this file does not contain

- No message text, dates, or reply threads. The bot queue was empty and the public web preview does not expose group history.
- No posts were sent to either group.
