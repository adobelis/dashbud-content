And turns out, okay. There's a bunch of stuff that you're fixing. So, then you know, I make up the um. The surgery, that's crazy, was a year and a half of, in essence, arguing. Like?

Speaker 1   00:13
It's weird right in. That situation would be, like, yeah, I'm sick. I know something's broken, and then you have someone being like, well, you have to go. Right around the block for a few times, then come back so to speak. But anyway, so it's done. Now, I'm good a few weeks.

Good recovery.

Speaker 2   00:33
Um, so hey, you've been self-employed for three years. Yeah, yeah, I was actually even paid for some of that. Um, so on that period? Um,

Speaker 1   00:43
But I have recently not been. I'm recently, like, totally start up. Um, hey, so what's the difference between self-employed and startup? Uh, startup self-employed. I mean, we don't have any Revenue yet, we might. Actually, it depends on what happened today, whether we actually got a check. Um, because excuse me, we have a very adorable cat.

And

Speaker 2   01:08
Yeah, Lily, gotta maybe.

Speaker 1   01:14
Okay.

So, um? Yeah, so where we are just hitting the market, and now we, well, we actually? We actually have had a like a working useful product, um. For about two or three months. And so the check that might be coming in this week is. From. A from a company that signed on the dotted line for like an annual annual, uh?

License for? Six. Now, seven people they just added another. Um. And it's, uh, it's. It's basically it's analytics for analytics have-nots. It's um, the people who can't really afford a full, you know,

Speaker 2   02:04
Data Lake

Speaker 1   02:05
Build out. And, um. And to hire like a full-time data person, who will, who knows where everything is in the data Lake and will then build out reports for everybody. Yeah. Yeah, that's awesome. Dude, that's. It's funny, I I? I think they have Equity. We should check on it.

Speaker 2   02:28
In the early AI, start up in. Like, 2021, it was basically doing that. The whole thing was like, you know, plug in any data source, right? So, like, Google Sheets or whatever, and they kind of like reduce going the integration route so you could integrate, you know, your med ads, and you can integrate your Salesforce and then just ask it questions kind of thing, um, and then going through the work is sort of like.

I, I, it was. It was almost in a sense, cheating, right? Cuz they were like, pre-baking, you know, the schema and stuff for, like, how to, how to get at the data? And so I think it ended up being difficult to scale. And I think honestly. Probably the models have gone so much better.

It just doesn't make sense anymore, but um, yeah, it was a tough state. But the reason that that those guys had a tough time. Um, they couldn't charge enough so the the. The distribution is really hard. Uh, and so it was relatively thin. Very broad type of product.

Consumers. I think they had. They, they did have some success going through, like the Chrome Store, like Chrome extensions. Oh, interesting. Um. But not, not enough to? You know, make the thing take off. Um, well, kind of. Sorry, I always jump right into this. No, what's our, what's our ICP?

And so did you? Did you build it so not originally?

Speaker 3   04:17
This is how this. This is like one of the things I was paid for, um.

Speaker 1   04:22
Last year was was being there kind of head of. It started off, like marketing, go to market sales. But then it pre, it immediately became product. Because I just they, they really needed someone to sharpen their product focus. And so, you know, immediately, like the things that I, the feedback I gave went right into the?

The, you know, the road map right at the front of the road map and? Um, which was great. Um, but it was still built on. Like, low code crap basically. They were.

Speaker 3   05:05
It's called Alpha anywhere. It's like, it's some thing like you've never heard of. Yeah. Um, but? My, the guy who hired me the the original founder was like had built like 20 websites, 20 data driven business. Apps. Using this platform, and so he went with what he knew.

Speaker 1   05:31
And

Speaker 2   05:32
He,

Speaker 1   05:32
Yeah, even though you know his two Engineers protested. Um, yeah, but they've protested mildly. They were happy to be working on something interesting. Um, you know, and and they were also like resourceful and would like work around, you know, the inherent limitations as much as they possibly could. And then, like, finally sometime in July of last year, um.

We had. He was doing a demo for one of his, um, custom software development customers clients that he was trying to get using dashbud,

Speaker 2   06:06
Um. And it just

Speaker 1   06:08
Went so incredibly poorly. Like everything broke all at once, and it was just so embarrassing that he was like he had his like kind of come to Jesus moment and and. You know, there was still some idea that we could. The the? Well, I wasn't. I shut up because this, I really wasn't my job at the time.

Yeah, but the

Speaker 2   06:31
The

Speaker 1   06:32
Junior of the two Engineers, the senior like was like, no, I can fix it. I can, you know, we can. We can work with this, but the junior was like, I would like to propose it. We tear the entire thing up and stuff from scratch, and I was like, yes, I mean, I told him that we needed to do that at some point.

I just didn't want to be seen to be kind of digging the knife in at this moment. Of like pain?

Speaker 2   06:55
Um.

Speaker 1   06:56
And thankfully, I didn't. I didn't have to do anything of the sort because he. I, you know, I agree. I said that, I agreed. We moved immediately to a different kind of, and we started thinking about what to how to approach that. But so then. Then I started getting involved and I.

Started using my architecture, and you know, engineering management background to kind of structure the whole thing because we had a not totally Junior, but but a guy who had never worked on a big SAS project before. Um, let alone built it from the ground up, so we built it you, so I, you know, strongly encourage them to use a stack that I knew was effective.

I knew would scale. We built it in, um, so it's. It's flask via serverless.

Speaker 2   07:47
Okay, so it's

Speaker 1   07:48
All everything runs through lambdas and and API Gateway. And that's the back end. And then the, the front

Speaker 2   07:54
End is react.

Speaker 1   07:58
With a lot of, I wasn't up to date on some of the react packages like. Um, you know, I remember router, but now there's react. Query, I guess, has grown out of that, or tense, that query and zest end. And so, that's our. That's our front end stack.

Speaker 2   08:15
Oh man, yeah, I mean, I mean, front end. They get the back end stuff, particularly for, like these data, heavy applications. It's um, its own little world. Yeah, I had I think the last year dealing with. Because it's even worse than that. It was like a like a legacy Ruby on Rails site, um.

Which,

Speaker 1   08:34
Oh, I, I know, a Founder, who is he builds, he's he's now doing all everything himself, and he's, like, still like rails is the best, I won't, I, you know, prove me wrong? Um. Testing and? So

FP   08:54
They were paying you. It sounds like for a while to do that, and now you've kind of joined you've taken on more risk and become a founder kind of care center. 

AD   09:21
Yeah, well, what happened was the um? Scott, my co-founder, stopped paying people in October. Right? And it's a little bit annoying because he had said that, um. You know, we would be. He was going to fund it through relaunching. The site and I I? You know, I start. I've now became. Kind of. No, I wasn't on the team, but I was the main, you know? Keeping things on track, person testing things as needed. Um, when they're ready to be looked at, um, looking at code a little bit here and there.

