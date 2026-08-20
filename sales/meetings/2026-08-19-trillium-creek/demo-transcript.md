Quality practice.

Speaker 1   00:01
We've got several locations. We have a Medina, Worcester, Wadsworth, Brunswick, Strongsville, so we have five locations and a Mo's surgery Center. Um, over 14 providers. We have nd's Pas RNs. Not sure what else you want to know?

Speaker 2   00:20
Um, no, that's that's about it, I guess. Uh, my my, uh, and I guess we, we gathered that from. Um. The from from looking at your you know your your your web presence, but um, what in particular are you looking for in um? In data analytics. Um, I just kind of stumbled across your platform looking on the mod Med, like synapse.

Website, and there wasn't obviously a ton of information, uh, but I just wanted to reach out and kind of see what you have to offer.

Speaker 1   00:56
Um, we have been implementing a lot of AI and automation across different parts of the practice.

Speaker 2   01:02
Um,

Speaker 1   01:02
We do run a lot of monthly reports daily weekly, so we just kind of wanted to see what you guys have to offer. Are you connecting directly to the modmed API in order to do that? I run everything straight out of mod that directly I use all of their reporting functionality that they have natively so I can connect or use anything external right now.

Okay, but I guess

Speaker 2   01:26
I was curious what the, um, automation that you're doing with, um, you know where, what the data sources are for that or is is? The other automation. Yes, the other automation is typically usually through an API. Okay, but not, not, not not. You're not doing that with modmed data yet.

Speaker 1   01:47
We are so, like, not with reporting, but other parts of the practice we have apis for. For example, AI voice for scheduling. Okay, sure. Yeah. Um, sure, well, um? That is very good to know.

Speaker 2   02:07
We are, so we're hi, Aaron, um. Welcome, sorry. I was just meeting with one of the marketing ladies, uh, no problem.

Speaker 3   02:15
Nice to meet you. Um, we are Arthur and Scott, and we're the two founders of dashbud. Um, we're.

Speaker 2   02:23
A reporting platform that leverages AI, so we're not, you know, we're not in, uh, just an agent. It's really more like a system. Um. It is a system, in fact, um. That allows you to pull all of your data into one place and then have, like, a, I guess, a more structured approach to, uh, running reporting, rather than let's say Vibe.

Coding reports, which I guess you really wouldn't ever want to do with, like a, with Claude, you just wouldn't want to sit down and say, hey, Claude! Here's a whole bunch of medical data. Here's an access to an API. Go ahead and and write me a report. Uh, obviously, you know, I mean, you, you can do that, and you can create your own guard rails, and you can like, be very, very careful about that.

But, um, I guess what? You know where we differ from, that kind of approach is that it's really Safety. First, it's it's it's privacy first, um, and uh avoiding. Um, you know, avoiding the the issues that can arise from that and also, um, you know, when you when you start setting up those kinds of that kind of report.

Systems like that, um, and uh, as far as Michelle said that you hadn't hadn't actually started doing that. Um, with, uh, with your existing, um? Um AI automation that you hadn't actually been reporting yet, but um. The other. The other question there is just sustainability, so you know if if if somebody leaves, um, will, will somebody else be able to fix the code that they vibe coded that they may or may not.

You know, I don't know what your level of coding expertise is that you apply to this, but you know if if Claude generated, or whoever, whichever pick your agent generated a whole bunch of? Um, python code for you. Do you have somebody you know? Does the person who, uh?

Who who vibe coded it or who you know who generated it using AI fully understand it themselves? Is Claude running? Every time you generate a report because that's very bad because it's because it's non-deterministic so you can get a different answer. Depending on what day you asked it and not because the date is different, just because Claude decided to do something different, because that's what AI does and then the and.

Then, finally, you know, if somebody leaves, can somebody else just take over that whole, um, set of automation very easily? Um, and so dashboard is designed to solve a lot of those problems, and I know we're probably running ahead of where you are. But um, we do, you know, often one of the biggest questions we get and what you have.

Very, you know, we're very happy with our answer to is, why not just do it myself using automation tools?

Any questions or thoughts about that? I, I do like to have that conversation right up front because it's, you know, it's. It's a good one to have.

Speaker 1   05:18
I think I don't have any questions initially. I think we just need to dive a little bit more into, like what it looks like how it works. That kind of thing, because right now I'm not really sure. Like what your software does other than help with reports sure, sure?

Um. Will then, um? You know, I will.

Speaker 3   05:45
I guess we'll jump right into a demo because it's, uh, that's if that's the right approach. Um, that's fine.

Can you do integrate with mods like you on their website? Um, we.

Speaker 2   06:18
So, the we had a previous version of our product, which integrated with modmed, and we have totally rebuilt our product, but we still have the code to integrate. We just haven't, um. We haven't had an actual modmed customer who needed it. So, um Scott you, you, you have a relationship with modmed correct?

Yeah, um, I. I have a relationship with Adam. Do you know Adam cooperman? It's not someone I think I regularly work with. Okay, um, yeah, anyway. The short answer is yes. We have a really a good relationship with mymed and. We could. You know, pretty smoothly and easily. Um, get the API, uh, get the connectivity back back on track.

Speaker 4   07:11
With, uh, with the platform, so that's not. That's not a concern.

Speaker 3   07:19
All,

