---
title: "2026/05/26 本週 GitHub AI 趨勢"
date: 2026-05-26
draft: false
tags: ["GitHub趨勢", "AI週報", "AI代理", "LLM應用", "程式碼智慧", "邊緣AI"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---

From the top 15 GitHub Trending projects this week, **14** AI/LLM-related projects have been selected:

---

## 1. [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)

> [→ GitHub Link](https://github.com/colbymchenry/codegraph)

CodeGraph is a pre-indexed code knowledge graph specifically designed for AI code agents (such as Claude Code, Cursor, Codex, etc.). Traditionally, AI agents exploring codebases rely on expensive and time-consuming file scanning tools (like grep, glob, Read), which not only consume a large number of tokens but also extend processing time. CodeGraph's core value lies in enabling agents to query instantly, rather than repeatedly scanning, by building knowledge like symbol relationships, call graphs, and code structures. It claims to save approximately 35% on costs, reduce tool calls by 70%, and speed up processing by 46%, with all operations executed 100% locally, balancing efficiency and privacy. For teams developing large projects, CodeGraph can significantly boost the efficiency of AI-assisted development, representing an important direction for optimizing LLM applications in software engineering.

---

## 2. [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)

> [→ GitHub Link](https://github.com/tinyhumansai/openhuman)

OpenHuman is an open-source personal AI super-intelligence agent designed to deeply integrate into a user's daily workflow. It addresses many of the "cold start" pain points of AI assistants by automatically fetching and compressing data from 118+ third-party services (e.g., Gmail, Notion, GitHub), storing it locally as a "memory tree" and Obsidian-compatible Markdown files. This local-first memory mode ensures user data privacy and allows the AI agent to gain comprehensive context within minutes, eliminating lengthy training periods. Furthermore, OpenHuman's built-in intelligent token compression technology (TokenJuice) significantly reduces costs and latency. Its one-stop solution (including web search, code toolkit, voice capabilities) makes it a noteworthy option for developers seeking an efficient, private, and powerful AI assistant.

---

## 3. [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything)

> [→ GitHub Link](https://github.com/Lum1104/Understand-Anything)

Understand-Anything is a Claude Code plugin that can convert any codebase, knowledge base, or document into an interactive knowledge graph. For developers joining new teams or facing large projects, it solves the challenge of quickly understanding complex systems. This project uses a multi-agent pipeline, combining `tree-sitter` for structural analysis with LLMs for semantic understanding, to automatically build a knowledge graph including files, functions, classes, and dependencies, and provides a visual dashboard. Its unique features, such as "guided tours," "diff impact analysis," and "hierarchical visualization," help users grasp code structure and business logic from a macro to a micro level. The generated graph can be shared as a JSON file with the team, greatly improving team collaboration and the learning efficiency of new members, making it a powerful tool for boosting developer productivity.

---

## 4. [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

> [→ GitHub Link](https://github.com/Imbad0202/academic-research-skills)

Academic Research Skills (ARS) is a suite of academic research skills designed for Claude Code, covering the complete workflow from research, writing, to reviewing, revision, and finalization. It addresses many common issues of AI in academic writing, such as hallucinations, corner-cutting, and catering to humans. The core philosophy of ARS is "AI assists, not replaces, humans," handling tedious tasks like citation formatting, data verification, and logical consistency checks, while encouraging critical thinking from human researchers through features like "Opponent's Agreement" and "Intent Detection Layer." Its emphasis on human-computer collaboration, phased validation, and detailed versioning makes it a paradigm for developing highly reliable AI-assisted tools, especially in the rigorous academic field, providing deep insights into responsible AI applications.

---

## 5. [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)

> [→ GitHub Link](https://github.com/rohitg00/ai-engineering-from-scratch)

AI Engineering From Scratch is a comprehensive and practice-oriented AI engineering course, comprising 435 lessons, 20 stages, and approximately 320 hours of learning content. It aims to bridge the gap between theoretical knowledge and professional application, using a "from scratch" teaching philosophy to guide learners from mathematical fundamentals to building every AI algorithm by hand, rather than just calling APIs. The course covers a wide range of topics from linear algebra to autonomous agent collectives, with each lesson culminating in reusable artifacts (e.g., prompts, skills, agents) that form a personal portfolio. Notably, it integrates AI code agents to provide personalized learning paths and quizzes, making the learning process more interactive and efficient. This course is undoubtedly a valuable resource for engineers who wish to deeply understand and build AI systems themselves.

---

## 6. [ruvnet/RuView](https://github.com/ruvnet/RuView)

> [→ GitHub Link](https://github.com/ruvnet/RuView)

RuView is a revolutionary WiFi sensing platform that transforms ordinary WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection capabilities. It addresses the issues of privacy, line-of-sight limitations, and user compliance associated with traditional sensing technologies (such as cameras and wearables). By utilizing Channel State Information (CSI) captured by ESP32 sensors, RuView can detect people indoors, measure breathing and heart rate, and even perform activity recognition and fall detection through walls, without cameras or wearables. Its localized edge computing (ESP32 + Cognitum Seed) and open-source nature, coupled with integration into mainstream smart home ecosystems, give it enormous potential in healthcare, retail, and security monitoring, offering an innovative and privacy-focused environmental sensing solution.

---

## 7. [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

> [→ GitHub Link](https://github.com/rohitg00/agentmemory)

Agentmemory is a persistent memory solution specifically designed for AI code agents, inspired by Karpathy's LLM Wiki pattern, aimed at solving the common "amnesia" problem agents face between sessions. Traditionally, users constantly have to repeat explanations of project architecture and preferences. Agentmemory silently captures agent interactions like tool usage and prompts, compresses them into searchable memories (facts, concepts, knowledge graphs), and injects relevant context at the start of the next session. This significantly boosts agent efficiency and coherence. Its hybrid search (BM25 + vector + graph), four-layer memory integration mechanism, and broad support for various AI agents (e.g., Claude Code, Cursor, Gemini CLI) make it a key tool for enabling AI assistants to truly possess long-term, evolvable intelligence.

---

## 8. [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser)

> [→ GitHub Link](https://github.com/CloakHQ/CloakBrowser)

CloakBrowser is a Chromium browser with stealth capabilities, modifying fingerprints at the C++ source code level to pass various bot detection tests. It addresses the issue of traditional automation tools (like Playwright, Puppeteer) being easily identified by anti-bot systems due to JavaScript injection or configuration-level modifications. CloakBrowser has 58 source code patches built-in, covering multiple fingerprint parameters such as Canvas, WebGL, audio, and GPU, making its behavior indistinguishable from a real browser. It achieves a human-level score of 0.9 on reCAPTCHA v3 and passes Cloudflare Turnstile and other challenges. Additionally, the "humanize=True" option can simulate human mouse, keyboard, and scrolling behavior, making it a powerful tool for AI agents and automation tasks that require reliable website interaction, providing a more robust solution for legitimate web scraping and automation.

---

## 9. [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic)

> [→ GitHub Link](https://github.com/supertone-inc/supertonic)

Supertonic is an ultra-fast, localized, and multilingual text-to-speech (TTS) system that runs natively on devices via ONNX Runtime. It solves the latency, cost, and privacy issues associated with traditional high-quality TTS relying on cloud services. Supertonic's core advantage lies in its lightweight (99M parameter) model, which can generate high-quality 44.1kHz audio with extremely low latency on desktops, mobile devices, and even edge devices like Raspberry Pi, supporting 31 languages. It requires no GPU and can handle complex text content (such as financial expressions, phone numbers, and technical units), even offering emotion tags to enhance speech naturalness. Supertonic and its multi-runtime SDK examples (Python, Node.js, Browser, iOS, etc.) make it a highly attractive solution for developers seeking real-time, private, and efficient voice applications.

---

## 10. [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)

> [→ GitHub Link](https://github.com/can1357/oh-my-pi)

Oh-My-Pi (omp) is a terminal AI code agent, forked from Mario Zechner's Pi project, significantly enhanced with a deeply integrated development toolchain and a code-first workflow. Omp addresses many pain points where AI agents in actual development lack deep integration with LSP, debuggers, and real shells. It embeds IDE intelligence (e.g., semantic refactoring, error diagnostics) and efficient native tools (e.g., ripgrep, glob) into the agent process, and introduces innovative features like "content-hash anchored editing," significantly improving editing precision and saving tokens. Its support for sub-agents, multi-backend web search, and the intelligent memory system "Hindsight" makes it a feature-rich, high-performance autonomous software engineering platform, designed to enable AI agents to execute complex development tasks more efficiently.

---

## 11. [dograh-hq/dograh](https://github.com/dograh-hq/dograh)

> [→ GitHub Link](https://github.com/dograh-hq/dograh)

Dograh is an open-source, self-hostable voice agent platform designed to be an alternative to proprietary solutions like Vapi and Retell. It addresses vendor lock-in, per-minute billing, and limited customization issues associated with proprietary platforms. Dograh offers complete source code control and transparency, allowing developers to integrate their own LLM, TTS, and STT models, and build a working voice bot in two minutes via a drag-and-drop workflow builder. Its Python-based and Docker-first architecture ensures consistent and flexible deployment. For teams seeking autonomy, cost-effectiveness, and deep customization, Dograh's open-source commitment and powerful features make it an ideal choice for building production-grade voice agents.

---

## 12. [presenton/presenton](https://github.com/presenton/presenton)

> [→ GitHub Link](https://github.com/presenton/presenton)

Presenton is an open-source AI presentation generator and API, aiming to provide a self-hosted alternative to tools like Gamma and Beautiful AI. It addresses common problems with proprietary presentation tools such as subscription lock-in, limited model choices, and insufficient data control. Presenton's core value lies in giving users complete control over their AI presentation workflow, supporting various LLM and image generation models (e.g., OpenAI, Gemini, Ollama), and allowing the use of custom HTML/Tailwind CSS templates. Whether deployed via Docker or run as an Electron desktop application, Presenton allows users to maintain data privacy and flexible customization. Its ability to generate editable PPTX files, and the option to deploy as an API service, make it an ideal choice for individuals and teams seeking autonomy, flexible design, and reduced costs.

---

## 13. [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)

> [→ GitHub Link](https://github.com/HKUDS/CLI-Anything)

CLI-Anything aims to make all software "agent-native" by automatically generating CLI scripts, solving the challenges AI agents face when operating real professional software. Many AI agents excel at reasoning but struggle to effectively utilize actual applications, as traditional UI automation is fragile and API support is limited. CLI-Anything creates full-featured, structured, and reliable CLI interfaces for any codebase through a seven-stage automation process, enabling precise control by AI agents. The project's CLI-Hub allows agents to autonomously discover, install, and manage these CLIs. Its rigorous testing on 18 different professional software (e.g., GIMP, Blender, LibreOffice), with over 2,330 tests, demonstrates its immense potential in transforming human-designed software into AI-agent-native tools, making it a critical infrastructure for achieving truly autonomous agents.

---

## 14. [obra/superpowers](https://github.com/obra/superpowers)

> [→ GitHub Link](https://github.com/obra/superpowers)

Superpowers is a software development methodology and skill framework specifically designed for AI code agents (such as Claude Code, Cursor, Gemini CLI, etc.). It addresses the common problem of AI agents "blindly writing code" or operating out of context. By providing a set of composable skills and instructions, it forces agents to "brainstorm" to clarify requirements and produce design documents before starting work. After human confirmation, it strictly adheres to "Test-Driven Development (TDD)" and "Subagent-driven-development" processes. This enables AI to break down complex tasks into small increments and verify them step-by-step, even operating autonomously for several hours without deviating from the goal. For developers who wish to constrain AI agent behavior and significantly improve the quality of generated code and project stability, this is a powerful plugin that can transform AI into a rigorous engineer.