I wish I'd done a little bit more of that. Because I ended up owning the code base in January because you know he stopped paying people on in in late October, um? The lead Engineers kept working on it, but was basically nailing it in, and not, you know. So, he only like, worked, you know.

He didn't like work it. He didn't work half of December, and then he gave notice in, like first week of January. So, um? He gave, you know, he gave two weeks and? I was able to take over in those two weeks like God bless. Claude, you know, I, I went in and just like, had everything summarized for me and kind of figured out like the patterns that he was using that I wasn't familiar with.

Yeah, and. And so on, and so on and, and did, uh, you know, I use, then my kind of management, um. Background like you know is? Engineering manager. Behold myself to, like, we're gonna do a full Dr exercise like that's before he leaves, but for, you know, I am going to relaunch the site myself from yeah from IAC from, you know from, like?

From a a GitHub actions like script set, and uh. And terraform and?

Speaker 2   11:10
And so, yeah,

Speaker 1   11:11
And so I did. And, uh, and I'm gonna build the feature so that I can, you know? Like something that's missing right now, so that I can prove to myself that I know how.

Speaker 2   11:22
Yeah, and that was week, weeks, one, and two.

Speaker 1   11:26
And, uh, yeah, and then I basically went ahead and. Built everything that wasn't there yet, which? A lot, but it was good. Also, you know, there's a lot of refactoring and like, figuring out like incomplete patterns and things that you know, there are a lot of good ideas that he had brought that I never would have.

Thought of never would have thought to ask and likewise with the junior guy who is front end and ended up leaving a few months, a couple months after that he kept on actually getting to it because he was doing work for the for the first Scots, other company that makes money.

So, Scott provided him. As a resource, but I actually didn't even know. Catholics need plastic, um, uh?

Provided him as a resource, but it was I, I actually didn't realize he was doing it full time. That's how low the productivity was, and it was in some ways good because he was looking at everything himself. He wasn't using AI for anything. Um. Be, and so you know.

And then he ended up leaving for another opportunity. Anyhow, like that's the measure of quality? Well, it was good for somebody who's Junior not to be. Producing crap that they don't understand.

Speaker 2   12:45
I mean, it's just anyway. It's a large and separate conversation. Yeah. So, um.

Speaker 1   12:53
Hey!

There, yeah, including managing my former boss now. 50/50 partner. Um. In there. Who sold the deal? By the way, oh, is there anything you particularly want to get out of this because I'm just like catching up? And I like finding out about people's startups, um, I would. Yeah, but I figure let's do that.

First, you know, I mean, I'd love to like, dig into, like what you know or go to market strategy is, and kind of like, where we find ourselves and stuff like that, um.

But yeah, he who sold the deal. He, so he set it up. He knew this guy who was, like, fractional CIO. A framing, uh, Supply Company. Eight warehouses.

Speaker 2   14:12
Yeah,

Speaker 1   14:13
About 50 million a year in Revenue.

Speaker 2   14:15
Yeah, you

Speaker 1   14:16
Know, probably 50 people. 20 of them are sales people, and 20 of them work in a warehouse.

Speaker 2   14:26
Crimea, both framing. Okay, yes,

Speaker 1   14:28
Yeah. We're actually just sourcing, framing, and then storing it. And, yeah, and sometimes sometimes actually build complete frames.

Speaker 2   14:35
Um, they have

Speaker 1   14:36
A. As the co, that's the as the, uh? So, with PE LED ownership, new ownership, taking over taking over family-owned company.

Speaker 2   14:49
Uh interesting, and so you guys work for the PE shop or for the company itself. So it's all

Speaker 1   14:54
One because he's, uh, it's PE LED, but it's like, I think people do this, like the operator is one of the investors, and then brings in like partners

Speaker 2   15:03
Basically starting.

Speaker 1   15:05
Yeah, but it could also just be taking a profitable company and like working The Kinks out so that it's as profitable as possible and just spends cash.

Speaker 2   15:15
Yeah, yeah. Interesting, and so the pitch to those guys is you've got eight locations and a bunch of data, and we can. Help you either save, and they'll make some percent more or loss. 

AD   15:30
It's actually simpler than that. Robert is a CEO and as he described it in our first meeting. And so, the question of who sold the deal? Is a little bit, so Scott definitely brought the deal. But in that, in that meeting with Robert, you know, I was doing. 80% of the talking.

Um, so you know? So, you know, I'm getting that part, and I'm fine with that distribution of Labor. Um, as long as I have. Time to, you know, as long as things are working, and I don't have to like split my brain entirely between totally technical, you know, stuff, and?

Um, but yeah, so he, as Robert said, um. You know, we have? Blue screen ERP that runs our entire business.

FP   16:25
And

AD   16:25
It's as simple as he's a guy who wants who has higher standards for what, what the quality of data? And the and how that data is distributed and what kind of analysis he can do on that data. So, the first exercise, which was after they'd already signed on the dotted line, but they still haven't paid us, but um, hopefully there's enough moral, you know, yeah?

Was he took? He actually had, um Claude, go in and analyze, like how the? How is reporting works? Um, what is, you know? What does he need in order to do like a bridge report like a q1 to q1 Bridge report for last year? And. And, and then some of the anomalies and or, you know, eccentricities and how things are calculated.

And um, so there's some for this, you know, their framing supplies all of their volume. Measurements are different. Um, for different types of products. So, understanding what constitutes like a unit for these different products? Um, is. Is, you know, is important. And because the other thing he wanted to do was like a price volume, mix analysis.

And so volume, you know, needs to be nailed down somehow. So,

FP   17:44
Yeah, I guess blue screen is quite coming. Yeah, it's like, it's in IBM informix Erp that was probably spun up 30 to 40 years ago. Fascinating, okay, yeah, probably upgraded, like 15 years ago or something.

There's a jtm. Um, okay. Uh, and then. So, I guess what was involved for you guys to get in, so he did some stuff in Claude? Based on that Stephen's law, he figured out that he needed something else. And you guys are, that, is that roughly right?

AD   18:26
Yeah, I guess the thing is, like, we, you know, all that information about how things how to calculate things is good, but then operationalizing. How like to get reports into people's hands and make sure that they have consistent quality and that you can that you set a rule once and then don't have to reset it, you know.

Don't have to check in on it. Make sure that it's being followed.

Speaker 2   18:46
That's

Speaker 1   18:47
What's built in. We have a semantic modeling layer that serves that purpose, and so you see you. You hopefully don't have to touch that. All that frequently. Um, and so you're just working with. A data, you know, a data analysis, or like query writing agent

Speaker 2   19:06
That has all

Speaker 1   19:07
That built into its prompting. It understands like, what all your table in row table and column, you know, semantics are? Um, and some of these, you know, in this is actually really good. You know, there are many strangely and similarly named. Columns in a in IBM Informix. Warehousing. ERP.

