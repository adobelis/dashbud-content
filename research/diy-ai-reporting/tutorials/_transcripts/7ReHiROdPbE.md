# Build Your First AI Agent in 10 Minutes — No Coding

**Channel:** The Tech Girl  
**Views:** 806986  
**Published:** 2026-09-05 13:00:33 +00:00  
**URL:** https://www.youtube.com/watch?v=7ReHiROdPbE

## Description

Build your first AI agent in just 10 minutes — no coding, APIs, or complicated automation workflows required.
In this video, I’ll show you how to build a simple but genuinely useful AI agent using Claude Cowork. We’ll create a Daily AI Research Agent that searches the web for important AI news, summarizes the biggest stories, explains why they matter, and then automatically saves the finished report to Google Drive every morning.
You’ll see how to give an AI agent a clear goal, improve its instructions, give it access to the right tools, and turn the workflow into an automated scheduled task.
We’ll also cover what actually makes something an AI agent, why you don’t need a giant workflow with dozens of integrations to get started, and an important safety consideration before giving AI agents access to your apps and accounts.

🔗 Free HubSpot AI Agent Course: https://clickhubspot.com/6ed411

CHAPTERS:

00:00 Build Your First AI Agent
00:37 What Is an AI Agent?
01:16 The AI Agent We’re Building
02:27 Build an Agent with Claude Cowork
04:08 Free HubSpot AI Agent Course
05:31 Check What your agent produces
07:06 Automate Your AI Agent
08:12 Why This Is Actually an AI Agent
09:00 One Important AI Agent Warning

#AIAgents #ClaudeAI #ArtificialIntelligence #AIAutomation #ClaudeCowork #NoCode #AITools #Automation #Anthropic #GenerativeAI

Subscribe if you liked the video: https://www.youtube.com/@anjanagowtham?Sub_Confirmation=1

❤ Anjana

## Transcript

