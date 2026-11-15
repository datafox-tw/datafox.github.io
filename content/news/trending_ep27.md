---
title: "2026/11/15 本週 GitHub AI 趨勢"
date: 2026-11-15
draft: false
tags: ["GitHub趨勢", "AI週報", "AI代理", "開源AI", "大型語言模型"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---

本週從 GitHub Trending 前 15 名中，篩選出 **11 個** AI/LLM 相關專案：

---

## 1. [meta/astryx](https://github.com/meta/astryx)

> [→ GitHub 連結](https://github.com/meta/astryx)

Astryx 是 Meta 開源的 React 設計系統，源自內部支撐超過 1.3 萬款應用的實戰經驗，提供逾 150 個無樣式綁定的元件。在 AI 開發浪潮下，它最引人注目的是「Agent-ready」定位：Meta 將元件 API、命名慣例、文件與專屬 CLI 進行高度標準化設計，讓 Coding Agent 能以極低的幻覺成本理解結構、檢索元件並自動化構建 UI。它代表了設計系統從單純服務人類，轉向適配「人機協同寫碼」的重要演進，對前端與 AI 整合極具參考價值。

---

## 2. [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)

> [→ GitHub 連結](https://github.com/sherlock-project/sherlock)

Sherlock 是一款強大的開源情報（OSINT）工具，能透過單一使用者名稱，快速檢索超過 400 個社群平台的帳號關聯。在 AI Agent 與自動化流程興起的當下，它常被封裝為 LLM 的外部工具（Tool Calling），協助自主代理人執行背景調查與數位足跡分析。對開發者而言，Sherlock 提供了標準化且覆蓋極廣的實體感知端點，是建構調查型 Agent 或身分驗證工作流時極為實用的基礎元件。

---

## 3. [anthropics/skills](https://github.com/anthropics/skills)

> [→ GitHub 連結](https://github.com/anthropics/skills)

anthropics/skills 是 Anthropic 官方釋出的 Agent Skills 實作與規範。為解決 LLM 執行專業任務時難以維持一致流程與格式的痛點，它透過標準化的指令、腳本與設定檔，讓 Claude 能動態載入特定技能。專案最大亮點在於直接開源了 Claude 線上處理 PDF、Word 等文件的生產級技能，並全面支援 Claude Code 與 API。這為社群展示了企業級 Agent 模組化擴展的標準解法，是探索 Agentic 工作流落地非常值得借鏡的參考實作。

---

## 4. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

> [→ GitHub 連結](https://github.com/vercel-labs/agent-browser)

vercel-labs 推出的 agent-browser 是一款專為 AI Agent 設計的 Rust 原生瀏覽器自動化 CLI。過往讓 LLM 操控網頁時，解析完整 HTML 容易消耗大量 Token 且定位不穩；該專案將頁面轉為無障礙樹（Accessibility Tree）的精簡快照，並替互動元素標註唯一參照（如 @e1），讓模型能以極低 Token 成本精準操作。此外，它內建 MCP 伺服器並以背景常駐程序維持工作階段，大幅降低了打造 Web Agent 的延遲與整合門檻。

---

## 5. [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)

> [→ GitHub 連結](https://github.com/google/elephant-goldfish-model)

Google 開源的 Elephant-Goldfish Model (EGM) 是一款專為 Coding Agent 設計的架構審查外掛。它直擊 LLM 長對話容易產生「盲目認同」與思維盲點的問題：由記住所有脈絡的「大象」負責探索需求並起草規格，再交由上下文乾淨的「金魚」子 Agent 以全新視角挑出未言明的假設與風險。這種透過上下文隔離（Context Isolation）實現自我校驗的機制，為 Spec-driven 的 Agent 協作開拓了極具參考價值的落地方向。

---

## 6. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

> [→ GitHub 連結](https://github.com/milind-soni/OpenMausBot)

OpenMausBot 是一款開源且主打 Local-first 的多 Agent 協作桌面應用，旨在提供 Grok Bot 或 Manus Cue 等閉源產品的替代方案。它將 AI 封裝為即時通訊軟體架構，讓使用者能同時調度多個 Agent。每個 Bot 可配置不同模型（直接調用本機 Claude 或 Codex CLI）、獨立虛擬環境與數百種工具。專案特別引入權限仲裁機制，確保執行終端指令與修改檔案等敏感操作需經人工核准。它示範了如何兼顧隱私與自主執行力，是個人團隊化 Agent 的亮眼實踐。

---

## 7. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)

> [→ GitHub 連結](https://github.com/ZhuLinsen/daily_stock_analysis)

daily_stock_analysis 是一個開源的多市場股票智慧分析與決策推送系統，解決了投資人每日追蹤跨市場行情、公告與海量新聞時資訊過載的痛點。在 LLM 領域中，它完整示範了垂直金融場景的 Agent 化工程落地：透過 Tool Use 串接多源金融 API 與搜尋引擎，並結合纏論、波浪等量化技術指標，由大模型輸出結構化的決策看板。其支援 GitHub Actions 零成本排程與多模型路由，是研究 AI Agent 工具調用、資料融合與自動化管線極佳的實戰範例。

---

## 8. [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)

> [→ GitHub 連結](https://github.com/google-deepmind/mujoco)

MuJoCo（Multi-Joint dynamics with Contact）是 Google DeepMind 主導的高效能物理模擬引擎，專為多關節結構與複雜接觸動力學設計。在 AI 領域，它長期是強化學習（RL）與機器人控制的標竿環境。隨著具身智能（Embodied AI）成為大模型落地的新前線，MuJoCo 不僅提供極速且精準的動態模擬，其基於 JAX 的 MJX 分支更支援大規模 GPU 平行模擬與可微物理計算，大幅縮短 Sim-to-Real 的策略訓練週期，是連結決策大腦與實體世界不可或缺的底層基建。

---

## 9. [backnotprop/plannotator](https://github.com/backnotprop/plannotator)

> [→ GitHub 連結](https://github.com/backnotprop/plannotator)

Plannotator 是一款專為 AI Coding Agent 設計的本機瀏覽器審查介面，支援 Claude Code、Codex 與 Copilot CLI 等主流工具。它解決了開發者在終端機中難以直觀審查 Agent 龐大規劃、程式碼 Diff 與 Artifacts 的痛點。透過 Hook 機制與 MCP，Agent 擬定計畫時會自動開啟網頁，供開發者進行行內標註並將反饋一鍵送回交談輪次。隨著 Agent 逐漸走向自主執行，這種兼具非同步效率與高資訊密度的人機協作介面（Human-in-the-loop），是確保 AI 生成品質與控制權的關鍵拼圖。

---

## 10. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

> [→ GitHub 連結](https://github.com/addyosmani/agent-skills)

由資深工程師 Addy Osmani 發起的開源專案，專為 AI Coding Agent 打造生產級的工程工作流。現行 AI 寫程式常貪圖捷徑，容易跳過測試、架構規劃與安全審查；該專案將 Google 等頂尖工程文化的規範包裝為 25 個結構化技能，涵蓋規格制定、TDD 到程式審查等全生命週期。它支援 Cursor、Claude Code 等多種代理工具，並引入反偷懶驗證機制，是推動 AI 從「寫玩具 Demo」邁向「交付嚴謹生產代碼」的關鍵實踐。

---

## 11. [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts)

> [→ GitHub 連結](https://github.com/anthropics/claude-quickstarts)

anthropics/claude-quickstarts 是 Anthropic 官方推出的應用範本庫，旨在解決開發者將 Claude API 落地至生產環境時缺乏架構指引的痛點。專案不僅涵蓋常見的客服與數據分析範例，更深入展示了 Claude 最具前瞻性的能力：從 Computer Use 與 Browser Use 的桌面自動化、雙 Agent 自主編程，到透過 MCP 與 Managed Agents 串接 Slack 與 Sentry 等工具。對於想超越單純 Prompt 呼叫、構建具備工具執行與持久化狀態之複雜 Agent 系統的工程師而言，這是掌握官方最佳實踐的必讀藍圖。