And so, understanding what all those things are, you know, just having to tell it once. And then, you know, the semantic model knows what each one of these. Um, you know what, how, to, how to like? There are like three different date fields. Which ones do we use for like for accounting purposes?

FP   19:53
Interesting, so I'm guessing you've already gone in and looked to see how many framing supply businesses there are in the US and sort of how to figure out if someone's using IBM and forbix and this type of stuff. No, I haven't yet. I'm I'm, I think that's. That's definitely one approach, I don't, you know?

AD   20:17
I'm thinking more in terms of function than vertical right now, because I think companies that do warehousing of any kind of, you know, products. Sufficiently specialty that they're not using a logistics. You know, system that we would have to think about plugging into. Um, so they're rolling their own Erp, so that's, you know?

Speaker 2   20:39
That's our

Speaker 1   20:39
Framing company right there? Um, but that would be the way I would generalize that. Um, I think manufacturing is another one. I've talked to. Of a friend of Dana's who's a, um? Is also a member of like, what was a family owned? Chemicals business, um, soap. Um, like industrial soap, and you know, commercial hand soap and supplying, and then also, you know, retail?

Um, yeah, and they're New York based, which is crazy. Um, they actually manufacture soap in Queens. That's amazing. Yeah. Of these non-sexy businesses. Yeah, so that's, like, I think that would be a good.

FP   21:32
The start of that. I've been working on for the last year, um. There's also AI, but you know, it targets real estate agents, and it's kind of like people ask, why can't these real estate agents do what you do? Quad, basically, you know, just like, kind of. And um?

It could, but they never will, right? Like, what f****** real estate agent's going to take the time to become? Couldn't have applaud to do that, um? Which I think is basically the same argument that you know your startup is, like, that guy's never gonna become handy enough with Claude to like, settle this up, right?

But I looked at...

AD   22:13
Is that this dash Fox? [Yeah] Okay, I didn't realize it was actually targeted at real estate agents. That's interesting. 

FP
Yeah, it is, we don't. Long story, but anyway. You have. It's all on landing pages and stuff people. They, when they. It's actually, um.

It's even crazier than that, so? By the way, I just left, um, [oh, really?] Yeah, so the product is your real estate agent on DashFox. We connect to your email.

FP   22:49
Pull it all up. We we exfiltrate it, and then we analyze it to find every client we've ever had. Every customer we've ever had, and then. You know that email? There's a ton of just personal stuff right by studying abroad.

Pets, pets, having cancer, or whatever. And so we draft we engagement emails for people who haven't been in touch with for a while. And it turns out that if you're real estate agent and you help someone buy a house seven years later, they're gonna sell it to over 50, 000 incentive to stay in touch with them for seven years.

Yeah, and they don't do it like real estate you just don't do that sure. Um. So that is a product, and it works, and people pay for it. And you know, it's a nice little product. Um, I was advising you guys a time. But at the time. What I realized and what I suggested they test is that if you have access to someone's mailbox, not only can you find all their past clients and Prospects.

You can find literally. Every other f****** agent that, they know. Right, and he nailed it. From them, right? And so the the premise was, see if you can get people to? First off, approve that you find all the agents in their inbox. Approve, sending some number of introductory emails saying, you know, hey Fred, uh, meet Fernando.

I've been working with good guy. It's a call, and I'm on CC on that email. So I follow up with Fred, right? And so that is really interesting. Wait. So, wait, wait, what's who? Is cc'd? Sorry. Okay, okay. Rhonda's following up a Fred? And so, what that does is it generates a lot of top of funnel at no cost. And...

AD   24:47
Wait, but is this for cross-selling? So why are you contacting I? I know more than I want to about the real estate business, but not. Not everything. So. Um, so is this? Are you contacting another real estate agent so that you can be the buyer's agent so they will like refer you as a sell-side...? 

FP   25:11
No, no... Arthur: Arthur is introducing Fernando to Fred. [Uh-huh.] Arthur is using DashFox and likes it. Okay. Okay. So friend, meet Fernando. He's a DashFox. You should hear him out. That's the mechanism. Okay, if they will, if they'll let you do that, if you will let them.

FP   25:33
Yeah, and it turns out that a significant portion of them will let you do that some number of average. You know you find some number of Agents in the actual mailbox? You send out some average number of introductions and some average number of those turn into meetings, right? Got it so that? Is unique that doesn't exist in the world of sales.

Think about it right, or you are controlling the word of mouth of your customers. It's really powerful, and it's totally. I'm writing. What's in that email, you'll prove it. But nine times out of 10, you just approve it. So, I'm like, Fernando's the greatest looking guy ever, right? You should talk to him.

It's amazing! Jump on banana, and so, like. So, I'm confirming in Word of Mouth. Plus, I'm sending it the email from your account. Plus, I'm following up with the guy, right? So

Speaker 1   26:25
Did they? Did they do that successfully? Did they not work? And so, so you know there's a lot of conversion points in there? Um, and the net of everything is that?

Speaker 2   26:39
So, at that point, I joined because I was like, this is amazing, because if this works,

Speaker 1   26:43
You

Speaker 2   26:44
Could end up with the K Factor that looks like a social network rather than a B2B business, right, right? Because every customer needs to more than one new customer, right, which is insane? It didn't turn out that way. So, it turns out that the K factor is much lower.

It's like probably a 0.7 or 0.6, but what that does, is it lowers your cost of acquisition, right? Sure, you're basically getting a lot of users for free.

Speaker 1   27:13
So, so we never use the website. The website never had to convert. I see, I see.

Speaker 2   27:21
All of our business came from referrals a hundred percent of our top of funnel came from. That is funny. Isn't that crazy? Yeah, like people and referrals that you literally automated. Yes, yeah. Yes, yeah. Um,

Speaker 1   27:44
How involved are you still with DashFox are?

Speaker 2   27:52
The there's several things they've always been cash poor. They're bootstraps. They both don't want to raise, and I think it's impossible for them to raise because they don't have data that's taking them from zero to 50 million in two years, it's like they have data that maybe says they're going to get one, two, maybe even 5 million right, but that's no longer enough to get refunding right, right?

Um, right, and so, and how many people do they have? It is like it maxed out at about 10, but um. You know, they really stretch to hire me for what I thought was like a pittance on a risk.

Speaker 1   28:31
Yeah,

Speaker 2   28:32
Joined them, and you know, it got to a point where they were starting to cut my salary and all this kind of stuff. I was just like, yeah, I do think it'll work out because what I just described to you is incredibly powerful, right? And they've got the product more or less.

Already, and so they can start to kind of. They can start working on the churn, you know?

And they don't need a u for that. No enemy for that, and I just don't have the time. Man, I'm I'm 50, almost two now, and like, you know, I'm on my last stretch, I I'm not up for putting in seven years to see if it's a home run or not.

