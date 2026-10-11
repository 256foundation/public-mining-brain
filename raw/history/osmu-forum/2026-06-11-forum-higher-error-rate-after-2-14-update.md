# Higher Error Rate After 2.14 Update

> Source: https://osmu.xyz/t/higher-error-rate-after-2-14-update/40
> Collected: 2026-10-10
> Published: 2026-06-11
> Registry ID: osmu-forum

monti55 | 2026-06-11 13:39:18 UTC | #1

After updating to 2.14 I’ve noticed the error rate over time has increased. I have a 4 hour running average of the error rate for monitoring and its increases from 0.5% to 0.7% without changing settings. My average stat polls the API every 60 seconds.

I’ve seen people complain and revert to 2.13.x but I was wondering what is the reason for a higher error rate? Sometimes I feel like knowing the error rate is detrimental to the experience since I’m trying to min max the efficiency and error rate.

My rudimentary understanding would be the new websocket polling changes how often the error rate is computed. The actual error register value is the same but with faster updates the number of “good” hashes has decreased leading to a higher percentage.

Otherwise love the update!

-------------------------

mutatrum | 2026-06-20 19:24:40 UTC | #2

Internally in the ASIC the error rate is a counter. So it shouldn’t be different if the rate you read it is different. It’s possible the way it’s converted to a percentage is skewing the values now it’s read more often (once a second, instead once every 5 seconds before websockets).

-------------------------

Lidamao | 2026-07-31 01:49:47 UTC | #3

That’s nothing,My device show 100% error and 400Ths

-------------------------

WantClue | 2026-07-31 11:04:48 UTC | #4

Than the asic is defect. With the newest firmware versions we changed to actually read the asic registers and with that you now see issues that have not been visible before. Even if older versions show you hashrate that looks nominal it won’t show issues because we never read them previously
