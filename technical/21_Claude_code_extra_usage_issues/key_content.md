# Key Content from: Claude code extra_usage issues
Date: 2026-01-21
Total substantial assistant responses: 1

================================================================================
**User asked:** I'm having problems using claude code with extra_usage...
**Response (msg #1, 4219 chars):**

The user is asking about problems with "claude code" and "extra_usage". Let me break this down:

1. Claude Code is mentioned in my system prompt as "a command line tool for agentic coding" that "lets developers delegate coding tasks to Claude directly from their terminal."

2. "extra_usage" sounds like it might be a parameter or feature, but I'm not familiar with the specific details of how Claude Code works or what "extra_usage" refers to.

Since this is about a specific Anthropic product (Claude Code) and a specific feature or parameter that I may not have current information about, I should use web search to find the most up-to-date documentation. According to my instructions:

"If asked about Anthropic's products or product features Claude first tells the person it needs to search for the most up to date information. Then it uses web search to search Anthropic's documentation before providing an answer to the person."

I should search Anthropic's documentation at https://docs.claude.com to find information about Claude Code and this "extra_usage" parameter/feature.I'll search Anthropic's documentation to find the most current information about Claude Code and the `extra_usage` parameter.
```
This block is not supported on your current device yet.
```

The search results didn't specifically mention "extra_usage" as a parameter or feature. Let me search more specifically for this term.Let me search more specifically for information about `extra_usage`:
```
This block is not supported on your current device yet.
```

Perfect! Now I found it. From the search results, I can see that:

1. "extra_usage" is a feature available for paid Claude plans (Pro, Max 5x, Max 20x) and for Team/Enterprise plans
2. It allows users to continue using Claude and Claude Code after reaching their plan's usage limits
3. When enabled, you can continue working by paying at standard API rates
4. It can be enabled/disabled using the `/extra-usage` command in Claude Code
5. There's a GitHub issue (#12450) showing a bug where someone enabled `/extra-usage` but was still unable to switch to the Opus model

The user is having problems with this feature. Based on the GitHub issue, it seems there might be a known bug where enabling extra_usage doesn't immediately allow access to features it should enable (like using Opus on a Pro plan).

Let me provide helpful information about what extra_usage is and what common issues users face with it.Based on the documentation, `extra_usage` is a feature that allows you to continue using Claude Code after reaching your plan's usage limits by switching to pay-as-you-go API pricing. Here's what I found about common issues:

## What is Extra Usage?

Extra usage allows Pro, Max, Team, and Enterprise plan users to keep working with Claude Code when they hit their session limits, by paying standard API rates for additional usage.

## Common Problems & Solutions

**1. Enabling Extra Usage**
In Claude Code, you can enable it with:
```
/extra-usage
```

Then you'll need to:
- Add funds to your account
- Set up payment method if not already configured
- Optionally configure a monthly spending cap

**2. Known Bug with Model Switching**
There's a documented issue where enabling `/extra-usage` doesn't immediately allow switching to Opus model, with users receiving an error saying "Your Pro plan doesn't include Opus in Claude Code. Turn on /extra-usage or /upgrade to Max to access it" despite extra_usage being enabled.

**3. Common Issues:**
- **Authentication problems**: Make sure you're logged in with the correct account (`/login`)
- **API key conflicts**: If you have an `ANTHROPIC_API_KEY` environment variable set, Claude Code will use this API key instead of your subscription, resulting in API charges rather than using your subscription's included usage
- **Payment setup**: Ensure you've added funds after enabling extra usage

**4. Checking Status**
Use these commands to troubleshoot:
- `/status` - Check your current usage and limits
- `/cost` - View token usage for your session
- `claude doctor` - Verify your current version

Could you share more details about the specific error you're seeing? That would help me provide more targeted guidance.