I'm just like, I'm just gonna get paid for. Um. Which may or may not resonate free. I don't know what to do, your circumstances are, but so for me, it's like, you know, I've taken a lot of swings at the bat and I'm kind of like there's just no longer.

You know? Uh, and sorry. So, and basically, I want to be done that time. I'm like 55 or something. So, oh, okay. God bless! I figure I will probably work until I'm whatever, yeah.

Speaker 1   29:44
I mean, we could. But I think both, both my wife and I are just like, you know, what like the number can always go up. And.

Speaker 2   29:53
The time you either you either fix a number, or you fix a date, and we've chosen to fix the date I said. Yeah, yeah. Um. But yeah, so generous thing. Are there like specific things you're trying to figure out or like, what's like, what's front burner for you, I guess?

Yeah, I guess I'm trying to figure out like?

Speaker 1   30:22
Good approaches to prospecting. You know? Um, an interesting. Thing is that, like, my personal network is not necessarily? You know, the? The best for this. I don't know that many people who run so the other, so the so the other. I think if you want, you know, I really do.

I like the framing of like data Have Nots because there is like there is. For whatever reason, there's a there's there are businesses that have been left out of, like? Bi good, like, good, you know? Data analytics tools? Mostly, you know, because they have, you know, inconvenient sources of data that would require a whole, you know, data Lake that if you're like in a?

Small scale, like mid-market private Equity situation, you know, building a data Lake. Just kill your margins, and that's what it's all about.

Speaker 2   31:18
Yeah,

Speaker 1   31:20
Um, you know, and hiring and hiring even like a, you know, a one-person data team would be, would likewise, it's just like I'm taking on overhead and I'm trying to avoid that. Like, I'm actually trying to reduce overhead for this company. Um, for another, you know? Data have not is like mid-size.

Doctor's offices, like, with, uh, with like, a, you know, let's say.

5 to 20 or even. Um. A network of, you know, network of practices? Um. That where it's multi-site? So you have, you know, your management is not able to see what's going on? Every day has to look at aggregate numbers. And likewise, you know, they don't like emrs and HR tools and all the different things you'd have to pull together.

They just don't have good data reporting, let alone like integrated data reporting where you can pull from multiple sources and put it all together.

Speaker 2   32:23
So,

Speaker 1   32:23
That's the kind of um, those are those are two that I'm two that I don't particularly have a lot of, you know, friends or friends of friends? In those particular businesses. So, I'm trying to figure out, I think, probably, they're not that hard to find, but I'm thinking about, like, how best to approach them?

What I mean at this level? At this level, if you're a founder.

Speaker 2   32:49
You can just reach out to the CEO of whatever that, you know, like, find the find the hundred percent like just at this scale. It is literally you reaching out with an email, a LinkedIn connection where, like, it's actually me. I'm the founder. Here's what I'm working on. You should not probably.

And. You know, it's not great, but? You'll probably get one out of. 20, you know of, those will respond, and you just start a conversation. Because you're just trying to get. They're trying to get to some critical mass of like? I'm gonna make this up, but. How much is your Enterprise actually just looking at your pricing on on your website?

Your your pricing is low enough, you're going to need. You know, on the order of 5800 customers to be able to tell, like the only way your business is going to work is in the thousands of customers, right? So, oh yeah, uh. And you can't jump straight, like none.

None of the go to market motions that pay. That level of ACV? Things that you can create without, like, really knowing who your customer is and what their pain points are and all that stuff. So, the goal is to get to that initial, call it, call it 50 customers where you're literally just dialing about getting the meetings if you're getting them to sign up and paying all that stuff, but if nothing else like, record everything right, so that then you can start doing the stuff around running ads, creating contents doing all the stuff that's fed by your ICP and.

You know, knowing vertical specific stuff and creating vertical specific content like? Which all of it, you know, will compound into more like a um. It's gonna it's just by default. It's going to be a marketing kind of lead business, you know, because of because of your target. And an inbound one.

Like, you gotta get. You gotta get to the point where people are finding you online or whatever, and you're getting inbound needs because you're not. You will never afford. You know sdrs to cold call and all that kind of stuff at field sales? Yeah, um. But initially, yeah, I mean, I don't think there's a shortcut.

You're just like connecting people on LinkedIn all the meeting, like, um.

Um, yeah, there's no, it's hard to shortcut that initial. Get your first 50 conversations, you know, yeah. Um, and that's basically what I figured. I mean, I figured. Linkedin and Linkedin sales Navigator are probably my friend. Um, yeah, doing some cold email from a from a like non.

Speaker 1   35:38
Not, uh, you know, a fairly hot, like, a, a non-bounce domain. You know? Yeah, I mean, look, you're not gonna, I mean. It doesn't matter, right? Because at this stage, you shouldn't be sending. Thousands, you know, even hundreds of emails are gonna be too much, right? You're going to want to like, actually, I mean, you could shortcut this with AI, right?

You could sign up for.

Speaker 2   36:04
Even clay might be Overkill, but let's just say you use Claude and you come up with a list of 100, you know, warehouses? That are have been around for more than 40 or 50 years. Therefore, their Technologies likely to be old and they're full of a certain size. Therefore, they're unlikely we've been invested in and then, like.

You know, so you come up with a list of maybe a total of 100, but then you're actually creating each each email, right? Um.

Speaker 1   36:31
The description your description of like if you have a blue screen Erp I think is like? Pretty evocative, like, you know, if you reach out to the guy that runs?

Speaker 2   36:41
You know, who currently runs a warehouse that's been around for more than 40 years and ask him, like, hey, or you wanted for mix or something like that? You know, like, he hates it. So right, rings somewhere

Speaker 1   36:57
In his brains, like someone's going to help me with that damn Erp that I love hate because I know that it it does everything that I need, but I can't

Speaker 2   37:05
Get

Speaker 1   37:05
Any numbers out of it without wanting to kill myself. Yeah,

Speaker 2   37:08
And it's a general thing in these emails. Don't leave with head. Build those things as a, b, c, d, e, right? Just like, figure out the thing that they're. It's important to them that they're going to respond to like. You know, do you want an IBM informants or something similarly clunky?

Or, you know, are you able to produce a there's a kind of report that you described that you know that IBM can't do, right? Yeah,

Speaker 1   37:32
Like something like a, uh, you know, price, value, mix, or like a or a bridge. Q1. Bridge,

Speaker 2   37:39
You know, like, does your Erp let you do a price value mix because price volume mix?

You know what I mean, like

Speaker 1   37:49
That initial thing has to be asked about something that they're gonna be, like, oh yeah, that hurts, yeah. Yeah, some other thoughts I've had that I figure I might bounce. Yeah, so that's by the way. Thank you, that is. That kind of? Language targeting around. Pain points like subtle pain points like things that are not that that make you sound knowledgeable, empathetic.

Um, not just kind of.

