---
title: "2026/11/08 本週 GitHub AI 趨勢"
date: 2026-11-08
draft: false
tags: ["GitHub趨勢", "AI週報", "Claude生態", "AI代理", "開源工具"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---

本週從 GitHub Trending 前 15 名中，篩選出 **15 個** AI/LLM 相關專案：

---

## 1. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

> [→ GitHub 連結](https://github.com/thedotmack/claude-mem)

許多開發者在使用 Claude Code 或 Cursor 時，最常面臨每次開新 Session，Agent 就「失憶」重蹈覆轍的痛點。claude-mem 為各類 Coding Agent 打造跨 Session 的持久記憶層。它採用旁路 Observer 機制，在背景記錄工具調用軌跡並壓縮為結構化觀察，存入本地 SQLite 與向量庫。新對話啟動時，透過漸進式索引與 MCP 工具按需拉取細節，兼顧極低 Token 消耗與脈絡延續性。這專案實踐了當前 Context Engineering 在長期任務管理上的最佳範式，極具參考價值。

---

## 2. [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)

> [→ GitHub 連結](https://github.com/max-sixty/worktrunk)

Worktrunk 是一款專為「多 AI Agent 並行開發」設計的 Git worktree CLI 工具。隨著 Claude Code 等 Coding Agent 能自主執行長任務，開發者常需同時調度多個 Agent 平行改 code；然而 Git 原生的 worktree 雖然能隔離工作區，指令卻相當繁瑣。Worktrunk 讓 worktree 操作如切換分支般直覺，支援一鍵建立目錄並喚起 Agent，更透過 CoW 技術共享構建快取，並內建 LLM Commit 摘要。在工程典範轉向監督與並行 Agent 的當下，它精準切中了本地多任務隔離與切換的痛點。

---

## 3. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)

> [→ GitHub 連結](https://github.com/Donchitos/Claude-Code-Game-Studios)

Claude-Code-Game-Studios 是一個基於 Claude Code 的多 Agent 遊戲開發框架。為解決單一對話開發容易產生雜亂代碼與缺乏品管的問題，它將會話拆解為 49 位階層化 Agent，並整合 74 種工作流技能與路徑約束規則。其在 AI 領域的亮點在於落實嚴謹的「系統性工程約束」：引入權限守門、自動化 Hook 與必須截圖佐證的驗收機制，展示了如何將 Agent 從天馬行空的生成輔助，轉化為具備可控性與工業化水準的協作管線。

---

## 4. [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu)

> [→ GitHub 連結](https://github.com/Renhuai123/ziwei-doushu)

這是一個將中國傳統「紫微斗數」完全開源的排盤引擎與超大型命理數據集。過去玄學領域的排盤算法與斷語資料多被商業軟體鎖在圍牆內，該專案不僅用 TypeScript 實現了包含真太陽時校正、夏令時判定與格局推演的排盤引擎，更釋出了高達 56.6 GB（約 204 億字）的 v4.0 高質量解讀數據集。

在 AI/LLM 領域，這項專案解決了傳統文化與玄學垂直領域極度缺乏結構化訓練語料的痛點。其產出的 67.5 萬張命盤與 877 萬段 13 維度文本，非常適合直接用做 LLM 微調（SFT）語料、RAG 知識庫檢索源，或作為建構命理 AI Agent 的底層邏輯驅動引擎。

---

## 5. [pingdotgg/t3code](https://github.com/pingdotgg/t3code)

> [→ GitHub 連結](https://github.com/pingdotgg/t3code)

隨著 Claude Code、Codex 與 Cursor 等 Coding Agent 普及，開發者常在破碎的終端介面與工具間反覆切換。T3 Code 定位為統一的「Agent 操控面板」，旨在直接調度本機運行的多種 AI Agent。它善用開發者既有的 CLI 認證，並提供 Electron 桌面版、Web 與 iOS/Android 行動端介面。這項專案值得關注之處，在於它將 Agent 從單一終端解放，實現支援遠端存取且高效能的控制工作流，甚至能用手機監控本機的程式生成，是探索多 Agent 開發體驗極具代表性的開源嘗試。

---

## 6. [anthropics/skills](https://github.com/anthropics/skills)

> [→ GitHub 連結](https://github.com/anthropics/skills)

anthropics/skills 是 Anthropic 官方推出的 Agent Skills 開源專案，旨在透過模組化的指令與腳本，讓 Claude 動態載入特定領域的專業能力。它解決了傳統 Prompt 工程難以標準化與重用複雜工作流的痛點。值得關注的是，專案直接公開了 Claude.ai 背後處理 Office 文件的生產級實作（如 docx、pdf 等技能），並導入 agentskills.io 開放標準，為社群構建可擴展、可重用的企業級 AI Agent 提供了極具參考價值的架構範本。

---

## 7. [Nutlope/hallmark](https://github.com/Nutlope/hallmark)

> [→ GitHub 連結](https://github.com/Nutlope/hallmark)

Nutlope/hallmark 是一套專為 Claude Code、Cursor 等 Coding Agent 打造的「反 AI 塑料感（Anti-AI-slop）」設計技能。多數 LLM 生成前端時，常陷入標題跳色、濫用標籤與死板結構等套版陷阱；Hallmark 透過 50 種精選主題、真實瀏覽器渲染檢驗（sloplint）與分層門禁，杜絕機器手痕。它不放任模型盲猜，而是以嚴謹的設計規範約束輸出，示範了如何將 AI 原型提升為兼具品味與可用性的真實產品。

---

## 8. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

> [→ GitHub 連結](https://github.com/milind-soni/OpenMausBot)

OpenMausBot 是一款主打 Local-first 的開源多 Agent 協同平台，定位為 Grok Bot 與 Manus 的開源替代品。它將 AI 團隊化為即時通訊介面，每個 Bot 都能配置不同模型（直接複用本機 Claude 或 Codex CLI）與專屬虛擬機，具備桌面操作與工具調用能力。專案核心亮點在於資料完全留存本地，且內建權限審查機制，危險指令皆須人工核可。對重視隱私又想探索自主 Agent 協作與系統操作的開發者而言，極具參考價值。

---

## 9. [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

> [→ GitHub 連結](https://github.com/D4Vinci/Scrapling)

Scrapling 是 Python 的現代化網路爬蟲框架，解決了傳統工具面對 Cloudflare 等反爬蟲機制、動態渲染與效能低下等痛點。它將 HTTP 指紋偽裝、隱蔽瀏覽器自動化與高併發 Spider 整合於一身。在 AI/LLM 應用中，Scrapling 尤為關鍵：它內建 MCP 伺服器與 Agent Skill，可直接作為 LLM Agent 的瀏覽器與資料擷取工具；同時提供一鍵生成 RAG 專用 Markdown 的功能，無需額外消耗 Token 清洗資料。無論建構 LLM 知識庫或賦予 Agent 即時連網能力，它都是極具價值的基礎設施。

---

## 10. [jakubkrehel/skills](https://github.com/jakubkrehel/skills)

> [→ GitHub 連結](https://github.com/jakubkrehel/skills)

jakubkrehel/skills 是一套專為 Coding Agent 打造的設計工程技能集合，全面涵蓋 UI 排版、色彩系統、WCAG 無障礙檢測與狀態測試。現階段 LLM 寫前端雖然高效，但往往忽視視覺細節與邊界情境。該專案將嚴謹的 Design Engineering 知識模組化，賦予 Agent 在審查 PR 或生成元件時，自動校準光學對齊、色彩對比度與無障礙語意的能力。這展現了 AI 輔助開發正從「能跑就好」邁向專業產品級精緻交付的重要趨勢。

---

## 11. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

> [→ GitHub 連結](https://github.com/vercel-labs/agent-browser)

agent-browser 是 Vercel Labs 專為 AI Agent 打造的 Rust 瀏覽器自動化 CLI。傳統讓 LLM 操作網頁時，龐雜的 DOM 往往浪費大量 Token 且容易誤判；該工具將網頁轉化為無障礙樹快照，替互動元素加上 `@e1` 般的參照碼，讓 Agent 透過短指令即可精準點擊與讀取。背景 Daemon 能維持狀態並原生支援 MCP 協定，這種大幅降低 Context 負擔且高度穩定的設計，為 Agent 網頁自動化立下了非常實用的參考標準。

---

## 12. [mattpocock/skills](https://github.com/mattpocock/skills)

> [→ GitHub 連結](https://github.com/mattpocock/skills)

mattpocock/skills 是針對 AI 輔助開發（如 Claude Code、Copilot 等）設計的開源技能庫。不同於盲目的「vibe coding」，它將領域驅動設計（DDD）與測試驅動開發（TDD）等經典工程實踐轉化為 Agent 指令。透過事前的深度訪談對齊需求、維護統一領域詞彙降低溝通耗損，並藉由嚴格測試迴圈遏止架構腐化。它展示了如何以紮實工程底蘊駕馭 Coding Agent，是推動 AI 走向嚴謹軟體工程的代表作。

---

## 13. [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland)

> [→ GitHub 連結](https://github.com/hyprwm/Hyprland)

Hyprland 是一個獨立開發的動態拼貼式 Wayland 視窗管理器，兼具流暢視覺特效與高度客製化，解決了傳統桌面環境資源佔用過高與多視窗排版效率不足的痛點。

在 AI/LLM 領域，這款專案備受關注的原因在於其極輕量化的架構，能最大化釋放 CPU 與記憶體資源供本地 LLM 推理與微調任務使用。結合其強大的 Socket IPC 與靈活的視窗規則，工程師能打造高度自動化的 AI 開發工作流——一鍵無縫並排 GPU 資源監控、多個 LLM Agent 終端與代碼編輯器，顯著提升複雜 AI 實驗與開發的效率。

---

## 14. [github/spec-kit](https://github.com/github/spec-kit)

> [→ GitHub 連結](https://github.com/github/spec-kit)

讓 AI Coding Agent 直接寫程式，常因缺乏結構而陷入邊摸索邊修 Bug 的泥淖。GitHub 推出的 Spec Kit 為 AI Agent 建立了一套規格驅動開發（SDD）的標準化架構與工作流。它透過結構化的規格書、實施計畫、任務拆解與收斂驗證，引導 Agent 循序漸進地開發功能、診斷 Bug 或評估概念。在 LLM 邁向工程化與團隊協作的當下，Spec Kit 的價值在於將隨機的 Prompt 轉化為可預測、可擴充且具治理性的軟體工程流程，是實現高品質 AI 協作開發不可忽視的核心工具。

---

## 15. [obra/superpowers](https://github.com/obra/superpowers)

> [→ GitHub 連結](https://github.com/obra/superpowers)

`obra/superpowers` 是一個專為 Coding Agent 設計的技能框架與開發方法學。現今 AI 助手常在未釐清需求前就急於寫 code，導致結構混亂。Superpowers 透過注入技能模組，強制 Agent 執行需求腦暴、任務拆解、嚴格 TDD 與 Subagent 審查流程。它之所以值得關注，在於將開發紀律帶入 Agent 領域，不僅無縫支援 Claude Code、Cursor 等十數種工具，更引領 AI 開發從「隨機寫程式碼」邁向「規範化自動化工程」。