[0:00] AI agents are everywhere right now, but
[0:03] I think we have made them sound way more
[0:05] complicated than they actually are. When
[0:07] someone says build an AI agent, you
[0:09] probably imagine coding APIs, automation
[0:13] tools, and one of those giant workflows
[0:15] with 20 different boxes connected
[0:17] together. But your first AI agent
[0:19] doesn't need any of [music] that. In
[0:21] this video, I'm going to show you one of
[0:22] the easiest way to build a genuinely
[0:25] useful AI agent using Claude. We're
[0:27] basically going to describe what we want
[0:29] in normal English, give the AI a job,
[0:31] test the result, improve it, and then
[0:34] make it run automatically and no coding
[0:36] at all.
[0:41] Before we build anything, let me quickly
[0:43] explain what an AI agent actually is.
[0:46] Normally, when you use AI chatbot, you
[0:48] ask it a question. It gives you an
[0:50] answer, and that interaction is
[0:52] basically finished. An AI agent is
[0:55] slightly different because instead of
[0:56] giving the AI one question, we give it a
[0:58] job or an outcome that we want it to
[1:01] achieve. The AI can then work through
[1:03] the steps required to complete that job.
[1:05] Depending on the task, it might search
[1:07] the internet, read multiple sources,
[1:09] compare information, work with files,
[1:12] use connected apps, organize everything,
[1:15] and then give you the final result.
[1:21] For our first agent, I want to keep
[1:23] things really simple, but still build
[1:25] something that I would actually use.
[1:27] We're going to create a daily AI
[1:29] research agent. So, every morning, I
[1:32] want this agent to search the web and
[1:34] find the five most important AI stories
[1:37] from the previous 24 hours. I don't want
[1:39] every tiny funding announcements or
[1:41] random AI update. I want it to figure
[1:44] out which stories are actually
[1:46] important, give me a short summary of
[1:49] each one, explain why each story
[1:51] matters, and include links to the
[1:53] original sources. Then, once we know
[1:55] that our agent is doing a good job,
[1:57] we'll make it run automatically every
[1:59] morning and then save the finished
[2:01] report straight into Google Drive. And
[2:03] obviously, you can replace this example
[2:05] with almost anything you want. You could
[2:07] create a stock research agent, a
[2:09] competitor research agent, a job search
[2:11] agent, a travel search agent, a content
[2:14] idea agent, or even an agent that checks
[2:16] information from your connected apps and
[2:18] tells you what needs your attention. But
[2:21] for your first one, I would highly
[2:22] recommend choosing one very clear job
[2:25] instead of trying to build an agent that
[2:27] does [music] everything.
[2:32] So now I'm going to build this using
[2:34] Claude co-work. If you have used Claude
[2:35] before, you're probably familiar with
[2:37] normal chat where you have a back and
[2:39] forth conversation with Claude. Co-work
[2:41] is designed more around giving Claude
[2:44] larger tasks and letting it actually
[2:46] work through them for you. So open
[2:48] Claude, preferably on your desktop,
[2:50] switch from chat to co-work near the
[2:53] message box, and now we essentially have
[2:56] our workspace for building this agent.
[2:58] The first thing we need to do is explain
[3:00] the job clearly, and this is where
[3:02] people sometimes make agents
[3:03] unnecessarily complicated. You don't
[3:05] need to write some massive technical
[3:07] prompt, just describe what you want the
[3:09] finished result to look like. For
[3:11] example, I could say, "Research the five
[3:13] most important artificial intelligence
[3:15] stories from the last 24 hours.
[3:17] Prioritize major AI product launches,
[3:20] new AI models, important research, and
[3:24] significant announcements from companies
[3:26] like OpenAI, Anthropic, Google, Apple,
[3:30] Meta, and Microsoft. For each story,
[3:33] give me a short summary, explain why it
[3:35] matters, and include links to reliable
[3:38] original sources. Avoid duplicate
[3:40] stories and minor announcements. That's
[3:43] already enough to give Claude a very
[3:44] clear job. Did you notice that I mainly
[3:46] described the outcome? I'm not telling
[3:48] Claude, "First search the website, then
[3:51] open this website, compare these three
[3:53] articles, then create a document. Claude
[3:56] can figure out many of these
[3:57] intermediate steps itself. Now, we let
[4:00] Claude run the research. It has the
[4:02] goal, it understands the output I want,
[4:04] and it can work through the intermediate
[4:06] steps necessary to get there.
[4:11] >> [snorts]
[4:12] >> Before we move on, I want to quickly
[4:13] thank HubSpot for sponsoring this part
[4:15] of the video. If you enjoyed building
[4:17] this agent and you want to experiment
[4:20] with more advanced ones, HubSpot
[4:22] partnered with Futurepedia to create a
[4:24] completely free build your first AI
[4:26] agent course. And this is actually a
[4:29] really useful next step after what we
[4:31] just built. There are 18 hands-on videos
[4:34] where they walk you through building
[4:35] different AI agents using tools like
[4:38] N8N. And it's not just explaining what
[4:41] an AI agent is, you're actually building
[4:43] things. For example, you will learn how
[4:45] to connect an agent to Gmail, Google
[4:47] Calendar, and Google Sheets, build a
[4:50] personal assistant, create an agent that
[4:53] turns YouTube scripts into LinkedIn
[4:54] posts, and short-form scripts, and even
[4:57] build a customer support agent trained
[5:00] on a website. They also give you the
[5:01] actual system prompts and explain the
[5:04] really simple brain, memory, and tools
[5:06] frameworks that you can reuse when
[5:09] building your own agents. My favorite
[5:11] part is that it's very hands-on. You're
[5:13] not just learning the theory behind AI
[5:16] agents, you're actually building useful
[5:18] agents step-by-step and connecting them
[5:20] to tools that you already use like
[5:22] Gmail, Google Calendar, and Google
[5:24] Sheets. The whole course is free, so
[5:27] I'll leave the HubSpot link below if you
[5:29] want to check it out. Now, let's get
[5:31] back to the video.
[5:35] Once Claude finishes, look at the
[5:37] results. Your first version probably
[5:40] won't be perfect, and that's completely
[5:42] normal. You can improve the agent. I can
[5:45] say, "Keep each story under 100 words.
[5:48] I can revise further and customize it
[5:51] with all my requirements. Now, the agent
[5:54] becomes much more useful because it
[5:56] understands the actual workflow that I'm
[5:58] trying to accomplish. The next thing to
[6:00] understand is tools. Agents become much
[6:03] more powerful when they have access to
[6:05] tools, but again, this sounds more
[6:07] technical than it really is. A tool is
[6:10] simply something the AI is allowed to
[6:12] use. Web search is a tool. Google Drive
[6:15] can be a tool. Gmail can be a tool. Your
[6:18] calendar can be a tool. Different
[6:20] services and connectors can give an
[6:22] agent access to different information or
[6:24] actions. For example, if you connect
[6:27] Google Drive, you could create agent
[6:29] that works with information stored
[6:31] inside your drive, rather than requiring
[6:33] you to manually copy and paste
[6:35] everything into Claude. If you connect
[6:36] an email service, you could build
[6:38] workflows around finding messages that
[6:41] need your attention, summarizing certain
[6:43] emails, or helping you prepare
[6:45] responses. For our AI news agent,
[6:47] though, we honestly don't need many
[6:49] tools. Web research is enough, and I
[6:51] would actually recommend keeping your
[6:53] first agent this simple. Don't connect
[6:55] 10 different apps just because you can.
[6:57] The more access you give an agent, the
[6:59] more complicated the workflow becomes.
[7:01] Start by asking, what does this agent
[7:03] actually need to complete its job, and
[7:06] only give it those tools.
[7:11] At this point, our AI research agent
[7:13] already works, but there is one problem.
[7:16] I have to remember to come into Claude
[7:18] and ask it to do the research every
[7:20] morning. So, the final step is to
[7:22] automate that part. Inside Claude
[7:24] co-work, go to the schedule section, and
[7:27] create a new schedule task.
[7:29] I'm going to call mine daily AI news
[7:31] brief. Then, I can use essentially the
[7:34] same instructions we just tested, but
[7:37] I'm going to add one more thing. I've
[7:39] connected Google Drive, so I'll tell
[7:41] Claude, "Every morning, create this AI
[7:44] news brief and save the finished report
[7:46] to my daily AI news briefs folder in
[7:49] Google Drive with the date in the file
[7:51] name. Now, to run this task every day
[7:53] automatically, I can again simply say
[7:56] run this workflow every day morning at
[7:58] 8:00 a.m. automatically as a scheduled
[8:01] task. So, every day Claude can do the
[8:03] research automatically, create the
[8:05] report, and save a new dated copy
[8:08] directly into my Google Drive. I don't
[8:10] even have to remember to come back and
[8:12] run it myself.
[8:17] You might think couldn't I just paste
[8:19] this exact prompt into normal Claude
[8:21] every morning? Absolutely, you could.
[8:23] The difference is that then you're still
[8:25] responsible for starting and managing
[8:27] that process every single morning. Here,
[8:30] we have given Claude the goal. We have
[8:32] given it instructions about what a good
[8:34] result looks like. It can use tools like
[8:36] web research to gather the information.
[8:38] It can work through multiple steps to
[8:40] complete the task. And then, we have
[8:42] told it to repeat that task on a
[8:44] schedule. That's really the easiest
[8:45] mental model for an AI agent. It has a
[8:48] goal. It has instructions. It has tools.
[8:51] And it can work through multiple steps
[8:53] to complete the job. And if the task
[8:55] happens repeatedly, automation makes it
[8:57] even more useful.
[9:02] One thing to keep in mind before
[9:03] connecting everything, be careful on how
[9:06] much control you give an agent. There is
[9:08] a big difference between letting it
[9:10] research or summarize information and
[9:12] letting it edit files, send messages,
[9:15] delete data, or take actions inside your
[9:17] accounts. Start with low-risk tasks like
[9:20] research, planning, organization, and
[9:23] drafting. For anything that can make
[9:25] important changes or communicate on your
[9:27] behalf, keep a review step in place
[9:29] until you're confident the workflow is
[9:31] reliable. And that's really all you need
[9:33] to build your first AI agent. Let us
[9:35] know in the comments some of the
[9:37] interesting agents that you have built
[9:38] or going to build. I'll catch you in the
[9:40] next one. This is Sanjana. Bye-bye.