Speaker 2   07:19
Right. Well, so this is dashboard, and this is a typical view that you might that you might use. You can, you know, type in, um? Analytical questions about your data, and I guess you know, it sounds like you're all you all. Fairly Advanced, and uh, you know, in terms of?

Um, technically, so I'll take you back to the very beginning. Data sources, what we did, and you know to prepare for this. We just we, we created. A we, we have a standard, um, medical practice. We. Demo. Uh, created a Dermatological practice version of it. And um? You know and, and so we and we loaded that in.

That's one way that you can access data, so if you don't happen to have a connection to certain data sources. You can absolutely load them in as Imports, and we even have, uh, an append feature so that, um, we can append and deduplicate. Let's say there's, you know, you have your latest month of data, and you just want to drop that in, and you want it to, um.

Update your tables not to. Have to go through like you would in Excel. You would have to, you know, figure out, you know, a pen, exactly, to the end of um? Of where your data ends. Make sure that you don't have any duplicative data. Um, and we kind of handle all that.

And as you can see, it's well, you couldn't see there. But this was this is a, you know, a multi, um, cable demo, data set, and so apologies, if any, if it's if it's a little, um, you know if that this is, we're just working off of demo data.

Obviously, we can't work off. Real medical data. Um.

Speaker 4   09:05
But so this is the view. I guess you

Speaker 2   09:07
Could call this the view from a from from our agent. What our agent knows about your data. We are absolutely dedicated to not giving. Raw data to AI agents. We think it's, you know, it's irresponsible. It's. You know on, it's probably you know, in most cases, uh, 99 of the time.

It also would be like, not, you know, HIPAA compliant. Um, and uh, and so, you know. So, so what we do, what we? Exposed to our agents is really just all the information they need in order to. Understand your data and write accurate queries against it. So, you know, in this case, we have a patient.

An appointments table. That would be this would represent, for example, an export from modmed. So, when your appointments table, you know? All of these, uh, relationships patient ID provider ID. These are all established within the system, and so it can write multi-table queries to pull the right answers out.

Um, and again, you set this once. If you have particular information that you need to fill it in about, like, here, I had some. Office data, so I actually allowed it to look at just the locations, so it knows the actual locations of the office. So it's not offices, so it's not guessing when it.

Um, when it writes a query for a single office, but that was again, that's not PR, private patient data, and so it was only allowed to look at. Um. That data in particular? Um, but you see, you know, the? These are all. Basically like tables and columns, and then you can.

Also, if there's something particularly like, you have different words that you use, like, you know, um, encounters or also visits or? Um, you know, that kind of thing if it's intuitive, then AI is pretty smart, and you can get it. But sometimes, you know, a particular column isn't named very semantically, or you have particular.

Let's say you want to pull in some accounting data, and you have particular accounting practices again. This is where you would, um. Inform our agent about all those practices so that if you're doing, you know, accrual based accounting. Um, it? It knows that, and it doesn't. And, and it doesn't.

Provide incorrect answers based on. Uh, other accounting systems, so. You know, this is not a page that you'll visit all the time, but I find it's actually for people who have kind of a technical background. It's useful just to know just to see the um. This step in the process.

Um, and that it exists, which again, this is like, what we're solving against for sustainable reporting for, um, for all sorts of, let's say, mid-tier businesses. Um, data Explorer is where you ask questions and get answers so? Count diagnoses by type monthly, you know, again, we we put in.

We tried to put in some. Dermatology. Diagnoses, but you know, again, this is just pulling directly from the data set that we that we loaded in. If there were particular, let's say, categories that you wanted to impose on this. So, you didn't really want to see the raw diagnosis codes, but you wanted to say, you know, this this?

Or, you know, actually, I guess, like ICD-10, is pretty well organized that way. So, like, you could, you could actually. Say, a higher level code, and you want to filter on that on that description again. You can educate the, um, the semantic model on that, or you can load in an additional table that it can read in order to understand exactly the kinds of questions.

But you might also just want to. Uh, you know, ask, like, more kind of utilization questions, um? About, you know how many visits different providers are are taking on in any given week, and so that kind of this is again, uh, use the wrong office name, so I'd actually given it.

I changed the office names on it, and uh. So, uh? So, Ridgewood office is the correct the, the correct naming, um, again. It's conversational, so I, you know, I gave it a, uh, a not very good? Question, um, and I then actually. What I realized was, I actually hadn't let it inspect the office names yet.

So

Speaker 4   13:53
When I gave it Ridgewood office, it?

Speaker 2   13:56
Ridgewood, it just asks for Ridgewood. Um. Now that it knows allowed again, notice that it's very restricted, what it's allowed to look at now, that it knows that the name of the office is Ridgewood office. Um, it creates the correct query.

Um.

Speaker 4   14:16
Any questions about that process?

Speaker 1   14:19
So, basically, here, you just ask. It's quite it's question. Ask it a question for a report you want, and it pulls the data from modbed and just spits out the report. Correct? Okay, yeah.

Speaker 2   14:34
And then you know. So now, this is a great interface for generating reports. And if you also have ad hoc, you know reporting questions like, you just have a very specific you want to drill down to a particular, let's say, provider, um, or a combination of data. That wouldn't be so easy to get out of.

