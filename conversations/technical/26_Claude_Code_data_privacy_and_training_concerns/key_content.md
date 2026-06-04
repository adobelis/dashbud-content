# Key Content from: Claude Code data privacy and training concerns
Date: 2025-11-26
Total substantial assistant responses: 3

================================================================================
**User asked:** Does Claude Code train on my data? Will it steal my orchestration?...
**Response (msg #1, 2799 chars):**

The user is asking about Claude Code and whether it trains on their data, and specifically mentions concerns about it "stealing" their orchestration. This seems to be asking about data privacy and training policies.

I should search for the most up-to-date information about Claude Code's data usage and privacy policies. According to my instructions, when asked about Anthropic's products or product features, I should search for the most up-to-date information from Anthropic's documentation.

Let me search for information about Claude Code's data privacy and training policies.I'll search for the most current information about Claude Code's data privacy and training policies.
```
This block is not supported on your current device yet.
```

Good, I found detailed information about Claude Code's data usage and training policies. Let me summarize the key points:

1. For consumer accounts (Free, Pro, Max): Data can be used for training if users opt in. Users have control over this setting.
2. For commercial accounts (Team, Enterprise, API): Anthropic does not train models on this data.
3. There's a choice users can make about whether their data is used for training.
4. Data is de-identified before use.
5. Users can opt out at any time.

Let me provide a clear answer to the user's questions about whether Claude Code trains on their data and whether it will "steal their orchestration."Based on the official documentation, here's what you need to know about Claude Code and your data:

**For Consumer Accounts (Free, Pro, Max):**
You have full control over whether your chats and coding sessions are used to improve Claude models. You can opt in or out of this setting in your Privacy Settings at claude.ai/settings/data-privacy-controls. If you opt out:
- Your data is retained for only 30 days
- It won't be used for future model training

If you opt in:
- Data is retained for up to 5 years for model improvement purposes and is automatically de-linked from your user ID before use

**For Commercial Users (Team, Enterprise, API):**
Anthropic does not train generative models using code or prompts sent to Claude. Commercial accounts maintain much stricter privacy protections.

**Your orchestration won't be "stolen"** - data is used solely to make Claude better for everyone, not to contact people, build profiles, or sell information to third parties. The data goes through privacy-preserving filters and is de-identified.

**My recommendation:** If you're working with proprietary code or sensitive orchestration logic, either:
1. Opt out of model training in your settings, or
2. Use API authentication or a commercial account, which has different (stricter) data processing terms

Does this address your concerns? Would you like help checking or changing your privacy settings?

================================================================================
**User asked:** Ok. How do I add my project to Claude Code and set the settings to private -- "no training"...
**Response (msg #3, 2734 chars):**

The user wants to know two things:
1. How to add their project to Claude Code
2. How to set privacy settings to opt out of training

Let me search for specific instructions on how to use Claude Code with projects and how to configure the privacy settings.I'll search for instructions on how to add projects to Claude Code and configure the privacy settings.
```
This block is not supported on your current device yet.
```

Good, I have information about how to use Claude Code with projects. Now I need to search specifically for how to configure privacy settings to opt out of training.
```
This block is not supported on your current device yet.
```

Perfect! Now I have all the information I need to help the user:
1. How to add a project to Claude Code (navigate to the project directory and run `claude`)
2. How to set privacy settings to opt out of training (Settings > Privacy > Privacy Settings > toggle off "Help improve Claude")

Let me provide a clear, step-by-step guide for both.Perfect! Here's how to set up Claude Code with your project and configure privacy to opt out of training:

## **Adding Your Project to Claude Code**

1. **Install Claude Code** (if you haven't already):
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

2. **Navigate to your project directory**:
   ```bash
   cd /path/to/your/project
   ```

3. **Start Claude Code**:
   ```bash
   claude
   ```
   
   The first time you run it, you'll need to authenticate either through the Claude Console or with your Claude Pro/Max account.

4. **Claude Code automatically has access to your current directory**. You can also:
   - Add additional directories: `claude --add-dir /path/to/another/directory`
   - Or use the `/add-dir` command within an active Claude Code session

## **Setting Privacy to "No Training"**

Here's how to opt out of model training:

1. **Go to Claude.ai** and sign in
2. **Click your profile icon** (top right)
3. **Go to Settings > Privacy > Privacy Settings**
4. **Find "Help improve Claude"** toggle
5. **Turn it OFF** (toggle should be gray and to the left)

The change takes effect immediately and applies to all new chats and coding sessions. With this setting off:
- Your data is only retained for 30 days (instead of 5 years)
- Your code and conversations won't be used for future model training

## **Additional Privacy Tips**

- Use Incognito mode for extra-sensitive work - incognito chats are never used for training even if you have model improvement enabled
- Delete any sensitive chats you don't want retained
- Consider using API authentication for maximum privacy control (operates under different commercial terms)

Your orchestration and code will stay private with these settings configured!

================================================================================
**User asked:** can I NPM install locally (not -g)...
**Response (msg #5, 2692 chars):**

The user is asking if they can install Claude Code locally to their project instead of globally. This is a good question about npm installation options. Let me search for information about local installation of Claude Code.
```
This block is not supported on your current device yet.
```

The user is asking if they can install Claude Code locally to a project instead of globally. From the search results, I can see that Claude Code is designed to be installed globally (with -g flag) or using the native installer. I don't see any evidence that Claude Code supports local per-project installation like a typical npm package would.

Looking at the issues and documentation, all the installation methods refer to either:
1. Global npm installation (`npm install -g`)
2. Native binary installation (using the install script)

There's no mention of local project installation. The tool is designed to be a CLI that you run from anywhere, not a project dependency. This makes sense given that it's an interactive terminal tool that needs to work across multiple projects.

I should clarify this for the user and explain why Claude Code is different from typical npm packages.No, Claude Code is designed to be installed globally, not as a local project dependency. Here's why:

## **Why Claude Code Requires Global Installation**

Claude Code is a **CLI tool** (command-line interface) that's meant to work across all your projects, similar to tools like `git` or `npm` itself. It's not a library or package you import into your code.

**Installation options are:**

1. **Global npm install** (recommended by docs):
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

2. **Native binary installer** (newest method, doesn't require npm at all):
   ```bash
   # macOS/Linux/WSL
   curl -fsSL https://claude.ai/install.sh | bash
   
   # Windows PowerShell
   irm https://claude.ai/install.ps1 | iex
   ```

## **Why Not Local Installation?**

- Claude Code needs to be accessible from **any directory** on your system
- It's an interactive terminal tool, not a project dependency
- It maintains its own configuration in `~/.claude/` regardless of project location
- You want one installation that can work with multiple projects

## **How It Works With Your Project**

Once installed globally:
1. Navigate to any project directory: `cd /path/to/your/project`
2. Run: `claude`
3. Claude Code automatically has access to that directory's files

Think of it like Git - you install it once globally, then use it in any project folder you navigate to.

**Recommendation:** Use the native installer (option 2) as it's more reliable and doesn't depend on npm/Node.js being configured correctly.
