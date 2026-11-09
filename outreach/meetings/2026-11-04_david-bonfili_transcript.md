---
contact_id: 47
person: David Bonfili
company: Tactical Ventures
title: Managing Partner
date: 2026-11-04
type: meeting_transcript
duration: ~29 minutes
participants: Arthur Dobelis, David Bonfili
relationship: college friend (Harvard), inner circle
source_file: Google Doc (arthur@octetdata.com), exported manually
transcription: Google transcription, raw — not cleaned
notes: >
  Speaker labels are unreliable. Diarization produced three speaker IDs for a
  two-person call and attributes consecutive Arthur passages to different
  speakers. Read by content, not by label. Transcript opens mid-sentence on
  David's "why not just do this myself" question — the demo that filled the
  first half of the call is not in this recording. Last ~2 minutes are personal
  (family, a cat named Dana).
topics:
  - specification / generation / validation frame (Mylovanov, via Bonfili, ~19:46)
  - zero data exposure / passthrough architecture
  - "why Dashbud" vs. raw AI workflows
  - shared rules and governance via workspace + semantic model
  - legacy/crufty data as proven use case
  - pricing ($100/mo or $1k/yr per seat)
  - who the customer is (breadth problem)
  - agentic transformation of business functions
---

Whatever, and just like do this myself. What's the? What's the like value? What's the value add that they're getting from? And you do this instead of just like connecting the data sources to.

Speaker 1   00:15  
And it's fair because, like, for a very simple use case, it's totally fine to do that. Um, the. The the thing, the things that we provide. Um, that, are, you know, more than just a little bit helpful, I think, are number one, um?

Speaker 2   00:35  
You know, a reusable framework. So, you know, once you start getting Beyond just like, I want to move number a over to, you know, numbers a, b, and c into a report that comes directly off of a? Uh, a database, you know, where I have a very simple query or a spreadsheet where I'm just summing one column, right, you know?

Once you start actually doing real calculations, then those have to be somewhat agreed upon and are best kind of set up in advance so that you know that you're doing it the same way. You don't know that you're doing it correctly, so that's the accuracy kind of business rules piece.

Um. Then, there's the. Privacy and governance. Which is that, like, if you're just using Claude to access an API, you do not have the setup that I described where the where the agent only has literally within its what they call control plane. So, within it's a bit, it literally has no.

Ability to see the underlying data. It just. There's there is no, there is nothing it can say or do. It is trapped within this kind of metadata world. Um, it's a we loosen it a little bit for the semantic modeling exercise, but then once you're in the querying, you know world, you're just writing SQL queries on a.

Metadata description. Um. And then, um, then there are all of the, you know, kind of? Supportability. Like, if if you want to support your own workflows forever? Great, but like if you want actually something that you can come back to and it's set up all the time, it's actually a real joy for me with because I have so many.

I do so much data analysis for myself, and you know, and professionally, like and, and literally, just like having to dive back in and be, like, oh, what did I do here? You know, there's a cost to that. And, um. And it's, and so it's it's sort of an organizational.

Um, across at you that that you all float on to us.

And then, you know.

Oh no, no, no, I, I'm just one more thing to that. You know, if you have a workflow that you like a, and if you do want to create custom workflows, or you have like a system that runs workflows for you, or you've really, you know, tailored your clawed environment.

You can always like use our API and use us as the governance and shared business rules layer. So, you know, to limit to limit the access. Now, that doesn't prevent if you set the if you don't set that up so that, you know, that means that you're giving clawed whatever end user access you would provide to an end user.

Now, you could create a special workspace for Claude and say, okay, you know, human beings are allowed to query in, you know, are allowed to ask for XYZ data. Um, Claude is only allowed to see these kinds of, you know? Um, so that's, you know? That's another option. Go ahead.

Okay, um?

And so, who do you think the customer is? Um, it's so the thing is. This is the worst part, um. It's pretty broad, and so there's kind of to some extent. I, I've I can see. I've seen certain use cases work, and so in particular, this kind of like Legacy data work, um.

Use case because we built pretty good tools. Frankly, a little bit on the Fly because their data was so crufty. But, you know, built them into crafty, you know, full of junk? Um, you know? We're, you know, there were some things like, we were perfectly ready for weird for a certain amount of weird formatting, and like, kind of cleaning up data, but we but but?

I added additional. Um. Uh, tools within dashboard for cleaning up data based on the kind of problems that kept on coming up, loading their data in so that that's a place where there's a. There's an advantage that I think you can see, and it saves an enormous amount of like, you know, P folks are cheap, they don't want to, you know, pay a lot of money, for they certainly don't want to migrate their data out of a perfectly well working database if they can avoid it.

