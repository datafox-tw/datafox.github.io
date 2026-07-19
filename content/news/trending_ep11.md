---
title: "2026/07/19 本週 GitHub AI 趨勢"
date: 2026-07-19
draft: false
tags: ["GitHub趨勢", "AI週報", "AI助理與代理", "大型語言模型 (LLM)", "智能辦公與生產力"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---

本週從 GitHub Trending 前 15 名中，篩選出 **15 個** AI/LLM 相關專案：

---

## 1. [Nutlope/hallmark](https://github.com/Nutlope/hallmark)

> [→ GitHub 連結](https://github.com/Nutlope/hallmark)

Nutlope 的 Hallmark 是一個在 AI/LLM 領域中極具開創性的專案，它精準地捕捉並解決了當前 AI 生成設計常見的「AI 浮濫」（AI slop）問題。作為專為 Claude Code、Cursor 和 Codex 等 AI 編碼工具設計的「技能」，Hallmark 的核心價值在於其能夠產出獨特且「拒絕看起來像 AI 生成」的 UI 設計。這直接挑戰了許多 AI 生成內容容易流於樣板化、缺乏原創性與同質化的痛點。它透過豐富的宏觀結構、多達二十種主題，並實施嚴格的「浮濫測試」（slop-test gates），確保每個輸出的設計都擁有獨特的「指紋」。更令人印象深刻的是，當預設主題無法滿足創意需求時，它能啟動自訂模式，從頭開始設計。對於 AI/LLM 技術社群來說，Hallmark 展示了如何引導大型語言模型，使其不再是單純的內容生成器，而是能成為創造出高品質、兼具原創性與美學深度作品的協作者，為 AI 輔助設計指明了一條高標準的路徑。

---

## 2. [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)

> [→ GitHub 連結](https://github.com/OpenCut-app/OpenCut)

OpenCut 是一個旨在成為 CapCut 替代品的開源影片編輯器，提供免費且跨網頁、桌面與行動裝置的解決方案。它不僅滿足了社群對多功能開源編輯工具的需求，其目前從頭重寫的計畫更值得關注。新架構將採用 Rust 核心，並引入 Editor API、插件優先設計以及內建腳本編輯器，大幅提升了開發彈性與擴展性。對於 AI/LLM 技術社群來說，OpenCut 的潛力尤其巨大。專案規劃中的「MCP server (for AI agents)」和無頭模式 (headless mode) 清楚表明，它將不只是一個傳統編輯器，更可能成為 AI 代理進行影片自動化生成、內容批次處理與分析的強大平台。此外，其贊助商 fal.ai 專精於生成式 AI 模型，進一步強化了 OpenCut 深度整合 AI 的意圖。開發者將能透過其插件或腳本機制，將最新的 AI/LLM 技術融入影片製作工作流，實現前所未有的智慧化內容創作。

---

## 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

> [→ GitHub 連結](https://github.com/Shubhamsaboo/awesome-llm-apps)

「Shubhamsaboo/awesome-llm-apps」這個專案無疑是當前 LLM 開發者的一座寶庫。它集結了超過 100 個可實際運行的開源 AI Agent 與 RAG 應用，從單一功能的 Agent Skill 到複雜的多 Agent 團隊，涵蓋了聊天、記憶、生成式 UI 甚至是遊戲等多元場景。對於那些想將 LLM 理論付諸實踐，卻又苦於起步或尋找具體範例的開發者而言，這個專案提供了即插即用的解決方案。它不只提供程式碼，更有詳細的快速啟動指南和框架教學，支援主流 LLM 模型，並強調程式碼的實際運行與客製化彈性。這讓我們能以更低的門檻，快速打造出各種創新且具商業潛力的 LLM 應用，解決從概念到產品的實作痛點，是值得深度探索與借鑒的實用資源。

---

## 4. [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)

> [→ GitHub 連結](https://github.com/HKUDS/Vibe-Trading)

HKUDS 的 Vibe-Trading 是一個將自然語言轉化為可執行金融分析的開源研究平台。它解決了傳統量化研究中數據獲取、策略生成及回測的複雜耗時問題，使金融分析更高效。此專案在 AI/LLM 領域尤其值得關注，其核心是一個自進化的工具型 AI 代理。Vibe-Trading 運用大型語言模型驅動多代理團隊，如投資或量化策略小組，進行市場研究、生成交易策略，甚至能透過「影子帳戶」分析並優化個人交易行為。這種將 LLM 智能與金融工具鏈深度整合，展示了 AI 在自動化金融決策流程中的巨大潛力，為開發者提供了探索 AI 賦能金融的絕佳範例。

---

## 5. [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)

> [→ GitHub 連結](https://github.com/HKUDS/DeepTutor)

HKUDS/DeepTutor 是一款以「智能體原生」(agent-native) 架構為核心的 AI 學習平台，旨在提供終身個人化輔導，整合多元學習模式，解決了傳統工具碎片化問題。其在 AI/LLM 領域值得關注，在於其先進的多引擎 RAG 知識庫（支援 LlamaIndex、GraphRAG）及創新的三層可檢視記憶系統，極大提升了 AI 學習過程的透明度與可追溯性。DeepTutor 展現了 Agentic AI 在教育領域的巨大潛力，透過模組化工具和 EduHub 技能生態系，為開發者提供豐富的擴展性與實踐範例，推動智能教學發展。

---

## 6. [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)

> [→ GitHub 連結](https://github.com/iOfficeAI/OfficeCLI)

OfficeCLI 是一個專為 AI Agent 設計的開源 Office 套件，讓 AI 能輕鬆讀取、編輯、自動化 Word、Excel、PowerPoint 文件。它解決了傳統 Office 自動化方案的複雜性與環境依賴，以單一二進位檔實現跨平台、免安裝，為開發者與 AI Agent 提供了高效處理 Office 文件的全新途徑。

在 AI/LLM 領域，OfficeCLI 的出現令人印象深刻。其關鍵在於內建高擬真渲染引擎，讓 AI Agent 不僅能解析文件內容，更能「看見」實際的排版效果，從而實現「渲染→觀察→修正」的智能閉環，徹底解決 AI 在處理視覺化文件時常遇到的佈局問題。此外，它提供 AI-native 的 CLI 介面、確定性 JSON 輸出與路徑式元素存取，大幅簡化了 LLM 整合的複雜度與 token 成本。結合模板合併與文件結構傾印等功能，OfficeCLI 賦予 AI Agent 更智慧、高效處理辦公文件的能力，是提升 AI 辦公自動化水平的利器。

---

## 7. [mattpocock/skills](https://github.com/mattpocock/skills)

> [→ GitHub 連結](https://github.com/mattpocock/skills)

`mattpocock/skills` 是一個為 AI 程式碼代理（coding agents）精心打造的技能庫，旨在將扎實的軟體工程原則融入 AI 輔助的開發流程。它解決了 AI 在開發中常見的痛點：包括需求理解的錯位、程式碼過於冗長、產出品質不佳，以及避免專案演變成「泥球式架構」。

此專案透過一系列精巧且可組合的指令，例如 `/grill-me` 用於深度訪談以確保需求對齊、`/grill-with-docs` 協助建立共享語言以提升溝通效率、`/tdd` 實踐測試驅動開發，以及 `/improve-codebase-architecture` 幫助持續優化系統設計。它提供兩種安裝方式：可自行修改的 `skills.sh` 或作為 Claude Code 的訂閱式外掛。對於希望讓 LLM 不僅能「寫程式」，更能「寫好程式」、遵循嚴謹工程規範的開發者而言，`mattpocock/skills` 提供了極具洞察力的實用工具與方法，是提升 AI 輔助開發品質與效率的寶貴資源。

---

## 8. [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)

> [→ GitHub 連結](https://github.com/kangarooking/cangjie-skill)

`kangarooking/cangjie-skill` 是一個將書籍、長影片、播客等高價值內容「蒸餾」成 AI Agent 可用技能的創新專案。它精準解決了人們知識吸收雖多卻難以實際應用，以及傳統摘要無法為 AI Agent 提供結構化、可執行知識的核心痛點。

在 AI/LLM 領域，此專案透過獨特的 RIA-TV++ 流程，嚴謹提取並驗證內容中的方法論與原則，將知識轉化為具備「操作性」的工具。這將 AI 能力從單純的內容理解提升至知識「操作與執行」，大幅增強 AI Agent 的實戰價值，是推動知識實用化、智慧操作化的關鍵一步。

---

## 9. [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)

> [→ GitHub 連結](https://github.com/wonderwhy-er/DesktopCommanderMCP)

Desktop Commander MCP 是一個基於 Model Context Protocol (MCP) 的開源專案，它賦予 AI 模型（如 Claude，其專屬應用程式更支援 GPT-4.5、Gemini 等）直接控制本機終端機、搜尋檔案系統與執行編輯的強大能力。它旨在將 AI 轉化為全能的開發助理，不僅能執行程式碼、管理多種檔案（包含 Excel, PDF, DOCX），還能自動化任務，其廣泛的系統級控制能力遠超越傳統 IDE 內建的 AI 工具。這個專案在 AI/LLM 社群中值得關注，在於它有效地彌合了大型語言模型與本機操作系統之間的互動鴻溝。透過整合進階終端管理、視覺化檔案預覽及無需額外 API 費用的運作模式（利用現有訂閱），Desktop Commander 大幅降低了 AI 自動化的門檻，提供了一個安全且具成本效益的方式，讓 AI 能更深入地參與開發流程，為打造實用且高效的 AI Agent 奠定了重要基礎。

---

## 10. [openai/codex](https://github.com/openai/codex)

> [→ GitHub 連結](https://github.com/openai/codex)

openai/codex 是一個由 OpenAI 推出的輕量級編碼代理程式，旨在將強大的 AI 編碼能力直接帶到開發者的終端機。它提供命令行介面 (CLI) 運行，也支援整合到 VS Code 等主流 IDE，甚至有獨立的桌面應用程式，解決了開發者對於 AI 輔助工具能更彈性、更深入整合日常工作流的需求。在 AI/LLM 領域，這個專案之所以值得關注，是因為它不僅是 OpenAI 的官方出品，更展示了 LLM 應用如何從單純的聊天互動，進化成個人化、深度整合開發環境的智能助手。透過與現有 ChatGPT 訂閱方案的無縫接軌，它顯著降低了專業 AI 編碼工具的使用門檻，讓開發者能更有效率地利用 AI 進行程式碼生成、重構或除錯等任務，是 AI 輔助開發工具走向實用化和整合化的重要里程碑。

---

## 11. [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)

> [→ GitHub 連結](https://github.com/openinterpreter/openinterpreter)

openinterpreter/openinterpreter 專案以 Rust 重新實作，並從 OpenAI 的 Codex 分支而來，其核心目標是打造一個優化於低成本大型語言模型的編碼代理。它透過精巧的代理程式框架 (agent harness) 模擬，能讓 Kimi K3 等模型發揮最佳性能。這解決了傳統上低成本模型在複雜編碼和任務執行上的效率問題，讓更多開發者能運用經濟實惠的模型建立功能強大的代理。 

該專案最值得關注的亮點在於，它將 LLM 從單純的文本生成提升到實際的「電腦操作」。透過 `openinterpreter`，LLM 能在 macOS、Linux、Windows 上執行原生指令，驅動瀏覽器測試網頁應用，甚至操作桌面軟體。其支援多種模型提供商與內建的 harness 切換功能，為開發者提供了極大的彈性和效率，使 AI 代理能夠更深入地與真實世界互動，是目前 AI Agent 領域中極具潛力的開源工具。

---

## 12. [abseil/abseil-cpp](https://github.com/abseil/abseil-cpp)

> [→ GitHub 連結](https://github.com/abseil/abseil-cpp)

「abseil/abseil-cpp」是 Google 開源的一套 C++ 常用函式庫，旨在補足並擴充 C++ 標準函式庫。它匯集了 Google 內部歷經廣泛測試與生產驗證的程式碼，提供了高效能的「Swiss table」無序容器、強健的錯誤處理機制（`absl::Status`）、多執行緒同步原語，以及實用的字串和時間處理工具。這些模組解決了標準函式庫的某些限制或提供了更優化的替代方案，是構建高效能、可靠 C++ 應用程式的堅實基礎。在 AI/LLM 領域，特別是開發高效能推論引擎、自定義運算子或大規模資料管線時，C++ 的效能至關重要。abseil-cpp 這些經過實戰考驗的工具，能顯著提升 AI 基礎設施的效能與可靠性，讓開發者能更專注於 AI 核心創新，而非底層複雜性，加速專案開發並確保系統穩定。

---

## 13. [stablyai/orca](https://github.com/stablyai/orca)

> [→ GitHub 連結](https://github.com/stablyai/orca)

「stablyai/orca」在GitHub Trending上備受矚目，它是一個專為AI時代開發者設計的「AI代理開發環境」（ADE）或「AI協調器」。隨著AI編碼代理日益普及，開發者面臨如何高效管理、協作並比較這些代理產出成果的挑戰。Orca正是為了解決此痛點而生。

它允許你同時運行多個AI代理，每個代理在獨立的Git工作樹（Parallel Worktrees）中運作，讓你將同一Prompt發送給不同代理，快速比較結果並選取最佳方案。Orca深度整合了開發者工具鏈，包括VS Code風格編輯器、WebGL終端、GitHub與Linear整合，甚至能將UI元素直接送入代理Prompt。其行動伴侶應用更讓你隨時隨地監控與引導AI代理。對於追求高效率的開發者，Orca提供了一個強大平台來駕馭AI代理艦隊，加速開發流程，無疑是AI/LLM領域值得關注的創新工具。

---

## 14. [ibelick/ui-skills](https://github.com/ibelick/ui-skills)

> [→ GitHub 連結](https://github.com/ibelick/ui-skills)

ibelick/ui-skills 是一個專為「設計工程師」打造的 UI 技能集合工具，其核心目標是為 AI 代理或開發者提供一套結構化的方法，以理解並應用複雜的使用者介面設計技能。它解決了 AI 在嘗試處理或生成設計任務時，往往缺乏特定領域設計知識與最佳實踐的痛點。透過其直觀的 CLI 工具，開發者能夠引導 AI 代理，依據特定任務需求（例如動態效果或基礎 UI 原則），精準地定位並啟用相關的 UI 技能集。

在 AI/LLM 領域中，這個專案的價值不容小覷。它為 AI 代理提供了一個可操作且專業的「UI 知識庫」，彌補了 AI 在視覺設計專業度上的不足。當我們期望 AI 不僅能處理語義，還能輔助、甚至自動化 UI 設計流程時，ui-skills 就能扮演關鍵角色。它可作為 LLM 訓練、微調或 RAG 系統的寶貴資源，賦予 AI 代理在設計過程中展現更深層次的理解與更高的專業性，進而有效縮短設計與開發之間的鴻溝，全面提升設計效率與最終品質。

---

## 15. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

> [→ GitHub 連結](https://github.com/Graphify-Labs/graphify)

Graphify-Labs/graphify 是一個創新的 AI 程式碼輔助工具技能，它能將專案中的程式碼、文件、資料庫結構，甚至是多媒體內容，轉化為一個可查詢的知識圖譜。這解決了開發者在面對複雜專案時，難以快速理解其架構與內部關聯的問題，讓 AI 助理能以超越傳統檔案搜尋的方式，提供更深層次的專案洞察。

在 AI/LLM 領域，Graphify 的價值在於其獨特的「真圖譜」方法。它不依賴向量嵌入，而是透過 `tree-sitter` 在本地端精確解析程式碼 AST，生成確定性的知識圖譜，確保程式碼隱私且不產生 LLM 成本。對於文件、圖片等非程式碼內容，則能整合如 Claude Code、Cursor 等多種 AI 助理的模型進行語義提取。這種結合本地精確解析與 LLM 語義理解的混合模式，大幅提升了 AI 助理對專案脈絡的掌握度，讓 `explain`、`query`、`path` 等操作更精準，是 LLM 應用於軟體工程理解與協作的重要進展。
