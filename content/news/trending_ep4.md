---
title: "2026/05/26 本週 GitHub AI 趨勢"
date: 2026-05-26
draft: false
tags: ["GitHub趨勢", "AI週報", "AI代理", "LLM應用", "程式碼智慧", "邊緣AI"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---
{{< lang-toggle >}}

<div class="lang-zh">

本週從 GitHub Trending 前 15 名中，篩選出 **14 個** AI/LLM 相關專案：

---

## 1. [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)

> [→ GitHub 連結](https://github.com/colbymchenry/codegraph)

CodeGraph 是一個專為 AI 程式碼代理（如 Claude Code, Cursor, Codex 等）設計的預索引程式碼知識圖譜。傳統上，AI 代理在探索程式碼庫時，依賴於昂貴且耗時的檔案掃描工具（如 grep, glob, Read），這不僅消耗大量 tokens，也拉長了處理時間。CodeGraph 的核心價值在於透過建立符號關係、呼叫圖及程式碼結構等知識，讓代理能即時查詢，而非重複掃描。它宣稱可節省約 35% 的成本，減少 70% 的工具呼叫，並加快 46% 的處理速度，且所有操作 100% 在本地執行，兼顧效率與隱私。對於開發大型專案的團隊來說，CodeGraph 能顯著提升 AI 輔助開發的效率，是優化 LLM 在軟體工程領域應用的一個重要方向。

---

## 2. [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)

> [→ GitHub 連結](https://github.com/tinyhumansai/openhuman)

OpenHuman 是一個開源的個人 AI 超級智慧代理，旨在深度融入用戶的日常工作流程。它解決了許多 AI 助理「冷啟動」的痛點，透過自動抓取並壓縮來自 118+ 個第三方服務（如 Gmail, Notion, GitHub）的數據，將其儲存為本地的「記憶樹」及與 Obsidian 相容的 Markdown 檔案。這種本地優先的記憶模式，確保了用戶數據的隱私性，並讓 AI 代理在幾分鐘內就能擁有全面的上下文，省去冗長的訓練期。此外，OpenHuman 內建的智慧 token 壓縮技術（TokenJuice）能顯著降低成本與延遲，其一站式解決方案（包括網頁搜尋、程式碼工具組、語音功能）使其成為尋求高效、私有且功能強大 AI 助手的開發者，一個值得關注的選項。

---

## 3. [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything)

> [→ GitHub 連結](https://github.com/Lum1104/Understand-Anything)

Understand-Anything 是一個能將任何程式碼庫、知識庫或文件轉換為互動式知識圖譜的 Claude Code 插件。對於加入新團隊或面對龐大專案的開發者而言，它解決了快速理解複雜系統的挑戰。該專案透過多代理管道，結合 `tree-sitter` 的結構分析與 LLM 的語義理解，自動建立包含檔案、函數、類別和依賴關係的知識圖譜，並提供視覺化儀表板。其獨特功能如「引導式導覽」、「差異影響分析」和「分層視覺化」，能幫助用戶從宏觀到微觀掌握程式碼結構與業務邏輯。生成的圖譜可以作為 JSON 檔案與團隊共享，大幅提升了團隊協作和新成員的學習效率，是提升開發者生產力的利器。

---

## 4. [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

> [→ GitHub 連結](https://github.com/Imbad0202/academic-research-skills)

Academic Research Skills (ARS) 是一個為 Claude Code 設計的學術研究技能套件，涵蓋從研究、寫作到審閱、修改和定稿的完整流程。它解決了許多 AI 在學術寫作中常見的幻覺、偷工減料和迎合人類等問題。ARS 的核心理念是「AI 輔助而非取代人類」，它處理繁瑣工作如引用格式、數據驗證和邏輯一致性檢查，同時透過如「反對者協議」和「意圖偵測層」等功能，鼓勵人類研究者的批判性思考。其強調人機協作、階段性驗證和詳細的版本記錄，使其成為開發高可靠性 AI 輔助工具的典範，特別在要求嚴謹的學術領域中，為負責任的 AI 應用提供了深刻的洞見。

---

## 5. [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)

> [→ GitHub 連結](https://github.com/rohitg00/ai-engineering-from-scratch)

AI Engineering From Scratch 是一個全面且實作導向的 AI 工程學課程，包含 435 堂課、20 個階段，約 320 小時的學習內容。它旨在彌補理論知識與專業應用之間的鴻溝，透過「從零開始」的教學理念，讓學習者從數學基礎開始，親手建構每個 AI 演算法，而非僅止於 API 調用。課程涵蓋從線性代數到自主代理群體等廣泛主題，每堂課結束時都產出可重複使用的成品（如 prompts, skills, agents），形成個人作品集。特別值得關注的是，它整合了 AI 程式碼代理來提供個人化學習路徑和測驗，使得學習過程更具互動性和效率。這份課程對於期望深度理解並親手打造 AI 系統的工程師來說，無疑是一份寶貴的資源。

---

## 6. [ruvnet/RuView](https://github.com/ruvnet/RuView)

> [→ GitHub 連結](https://github.com/ruvnet/RuView)

RuView 是一個革命性的 WiFi 感測平台，能將普通的 WiFi 訊號轉化為即時空間智慧、生命體徵監測和存在檢測功能。它解決了傳統感測技術（如攝影機和穿戴設備）在隱私、視線限制和使用者依從性方面的問題。透過利用 ESP32 傳感器捕捉的通道狀態資訊（CSI），RuView 無需攝影機或穿戴設備，就能穿牆偵測室內人員、測量呼吸和心率，甚至進行活動識別和跌倒檢測。其本地化邊緣運算（ESP32 + Cognitum Seed）和開源特性，加上與主流智慧家庭生態系統的整合，使其在醫療照護、零售和安全監控等領域具備巨大潛力，提供一種創新且注重隱私的環境感知解決方案。

---

## 7. [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

> [→ GitHub 連結](https://github.com/rohitg00/agentmemory)

Agentmemory 是一個專為 AI 程式碼代理設計的持久性記憶體解決方案，它以 Karpathy 的 LLM Wiki 模式為靈感，旨在解決代理在不同會話間「失憶」的常見問題。傳統上，用戶需不斷重複解釋專案架構和偏好，Agentmemory 透過靜默捕捉代理的工具使用、提示等互動，將其壓縮成可搜尋的記憶（事實、概念、知識圖譜），並在下次會話開始時注入相關上下文。這大幅提升了代理的效率和連貫性。其混合搜尋（BM25 + 向量 + 圖譜）、四層記憶整合機制，以及對多種 AI 代理（如 Claude Code, Cursor, Gemini CLI）的廣泛支援，使其成為讓 AI 助理真正具備長期、可演化智慧的關鍵工具。

---

## 8. [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser)

> [→ GitHub 連結](https://github.com/CloakHQ/CloakBrowser)

CloakBrowser 是一個具備隱形功能的 Chromium 瀏覽器，透過在 C++ 原始碼層級進行指紋修改，使其能夠通過各種機器人偵測測試。它解決了傳統自動化工具（如 Playwright, Puppeteer）因 JavaScript 注入或配置層級修改而容易被反機器人系統識別的問題。CloakBrowser 內建 58 項源碼補丁，涵蓋了 Canvas、WebGL、音訊、GPU 等多個指紋參數，使其行為與真實瀏覽器無異，並能達到 reCAPTCHA v3 達 0.9 的人類級分數，並通過 Cloudflare Turnstile 等多項挑戰。此外，「humanize=True」選項可模擬人類的滑鼠、鍵盤和捲動行為，使其成為需要可靠地與網站互動的 AI 代理和自動化任務的強大工具，為合法爬蟲和自動化提供了更為穩健的解決方案。

---

## 9. [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic)

> [→ GitHub 連結](https://github.com/supertone-inc/supertonic)

Supertonic 是一個超高速、本地化且多語言的文字轉語音（TTS）系統，透過 ONNX Runtime 在設備上原生運行。它解決了傳統高品質 TTS 依賴雲端服務帶來的延遲、成本和隱私問題。Supertonic 的核心優勢在於其輕量級（99M 參數）模型能在桌面、行動裝置乃至 Raspberry Pi 等邊緣設備上，以極低的延遲生成 44.1kHz 的高品質音訊，且支援 31 種語言。它無需 GPU，並能處理複雜的文本內容（如財務表達、電話號碼和技術單位），甚至提供表情標籤以增加語音的自然度。Supertonic 及其多 runtime SDK 範例（Python, Node.js, Browser, iOS 等）使其成為開發者在追求即時、私密且高效語音應用時，一個極具吸引力的解決方案。

---

## 10. [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)

> [→ GitHub 連結](https://github.com/can1357/oh-my-pi)

Oh-My-Pi (omp) 是一個終端機 AI 程式碼代理，作為 Mario Zechner 的 Pi 專案分支，它在原有的基礎上大幅強化，提供了深度整合的開發工具鍊和程式碼優先的工作流程。Omp 解決了許多 AI 代理在實際開發中缺乏與 LSP、除錯器和真實 shell 深度整合的痛點。它將 IDE 的智慧（如語義重構、錯誤診斷）和高效的原生工具（如 ripgrep, glob）嵌入代理流程中，並引入「內容哈希錨定編輯」等創新功能，顯著提升編輯的精準度並節省 tokens。其支援子代理、多後端網頁搜尋以及智慧記憶系統「Hindsight」，使其成為一個功能豐富、性能卓越的自主軟體工程平台，旨在讓 AI 代理能夠更有效率地執行複雜的開發任務。

---

## 11. [dograh-hq/dograh](https://github.com/dograh-hq/dograh)

> [→ GitHub 連結](https://github.com/dograh-hq/dograh)

Dograh 是一個開源、可自託管的語音代理平台，旨在成為 Vapi 和 Retell 等專有解決方案的替代品。它解決了專有平台帶來的供應商鎖定、按分鐘計費及客製化受限等問題。Dograh 提供完全的原始碼控制和透明度，允許開發者整合自己的 LLM、TTS 和 STT 模型，並透過拖放式工作流建構器，在兩分鐘內建立一個可運作的語音機器人。其 Python-based 和 Docker-first 的架構確保了部署的一致性和靈活性。對於尋求自主性、成本效益及深度客製化的團隊而言，Dograh 的開源承諾和強大功能，使其成為建構生產級語音代理的理想選擇。

---

## 12. [presenton/presenton](https://github.com/presenton/presenton)

> [→ GitHub 連結](https://github.com/presenton/presenton)

Presenton 是一個開源的 AI 簡報生成器和 API，旨在提供 Gamma、Beautiful AI 等工具的自託管替代方案。它解決了專有簡報工具常見的訂閱鎖定、模型選擇受限及數據控制不足等問題。Presenton 的核心價值在於讓用戶完全掌控其 AI 簡報工作流程，支援多種 LLM 和圖片生成模型（如 OpenAI, Gemini, Ollama），並可使用自定義的 HTML/Tailwind CSS 模板。無論是透過 Docker 部署還是作為 Electron 桌面應用程式執行，Presenton 都允許用戶保有數據隱私並靈活客製化。其生成可編輯 PPTX 檔案的能力，以及作為 API 服務部署的選項，使其成為追求自主性、靈活設計和降低成本的個人和團隊的理想選擇。

---

## 13. [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)

> [→ GitHub 連結](https://github.com/HKUDS/CLI-Anything)

CLI-Anything 旨在透過自動生成 CLI 腳本，讓所有軟體都能「代理原生化」，解決 AI 代理在操作真實專業軟體時面臨的挑戰。許多 AI 代理擅長推理卻難以有效運用實際應用程式，因為傳統的 UI 自動化脆弱且 API 支援有限。CLI-Anything 透過七階段自動化流程，為任何程式碼庫創建功能全面、結構化且可靠的 CLI 接口，使其能被 AI 代理精準控制。專案的 CLI-Hub 讓代理可以自主發現、安裝和管理這些 CLI。其對 18 個不同專業軟體（如 GIMP, Blender, LibreOffice）進行了超過 2,330 項嚴格測試，證明了其在將人類設計的軟體轉化為 AI 代理原生工具方面的巨大潛力，是實現真正自主代理的關鍵基礎設施。

---

## 14. [obra/superpowers](https://github.com/obra/superpowers)

> [→ GitHub 連結](https://github.com/obra/superpowers)

Superpowers 是一個專為 AI 程式碼代理（如 Claude Code, Cursor, Gemini CLI 等）設計的軟體開發方法論與技能框架。它解決了 AI 代理常會「盲目寫 code」或脫離上下文的問題。透過提供一組可組合的技能與指令，它會強迫代理在動工前先進行「腦力激盪」釐清需求、產出設計文件，並在人類確認後，嚴格遵循「測試驅動開發 (TDD)」與「子代理驅動開發 (Subagent-driven-development)」流程。這使得 AI 能將複雜工作拆解為微小任務並逐步驗證，甚至能連續自主運作數小時而不偏離目標。對於希望約束 AI 代理行為、大幅提升生成程式碼品質與專案穩定性的開發者而言，這是一個能讓 AI 化身為嚴謹工程師的強大外掛。

</div>

<div class="lang-en">

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

</div>
