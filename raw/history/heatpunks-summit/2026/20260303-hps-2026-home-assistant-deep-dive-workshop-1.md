# HPS 2026 — Home Assistant Deep Dive (Workshop 1)

> Source: https://www.youtube.com/watch?v=k_x48ErmSh8 (2026 Heatpunk Summit playlist PLgYVdSZznAdM7JVqScdZcKJ5i4ILABNC4; channel: The Space)
> Collected: 2026-10-10
> Published: 20260303
> Registry ID: heatpunk-summit-2025
> Posture: extract (auto-caption transcript; machine captions, no speaker labels)

[00:00:00] All right, gentlemen. Thanks for joining me. >> Does anyone know what Home Assistant is? >> Other than my bear friend over here. Does anyone use Home Assistant? Hey. [laughter] All right. So, Home Assistant is at its basic. It's just a way to automate things at home. Like that's low or highest level, but you can get weird with it. Um, these things run great on just like normal hardware.

[00:00:33] You start at home assistant.io. You can buy it from them if you want or you just run it on a pi or in a container on a proxmox server or whenever they release it. Start start 9 040 that's been promised to us for two years. I ran the alpha and the beta. It works. It's just not publicly released yet. Uh you can get it. But anyways, Home Assistant is best viewed I think as an aggregator of everything you can tie in high level.

[00:01:09] There are this is a technical term a gazillion integrations you can integrate into this. uh starting with, you know, various main products that you see like you can get at Home Depot or stuff that integrates with your Apple HomeKit and such stuff from IKEA. Um you can utilize Ziggb or Bluetooth or Wi-Fi. Pretty much any protocol you can integrate into Home Assistant. And so like these are just some of what is available. Let's get rid of the featured tag.

[00:01:40] And then you can see all this that's going to be on the recording. Um, there's I'm just in a like there's you can integrate most everything. Some stuff you can run locally and not have to go to a third party server. Other stuff you have to go through a third party server. I'm finding that with Claude you can take out the middleman and kind of hack everyone's API to run it locally, but we'll talk about that later. Um, when you add things to Home Assistant, it it's going to want to like make a dashboard.

[00:02:15] So, this is I didn't make this. Home Assistant made it itself. It can break out into areas like bathroom, bedroom, crawl space, etc. Give you summaries of what's on. So, these are my lights. None of them are on this. We are looking at my home right now. I think this dashboard sucks. Uh, it's useful for like popular stuff you use or seeing what's on, but you can get crazy with it. Make your own. So, here is like one demo dashboard I've created covering my my house.

[00:02:47] Looks fine on a computer, but on your phone, you might want something else. So, this guy looks great on my phone. I This all stacks up. I can go into my office and see everything in my office and put that away and turn things on and off. It works pretty well. So high level you can kind of add in whatever you want. Uh you can be as simple as going into the settings. There's so much in this. I'm not going to have time to show everything. Uh Home Assistant is insanely powerful, but like let's start at the basics.

[00:03:23] This is everything connected to my home assistant. So alarms, backups, Bluetooth, Bond is a is a bridge. So I can talk to uh different fans in my house. You can build your own. We built a DATM gateway. We built a BitAx integration. You can click into that and see all the stats about your Bitax. Uh Home Assistant was in no way, shape or form built for Bitexes. But because it's open source and you can build in whatever code you want, you can add in whatever you want, such as Bitex.

[00:03:57] And the API for Bitex is great. It reports a whole bunch of stuff that you don't really care about, but it's there and it looks cool. Additionally, there's like this is a Home Depot product. Uh you can bring in weather and different controllers and such. Anything you want to monitor, odds are there is a way to bring it into Home Assistant. And the beauty of that is you don't have to scroll through 20 different apps in your phone, like to turn on one light over here and go to a different app and turn on a fan over here. You can see all of it in one place which brings sanity to my life.

[00:04:30] What's up, >> Travis? Y >> API >> 100%. So, you can add in forecasting. You can add in a script or an automation that allows you to look one day into the future for what the forecast is supposed to be. like, oh, it's snowing and it's going to be freezing. Crank the boiler. Crank the miner that's going to heat the slab. And then, additionally, you can have temperature sensors throughout the slab or at the input or output of the slab and make sure there's flow.