A reporter dashboard, or you wouldn't want to generate. You wouldn't want to go hunting through a report for, you know, for. For a provider specific answer. You can just ask that right here and and and get that particular answer.

Speaker 1   15:11
Okay, I see there's a favorite section. So, each month, we have a set of. I would say 10 to 20 reports. We run the same report every month after we're we close the month. Yeah, would that be something we could set up as favorites exactly?

Speaker 2   15:27
So, from here, you would just save. Let's say, you know, you're creating that favorite that monthly report, um? If this is one of this, might not be one of the? Ones that you put in there, but you know, this is like a top diagnosis. By month. And again, you know.

I put in a lot of monthly to show the how it graphs. Time series data. If you have more if you have more. Non-Time series data like you just want to see last month's? Um, information, then that's. Uh, that works as well. Um. So, now I've you know, I'm gonna just add.

Like, again, I'm just adding reports that are already in here, but um, this one was, uh, provider weekly. Uh, procedures. All right, and I've saved these over here. So, you know, I might have asked a lot of questions, but I'm not really interested. Long term in the answers to those questions.

Or maybe I just didn't get exact. It didn't. Quite. The agent didn't do exactly what I wanted it to do. There sometimes is a bit of trial and error.

Speaker 4   16:45
Um. You know, we don't just force you to, you know?

Speaker 2   16:50
Look hunt through all of these different. Uh, things that you've looked for in this conversational interface. We allow you to save those for the long term as assets, and then if you go into the dashboards and reports section. Um. Uh.

Speaker 4   17:10
I already had one report in here. I can edit this and

Speaker 2   17:13
Just add. Um. Top diagnoses by month and. That's. And I can.

Drag and drop it. As as I will. Um.

Speaker 4   17:44
Um.

So, yeah, go ahead.

Speaker 2   17:50
Yeah, uh, no,

Speaker 3   17:51
I was just going to add. You can, if you want to change the view from a chart display to data display. You can also view the data, view the chart, or view the report as as data. Right? And these these. If you just want to see a table like that, um?

Speaker 2   18:10
You can also that way. You know, you can have higher dimensional data that fits into a table and doesn't really. Work in a like, you know, in a in a in a chart, um? You can add also add, you know, easily add line, like a total line where you can add if you were interested in the diff.

Let's say you were comparing like q1 and Q2. You can add a difference line very easily right here.

Speaker 1   18:37
Okay, so you just said you can compare, like, do one versus Q2. Can you compare different things? Um, with previous years, so we do a lot of things where we look at this month this year versus this month last year, like provider, how many patients did they see in this 26, 25, 24?

Speaker 4   18:57
Yep.

Speaker 2   18:57
So, in the data Explorer, if you just said, I'd like to see. Um.

Speaker 4   19:46
Did it get it right?

Speaker 2   19:55
Only show me Jan 2026, so let's see.

Speaker 4   20:37
I got a little confused by that. Let me just show me.

Speaker 2   21:16
All right, and then the way I would do this in, you know, I'm sort of bailing a little bit here, but I can, um. I can.

Speaker 4   22:03
I'm fumbling around a little bit here. Um. Trust me, it's possible. But I can I, I will, if you, if you would like to, um. See.

Speaker 2   22:14
You know, a more, um, a more customized demo for, like, the kinds of things that you want to report, you know, we're I'm happy to spend some time and make sure that that those reports are actually like, um. That are those are fully baked for the for our agent, um?

Frankly, I've been. I haven't worked with this data set in a while, and so I, I would like to to, you know, would love to, uh? Would love to, um, produce exactly the numbers that that you need to see, and then show you how that it's generalizable. Because our goal is not to,

Speaker 3   22:45
Yeah,

Speaker 5   22:46
So all the data and everything that we would want to inquire about, though everything is basically you have to type in. Potentially what it is you're looking for? So, we would have to learn and understand what words to be using what inquiring.

Speaker 2   23:06
Yeah, and that sounds like a learning curve, but actually, it's it's. In the end, it's pretty, you know, I actually haven't run a month on month report. Um, in a while. And, uh, and once you get the hang of it, it's just, I mean. You know, I've used. You know, Tableau power bi Domo, you know, compared to the kind of pointing and clicking that you have to do in order to get a report right in those platforms?

It's a lot easier. Once you get the, you know, once you get the hang of it? Um, because again, it's just, you know, that it's, it's kind of. It's kind of more like magic words.

And is, um.

Speaker 5   23:51
How detail can this potentially get if I want to get into? You know a couple different things like various locations? Um, by diagnosis. What we're collecting on diagnosis? What an insurance companies are paying in comparison to each other for those type of things. Is that all? Capable.

Speaker 2   24:16
Absolutely, absolutely. That is actually, you know, some little little display things like comparing, you know, two months of comparing, like year on year. Statistics can be are actually much more dicey much more. Require a lot more Nuance than just the basic

Speaker 4   24:38
Filtering.

Speaker 2   24:40
On on multiple Dimensions, so that stuff it. It does very handily.

Filtering and and and sorting? Um, and uh. And one thing that we have some of you can see in this in this report here is, is parametrization so that it actually allows you to create a? A report. That.

That is, uh.

Speaker 4   25:21
You know, there

Speaker 2   25:22
Can be there can be, um? Custom filtered on demand.

Okay.