Speaker 2   38:21
I read

Speaker 1   38:21
That the people of your type have problems.

Speaker 2   38:26
Like, I'm guessing that you went through with this guy, even implementing this, you know thing for the warehouse where you're like, you could. You could literally make some inside joke about IBM and formics. Right about, like, oh, you know, don't you hate it when you know glitches? Try to run command also.

Delete whatever, yeah, right? Well, except for the fact that I've only gotten.

Speaker 1   38:46
They can't connect directly to their informix database, so they're doing everything off of exports. And that's actually how we're going to run. And so that's another feature of our platform. That's kind of cool, is you can just drop exports in, and it figures out, you know, deduplicates? Yeah, just be, like, so many experts.

Are you trying how many exports are you running from your database every week or every month, right, like? Isn't that a pain anyway?

Speaker 2   39:12
Um, the other things I think might be.

Speaker 1   39:16
Beneficial. Are one. We just had actually our first incoming. Um, lead off of. A and it was off of an EMR website. So, the um? Head of operations for this Dermatology 556. Office Dermatology practice in Ohio.

Speaker 2   39:42
Yeah, um was

Speaker 1   39:43
Using modmed, which is a modern as it says a modern, you know, EMR, it's, and but they don't have. So we actually. Are officially? From, like, a year and a half ago, based on one of Scott's personal relationships, which, by the way, I'm not underselling, you know, operationally, he's not that involved.

But, like, there's connections are great. Um, I mean gold really? So, yeah, so we're on there, you know? We're a partner of modmed, even though we only we kind of did some integration work. Like, you know, a year and a half ago and haven't touched it since because I don't know.

We never got any customers off of it and. You know, the the platform wasn't ready for prime time. It was the old version of the platform at that point, so. Yeah, I'm one. I'm also thinking, you know, modmed, you know, looking for modmed customers or asking if we can partner with modmed to, you know if if there are any customer lists that they could help us with to once we've proven to them that we can actually make modmed better?

Um, the only other partner they have in analytics is Domo, which I've used. You know, I mean, it works, but it's like, not fun, it's not. It's, it's not easy to use. It's not the sort of thing. Yeah,

Speaker 2   41:06
Yeah, and it's, not it. It is said, didn't forget it, but it's like adding a report is, like, pretty terrible, you know, right? Yeah, I mean, that's another thing. So, um, at this stage? The most valuable thing is conversations, right? Everything you're doing, like Daniel emails, is about getting conversations and.

For as much as people poo poo it like conferences or where you can just knock out like in 20 conversations in a day and? To the extent that some and you can just attend right, but the way that you really like, get a lot of conversations is you have a booth.

No, that's very expensive. But if modmed is far enough along that, they're going to conferences, and they're going to have a booth anyway. That's the end because hey, are you gonna have a booth at a conference at any time in the next. Whatever we'd like to, would it be cool if we just we just sat at your at your booth as like a partner and?

And usually you. Do you know they'll just let you do it for free, but um. You know, it's definitely cheaper. And then you're capitalizing on their branding, right? So, um. And even separate from that. Whether you're able to get that, then I would say conferences are just the place that you can just early on, you just get more conversations out of the way than it's just really efficient.

It's very high leverage because it's your time anyway. Like, the argument against conferences is always like, oh, it takes so much time from Founders and could be building blah, blah. But if you literally still found or selling, then it's the most efficient way to found yourself, right? We've actually looked at.

I mean, so? Question on that is like, what are the right conferences? No, you don't you just done another one.

Speaker 1   42:54
Yeah,

Speaker 2   42:54
Right, gotta go to a few. Yeah, I

Speaker 1   42:56
Mean, Scott

Speaker 2   42:57
Looked at. What right, again? Throwing spaghetti at the wall and seeing what sticks. And, like, yeah, one thing you just start clicking on that, right? I don't wonder, so there's one, I'm sorry. I would argue that the two leads that you have are already like that sounds great, right?

Like, go click on book on people running. Magnet or whatever? Whatever the magnet precursor is, and then. The very big EMR. Um, there's only like two big EMR players, right, like, Edge, and

Speaker 1   43:36
Yeah, there's epic. That's the one you see in, like every hospital, and most large, you know, practices. There's a, there's a very interesting open source one. I don't know if you've seen that.

Speaker 2   43:51
Which is an open source platform, and they basically got really big, primarily outside of the US, because I think it's so expensive, but in, like certain, like smaller systems, um, open EMR, you know, it's developed for open source reasons, but it's big. It's got like. Like thousands or tens of thousands of, you know, um?

Of businesses, and I think that that's like. I mean, that's also for something like what you're doing, right? It might be an interesting little play. Yeah. And

Speaker 1   44:23
Also, it probably has, like an installer Network, you know, like, a that's right, that size. There's definitely a size to do it. Yeah. What's an SI sorry?

Speaker 2   44:33
Systems integrator

Speaker 1   44:34
Systems integrator okay, yeah, um, yeah, you know, you've paid Deloitte or something like that to put in Epic, but I'm sure there's like, right?

Yeah. Yeah.

Whatever, Latin, American, Middle East. Oh interesting, yeah. Yeah, I mean, you know, there's nothing preventing us from also selling other countries. Um, yeah. Um. That's cool. Man, I mean, are you enjoying it? I'd better be. No, I, I, am I, I mean, I've enjoy. I really enjoyed building out the platform, too, um?

And then you know and and and all that went with that. Like having these moments where it's like, oh my God, it's alive, you know, it works and does stuff. And then the first time, you know, having live customer data in there and seeing it, you know, produce, like useful reports?

Um, and then building all you know. And then there are all these opportunities to fill in the product gaps where you're, like, oh well, they, you know, we were mostly focused on like charitable data, and we're very proud that our agent has a. You know, you know, has prompting that actually allows it to understand what's charitable and not?

Speaker 2   46:03
Sure, and so, which

Speaker 1   46:04
Is not necessarily intuitive, so like and then export, you know? Metadata. That allows a a UI to then chart, like the data that you have effectively, so we're focused on charting, and then you know we're asked for, like, a, a, you know, q1, to q1 Bridge report that has, like, you know, five different columns, and it's, like, well, that's not charitable at all, and our tables look like crap so.

You know, we have tables. They work. But like, they're not nice. And they don't have any UI, you know, goodness to them. Tightened columns or hiding, you know?

Yeah, I mean. I guess as long as?

Speaker 2   46:49
Yeah, I don't know if you've been through this before, but there's really an endless number of features that you can add. But. Very quickly. As a teacher, that you add just makes the product more complicated and difficult to use. So, like, initially, just figure out what the like? I don't know if, in your case, it's like three charts.

Or, you know, three data Integrations, or like, whatever that just makes it super clean, and like, yeah. Allows you to? You know, like basically, allows you to say, like, oh this, is this will allow you to back, you know, across 10 medical locations by specialty, you know and safe?