They don't want to pay a consultant. You know, let's say, a hundred thousand dollars for a one-time contract to come in and create, you know. Set up a system for, you know, to create a certain amount of reports, you know, it's. It's a model, but it's like, but it gets pretty expensive, pretty fast, and you, it's pretty eye-watering.

The amounts that people quote for a human being just to set, who knows, you know? Ibm and formax, or whatever the you know, whatever your database is. Um. So, what's the cost model?

Speaker 1   06:02  
For

Speaker 2   06:03  
Our cost model is, it's a little underpriced, I would say, but it's yet subscription based. And right now, we're quoting, like, um, you know, a thousand dollars per year for a seat? Um or a hundred dollars a month for a seat, and then you know. For smaller use cases, you know?

Like, you know, half that, but then we're trying to, you know, really figure out? Nobody really needs. A useful business tool. Just for 50 a month. Like, if it's really useful, it's worth 100 a month. So, yeah. Okay, yeah, I guess. So, what I'm trying to do is sort of figure out is, I like.

We've had. It's some number of conversations around.

Speaker 1   06:53  
And obviously the news is is sort of. Build us a number of examples around. That is being set up to manage. For the adoption of genetic systems in businesses. And.

As a question, um. As I try and think through, this is. If I'm a business act? Am I going to try and solve the problem?

Potentially supported data analytics. Or, am I going to try and solve the problem of how I gently agentically transform? Business. Or, I want someone to come in to say, okay. A marketing function. I have an accounting function and I have. Data analytics function, like, here's the menu of, like, I want these three things to be agentified, or I want like you to like, look at the whole business and come back with a plan for what we should into the fire, not identify. Because that's that's sort of like the the. Question in my mind, is, is it? They're like. You've built? Um.

Speaker 2   08:22  
You know the pair of tweezers, but like people may want the like Swiss army knife? You don't have like a good pair of tweezers, but it means that your customer may not be a person buying this was Army knife. It may be the person making the Swiss army knife where you're selling them the tweezers. I think that's fair. I think that you know, I do think that, um.

Speaker 2   08:49  
Setting up those agentic workflows or departments within a company is a. Very valid, kind of scoping for the whole project, and that a lot of people are more in the market right now for that than they are for a. Um, now I don't know if this is the right way to do it, you know?

Whether this actually reflects their like their their best approach, but from a marketing perspective and from a um meeting, people where they are, you know? I, I think that they're probably more focused on the. Ai problem than they are on the? Data reporting, let's say, problem. But if you're like a PE investor and you've bought this company and you have, you know?

Speaker 1   09:44  
Functionally, unless you're just like I forecast the future better than other people. And I know that this is going to be more valuable in the future, and therefore I bought it. Now, it's not how most PE works. Most P says, like I bought this company, and I'm going to engage in financial engineering and make it worth more through that.

But I think increasingly what you're going to see is the companies coming in and saying? About this company, and I'm going to radically improve its margins through operational transformation driven by the development deployment of agentic systems, and so. If you're delivering that solution, then that's very compelling to the sponsors who are invested in these companies.

If you're making like a part of their life easier, that's not that it's not useful, but it's not like the same. Compelling. A position with us. It's like, it's probably not something the sponsor is going to be pushing themselves. It's, it's probably more. The sponsor is going to be.

Agnostic, or like, generically. Is going to have to come from then within the company, and the company is going to be getting pressure. I think to? More holistically. About. Materially transform the business. Rather than like one of, you know? Doesn't quarter functions, no matter how core that function is.

It's just something that to think about. Yeah. And I think you know. That's why I think our one thing that we that we need to. Figure out how to sell better. Is this kind of?

Speaker 2   11:33  
My perspective on this is that you know what you're describing is essentially a Consulting task, and it might actually be something that's in-house at PE. If not now, then very soon that people that go into PE are people who are good at figuring out how to identify like large portions or significant portions, if not large, portions of their business and but, but what, I think, that?

And Dashbud is part of the model that I see. As being like, not the use. Like, I'm really good at using Claude for everything and building everything from scratch. Um, yes, I do build things from a lot from scratch with Claude or with Claude as part of the workflow or with whatever agent is part of the workflow from scratch, or I have my own patterns that I built in my own internal tooling that I've used other places that I can use.

They can leverage, but also that there are parts of the. The stack. That AI stack that you don't want to build yourself over and over again, and also where, like, it's what's valuable, is having both an AI. Surface interface, right? So, like the API, and that's that that is consistent with also what you're showing to human beings.

So, there's a level of, like, uh of, um? Of. Oversight and consistency that you can achieve. And you know, basically seeing, like, okay, I'm seeing exactly what the you know when, when the? When the agent made the decision to do X, Y, and Z, or as part of the workflow, like, here's the data that they?