[00:05:05] Make sure the temperatures are what you want them to be. And can also control the pump speed. You can you can anything you want to control, you can add into this. You might have to get kind of hacky with it, but it works. Um, I particularly like, so, as I mentioned, you can use Wi-Fi, Z-Wave, that may be new to you. ZigGB, that's another one. Uh, Bluetooth, probably pigeon carrier if you wanted to. Um, everything integrates. I really like ZigGB. Uh, you don't rely on internet for it.

[00:05:36] It's a mixes mesh network. Oh, that one's down. Uh, and everything kind of talks to each other and allows you to increase range because it's a mesh network and they all can communicate and bridge each other. I think this works really well. Uh, I have a bunch of the contact sensors for my my doors and windows. So, I know like for example, my furnace won't turn on if I call for heat and a window is open because I don't want to dump heat outside. Uh, that's just waste.

[00:06:08] On the other hand, it would allow my miners to run for longer. So maybe I need to revisit that. Um, but the reason you guys are all here is you probably want to integrate your mining system with Home Assistant. At a high level, these are controls that we've built for Canon Nano3S Mini3s. We also have a queue, but I don't have a queue at home, but I can show you on I have home assistants everywhere.

[00:06:39] Uh, this is a crazy page. Home Assistant AL also likes to just add everything to one page. This is insane. In no way is this useful, but you know what? You can see everything. I got a couple broken entities I got deleted that weren't removed here. But anyways, um, you can see that. Oh, god damn it, Tyler. Uh go in here. Go into Kanan. Anyways, so you can see we also have Q control.

[00:07:10] So we have control for all the home series for uh Kanan Avalon home stuff. Really all you care about is bang or the level at which it's working. Um so that's it. Now, at home, I have tied in my living room Mini3 and my office Mini3. They're space heaters, right? They should be on a thermostat. So, right now, my office is 67 degrees, but you know, maybe when it's 70.

[00:07:44] So, just by doing that, the Mini3 will turn on, start hashing, and once the room reads 70 degrees with the temperature sensor I have in there, it kills the minor. Now, I used to have this set up such that when you got to 70 degrees, it put it into a super low mode. So, it's still hashing but not producing as much heat. So, there's trade-offs for everything. You might have a different use case than me, but the optionality exists. Now, in Home Assistant, they give you full control, which is both good and bad.

[00:08:18] Um, automations is really what we're after here. And you can just come into this automation guey, click automation, pick, you know, a trigger you want maybe on a certain date or there's a calendar event happening or a certain device does something and you want to react to that, you can just click through this, add a condition, then do this. This is simple. If this then that. Not everyone likes gooies. So you can also don't see go into the YAML configuration.

[00:08:56] This is a simple one. I don't really have anything in this one. If we go into this guy, you can get crazy with it. So I mentioned this is this is an automation, but I mentioned sometimes you need to hack the third party server to figure out communications. You don't have to go through somebody else. For example, the hot tub outside has this terrible [clears throat] proprietary control that you have to log in to their app or to their web page with an email and a password. The web page doesn't give you control.

[00:09:27] There's no documented API endpoints that you can just easily call. So, I had to reverse engineer their API and then scrape it and condense it all into these different entities. But now we're able to see, oh, is the pump on? Is the secondary pump on? was the light on, etc. But it's another example of this thing that was not built at all for Home Assistant, but because it's available online, you can pull it in. Sometimes it needs some formatting, but it's generally pretty straightforward to add, especially if you have a cloud subscription.

[00:10:01] Cloud is the home. Um, so you can build automations this way as well. I think I have some right here ready to show. Yeah. So you can build automations in that nice easy guey I was showing you or like this is a whole automation which is fine. Sometimes it's easier to format things in this but also in that guey you can switch into code mode back and forth and kind of build whatever you want. Maybe you want to add a delay. Maybe you only want things to turn on on Tuesdays and whatever you can think of.