Speaker 4   25:48
Other thoughts? Questions. Yes, I don't have any other questions at the moment. I think I personally just need to.

Speaker 1   25:55
Digest. Probably regroup with Aaron. Yeah, okay, the same. Yeah, sure. And we're happy to set up a a trial for you if you would like, um. You know? You can put either real data that you have in in.

Speaker 2   26:14
And you know, we can't connect directly to the AP of the modmed API right now, but we, um? You know, you could certainly put in whatever data you need, or if you want to sign, you know, an NDA. And, you know, and would prefer to see some reporting that comes directly out of the system.

Um, completely, transparently, I'll, you know, show you how, uh, you know, how I generated all the reports? Um. Then, or, or even, you know, even if if you want us to generate a demo, uh, set around that, or you have some demo data. If you'd rather not put live data or real data,

Speaker 4   26:54
What is the pricing structure for this?

Speaker 2   26:57
So, for smaller installs, we we charge 40 dollars per month for an annual contractor fifty dollars a month if it's monthly. Um, and that's per seat. And that is for active users of the platform, so people who will need to access the report generation. Capabilities. If it's? If it's, uh, you know, so that then, and you, we have a two-seat minimum in order to allow.

Basically to allow you to share reports with users who aren't paid users. Um, so for two seats. For one seat, you get, you know? You get, um? Uh, you know, a, a system that you can use yourself, and you can say. Um, you know? Forward a report to some, a report to somebody.

But if you want the full Federation distribution of data, you know, to all, the to all the all the stakeholders who might want to see it. Um, then you get, you know, live dashboards and? And Report sending. With with two seats.

Speaker 5   28:19
Okay, so if Michelle and I just want access, we want to be able to generate whatever data we want to generate and print and review just her, and I is it a hundred dollars a month, then yes, for monthly, and then for annual. Discount it somewhat.

Okay.

Speaker 4   28:42
Well, I appreciate it. Let me chat with, uh, Michelle. And then we will Circle back. Okay.

Speaker 3   28:50
Great!

Speaker 4   28:50
Great! Thanks!

Speaker 5   28:51
Nice meeting you! I appreciate your time likewise! Thank

Speaker 2   28:55
You!

Speaker 3   29:04
Catch you on the other line. Yeah.

Um,

Speaker 2   29:36
Agent got Dumber. That was a that was something that I've done a million times with. Maybe there's something in the data itself, but the. But that year on year report is exactly what I was producing. For. For um? Verb, uh, Omega.

Speaker 3   29:54
There you go.

Speaker 2   29:55
Yeah, that year on your report is like, it's pretty basic s***, and honestly, the agent should not be that stupid. And, um. But it happens. Sometimes the age the agents change over time, there's drift. And I need to check to make sure that we're using the most up-to-date agent.

Um, if we need to, then we need to. Then, we should upgrade to, um. To a higher. Agent, but that was f****** that sucked.

Speaker 3   30:22
I, I thought, the rest of it was, was fine. Like, I thought, the rest of it went well. Um, yeah, that was a little bit of a hiccup, but I don't think that. You know, um, I think the rest of it was. Was fine really. I, yeah, okay, good?

The other thing is that one beat yourself up over over that? Um.

Speaker 2   30:47
Yeah, thank you. I'm bummed, but um, I will, um, I'm gonna go, and I will not beat myself up, but I will go and figure out what the f*** happened there, because that was annoying. No, I can totally appreciate all that's frustrating. I totally get it, um? You know?

Yeah. I think that.

Speaker 4   31:16
I think that they were very, very tough reading. First of all, I hate when people don't have their cameras on. And meetings like that? Yeah. That's like. You know, so I'm gonna eat something. Oh wait, let me turn on my camera. Sorry. And then you can watch me eat.

I think that. That right away of determined, you don't know. That automatically. You're gonna have a tough time reading here. Um.

Speaker 3   31:56
And I don't think they, I think they, in addition to that, they were just a tough read. Um, like the similar word answers. The voting, uh, oh yeah, that's cool. Oh, that's. That's. Unfortunately, they can do that. Or, oh, I wish we could do this. Or, you know, like, there's nothing Beyond, okay?

Um. But you didn't get that. You know, you don't get that. Yeah.

Speaker 4   32:28
I guess I think the fact that Aaron? Um, how you know what the pricing structure is? Food. Well, because I think there's an interest, I think that. That usually. Is indicative of there being an interest. Up until. That point at least. Right, they're interested, and they want to know how much it is.

Speaker 3   33:01
Then responded and, and, you know, went over the pricing structure. All I could think was, we're f****** giving this thing away.

You know, um not. I'm not saying we should spend time revisiting our pricing structure, but like, we gain some more traction. I think we should.

Speaker 2   33:35
Especially for? Smaller accounts.

Yeah, it don't. Even even if it's a larger account, it's still, it's still really inexpensive. Um. Yeah. No, I feel funny saying that, it's like, yeah, and there are two of us here. Trying to pitch you on it, but we're early, um.

Speaker 4   34:07
I think that. I'm just trying to. If it's worth going back to my bed and?

Speaker 3   34:20
Establishing the whole API.

Having a conversation again.

I would absolutely do that.

Especially

Speaker 2   34:35
If we could possibly demo for mobmed. And say, hey.

Speaker 6   34:40
You know?

