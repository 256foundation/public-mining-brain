# Colab wanted with 256 Foundation demo hydronic design

> Source: https://forum.heatpunks.org/t/colab-wanted-with-256-foundation-demo-hydronic-design/226
> Collected: 2026-10-10
> Published: 2025-11-30
> Registry ID: heatpunks-forum

ryan | 2025-11-30 21:10:43 UTC | #1

Hi y’all, [Mujina firmware](https://github.com/256foundation/mujina) dev here looking for mechanically-gifted collaborators. For the upcoming 256 Foundation [Telehash Fundraiser](https://x.com/bitcoinpark_/status/1965024832942395463), [NEMS](https://x.com/bitcoinpark_/status/1965024831726104726), and [Heatpunk Summit](https://denver.space/heatpunk_summit) events; I’d like to demo our full 256 Foundation open-source mining stack in a heat-reuse application—**a sous vide cooker**. That’s right, Bitcoin-purchased pasture-raised beef cooking live on stage with open-source mining hardware and software.

I envision a system with at least three open-source [emberOne/00](https://github.com/256foundation/emberone00-pcb/tree/master?tab=readme-ov-file#emberone00) 100W hash boards with water blocks, delivering heat at ~54 degC to a [water bath](https://anovaculinary.com/products/anova-precision-cooker-nano-3) with the meat. I think it’s feasible if we size the bath appropriately, insulate, and expect a long pre-heat time. Thermal guys please chime in.

The emberOnes are driven by our open-source [Libre-Board](https://github.com/256foundation/libreboard?tab=readme-ov-file#libre-board) control board, running Mujina firmware of course. And did I mention the system is hashing to our open-source pool software [Hydrapool](https://github.com/256foundation/hydrapool?tab=readme-ov-file#hydrapool) as well?

The problem is: I’m a software and electrical guy, not a mechanical guy. I could really use some collaborators on:

1. Water block design and construction, and

2. Hydronic system design: liquid, pumps, tubes, exchangers, etc.

Any advice—or better yet—offers to participate?

Honour and recognition in case of success.

-------------------------

Cody | 2025-12-01 16:49:17 UTC | #2

Wow, this looks really interesting!  Are you against using immersion instead of hydro?  It seems much easier and faster to iterate on than hydro(maybe i’m wrong here).

I guess the major advantage of hydro in this application is that you could reduce complexity by just using the sous vide water as the coolant(single loop).  There are of course drawbacks to that, but not if the product is to used infrequently.

But immersion has already been proven out for this use case.  RevHodl was sous viding rabbit last winter directly in immersion oil(vegetable oil in his case)

Anyway, can’t wait to see some of this tech in action!!

-------------------------

alro | 2025-12-01 18:47:45 UTC | #3

I am interested in helping out!

I am a mechanical engineer by trade, with some experience with pump systems from my last work. I can commit a few hours per week to hashing out a design, hope I may be of help.

-------------------------

ryan | 2025-12-02 21:54:50 UTC | #4

> Are you against using immersion instead of hydro?

Good idea, but in this case yes, I’m opposed. The open-source hardware is sort of the star of the show, so I don’t want to hide it in a tank. Plus, it’s scarce development hardware, so I want it to remain accessible for probing, repair, etc. and not get permanently gunked up.

-------------------------

ryan | 2025-12-02 22:15:32 UTC | #5

Welcome to the forum @alro, and thanks for volunteering! Please give me a few more days to see what develops in terms of help, and we’ll come up with some kind of plan.

Mechanically, I’m thinking it might be nice to gut, hack, or replicate one of these [sous vide heaters](https://anovaculinary.com/pages/find-your-anova-precision-cooker) and put a heat exchanger (and pump?) inside. I have a few. They have a propeller inside them which circulates the water bath. And they would conveniently clip onto the water tub.

Adding to my comment about immersion above: the closer this looks to an end-user product—the less an observer has to use their imagination—the better. Immersion seems less like a product to me.

-------------------------

tylerkstevens | 2025-12-06 00:44:05 UTC | #6

Yea the main thing that’s needed is a water block for the Ember One hashboard. Have you chat with Ryan Ramminger from [http://cryobytelabs.com](http://cryobytelabs.com) ?

I’m sure there are other services that could mock one up relatively quick from the dimensions in the KiCAD file! I might take a stab at this if I find the time.

Anyone good with CAD? @PizzAndy perhaps?

-------------------------

418Mining | 2025-12-06 18:09:51 UTC | #7

My CAD skills are… “juvenile”, in that I pretty much only use Tinkercad. I can, however, bend it to my will to accomplish some reasonably impressive things.

I’m also multi-disciplined in that I know my way around a soldering iron, electricity, some plumbing stuff, etc. (I was a Nuke ET in the USN many years ago.)

I’d be happy to lend my skills if you’d like them on the project. At the very least I’m good at rapid prototyping and getting functional designs done. Aesthetics aren’t my strongest point, but I don’t have a lot of ego there either so I’m happy to hand off an engineering-focused design to someone else to pretty-up.

-------------------------

PizzAndy | 2025-12-06 20:32:31 UTC | #8

> **tylerkstevens:**
>
> > nyone good with CAD? @

I’ve been summoned.

I don’t have any first hand experience with liquid cooling things, but I can certainly draw some fancy things in 3D and run thermal simulations.

-------------------------

ryan | 2025-12-09 17:50:06 UTC | #9

I’ll definitely reach out to Ryan Ramminger; that’s a good idea.

Schnitzel said that under 1 kW, we’re in a good position to reuse PC cooling gear, readily available on Amazon. So a custom water block that fits the e1/00—that’s compatible with the PC-cooling ecosystem—is probably what we need.

What do you all think about the system design? I’m imagining a loop through the water blocks into some kind of exchanger in the water bath. What liquid should we use in the loop? What is needed for a good heat exchange into the water bath? At what points should temperature be measured? I don’t need a secondary place to dump unneeded energy because this is Mujina, so I can modulate the energy production at the source.

-------------------------

alro | 2025-12-10 07:31:26 UTC | #10

Hi Ryan,

I actually have one of those Sous Vide heaters, I brought it home from work. I can tear it down and document the design.

I am currently in the midsts of finals, so I will be more available soon as they are over.

-------------------------

ryan | 2026-02-11 15:11:35 UTC | #11

Hey y’all, I just wanted to follow up and show everyone here what became of this. We demonstrated the following at the 256F Telehash and NEMS’26 at Bitcoin Park in late January:

[![IMG_0544](https://forum.heatpunks.org/uploads/default/optimized/1X/ed2ca609e072556be7345a83dee5f94ac1958d59_2_666x500.jpeg)IMG_05441920×1440 603 KB](https://forum.heatpunks.org/uploads/default/original/1X/ed2ca609e072556be7345a83dee5f94ac1958d59.jpeg)

That’s the full 256 Foundation open-source mining stack demonstrating a heat-reuse application—a sous vide cooker. Or with my Heatpunk hat on, maybe I should say: it’s a sous vide cooker that co-produces bitcoin and freedom for all of humanity. Plus the steak was tasty.

Check out Schnitzel’s X thread for some more [pictures and details](https://x.com/Schnitzel/status/2014833750647988553).

We’ll be bringing this to the Heatpunk Summit in a couple of weeks. If you’re there, come see it for yourself!

A big shout-out to Ryan Ramminger from [http://cryobytelabs.com](http://cryobytelabs.com) for coming up with a dope water block design, producing several himself at the last minute, and helping with pumps and tubing as well. Check these things out! He had the brilliant idea to have ports on both sides of the water block, and extend the blocks off the edge of the board, so we could stack together three in series. It turned out so well. Render and reality:

[![Screenshot 2026-02-11 at 09.04.49](https://forum.heatpunks.org/uploads/default/optimized/1X/294b2af7cb711027223e4ab0d9d4e4449097b627_2_520x500.jpeg)Screenshot 2026-02-11 at 09.04.49806×774 85.6 KB](https://forum.heatpunks.org/uploads/default/original/1X/294b2af7cb711027223e4ab0d9d4e4449097b627.jpeg)

[![photo_2026-02-11 09.03.18](https://forum.heatpunks.org/uploads/default/optimized/1X/e059949c8ba3731a922b70d1703da1097662a1c4_2_666x500.jpeg)photo_2026-02-11 09.03.181280×960 165 KB](https://forum.heatpunks.org/uploads/default/original/1X/e059949c8ba3731a922b70d1703da1097662a1c4.jpeg)

-------------------------

Plunger | 2026-02-12 01:38:52 UTC | #12

My mouth started watering when I saw the cooked steak on the plate. Is this project going to be at the Summit?

-------------------------

ryan | 2026-02-21 20:03:02 UTC | #13

Indeed, it will be at the Heat Punk Summit next week.