[00:10:34] You can tie it in together. just look at the world through a viewpoint of this does something and then I can make something do something because that did something. So everything is an input and you can make it react however you want. Are you in a room with presence detection? You can just have the lights automatically turn on. Is there a motion sensor activated in one room? Maybe you just heat that room and not other rooms where there's not motion because it's not occupied. You can build in logic in here where it's kind of guessing, oh, there was motion in here five minutes ago.

[00:11:09] It's probably still occupied, but open now there's no motion in 10 minutes, it's definitely not occupied and such like that. You can build that out in the home system. Um, and then I wanted to show another way I like I think it kind of bridge bridges the gap of the guey from default guey and this YAML coding. It's called node red and it looks really complicated but it's it's not. It's just a bunch of block diagrams. It's still the same logic. If this does something and this condition matches, tell me about it.

[00:11:42] Uh so for me, I think this is easier to visualize the thing a condition what it's doing. And so what I like about this as well is you can add a bunch of actions in parallel. So, it's not it doesn't have to be just one one bang bang. You can have my alarm in the morning. You can add delays to it. And am I on vacation or not? Do you want the house to turn on? Whatever. Like again, whatever you want the world is your oyster.

[00:12:12] And I feel like I'm struggling to explain this because there's so much you can do in this whether it's mine. It's not just mining control. It's automation. It's about everything. And if you do it right, the wife approval factor is what you need to aim for because, and we're going to talk about this in the panel next, no one's partner is going to do this. Maybe Steph, but no one try to convince your wife to come in here and do this.

[00:12:43] The the action needs to be as simple as you want heat, go to the thermostat, turn on. They don't need to know that in the back end. All this crazy stuff is happening to make the minor turn on. They just want to see I want 72. Is it hot? Um, not all thermostats are made equally. Uh, anyone have an EcoB? That sucks. [laughter] Uh, they used to have open API and you could just go like great documentation.

[00:13:13] It's all you can control whatever you want and then they just closed it for no apparent reason. Um, we found Vinstars, specifically like a T7900, something like that. It looks like it's from 2005. They give you full local API control. And so, if you wire it correctly, for example, the ones around the building, we have them wired such that the furnace is on stage two. Stage one is not wired at all. But when stage when that thermostat calls for stage one heat, it kicks a minor on and the blower fan and sucks the the minor that's ducted in sucks that heat all over and pushes it around the building.

[00:13:56] Then after 15 minutes, if you're not a temperature or 20 minutes if you want, whatever is comfortable for you, the furnace turns on. Or maybe you're too far away. The delta's too far from your set point and the actual temperature. Then the furnace can get you halfway there and then the minor runs the distance similar to how the h the hashtub is working. >> But that's all home assistant. Like there's no I didn't do anything special. It was just like here's this input. The thermostat tells me what it wants and then I just react accordingly to it. Um, I feel like this might be best if we just kind of have general questions because I I just gave a really high level for anyone that isn't Cody.

[00:14:43] >> Yep. Yeah. So um it depends uh if it's on the home assistant instance here for XRG I allow SSH action access into Home Assistant and I just went real real reckless and said you have access to all of the AML configuration files. Here's what I want. Go build it. Now at home I don't do that because I'm just more secure at home.

[00:15:16] I will pull out a YAML file or I will just tell it give me the YAML configuration to do X based on Y and then it'll it'll build out the YAML or it can build out what to copy and paste into an automation guey and it's generally mostly right. Sometimes it's on an older version of documentation and I have to yell at it say no use the new stuff. Um, I have not tried that yet, but I know what I'm doing tonight.

[00:15:49] [laughter] Anyone else? >> Yeah. It's really frustrating because I've been running home assistant for like seven or eight years now and it took a lot of time for me just

[00:16:34] banging my head against the wall to get the to work. And now you can just go, hey, make me a thermostat tied to this minor. I want it all to work. Uh, make no mistakes. [laughter] Um, so Cloud has been immensely helpful in uh building out all this crap because there's a lot of stuff in the configuration I might forget to add or I might misread the documentation, but generally the AI assistants can come in here and build it as easily as you need.

