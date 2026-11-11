# n8n will change your life as a developer...

**Channel:** Fireship  
**Views:** 1279560  
**Published:** 2025-09-29 18:11:47 +00:00  
**URL:** https://www.youtube.com/watch?v=bS9R6aCVEzw

## Description

Get up to 67% off VPS at Hostinger to self-host your own automations. Use code FIRESHIP for an extra discount at https://hostinger.com/fireshipn8n

As programmers, we have the unique ability to prevent lost time through automation but it's often difficult and expensive to pull off.

But in today's video we'll look at how an open-source project called n8n could change the way you think about automating work forever. 

#coding #programming #codereport

💬 Chat with Me on Discord

https://discord.gg/fireship

🔗 Resources
- https://n8n.io/

🔥 Get More Content - Upgrade to PRO

Upgrade at https://fireship.io/pro
Use code YT25 for 25% off PRO access 

🎨 My Editor Settings

- Atom One Dark 
- vscode-icons
- Fira Code Font

🔖 Topics Covered
- What is n8n?
- Automation software
- n8n vs Zapier
- Crazy ways to use n8n
-  n8n Linux VPS install

## Transcript

[0:00] Benjamin Franklin once said, "Losts time
[0:02] is never found again." As programmers,
[0:05] we have the unique ability to prevent
[0:06] lost time through the power of
[0:08] automation. Like when your Gen Z boss in
[0:10] a mini tells you to put a TPS report on
[0:12] her desk by 5:00 p.m.
[0:14] >> Gen Z boss in a mini.
[0:15] >> We don't do it manually. Instead, we
[0:17] build highly sophisticated automation
[0:19] workflows that look like this. Because
[0:21] why spend 1 hour doing something when
[0:23] you can spend 10 hours failing to
[0:24] automate it. Hell, some people even pay
[0:26] $500 per month for tools like Zapier to
[0:29] do all the heavy lifting for them. In
[0:30] fact, that's exactly what this guy was
[0:32] doing until he said, "Screw it. I'm
[0:34] building my own Zapier from scratch."
[0:36] The end result was a platform called
[0:37] N8N, which is an open-source
[0:39] self-hostable automation tool. And no,
[0:42] it's not the sponsor of this video. It's
[0:43] just a truly awesome project that you
[0:45] need to know about, and we'll change the
[0:47] way you think about automating all the
[0:48] boring work you do in life. In today's
[0:50] video, we'll look at some crazy ways you
[0:52] can use it, then deploy our own private
[0:54] automation system on a Linux VPS. It is
[0:57] September 29th, 2025, and you're
[0:59] watching the code report. But first of
[1:01] all, what is NADN? Well, if you know
[1:03] what Zapier is, the easiest way to think
[1:05] about it is like the free and open-
[1:07] source alternative to Zapier. It's a
[1:09] tool that allows you to take some input
[1:11] trigger like a website form submission,
[1:13] a database, write, a voice command, a
[1:15] GitHub issue, etc. then take the data
[1:18] from that event and run it through a
[1:19] pipeline of steps that might include
[1:21] third party apps or your own code. There
[1:23] are literally hundreds of different
[1:24] examples of things you can do. Like if
[1:26] you're a developer, you might run a
[1:27] workflow that triggers on a GitHub PR
[1:30] merge, which goes on to build a Docker
[1:31] image and then notify everybody on
[1:33] Discord. If you're a YouTuber, you might
[1:35] use it to automatically share your
[1:37] content on different social media
[1:38] platforms every time you upload a video.
[1:40] If you're into IoT, you could run a
[1:42] workflow that automatically sounds an
[1:44] alarm when the smart camera detects law
[1:46] enforcement around your compound. Or if
[1:48] you're a degenerate gambler, you could
[1:49] use it to automatically scrape football
[1:51] stats, then use AI to suggest which bets
[1:53] you should place next week. The
[1:55] possibilities are endless. But the crazy
[1:57] thing is that all this can be
[1:58] accomplished without writing a single
[2:00] line of code. Instead, you diagram
[2:02] everything in a flowchart style editor
[2:04] that makes the logic so clear that any
[2:06] non-technical person can approach it.
[2:07] And what's even more crazy is that you
[2:09] can unlock all this power in 5 seconds
[2:11] by simply running npx nadn from your
[2:14] terminal right now. After a few seconds,
[2:16] that'll bring up this beautiful UI where
[2:17] you can start building automation
[2:19] workflows. A UI that was built with
[2:20] Vue.js, by the way. We can play around
[2:22] with it on local host, but if you're
[2:24] serious, you'll want an actual server to
[2:26] host it. This is a serious channel. So
[2:28] today, we'll host it for just a few
[2:29] bucks per month on Hostinger, the
[2:31] sponsor of today's video. that they're
[2:33] famous for providing Linux- based
[2:34] virtual private servers to host all of
[2:36] your apps without needing big cloud
[2:38] providers. And it's a great place to
[2:40] launch our own private NADN app. And we
[2:42] can do that by selecting a new VPS and a
[2:44] region to host it in. From there, we
[2:46] could use a base Linux system and
[2:47] manually install N8N. But a much easier
[2:50] approach is to use their pre-built
[2:51] template. It runs Ubuntu as the
[2:53] operating system with N8N ready to go
[2:55] out of the box. Choose a password, then
[2:57] choose a plan for just five bucks a
[2:59] month. And if you're too poor to afford
[3:01] that, also use the code fire ship to
[3:03] save even more money. A few minutes
[3:04] later, we now have access to manage our
[3:06] VPS on the dashboard. We could SSH into
[3:09] the server to manage it, but there's no
[3:11] need. We can just click on this button
[3:12] to go directly to Nadn. Once you get
[3:15] here, you might be wondering what you do
[3:16] next. In my opinion, the first thing
[3:18] you'll want to check out are the
[3:19] templates. Like this one will generate
[3:21] AI viral videos with Nano Banana and V3
[3:24] and then share everything on social
[3:26] media with Plateo. The actual workflows
[3:28] are just JSON based or because we now
[3:30] have an N8N instance deployed, we can
[3:32] import this template directly into our
[3:34] own project. This one's a bit too crazy
[3:36] for me. So, let's build a new one from
[3:38] scratch. On the dashboard, we have the
[3:40] option here to create a new node. And
[3:42] the first type of node you'll create is
[3:43] some type of trigger. It could be
[3:45] triggered manually or triggered on a
[3:47] schedule, but in many cases, you'll want
[3:48] to connect to some kind of third party
[3:50] app. As you can see, there are hundreds
[3:52] of different third party apps you can
[3:53] connect to. But in my case, I'm going to
[3:55] connect to Telegram and I want it to
[3:56] trigger anytime my wife sends me a
[3:58] message through this app. Just provide
[4:00] the required config info and you're good
[4:02] to go. Then from there, we can take the
[4:04] data received from the trigger and do
[4:05] all sorts of crazy stuff with it. We
[4:07] could send it off to AI to be analyzed.
[4:09] We could trigger an action in a
[4:11] different app and also handle things
[4:12] like conditional logic like you would
[4:14] with code. Let's go ahead and add an if
[4:16] branch right here. I know if my wife
[4:18] sends me this emoji that I've done
[4:19] something really bad. I can capture that
[4:21] data in this conditional statement by
[4:23] going to the string option and using
[4:25] contains. And now whenever I get a
[4:26] message with that emoji, I can run some
[4:28] code. Most importantly, the first way to
[4:30] resolve a domestic dispute is to order
[4:33] flowers. Unfortunately, there's no
[4:35] built-in third party apps that can do
[4:36] that as far as I know. But we can also
[4:39] create a node here to run any arbitrary
[4:41] code or hit a thirdparty API. I know a
[4:44] guy that has a flowers API, so we'll go
[4:46] ahead and use it to order flowers for
[4:47] immediate delivery. That's done, but
[4:49] it's not enough. We also need to write
[4:51] an apology letter. Now, I have no idea
[4:53] what I did wrong because I didn't read
[4:55] my wife's message, but luckily, we can
[4:56] have AI deal with that. We'll create a
[4:58] new AI agent node and give it a custom
[5:01] prompt to have it generate an apology
[5:02] letter. We can even have it use data
[5:04] from previous points in the workflow,
[5:06] like my wife's message, to customize the
[5:08] prompt dynamically. In addition, you'll
[5:10] notice the AI agent node allows us to
[5:12] choose any custom model we want, as well
[5:14] as provide data for memory and tools for
[5:17] the model context protocol. But now that
[5:19] we have an apology letter, we need a way
[5:20] to send it to her. I could do that with
[5:22] a Telegram message, but I'd rather show
[5:24] the world what a great husband I am by
[5:26] tweeting it publicly on X. That's a
[5:28] surefire way to resolve a domestic
[5:30] dispute. But just in case, we'll also
[5:32] want to make sure to record the whole
[5:33] interaction on Google Sheets, as this
[5:35] may come in handy in future divorce
[5:37] proceedings. But there's so much more we
[5:38] could do here when it comes to running a
[5:40] software as a service business. And it's
[5:42] kind of mind-blowing that we have full
[5:43] control over this on a $5 VPS. Huge
[5:46] thanks again to Hostinger for sponsoring
[5:48] this video. And get your own VPS with a
[5:50] discount code using the link below. This
[5:52] has been the Code Report. Thanks for
[5:53] watching and I will see you in the next