20 on costs. Well, whatever it is, like, yeah.

Speaker 1   47:34
Yeah, I've got, you know, I'm trying to be. I sort of. I. You know, for I was hoping Scott, I think, is going to continue to run his practice, and not really. I think he'll be really good for connecting people, and as a sounding board. Yeah. But he's moving.

I think a little bit more into being, like the main investor and and connector. Um. Uh, that you're splitting 50/50 with him. Good question.

Speaker 2   48:10
No, I mean,

Speaker 1   48:11
We, yeah, no, we need to rework. We, we have an mou from six months ago that made me when I, when we first had, like almost a product, and I'd spent three months or a month, um, two and a half months full time on it with no pay and also being everything.

Being the head of engineering being the head of. So, that was six months ago, and we were supposed to be 50 50. So I've been talking with. Start up, uh, lawyer friend, who. You gave me some ideas on how to retroactively make that make sense.

Speaker 2   48:49
Yeah, you just, yeah, I mean, on the face of, like, just what you just described, that's going to lead to like f****** problems. So, yes, you just need to fix that now and. Whatever the hard conversation is like, just have it. Yeah, cuz. That'll f****** and it'll make you unhappy.

It's gonna f****** your calf table. It's gonna make it hard to invest, like all the stuff. If if you guys want to raise BC at some point which I don't necessarily know you want to do, but um? Even if you don't, so it f**** up your account table if you do.

Even if you don't, it's not going to make you happy and right. Right, right?

Speaker 3   49:30
Yeah, no, we did. We, I we need to, and we also need to do it, you know? I think it's okay to.

Speaker 1   49:37
I have a little bit of Revenue before we do that, but like, once we start seeing the light, it's once you start seeing. That's right, it get like that is absolutely right. You got it, um, something else that I'm going to say about this?

Speaker 2   49:59
And wouldn't start creating content. Even if it's s***** content, so I have. I have.

A guy who wrote a book with successful entrepreneur multiple exits. He's currently on his something startup. I think I only and. Um.

Is this guy by the way?

Speaker 3   50:28
Yeah, yeah, yeah, you introduced me. Two years ago, we had a really good conversation. Great! So if you, if you don't like it, then you know he's the real deal, um.

Speaker 2   50:37
He started this his own, you know, startup? Two years ago, and the guy were doing customer research stuff, whatever, whatever hired marketers so and so on, anyway. Long story short, he was, like, look. First of all. Seo and Ayo. The new game. There is no at some point you are going to have to start producing content in order to.

Drive inbound. Like, yeah, right, so? Regardless of what you choose to do it now or later, you can do it when you start. There's going to be a lag, so assume that it's six months, nine months, whatever it is, right. And. Either just using fog, or like, I think she's basically he's he has built out now a.

An agent that looks at their internal conversations about whatever product feature they're going to do or whatever. Stupid little s***** thing is, and it's releasing, like. Multiple articles just a day, right? Automatically, but he's not even touching it, or maybe. And so, he has like

Speaker 1   51:47
A Blog page and also on LinkedIn, like the LinkedIn page for the. Whatever, something like that?

Speaker 2   51:56
You know, I've been consuming the tweets because he's in my team and I was, like, I'm supposed AI. Is it not AI, um? But good enough. Yeah, right. And maybe it's there or whatever. And I think, um, what? I've come to realize, and we should have done this. A dance box.

We didn't because we had all these leads. Um, is. You should just start. Even if it's s***** content, right,

Speaker 1   52:23
Right?

Speaker 2   52:24
Even if you just tell it look, we're targeting people that are on ABM and 4X that have blue screen Erp and medical doctors is what we're doing put. Like, just telling it to come up with, like, some work plan of topics that are interesting to those people and plug it into whatever your internal slack is and how you're talking about the product and whatever, whatever, and just have it start s******* out content, right?

Like? Like, this is one of those times where? Um. It's such a low effort to get it up and running relative to the leverage it gets you, and it just starts moving you across that six month timeline. Um, the the lag for?

Speaker 1   53:07
Aeo and SEO to start treating your domain as like, oh, this is where we get content from.

Speaker 2   53:15
Yeah, that's right,

Speaker 1   53:16
Yeah,

Speaker 2   53:17
Just start, start producing it. Um, and I mean, like, I don't think you need to over rotate on it. I don't know what front end you use, but like, you know, just like basic, like, make sure there's a Blog page, and it's roughly SEO optimized. But yeah, I mean, fun.

Does it fold for you anyway now because? Um, yeah, but we're very, we're we're, uh, we're we use, um. Astro, which is like a static set generator. Nice. Yeah. I have my personal domain on them, cloudflare pages, and I just found out that, like the entire thing has been hijacked.

And, like all my links and going out somewhere else.

Speaker 1   53:55
No, no, it's all it's. This is a custom built set, you know, format site with, uh, using user cell as our as our host and host and? Um, but everything, all our app stuff is on is on. Um, yeah, I mean, AWS, no matter what. No matter what.

Speaker 2   54:17
You're going to need to start producing content to drive in mounts, and it just, you know, like? You're gonna you're gonna be doing these interviews. You could basically do these interviews, record them, and like, have you know, like, and then have? Have it distilled out into a blog post.

I know you're so. It's important to people who all of us managers who have IBM formics. And here's the problems that they deal with nothing on, just anonymize it and put it out there, right? There's so you can just the whole thing can be automated, um? That's very, I think low and and one guy told me basically.

And I think I'm making it to heart is he's, like, you know, what? Like, in the initial stages for this, like getting the marketing flywheel going

Speaker 1   55:00
There

Speaker 2   55:01
Is, it's just you just have to gut it out. And you know, after three months, like one person, will come to the website

Speaker 1   55:09
Right then, after four

Speaker 2   55:10
And, and then it's like one person per week, and then all of a sudden it's one person per day. And then all of a sudden, it's like, oh, wait a minute. Now, it's okay. You know, but if there's no shortcutting it, so you might as well start now.

Speaker 1   55:21
Yeah, I mean, yeah, I hate the idea of getting into Twitter because it's such a f****** cesspool, but um. But I realize that LinkedIn is good, you know, and Twitter is necessary, and people will probably you know.

Speaker 2   55:40
There's a I met these guys the other day who are pretty interesting.

They, they automate it. And then they put a human in the loop. And then they distribute it. You know, I don't. You guys aren't making enough money for. You won't necessarily do that, but. Really, I'd be godsmacked if you. Just get, uh, yeah, yeah, I mean, I have, like?

Speaker 1   56:12
I right now. I have like 10 agents waiting. I don't do a lot with, like orchestration, things running in the background, but I have, you know, named, like, you know, four agents related to marketing and go to market and three agents relate to product development and? You know, and and I'm just used to kind of spinning up new information environments locally and then.

