---
title: "2026/11/22 本週 GitHub AI 趨勢"
date: 2026-11-22
draft: false
tags: ["GitHub趨勢", "AI週報", "開源專案", "AI工具", "開發者工具"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---

本週從 GitHub Trending 前 15 名中，篩選出 **13 個** AI/LLM 相關專案：

---

## 1. [backnotprop/plannotator](https://github.com/backnotprop/plannotator)

> [→ GitHub 連結](https://github.com/backnotprop/plannotator)

Plannotator 是為 AI Coding Agent（如 Claude Code、Codex）打造的本地視覺化審查工作台。當 Agent 提出執行計畫、修改程式碼或產出 Artifact 時，它會喚起瀏覽器介面，讓開發者直觀地標註文本、審查 diff 並一鍵將回饋送回 Agent 繼續執行。隨著 Agent 走向多步驟自主推理，終端機互動已難以滿足高頻的審查需求；Plannotator 補齊了 Human-in-the-loop 關鍵的體驗斷層，大幅降低了與 Agent 協作的認知負擔。

---

## 2. [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)

> [→ GitHub 連結](https://github.com/google-labs-code/stitch-skills)

Stitch Skills 是 Google Labs 基於 Agent Skills 開放標準與 MCP 架構推出的技能庫，專門對接 Google Stitch。它讓 Cursor、Claude Code 等 Coding Agent 能無縫串聯 UI 設計與代碼生成，涵蓋設計系統提取、畫面變體生成及 React/React Native 代碼轉換。此專案值得關注在於它示範了 MCP 與模組化技能的結合：Agent 不再只是被動補全代碼，而是能透過結構化規範雙向協同設計與工程，是 AI 輔助前端開發邁向端到端自動化的重要演進。

---

## 3. [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

> [→ GitHub 連結](https://github.com/GoogleChrome/modern-web-guidance-src)

由 Google Chrome 與 MDN 等團隊打造的 Modern Web Guidance，旨在解決 AI Coding Agent 因訓練資料滯後而頻繁生成過時、臃腫前端代碼的痛點。專案涵蓋現代瀏覽器原生 API（如 View Transitions、Popover），透過輕量本機檢索在 Agent 生成時動態注入最佳實踐與相容性建議。它展示了標準組織如何以「Agent Skill」主動校準模型知識，實測能顯著拉高代碼品質與通過率，是改善 Coding Agent 實用性極佳的示範。

---

## 4. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

> [→ GitHub 連結](https://github.com/alibaba/open-code-review)

Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible. https://open-codereview.ai  
       
  OpenCodeReview  
  
          
                
              
                  
  English |  简体中文  |  日本語  |  한국어  |  Русский    
  
 What is Open Code Review?  
 Open Code Review is an AI-powered code review CLI tool. It originated as Alibaba Group's internal official AI code review assistant — over the past two years, it has served tens of thousands of developers and identified millions of code defects. After thorough validation at massive scale, we incubated it into an open source project for the community. Simply configure a model endpoint to get started.  
 It reads Git diffs, sends changed files to a configurable LLM via an agent with tool-use capabilities, and generates structured review comments with line-level precision. The agent can read full file contents, search the codebase, inspect other changed files for context, and produce deep reviews — not just surface-level diff feedback. Beyond diff review,  ocr scan  reviews entire files for auditing unfamiliar codebases or directories that have no meaningful diff.  
 Visit the  official website  for more details.  
  
 Benchmark  
  
  Compared to general-purpose agents (Claude Code), Open Code Review achieves significantly higher  Precision  and  F1  with the same underlying model, while consuming only  ~1/9 of the tokens  and completing reviews faster. Note that its Recall is lower than general-purpose agents — a deliberate trade-off favoring precision over noise.  
  
 A real-world code review benchmark built from  50  popular open-source repositories,  200  real Pull Requests, and  10  programming languages — cross-validated by 80+ senior engineers ( 1,505  annotated ground-truth issues).  
  Explore the AACR-Bench dataset on Hugging Face .  
  
   
    
    Metric  
    What it measures  
    Why it matters  
    
   
   
    
    F1  
    Harmonic mean of precision and recall  
    Best single number for overall review quality  
    
    
    Precision  
    Proportion of reported issues that are real defects  
    Higher = fewer false alarms to triage  
    
    
    Recall  
    Proportion of real defects that are found  
    Higher = fewer issues slip through review  
    
    
    Avg Time  
    Wall-clock time per review  
    Matters for CI pipeline latency  
    
    
    Avg Token  
    Total tokens consumed per review  
    Directly impacts API cost  
    
   
  
  
 Why Open Code Review?  
 The Problem with General-Purpose Agents  
 If you've used general-purpose agents like Claude Code with Skills for code review, you've likely encountered these pain points:  
  
  Incomplete coverage  — On larger changesets, agents tend to "cut corners," selectively reviewing only some files and missing others.  
  Position drift  — Reported issues frequently don't match the actual code location, with line numbers or file references drifting off target.  
  Unstable quality  — Natural-language-driven Skills are hard to debug, and review quality fluctuates significantly with minor prompt variations.  
  
 The root cause: a purely language-driven architecture lacks hard constraints on the review process.  
 Core Design: Deterministic Engineering × Agent Hybrid  
 Open Code Review's core philosophy is to combine deterministic engineering with an agent, each handling what it does best.  
 Deterministic Engineering — Hard Constraints  
 For review steps that  must not go wrong , engineering logic — not the language model — guarantees correctness:  
  
  Precise file selection  — Determines exactly which files need review and which should be filtered, ensuring no important change is missed.  
  Smart file bundling  — Groups related files into a single review unit (e.g.,  message_en.properties  and  message_zh.properties  are bundled together). Each bundle runs as a sub-agent with isolated context — a divide-and-conquer strategy that stays stable on very large changesets and naturally supports concurrent review.  
  Fine-grained rule matching  — Matches review rules to each file's characteristics, keeping the model's attention sharply focused and eliminating information noise at the source. Compared to purely language-driven rule guidance, template-engine-based rule matching is more stable and predictable.  
  External positioning and reflection modules  — Independent comment-positioning and comment-reflection modules systematically improve both the location accuracy and content accuracy of AI feedback.  
  
 Agent — Dynamic Decision-Making  
 The agent's strengths are concentrated where they matter most — dynamic decisions and dynamic context retrieval:  
  
  Scenario-tuned prompts  — Prompt templates deeply optimized for code review, improving effectiveness while reducing token consumption.  
  Scenario-tuned toolset  — Distilled from deep analysis of tool-call traces in large-scale production data — including call frequency distributions, per-tool repetition rates, and the impact of new tools on the overall call chain — resulting in a purpose-built toolset that is more stable and predictable for code review than a generic agent toolkit.  
  
 How to Use  
 Prerequisites  
  
  Git >= 2.41  — Open Code Review relies on Git for diff generation, code search, and repository operations.  
  
  
 Agent Skills  
 Use the skills in Claude Code, Codex, Cursor, Kimi Code, or another agent that supports Agent Skills and can run local commands. Both modes require  Git >= 2.41  and the  ocr  CLI ; only native mode requires an OCR model provider.  
 1. Install the Skills  
 Run in the project you want to review, then select the skills you need and your agent in the installer:  
 npx skills add alibaba/open-code-review
  
 The skills guide your agent to install  ocr  if it is missing, subject to your environment's permissions. You can also install it ahead of time with  npm install -g @alibaba-group/open-code-review . Prefer a plugin or manual installation? See the  agent-specific setup guide , or copy the desired folders from  skills/  into your agent's skill directory.  
 2. Choose a Review Mode  
  
   
    
     
    Native mode  
    Delegation mode  
    
   
   
    
    Skill  
    open-code-review  
    open-code-review-delegate  
    
    
    Who reviews?  
    OCR's specialized review agent and pipeline  
    Your current coding agent, following OCR's review pipeline and guardrails  
    
    
    Model and authentication  
    OCR's own provider configuration  
    Your host agent's existing model and authentication  
    
    
    Choose it when  
    You have a model endpoint for OCR and want its full review pipeline  
    You have no separate API key, or want to use your existing agent subscription/setup  
    
   
  
 No separate key? Start with delegation mode.  It skips OCR provider setup, not the host agent's own authentication, usage limits, or costs. A host-agent subscription is not automatically an API credential for native mode. In delegation mode, OCR's CLI and skill together provide the review pipeline and guardrails: file selection, rule resolution, coverage requirements, and structured reporting. The host agent performs analysis, positioning, and reporting within that workflow; it does not run OCR's full native pipeline.  
 For native mode, configure a provider once with  ocr config provider  and  ocr config model . Authentication depends on the provider; see  Configuration .  
 CLI  
 Install  
 npm install -g @alibaba-group/open-code-review
  
 After installation, the  ocr  command is available globally.  
 For other installation methods (install script, GitHub Release binary, from source), see  Installation .  
 Quick Start  
 1. Configure LLM  
 You must configure an LLM before reviewing code, unless you use  Delegation Mode .  
  
  OCR calls the model:   ocr review , the  /open-code-review:review  command, and the  open-code-review  skill use OCR's own provider configuration, not your Claude Code Team/Pro subscription login. Authentication requirements depend on the provider; see  Configuration .  
  The host agent calls the model:  the  /open-code-review:delegate-review  command and the  open-code-review-delegate  skill use the host agent's configured model and authentication. No separate LLM configuration or credentials are needed in OCR. See the  Claude Code install steps .  
  
 ocr config provider          # Select a built-in provider or add a custom one
ocr config model             # Pick a model for the active provider
  
  
 The interactive UI guides you through provider selection, API key entry, and model configuration, then automatically tests connectivity.  
 For CLI setup, environment variables, custom providers, and other advanced configuration, see  Configuration .  
 2. Review  
 cd your-project

# Workspace mode — review all staged, unstaged, and untracked changes
ocr review

# Current branch — review changes since it diverged from main (--to defaults to HEAD)
ocr review --from main

# Branch range — reviews feature-branch's changes since it diverged from main (merge-base mode)
ocr review --from main --to feature-branch

# Single commit
ocr review --commit abc123

# Resume an interrupted range or commit review
ocr session list
ocr review --from main --to feature-branch --resume <session-id>

# Full-file scan — review whole files instead of a diff (no git history needed)
ocr scan                          # scan the entire repository
ocr scan --path internal/agent    # scan a directory or specific files
ocr scan --resume <session-id>   # resume an interrupted full-file scan

# Save results to a file (recommended for AI host agents)
ocr review --format json --output result.json

# Delegation mode — let your AI coding agent perform the review itself
# OCR handles file selection and rule resolution; no LLM configuration needed
ocr delegate preview
ocr delegate rule src/main.go src/handler.go
  
 Documentation  
 Full documentation lives at  open-codereview.ai/docs :  
  
  Quickstart  — install and run your first review  
  Installation  — all platforms and package managers  
  CLI Reference  — every command and flag  
  Review Rules  — customize review rules with path filtering and targeting  
  Configuration  — config keys and environment variables  
  MCP Server  — extend the review agent with external tools  
  Coding Agent Integrations — choose the platform you use 
    
    Claude Code  — install a plugin with review slash commands  
    Codex  — install a plugin with callable review skills  
    Cursor  — install a plugin with portable review skills  
    Kimi Code  — install a plugin with review slash commands and skills  
    OpenCode  — install native review tools and slash commands  
    QCA Forward  — run delegation mode with the QCA host model and a ready-to-publish template  
    Skill-compatible agents  — install the portable agent skill  
      
  Review Execution Modes — after integration, choose which LLM performs the review 
    
    Default (OCR-managed)  — OCR runs the review using its configured LLM  
    Delegation Mode  — your coding agent runs the review using its own LLM; no OCR API key required  
      
  CI/CD Integration  — GitHub Actions, GitLab CI, GitFlic CI, and Gerrit integration  
  Session Viewer  — browse and replay review sessions in browser, mark comments as fixed or ignored and hide them while you work through the findings  
  Telemetry  — OpenTelemetry integration for observability  
  FAQ  — common questions and troubleshooting  
  
 Contributing  
 This project exists thanks to all the people who contribute. See  CONTRIBUTING.md  for development setup, coding guidelines, and how to submit pull requests.  
      
 License  
 Apache-2.0  — Copyright 2026 Alibaba

---

## 5. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

> [→ GitHub 連結](https://github.com/mvanhorn/last30days-skill)

last30days-skill 是專為 Claude Code、Cursor 等 Agent 打造的深度研究技能。傳統搜尋常受限於 SEO 農場文與平台壁壘，難以捕捉真實社群動態；該專案平行檢索 Reddit、X、YouTube、HN 與 Polymarket 過去 30 天的內容，改以互動量、留言與預測市場賠率加權排序。在技術瞬息萬變的 AI 領域，它打破各平台封閉花園，讓 Agent 即時提煉出高訊噪比的第一線反饋，是目前 Agentic Search 相當務實且具啟發性的落地實踐。

---

## 6. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

> [→ GitHub 連結](https://github.com/ChromeDevTools/chrome-devtools-mcp)

Chrome DevTools MCP 是 Google 官方推出的 MCP 伺服器，讓 Cursor、Claude Code 等 AI Coding Agent 能直接操控並檢視活體 Chrome 瀏覽器。過去 AI 開發前端多依賴靜態程式碼推斷或單純截圖，該專案透過 Puppeteer 與 DevTools 深度整合，使 Agent 具備讀取 Source-mapped 報錯、監控網路流量及診斷效能瓶頸（如 LCP 與記憶體洩漏）的能力。這標誌著 AI 輔助開發真正跨入「實時除錯與閉環驗證」的新階段，是當前 Agent 生態不可忽視的基建利器。

---

## 7. [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)

> [→ GitHub 連結](https://github.com/tradermonty/claude-trading-skills)

tradermonty/claude-trading-skills 是一個專為個人投資者設計的 Claude Skills 交易工作流工具包。它解決了散戶缺乏時間與紀律的痛點，不將買賣決策外包給 AI，而是透過市場分析、風控熔斷與交易日誌覆盤，為人為決策建立結構化流程。在 AI/LLM 領域，這項專案極具參考價值。它示範了如何利用 Anthropic 的 Claude Skills 構建高模組化的 Agent 系統，透過明確的 YAML 規範、狀態機門控與彈性 API 整合，展現了 LLM 在高風險專業領域中作為邏輯嚴密的「協作 Copilot」而非盲目自動化代理的落地路徑。

---

## 8. [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)

> [→ GitHub 連結](https://github.com/ag-ui-protocol/ag-ui)

AG-UI 是一個專為 AI Agent 與前端應用打造的開放式事件導向協定。由於 Agent 涉及流式 Token、中間工具調用與狀態同步，傳統 API 難以規範。AG-UI 透過雙向事件流將這些互動標準化，讓任何 Agent 能輕鬆對接 Web、行動端或 Slack。

在 LLM 生態中，相較於 MCP 解決 Agent 調用工具，AG-UI 補齊了 Agent 到使用者介面的最後一哩路。它將 UI 與後端框架解耦，解決前端重複開發問題，是構建跨平台 Agent 應用的重要基石。

---

## 9. [meta/astryx](https://github.com/meta/astryx)

> [→ GitHub 連結](https://github.com/meta/astryx)

meta/astryx 是 Meta 開源的設計系統，源於內部八年淬鍊並支援了上萬個應用。它解決了傳統元件庫 API 封閉、樣式強烈綁定與設定繁瑣的痛點，既不強制綁定特定 CSS 框架，也讓開發者能直接抽換底層元件細節。更值得 AI 社群關注的是其「Agent-Ready」設計：透過 CLI 會自動產生 AGENTS.md 等脈絡文件，讓 Claude 或 Cursor 等 Coding Agent 在生成前端程式碼時有明確的規範可循，有效減少 AI 瞎猜與壞碼，真正實現人與 AI 共用同一套 UI 設計語言。

---

## 10. [pookjw/HermesEnabler](https://github.com/pookjw/HermesEnabler)

> [→ GitHub 連結](https://github.com/pookjw/HermesEnabler)

Enable Hermès Watch Faces on any Apple Watch devices HermesEnabler 2  
 English  ·  Tiếng Việt  ·  한국어  ·  简体中文  ·  繁體中文  ·  日本語  ·  Español  ·  Français  ·  Deutsch  ·  Português  
  
  
  Supported on watchOS 27.0 through 27.3 beta 1. If you’re using an unsupported watchOS version, use  Clocky .  
  
 Installation  
 macOS  
 On macOS you can install the prebuilt IPA with Sideloadly or build the app directly with Xcode. Either way, the iPhone must be paired with the target Apple Watch, and the Watch must run a supported watchOS version.  
 Install the IPA  
  
  Download the IPA from  Releases .  
  Install  Sideloadly  on your Mac, connect your iPhone with a cable, and select it in Sideloadly.  
  Drag the IPA into Sideloadly and enter your Apple ID. Turn off  Use automatic bundle ID , set a fixed Bundle Identifier, and start signing.  
  On the iPhone, open  Settings → General → VPN & Device Management  and trust your developer certificate.  
  On the iPhone, open  Settings → Privacy & Security → Developer Mode , turn it on, restart, and confirm.  
  On the iPhone, open the  Watch  app, go to  My Watch → Apps , and install  HermesEnabler2  on the Watch.  
  On the Apple Watch, open  Settings → Privacy & Security → Developer Mode , turn it on, restart, and confirm. If the option is not shown, install the Watch app first and check again.  
  Open  HermesEnabler2  on your Apple Watch and follow the steps in the app.  
  
 Build with Xcode  
  
  Open  HermesEnabler2.xcodeproj  in Xcode.  
  Select your Apple Watch as the run destination and click  Run .  
  Open  HermesEnabler2  on your Apple Watch and follow the steps in the app.  
  
 Windows  
 Windows uses  WatchBridge , a community tool that prepares Developer Mode and installs an IPA containing both an iPhone host app and a Watch app. It is not affiliated with Apple or with this project.  
  
  Install  Apple Mobile Device Service  by installing  iTunes  or the  Apple Devices  app from the Microsoft Store. WatchBridge needs it for USB and Wi-Fi communication. WebView2 is built into Windows 11.  
  Make sure your iPhone is paired with the target Apple Watch. WatchBridge supports only one paired Watch at a time; if more than one is paired, the preparation step stops instead of guessing.  
  Download  watchbridge-windows.zip  from  WatchBridge Releases , extract it, and run  WatchBridge.exe . The executable is unsigned, so Windows SmartScreen may warn on first launch.  
  Download the IPA from  Releases . Use the original IPA that contains both the iPhone host and the  Watch/*.app ; Watch-only packages are not supported.  
  Connect the paired iPhone over USB and select it in WatchBridge.  
  Pair the Watch and confirm the trust prompt on the Watch. Request the  Developer Mode  switch, then on the Watch open  Settings → Privacy & Security → Developer Mode , turn it on, restart, and confirm. Return to WatchBridge and click  Check again . WatchBridge does not enable Developer Mode or restart the Watch for you.  
  Sign in with your Apple ID, select the HermesEnabler2 IPA, and start signing and installation. WatchBridge installs the iPhone host app first, then the Watch app.  
  Open  HermesEnabler2  on your Apple Watch and follow the steps in the app.  
  
  
  Developer-mode preparation requires a USB connection. After pairing over USB once, installs and renewals can use Wi-Fi.  
  
 Cautions  
  
  watchOS 26 is not supported.  
  In Sideloadly, disable  Use automatic bundle ID  and use a fixed Bundle Identifier. Keep the same Bundle Identifier and Apple ID for every update so the app can retain its existing data and backup.  
  If the iPhone app installs but the Watch app does not appear, check the Sideloadly log for  Watch apps will be stripped from the IPA . This means the embedded Watch app was removed; installing the iPhone app alone will not install it. Use Xcode to install the Watch app.  
  Before deleting the app, always restore your MobileGestalt backup through the HermesEnabler2 app.  
  
 Credits  
 This project incorporates code from  Gester .  
 Use at your own risk.

---

## 11. [we-promise/sure](https://github.com/we-promise/sure)

> [→ GitHub 連結](https://github.com/we-promise/sure)

The personal finance app for everyone (by everyone) https://sure.am        
 
   
   
 
  
    Deutsch  |  Español  |  Français  |  日本語  |  한국어  |  Português  |  Русский  |  中文    
 Sure: The personal finance app for everyone  
 Get involved:  Discord  •  Website  •  Issues  
 
  
   
    
   Important 
  This repository is a community fork of the now-abandoned Maybe Finance project.   Learn more in their  final release  doc.  
  
 Backstory  
 The  Maybe Finance  (archived/abandoned repo) team spent most of 2021–2022 building a full-featured personal finance and wealth management app. It even included an “Ask an Advisor” feature that connected users with a real CFP/CFA — all included with your subscription.  
 The business end of things didn't work out, and so they stopped developing the app in mid-2023.  
 After spending nearly $1 million on development (employees, contractors, data providers, infra, etc.), the team open-sourced the app. Their goal was to let users self-host it for free — and eventually launch a hosted version for a small fee.  
 They actually did launch that hosted version … briefly.  
 That also didn’t work out — at least not as a sustainable B2C business — so now here we are: hosting a community-maintained fork to keep the codebase alive and see where this can go next.  
 Join us!  
 Hosting Sure  
 Sure is a fully working personal finance app that can be  self hosted with Docker . Sure can be accessed from a browser, the macOS desktop app, the mobile app, API clients, and LLM agents. See  Sure Clients  for an overview.  
 Forking and Attribution  
 This repo is a community fork of the archived Maybe Finance repo. You’re free to fork it under the AGPLv3 license — but we’d love it if you stuck around and contributed here instead.  
 To stay compliant and avoid trademark issues:  
  
  Be sure to include the original  AGPLv3 license  and clearly state in your README that your fork is based on Maybe Finance but is  not affiliated with or endorsed by  Maybe Finance Inc.  
  "Maybe" is a trademark of Maybe Finance Inc. and therefore, use of it is NOT allowed in forked repositories (or the logo)  
  
 Performance Issues  
 With data-heavy apps, inevitably, there are performance issues. We've set up a public dashboard showing the problematic requests seen on the demo site, along with the stacktraces to help debug them.  
 https://www.skylight.io/app/applications/s6PEZSKwcklL/recent/6h/endpoints  
 Any contributions that help improve performance are very much welcome.  
 Local Development Setup  
 If you are trying to  self-host  the app,  read this guide to get started .  
 The instructions below are for developers to get started with contributing to the app.  
 Requirements  
  
  See  .ruby-version  file for required Ruby version  
  PostgreSQL >9.3 (latest stable version recommended)  
  Redis > 5.4 (latest stable version recommended)  
  
 Getting Started  
 cd sure
cp .env.local.example .env.local
bin/setup
bin/dev

# Optionally, load demo data
rake demo_data:default
  
 Visit  http://localhost:3000  to view the app.  
 If you loaded the optional demo data, log in with these credentials:  
  
  Email:  user@example.com  
  Password:  Password1!  
  
 For further instructions, see guides below.  
 Setup Guides  
  
  Mac dev setup  
  Linux dev setup  
  Windows dev setup  
  Dev containers - visit  this guide  
  
 One-click Install  
 Render expects each button target branch to have a  render.yaml  at the repository root. The branch-ready Blueprint files live in  branches/<branch-name>/render.yaml  in a separate repo and can be copied to each corresponding branch root.  
  
   
    
    Option  
    What it deploys  
    latest  
    stable  
    
   
   
    
    Sure - No AI  
    Sure web, Sidekiq worker, Render Postgres, and Render Key Value. AI tokens are intentionally blank.  
     
     
    
    
    Sure - Simple AI  
    Sure with OpenAI-backed AI settings, pgvector-ready Postgres, Sidekiq, and Render Key Value. Render prompts for the OpenAI token.  
     
     
    
    
    Sure - External AI  
    Sure with external assistant settings plus AlphaClaw, which manages the OpenClaw gateway on Render.  
     
     
    
   
  
  
  
 License and Trademarks  
 Maybe and Sure are both distributed under an  AGPLv3 license .  
  
  "Maybe" is a trademark of Maybe Finance, Inc.  
  "Sure" is not, and refers to this community fork.

---

## 12. [dream-num/univer](https://github.com/dream-num/univer)

> [→ GitHub 連結](https://github.com/dream-num/univer)

Univer 是一個開源的跨平台 Office SDK，旨在協助開發者在自家產品中無縫內嵌如同 Google Docs 或 Sheets 的文檔與表格編輯器。它解決了傳統 Office 軟體封閉、難以自訂以及後端自動化處理困難的痛點。在 AI/LLM 領域，Univer 的核心價值在於提供強大的 Headless 處理能力與統一的 Facade API，讓 AI Agent 能以結構化方式直接對試算表與文檔進行精準讀寫、公式計算與視覺化校對。這打破了 LLM 只能處理純文字的限制，使 AI 能夠以與人類相同的文檔模型深度參與複雜的大規模辦公自動化工作流。

---

## 13. [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)

> [→ GitHub 連結](https://github.com/kajisho5/ffmpeg-skill)

kajisho5/ffmpeg-skill 是專為 Coding Agent（如 Claude Code、Cursor）設計的本地影片處理工具組與 MCP 伺服器。傳統 LLM 在使用 FFmpeg 時，常因盲猜參數、複雜指令幻覺或缺乏產出校驗而執行失敗。該專案透過封裝 42 個具備機器可讀合約（SPEC）的型別化工具，建立了「先探測、無損剪輯、後校驗」的確定性工作流。它在 AI 領域值得關注，在於展示了如何利用「驗證導向開發」（Verification-Driven Coding）原則，讓 Agent 無需依賴雲端 API，就能安全、精準地操縱低階媒體工具鏈，是 LLM 落地複雜工程自動化的絕佳範例。