[00:17:06] and it allows you to build cool custom dashboards. It can help you build the front end, the back end, and everything in between. >> I don't have a solution for that yet, but I know there are some guys in here that do have a solution for that. Uh because it's super it's necessary. You can't just rely on what the minor is saying. it's consuming because it's generally wrong.

[00:17:38] Um, I don't know that a bang bang solution like a smart relay exists. You might have to build it yourself, but that's not impossible. Um, there are certainly tutorials for that online. >> Yeah. Oh, I guess I I I do have an answer for that. We have this thing called an Elk product. I can find a link for it later. Uh, it how it works is it's an L630N, so it's a 30 amp and it's got this like relay interceptor that just goes into 120 and I put a smart I put a Wi-Fi switch on that.

[00:18:18] And so if power is called on that switch, it kills the relay for the 220. But if there's no call on the 120, it turns that power back on. It works inversely. Or you can configure it the other way as well. All right, Cody. Oh, spicy.

[00:18:49] Uh, I I think it's immensely helpful for monitoring for controls, assuming you're not running a crappy firmware that like you can't really talk to. Um, it's most helpful in tying it into the everyday aspect of your life, I think, and we'll fight on that. But

[00:19:28] >> so I would agree with you up until like two years ago uh because like I said I've been running home assistant for a long time and some upgrades they've made totally redid the whole architecture of the system. I've had to nuke my system because of upgrades a couple times. Now the code the coder the developers claim that they are done doing that kind of stuff but you know >> yeah Don't ever [laughter]

[00:20:03] >> uh yeah, I don't know. I think it's pretty reliable now. >> What's up? >> Why? Uh so by default um it's only accessible locally. You can go in uh you can pay for a subscription to them. It's like $6 a month and get this crazy URL that's very private through their bridge Nabukasa uh access.

[00:20:39] It doesn't open any ports or anything, but it it kind of gives you a backdoor in for you personally. Uh you can also get reckless and just open a port and you know tail scale works great for this. Um yeah

[00:21:11] >> yeah. So, not only are there a bunch of integrations, there are also they used to be called add-ons, now they're called apps. If my thing will load, let's try a different one. Uh, and these are essentially other services that run in parallel on Home Assistant, I think, is the best way to say it. And so, it adds something if it loads. Uh, it gives you optionality to add additional services. Aha like SSH or Node Red or you can tie in duct DNS or in GenX proxy.

[00:21:50] Uh MQTT is something else you can add through this. These aren't necessarily na native to home assistant but there are other services you can run on top of or in addition to home assistant and these are continuously being built out. There are these are the official ones you can add in custom repos if you want. There's also it's called hacks home assistant community services and these are things that people have built themselves and put repos up to share whether they're themes or dashboards or different integrations that home assistant themselves don't officially support.

[00:22:24] I think of it as like start 9 has their official marketplace and the community marketplace. This is very akin to that.

[00:23:32] Yeah. And there's like the vin diagram or I guess I' I'd say it's disappointing how many home assistant unit users are not bitcoiners because the ethos is very much the same like private locally controlled no third party and the amount of bitcoiners using home assistant is actively growing which I and just loving scene because for the longest time I thought it was just like Brett Jetel and myself and then Cody reluctantly. Uh [laughter]

[00:24:03] >> Josh

[00:25:13] So I had a similar issue to this in my hacky way before I eventually caved and moved everything. I put a very smaller home assistant instance on that IoT network and then there's add-ons. There's like different REST API so you could have different home assistant instances talk to one another. And so you could have A populate B or B scrape from A, however you want to do it. You can do a pushpull situation. So that way you don't have to even though you're going to eventually, you don't have to nuke your current setup and migrate it.

[00:25:47] This is that works really well and it's near live when you're local relative to each other.

[00:26:25] I mean, that's the beauty of this. There's you can solve it any which way you think is best. >> Don't we all? Yeah.

[00:26:58] This is good. This is good. Yeah. So, there's a number of ways. Uh, you guys can't see it, but there's a temperature sensor on top of that room right there that talks to Ziggbby.