Speaker 2   34:42
Because again.

Speaker 4   34:44
I haven't used Domo in.

Speaker 2   34:46
Three years, but Domo is just again. I don't want to say like it's s***, but it's bad. It's hard to use. Yeah, you do not want. To put that force that on people. You know, here you have. Technically Savvy, but probably non, you

Speaker 4   35:09
Know, operational people. It seems like.

Speaker 2   35:12
Um, why the f*** do they want to be like clicking around and stuff and being, like, Oh, that generated no data? Why? Because I got my. Axis selection wrong or something, you know, all the stuff that they they they do to make things hard? So, yeah. And also,

Speaker 4   35:30
I think

Speaker 2   35:31
Modmed is probably. I mean, Domo is probably more expensive than us. So? Because it's considered an expert tool that you give to, you know? Did Alice? All right, I'm gonna, uh, connect with.

Speaker 3   35:50
And we're going to do.

Conversation, um?

And also. Yeah. Both on the API frame and on the. Just a bigger conversation about data analytics and Reporting. I mean.

I mean.

Speaker 2   36:24
If it's easy enough just to say? If they if they don't want. Invest time yet.

Or, you know if their partner, new partner, if they didn't get a new partner, person, or whatever they, you know, if there's there, any issues where they are, like, well, you know, we don't really want. Talk about having you be like an official partner. For whatever reason, I would.

I'd be very happy. Just to connect their date, their their API, and be able to say that it's that and then and then to Market around that. Um, yeah. To come up in searches of like modmed data. You know, because that's that's an area, you know, you're taught. We've talked in the past about SEO, and what we should invest in SEO.

Having a page dedicated to how what you can do with modmed? Um, with dashbud is a very good way to rank like, you know, once, like, right up there, when somebody says. Modmed data analytics.

Speaker 3   38:29
Yeah, okay, um?

Yeah.

Speaker 4   38:48
I want that

Speaker 2   38:49
That one demo moment back. That's, that's all I thought I thought it went. I thought it is when I, I agree. They're very, they're tough read. And I don't love people who. You know, don't turn on their their cameras and who, like, basically tell you like, yeah, we're like a five office durm practice.

It's like. Okay, okay. But what, what else, like, what do you specialize in? Yeah.

Yeah. But um, yeah, here we are. We've got our. Shining faces all nice in front of you. This is an opportunity for you to have to tell your story. People who care? Anyway. When I can't read people because I I?

Speaker 3   39:47
Enjoy meeting people out. I think I'm pretty good at it, and when I can't read people. Either because I can't see them or become this. I get one word answers. It really frustrates the hell at me. Um. But yeah, I think. Overall, I think it was the right move not to do a whole.

You know, presentation. Even though presentation was great, yeah.

Speaker 7   40:21
Some people they just want to see and, and you know, some people they just want to see the s***, and she said that, and so it's like.

Speaker 2   40:29
All right, yeah, that's

Speaker 3   40:30
What you

Speaker 2   40:30
Want. And also, I've given them the Spiel on, like, why you should not Vibe code your analytics platform. Why you should not use do do the same Playbook that you've been using for automation so that you can have voice based a port appointment tracking? That's fine. That's not, you know, patient data.

Yeah. Um, that I think that was more valuable.

To tell them in advance. What I think of? May be planned. To like, just throw Claude on, like, uh, the mod Med API and start have pods start pulling data out and sending them reports. It's not a good plan.

Was that too heavy-handed, or was that about?

Speaker 3   41:25
No, I, yeah, I think it was. I think it was good. I mean, I, I like that you. Sort of. Got that out of the way? Um. I don't know if it would have come out, but I think it was. Clear and? In a very non-technical. As non-technical as it could be.

Um. And. You know, like? I've gotten my questions so much.

That. You know?

Something that I think is worth. Tackling. Being very proactive about.

I actually did I tell you about my conversation with Alyssa my call, uh, she's actually not college friend. She's a friend from Cambridge. Uh, living in Cambridge after college.

Speaker 2   42:34
She's a data analytics person. Um. Uh, we had a. Really good. She gave me a lot of her time. She went over the website and gave me. We went out to lunch, and she, we talked basically about, like dashboard and data analytics, for like almost two hours. Um, yeah, she

Speaker 3   42:56
She

Speaker 2   42:57
Really liked the site look. The same thing comes up over and over again. I think we need to. The website needs to communicate this a little bit more. But. But. But we also need like a dedicated page

Speaker 7   43:12
That's about, like, who is it for? Like, what

Speaker 2   43:15
Is our ideal customer? Who are our customers? Um. That's now come up. Literally. Every conversation I've had with people about the website and the product from a strategic level. Um, and I think the story of like? Of companies that have? And Erp, or some sort of data that they don't.

Have in a warehouse, or even if they have it in a warehouse. And they don't, and they. Don't have the staff to get the answers out of the warehouse? Um. Dashboard is good, good fit, but basically basically, you know, something like an Omega molding where you're where? You have?

Like? You know where you have a 30-year-old system that has all the data you need in order to get the answers you need in order to improve your operations? And, you know, provide better visibility. But it doesn't. Have a s***** s***** data reporting, that's, you know? A very big win for us and then.