Made that decision based on now. Some of that's not going to be tabular data that's going to be, you know, unstructured data, but to the extent that it is like Trend based or whatever you're going to want to have a visualization so that you can do what? Ai kind of fakes, which is like, eyeball it?

So, yeah, so being, you know, governance business rules stuff that you just don't want to have to rebuild?

Speaker 1   13:48  
I guess this is like, this is, like, part of just the as again, just me, sort of thinking out loud here. It starts with. Products. Not actually be.

Demantic data visualization and dashboards, and Reporting that the black is the business rules around. Are you access to manipulate? Data while? Providing appropriate. Security and protection. They would hate. David, you don't want to bear. And if that's the case, then?

It's almost a different product. It's like the. Product is the interface rather than what you're doing with the interface, and it may not be. Reporting data reporting. It may be drafting proposals, it may be running marketing campaigns. It may be like any other function within the business, which is, you know, a difference?

Generation. Process, but the interface. Process is the is the say. So, what? You're what you're really building is the way to manipulate your? Data while protecting your data. Yes. Yeah, regardless of what you want to do with that dude. Yes.

Speaker 2   15:30  
I mean, I think that's that's in

Speaker 1   15:31  
That case. Like, that's what I would try. And if I were you, I would. I would like make sure you have that interface locked down, like, work through the use cases, and then I would just sell that. Sell that to someone who is running one of these agentic transformation consulting companies and thinking about going in and understanding the business processes and having the people who build the agents and implementing them really like, yeah, Chef's, all fine and good. But, like, you need a way to connect what you're doing with what they have in the way that people are comfortable with.

And that's the glue that I've.

Sorry, that's the glue that. To that. You've built the like, the the VPN tunnel, the you know? Allow things that are being built in this environment to manipulate things in this environment while protecting

Speaker 3   16:23  
The Integrity of this without having to hand everything over right people over here. So, build your shit here.

Speaker 1   16:28  
Take the stuff there. Let me connect them together in a way that you can assure the data conscious. Person that? Andre is still their boundary, right?

Arthur  16:42  
Yeah, taking the "oh shit" out of agentic innovation.

David   16:53  
Just whatever that thought's worth like, yeah, no? Maybe, if, like, one path is like, selling, you know, secure data analytics tools directly to customers, but another path might be selling the connector, the business rules logic, the methodology for doing that? Do all the companies that are trying to go and do these agentic transformation consulting engagements.

Arthur  17:20
Yeah, and it's more specific. Also.

David   17:27  
Because, as I was saying, I mean, I, you know, literally, this could be for anybody but conversation. Yeah, because the conversation? Link starts out as well. Like, why can't I just do this myself, and you have to explain, like, what it is that you're doing? That's not the stuff that you could just do yourself. But then, when you provide that explanation. Like that explanation is not actually focused exclusively on the data reporting. [17:59] It's focused on the interface for any manipulation of the of the data, and so if that's like a lot of the value add is, and maybe that's actually the product.

Arthur   18:21  
It's certainly *a* product, and it's probably a lot more of a forward-thinking, the kind of thing that would catch people's imagination and attention, as opposed to, hey, I built a better mousetrap. Remember whatever master is, and you thought that you didn't need mouse traps, and how do I protect my data, right,

David   18:40  
Right? So you start with something that know they can use to protect their data, which they don't understand how to do themselves, rather than starting with something that they need that they think maybe they could do themselves for these col new tools that they have.

Arthur   18:56  
Right, well, and the the um business rules and consistency is also a real thing -- if we're doing that at this at scale. One friend of mine who's actually, she recently left a company where they were trying to use Lovable -- they basically had told everybody: you have unlimited Lovable tokens -- build your own data apps. Um, build your own apps, but in particular, build your own data apps.

And she was the head of customer experience and data analytics or something like that, and she was just going nuts because everybody was building their own data apps, and they all said different things. And then, you know, also, there's the security aspect. I'm not sure they were so worried about that. It depends on what kind of business you're in. 

David   19:46  
Yes, the the the other thing I've had for out there and then I gotta I gotta run this other meeting, but you know, I was talking to, uh, and who runs the Kyiv School of Economics, which is a university in Ukraine, and he's been trying to think about how to integrate AI into. The curriculum, and they're running like a summer program is like a concentrated boot camp, um.

To kind of like test out some Theses like in the mental model that he's using. I think it's sort of helpful for people is that? Is a?

A good and valid one. 

If you think about it like that, what the sort of movement into the world of AI allows you to do is to outsource the generation stage. That process that you would have done sort of manually yourself before, but it doesn't allow you to outsource the specification stage or the validation stage. In fact, what it means is the specification validation stage become materially more important, because if you don't specify correctly or validate appropriately.

