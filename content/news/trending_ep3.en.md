---
title: "2026/05/17 本週 GitHub AI 趨勢"
date: 2026-05-17
draft: false
tags: ["GitHub趨勢", "AI週報", "AI智能體", "LLM開發工具", "AI應用場景", "效率與成本優化"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---

This week, from the top 15 projects on GitHub Trending, **14** AI/LLM-related projects were selected:

---

## 1. [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser)

> [→ GitHub Link](https://github.com/CloakHQ/CloakBrowser)

CloakBrowser is a stealthy Chromium browser designed to evade bot detection. It achieves high anonymity through C++ source code-level fingerprint modification, rather than simple JavaScript injection or configuration adjustments. This project passes all 30 bot detection tests, allowing automated browsers to achieve a human score of up to 0.9 in ReCAPTCHA v3 and successfully bypass Cloudflare Turnstile. For the AI/LLM field, CloakBrowser solves the pain point where AI agents or automation frameworks (such as LangChain, Playwright) are blocked when performing web scraping, interaction, or automation tasks because they are detected as bots. Its "humanize=True" feature can further simulate human mouse movements, keyboard input, and scrolling patterns, making AI agents' behavior more natural and harder to detect. This provides a more stable and cost-effective infrastructure for AI-driven web automation, significantly improving task success rates and reliability, making it an indispensable tool for developing web agents.

---

## 2. [yikart/AiToEarn](https://github.com/yikart/AiToEarn)

> [→ GitHub Link](https://github.com/yikart/AiToEarn)

AiToEarn is a one-stop platform designed to help One Person Companies (OPC), creators, brands, and enterprises create, distribute, and monetize content on major global platforms through AI Agent automation. It addresses the huge time cost associated with content creation and multi-platform publishing, supporting over a dozen platforms like Douyin, Xiaohongshu, TikTok, and YouTube. In the AI/LLM domain, AiToEarn's value lies in demonstrating how AI Agents can integrate multimodal AI models (such as Grok, Veo, Nano Banana) to achieve end-to-end automation, from content ideation, video/image generation, translation, editing, to cross-platform publishing, and even interactive operations (e.g., AI intelligent comment replies). This not only greatly improves the efficiency of content production and promotion but also opens up new possibilities for AI applications in content marketing and commercial monetization, serving as a prime example of AI Agents empowering the creator economy.

---

## 3. [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

> [→ GitHub Link](https://github.com/rohitg00/agentmemory)

Agentmemory provides a powerful persistent memory system for AI coding agents, designed to solve the "forgetfulness" problem of existing AI assistants, allowing developers to no longer repeatedly explain project architecture, programming errors, or preference settings. It is based on the `iii engine`, combining traditional BM25 search, vector embeddings, and knowledge graphs, achieving a retrieval accuracy of up to 95.2% and significantly saving token costs. For the AI/LLM domain, Agentmemory is a critical infrastructure for building smarter, more autonomous AI agents. By automatically capturing every tool usage by the agent, compressing it into searchable memories, and injecting relevant context when needed, it greatly enhances the efficiency and continuity of coding agents, enabling them to exhibit human-like "learning" and "memory" capabilities in long-term complex software development tasks, making it a core component for improving AI coding assistants.

---

## 4. [anthropics/financial-services](https://github.com/anthropics/financial-services)

> [→ GitHub Link](https://github.com/anthropics/financial-services)

Anthropic's `financial-services` project provides a set of Claude reference agents, skills, and data connectors specifically designed for financial services workflows, covering areas such as investment banking, equity research, private equity, and wealth management. It aims to automate complex and specialized financial tasks through AI agents, such as bid preparation, market research, general ledger reconciliation, and financial statement review. In the AI/LLM domain, this project demonstrates how large language models can be applied in highly specialized and heavily regulated industries. Its design emphasizes the importance of "human oversight," indicating that AI plays an assistive role in high-risk decisions, providing analysis and drafts, with final confirmation still required from professionals. This not only showcases AI's strong potential in specific vertical sectors but also offers a valuable reference architecture and best practices for enterprises on how to securely integrate LLMs without sacrificing compliance and accuracy.

---

## 5. [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)

> [→ GitHub Link](https://github.com/bytedance/UI-TARS-desktop)

UI-TARS-desktop is a multimodal AI Agent stack launched by ByteDance, specifically its desktop application, which enables natural language control over local computers and browsers. It leverages state-of-the-art vision-language models (VLMs) and GUI agent technology, allowing AI to "understand" and operate graphical user interfaces to perform complex desktop and web tasks. For the AI/LLM domain, the highlight of this project is its breakthrough in the traditional limitation of AI Agents primarily interacting via text, giving AI a visual perception and operational capability closer to humans. Whether it's automatically booking flights, generating charts, or checking project issues on GitHub, UI-TARS demonstrates how multimodal AI can directly intervene in real-world operating environments, greatly expanding the application boundaries of AI automation and serving as an important step towards the vision of General AI Agents.

---

## 6. [decolua/9router](https://github.com/decolua/9router)

> [→ GitHub Link](https://github.com/decolua/9router)

9Router is an innovative AI routing and token saving tool designed to address the high costs, quota limits, and interruptions faced by AI coders when using multiple large language models (LLMs). It can connect various AI coding tools like Claude Code, Codex, and Cursor to over 40 LLM providers and more than 100 models, ensuring uninterrupted coding through an intelligent three-tier fallback mechanism (subscription -> cheaper -> free). Notably, its "RTK Token Saver" can automatically compress tool outputs, saving 20-40% of input tokens. In the AI/LLM domain, 9Router is an extremely practical tool. It not only lowers the economic barrier for AI development and improves development efficiency but also demonstrates how to effectively manage diverse LLM resources through intelligent routing and optimization strategies, achieving efficient and sustainable AI application development. For developers pursuing efficiency and cost-effectiveness, this is undoubtedly a boon.

---

## 7. [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

> [→ GitHub Link](https://github.com/Imbad0202/academic-research-skills)

Academic Research Skills is an academic research skill suite designed for Claude Code, covering the entire academic paper publication process from research, writing, reviewing, to revising and finalizing. It aims to make AI a "copilot" for researchers, automatically handling tedious "grunt work" like literature tracking, citation formatting, data validation, and logical consistency checks. In the AI/LLM domain, this project demonstrates how AI agents can be applied to highly specialized and knowledge-intensive academic work, with a particular emphasis on the importance of "human-AI collaboration." The project not only offers paper planning, writing assistance, and peer review agents but also delves into the structural limitations that AI might encounter in academic writing, such as "hallucinations," "frame locking," and "flattery," proposing corresponding solutions and integrity verification mechanisms. This sets a new benchmark for developing responsible and high-quality AI academic tools.

---

## 8. [oven-sh/bun](https://github.com/oven-sh/bun)

> [→ GitHub 連結](https://github.com/oven-sh/bun)

Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one      
 Bun  
          
  
  Documentation  
    •    
  Discord  
    •    
  Issues  
    •    
  Roadmap  
   
  
 Read the docs →  
 What is Bun?  
 Bun is an all-in-one toolkit for JavaScript and TypeScript apps. It ships as a single executable called  bun .  
 At its core is the  Bun runtime , a fast JavaScript runtime designed as  a drop-in replacement for Node.js . It's written in Zig and powered by JavaScriptCore under the hood, dramatically reducing startup times and memory usage.  
 `bun run index.tsx`             # TS and JSX supported out-of-the-box
  
 The  bun  command-line tool also implements a test runner, script runner, and Node.js-compatible package manager. Instead of 1,000 node_modules for development, you only need  bun . Bun's built-in tools are significantly faster than existing options and usable in existing Node.js projects with little to no changes.  
 `bun test`                      # run tests
`bun run start`                 # run the `start` script in `package.json`
`bun install <pkg>`             # install a package
`bunx cowsay 'Hello, world!'`   # execute a package
  
 Install  
 Bun supports Linux (x64 & arm64), macOS (x64 & Apple Silicon), and Windows (x64 & arm64).  
  
  Linux users  — Kernel version 5.6 or higher is strongly recommended, but the minimum is 5.1.  
  
  
  x64 users  — if you see "illegal instruction" or similar errors, check our  CPU requirements  
  
 ```bash
# with install script (recommended)
curl -fsSL https://bun.com/install | bash

# on windows
powershell -c "irm bun.sh/install.ps1 | iex"

# with npm
npm install -g bun

# with Homebrew
brew tap oven-sh/bun
brew install bun

# with Docker
docker pull oven/bun
docker run --rm --init --ulimit memlock=-1:-1 oven/bun
```
  
 Upgrade  
 To upgrade to the latest version of Bun, run:  
 `bun upgrade`
  
 Bun automatically releases a canary build on every commit to  main . To upgrade to the latest canary build, run:  
 `bun upgrade --canary`
  
 View canary build  
 Quick links  
  
    Intro  
    
    What is Bun?  
    Installation  
    Quickstart  
    TypeScript  
    TypeScript 6  
      
    Templating  
    
    bun init  
    bun create  
      
    Runtime  
    
    bun run  
    File types (Loaders)  
    JSX  
    Environment variables  
    Bun APIs  
    Web APIs  
    Node.js compatibility  
    Plugins  
    Watch mode / Hot Reloading  
    Module resolution  
    Auto-install  
    bunfig.toml  
    Debugger  
    REPL  
    $ Shell  
      
    Package manager  
    
    bun install  
    bun add  
    bun remove  
    bun update  
    bun link  
    bun pm  
    bun outdated  
    bun publish  
    bun patch  
    bun why  
    bun audit  
    bun info  
    Global cache  
    Global store  
    Isolated installs  
    Workspaces  
    Catalogs  
    Lifecycle scripts  
    Filter  
    Lockfile  
    Scopes and registries  
    Overrides and resolutions  
    Security scanner API  
    .npmrc  
      
    Bundler  
    
    Bun.build  
    Loaders  
    Plugins  
    Macros  
    vs esbuild  
    Single-file executable  
    CSS  
    HTML & static sites  
    Hot Module Replacement (HMR)  
    Full-stack with HTML imports  
    Standalone HTML  
    Bytecode caching  
    Minifier  
      
    Test runner  
    
    bun test  
    Writing tests  
    Lifecycle hooks  
    Mocks  
    Snapshots  
    Dates and times  
    DOM testing  
    Code coverage  
    Configuration  
    Discovery  
    Reporters  
    Runtime Behavior  
      
    Package runner  
    
    bunx  
      
    API  
    
    HTTP server ( Bun.serve )  
    HTTP routing  
    HTTP error handling  
    HTTP metrics  
    WebSockets  
    Workers  
    Binary data  
    Streams  
    File I/O ( Bun.file )  
    Archive (tar)  
    SQLite ( bun:sqlite )  
    PostgreSQL ( Bun.sql )  
    Redis ( Bun.redis )  
    S3 Client ( Bun.s3 )  
    FileSystemRouter  
    TCP sockets  
    UDP sockets  
    Globals  
    Child processes (spawn)  
    Cron ( Bun.cron )  
    WebView  
    Transpiler ( Bun.Transpiler )  
    Hashing  
    Colors ( Bun.color )  
    Console  
    FFI ( bun:ffi )  
    C Compiler ( bun:ffi  cc)  
    HTMLRewriter  
    Cookies ( Bun.Cookie )  
    CSRF ( Bun.CSRF )  
    Secrets ( Bun.secrets )  
    YAML ( Bun.YAML )  
    TOML ( Bun.TOML )  
    JSON5  
    JSONL  
    Markdown  
    Image processing  
    Utils  
    Node-API  
    Glob ( Bun.Glob )  
    Semver ( Bun.semver )  
    DNS  
    fetch API extensions  
      
  
 Guides  
  
    Deployment  
    
    Deploy to Vercel  
    Deploy to Railway  
    Deploy to Render  
    Deploy to AWS Lambda  
    Deploy to DigitalOcean  
    Deploy to Google Cloud Run  
      
    Binary  
    
    Convert a Blob to a string  
    Convert a Buffer to a blob  
    Convert a Blob to a DataView  
    Convert a Buffer to a string  
    Convert a Blob to a ReadableStream  
    Convert a Blob to a Uint8Array  
    Convert a DataView to a string  
    Convert a Uint8Array to a Blob  
    Convert a Blob to an ArrayBuffer  
    Convert an ArrayBuffer to a Blob  
    Convert a Buffer to a Uint8Array  
    Convert a Uint8Array to a Buffer  
    Convert a Uint8Array to a string  
    Convert a Buffer to an ArrayBuffer  
    Convert an ArrayBuffer to a Buffer  
    Convert an ArrayBuffer to a string  
    Convert a Uint8Array to a DataView  
    Convert a Buffer to a ReadableStream  
    Convert a Uint8Array to an ArrayBuffer  
    Convert an ArrayBuffer to a Uint8Array  
    Convert an ArrayBuffer to an array of numbers  
    Convert a Uint8Array to a ReadableStream  
      
    Ecosystem  
    
    Use React and JSX  
    Use Gel with Bun  
    Use Prisma with Bun  
    Use Prisma Postgres with Bun  
    Add Sentry to a Bun app  
    Create a Discord bot  
    Run Bun as a daemon with PM2  
    Use Drizzle ORM with Bun  
    Use Upstash Redis with Bun  
    Build an app with Nuxt and Bun  
    Build an app with Qwik and Bun  
    Build an app with Astro and Bun  
    Build an app with Remix and Bun  
    Build a frontend using Vite and Bun  
    Build an app with Next.js and Bun  
    Run Bun as a daemon with systemd  
    Build an HTTP server using Hono and Bun  
    Build an app with SvelteKit and Bun  
    Build an app with SolidStart and Bun  
    Build an app with TanStack Start and Bun  
    Build an HTTP server using Elysia and Bun  
    Build an HTTP server using StricJS and Bun  
    Containerize a Bun application with Docker  
    Build an HTTP server using Express and Bun  
    Use Neon Postgres through Drizzle ORM  
    Server-side render (SSR) a React component  
    Read and write data to MongoDB using Mongoose and Bun  
    Use Neon's Serverless Postgres with Bun  
      
    HTMLRewriter  
    
    Extract links from a webpage using HTMLRewriter  
    Extract social share images and Open Graph tags  
      
    HTTP  
    
    Hot reload an HTTP server  
    Common HTTP server usage  
    Write a simple HTTP server  
    Configure TLS on an HTTP server  
    Send an HTTP request using fetch  
    Proxy HTTP requests using fetch()  
    Start a cluster of HTTP servers  
    Stream a file as an HTTP Response  
    fetch with unix domain sockets in Bun  
    Upload files via HTTP using FormData  
    Streaming HTTP Server with Async Iterators  
    Streaming HTTP Server with Node.js Streams  
    Server-Sent Events (SSE) with Bun  
      
    Install  
    
    Add a dependency  
    Add a Git dependency  
    Add a peer dependency  
    Add a trusted dependency  
    Add a development dependency  
    Add a tarball dependency  
    Add an optional dependency  
    Generate a yarn-compatible lockfile  
    Configuring a monorepo using workspaces  
    Install a package under a different name  
    Install dependencies with Bun in GitHub Actions  
    Using bun install with Artifactory  
    Configure git to diff Bun's lockb lockfile  
    Override the default npm registry for bun install  
    Using bun install with an Azure Artifacts npm registry  
    Migrate from npm install to bun install  
    Configure a private registry for an organization scope with bun install  
      
    Process  
    
    Read from stdin  
    Listen for CTRL+C  
    Spawn a child process  
    Listen to OS signals  
    Parse command-line arguments  
    Read stderr from a child process  
    Read stdout from a child process  
    Get the process uptime in nanoseconds  
    Spawn a child process and communicate using IPC  
      
    Read file  
    
    Read a JSON file  
    Check if a file exists  
    Read a file as a string  
    Read a file to a Buffer  
    Get the MIME type of a file  
    Watch a directory for changes  
    Read a file as a ReadableStream  
    Read a file to a Uint8Array  
    Read a file to an ArrayBuffer  
      
    Runtime  
    
    Delete files  
    Run a Shell Command  
    Import a JSON file  
    Import a TOML file  
    Import a YAML file  
    Import a JSON5 file  
    Set a time zone in Bun  
    Set environment variables  
    Re-map import paths  
    Delete directories  
    Read environment variables  
    Import a HTML file as text  
    Install and run Bun in GitHub Actions  
    Debugging Bun with the web debugger  
    Install TypeScript declarations for Bun  
    Debugging Bun with the VS Code extension  
    Inspect memory usage using V8 heap snapshots  
    Define and replace static globals & constants  
    Build-time constants with --define  
    Codesign a single-file JavaScript executable on macOS  
      
    Streams  
    
    Convert a ReadableStream to JSON  
    Convert a ReadableStream to a Blob  
    Convert a ReadableStream to a Buffer  
    Convert a ReadableStream to a string  
    Convert a ReadableStream to a Uint8Array  
    Convert a ReadableStream to an array of chunks  
    Convert a Node.js Readable to JSON  
    Convert a Node.js Readable to a Blob  
    Convert a Node.js Readable to a string  
    Convert a Node.js Readable to an Uint8Array  
    Convert a Node.js Readable to an ArrayBuffer  
      
    Test  
    
    Spy on methods in  bun test  
    Bail early with the Bun test runner  
    Mock functions in  bun test  
    Run tests in watch mode with Bun  
    Use snapshot testing in  bun test  
    Skip tests with the Bun test runner  
    Using Testing Library with Bun  
    Update snapshots in  bun test  
    Run your tests with the Bun test runner  
    Set the system time in Bun's test runner  
    Set a per-test timeout with the Bun test runner  
    Migrate from Jest to Bun's test runner  
    Write browser DOM tests with Bun and happy-dom  
    Mark a test as a "todo" with the Bun test runner  
    Re-run tests multiple times with the Bun test runner  
    Generate code coverage reports with the Bun test runner  
    import, require, and test Svelte components with bun test  
    Set a code coverage threshold with the Bun test runner  
    Selectively run tests concurrently with glob patterns  
      
    Util  
    
    Generate a UUID  
    Hash a password  
    Escape an HTML string  
    Get the current Bun version  
    Upgrade Bun to the latest version  
    Encode and decode base64 strings  
    Compress and decompress data with gzip  
    Sleep for a fixed number of milliseconds  
    Detect when code is executed with Bun  
    Check if two objects are deeply equal  
    Compress and decompress data with DEFLATE  
    Get the absolute path to the current entrypoint  
    Get the directory of the current file  
    Check if the current file is the entrypoint  
    Get the file name of the current file  
    Convert a file URL to an absolute path  
    Convert an absolute path to a file URL  
    Get the absolute path of the current file  
    Get the path to an executable bin file  
      
    WebSocket  
    
    Build a publish-subscribe WebSocket server  
    Build a simple WebSocket server  
    Enable compression for WebSocket messages  
    Set per-socket contextual data on a WebSocket  
      
    Write file  
    
    Delete a file  
    Write to stdout  
    Write a file to stdout  
    Write a Blob to a file  
    Write a string to a file  
    Append content to a file  
    Write a file incrementally  
    Write a Response to a file  
    Copy a file to another location  
    Write a ReadableStream to a file  
      
  
 Contributing  
 Refer to the  Project > Contributing  guide to start contributing to Bun.  
 License  
 Refer to the  Project > License  page for information about Bun's licensing.

---

## 9. [mattpocock/skills](https://github.com/mattpocock/skills)

> [→ GitHub 連結](https://github.com/mattpocock/skills)

Skills for Real Engineers. Straight from my .claude directory.    
   
     
     
     
       
 Skills For Real Engineers  
  
 My agent skills that I use every day to do real engineering - not vibe coding.  
 Developing real applications is hard. Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.  
 These skills are designed to be small, easy to adapt, and composable. They work with any model. They're based on decades of engineering experience. Hack around with them. Make them your own. Enjoy.  
 If you want to keep up with changes to these skills, and any new ones I create, you can join ~60,000 other devs on my newsletter:  
 Sign Up To The Newsletter  
 Quickstart (30-second setup)  
  
  Run the  `skills.sh`  installer:  
  
 ```bash
npx skills@latest add mattpocock/skills
```
  
    Pick the skills you want, and which coding agents you want to install them on.  Make sure you select  `/setup-matt-pocock-skills` .    
    Run  `/setup-matt-pocock-skills`  in your agent. It will:  
    
    Ask you which issue tracker you want to use (GitHub, Linear, or local files)  
    Ask you what labels you apply to ticks when you triage them ( `/triage`  uses labels)  
    Ask you where you want to save any docs we create  
      
    Bam - you're ready to go.    
  
 Why These Skills Exist  
 I built these skills as a way to fix common failure modes I see with Claude Code, Codex, and other coding agents.  
 #1: The Agent Didn't Do What I Want  
  
  "No-one knows exactly what they want"  
  David Thomas & Andrew Hunt,  The Pragmatic Programmer  
  
 The Problem . The most common failure mode in software development is misalignment. You think the dev knows what you want. Then you see what they've built - and you realize it didn't understand you at all.  
 This is just the same in the AI age. There is a communication gap between you and the agent. The fix for this is a  grilling session  - getting the agent to ask you detailed questions about what you're building.  
 The Fix  is to use:  
  
  `/grill-me`  - for non-code uses  
  `/grill-with-docs`  - same as  `/grill-me` , but adds more goodies (see below)  
  
 These are my most popular skills. They help you align with the agent before you get started, and think deeply about the change you're making. Use them  every  time you want to make a change.  
 #2: The Agent Is Way Too Verbose  
  
  With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.  
  Eric Evans,  Domain-Driven-Design  
  
 The Problem : At the start of a project, devs and the people they're building the software for (the domain experts) are usually speaking different languages.  
 I felt the same tension with my agents. Agents are usually dropped into a project and asked to figure out the jargon as they go. So they use 20 words where 1 will do.  
 The Fix  for this is a shared language. It's a document that helps agents decode the jargon used in the project.  
  
  Example  
  Here's an example  `CONTEXT.md` , from my  `course-video-manager`  repo. Which one is easier to read?  
   
   BEFORE : "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"  
   AFTER : "There's a problem with the materialization cascade"  
   
  This concision pays off session after session.  
  
 This is built into  `/grill-with-docs` . It's a grilling session, but that helps you build a shared language with the AI, and document hard-to-explain decisions in ADR's.  
 It's hard to explain how powerful this is. It might be the single coolest technique in this repo. Try it, and see.  
 
  
   
    
   Tip 
  A shared language has many other benefits than reducing verbosity:  
   
   Variables, functions and files are named consistently , using the shared language  
   As a result, the  codebase is easier to navigate  for the agent  
   The agent also  spends fewer tokens on thinking , because it has access to a more concise language  
   
  
 #3: The Code Doesn't Work  
  
  "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that’s too big."  
  David Thomas & Andrew Hunt,  The Pragmatic Programmer  
  
 The Problem : Let's say that you and the agent are aligned on what to build. What happens when the agent  still  produces crap?  
 It's time to look at your feedback loops. Without feedback on how the code it produces actually runs, the agent will be flying blind.  
 The Fix : You need the usual tranche of feedback loops: static types, browser access, and automated tests.  
 For automated tests, a red-green-refactor loop is critical. This is where the agent writes a failing test first, then fixes the test. This helps give the agent a consistent level of feedback that results in far better code.  
 I've built a  `/tdd`  skill  you can slot into any project. It encourages red-green-refactor and gives the agent plenty of guidance on what makes good and bad tests.  
 For debugging, I've also built a  `/diagnose`  skill that wraps best debugging practices into a simple loop.  
 #4: We Built A Ball Of Mud  
  
  "Invest in the design of the system  every day ."  
  Kent Beck,  Extreme Programming Explained  
  
  
  "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."  
  John Ousterhout,  A Philosophy Of Software Design  
  
 The Problem : Most apps built with agents are complex and hard to change. Because agents can radically speed up coding, they also accelerate software entropy. Codebases get more complex at an unprecedented rate.  
 The Fix  for this is a radical new approach to AI-powered development: caring about the design of the code.  
 This is built in to every layer of these skills:  
  
  `/to-prd`  quizzes you about which modules you're touching before creating a PRD  
  `/zoom-out`  tells the agent to explain code in the context of the whole system  
  
 And crucially,  `/improve-codebase-architecture`  helps you rescue a codebase that has become a ball of mud. I recommend running it on your codebase once every few days.  
 Summary  
 Software engineering fundamentals matter more than ever. These skills are my best effort at condensing these fundamentals into repeatable practices, to help you ship the best apps of your career. Enjoy.  
 Reference  
 Engineering  
 Skills I use daily for code work.  
  
  `diagnose`  — Disciplined diagnosis loop for hard bugs and performance regressions: reproduce → minimise → hypothesise → instrument → fix → regression-test.  
  `grill-with-docs`  — Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates  `CONTEXT.md`  and ADRs inline.  
  `triage`  — Triage issues through a state machine of triage roles.  
  `improve-codebase-architecture`  — Find deepening opportunities in a codebase, informed by the domain language in  `CONTEXT.md`  and the decisions in  `docs/adr/` .  
  `setup-matt-pocock-skills`  — Scaffold the per-repo config (issue tracker, triage label vocabulary, domain doc layout) that the other engineering skills consume. Run once per repo before using  `to-issues` ,  `to-prd` ,  `triage` ,  `diagnose` ,  `tdd` ,  `improve-codebase-architecture` , or  `zoom-out` .  
  `tdd`  — Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.  
  `to-issues`  — Break any plan, spec, or PRD into independently-grabbable GitHub issues using vertical slices.  
  `to-prd`  — Turn the current conversation context into a PRD and submit it as a GitHub issue. No interview — just synthesizes what you've already discussed.  
  `zoom-out`  — Tell the agent to zoom out and give broader context or a higher-level perspective on an unfamiliar section of code.  
  `prototype`  — Build a throwaway prototype to flesh out a design — either a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route.  
  
 Productivity  
 General workflow tools, not code-specific.  
  
  `caveman`  — Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler while keeping full technical accuracy.  
  `grill-me`  — Get relentlessly interviewed about a plan or design until every branch of the decision tree is resolved.  
  `handoff`  — Compact the current conversation into a handoff document so another agent can continue the work.  
  `write-a-skill`  — Create new skills with proper structure, progressive disclosure, and bundled resources.  
  
 Misc  
 Tools I keep around but rarely use.  
  
  `git-guardrails-claude-code`  — Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, etc.) before they execute.  
  `migrate-to-shoehorn`  — Migrate test files from  `as`  type assertions to @total-typescript/shoehorn.  
  `scaffold-exercises`  — Create exercise directory structures with sections, problems, solutions, and explainers.  
  `setup-pre-commit`  — Set up Husky pre-commit hooks with lint-staged, Prettier, type checking, and tests.

---

## 10. [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI)

> [→ GitHub Link](https://github.com/Hmbown/DeepSeek-TUI)

DeepSeek-TUI is a DeepSeek model coding agent that runs in the terminal, offering an interactive coding experience in a TUI (Text User Interface) format and supporting models such as DeepSeek V4 Pro/Flash. The project's highlight is its "thought process streaming" feature, which displays the model's workflow in real-time, along with various toolkits (file operations, Shell execution, Git, web search) and sub-agents working collaboratively. For AI/LLM developers, DeepSeek-TUI provides a transparent and efficient AI coding interface, allowing users to precisely control AI's behavior, for example, by automatically selecting models and thought levels via "Auto Mode," or ensuring safe editing through the "workspace rollback" feature. This not only enhances the practicality of AI-assisted coding but also offers an excellent platform for developers to deeply understand and fine-tune large models in real-world applications.

---

## 11. [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader)

> [→ GitHub Link](https://github.com/HKUDS/AI-Trader)

AI-Trader is an "agent-native" fully automated trading platform that allows AI agents to exchange trading strategies, learn, and execute trades in financial markets. It supports major markets such as stocks, cryptocurrencies, forex, options, and futures, and provides features like real-time market data, signal publication, collective intelligence trading, and one-click copy trading. In the AI/LLM domain, the launch of AI-Trader holds epoch-making significance. It is not only a direct application of AI Agents in the high-risk, high-reward financial sector but also, through its "collective intelligence trading" model, allows multiple AI agents to work collaboratively to explore optimal strategies. This project demonstrates how AI can achieve highly autonomous operations and transform complex financial decision-making processes into tasks understandable and executable by agents, providing a forward-looking technological foundation for future intelligent finance and automated investment, as well as a new avenue for human traders to understand and leverage AI trading capabilities.

---

## 12. [ruvnet/RuView](https://github.com/ruvnet/RuView)

> [→ GitHub 連結](https://github.com/ruvnet/RuView)

π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all without a single pixel of video. π RuView  
          
  
  Beta Software  — Under active development. APIs and firmware may change. Known limitations:  
   
   ESP32-C3 and original ESP32 are not supported (single-core, insufficient for CSI DSP)  
   Single ESP32 deployments have limited spatial resolution — use 2+ nodes or add a  Cognitum Seed  for best results  
   Camera-free pose accuracy is limited (PCK@20 ≈ 2.5% with proxy labels) —  camera ground-truth training  targets  35%+ PCK@20 ; the pipeline is implemented, but the data-collection and evaluation phases (ADR-079 P7–P9) are still pending, so no measured camera-supervised PCK@20 has been published yet  
   
  Contributions and bug reports welcome at  Issues .  
  
 See through walls with WiFi  
 Turn ordinary WiFi into a spatial intelligence / sensing system.  Detect people, measure breathing and heart rate, track movement, and monitor rooms — through walls, in the dark, with no cameras or wearables. Just physics.  
 π RuView is a WiFi sensing platform that turns radio signals into spatial intelligence.  
 Every WiFi router already fills your space with radio waves. When people move, breathe, or even sit still, they disturb those waves in measurable ways. RuView captures these disturbances using Channel State Information (CSI) from low-cost ESP32 sensors and turns them into actionable data: who's there, what they're doing, and whether they're okay.  
 What it senses:  
  
  Presence and occupancy  — detect people through walls, count them, track entries and exits  
  Vital signs  — breathing rate and heart rate, contactless, while sleeping or sitting  
  Activity recognition  — walking, sitting, gestures, falls — from temporal CSI patterns  
  Environment mapping  — RF fingerprinting identifies rooms, detects moved furniture, spots new objects  
  Sleep quality  — overnight monitoring with sleep stage classification and apnea screening  
  
 Built on  RuVector  and  Cognitum Seed , RuView runs entirely on edge hardware — an ESP32 mesh (as low as $9 per node) paired with a Cognitum Seed for persistent memory, cryptographic attestation, and AI integration. No cloud, no cameras, no internet required.  
 The system learns each environment locally using spiking neural networks that adapt in under 30 seconds, with multi-frequency mesh scanning across 6 WiFi channels that uses your neighbors' routers as free radar illuminators. Every measurement is cryptographically attested via an Ed25519 witness chain.  
 RuView also supports pose estimation (17 COCO keypoints via the WiFlow architecture), trained entirely without cameras using 10 sensor signals — a technique pioneered from the original  DensePose From WiFi  research at Carnegie Mellon University.  
 Built for low-power edge applications  
 Edge modules  are small programs that run directly on the ESP32 sensor — no internet needed, no cloud fees, instant response.  
              
  
   
    
     
     What  
     How  
     Speed  
     
    
    
     
     🦴  Pose estimation  
     CSI subcarrier amplitude/phase → 17 COCO keypoints  
     171K emb/s (M4 Pro)  
     
     
     🫁  Breathing detection  
     Bandpass 0.1-0.5 Hz → zero-crossing BPM  
     6-30 BPM  
     
     
     💓  Heart rate  
     Bandpass 0.8-2.0 Hz → zero-crossing BPM  
     40-120 BPM  
     
     
     👤  Presence sensing  
     Trained model + PIR fusion — 100% accuracy  
     0.012 ms latency  
     
     
     🧱  Through-wall  
     Fresnel zone geometry + multipath modeling  
     Up to 5m depth  
     
     
     🧠  Edge intelligence  
     8-dim feature vectors + RVF store on Cognitum Seed  
     $140 total BOM  
     
     
     🎯  Camera-free training  
     10 sensor signals, no labels needed  
     84s on M4 Pro  
     
     
     📷  Camera-supervised training  
     MediaPipe + ESP32 CSI →  35%+ PCK@20 target  (ADR-079; eval phases pending)  
     ~19 min on laptop (pipeline)  
     
     
     📡  Multi-frequency mesh  
     Channel hopping across 6 bands, neighbor APs as illuminators  
     3x sensing bandwidth  
     
     
     🌐  3D point cloud   (optional fusion)  
     Camera depth (MiDaS) + WiFi CSI + mmWave radar → unified spatial model  
     22 ms pipeline · 19K+ points/frame  
     
    
   
  
 # Option 1: Docker (simulated data, no hardware needed)
```bash
docker pull ruvnet/wifi-densepose:latest
docker run -p 3000:3000 ruvnet/wifi-densepose:latest
# Open http://localhost:3000
```

# Option 2: Live sensing with ESP32-S3 hardware ($9)
# Flash firmware, provision WiFi, and start sensing:
```bash
python -m esptool --chip esp32s3 --port COM9 --baud 460800 \
  write_flash 0x0 bootloader.bin 0x8000 partition-table.bin \
  0xf000 ota_data_initial.bin 0x20000 esp32-csi-node.bin
python firmware/esp32-csi-node/provision.py --port COM9 \
  --ssid "YourWiFi" --password "secret" --target-ip 192.168.1.20
```

# Option 3: Full system with Cognitum Seed ($140)
# ESP32 streams CSI → bridge forwards to Seed for persistent storage + kNN + witness chain
```bash
node scripts/rf-scan.js --port 5006           # Live RF room scan
node scripts/snn-csi-processor.js --port 5006  # SNN real-time learning
node scripts/mincut-person-counter.js --port 5006  # Correct person counting
```
  
 
  
   
    
   Note 
  CSI-capable hardware recommended.  Presence, vital signs, through-wall sensing, and all advanced capabilities require Channel State Information (CSI) from an ESP32-S3 ($9) or research NIC. The Docker image runs with simulated data for evaluation. Consumer WiFi laptops provide RSSI-only presence detection.  
  
  
  Hardware options  for live CSI capture:  
   
    
     
     Option  
     Hardware  
     Cost  
     Full CSI  
     Capabilities  
     
    
    
     
     ESP32 + Cognitum Seed  (recommended)  
     ESP32-S3 +  Cognitum Seed  
     ~$140  
     Yes  
     Pose, breathing, heartbeat, motion, presence + persistent vector store, kNN search, witness chain, MCP proxy  
     
     
     ESP32 Mesh  
     3-6x ESP32-S3 + WiFi router  
     ~$54  
     Yes  
     Pose, breathing, heartbeat, motion, presence  
     
     
     Research NIC  
     Intel 5300 / Atheros AR9580  
     ~$50-100  
     Yes  
     Full CSI with 3x3 MIMO  
     
     
     Any WiFi  
     Windows, macOS, or Linux laptop  
     $0  
     No  
     RSSI-only: coarse presence and motion  
     
    
   
  No hardware? Verify the signal processing pipeline with the deterministic reference signal:  `python archive/v1/data/proof/verify.py`  
  
  
      
  
 Real-time pose skeleton from WiFi CSI signals — no cameras, no wearables  
 
  
 ▶ Live Observatory Demo   |  
 ▶ Dual-Modal Pose Fusion Demo   |  
 ▶ Live 3D Point Cloud  
  
  The  server  is optional for visualization and aggregation — the ESP32  runs independently  for presence detection, vital signs, and fall alerts.  
  Live ESP32 pipeline : Connect an ESP32-S3 node → run the  sensing server  → open the  pose fusion demo  for real-time dual-modal pose estimation (webcam + WiFi CSI). See  ADR-059 .  
  
 🔬 How It Works  
 WiFi routers flood every room with radio waves. When a person moves — or even breathes — those waves scatter differently. WiFi DensePose reads that scattering pattern and reconstructs what happened:  
 `WiFi Router → radio waves pass through room → hit human body → scatter`
    `↓`
`ESP32 mesh (4-6 nodes) captures CSI on channels 1/6/11 via TDM protocol`
    `↓`
`Multi-Band Fusion: 3 channels × 56 subcarriers = 168 virtual subcarriers per link`
    `↓`
`Multistatic Fusion: N×(N-1) links → attention-weighted cross-viewpoint embedding`
    `↓`
`Coherence Gate: accept/reject measurements → stable for days without tuning`
    `↓`
`Signal Processing: Hampel, SpotFi, Fresnel, BVP, spectrogram → clean features`
    `↓`
`AI Backbone (RuVector): attention, graph algorithms, compression, field model`
    `↓`
`Signal-Line Protocol (CRV): 6-stage gestalt → sensory → topology → coherence → search → model`
    `↓`
`Neural Network: processed signals → 17 body keypoints + vital signs + room model`
    `↓`
`Output: real-time pose, breathing, heart rate, room fingerprint, drift alerts`
  
 No training cameras required — the  Self-Learning system (ADR-024)  bootstraps from raw WiFi data alone.  MERIDIAN (ADR-027)  ensures the model works in any room, not just the one it trained in.  
  
 🏢 Use Cases & Applications  
 WiFi sensing works anywhere WiFi exists. No new hardware in most cases — just software on existing access points or a $8 ESP32 add-on. Because there are no cameras, deployments avoid privacy regulations (GDPR video, HIPAA imaging) by design.  
 Scaling:  Each AP distinguishes ~3-5 people (56 subcarriers). Multi-AP multiplies linearly — a 4-AP retail mesh covers ~15-20 occupants. No hard software limit; the practical ceiling is signal physics.  
  
   
    
    Why WiFi sensing wins  
    Traditional alternative  
    
   
   
    
    🔒  
    No video, no GDPR/HIPAA imaging rules  
    Cameras require consent, signage, data retention policies  
    
    
    🧱  
    Works through walls, shelving, debris  
    Cameras need line-of-sight per room  
    
    
    🌙  
    Works in total darkness  
    Cameras need IR or visible light  
    
    
    💰  
    $0-$8 per zone  (existing WiFi or ESP32)  
    Camera systems: $200-$2,000 per zone  
    
    
    🔌  
    WiFi already deployed everywhere  
    PIR/radar sensors require new wiring per room  
    
   
  
  
  🏥 Everyday  — Healthcare, retail, office, hospitality (commodity WiFi) 
   
    
     
     Use Case  
     What It Does  
     Hardware  
     Key Metric  
     Edge Module  
     
    
    
     
     Elderly care / assisted living  
     Fall detection, nighttime activity monitoring, breathing rate during sleep — no wearable compliance needed  
     1 ESP32-S3 per room ($8)  
     Fall alert <2s  
     Sleep Apnea ,  Gait Analysis  
     
     
     Hospital patient monitoring  
     Continuous breathing + heart rate for non-critical beds without wired sensors; nurse alert on anomaly  
     1-2 APs per ward  
     Breathing: 6-30 BPM  
     Respiratory Distress ,  Cardiac Arrhythmia  
     
     
     Emergency room triage  
     Automated occupancy count + wait-time estimation; detect patient distress (abnormal breathing) in waiting areas  
     Existing hospital WiFi  
     Occupancy accuracy >95%  
     Queue Length ,  Panic Motion  
     
     
     Retail occupancy & flow  
     Real-time foot traffic, dwell time by zone, queue length — no cameras, no opt-in, GDPR-friendly  
     Existing store WiFi + 1 ESP32  
     Dwell resolution ~1m  
     Customer Flow ,  Dwell Heatmap  
     
     
     Office space utilization  
     Which desks/rooms are actually occupied, meeting room no-shows, HVAC optimization based on real presence  
     Existing enterprise WiFi  
     Presence latency <1s  
     Meeting Room ,  HVAC Presence  
     
     
     Hotel & hospitality  
     Room occupancy without door sensors, minibar/bathroom usage patterns, energy savings on empty rooms  
     Existing hotel WiFi  
     15-30% HVAC savings  
     Energy Audit ,  Lighting Zones  
     
     
     Restaurants & food service  
     Table turnover tracking, kitchen staff presence, restroom occupancy displays — no cameras in dining areas  
     Existing WiFi  
     Queue wait ±30s  
     Table Turnover ,  Queue Length  
     
     
     Parking garages  
     Pedestrian presence in stairwells and elevators where cameras have blind spots; security alert if someone lingers  
     Existing WiFi  
     Through-concrete walls  
     Loitering ,  Elevator Count  
     
    
   
  
  
  🏟️ Specialized  — Events, fitness, education, civic (CSI-capable hardware) 
   
    
     
     Use Case  
     What It Does  
     Hardware  
     Key Metric  
     Edge Module  
     
    
    
     
     Smart home automation  
     Room-level presence triggers (lights, HVAC, music) that work through walls — no dead zones, no motion-sensor timeouts  
     2-3 ESP32-S3 nodes ($24)  
     Through-wall range ~5m  
     HVAC Presence ,  Lighting Zones  
     
     
     Fitness & sports  
     Rep counting, posture correction, breathing cadence during exercise — no wearable, no camera in locker rooms  
     3+ ESP32-S3 mesh  
     Pose: 17 keypoints  
     Breathing Sync ,  Gait Analysis  
     
     
     Childcare & schools  
     Naptime breathing monitoring, playground headcount, restricted-area alerts — privacy-safe for minors  
     2-4 ESP32-S3 per zone  
     Breathing: ±1 BPM  
     Sleep Apnea ,  Perimeter Breach  
     
     
     Event venues & concerts  
     Crowd density mapping, crush-risk detection via breathing compression, emergency evacuation flow tracking  
     Multi-AP mesh (4-8 APs)  
     Density per m²  
     Customer Flow ,  Panic Motion  
     
     
     Stadiums & arenas  
     Section-level occupancy for dynamic pricing, concession staffing, emergency egress flow modeling  
     Enterprise AP grid  
     15-20 per AP mesh  
     Dwell Heatmap ,  Queue Length  
     
     
     Houses of worship  
     Attendance counting without facial recognition — privacy-sensitive congregations, multi-room campus tracking  
     Existing WiFi  
     Zone-level accuracy  
     Elevator Count ,  Energy Audit  
     
     
     Warehouse & logistics  
     Worker safety zones, forklift proximity alerts, occupancy in hazardous areas — works through shelving and pallets  
     Industrial AP mesh  
     Alert latency <500ms  
     Forklift Proximity ,  Confined Space  
     
     
     Civic infrastructure  
     Public restroom occupancy (no cameras possible), subway platform crowding, shelter headcount during emergencies  
     Municipal WiFi + ESP32  
     Real-time headcount  
     Customer Flow ,  Loitering  
     
     
     Museums & galleries  
     Visitor flow heatmaps, exhibit dwell time, crowd bottleneck alerts — no cameras near artwork (flash/theft risk)  
     Existing WiFi  
     Zone dwell ±5s  
     Dwell Heatmap ,  Shelf Engagement  
     
    
   
  
  
  🤖 Robotics & Industrial  — Autonomous systems, manufacturing, android spatial awareness 
  WiFi sensing gives robots and autonomous systems a spatial awareness layer that works where LIDAR and cameras fail — through dust, smoke, fog, and around corners. The CSI signal field acts as a "sixth sense" for detecting humans in the environment without requiring line-of-sight.  
   
    
     
     Use Case  
     What It Does  
     Hardware  
     Key Metric  
     Edge Module  
     
    
    
     
     Cobot safety zones  
     Detect human presence near collaborative robots — auto-slow or stop before contact, even behind obstructions  
     2-3 ESP32-S3 per cell  
     Presence latency <100ms  
     Forklift Proximity ,  Perimeter Breach  
     
     
     Warehouse AMR navigation  
     Autonomous mobile robots sense humans around blind corners, through shelving racks — no LIDAR occlusion  
     ESP32 mesh along aisles  
     Through-shelf detection  
     Forklift Proximity ,  Loitering  
     
     
     Android / humanoid spatial awareness  
     Ambient human pose sensing for social robots — detect gestures, approach direction, and personal space without cameras always on  
     Onboard ESP32-S3 module  
     17-keypoint pose  
     Gesture Language ,  Emotion Detection  
     
     
     Manufacturing line monitoring  
     Worker presence at each station, ergonomic posture alerts, headcount for shift compliance — works through equipment  
     Industrial AP per zone  
     Pose + breathing  
     Confined Space ,  Gait Analysis  
     
     
     Construction site safety  
     Exclusion zone enforcement around heavy machinery, fall detection from scaffolding, personnel headcount  
     Ruggedized ESP32 mesh  
     Alert <2s, through-dust  
     Panic Motion ,  Structural Vibration  
     
     
     Agricultural robotics  
     Detect farm workers near autonomous harvesters in dusty/foggy field conditions where cameras are unreliable  
     Weatherproof ESP32 nodes  
     Range ~10m open field  
     Forklift Proximity ,  Rain Detection  
     
     
     Drone landing zones  
     Verify landing area is clear of humans — WiFi sensing works in rain, dust, and low light where downward cameras fail  
     Ground ESP32 nodes  
     Presence: >95% accuracy  
     Perimeter Breach ,  Tailgating  
     
     
     Clean room monitoring  
     Personnel tracking without cameras (particle contamination risk from camera fans) — gown compliance via pose  
     Existing cleanroom WiFi  
     No particulate emission  
     Clean Room ,  Livestock Monitor  
     
    
   
  
  
  🔥 Extreme  — Through-wall, disaster, defense, underground 
  These scenarios exploit WiFi's ability to penetrate solid materials — concrete, rubble, earth — where no optical or infrared sensor can reach. The WiFi-Mat disaster module (ADR-001) is specifically designed for this tier.  
   
    
     
     Use Case  
     What It Does  
     Hardware  
     Key Metric  
     Edge Module  
     
    
    
     
     Search & rescue (WiFi-Mat)  
     Detect survivors through rubble/debris via breathing signature, START triage color classification, 3D localization  
     Portable ESP32 mesh + laptop  
     Through 30cm concrete  
     Respiratory Distress ,  Seizure Detection  
     
     
     Firefighting  
     Locate occupants through smoke and walls before entry; breathing detection confirms life signs remotely  
     Portable mesh on truck  
     Works in zero visibility  
     Sleep Apnea ,  Panic Motion  
     
     
     Prison & secure facilities  
     Cell occupancy verification, distress detection (abnormal vitals), perimeter sensing — no camera blind spots  
     Dedicated AP infrastructure  
     24/7 vital signs  
     Cardiac Arrhythmia ,  Loitering  
     
     
     Military / tactical  
     Through-wall personnel detection, room clearing confirmation, hostage vital signs at standoff distance  
     Directional WiFi + custom FW  
     Range: 5m through wall  
     Perimeter Breach ,  Weapon Detection  
     
     
     Border & perimeter security  
     Detect human presence in tunnels, behind fences, in vehicles — passive sensing, no active illumination to reveal position  
     Concealed ESP32 mesh  
     Passive / covert  
     Perimeter Breach ,  Tailgating  
     
     
     Mining & underground  
     Worker presence in tunnels where GPS/cameras fail, breathing detection after collapse, headcount at safety points  
     Ruggedized ESP32 mesh  
     Through rock/earth  
     Confined Space ,  Respiratory Distress  
     
     
     Maritime & naval  
     Below-deck personnel tracking through steel bulkheads (limited range, requires tuning), man-overboard detection  
     Ship WiFi + ESP32  
     Through 1-2 bulkheads  
     Structural Vibration ,  Panic Motion  
     
     
     Wildlife research  
     Non-invasive animal activity monitoring in enclosures or dens — no light pollution, no visual disturbance  
     Weatherproof ESP32 nodes  
     Zero light emission  
     Livestock Monitor ,  Dream Stage  
     
    
   
  
  
  🧩 Edge Intelligence ( ADR-041 )  — 60 WASM modules across 13 categories, all implemented (609 tests) 
  Small programs that run directly on the ESP32 sensor — no internet needed, no cloud fees, instant response. Each module is a tiny WASM file (5-30 KB) that you upload to the device over-the-air. It reads WiFi signal data and makes decisions locally in under 10 ms.  ADR-041  defines 60 modules across 13 categories — all 60 are implemented with 609 tests passing.  
   
    
     
      
     Category  
     Examples  
     
    
    
     
     🏥  
     Medical & Health  
     Sleep apnea detection, cardiac arrhythmia, gait analysis, seizure detection  
     
     
     🔐  
     Security & Safety  
     Intrusion detection, perimeter breach, loitering, panic motion  
     
     
     🏢  
     Smart Building  
     Zone occupancy, HVAC control, elevator counting, meeting room tracking  
     
     
     🛒  
     Retail & Hospitality  
     Queue length, dwell heatmaps, customer flow, table turnover  
     
     
     🏭  
     Industrial  
     Forklift proximity, confined space monitoring, structural vibration  
     
     
     🔮  
     Exotic & Research  
     Sleep staging, emotion detection, sign language, breathing sync  
     
     
     📡  
     Signal Intelligence  
     Cleans and sharpens raw WiFi signals — focuses on important regions, filters noise, fills in missing data, and tracks which person is which  
     
     
     🧠  
     Adaptive Learning  
     The sensor learns new gestures and patterns on its own over time — no cloud needed, remembers what it learned even after updates  
     
     
     🗺️  
     Spatial Reasoning  
     Figures out where people are in a room, which zones matter most, and tracks movement across areas using graph-based spatial logic  
     
     
     ⏱️  
     Temporal Analysis  
     Learns daily routines, detects when patterns break (someone didn't get up), and verifies safety rules are being followed over time  
     
     
     🛡️  
     AI Security  
     Detects signal replay attacks, WiFi jamming, injection attempts, and flags abnormal behavior that could indicate tampering  
     
     
     ⚛️  
     Quantum-Inspired  
     Uses quantum-inspired math to map room-wide signal coherence and search for optimal sensor configurations  
     
     
     🤖  
     Autonomous & Exotic  
     Self-managing sensor mesh — auto-heals dropped nodes, plans its own actions, and explores experimental signal representations  
     
    
   
  All implemented modules are  `no_std`  Rust, share a  common utility library , and talk to the host through a 12-function API. Full documentation:  Edge Modules Guide . See the  complete implemented module list  below.  
  
  
  🧩 Edge Intelligence —  All 65 Modules Implemented  (ADR-041 complete) 
  All 60 modules are implemented, tested (609 tests passing), and ready to deploy. They compile to  `wasm32-unknown-unknown` , run on ESP32-S3 via WASM3, and share a  common utility library . Source:  `crates/wifi-densepose-wasm-edge/src/`  
  Core modules  (ADR-040 flagship + early implementations):  
   
    
     
     Module  
     File  
     What It Does  
     
    
    
     
     Gesture Classifier  
     `gesture.rs`  
     DTW template matching for hand gestures  
     
     
     Coherence Filter  
     `coherence.rs`  
     Phase coherence gating for signal quality  
     
     
     Adversarial Detector  
     `adversarial.rs`  
     Detects physically impossible signal patterns  
     
     
     Intrusion Detector  
     `intrusion.rs`  
     Human vs non-human motion classification  
     
     
     Occupancy Counter  
     `occupancy.rs`  
     Zone-level person counting  
     
     
     Vital Trend  
     `vital_trend.rs`  
     Long-term breathing and heart rate trending  
     
     
     RVF Parser  
     `rvf.rs`  
     RVF container format parsing  
     
    
   
  Vendor-integrated modules  (24 modules, ADR-041 Category 7):  
  📡 Signal Intelligence  — Real-time CSI analysis and feature extraction  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Flash Attention  
     `sig_flash_attention.rs`  
     Tiled attention over 8 subcarrier groups — finds spatial focus regions and entropy  
     S (<5ms)  
     
     
     Coherence Gate  
     `sig_coherence_gate.rs`  
     Z-score phasor gating with hysteresis: Accept / PredictOnly / Reject / Recalibrate  
     L (<2ms)  
     
     
     Temporal Compress  
     `sig_temporal_compress.rs`  
     3-tier adaptive quantization (8-bit hot / 5-bit warm / 3-bit cold)  
     L (<2ms)  
     
     
     Sparse Recovery  
     `sig_sparse_recovery.rs`  
     ISTA L1 reconstruction for dropped subcarriers  
     H (<10ms)  
     
     
     Person Match  
     `sig_mincut_person_match.rs`  
     Hungarian-lite bipartite assignment for multi-person tracking  
     S (<5ms)  
     
     
     Optimal Transport  
     `sig_optimal_transport.rs`  
     Sliced Wasserstein-1 distance with 4 projections  
     L (<2ms)  
     
    
   
  🧠 Adaptive Learning  — On-device learning without cloud connectivity  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     DTW Gesture Learn  
     `lrn_dtw_gesture_learn.rs`  
     User-teachable gesture recognition — 3-rehearsal protocol, 16 templates  
     S (<5ms)  
     
     
     Anomaly Attractor  
     `lrn_anomaly_attractor.rs`  
     4D dynamical system attractor classification with Lyapunov exponents  
     H (<10ms)  
     
     
     Meta Adapt  
     `lrn_meta_adapt.rs`  
     Hill-climbing self-optimization with safety rollback  
     L (<2ms)  
     
     
     EWC Lifelong  
     `lrn_ewc_lifelong.rs`  
     Elastic Weight Consolidation — remembers past tasks while learning new ones  
     S (<5ms)  
     
    
   
  🗺️ Spatial Reasoning  — Location, proximity, and influence mapping  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     PageRank Influence  
     `spt_pagerank_influence.rs`  
     4x4 cross-correlation graph with power iteration PageRank  
     L (<2ms)  
     
     
     Micro HNSW  
     `spt_micro_hnsw.rs`  
     64-vector navigable small-world graph for nearest-neighbor search  
     S (<5ms)  
     
     
     Spiking Tracker  
     `spt_spiking_tracker.rs`  
     32 LIF neurons + 4 output zone neurons with STDP learning  
     S (<5ms)  
     
    
   
  ⏱️ Temporal Analysis  — Activity patterns, logic verification, autonomous planning  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Pattern Sequence  
     `tmp_pattern_sequence.rs`  
     Activity routine detection and deviation alerts  
     S (<5ms)  
     
     
     Temporal Logic Guard  
     `tmp_temporal_logic_guard.rs`  
     LTL formula verification on CSI event streams  
     S (<5ms)  
     
     
     GOAP Autonomy  
     `tmp_goap_autonomy.rs`  
     Goal-Oriented Action Planning for autonomous module management  
     S (<5ms)  
     
    
   
  🛡️ AI Security  — Tamper detection and behavioral anomaly profiling  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Prompt Shield  
     `ais_prompt_shield.rs`  
     FNV-1a replay detection, injection detection (10x amplitude), jamming (SNR)  
     L (<2ms)  
     
     
     Behavioral Profiler  
     `ais_behavioral_profiler.rs`  
     6D behavioral profile with Mahalanobis anomaly scoring  
     S (<5ms)  
     
    
   
  ⚛️ Quantum-Inspired  — Quantum computing metaphors applied to CSI analysis  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Quantum Coherence  
     `qnt_quantum_coherence.rs`  
     Bloch sphere mapping, Von Neumann entropy, decoherence detection  
     S (<5ms)  
     
     
     Interference Search  
     `qnt_interference_search.rs`  
     16 room-state hypotheses with Grover-inspired oracle + diffusion  
     S (<5ms)  
     
    
   
  🤖 Autonomous Systems  — Self-governing and self-healing behaviors  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Psycho-Symbolic  
     `aut_psycho_symbolic.rs`  
     16-rule forward-chaining knowledge base with contradiction detection  
     S (<5ms)  
     
     
     Self-Healing Mesh  
     `aut_self_healing_mesh.rs`  
     8-node mesh with health tracking, degradation/recovery, coverage healing  
     S (<5ms)  
     
    
   
  🔮 Exotic (Vendor)  — Novel mathematical models for CSI interpretation  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Time Crystal  
     `exo_time_crystal.rs`  
     Autocorrelation subharmonic detection in 256-frame history  
     S (<5ms)  
     
     
     Hyperbolic Space  
     `exo_hyperbolic_space.rs`  
     Poincare ball embedding with 32 reference locations, hyperbolic distance  
     S (<5ms)  
     
    
   
  🏥 Medical & Health  (Category 1) — Contactless health monitoring  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Sleep Apnea  
     `med_sleep_apnea.rs`  
     Detects breathing pauses during sleep  
     S (<5ms)  
     
     
     Cardiac Arrhythmia  
     `med_cardiac_arrhythmia.rs`  
     Monitors heart rate for irregular rhythms  
     S (<5ms)  
     
     
     Respiratory Distress  
     `med_respiratory_distress.rs`  
     Alerts on abnormal breathing patterns  
     S (<5ms)  
     
     
     Gait Analysis  
     `med_gait_analysis.rs`  
     Tracks walking patterns and detects changes  
     S (<5ms)  
     
     
     Seizure Detection  
     `med_seizure_detect.rs`  
     6-state machine for tonic-clonic seizure recognition  
     S (<5ms)  
     
    
   
  🔐 Security & Safety  (Category 2) — Perimeter and threat detection  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Perimeter Breach  
     `sec_perimeter_breach.rs`  
     Detects boundary crossings with approach/departure  
     S (<5ms)  
     
     
     Weapon Detection  
     `sec_weapon_detect.rs`  
     Metal anomaly detection via CSI amplitude shifts  
     S (<5ms)  
     
     
     Tailgating  
     `sec_tailgating.rs`  
     Detects unauthorized follow-through at access points  
     S (<5ms)  
     
     
     Loitering  
     `sec_loitering.rs`  
     Alerts when someone lingers too long in a zone  
     S (<5ms)  
     
     
     Panic Motion  
     `sec_panic_motion.rs`  
     Detects fleeing, struggling, or panic movement  
     S (<5ms)  
     
    
   
  🏢 Smart Building  (Category 3) — Automation and energy efficiency  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     HVAC Presence  
     `bld_hvac_presence.rs`  
     Occupancy-driven HVAC control with departure countdown  
     S (<5ms)  
     
     
     Lighting Zones  
     `bld_lighting_zones.rs`  
     Auto-dim/off lighting based on zone activity  
     S (<5ms)  
     
     
     Elevator Count  
     `bld_elevator_count.rs`  
     Counts people entering/leaving with overload warning  
     S (<5ms)  
     
     
     Meeting Room  
     `bld_meeting_room.rs`  
     Tracks meeting lifecycle: start, headcount, end, availability  
     S (<5ms)  
     
     
     Energy Audit  
     `bld_energy_audit.rs`  
     Tracks after-hours usage and room utilization rates  
     S (<5ms)  
     
    
   
  🛒 Retail & Hospitality  (Category 4) — Customer insights without cameras  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Queue Length  
     `ret_queue_length.rs`  
     Estimates queue size and wait times  
     S (<5ms)  
     
     
     Dwell Heatmap  
     `ret_dwell_heatmap.rs`  
     Shows where people spend time (hot/cold zones)  
     S (<5ms)  
     
     
     Customer Flow  
     `ret_customer_flow.rs`  
     Counts ins/outs and tracks net occupancy  
     S (<5ms)  
     
     
     Table Turnover  
     `ret_table_turnover.rs`  
     Restaurant table lifecycle: seated, dining, vacated  
     S (<5ms)  
     
     
     Shelf Engagement  
     `ret_shelf_engagement.rs`  
     Detects browsing, considering, and reaching for products  
     S (<5ms)  
     
    
   
  🏭 Industrial & Specialized  (Category 5) — Safety and compliance  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Forklift Proximity  
     `ind_forklift_proximity.rs`  
     Warns when people get too close to vehicles  
     S (<5ms)  
     
     
     Confined Space  
     `ind_confined_space.rs`  
     OSHA-compliant worker monitoring with extraction alerts  
     S (<5ms)  
     
     
     Clean Room  
     `ind_clean_room.rs`  
     Occupancy limits and turbulent motion detection  
     S (<5ms)  
     
     
     Livestock Monitor  
     `ind_livestock_monitor.rs`  
     Animal presence, stillness, and escape alerts  
     S (<5ms)  
     
     
     Structural Vibration  
     `ind_structural_vibration.rs`  
     Seismic events, mechanical resonance, structural drift  
     S (<5ms)  
     
    
   
  🔮 Exotic & Research  (Category 6) — Experimental sensing applications  
   
    
     
     Module  
     File  
     What It Does  
     Budget  
     
    
    
     
     Dream Stage  
     `exo_dream_stage.rs`  
     Contactless sleep stage classification (wake/light/deep/REM)  
     S (<5ms)  
     
     
     Emotion Detection  
     `exo_emotion_detect.rs`  
     Arousal, stress, and calm detection from micro-movements  
     S (<5ms)  
     
     
     Gesture Language  
     `exo_gesture_language.rs`  
     Sign language letter recognition via WiFi  
     S (<5ms)  
     
     
     Music Conductor  
     `exo_music_conductor.rs`  
     Tempo and dynamic tracking from conducting gestures  
     S (<5ms)  
     
     
     Plant Growth  
     `exo_plant_growth.rs`  
     Monitors plant growth, circadian rhythms, wilt detection  
     S (<5ms)  
     
     
     Ghost Hunter  
     `exo_ghost_hunter.rs`  
     Environmental anomaly classification (draft/insect/wind/unknown)  
     S (<5ms)  
     
     
     Rain Detection  
     `exo_rain_detect.rs`  
     Detects rain onset, intensity, and cessation via signal scatter  
     S (<5ms)  
     
     
     Breathing Sync  
     `exo_breathing_sync.rs`  
     Detects synchronized breathing between multiple people  
     S (<5ms)  
     
    
   
  
  
  
  🧠 Self-Learning WiFi AI (ADR-024)  — Adaptive recognition, self-optimization, and intelligent anomaly detection 
  Every WiFi signal that passes through a room creates a unique fingerprint of that space. WiFi-DensePose already reads these fingerprints to track people, but until now it threw away the internal "understanding" after each reading. The Self-Learning WiFi AI captures and preserves that understanding as compact, reusable vectors — and continuously optimizes itself for each new environment.  
  What it does in plain terms:  
   
   Turns any WiFi signal into a 128-number "fingerprint" that uniquely describes what's happening in a room  
   Learns entirely on its own from raw WiFi data — no cameras, no labeling, no human supervision needed  
   Recognizes rooms, detects intruders, identifies people, and classifies activities using only WiFi  
   Runs on an $8 ESP32 chip (the entire model fits in 55 KB of memory)  
   Produces both body pose tracking AND environment fingerprints in a single computation  
   
  Key Capabilities  
   
    
     
     What  
     How it works  
     Why it matters  
     
    
    
     
     Self-supervised learning  
     The model watches WiFi signals and teaches itself what "similar" and "different" look like, without any human-labeled data  
     Deploy anywhere — just plug in a WiFi sensor and wait 10 minutes  
     
     
     Room identification  
     Each room produces a distinct WiFi fingerprint pattern  
     Know which room someone is in without GPS or beacons  
     
     
     Anomaly detection  
     An unexpected person or event creates a fingerprint that doesn't match anything seen before  
     Automatic intrusion and fall detection as a free byproduct  
     
     
     Person re-identification  
     Each person disturbs WiFi in a slightly different way, creating a personal signature  
     Track individuals across sessions without cameras  
     
     
     Environment adaptation  
     MicroLoRA adapters (1,792 parameters per room) fine-tune the model for each new space  
     Adapts to a new room with minimal data — 93% less than retraining from scratch  
     
     
     Memory preservation  
     EWC++ regularization remembers what was learned during pretraining  
     Switching to a new task doesn't erase prior knowledge  
     
     
     Hard-negative mining  
     Training focuses on the most confusing examples to learn faster  
     Better accuracy with the same amount of training data  
     
    
   
  Architecture  
  `WiFi Signal [56 channels] → Transformer + Graph Neural Network`
                                  `├→ 128-dim environment fingerprint (for search + identification)`
                                  `└→ 17-joint body pose (for human tracking)`
  
  Quick Start  
  ```bash
# Step 1: Learn from raw WiFi data (no labels needed)
cargo run -p wifi-densepose-sensing-server -- --pretrain --dataset data/csi/ --pretrain-epochs 50

# Step 2: Fine-tune with pose labels for full capability
cargo run -p wifi-densepose-sensing-server -- --train --dataset data/mmfi/ --epochs 100 --save-rvf model.rvf

# Step 3: Use the model — extract fingerprints from live WiFi
cargo run -p wifi-densepose-sensing-server -- --model model.rvf --embed

# Step 4: Search — find similar environments or detect anomalies
cargo run -p wifi-densepose-sensing-server -- --model model.rvf --build-index env
```
  
  Training Modes  
   
    
     
     Mode  
     What you need  
     What you get  
     
    
    
     
     Self-Supervised  
     Just raw WiFi data  
     A model that understands WiFi signal structure  
     
     
     Supervised  
     WiFi data + body pose labels  
     Full pose tracking + environment fingerprints  
     
     
     Cross-Modal  
     WiFi data + camera footage  
     Fingerprints aligned with visual understanding  
     
    
   
  Fingerprint Index Types  
   
    
     
     Index  
     What it stores  
     Real-world use  
     
    
    
     
     env_fingerprint  
     Average room fingerprint  
     "Is this the kitchen or the bedroom?"  
     
     
     activity_pattern  
     Activity boundaries  
     "Is someone cooking, sleeping, or exercising?"  
     
     
     temporal_baseline  
     Normal conditions  
     "Something unusual just happened in this room"  
     
     
     person_track  
     Individual movement signatures  
     "Person A just entered the living room"  
     
    
   
  Model Size  
   
    
     
     Component  
     Parameters  
     Memory (on ESP32)  
     
    
    
     
     Transformer backbone  
     ~28,000  
     28 KB  
     
     
     Embedding projection head  
     ~25,000  
     25 KB  
     
     
     Per-room MicroLoRA adapter  
     ~1,800  
     2 KB  
     
     
     Total  
     ~55,000  
     55 KB  (of 520 KB available)  
     
    
   
  The self-learning system builds on the  AI Backbone (RuVector)  signal-processing layer — attention, graph algorithms, and compression — adding contrastive learning on top.  
  See  `docs/adr/ADR-024-contrastive-csi-embedding-model.md`  for full architectural details.  
  
  
 🧩 Claude Code & Codex Plugin  
 RuView ships a  Claude Code  plugin (and Codex prompt mirror) that wraps the whole workflow — onboarding, ESP32 setup, configuration, sensing apps, model training, advanced multistatic sensing, CLI/API/WASM, mmWave radar, and witness verification — as 9 skills, 7  `/ruview-*`  commands, and 3 agents. It lives in  `plugins/ruview/` ; the marketplace manifest is  `.claude-plugin/marketplace.json`  at the repo root.  
 ```bash
# In Claude Code — add this repo as a plugin marketplace, then install:
/plugin marketplace add ruvnet/RuView
/plugin install ruview@ruview

# Or try it for one session without installing (from a local clone of the repo):
claude --plugin-dir ./plugins/ruview

# Then, in Claude Code:
#   /ruview-start      → onboarding (Docker demo / repo build / live ESP32)
#   /ruview-flash      → build + flash ESP32 firmware
#   /ruview-provision  → provision WiFi creds, sink IP, channel/MAC, mesh slots
#   /ruview-app        → run a sensing application (presence / vitals / pose / sleep / MAT / point cloud)
#   /ruview-train      → train / evaluate / publish a model (incl. GPU on GCloud)
#   /ruview-advanced   → multistatic / tomography / cross-viewpoint / mesh-security
#   /ruview-verify     → tests + deterministic proof + witness bundle
```
  
 Codex (OpenAI CLI):   `cp plugins/ruview/codex/prompts/*.md ~/.codex/prompts/`  — the seven  `/ruview-*`  commands are mirrored as Codex prompts;  `plugins/ruview/codex/AGENTS.md`  carries the project rules. See  `plugins/ruview/codex/README.md` .  
 Verify the plugin structure:  `bash plugins/ruview/scripts/smoke.sh` . Full details:  `plugins/ruview/README.md` .  
  
 📖 Documentation  
  
   
    
    Document  
    Description  
    
   
   
    
    User Guide  
    Step-by-step guide: installation, first run, API usage, hardware setup, training  
    
    
    Build Guide  
    Building from source (Rust and Python)  
    
    
    Claude Code / Codex Plugin  
    The  `ruview`  plugin + marketplace — skills,  `/ruview-*`  commands, agents, and the Codex prompt mirror  
    
    
    Architecture Decisions  
    96 ADRs — why each technical choice was made, organized by domain (hardware, signal processing, ML, platform, infrastructure)  
    
    
    Domain Models  
    8 DDD models (RuvSense, Signal Processing, Training Pipeline, Hardware Platform, Sensing Server, WiFi-Mat, CHCI, rvCSI) — bounded contexts, aggregates, domain events, and ubiquitous language  
    
    
    rvCSI — edge RF sensing runtime  
    Rust-first / TypeScript-accessible / hardware-abstracted CSI runtime: multi-source ingestion (incl. real  `nexmon_csi`   `.pcap`  from a  Raspberry Pi 5  / Pi 4 / Pi 3B+ — CYW43455 / BCM43455c0) → validation → DSP → typed events → RuVector RF memory ( ADR-095 ,  ADR-096 ,  domain model ). Now its own repo —  ruvnet/rvcsi  — vendored here under  `vendor/rvcsi` ; 9  `rvcsi-*`  crates on  `crates.io` ,  `@ruv/rvcsi`  on npm, plus a Claude Code plugin.  
    
    
    Desktop App  
    WIP  — Tauri v2 desktop app for node management, OTA updates, WASM deployment, and mesh visualization  
    
    
    Medical Examples  
    Contactless blood pressure, heart rate, breathing rate via 60 GHz mmWave radar — $15 hardware, no wearable  
    
    
    Extended Documentation  
    Latest additions, key features, installation, quick start, signal processing, training, CLI, testing, deployment, and changelog  
    
   
  
  
 📄 License  
 MIT License — see  LICENSE  for details.  
 📞 Support  
 GitHub Issues  |  Discussions  |  PyPI  
  
 WiFi DensePose  — Privacy-preserving human pose estimation through WiFi signals.

---

## 13. [millionco/react-doctor](https://github.com/millionco/react-doctor)

> [→ GitHub 連結](https://github.com/millionco/react-doctor)

Your agent writes bad React. This catches it  
   
   
   
 
    
 Your agent writes bad React, this catches it.  
 One command scans your codebase and outputs a  `0 to 100 health score`  with actionable diagnostics.  
 Works with Next.js, Vite, and React Native.  
 See it in action →  
 Install  
 Run this at your project root:  
 ```bash
npx -y react-doctor@latest .
```
  
 You'll get a score (75+ Great, 50 to 74 Needs work, under 50 Critical) and a list of issues across state & effects, performance, architecture, security, accessibility, and dead code. Rules toggle automatically based on your framework and React version.  
 https://github.com/user-attachments/assets/07cc88d9-9589-44c3-aa73-5d603cb1c570  
 Install for your coding agent  
 Teach your coding agent React best practices so it stops writing the bad code in the first place.  
 ```bash
npx -y react-doctor@latest install
```
  
 You'll be prompted to pick which detected agents to install for. Pass  `--yes`  to skip prompts.  
 Works with Claude Code, Cursor, Codex, OpenCode, and 50+ other agents.  
 GitHub Actions  
 A composite action ships with this repository. Drop it into  `.github/workflows/react-doctor.yml` :  
 ```yaml
name: React Doctor

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read
  pull-requests: write # required to post PR comments

jobs:
  react-doctor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
        with:
          fetch-depth: 0 # required for `diff`
      - uses: millionco/react-doctor@main
        with:
          diff: main
          github-token: ${{ secrets.GITHUB_TOKEN }}
```
  
 When  `github-token`  is set on  `pull_request`  events, findings are posted (and updated) as a PR comment. The action also exposes a  `score`  output (0–100) you can use in subsequent steps.  
 Inputs:   `directory` ,  `verbose` ,  `project` ,  `diff` ,  `github-token` ,  `fail-on`  ( `error`  /  `warning`  /  `none` ),  `offline` ,  `node-version` . See  `action.yml`  for full descriptions.  
 Prefer not to add a marketplace action? The bare  `npx`  form works too:  
 ```yaml
- run: npx -y react-doctor@latest --fail-on warning
```
  
 Configuration  
 Create a  `react-doctor.config.json`  in your project root:  
 ```json
{
  "ignore": {
    "rules": ["react/no-danger", "jsx-a11y/no-autofocus"],
    "files": ["src/generated/**"],
    "overrides": [
      {
        "files": ["components/modules/diff/**"],
        "rules": ["react-doctor/no-array-index-as-key", "react-doctor/no-render-in-render"]
      },
      {
        "files": ["components/search/HighlightedSnippet.tsx"],
        "rules": ["react/no-danger"]
      }
    ]
  }
}
```
  
 Three nested keys, three layers of granularity — pick the narrowest one that fits:  
  
  `ignore.rules`  silences a rule across the whole codebase.  
  `ignore.files`  silences  every  rule on the matched files (use sparingly — it loses coverage for unrelated rules).  
  `ignore.overrides`  silences only the listed rules on the matched files, leaving every other rule active. This is what you want when a single file (or glob) legitimately needs an exemption from one or two rules but should still be scanned for everything else.  
  
 You can also use the  `"reactDoctor"`  key in  `package.json` . CLI flags always override config values.  
 React Doctor respects  `.gitignore` ,  `.eslintignore` ,  `.oxlintignore` ,  `.prettierignore` , and  `linguist-vendored`  /  `linguist-generated`  annotations in  `.gitattributes` . Inline  `// eslint-disable*`  and  `// oxlint-disable*`  comments are honored too.  
 If you have a JSON oxlint or eslint config ( `.oxlintrc.json`  or  `.eslintrc.json` ), its rules get merged into the scan automatically and count toward the score. Set  `adoptExistingLintConfig: false`  to opt out.  
 Surface controls (CLI, PR comments, score, CI failure)  
 Diagnostics flow through four independent surfaces —  `cli` ,  `prComment` ,  `score` , and  `ciFailure`  — and each one can be tuned per tag, category, or rule id. By default the  `design`  tag (Tailwind shorthand cleanup like  `w-5 h-5 → size-5` , pure-black backgrounds, gradient text, …) stays visible on the local CLI but is excluded from the PR comment, the score, and the  `--fail-on`  gate so style cleanup can't dilute meaningful React findings:  
 ```json
{
  "surfaces": {
    "prComment": {
      "includeTags": ["design"],
      "excludeCategories": ["Performance"]
    },
    "score": { "includeRules": ["react-doctor/design-no-redundant-size-axes"] },
    "ciFailure": { "excludeTags": ["test-noise"] }
  }
}
```
  
 Each surface accepts  `includeTags` ,  `excludeTags` ,  `includeCategories` ,  `excludeCategories` ,  `includeRules` , and  `excludeRules` . Include wins over exclude when both match. Run the CLI with  `--pr-comment`  (the GitHub Action passes it automatically when  `github-token`  is set) to apply the  `prComment`  surface to the printed output destined for sticky PR comments.  
 Optional companion plugins  
 When the following ESLint plugins are installed in the scanned project (or hoisted in your monorepo), React Doctor folds their rules into the same scan. Both are listed as  `optional peer dependencies`  — install only what you want.  
  
   
    
    Plugin  
    Adds  
    Namespace  
    
   
   
    
    eslint-plugin-react-hooks  (v6 or v7)  
    The React Compiler frontend's correctness rules — fired when a React Compiler is detected in the project.  
    `react-hooks-js/*`  
    
    
    eslint-plugin-react-you-might-not-need-an-effect  (v0.10+)  
    Complementary effects-as-anti-pattern rules ( `no-derived-state` ,  `no-chain-state-updates` ,  `no-event-handler` ,  `no-pass-data-to-parent` , …) that run alongside React Doctor's native State & Effects rules.  
    `effect/*`  
    
   
  
 Inline suppressions  
 ```javascript
// react-doctor-disable-next-line react-doctor/no-cascading-set-state
useEffect(() => {
  setA(value);
  setB(value);
}, [value]);
```
  
 When two rules fire on the same line, you have two equivalent options. Comma-separate the rule ids on a single comment:  
 ```javascript
// react-doctor-disable-next-line react-doctor/rerender-state-only-in-handlers, react-doctor/no-derived-useState
const [localSearch, setLocalSearch] = useState(searchQuery);
```
  
 Or stack one comment per rule directly above the diagnostic. Stacked comments are honored as long as nothing but other  `react-doctor-disable-next-line`  comments sits between them and the target line:  
 ```javascript
// react-doctor-disable-next-line react-doctor/rerender-state-only-in-handlers
// react-doctor-disable-next-line react-doctor/no-derived-useState
const [localSearch, setLocalSearch] = useState(searchQuery);
```
  
 A code line between stacked comments breaks the chain: only the comment immediately above the diagnostic (and any contiguous  `react-doctor-disable-next-line`  comments stacked on top of it) is honored. If a comment looks adjacent but the rule still fires, run  `react-doctor --explain <file:line>`  — it reports whether a nearby suppression was found, what rules it covers, and why it didn't apply.  
 Block comments work inside JSX:  
  
 ```jsx
{/* react-doctor-disable-next-line react/no-danger */}
<div dangerouslySetInnerHTML={{ __html }} />
```
  
 For multi-line JSX, putting the comment immediately above the opening tag covers the entire attribute list (matching ESLint convention).  
 Lint plugin (standalone)  
 The same rule set ships as both an oxlint plugin and an ESLint plugin, so you can wire it into whichever lint engine your project already runs. These are published as separate packages, so you can install just the lint integration without pulling in the full CLI.  
 `oxlint`  in  `.oxlintrc.json`  (install  `oxlint-plugin-react-doctor` ):  
 ```json
{
  "jsPlugins": [{ "name": "react-doctor", "specifier": "oxlint-plugin-react-doctor" }],
  "rules": {
    "react-doctor/no-fetch-in-effect": "warn",
    "react-doctor/no-derived-state-effect": "warn",
  },
}
```
  
 ESLint  flat config (install  `eslint-plugin-react-doctor` ):  
 ```javascript
import reactDoctor from "eslint-plugin-react-doctor";

export default [
  reactDoctor.configs.recommended,
  reactDoctor.configs.next,
  reactDoctor.configs["react-native"],
  reactDoctor.configs["tanstack-start"],
  reactDoctor.configs["tanstack-query"],
];
```
  
 The full rule list lives in  `packages/oxlint-plugin-react-doctor/src/plugin/rules` .  
 CLI reference  
 ```
Usage: react-doctor [directory] [options]

Options:
  -v, --version           display the version number
  --no-lint               skip linting
  --verbose               show every rule and per-file details (default shows top 3 rules)
  --score                 output only the score
  --json                  output a single structured JSON report
  -y, --yes               skip prompts, scan all workspace projects
  --full                  skip prompts, always run a full scan
  --project <name>        select workspace project (comma-separated for multiple)
  --diff [base]           scan only files changed vs base branch
  --staged                scan only staged files (for pre-commit hooks)
  --offline               skip the score API and share URL (no score shown)
  --fail-on <level>       exit with error on diagnostics: error, warning, none
  --annotations           output diagnostics as GitHub Actions annotations
  --pr-comment            tune CLI output for sticky PR comments (drops design
                          cleanup from the printed list and fail-on gate)
  --explain <file:line>   diagnose why a rule fired or why a suppression didn't apply
  --why <file:line>       alias for --explain
  -h, --help              display help
```
  
 When a suppression isn't working,  `--explain <file:line>`  (or its alias  `--why <file:line>` ) reports what the scanner sees at that location, including why a nearby  `react-doctor-disable-next-line`  didn't apply. The diagnosis distinguishes the common failure modes — adjacent comment for a different rule (use the comma form), a code line between the comment and the diagnostic (the chain is broken), or no nearby suppression at all. The same hint surfaces inline with  `--verbose`  for every flagged site, and in  `--json`  output as  `diagnostic.suppressionHint` , so a single scan doubles as a suppression audit without a separate flag.  
 `--json`  produces a parsable object on stdout with all human-readable output suppressed. Errors still produce a JSON object with  `ok: false` , so stdout is always a valid document.  
 Config keys  
  
   
    
    Key  
    Type  
    Default  
    
   
   
    
    `ignore.rules`  
    `string[]`  
    `[]`  
    
    
    `ignore.files`  
    `string[]`  
    `[]`  
    
    
    `ignore.overrides`  
    `{ files, rules? }[]`  
    `[]`  
    
    
    `lint`  
    `boolean`  
    `true`  
    
    
    `verbose`  
    `boolean`  
    `false`  
    
    
    `diff`  
    `boolean | string`  
     
    
    
    `failOn`  
    `"error" | "warning" | "none"`  
    `"none"`  
    
    
    `customRulesOnly`  
    `boolean`  
    `false`  
    
    
    `share`  
    `boolean`  
    `true`  
    
    
    `offline`  
    `boolean`  
    `false`  
    
    
    `textComponents`  
    `string[]`  
    `[]`  
    
    
    `rawTextWrapperComponents`  
    `string[]`  
    `[]`  
    
    
    `serverAuthFunctionNames`  
    `string[]`  
    `[]`  
    
    
    `respectInlineDisables`  
    `boolean`  
    `true`  
    
    
    `adoptExistingLintConfig`  
    `boolean`  
    `true`  
    
    
    `ignore.tags`  
    `string[]`  
    `[]`  
    
   
  
 `textComponents`  is the broad escape hatch for  `rn-no-raw-text`  — list components that themselves behave like React Native's  `<Text>`  (custom  `Typography` ,  `NativeTabs.Trigger.Label` , etc.) and the rule will treat them as text containers regardless of what their children look like.  
 `rawTextWrapperComponents`  is the narrower option for components that are not text elements but safely route string-only children through an internal  `<Text>`  (e.g.  `heroui-native` 's  `Button` , which stringifies its children and renders them through a  `ButtonLabel` ). Listed wrappers suppress  `rn-no-raw-text`  only when their children are entirely stringifiable. A wrapper with mixed children — e.g.  `<Button>Save<Icon /></Button>`  — still reports because the wrapper can't safely route raw text alongside a sibling JSX element.  
 `serverAuthFunctionNames`  teaches  `server-auth-actions`  about custom auth guards your codebase wraps around its auth library (e.g.  `requireWorkspaceMember` ,  `ensureSignedIn` ). Listed names are accepted as a valid top-of-action auth check whether called bare ( `requireWorkspaceMember()` ) or as a member ( `guards.requireWorkspaceMember()` ), and — unlike the built-in default list — are treated as distinctive so the receiver is not re-validated.  
 `ignore.tags`  suppresses entire categories of rules by tag. For example,  `"tags": ["design"]`  disables all opinionated design rules (gradient text, pure black backgrounds, side tab borders, default Tailwind palettes). Available tags:  `"design"` .  
 `offline`  skips the score API entirely — no score is shown and no share URL is generated. Automatically enabled in CI environments (GitHub Actions, GitLab CI, CircleCI) so CI runs don't depend on the network.  
 React Native rules in mixed monorepos  
 `rn-*`  rules respect per-package boundaries automatically. In a mixed React Native + web monorepo ( `apps/mobile`  alongside  `apps/web`  /  `apps/vite-app`  /  `packages/storybook`  /  `apps/docs` ), every  `rn-*`  rule walks up to the file's nearest  `package.json`  before running:  
  
  Packages that declare  `react-native` ,  `react-native-tvos` ,  `expo` ,  `expo-router` ,  `@expo/*` ,  `react-native-windows` ,  `react-native-macos` , anything under the  `@react-native/`  or  `@react-native-`  namespaces ( `@react-native-firebase/app` ,  `@react-native-async-storage/async-storage` , …), or Metro's top-level  `"react-native"`  resolution field → rules ON.  
  Packages that declare a web-only framework ( `next` ,  `vite` ,  `react-scripts` ,  `gatsby` ,  `@remix-run/*` ,  `@docusaurus/*` ,  `@storybook/*` , or plain  `react-dom`  without an RN sibling) → rules OFF.  
  Packages with no clear local signal → fall back to the project-level framework detection.  
  
 File extensions override the package classification when they're unambiguous:  `*.web.tsx`  /  `*.web.jsx`  are always skipped (Metro resolves these only against  `react-native-web` );  `*.ios.tsx`  /  `*.android.tsx`  /  `*.native.tsx`  are always scanned (mobile-only).  
 The detection is bidirectional: a web-rooted monorepo (root  `package.json`  declares  `next`  or  `vite` ) still loads the  `rn-*`  rules when any workspace targets React Native — the file-level boundary then keeps them silent on the web workspaces and active on the mobile ones.  
 `rn-no-raw-text`  additionally short-circuits raw text inside platform-fork branches:  
  
  `if (Platform.OS === "web") { … }`  consequent — and the  `else`  branch of  `if (Platform.OS !== "web")` .  
  `Platform.OS === "web" ? <X /> : …`  ternaries,  `Platform.OS === "web" && <X />`  short-circuits, and the reversed-operand form  `"web" === Platform.OS` .  
  `switch (Platform.OS) { case "web": … }`  case bodies (other cases still report).  
  `Platform.select({ web: <X />, default: <Y /> })`  — only the  `web`  arm is exempt.  
  `Platform?.OS === "web"`  (optional chain) and  `Platform.OS! === "web"`  (TS non-null assertion) parse the same way as the bare form.  
  
 The walker stops at function and  `Program`  boundaries — JSX defined inside a callback hoisted out of a  `Platform.OS`  branch does not inherit the parent guard. Negative platform checks like  `Platform.OS === "ios"`  are deliberately NOT treated as web exemptions; only the explicit web branch is.  
 Scoring  
 The health score formula:  `100 - (unique_error_rules x 1.5) - (unique_warning_rules x 0.75)` .  
 Scoring runs on react.doctor's API and is  `network-dependent` : without a successful API round-trip (or under  `--offline` ) the score is omitted and the rest of the report still renders normally. Key details:  
  
  The score counts  `unique rules triggered` , not total instances. Fixing 49 of 50  `no-barrel-import`  violations does not change the score; fixing all 50 removes the 0.75 penalty for that rule.  
  Error-severity rules cost 1.5 points each. Warning-severity rules cost 0.75 points each.  
  Category breakdowns shown in the output are for display only and do not weight the score.  
  
 Score labels: 75+ is  `Great` , 50 to 74 is  `Needs work` , under 50 is  `Critical` .  
 Scores may decrease across releases as new rules are added. Each new rule that fires in your codebase introduces an additional penalty. This is expected — it means the tool is catching more issues, not that your code got worse. Pin to a specific react-doctor version in CI if you need stable scores across upgrades.  
 Diff and staged modes  
 React Doctor can scan only changed files instead of the full project:  
  
  `--diff [base]`  scans files changed vs a base branch. Auto-detects  `main`  /  `master` , or pass an explicit branch:  `--diff develop` . Also available as a config key:  `"diff": true`  or  `"diff": "develop"` .  
  `--staged`  scans only files in the git staging area (index). Designed for pre-commit hooks — materializes staged file contents into a temp directory so the scan reflects exactly what will be committed.  
  `--full`  forces a full scan, overriding any  `diff`  value in config or CLI.  
  
 When on a feature branch without explicit flags, you'll be prompted: "Only scan changed files?" This prompt is suppressed in CI,  `--json`  mode, and non-interactive environments.  
 `--staged`  and  `--diff`  cannot be combined.  
 Agent and CI integration  
 React Doctor detects 50+ coding agents (Claude Code, Cursor, Codex, OpenCode, Windsurf, and more) and adapts its behavior automatically:  
  
  Install for agents :  `npx react-doctor@latest install`  writes agent-specific rule files ( `SKILL.md` ,  `AGENTS.md` , .cursorrules) into your project so agents learn React best practices.  
  JSON output :  `--json`  produces a structured  `JsonReport`  on stdout. Errors still produce a valid JSON document with  `ok: false` . Use  `--json-compact`  for minimal whitespace.  
  Score-only output :  `--score`  outputs just the numeric score (0-100), useful for threshold checks in agent loops.  
  GitHub Actions annotations :  `--annotations`  emits  `::error`  /  `::warning`  format for inline PR annotations.  
  Exit codes :  `--fail-on error`  (default) exits non-zero when error-severity diagnostics are found. Use  `--fail-on warning`  or  `--fail-on none`  to tune CI gating.  
  Programmatic API :  `import { diagnose } from "react-doctor/api"`  for direct integration in scripts and automation.  
  
 In CI environments, prompts are automatically skipped and  `--offline`  is implied (no network round-trip; score is omitted from the output).  
 Node.js API  
 ```javascript
import { diagnose, toJsonReport, summarizeDiagnostics } from "react-doctor/api";

const result = await diagnose("./path/to/your/react-project");

console.log(result.score); // { score: 82, label: "Great" } or null
console.log(result.diagnostics); // Diagnostic[]
console.log(result.project); // detected framework, React version, etc.
```
  
 `diagnose`  accepts a second argument:  `{ lint?: boolean }` .  
 `const report = toJsonReport(result, { version: "1.0.0" });`
`const counts = summarizeDiagnostics(result.diagnostics);`
  
 `react-doctor/api`  re-exports  `JsonReport` ,  `JsonReportSummary` ,  `JsonReportProjectEntry` ,  `JsonReportMode` , plus the lower-level  `buildJsonReport`  and  `buildJsonReportError`  builders. See  `packages/react-doctor/src/api.ts`  for the full types.  
 Leaderboard  
 Top React codebases scanned by React Doctor, ranked by score. Updated automatically from  millionco/react-doctor-benchmarks .  
  
  
  
   
    
    #  
    Repo  
    Score  
    
   
   
    
    1  
    executor  
    94  
    
    
    2  
    nodejs.org  
    86  
    
    
    3  
    tldraw  
    70  
    
    
    4  
    t3code  
    68  
    
    
    5  
    better-auth  
    64  
    
    
    6  
    excalidraw  
    63  
    
    
    7  
    mastra  
    63  
    
    
    8  
    payload  
    60  
    
    
    9  
    typebot  
    57  
    
    
    10  
    plane  
    56  
    
   
  
  
 See the  full leaderboard .  
 Resources & Contributing Back  
 Want to try it out? Check out  the demo .  
 Looking to contribute back? Clone the repo, install, build, and submit a PR.  
 ```bash
git clone https://github.com/millionco/react-doctor
cd react-doctor
pnpm install
pnpm build
node packages/react-doctor/bin/react-doctor.js /path/to/your/react-project
```
  
 Find a bug? Head to the  issue tracker .  
 License  
 React Doctor is MIT-licensed open-source software.

---

## 14. [playcanvas/supersplat](https://github.com/playcanvas/supersplat)

> [→ GitHub 連結](https://github.com/playcanvas/supersplat)

3D Gaussian Splat Editor SuperSplat Editor  
          
 |  SuperSplat Editor  |  User Guide  |  Blog  |  Forum  |  
 The SuperSplat Editor is a free and open source tool for inspecting, editing, optimizing and publishing 3D Gaussian Splats. It is built on web technologies and runs in the browser, so there's nothing to download or install.  
 A live version of this tool is available at:  https://superspl.at/editor  
  
 To learn more about using SuperSplat, please refer to the  User Guide .  
 Local Development  
 To initialize a local development environment for SuperSplat, ensure you have  Node.js  18 or later installed. Follow these steps:  
  
    Clone the repository:   `git clone https://github.com/playcanvas/supersplat.git`
`cd supersplat`
    
    Install dependencies:   `npm install`
    
    Build SuperSplat and start a local web server:   `npm run develop`
    
    Open a web browser tab and make sure network caching is disabled on the network tab and the other application caches are clear:  
    
    On Safari you can use  `Cmd+Option+e`  or Develop->Empty Caches.  
    On Chrome ensure the options "Update on reload" and "Bypass for network" are enabled in the Application->Service workers tab:  
        
    Navigate to  `http://localhost:3000`    
  
 When changes to the source are detected, SuperSplat is rebuilt automatically. Simply refresh your browser to see your changes.  
 Localizing the SuperSplat Editor  
 The currently supported languages are available here:  
 https://github.com/playcanvas/supersplat/tree/main/static/locales  
 Adding a New Language  
  
    Add a new  `<locale>.json`  file in the  `static/locales`  directory.    
    Add the locale to the list here:   https://github.com/playcanvas/supersplat/blob/main/src/ui/localization.ts    
  
 Testing Translations  
 To test your translations:  
  
    Run the development server:   `npm run develop`
    
    Open your browser and navigate to:   `http://localhost:3000/?lng=<locale>`
   Replace  `<locale>`  with your language code (e.g.,  `fr` ,  `de` ,  `es` ).    
  
 Contributors  
 SuperSplat is made possible by our amazing open source community:
