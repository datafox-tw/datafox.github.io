---
title: "2026/10/25 本週 GitHub AI 趨勢"
date: 2026-10-25
draft: false
tags: ["GitHub趨勢", "AI週報", "開源專案", "大語言模型", "AI工具"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---

本週從 GitHub Trending 前 15 名中，篩選出 **15 個** AI/LLM 相關專案：

---

## 1. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

> [→ GitHub 連結](https://github.com/cloudflare/security-audit-skill)

這是 Cloudflare 開源的 Coding Agent 擴充技能，旨在將一般程式碼 Agent 轉化為具備系統化審查能力的安全稽核員。傳統 LLM 做資安審查常面臨嚴重幻覺與高誤報，該專案採用六階段流程，並導入「對抗式驗證」機制——由獨立的 Agent 專門嘗試證偽候選漏洞，杜絕單一 Agent 的自我合理化。同時透過覆蓋率帳本與嚴格 Schema 確保審查可複驗。它不僅實用，更為 Multi-Agent 協同與批判約束機制解決複雜工程任務樹立了極佳範式。

---

## 2. [morluto/rea](https://github.com/morluto/rea)

> [→ GitHub 連結](https://github.com/morluto/rea)

morluto/rea 是一套專為 AI Agent 設計的逆向工程 MCP 伺服器，旨在打通軟體黑盒的底層邏輯。它能串接 Ghidra、IDA、Hopper 等專業工具，涵蓋從原生二進位檔、Electron、.NET 到 Android APK 等多元格式的靜態與動態分析。在 LLM 領域，它代表 Agent 能力正從「依賴現有開源程式碼」跨越到「直接逆向閉源成品並萃取邏輯」。開發者可讓 Agent 自主追蹤呼叫路徑並還原演算法，是 AI 工具調用深入系統層級的硬核實踐。

---

## 3. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

> [→ GitHub 連結](https://github.com/anthropics/claude-plugins-official)

這是 Anthropic 官方維護的 Claude Code 外掛市集目錄，旨在為其終端 AI 編程代理建立標準化的擴充生態。隨著開發者對自訂指令、外部工具與專屬技能的需求提升，此專案透過統一規範整合了官方與第三方外掛，全面支援 MCP 伺服器配置、Slash 指令與 Agent 技能綁定。在 LLM 領域，這象徵著 Anthropic 正加速將 AI Agent 從「封閉工具」推向「可擴展平台」，透過生態系讓開發者深度客製個人化工作流，是觀察 Agentic 開發架構演進的關鍵指標。

---

## 4. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

> [→ GitHub 連結](https://github.com/ruvnet/ruflo)

ruflo（前身為 Claude Flow）是專為 Claude Code 與 Codex 打造的 Agent 執行框架（Harness）。當前終端 AI 開發工具多受限於單次會話與孤立運作，ruflo 透過解耦「模型推理」與「執行環境」，為 Agent 補足協同治理層。它內建支援 HNSW 向量記憶的 AgentDB、多代理 Swarm 拓撲，並具備零信任跨機聯邦架構與 PII 防護。在 LLM 應用邁向自主化的當下，它補齊了長程記憶、動態路由與任務閉環，是將單兵 AI 升級為工程級團隊協作的重要參考實踐。

---

## 5. [stablyai/orca](https://github.com/stablyai/orca)

> [→ GitHub 連結](https://github.com/stablyai/orca)

Orca 是一款專為 AI 編程 Agent 設計的桌面與遠端編排工具，支援 Claude Code、Codex 等各類 CLI Agent。面對多模型協作的混亂痛點，它利用獨立的 Git worktree 同步調度多個 Agent 執行相同任務，讓開發者能平行比對代碼並擇優合併。專案還整合了終端機分割、Diff 註解、UI 截圖上下文抓取與手機端遠端監控。隨著開發模式從單一對話走向「Agent 艦隊並行探索」，Orca 為這種新型工作流提供了極具實用性與前瞻性的基礎架構。

---

## 6. [anomalyco/opencode](https://github.com/anomalyco/opencode)

> [→ GitHub 連結](https://github.com/anomalyco/opencode)

OpenCode 是一款開源的 AI 編碼代理（Coding Agent），提供 CLI 與桌面應用，解決了商業輔助工具封閉且難以掌控的問題。其亮點在於雙 Agent 機制：透過「build」（實作執行）與「plan」（唯讀分析）模式切換，有效降低模型直接修改代碼的風險。在當前 Agentic AI 落地開發場景的趨勢下，OpenCode 以透明的權限控管與開源生態，為工程師打造出兼具安全感與生產力的本地自主編程體驗。

---

## 7. [cursor/plugins](https://github.com/cursor/plugins)

> [→ GitHub 連結](https://github.com/cursor/plugins)

這是 Cursor 官方開源的外掛規範與市集倉庫，旨在為 Cursor Agent 建立標準化的能力擴充生態。專案將 Agent Skills、Cursor Rules 與 MCP（Model Context Protocol）整合為統一架構，涵蓋深度程式碼審查、多 Agent 協同編排到串接各類 SaaS 服務。它解決了以往 AI 工具難以標準化擴展外部能力與團隊工作流的痛點。這標誌著 AI 輔助開發正從模型對話邁向協議驅動、高度模組化的 Agentic 工作流，極具指標意義。

---

## 8. [android/skills](https://github.com/android/skills)

> [→ GitHub 連結](https://github.com/android/skills)

android/skills 是 Google 官方推出的 AI Agent Skill 模組庫，採用開放標準的 SKILL.md 規範。該專案不重複處理基礎範例，而是專注於解決 LLM 在複雜情境（如 R8 分析、Edge-to-Edge 佈局）表現不佳的問題，引導 AI 嚴格遵循 Android 官方最佳實踐。這在 AI 領域相當值得關注，展現了利用結構化上下文（Grounding）補足通用模型特定領域知識缺口的新趨勢，且能無縫整合至 Claude Code 與 Codex 等 Agent 工具，是提升程式碼 Agent 專業度與可靠性的重要範例。

---

## 9. [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

> [→ GitHub 連結](https://github.com/anthropics/knowledge-work-plugins)

Anthropic 推出的 knowledge-work-plugins 是專為知識工作者設計的開源插件庫，支援 Claude Cowork 與 Claude Code。它解決了通用 LLM 難以深度融入企業特定工具鏈與業務流程的痛點，透過 MCP 連接各類 SaaS 工具，並將領域專業與 SOP 封裝成純 Markdown 與 JSON 規範的技能與指令。這在 LLM 領域極具代表性：以輕量、零基建的宣告式架構標準化 Agent 工作流，為企業落地專職 Copilot 提供了清晰可複製的實踐路徑。

---

## 10. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

> [→ GitHub 連結](https://github.com/heygen-com/hyperframes)

HeyGen 開源的 HyperFrames 能將原生 HTML、CSS 與動畫渲染為 MP4 影片。它運用 Headless Chrome 與 FFmpeg 實現影格級的確定性渲染，無需複雜的 React 構建流程。

這款專案在 AI 領域備受矚目，原因在於 Coding Agent 極其擅長生成 HTML。HyperFrames 透過內建的 Agent Skills（支援 Claude Code、Cursor 等），讓 AI 只要接到自然語言指令，就能自動規劃鏡頭、撰寫動畫網頁並完成渲染，徹底打通了 Agent 自動化內容創作的最後一哩路。

---

## 11. [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)

> [→ GitHub 連結](https://github.com/Comfy-Org/ComfyUI)

ComfyUI 是生成式 AI 領域最具代表性的節點式工作流引擎與推論後端。它解決了傳統 WebUI 封閉且難以客製化的痛點，允許開發者以視覺化圖形精準串接模型、LoRA、ControlNet 與多模態管線。藉由優異的異步權重串流與記憶體管理，它甚至能在 4GB 顯存的消費級硬體上運行大型開源模型。隨著生圖與生影模型高速演進，ComfyUI 兼具高效推論與靈活 API，已成為銜接開源前沿技術與生產落地的事實標準。

---

## 12. [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

> [→ GitHub 連結](https://github.com/akitaonrails/ai-memory)

目前 Cursor、Claude Code 等各家 Coding Agent 雖有記憶功能，但彼此孤立且難以跨機協同。ai-memory 是以單一 Rust 二進位檔實現的 Agent 長期記憶系統，核心價值在於解決跨工具與跨設備的脈絡交接痛點——中斷 Claude Code 後能無縫切換到 Codex 繼續工作。它最大的技術亮點是以 Git 管理的純 Markdown 作為唯一真實來源，上層搭配 SQLite 與全文檢索，預設完全「零 LLM 呼叫」即可自動捕獲與檢索，兼顧資料可讀性、隱私與零成本，為多 Agent 開發生態補齊了關鍵的記憶基礎設施。

---

## 13. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

> [→ GitHub 連結](https://github.com/Graphify-Labs/graphify)

Graphify 將代碼庫、文檔與 SQL 結構轉換為可查詢的知識圖譜，可無縫整合至 Claude Code、Cursor 等 AI 助手。不同於依賴向量檢索或大量消耗 Token 的方案，它在本地藉由 Tree-sitter 進行確定性 AST 解析，精確建構跨檔案的調用與依賴關係。在 AI 寫程式邁向 Agent 化的當下，Graphify 解決了純向量 RAG 缺乏結構脈絡與反覆讀檔成本過高的痛點，用極低成本且重隱私的圖遍歷技術，為大型專案提供了更紮實的代碼理解底座。

---

## 14. [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)

> [→ GitHub 連結](https://github.com/HKUDS/CLI-Anything)

HKUDS 開源的 CLI-Anything 旨在解決 AI Agent 操控傳統軟體的痛點。過去依賴 GUI 畫面點擊既脆弱又耗 Token，手動寫 API 又極費工。CLI-Anything 能自動分析原始碼，生成具備 JSON 輸出的結構化 CLI，讓 Agent 用精準指令掌控 Blender 或 GIMP 等工具。這代表了「Computer Use」的範式轉移：把易碎的視覺操作轉為高確定性的命令列控制，並搭配 CLI-Hub 讓 Agent 自主檢索與安裝工具，是傳統軟體邁向 Agent-Native 生態的重要里程碑。

---

## 15. [vllm-project/vllm](https://github.com/vllm-project/vllm)

> [→ GitHub 連結](https://github.com/vllm-project/vllm)

vLLM 是源自伯克利 Sky Computing Lab 的高性能 LLM 推理與服務引擎，旨在解決大模型部署時顯存不足與 KV Cache 碎片化的痛點。其核心技術 PagedAttention 借用操作系統的分頁機制，顯著提升顯存利用率與請求吞吐量。除了連續批次處理、多種量化與並行技術外，它還具備跨硬體支援與 OpenAI 兼容介面。在 LLM 落地強調高效率與低成本的當下，vLLM 無疑是企業建構推理服務的首選基石。