Any kind of multi-site business. Where the, even if they're abusing fully modern tools like modbed to Modern EMR, they could be they probably are using maybe some modern. Um. Marketing. Uh, you know tools, they might be tracking where they're, you know. Other things using modern tools, but? Just when you're relying on a system that doesn't have?

Um, good analytics and a lot of these. Again, a lot of these, like a lot of tools, are built. For doing the thing. Not for. Observing the thing, not for reporting on the thing. So, you know, and, and I think, multi-site businesses again. They're the right scale.

Speaker 3   45:19
You don't have to explain to them why?

Speaker 2   45:22
Data is important. Right, because they can't literally can't understand what's going on with their business without somehow aggregating it.

Um.

Yeah. I think that's. That's pretty key. Um.

Speaker 3   45:49
What was? I was going to say, um.

Yeah.

Um.

I don't know where this is. In terms of?

Actually. Yeah, I was gonna say, I don't know where this is in terms of where this should be in terms of priority, but Thinking of either an article? Or a post, or I guess it's? A very good. Lincoln post or a page on the site?

Goes into. Why not? You just use clot. And comparing quad to dashboard.

Yeah.

Speaker 2   47:03
I mean, look, we've already got that in on the website, but it's inside the page on comparing that also has like spreadsheets. Sas platform on board reporting. Um. And.

Speaker 4   47:21
What are the other ones?

Speaker 3   47:33
More dashboard here. So, SAS dashboards bi tools? So, you know, that's comparing us to the Legacy spreadsheets?

Speaker 2   47:43
And AI workflows.

Speaker 4   47:48
But you're right, we could dig into the AI workflows.

Speaker 2   47:53
Um.

Speaker 3   48:05
I think we have a good story there.

Maybe I'll take a shot at just doing a post. And looking into that page. What do you think?

Um. Sure.

Speaker 4   48:31
Yeah, or do you want me to? I mean, I could also write, like a, a little.

Speaker 2   48:39
Peace on on that. I could just write up like. A one pager that's more like, um, less less structure a little bit more like, but like, kind of like a one sheet, like a one sheet. But in web form on that? And then you could. You could post that and then.

Speaker 4   48:54
And,

Speaker 2   48:54
And you could write your own kind of like description and then and then link to that. That'd be great. And then we can see also, then we could see, you know? It would be really. I'd be very interested now that we've got. You know, now that we've got a website, I think we can be proud of.

Which, isn't that like the original? The original website had its problems, but it was good. The, you know, the V2 that I worked on? In the fall. It was an upgrade, I think, over that. And I think now, I think we've got something very. Very good, and it'll be interesting to see how engaged people are going through it.

Indeed. Yeah, oh so anyway, so Alyssa. Let me just sorry before. While I have you her, you know, so her first question is really, you know, who's it for? Um, which is totally legit and. And

Speaker 3   49:48
We need to be more forward about that.

Speaker 2   49:51
Because it comes off as being very general purpose. Which it is, but um. That's a very hard way to. Go to market. Right? Um.

My friend love it. Um, also, the one who's more of a performance Marketing guy he was, like, yeah, I've had. I have a client that has also has a very horizontal, you know, general purpose tool. And their problem is that they, you know? Their users are happy, they, you know?

They, they get sales. Their users are happy, but they also have, like. Of 1 in 20 win rate on pitches. Because they're literally competing against like 15 other products. Um, which I'm happy to say. I don't think we do, but I think we could be even more specific. And have, like?

Nobody who really does as good a job with, let's say. Emr data as we do.

Speaker 3   51:00
And we could call ours

Speaker 2   51:01
If we could. Actually, once we have one customer uses, this way we say the best. Solution. I would feel bad saying that if we didn't have one happy customer. But um? Uh, anyway. So, uh? Alyssa she. Her background in brief is she? I don't know how she got into it, but she basically got in, became a um.

A data analytics person. She, her first job of this kind, was. Was a TIA craft or TIAA. So big, like a fun company that manages funds for, um, for public sector, and like, um, and University and Hospital employees. And then she moved over to popular bank, which is like the American subsidiary of, um.

Banco, Popular of. Puerto Rico. Um, so pretty big Bank, um, and she was there head of. Analytics and her job there was to get them from having no data that they could use. For a proper animal for for reporting on, like anything. Um. You know, between us, she said.

Like they didn't even know how many customers they had.

Speaker 3   52:26
They know how many accounts. Yeah, they could count them, but they're also like, let's say they're all in different systems. It's like. So? So she, she got them from zero through, like, a huge, you know, push to like?

Speaker 2   52:40
Clean and normalize and create pipelines. ETL pipelines of all their data into a data warehouse where they could actually. Understand their customer Behavior, understand their customer experience, understand whether they're winning or losing, how people are coming to them, and basically provide a whole data set for marketing.

Speaker 4   52:59
Um and customer retention. Um.

Speaker 2   53:02
And so that was a huge project. And then she sort of, you know. At some point she was getting really burnt out from working at a big place like that. And. She went over to success academies, which you may have seen advertised. It's like a chain of. Um, Charter schools or something like that and?

They are.

Speaker 5   53:28
And, and

Speaker 2   53:29
They were very, you know, like? The bank was very was very rigorous. They didn't had no idea what they were doing, but once they, but they were also very like they knew that they needed to get it right. They knew that they also what they wanted to stop people from doing this, like directly querying against like raw data resources, right?

