# Don't Give AI Your Data: How I (Actually) Use Claude Code for Data Analysis

**Channel:** Thu Vu  
**Views:** 142593  
**Published:** 2026-11-05 10:49:08 +00:00  
**URL:** https://www.youtube.com/watch?v=IPKOx66fogE

## Description

Try Claude Code yourself 👉 https://clau.de/ThuVu

🔖 Git repo for this demo 👉 https://github.com/thu-vu92/claude-code-data-analysis
📩  Get smarter in data & AI for 10 minutes a week 👉 https://thu-vu.ck.page/49c5ee08f6

🔑 TIMESTAMPS
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

00:00 Intro: Why uploading your data to AI is risky
00:41 The problem: Confidential data
01:30 The solution: Synthetic data proxy
02:51 Step 1: Create synthetic data locally (SDV)
05:02 Detecting metadata
06:27 Generating synthetic data
08:18 Pro tip: Data minimization
09:12 Step 2: Prompt Claude Code in the cloud
12:27 Step 3: Review the dashboard & Jupyter notebook
15:13 Step 4: Run code on real data
16:45 Outro

#dataanalysis #ai #python

## Transcript

[0:00] Thank you to Anthropic for sponsoring
[0:02] this video. If you're uploading your
[0:03] data set to AI tools, you are doing it
[0:06] wrong. Most tutorials tell you to upload
[0:09] your data or give an AI agent access to
[0:11] the local file, ask a few questions,
[0:14] generate some charts, and outcomes a
[0:15] fancy report. These demos look
[0:18] impressive, but they conveniently leave
[0:20] out one important question. Are you
[0:22] actually allowed to share that data? If
[0:24] you've worked in a real organization,
[0:26] you know useful data sets are often
[0:28] confidential. But the good news is you
[0:30] don't need to stop using AI systems
[0:33] either. In this video, I'll show you how
[0:35] I use cloud code to help analyze data
[0:38] without exposing the original data set.
[0:41] So, picture this. You are data analyst
[0:43] at a local boutique hotel. And one day,
[0:45] you handed a data set of guests. In this
[0:48] data set, you have every guest's email
[0:50] address, home or corporate building
[0:53] address, and full credit card number
[0:55] alongside with other information like
[0:57] the room types, nightly rates, and
[0:59] check-in checkout dates. And your job is
[1:01] to analyze the booking patterns, hotel
[1:03] customers, and revenue. So, how should
[1:05] you go about using AI on this data set
[1:08] without exposing any personal
[1:10] information of your hotel guest? You
[1:12] could of course use a local AI
[1:14] assistant, which I covered in some my
[1:16] previous videos, but that takes setup,
[1:18] decent hardware, and you're limited to
[1:20] the models your machine can actually
[1:22] run. Also, running Cloud Code or other
[1:24] AI agents in your terminal in your local
[1:27] computer. It still sends information,
[1:29] including your data, to the cloud to
[1:31] process your request. But here's the
[1:33] thing. If you're a data analyst or data
[1:35] scientist or a researcher, you don't
[1:37] actually need AI to analyze data for
[1:40] you. What you need is working analysis
[1:42] code that you can understand and inspect
[1:45] and check and run yourself. One simple
[1:47] solution that you could use is to create
[1:49] a synthetic data set. So on a local
[1:52] computer, we're going to generate a
[1:54] synthetic proxy of this original hotel
[1:57] data set. And you can think of it as a
[1:59] fake twin of your data set with the
[2:02] exact same columns, same data types,
[2:04] same structure as our real data, but
[2:07] with fake emails, fake credit card
[2:10] numbers, everything. And we'll share
[2:12] this data set to the AI tool like cloud
[2:14] code to generate all the code for our
[2:17] analysis. We'll ask cloud code to write
[2:19] and test all the code in the cloud
[2:22] against this synthetic data set. So
[2:24] cloud code have zero access to all the
[2:27] files locally on our computer. When it's
[2:30] done, you can either choose to download
[2:31] the code manually to your computer and
[2:34] run the code locally um on the real data
[2:37] set or if you're familiar with git and
[2:39] GitHub. You can also set up a private
[2:41] repo and connect it to your cloud code
[2:44] session. So you can actually push all
[2:46] the code to this repo and so you can
[2:48] pull the code back to your local
[2:50] computer and so you can collaborate with
[2:52] cloud code. Now, let me quickly walk you
[2:54] through how to actually create a
[2:56] synthetic proxy for your data set. So,
[2:59] I've created local project directory
[3:01] here on my computer. Inside the data
[3:03] folder, I have the real data set
[3:06] including all the guest data. And this
[3:08] data set includes in total 2,000 rows of
[3:12] customer records. Now, to be clear, this
[3:14] data set is actually fixures, but for
[3:16] the sake of this video, let's pretend
[3:18] that it's real. So now let me walk you
[3:20] through how to create a synthetic proxy
[3:22] for this data set. And I've prepared a
[3:25] Jupyter notebook over here and I'm going
[3:27] to share it in the GitHub repo linked in
[3:29] the description. We're going to use a
[3:31] Python package called SDV, synthetic
[3:34] data vault. It's one of the best
[3:36] libraries for creating tabular synthetic
[3:39] data. So as long as your data has a
[3:41] table structure, you can make use of
[3:44] this library. How it works is that it
[3:46] learns the statistical patterns in your
[3:48] data and generate realistic records that
[3:51] mimic those patterns. So now let's load
[3:54] this original data set that we have that
[3:56] is hotel guest data.csv. And we're going
[3:59] to use a CSV handler uh from this SDV
[4:03] package. And if you have any local
[4:04] database, you can also use specific
[4:07] handlers from SDV to connect to that
[4:10] database as well. So it's pretty neat.
[4:12] So here we're going to read the data
[4:14] from a folder uh named data that we have
[4:17] here and the file names of all the data
[4:20] files that we we want to import. So we
[4:23] can import multiple data sets. So if
[4:25] your data actually have three tables
[4:27] like hotel guest and hotel revenue or
[4:30] hotel locations, you can import those
[4:33] data as well. Just like what you would
[4:35] have in a database containing multiple
[4:37] tables connected to each other through
[4:40] certain keys. Here is the same concept
[4:42] and I'm going to call the output uh as
[4:46] real data and in this real data
[4:49] dictionary I have um the hotel guest
[4:52] data set and here I'm printing out 10
[4:54] first rows of this data set and you can
[4:57] see here these are the exact rows um
[5:00] with all the information of the hotel
[5:03] guest. Next before SDV can generate any
[5:06] synthetic data for us it needs something
[5:08] called meta data. If you're new to data
[5:10] analysis and wondering what is metadata?
[5:13] Now, simply put, it's a description of
[5:16] your data set like the blueprint of your
[5:19] table. So, instead of holding the actual
[5:21] guest records, metadata actually
[5:23] describes the names of your tables, the
[5:26] names of your columns in those tables,
[5:28] the data type in each column, like
[5:30] whether a column is an email, an
[5:32] address, a date, an email, or a
[5:35] category, and so on. If you have more
[5:37] than one table, it also describes how
[5:39] your tables actually connect. Now, if
[5:41] your data is stored in a proper
[5:43] database, you should have that meta data
[5:45] already. But here I'm having this data
[5:48] stored locally on the laptop. So, I'm
[5:50] actually have to create this meta data.
[5:53] And the good news is SDV can help us
[5:56] detect the metadata automatically. So,
[5:59] here I'm going to import this metadata
[6:02] class and we're going to create the meta
[6:04] data via auto detection. So here you can
[6:07] visualize the meta data that is
[6:10] automatically recognized. So here our
[6:13] data set has these columns and we have
[6:16] guest email as email, rewards as
[6:19] categorical, room type categorical,
[6:21] amenities fee numerical, check-in
[6:24] checkout date is daytime type. So that's
[6:27] correct. Room rate numerical correct.
[6:30] Let's now try to create the synthetic
[6:32] data set. We're going to use the Gshian
[6:34] copular synthesizer. If you want to read
[6:36] more about the synthesizers available in
[6:38] the SDV library, feel free to explore it
[6:41] in the docs. Then we're going to pass
[6:43] this metadata into this synthesizer. And
[6:46] next we'll fit this synthesizer on the
[6:49] real data that we have. And finally, we
[6:51] just need to sample um the number of
[6:54] rows that we want. For example, here I'm
[6:56] sampling 100 rows. So we have 100
[6:59] records in our synthetic data set. So
[7:01] let's go ahead and run this cell. And
[7:03] then we can just simply look at the um
[7:06] the synthetic data that we have just
[7:08] created. And as you can see this data
[7:10] set has exactly the same columns as what
[7:13] we had in our real data set. You can see
[7:16] that the billing address here. Just say
[7:18] something like SDV ID blah blah blah.
[7:21] It's not at all similar to what we have
[7:23] in our real data which is the actual
[7:26] address with the street numbers and the
[7:29] um postal code. Right? And this is
[7:31] because our metadata has it wrong. So
[7:34] here somehow it's identified as ID. So
[7:38] what we'll do is to update this
[7:40] metadata. So now I'm going to update
[7:42] this meta data set and also validate it
[7:45] to make sure that we have the correct
[7:48] type here specified and we're going to
[7:50] visualize the metadata again. And you
[7:52] can see that building address here has
[7:54] been updated to address data type. So
[7:57] that's great. And now let's go ahead and
[8:00] fit the data again. And let's take a
[8:03] look at the updated synthetic data. So
[8:06] you can see here the building address
[8:08] has been updated. And you can see that
[8:10] here there are some fake address here,
[8:12] right? Street numbers, city, and postal
[8:15] code. So it's very realistic and very
[8:17] usable for data analysis. And it's worth
[8:19] noting that even if this is a synthetic
[8:21] data set, none of those records are
[8:23] real. There's still potentially some
[8:25] sensitive information. For example,
[8:27] let's say the metadata, the column names
[8:30] are confidential or the types of room um
[8:33] is also confidential which is not but it
[8:36] can potentially be then you need to use
[8:38] some judgment here to say this is
[8:40] actually safe to share it on the
[8:42] internet. And also if your data set
[8:43] doesn't need all these columns for
[8:45] example you don't actually analyze guest
[8:48] email or building address or you don't
[8:51] actually care about the credit card
[8:53] number then just remove those irrelevant
[8:55] columns. The rule of thumb here is to
[8:57] use the minimum amount of data you need
[9:00] for your analysis questions, nothing
[9:02] more. So let's say now I'm happy with
[9:05] the synthetic data set. Then I'm going
[9:06] to save this as the hotel guest data
[9:09] synthetic. All right. Now we have it in
[9:12] our project. Let's now go to the fun
[9:14] part which is to do the analysis on this
[9:17] synthetic data with cloud code. Cloud
[9:20] code is a very smart coding agent and in
[9:22] this project is going to help us do the
[9:25] heavy lifting of creating a repeatable
[9:27] analysis workflow and all the code that
[9:30] you can use to run on your real data set
[9:32] locally and get the real data inside. I
[9:34] have my cloud desktop app here open and
[9:37] if you prefer to use a browser version
[9:39] you can do that as well. And here you
[9:40] can toggle between the chat and cloud
[9:43] code. And you can choose the environment
[9:45] here, whether to let cloud code work
[9:48] locally on this computer or you choose
[9:51] to have it run on the cloud. And this is
[9:54] the default option. For this project,
[9:56] I'm going to let cloud code run on the
[9:58] cloud because I don't want it to access
[10:00] my project folder including this uh
[10:03] sensitive data set that I have. So we
[10:06] are going to let it run completely on
[10:08] the cloud. And on this menu, you can
[10:09] choose different models. For example,
[10:11] here I'm using Opus 5.5, which is one of
[10:14] the best models for coding from
[10:16] Anthropic. And you can choose different
[10:19] effort level as well. Here I'm using
[10:21] medium. So now we're going to upload our
[10:24] synthetic data set to our cloud session.
[10:27] And make sure that we are choosing the
[10:29] synthetic data and not the real data.
[10:32] And this tiny synthetic data set will
[10:34] help give enough context for cloud to
[10:36] help us with the data analysis. So let's
[10:39] go ahead and attach this to our cloud
[10:42] session. And next we're going to say
[10:44] create a Jupyter notebook to explore
[10:47] this hotel guest data. Use pandas and
[10:52] plotly or any other package or library
[10:55] you prefer. Firstly, I want to know how
[10:57] many nights um our guests usually stay
[11:00] at our hotel. Secondly, I'm curious what
[11:03] are the most common um the most common
[11:08] email domains of of our guests. And as a
[11:12] small boutique hotel, you're leaning
[11:14] into customer loyalty. And so, you care
[11:17] a lot about loyal customers who actually
[11:19] stay frequently at your hotel. So I want
[11:22] to find out how many repeat individual
[11:24] customers we have and also how many high
[11:28] volume corporate offices we have as
[11:31] customers because a corporate office
[11:33] usually have a credit card that can be
[11:35] used by multiple employees for multiple
[11:37] states. So let's ask clot code to
[11:40] identify
[11:41] um how many regular uh individual
[11:45] household customers and how many high
[11:49] volume corporate office accounts we have
[11:53] in our data. So I'll stop here with the
[11:56] questions for now and I'm going to say
[11:59] add code comments to walk reader through
[12:02] mention or the got just and data warning
[12:06] because for some of these analysis we
[12:08] might come across data quality issues
[12:11] like missing values or invalid data. I
[12:13] want cloud code to write them down. And
[12:15] finally, I'm going to ask Cloudco to
[12:18] generate a um live dashboard for me to
[12:24] look at the result. All right, let's go
[12:25] ahead and hit enter.
[12:28] So, I just got some coffee while cloud
[12:30] code was working. And you can see that
[12:32] after a few minutes we uh are done with
[12:35] the analysis and clot code has created a
[12:37] dashboard for us with the information
[12:40] about the hotel guests together with the
[12:43] answers to all our analysis questions.
[12:46] For example, how many nights do guests
[12:48] stay? More than a half a check out
[12:50] before check-in. And this is because we
[12:52] are running it on the synthetic data
[12:54] set. And some of the checkout uh dates
[12:57] are actually before the checkin. Uh
[12:59] which doesn't make any sense, but it's
[13:00] just because this is synthetic data. Uh
[13:02] we also have the length of stay uh for
[13:05] all the valid bookings. And here we also
[13:08] have the common email domains. And for
[13:10] the third question, we have some
[13:12] insights about how many repeat bookings
[13:15] we have from one single billing address.
[13:18] So this is really great and it shows us
[13:20] some impression of how our analysis will
[13:23] eventually look like. So now let's take
[13:25] a look at the Jupyter notebook that
[13:27] Cloud Code has created. So here we have
[13:30] the analysis notebook already run with
[13:32] all outputs and charts included. So
[13:35] let's go ahead and download this one.
[13:38] Let's save it. and I'm going to move it
[13:40] into our analysis folder locally. So
[13:44] here we go. We have a self-contained
[13:46] Jupyter notebook that executes all the
[13:50] analysis for us. So here we have the
[13:52] load the data. We have data quality
[13:54] overview, checking for missing values
[13:57] per column, checking for numeric
[13:59] summary, checking for valid card
[14:02] numbers, etc. So this is a really great
[14:04] starting point. So without us having to
[14:06] actually tell plot code exactly what to
[14:09] do, what to check, it just did it for us
[14:12] using common sense based on all these
[14:14] columns. So this is really good. And
[14:16] then we have um the analysis per
[14:18] question. So how many nights do guests
[14:21] usually stay? We have the exact formula
[14:23] for how the nights are calculated based
[14:25] on the checkout and check-in date. We
[14:27] have different buckets for different
[14:29] scenarios. So this is really really
[14:31] cool. And so here's the overview of the
[14:34] stay status. We have some graph for the
[14:36] length of the stays. These graphs use
[14:39] plotly. So they are all interactive. Now
[14:41] all of this used to take me days to
[14:43] write and test and to get everything
[14:46] right. But now AI tools like plot code
[14:48] can really give you a very good starting
[14:50] point for your analysis without having
[14:52] to spend days. Of course, you have to
[14:54] read through everything in detail and
[14:57] check everything on the real data and
[14:59] see if everything still works and still
[15:01] makes sense, but hopefully you don't
[15:03] have to spend hours tinkering with some
[15:05] regular expressions or fixing your date
[15:07] columns. Oh, I hate dates. So, to run
[15:09] this notebook on our real data set, we
[15:12] are going to adjust the data path to
[15:15] point it to the actual real data set.
[15:18] So, hotel guest data. Now, let's run
[15:20] this. Let's save it and hopefully just
[15:24] run all and it should work. All right, I
[15:27] got some errors here. It says um we have
[15:31] some missing packages. So, meme type
[15:33] rendering requires NB format but it is
[15:36] not installed. So, we're missing some
[15:38] packages here. So, let's ask clot code
[15:40] to give us the requirements.txt file so
[15:43] we can install all the required
[15:45] packages. at least gave me a requirement
[15:48] file with the required packages to run
[15:53] this notebook. So if we download this
[15:55] requirements file, move it to our
[15:57] project, then we will be able to
[16:00] actually install these packages. So in
[16:04] this requirements file, we've got a few
[16:07] different libraries that are needed. So
[16:10] we are going to do pip install-r
[16:14] which is it stands for requirements
[16:17] requirements.txt.
[16:19] Now let's restart the kernel and try to
[16:22] run the notebook all again. And
[16:24] hopefully we don't have any error
[16:26] messages anymore. And as you can see we
[16:29] have loaded in here the real data set
[16:31] with 2,000 rows all the updated data
[16:34] quality check. And we can see that we
[16:36] have now more valid stays here. Um we
[16:39] have the updated median number of
[16:42] nights. We have guests by email domain
[16:44] and so on. So this is really great. AI
[16:47] is really changing the data analysis
[16:49] workflow. Coding tools like cloud code
[16:51] can really help you speed up some time
[16:53] consuming part of your workflow. For
[16:55] example, data cleaning or basic
[16:57] exploratory data analysis and
[16:59] visualization. And if you want to learn
[17:00] more about how AI is changing the data
[17:03] scientist workflow, check out this video
[17:05] over here and in the Git repo link in
[17:08] description below. You can get all the
[17:10] code and data that I use in this demo.
[17:12] Thank you for watching. Bye.