Uh, having them help me with, like, okay, where was I here? And like what you know? What's? What's the next thing? Um, and I think very easily integrate that

Speaker 2   56:46
Since you're already in touch with guy, you just gotten the note saying that I said that he's kind of good at this. Yeah,

Speaker 1   56:51
Wow. That would be great. I'd love to reconnect. It was a really nice conversation I had with him. He's a fun guy to talk to. He's a tough guy, but he's fun. He's a very tough guy. He's Israeli. Yeah, you can, you know, that's? I've got cousins, you know?

Speaker 2   57:14
Uh, good luck. I mean, it's. It sounds like a big, wide, open thing to do so, you know. And I don't think the dudes that are running IBM and more makes are going to set up Clan. To do it for them so?

Speaker 1   57:28
Fair, I mean, we have competitors too. And I think we are, if not, feature parity, you know with them, we are. I think we're doing the valuable part for the most part of what they're capable of doing. And they've all raised like 30 to 100 million dollars, and we've raised zero, so I think that's an advantage.

Yeah, I mean the other thing.

If you do want to raise? Um.

Speaker 2   58:02
This is my take on things other people might have others, but

In AI land. There's, um, there's a couple different models that are driving like, super fast growth, right? One is, you've got a. Business relevant product that is driven by consumer type adoption, right? You meant this was your bdu? Yeah, actually, it is, yeah, I've kind of. I've been thinking about it a little bit.

Yeah, okay. And then. So, the example is obviously charging BT, obviously, you know. But there are others, right? So any of the video generation ones all of those companies have like a consumer relevant product that grows quickly, and then they start doing Enterprise, right? Because that's where, like the real money is and like the stickiness, all these consumers tend to churn in BB land, right?

There are also companies that are growing super fast, and they're the ones that are attracting OVC money and. The the driver behind that is they create so much value, like just the introduction of AI creates so much value that. It's like it just it. You have to do a B2B sales motion on it, but there's just like so much value created that, like it goes super fast, right.

And so, um. And I think that my instinct, um? And it's related more to that. The insight from DashFox is that the bridge between those two is just like kind of product-led growth. And can you find anything in your product that will lead to right to the to the business spreading?

And so um, but

Speaker 1   59:45
Which the business spreading in what sense?

Speaker 2   59:49
Awesome and Mike in the in the DashFox case. It's like by delivering DashFox. I'm opening up a go to market motion that allows my customers to talk to other customers

Speaker 1   59:57
Happen

Speaker 2   59:58
To control it.

Speaker 3   59:59
Yeah,

Speaker 2   1:00:02
Dropbox or slack, or s*** like that, where it's like, you know, there's some elements. Yeah, yeah, yeah. And so, Dropbox is social because you give people access to your Dropbox. Now, they have to. Now, they're using Dropbox. That's right. And so, um, I don't, it's, it's. Immediately obvious to me that any of those paths are open to you, but what I will say is that?

Um. Log standard. B to B go to market motion. For you. Um, particularly, your ACV level, right? You're like, I'm guessing at the charges Enterprise guys, a couple thousand bucks a year or something like that, right?

Speaker 1   1:00:47
Uh, Enterprise guys are signed up for seven thousand a year. I

Speaker 2   1:00:52
Think you

Speaker 1   1:00:52
Know, we probably the biggest customer that we're going after right now, will probably. I would somewhere between I'd call it 30, 000. 

Speaker 2   1:01:06
Okay, so if that's the case. That changes. It changes the intensity of my point, but I still think that, like, you're going to end up with a lot of thousand dollar a year contracts. About a thousand dollar a year contracts and? Basically, a growth curve that goes like this as opposed to like this, right?

AD  1:01:39
Yeah, like, if you're um? And I don't have any. Let's put it this way. I don't have any plans to. Do that. I don't have, like, you know, like, oh, we're gonna?

We just need to do XYZ, and then it's going to take off like, crazy. I can see it taking off faster than the amount of effort that I put into it, certain things going well, like, let's say, you know, we get we all of a sudden modmed for no other reason than their own self-interest starts selling us.

FP   1:01:58
You know, Arthur. So, I think that's right. It's like, so, my, where I was heading with this is, if the goal is to get DC funding. Right, the the only way to get that is, like, through some through really fast growth, right? And so. You know? This, you still got to talk to 50 customers to like, figure out what your thing is.

There's no shortcutting mat, but I think from a GTM standpoint, you should also just be thinking about, like, okay, you know? Very quickly. We need to figure out things that make us. Roll really fast. What happens, um? Because it's just gotten so much like? You know if I said to you, you know, you're going to grow in the next 24 months.

You even go from zero to five million dollars, right? Like? Five years ago, or something that would have been like, great, right, and that'll raise my series a, and then whatever. And I just. It's no longer. All right. It's no longer like that, right? Um, yeah, I mean, I didn't.

AD   1:03:09
I've never really thought that this was look. I mean, I've always I've had the, you know, attitude that I don't even want to talk to VC with this company. Um, until we've really proven product Market fit, some sort of marketing motion like the, you know, like the the? We need.

We need to have a lot of things lined up. And then maybe it might make sense even just to have the conversation. Or even just to get funding. In order to have other more people in the world who have a stake in our success, sure.

AD   1:03:44
But not really to fund operations. Beyond, you know? I mean, if we can, you know, if we can get to that first, let's say. 100, 200, 300 customers at. Averaging $2,000 a year, then it's like, okay, then we can hire like, you know, one or two good people. That looks like this.

Yeah. And my, my point is.

FP   1:04:13
Yeah, yeah, yeah,

FP   1:04:13
Yeah, look not that I don't want it. Not that

FP  1:04:16
If you're doing that and you're making a couple money in the RR, then you could also very much choose to just pay yourself $400,000 a year. You know? Pretty good, too. Yeah, it's not terrible. Um. Um, one thing I? Don't want to. 

AD
So, what? What are you looking for yourself right now?

Yeah, uh, being very mercenary. So, basically, it's weird, like, I think my timing touch wood is actually pretty good. So, um? I'm looking for the founding go to market role at an AI startup. And there's just. The at this moment in the cycle. Whatever it is, is that like, there are a lot of, you know, startups that were like a couple technical guys that raised like 10 or 20 million dollars that have spent the last two years building and have like one or two customers, and they're now hiring the first first UTM, so not necessarily like a cro.

Um, because I'm more like a zero to one kind of guy. You know well funded enough to pay for someone senior to do it right in the beginning, I think, right? And how did these people get funding just because they're been there, done that, or like?

Speaker 1   1:05:34
You know if they don't if they're if they're zero to one, but they have enough money to hire you and you to feel comfortable? I don't even know how to describe these things now, so um.

FP   1:05:49
Uh, previously exited Founders. Um, yeah, that's what I meant. I've been there, done that. Yeah, Y combinator Affiliated kind of companies. Foundation model of Jason, but like? Enterprise Focus companies. So, like?

