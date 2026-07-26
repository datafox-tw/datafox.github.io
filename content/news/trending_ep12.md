---
title: "2026/07/26 本週 GitHub AI 趨勢"
date: 2026-07-26
draft: false
tags: ["GitHub趨勢", "AI週報", "AI應用", "大型語言模型", "程式工具"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---

本週從 GitHub Trending 前 15 名中，篩選出 **15 個** AI/LLM 相關專案：

---

## 1. [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

> [→ GitHub 連結](https://github.com/bojieli/ai-agent-book)

「bojieli/ai-agent-book」是《深入理解 AI Agent：設計原理與工程實踐》這本開源書籍的主倉庫，由李博杰所著。它為 AI/LLM 開發者提供了一套從核心理論到實踐的全面指南，深入解析「Agent = LLM + 上下文 + 工具」的核心公式，旨在解決建構實用 AI Agent 的工程挑戰。該書涵蓋十大章節，從基礎的上下文工程、記憶與知識庫，到工具應用、程式碼生成 Agent、評估與後訓練、多模態交互，乃至多 Agent 協作等關鍵議題。最引人注目的是，它提供了多達 92 個配套實驗項目，其中 70 多個可獨立運行，讓讀者能親手實踐，將抽象理論轉化為具體技能。其全書開源並提供多語言翻譯，不僅降低了學習門檻，也彰顯了知識共享的精神，是當前 AI Agent 領域極具參考價值且實用性高的學習資源。

---

## 2. [koala73/worldmonitor](https://github.com/koala73/worldmonitor)

> [→ GitHub 連結](https://github.com/koala73/worldmonitor)

koala73/worldmonitor 是一個令人注目的即時全球情報儀表板，旨在透過 AI 技術解決資訊過載與情勢感知不足的挑戰。它能聚合來自 500 多個精選來源的新聞，並利用 AI 提煉成簡報，同時整合地緣政治監控、基礎設施追蹤與金融市場數據，以直觀的雙地圖引擎呈現，讓使用者全面掌握全球脈動。在 AI/LLM 領域，World Monitor 備受關注的原因有二。首先，它強調「在地 AI」，支援透過 Ollama 在本地運行大部分核心功能，無須外部 API 金鑰，這大幅降低了隱私與營運成本，展示了邊緣 AI 在實用情境中的巨大潛力。其次，除了整合 Groq 與 OpenRouter 等 LLM 服務進行內容生成外，專案更設計了豐富的程式化介面和代理探索檔案（如 `llms.txt`），使其能輕易被其他 AI 代理或自動化腳本利用，直接獲取結構化情報，為 AI 驅動的情資分析與決策支援開闢了嶄新的應用途徑。

---

## 3. [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)

> [→ GitHub 連結](https://github.com/tirth8205/code-review-graph)

「tirth8205/code-review-graph」是一個針對AI輔助程式碼開發與審查的智慧圖譜工具。它解決了當前LLM在程式碼協作中常見的痛點：AI模型為了提供精確回饋，往往需要讀取專案中大量無關檔案，導致token消耗巨大且上下文視窗效率低下。

此專案透過Tree-sitter建立程式碼庫的結構化地圖，將函數、類別、依賴關係等解析為可查詢的知識圖譜。當進行程式碼審查或尋求AI幫助時，它能精準計算變更的「影響範圍」（blast-radius），只向AI提供最相關的程式碼片段，大幅減少所需的上下文大小。

其在AI/LLM領域值得關注之處在於，它不只是一個RAG方案，更提供深層次的程式碼結構理解，實現了高達82倍的token節省。這不僅顯著降低了AI開發成本，也提升了模型理解複雜專案的能力。結合對多種AI工具的支援以及本地優先的設計，`code-review-graph`為提升開發者工作流中的AI效率與隱私保護，帶來了實用且強大的解決方案。

---

## 4. [1jehuang/jcode](https://github.com/1jehuang/jcode)

> [→ GitHub 連結](https://github.com/1jehuang/jcode)

jcode 是一個針對程式碼開發設計的智慧型代理程式框架，旨在提升開發者在多會話工作流程中的效率與技能上限。其在 AI/LLM 領域的亮點在於卓越的效能與資源效率，其 RAM 佔用和啟動速度遠優於許多同類工具，這對規模化應用至關重要。jcode 創新的記憶體架構允許代理程式透過語義向量和記憶圖譜，像人類般自動回溯相關資訊，有效避免 token 浪費。更具特色的是，它支援多代理程式「Swarm」協同工作，能自動管理衝突，甚至讓代理程式自主建立團隊平行處理任務。此外，jcode 獨特的「自我開發模式」允許代理程式修改、建置、測試並自動重載自身的程式碼，展現了 LLM 自主進化的前瞻性。搭配對主流 LLM 服務商及本地模型的廣泛支援，jcode 無疑是值得關注的下一代 AI 編碼工具，揭示了 AI 輔助開發的巨大潛力。

---

## 5. [agegr/pi-web](https://github.com/agegr/pi-web)

> [→ GitHub 連結](https://github.com/agegr/pi-web)

agegr/pi-web 提供一個為 pi 程式碼代理（coding agent）量身打造的本地網頁使用者介面，旨在克服純指令行操作在管理 AI 代理時的局限性。它將本地的 pi 會話檔案轉化為功能豐富的瀏覽器工作空間，讓使用者能夠直觀地瀏覽歷史會話、進行即時互動、配置模型、管理技能，並即時預覽專案檔案。

在 AI/LLM 領域，pi-web 的出現深具意義。隨著 AI 代理日益複雜，開發者迫切需要一個能提供更好可觀察性、可重複性及互動控制的工具。pi-web 透過其獨特的會話管理（如分支與合併）、整合專案檔案瀏覽、以及透明化的代理狀態顯示（如成本與上下文使用），大大簡化了 AI 代理的開發與除錯流程。它將傳統 CLI 的代理互動提升至類似 IDE 的視覺化環境，讓開發者能更高效、更精確地掌握與引導 AI 代理，對於構建穩健的代理應用至關重要。

---

## 6. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

> [→ GitHub 連結](https://github.com/diegosouzapw/OmniRoute)

OmniRoute 是一個令人印象深刻的開源 AI 閘道專案，旨在解決使用多個 LLM 供應商時的複雜性和成本挑戰。它提供單一 API 端點，整合超過 290 個供應商與 500 個模型，涵蓋 OpenAI、Claude、Gemini 等主流服務，更匯集了 90 多個免費服務，每月提供高達 15 億的免費 Token。這使得開發者能無痛利用各平台的免費額度。專案的核心優勢在於其智慧路由與 Token 優化。OmniRoute 的「Auto-Combo」引擎能依據成本、延遲、配額、品質等 12 個因素，自動在不同模型間切換並進行故障轉移。內建的 12 種壓縮引擎，如 RTK 和 Caveman，能透明地將上下文與回應壓縮 15% 至 95%，大幅降低 Token 消耗。它與多種主流程式碼 CLI 和 AI 代理高度相容，並支援多平台部署。對於追求高效、低成本、高彈性且注重隱私的 AI 模型使用者來說，OmniRoute 無疑是一個值得關注的解決方案。

---

## 7. [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)

> [→ GitHub 連結](https://github.com/MoonshotAI/kimi-code)

Kimi Code CLI 是一款在終端機運作的 AI 編碼代理，旨在革新開發者與程式碼互動的方式。它不只負責讀寫程式碼，還能執行 shell 指令、搜尋檔案、甚至抓取網頁內容，並根據即時回饋自主決定下一步行動。其亮點在於一鍵安裝、毫秒級啟動的 TUI 介面，以及透過「視訊輸入」將螢幕錄影或展示轉化為程式碼或分析的能力，極大地簡化了複雜問題的描述。此外，它支援 Agent Client Protocol (ACP)，能無縫整合至 Zed、JetBrains 等主流編輯器，讓 AI 助理直接融入你的開發環境。Kimi Code CLI 不僅展示了大型語言模型在自動化多步驟開發任務上的潛力，更以其創新的互動模式和「下一代代理」的理念，為 AI/LLM 社群開啟了更高效、更直覺的開發新範式，非常值得關注。

---

## 8. [earendil-works/pi](https://github.com/earendil-works/pi)

> [→ GitHub 連結](https://github.com/earendil-works/pi)

Pi (earendil-works/pi) 是一個全面性的 AI 代理工具包，旨在簡化和強化 AI 代理的開發與部署。它解決了多個關鍵痛點，包括提供一個統一的多供應商 LLM API (支援 OpenAI, Anthropic, Google 等)，讓開發者無需處理各家 LLM 的介面差異。其核心是一個強大的代理運行時，內建工具調用與狀態管理機制，為構建複雜、智能的代理提供了堅實基礎。

特別值得關注的是其互動式編碼代理 CLI，展現了 AI 代理在實際開發工作中的巨大潛力。此外，專案對安全性的重視，透過沙盒和容器化方案來限制代理的系統存取，以及在供應鏈上的嚴格管理，都顯示了其在實用性和可靠性方面的深思熟慮。Pi 不僅提供工具，更鼓勵開發者分享開源編碼代理會話數據，以社群協作的方式推動代理技術的實際進步。對於希望構建高效率、安全且能實際運用的 AI 代理的開發者而言，Pi 絕對是值得深入探索的專案。

---

## 9. [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli)

> [→ GitHub 連結](https://github.com/MoonshotAI/kimi-cli)

Kimi CLI 是一個在終端機運行的 AI 代理，旨在協助開發者完成軟體開發與終端操作。它不只可以讀寫程式碼、執行 Shell 命令、搜尋網頁，還能自主規劃行動。其值得關注之處，在於它深度整合了開發者的工作流程。透過 VS Code 擴充功能、支援 ACP 的 IDE (如 Zed, JetBrains)，甚至 Zsh 整合，Kimi CLI 能將 AI 能力無縫嵌入開發環境。特別是它能切換為 Shell 模式，讓 AI 直接成為你的命令列工具，同時也支援如 ACP 與 MCP 等協定，展現其與進階開發工具協作的潛力，大幅提升效率。目前專案正進化為 Kimi Code CLI，預期將更專注於新一代終端 AI 程式碼代理，這使其成為 LLM 驅動開發工具領域的亮點，值得技術社群持續追蹤。

---

## 10. [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)

> [→ GitHub 連結](https://github.com/rohitg00/ai-engineering-from-scratch)

ai-engineering-from-scratch 是一個旨在將 AI 工具使用者轉變為能親手「建構、交付 AI 產品」的全面性學習專案。它包含 503 堂課、20 個階段，強調從數學基礎和原始程式碼（Python, TypeScript, Rust, Julia）親手實現 AI 演算法，如反向傳播、分詞器、注意力機制與 Agent 循環，確保學習者在接觸 PyTorch 等框架前，已對底層原理有深刻理解。

此專案在 AI/LLM 領域值得關注，因其提供了從理論到實踐的端到端學習路徑。它深入涵蓋 LLM 的從零建構、工程化、多模態應用、Agent Engineering、自主系統、多代理協作，乃至生產部署與倫理安全。每堂課結束都產出可重用的 prompt、技能或 agent，能直接整合至主流 AI 助手中。這種扎實且產出導向的課程設計，對於希望成為具備實戰能力的 AI/LLM 工程師來說，是極為寶貴的資源。

---

## 11. [mattpocock/skills](https://github.com/mattpocock/skills)

> [→ GitHub 連結](https://github.com/mattpocock/skills)

mattpocock/skills 是一套為 AI 程式代理人量身打造的實用技能集，旨在將數十年軟體工程經驗融入開發，讓 AI 告別「感覺寫程式」，邁向「實作工程」。它解決了 AI 輔助開發常見的問題，如需求對齊困難、輸出冗長、程式碼品質及架構混亂。專案透過一系列內建工程最佳實踐的核心技能，強制代理人遵循嚴謹規範。對 AI/LLM 社群而言，`mattpocock/skills` 提供了一套立即可用的方法論，能顯著提升 AI 輔助開發的效率與程式碼品質，將其轉化為可靠的工程協作者。

---

## 12. [ruvnet/RuView](https://github.com/ruvnet/RuView)

> [→ GitHub 連結](https://github.com/ruvnet/RuView)

RuView 是一個顛覆性的開源專案，它將普通的 Wi-Fi 訊號轉化為即時空間智慧。這套系統無需攝影機或穿戴設備，透過低成本的 ESP32 感測器即可實現生命體徵監測（呼吸、心率）、精確的存在與活動偵測，甚至穿牆感知。它巧妙解決了傳統感測方案在隱私、視線限制及部署複雜度上的痛點。  
  
對於 AI/LLM 技術社群，RuView 展現了邊緣 AI 的巨大潛力。其利用微型神經網路模型（可壓縮至 8KB），在 ESP32 上實現微秒級推斷，並透過自監督學習從原始 Wi-Fi 資料中自動適應環境。專案豐富的 AI 模組，如 RAG-local 和聯邦學習，以及與 Claude Code、Codex 等 LLM 工具的深度整合，都完美詮釋了 AI Agent 如何與現實世界無縫互動，為打造普惠且注重隱私的智慧感測應用提供了清晰路徑。這項技術不僅實用，更為 AI 應用開啟了新的想像空間。

---

## 13. [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)

> [→ GitHub 連結](https://github.com/HKUDS/DeepTutor)

DeepTutor 是一個由香港大學開發的 AI 驅動終身個人化導師系統，旨在整合學習過程中的各個環節，從輔導、解題到研究、視覺化和能力掌握。它解決了傳統學習工具各自獨立、情境分散的問題，透過其獨特的「智能體原生」（agent-native）架構，將所有功能整合於單一智能體循環中，確保學習情境的連貫性。

該專案在 AI/LLM 領域值得關注，在於其靈活多樣的 RAG 知識庫管理（支援 LlamaIndex、GraphRAG 等多種引擎），以及可自訂、可追溯的三層記憶系統，讓個人化學習體驗更透明、可控。此外，DeepTutor 支援多種 LLM 提供者，並提供強大的 CLI 介面，甚至能被其他 AI 智能體驅動，大幅提升了其在教學和研究場景中的應用潛力與擴展性。它不僅是一個學習工具，更是一個高度可配置、可協作的 AI 學習生態系統。

---

## 14. [Nutlope/hallmark](https://github.com/Nutlope/hallmark)

> [→ GitHub 連結](https://github.com/Nutlope/hallmark)

Nutlope/hallmark 是一個專為 Claude Code、Cursor 和 Codex 等 AI 程式碼助手設計的「反 AI 樣板化」(Anti-AI-slop) 設計技能。它旨在解決當前 LLM 在生成 UI/UX 時，普遍存在的設計缺乏獨特性、成果常顯得千篇一律的「AI 樣板」問題。Hallmark 的核心機制是為每個設計需求智能選擇獨特的宏觀結構，並套用二十種主題，同時經過嚴格的「防樣板測試」與預發布自評，刻意避免 LLM 訓練中常見的預設模式，確保每個產出都充滿新意，而非模板的顏色變體。

此專案在 AI/LLM 領域值得關注，因為它將設計的「原創性」和「獨特指紋」帶回 AI 生成流程。Hallmark 不僅能建構新的 UI，還能審核現有程式碼的設計品質，甚至透過 `hallmark study` 功能，從現有設計中提取其「DNA」精髓，創造出非像素級複製、充滿創意的設計。對於希望利用 AI 提升開發效率，同時堅持設計品質和品牌個性的開發者與設計師來說，Hallmark 無疑是個突破性的工具，為 AI 輔助設計開啟了更高水準的可能性。

---

## 15. [Pumpkin-MC/Pumpkin](https://github.com/Pumpkin-MC/Pumpkin)

> [→ GitHub 連結](https://github.com/Pumpkin-MC/Pumpkin)

Pumpkin-MC/Pumpkin 是一個以 Rust 語言完全重寫的 Minecraft 伺服器，旨在提供高效、穩定且高度客製化的遊戲體驗。它解決了傳統伺服器在效能與擴展性上的挑戰，運用 Rust 的多執行緒優勢、Vanilla 相容性與強化安全。專案範圍廣泛，從底層協定到世界生成、玩家互動，乃至精細的紅石與物理模擬，都致力於提供最佳效能與靈活性。

對於 AI/LLM 技術社群而言，Pumpkin 具備成為出色 AI 實驗平台的潛力。其明確規劃的「Entity AI」功能，使其不僅是遊戲伺服器，更是開發和測試複雜 AI 代理（如具身智慧、強化學習、多智能體系統）的理想沙盒。Rust 賦予的高效能，確保在大規模 AI 行為模擬時仍能維持流暢運算，為前沿 AI 研究提供了穩固且高度擴展的基礎。這讓研究人員得以在一個可控、高性能的環境中探索新的 AI 可能性。