Because this is. A regulated industry, so she got also all that kind of protection in place so that they're all their data was going in in a in a clean and sanitized way. So the head of success academies was basically his answer to everything. It's like, let's just throw it to AI.

Why can't we just do that? Now, interesting is how he operationalized that. Which is that he gave everybody in like management at the management level of, like, I guess the individual schools. And the corporate office and a lovable account. And lovable is like, Claude. But it adds API connectors.

Um, so that you can more easily access. All of your documents, spreadsheets, everything that you have. In your corporate. Data world. And allows you to create your own apps. Like, so it allows you to do individual automation.

Speaker 4   54:59
Lovable.

Speaker 2   55:03
Now, I haven't looked at lovable anything we probably should. Um, but? Alyssa was like? Her. Her answer to lovable was like. Shoot me now! Because like everybody starts doing their own analytics. Everybody's got their own answer. The same question. Right, right? It's exactly the kind of dueling spreadsheets. Wild West herding cats.

Um. I don't know. Did you see the herding cats? Graphic on the website. Oh, you should look at the website.

There was a there is a herding God. Um. That's not my favorite page, but. Did enjoy making those Graphics?

So hurting? Cats is, uh, you know, she, she basically. Ended up having to do everything that she would have to do.

And even more in a sense because she has to create a resource that's like foolproof that people can't. Ask questions the wrong way and get the wrong answer.

So?

Speaker 4   56:24
On the one hand.

Speaker 2   56:26
You know?

Speaker 4   56:28
Tools like that using quad code?

Speaker 2   56:33
And Vibe, coding, or like, even a structured vibe coding platform that gives you access. That facilitates access to. Your own data resources or your corporate data resources. If it's not controlled, if it's not if if you don't have? A semantic layer. That's based on shared understanding, and so basically, that's what she was.

I mean, that was kind of the project, and it was. And it was she. She left Success Academy pretty soon after. She didn't stay there long because? When she started running this project, she felt like it was, like, you know, the the CEO just was like, didn't get it, you know?

Speaker 4   57:17
Because

Speaker 2   57:17
He just thought it should just be easy. So when you're doing when you have to then com, like? Commandeer resources. In order to do something right, and the and your boss is like? Why do you even need to do that? That's who cares.

So anyway. Um.

Speaker 3   57:46
You didn't give her a dental noon, right? She just saw the website. But she, actually, she's in touch with, um, her.

Speaker 2   57:57
Her favorite person to work with it, and she's thinking about going back to actually at a higher level at the corporate level at banco Popular, which is the parent company. It probably won't happen soon, but but it's something she's talking with them about. Um.

And. The one, the person she's mainly in contact with, who would be, who is, I guess, her report, or like dotted line report? And she's basically one of their conditions of like going back to the bank would be to still work with him directly. Um. Is like a like a a data?

Guru guy. You know, data analyst, data scientists, data engineer. Um. And so she said if if you and he's still at at the bank, she's right now figuring s*** out. And it's not, you know, it's not, um? Uh, employed anywhere. Um, but uh. She offered to set up if he if he wants to set up a time with him.

To demo.

That's great. Yeah. And, you know, and it might more be like. To get his feedback to. Maybe he knows other data people, or like, get get integrated into some networks of people who like? Do data analytics? Because that's one thing that we don't. You and I are not particularly like.

I would say, like, we neither one of us has been, at least in a very long time, like corporate data, guy. Yeah. Yeah. We at one point. For you guys.

Yeah, not a long time. Right, I mean. And you know, of course, you're, you know, you do, you know, do that for? You know, let's say, mid-tier businesses as a. In an entrepreneurial way. All right as a service, but not.

Speaker 3   1:00:10
But not being inside a corporate system where you have, like a, you know? Those kinds of Demands.

Um.

Okay.

So, um?

I'm writing a follow-up email to thank them for their time and ask them if they'd like to if they'd like to. Uh, have a trial accounts. Um.

Speaker 2   1:00:49
To start a a one month to start a trial. And while you do that? Um,

Speaker 3   1:00:56
I'm going to, uh, reach out to my event and re-engage with them on. Um, the API front, as well as just talking about General. I'm not going to do it as like. I want to replace delmo. I'm going to do it as more, like I'd love to just talk about analytics and Reporting in general.

Right? Yeah, but I think the main the main ask is like we, we want to be a partner so that we can.

Speaker 2   1:01:27
Build our, you know, so that our app can consume your data? And also they have a Sandbox. So we could actually. I don't know whether how much data is in the sandbox, like how much fake data they put in there, but presumably they put a certain amount of fake data so that we could actually run a demo off of the.

Modmed sandbox. That's right. Okay.

Um.

And again, just the other thing is that, like, um? There's a certain amount of data that they expose. That's not, um.

That's required. Like, there's some federal requirement that you have to if you have medical data that you have to allow your.

Customers access to it. And so they they expose an API. That I think it's called IFR or something like that. Um. Anyway, um, it's in the. Did you see the? I feel like.

Speaker 3   1:02:37
Am I overwhelming you with s***?

Speaker 2   1:02:42
Yeah, this is very interesting and important for me to know so. Okay, because I mean, I also created this Wiki that I'm putting some stuff into, and I think I've shared that with you. Yeah, is admiring that yesterday when you shared that. Okay, it's a little. It's a little, um.