FP   1:06:11
One second.

FP   1:06:21
Um. And, you know, the gussing it up, but basically, it's. Um. Yeah, I don't even. I don't even know that qualitative. They're like different. You know, um, there are a lot of them.

AD   1:06:36
Yeah, I think having that funding those funding connections because you exited because you because you went through a program like, YC. You're like you all those things make. Yeah, starting position. 

FP   1:06:50
Yeah, I mean, and I, you know, I see that with DashFox. It's like, great products, you know, but no connections.

Speaker 1   1:07:03
In that world. Yeah, no, no connections, and kind of like, um.

Speaker 2   1:07:09
The initial. The the two founders are in New York. It's a really interesting story they. The CTO was at a kind of bank, and he convinced his longtime friend to come in as co-founder, and instead of starting something from scratch, they went and bought like an existing small business.

That was already built on Ruby on Rails and then on, and they pivoted a few times, and so, like. And so I think, like their original Vision, was almost by this thing and just kind of, like, we both make a few hundred grand a year. And that's great, right?

Yeah. What I just describe to you is like this very narrow vision, and so that doesn't lead you to, like, okay, let's go raise 10 million dollars and tell some crazy story. And then, yeah, yeah, whereas? Whereas, you know, when you're 22, and you're in Silicon Valley. And it's like, you know?

50 billion dollar market, and that's what I'm going to go after. And that's where I'm gonna go sell, you know, like, I think? Probably the skill sets aren't even that different, and probably the idea is not even that different or at least qualitatively. So, um, yeah, it's just a different game.

Yeah.

Speaker 1   1:08:22
So those are the kinds of yeah say again, so those are the kinds of opportunities that you're looking at that. Yeah, so that kind of first GTM, I, you know, I think there's, um.

Speaker 2   1:08:33
There's a small shot that I, I mean, I've had a couple conversations about, like doing an outside CEO gig again. Um, but those tend to be fewer and further between. And, you know, ironically, they pay less so. It basically would mean. Make less money, but take on more risk.

And I'm kind of like, I just like, sort of, like taking this thing. I've gotten a bit sale. Do you still have um? Equity, and do you have equity in dashfox?

Speaker 1   1:09:06
Yeah, I can't pay attention. I, I have to exercise, but yeah, okay. I mean, I hope that I hope, obviously. I hope they make it, um. The reason I ask is that I've actually been involved in. Almost like the opposite sides of what you just described. Um. But um?

But let's just say I know a lot about mining email for leads. Yeah, yeah, but in a totally different Market. Interesting, really? Oh, go. Um. Okay, as long as you don't run to DashFox and say, hey, guys, you're doing it all wrong. Go after this Market.

Speaker 2   1:09:50
I shouldn't guarantee that I won't do that. Okay, okay. Okay, I mean, it's a very different. It's a different, um.

Speaker 1   1:09:59
Uh, it's. It's for the legal market. It's for legal sales. Oh yeah, yeah, we looked. I mean, yeah, we. We definitely looked at that vertical, um.

Speaker 2   1:10:10
There's there are a few things about it that were, um, that were interesting. One is like, interestingly, lawyers don't like paying for stuff. Oh

Speaker 1   1:10:18
Yeah, no, they're terrible, f****** clients. That's why I haven't. That's why I never even. I never really, seriously, thought. I still, I, I did this. One-Off analysis, where I mined a friend who's a lawyer who's built an incredibly successful business, and I, I mined all of his email for all this stuff, which I'm going to.

We'll give away any secrets there, but um. But the but? But yeah, it's like, you know, then we're talking about, like? How he's even gonna, you know? Uh, he's sort of out of the out of the game a little bit, so he's not that worried about, like, you know?

Going to essentially competitors and selling. A platform. If you could sell it for enough? Um. But um? But yeah, it's just like every every. I'm still like skeptical that, you know. Do I really want to even deal individually, let alone with, like a whole Law Firm? Dude, I just came off of trying to sell.

Well, I, I think I did in fact sell some property today and the whole process. Um, went ended up going to lawyers for a variety of reasons. And. Um. The long story short, I ended up dealing with the lawyer who has bad intent, right, who's literally? Who has like?

Speaker 2   1:11:42
Conflict of interest stuff going on. Really? You know, like, yikes. And he works for, like, I'm paying him. So, um. It was horrible, like, just dealing with, um, dealing with. It was really, really stressful. So, like, like looking back, because we, you know, we thought about various directions. We would take dashboards in and.

Yeah, just having lawyers as clients I think would be.

Speaker 1   1:12:11
I mean, I, you know, I went to law school. I have a lot of friends who are boys, um, and I, I think they're mostly, you know, most most of the lawyers that I look almost all the lawyers that I know? Like, there's a lot of good intent. There are a lot of there are a lot of.

There's a lot of trust that's well earned. Um and well enforced, you know? When I left my job at a law firm, I was allowed to go into the office. They had fired me. I was allowed to go into the office and. Not retain, but like, go through and find whatever I wanted to out of my documents.

I had full access to all client information for 3 months.

Speaker 2   1:12:48
As

Speaker 3   1:12:48
Opposed to like

Speaker 1   1:12:49
In finance when you would literally be let out and you get your s*** in a box. Yeah, yeah.

Speaker 2   1:12:56
Yeah, yeah,

Speaker 1   1:12:56
So you know, they're but, but as far as? Customers. Mean they think they know everything they don't want to pay for, anything you know, and uh? You know. And then they, they hire, like, extremely bureaucratic, like technology companies, that

Speaker 4   1:13:15
This is so funny. I think it's very funny when little kitty here, like.

Speaker 1   1:13:21
It decides to like he hit me on the shoulder. It's like something wrong with you. You're not paying attention, I'm sorry. But yeah, there, then you have to deal with like the law firm tech department, which yeah I didn't like definition. Risk averse. Yeah, and I mean, what you're doing like, it's like.

Speaker 2   1:13:40
We're going to read all your email and like, you know, we don't. We don't look at attachments, but like, you know, everything else, and like, yeah, no, and in real estate, it's amazing. There's only one of the national Brokers who are, like, oh yeah, we won't let you access the emails of our, um.

Of our Brokers, right? Like, the right Department had an issue with it, but like we, and if you think about, like, you know, the pi that gets exchanged during a real estate transaction. It's pretty pretty P, right? Yeah. Uh, and. No, didn't come out, doesn't doesn't come up. Yeah, no, they're very, they're.

So, yeah, the other thing, um?

Speaker 1   1:14:24
Just so you know that I've been working on this and not. I have been working with a friend who doesn't. He only does, uh, rentals. But on automating his process and possibly helping him helping him, uh, create a product out of it. But that's like that. Very side side project right now!

What I've been actually more interested in, which is, I think, unrelated, but it uses the same quiz.