[00:27:31] It just looks like a little square. Um, but there are Aquaats and like flow meters, I guess, uh, that talk over ESP home or which is a Wi-Fi module. You can buy these pretty much anywhere kind of under any different communication protocol you want and it's kind of to each their own which you prefer. Uh personally I like to move away from Wi-Fi connected stuff because if your router goes down at home for whatever reason your home assistant can still be up and talk to all your ZigGB stuff and not be you know relyant on your local internet.

[00:28:08] Now might be difficult to talk to the home assistant itself but at least everything can still talk to one another. I know is dying to answer this question. [laughter]

[00:29:17] You You just had that in your pocket. [laughter] Oh, by the way,

[00:30:42] for now. >> Yeah. And odds are you're not the only person to think of this problem. Like the home assistant community has been the most powerful in my opinion and their willingness to help solve problems like exactly what we're talking about here.

[00:31:13] It's like, hey, how do I get A to do B? And so whether it's intercepting analog signals um with Arduinos or like Shelly devices that you can just shove into a wall socket and intercept your your switch, all of this is totally possible. So we are here and willing to answer questions. Yep.

[00:32:06] >> Yep. Correct.

[00:32:56] Sure. >> Yeah. And that's I mean [clears throat] that's what I like like a lot about this is that you can have it such that you're just running all the time bang bang and turn it on and off or you can have it self modulate where you have a heat demand you meet your heat demand and you put it into a low power state and so you're still hashing you just like kind of have it in like this P cycle

[00:33:41] and hit the target you need to and put itself still hashing just in the lower target. It's all however you want to build it. It's you have full capability and autonomy on whatever you want to do.

[00:34:22] You told me you were going to ask this question and I didn't totally prepare for it. Um, so let's take them one by one. Uh, if you Yeah. Yeah. Yeah. I mean everything's going to be on the straight and easy path. There's no edge cases. Uh so unless you're running like brains or luxos if you lose internet you're gonna or mujina uh you're going to lose your heat production. Uh because brains you can use the drain pool luxos. I haven't played with yet but they have the new feature where you'll keep hashing.

[00:34:56] I think Ryan he left. Uh I think I think it's included in Regina as well that if you lose internet you'll keep hashing as well because I think the grid list guys needed that. Um but then >> Yeah. Yeah. So you got to build in fail safes. Yeah. >> Yeah. >> Correct.

[00:35:32] Yeah. Or not found. >> There they are. >> Yeah, >> correct. So, >> kill it. Yeah.

[00:36:08] >> Oh yeah. >> [laughter] >> Yeah. So, for example, like here's my automations for my time of use.

[00:36:38] uh turn off at five, turn back on at 9. But we can see in here. There. Yeah, this is a simple one. I picked the wrong one. There's a hard one. I don't know. I'm a simple man. These aren't super complicated. >> Yeah. Yeah.

[00:37:09] Uh, >> I thought I had something in here that would do that for me, but I don't know. Uh, anyways, I mean, that's high level home assistant, guys. You can kind of build whatever you want. Uh, my favorite one that I have on here, well, one of my favorites, uh, this stupid complicated thing, I think it's this one.

[00:37:41] I get notified when Ocean finds a block. I like to get know when I'm getting paid. Uh, it doesn't do that by default, but I get a cool notification on my phone. Hey, you made X amount. And we have it documented in some repo somewhere that you can actually pull the stats out of Ocean. on this account I have this much in the next block. This much hasn't been paid out. You can see the different how the different templates stack up for Ocean. Pretty cool to see 91% on data.

[00:38:11] Um you can see your individual minor stats. That's valuable to me. Maybe not to everybody else, but again, Home Assistant is here to build what is good for you. Um I do love that the three most vocal people in this room besides Cody are on the next panel discussing control. So, uh I think next panel is 130 maybe 125. Um but that's it for me for now unless you guys have any other questions. It kind of really high level but 125.

[00:38:44] So we have about 15 minutes till the next panel but that's it for now. [applause]