You know, not in everything in. There is gold, so it's not, um, some of it's just stuff where I was like. You know, either did some research myself or? Ask an agent to do some research and and then just, you know, had a quick look at it and then dropped it in there for future reference, but I thought it would be good.

You know if I'm doing research if I'm looking up? Like what the top EMR systems are and what their capabilities are and whether they have apis and what the terms are for their. You know for partnership with them, I figured I'd be just going to create a resource that we can both look at and that, like, for future reference.

Rather than? It's also a bit of an accountability thing for me. Like, you know? Just making sure that I keep track of all the? All these. All this research. You know? Work. Yeah. Um, no, I thought it was great.

Speaker 3   1:04:02
I had an idea. That I wanted to run by you. Um. It's going to be a. No longer conversation.

Um.

What if we had, I'm trying to think of? New and creative ways. I'm trying to think of creative ways to.

Business development ideas okay? Um and. What if we had an in-person? Networking event. I'll use operating ports networking event because it's really a thinly veiled promotional dashboard. Um. At our new office.

Um. Somehow. Use it as an opportunity to. Um.

Promote the product.

Maintaining. Um. The.

That working event? You know? Um.

That it's a well maintaining that's a networking event, so. No, I, I like the idea. I think you know if you do it in.

Speaker 2   1:06:09
I don't know what you're like, you're kind of in-person. Network. Looks like you know, obviously, my in-person. Irl in real life Network. Is based in. New York City, primarily New York and Brooklyn. Um. You know, I'm I'm? Focusing a little bit more on just getting dashbud in front of people that I know, might you know, I don't know, to

Speaker 3   1:06:37
What

Speaker 2   1:06:37
Extent? Irl Network is our our primary dashboard users. But I think they are. You know, they may they. They may they have good ideas and are good people to bounce, like. Kind of business. Development ideas go to market ideas, stuff like that. Um. But it's less. I would be, you know, I would be less.

I wouldn't.

Speaker 3   1:07:10
I think at a certain point.

Speaker 2   1:07:14
Like a dashboard, you know? Sponsored Meetup of some sort. I would all would almost be like. You know. Like, let's look at meetup.com. And see if there are any New York area meetups. That. Like, we'd be good to get. You know, dashboard's name in front of? Um. Maybe there something to do with, like?

Manufacturing or doctors, or like, you know, like, specialty, kind of areas? Um.

If you're, you know, if you're, it really depends on who would show up to like the dashboard. Um. Meet up in Westchester! You know if if you think that if if you think that would be, you could get a good crowd, not just in terms of like it being like a fun event.

Because you know you want, you definitely want to burnish our brand that way. And also, we want to have fun ourselves and not

Speaker 3   1:08:16
Have a, you know, something that's like, under attended and or just?

Speaker 2   1:08:20
You know, random, not that interesting people. Um. But a good event. That's a, you know, for those real like networking and kind of like just having an event, it's nice to see people in person in these days of like digital connection. Um. If you think it could be both that?

And.

You know something that gets us in front of people that? Might be like, have like a? At least a 25 chance of being interested in dashbud, like having legitimately interested, not just like. That's interesting, but like that's something I could use.

Then, I would say, yeah. But those are the two conditions that you know that, that it's a good event because we want to have a good event we both want. Attend a good event. Um. And create a good environment for people. Um. And. That there's a reasonable chance of getting in front of.

Of of of? Getting.

Even like? Two to five dashbed trials out of it, let's see.

I wouldn't put it. You know, I wouldn't put the the bar too high in terms of finding. The people. Um. But I would. I would be bummed if we had an event and basically nobody who was. We didn't really get anybody who was. Legitimately interest. Get in front of anybody who is legitimately interested.

Yeah, that's definitely the risk. Um.

I have to give it some more thought. I've gone through my, uh, LinkedIn. Contacts and see who is Westchester?

Speaker 3   1:10:34
Or Connecticut, please. And. See what, technically, what kind of turnout we could? Um. Yeah, oh, shoot. I haven't needed in 3 minutes. Oh, s***. Um, what happened to you? Sorry.

Speaker 2   1:10:55
Would you be able to look into say, hey, we got to follow up for Michelle Maynard. Did you what happened to the um interview because I actually my? My uh, 2:00 p.m. Bumps.

Speaker 3   1:11:06
Oh, um. I it happened she needed to reschedule. Okay, okay,

Speaker 7   1:11:11
Yeah, so I'll let you know on times and then go from there. Okay.

Speaker 2   1:11:18
All right, um, good. Um, uh, Michelle asked about integration directly with modmed. Oh, okay, follow up.

Speaker 7   1:11:32
Good. Okay, I'll forward it to you. That's yeah.

Afford it right now.

Speaker 4   1:11:48
All right. Let me hop on this 215, um, and maybe it's not going to be around.

Um. I think so.

Speaker 2   1:12:00
Let me, um, I, I do want to at least, uh, agree on, like, what our response is to this email, so I will hold off for a little bit while you're, um, and I'll send you a proposed response. And if you have a chance to eyeball it? Okay. Okay, sounds good.

Okay. Thanks, sorry to no problem. I cut this hair properly. Right, right?

Speaker 3   1:12:53
That's fine.