You're going to have a very good chance of both getting a crap come through the generation process and not knowing that you got a crap out through the generation process, and so one way of maybe thinking about talking about what you're doing here is like providing structure around sort of specification validation.

That allow for more effective use of generation without putting that burden wholly on every individual user.

Arthur 22:04
Pulled noodle on that one. That is a very interesting abstraction of it. 

David   22:08  
It may be helpful. Yeah, helpful. Uh, yeah,

Arthur   22:11  
Yeah, no. I need to think about it some more. What's his name if he has any writings on online? I'll check him out.

This is his name. I don't know if he's written about it, uh? Publicly or not? Okay, yeah, he's the president of the the Keith School of.

Speaker 1   22:29  
Um, very, very interesting guy. I'm trying to run a school touring or. I know, um, yeah. I have a friend who visited recently, um.

Speaker 2   22:42  
For a gig and bounce were falling. It was before it was, like, a month, a month, and a half ago before the bombs were falling as much. It's about bulbs have been falling pretty hard since about July, so I mean there were Aries. Yeah, it was, but it was like I was, I was there like three weeks ago.

Oh wow, um. Uh, maybe four weeks ago, and it was, it was, it was characterized as. But I, I mean, I'm probably. About a dozen times in the last couple years. I would have characterized it is much worse than any other time I've left there, right? Yeah, so. So I've heard.

Okay, well, this is super helpful, so I let me let me think about.

Speaker 1   23:26  
Give me a place that might make sense for like an introduction. Thank you um\! And then come back with that. Yeah. Yeah, I mean, there's there's a couple of.

Someone who started a company. Focus on. Kind of automating the process of. Learn monitoring and evaluation for Community. But not like, uh, underwriting the issuance of new loans, but monitoring existing. Hmm loans and.

Yeah, there may be some. Relevance here. I think about things and, and it's bad, I know, maybe they're just getting like full exposure to all the data ever now. Yeah, you

Speaker 2   24:27  
Know, I'll say one thing. We, we have, um, one of the I complained about Mike, I, I shouldn't complain about mine. I was not complaining about my co-founder, um, you asked the question and? Didn't have a good answer. I'm sorry, um. But he has one of his clients. That's really interesting.

Is a social like a pretty big, like 5, 000 employee social services organization, and they're very interested. One of their they are very much HIPAA, you know, regulated, and

Speaker 1   24:53  
For that. In

Speaker 2   24:54  
Order to solve that and just generally kind of like

Speaker 1   24:56  
Want

Speaker 2   24:57  
Everything to be within their wall Garden. Is, you know, they even would like us to deploy. Um, into their Cloud. As part of the. The deal. So that's another possibility because I am are. We're push button deploy, so literally, I can deploy a dashboard into any AWS.

Speaker 1   25:20  
And. Have priced out an Azure deploy as well. So? Okay, yeah. Well, man. Congrats on, uh, where you've gotten to? With us and. To try and think through how it can be this helpful. And I think? Yeah, I don't have Cadence having a, uh, all day party, but, uh, hopefully, uh, see you soon if he, uh, if he, if he does, are things on the family front.

Uh, good, yeah, no, no, no big changes. Okay, yeah. How about you? Are you an empty nester yet, or you still got one? What's that? Oh no, we still got what we got. A 13 year old boy, who's like having a? Like a dog. It's lovely, but needy. So we got we got, uh?

Or in depth, more years before we're empty. Nesters got it. Still got a chirping birdie there. Yeah, yeah. Our daughter just started college this year, so that's one one down, but we've we've still. Got our son for quite some time. Nice. Where is she? Where is she? Is it Carnegie Mellon she's been doing?

Speaker 2   26:42  
Takes history and public policy, so she's doing their Humanities program, but she's interested in being a lawyer and interested in. Like AI at the law, like the ethics. I think she's in like a really.

Speaker 1   26:56  
Good place for for her, and it's a great school and a cool City, and he's just going to maybe. And do some work for the mayor, uh there, who's you know, like, kind of missing, purple States, uh, big city mayor? Oh, nice. That's, yeah, it's. She's really seems really happy so far.

That's exciting\!

Speaker 3   27:22  
All right, buddy, uh, good stuff, and uh, I'll try and think about some folks that might make sense to.

Speaker 1   27:28  
It gets you in front of. Thank you so much, I really appreciate it. And, but regardless, I, I really appreciate your thoughts. It was a really good session. Thank you.

Just see me.

Speaker 2   27:55  
You're pretty good. You are very good. You're a very good cat. Dana.

Speaker 3   29:08  
You're such a sweetie.