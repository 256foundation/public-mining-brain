# A Hashrate Retainer for your Plumber

> Source: https://forum.heatpunks.org/t/a-hashrate-retainer-for-your-plumber/235
> Collected: 2026-10-10
> Published: 2025-12-30
> Registry ID: heatpunks-forum

Cardiac | 2025-12-30 03:04:10 UTC | #1

Seeking ideas on how to structure the business side of allocating hashrate to your favorite plumber (or tradesman generally) to create a retainer of sats in reserve to pay for periodic maintenance or even emergency service.

Is there even a concept of passive income for tradesmen that could be studied as an example?

Starbucks has a rewards system that’s all fiat chicanery, when does your local jiffy lube start heating their garage bays with bitcoiner miners to generate customer rewards and/or employee benefits funding?

I think the tech is maturing in this direction with things like ehash and stratum v2 that are going to enable a ton of new business models and incentive structures that are mutually beneficial.

What are the ideas, experiences, and interfaces waiting to be built by the AI slaves?

-------------------------

Cody | 2025-12-30 15:47:27 UTC | #2

I’ve been thinking about this lately as well.  I do think that having a portion of hashrate directed to the installer is a decent incentive to keep the equipment maintained.  For my systems the payment split is already possible.  Epic control boards have a “Hashrate Split” feature that could be used for this.

One thing to figure out is who has admin access to the miners?  For reliable hashrate splitting you probably want the home owner to be able to get into the miners and adjust things.

-------------------------

SoftwarmLLC | 2025-12-30 19:23:40 UTC | #3

I split the share on the pool account for each customer, and we can both view the pool for full transparency. Hashrate splits on the machine are another option, but its kind of tedious when someone has 50 machines.

Also, the last thing I want to do is receive all the BTC production and then split it manually, or have them do the same. It becomes a tracking nightmare and you also run the risk of becoming a money services business. No thanks.

-------------------------

thak777 | 2025-12-31 13:02:00 UTC | #4

What pool(s) do you use for pool splitting?

-------------------------

Cardiac | 2025-12-31 13:33:10 UTC | #5

> **Cody:**
>
> > One thing to figure out is who has admin access to the miners? For reliable hashrate splitting you probably want the home owner to be able to get into the miners and adjust things.

I think this is too biased toward technical bitcoiners. Most users (assuming broad consumer adoption) won’t want to or care to manage their hashrate, the same way they don’t tune or monitor anything other than the thermostat or toilet. Any additional friction is a deterrent in our modern age of frictionless dopamine.

> **SoftwarmLLC:**
>
> > I split the share on the pool account for each customer

Could you elaborate? Is this a feature within the pool itself?

> **SoftwarmLLC:**
>
> > its kind of tedious when someone has 50 machines.

This begs the question of control. Manually logging into each web interface for more than 1 machine is tedious but there is software like pyasic and/or asic-rs that makes this more manageable. Ideally, these tools get a nice UI in front of them but that will take some time, methinks. I am hopeful for the Proto Fleet system that will allegedly be open source and enable users to more easily manage their machines in a unified interface.

> **SoftwarmLLC:**
>
> > split it manually,

Agreed. Similar to nostr zap splits and podcasting 2.0 splits, the % of the split should be automagical, otherwise what’s the point of programmable money?

> **thak777:**
>
> > What pool(s) do you use for pool splitting?

What do you mean by “pool splitting”?
