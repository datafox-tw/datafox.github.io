---
title: "2026/10/18 本週 GitHub AI 趨勢"
date: 2026-10-18
draft: false
tags: ["GitHub趨勢", "AI週報", "開源專案", "人工智慧", "大型語言模型"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---

本週從 GitHub Trending 前 15 名中，篩選出 **10 個** AI/LLM 相關專案：

---

## 1. [morluto/rea](https://github.com/morluto/rea)

> [→ GitHub 連結](https://github.com/morluto/rea)

REA（Reverse Engineer Anything）是一個專為 AI Agent 打造的逆向工程 MCP 伺服器，旨在打通 LLM 與底層軟體分析工具的鴻溝。它支援從 Native 二進位檔、Electron 應用到 Android APK 與韌體，能串接 Ghidra、IDA 等專業逆向工具。在 AI 領域，REA 展現了 MCP 的深度應用價值：它讓 Claude 或 Cursor 等 Agent 能直接調用反編譯引擎檢視偽代碼、提取特徵並理清架構，大幅降低了安全分析與逆向工程的門檻，是 Agent 落地高複雜度系統工程的代表作。

---

## 2. [storytold/artcraft](https://github.com/storytold/artcraft)

> [→ GitHub 連結](https://github.com/storytold/artcraft)

ArtCraft 是一款開源的「AI 創作 IDE」，旨在解決純文字 Prompt 難以精確掌控構圖、角色一致性與鏡位調度的痛點。它將生成式 AI 與 3D 場景調度（Scene Blocking）、2D 分層合成相結合，讓創作者能先直觀設定人偶姿態與虛擬機位，再引導模型定向算圖。專案深度整合了影像、影片到 3D 的數十款主流模型（如 FLUX、Sora、Hunyuan 3D）。在多模態快速發展的當下，ArtCraft 展現了 AI 生成工具從隨機「抽卡」走向專業化、可重現工程管線的關鍵一步。

---

## 3. [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5)

> [→ GitHub 連結](https://github.com/boykopovar/AnyPS5)

AnyPS5 是一套能將 PS5 執行檔自動移植至 Linux 與 Windows 的工具。它捨棄傳統模擬器的運行開銷，改以靜態重鏈結（Relinker）與著色器重編譯技術，將專有二進位檔直接轉換為原生應用。在 AI 與系統研究視角下，該專案體現了高度複雜的自動化代碼遷移與 ABI 映射管線；隨著大型語言模型在逆向工程與底層代碼生成的深入應用，此架構為 AI 驅動的軟體移植與自動化轉譯提供了極具價值的實證標的。

---

## 4. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

> [→ GitHub 連結](https://github.com/cathrynlavery/diagram-design)

過去 LLM 生成的架構圖常充斥著廉價陰影或呆板樣式，難以直接用於正式發布。`diagram-design` 是一款為 Cursor、Claude Code 等 Agent 設計的 Skill，專門產出出版級的單檔 HTML+SVG 圖表。它支援 45 種圖型，核心在於將美感規則化：嚴格遵循 4px 網格、1px 細線與品牌色自動擷取。在 AI 領域中，它不僅示範了如何約束模型產出高質感設計，其按需載入規範的上下文工程策略，更是 Agent 開發的絕佳參考。

---

## 5. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

> [→ GitHub 連結](https://github.com/anthropics/claude-plugins-official)

這是 Anthropic 官方維護的 Claude Code 插件目錄，為其終端代理工具建立標準化的擴充生態。隨著 Coding Agent 深入實際開發場景，單一工具難以滿足所有需求；該專案透過統一架構，整合了 Slash 指令、Agent 技能與 MCP 伺服器設定，讓開發者能靈活擴充 Claude 的編程能力。這象徵終端 AI 助理正邁向模組化生態系，是觀察 LLM 開發工具鏈如何標準化擴展的重要指標。

---

## 6. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

> [→ GitHub 連結](https://github.com/heygen-com/hyperframes)

HyperFrames 是 HeyGen 開源的視頻渲染框架，主打「用寫 HTML 的方式做影片」。它透過 Headless Chrome 與 FFmpeg，將原生 HTML/CSS 與動畫轉為確定性 MP4，無需 React 繁瑣的構建步驟。其核心亮點是「專為 AI Agent 設計」。相較於傳統剪輯軟體或專用 DSL，LLM 對 HTML 的生成最為穩定；搭配內建的 21 種 Agent Skills，能讓 Claude Code 等代理自主完成分鏡規劃、動畫適配與音訊混音，是將代碼生成延伸至影音自動化管線的關鍵基礎建設。

---

## 7. [mksglu/context-mode](https://github.com/mksglu/context-mode)

> [→ GitHub 連結](https://github.com/mksglu/context-mode)

Context Mode 是一套針對 AI Coding Agent 的上下文最佳化工具，透過 MCP 與 Hook 機制解決 Token 浪費與記憶丟失痛點。過去 Agent 呼叫工具常將大量 Log 或網頁原始碼硬塞進視窗，導致 Context 迅速耗盡且對話壓縮後容易遺忘進度。該專案引導模型「寫程式處理資料而非由 LLM 硬吞」，在沙盒執行後只回傳關鍵結果，節省高達 98% 空間；同時以本地 SQLite 與 FTS5 索引會話狀態。它改變了 Agent 的資料處理範式，對長任務落地極具參考價值。

---

## 8. [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

> [→ GitHub 連結](https://github.com/NationalSecurityAgency/ghidra)

Ghidra 是由美國國家安全局（NSA）開源的逆向工程框架，提供強大的反組譯與反編譯分析能力。在 AI 領域，它正成為構建二進制分析代理（Agent）的關鍵基座。透過其開放的腳本 API，開發者頻繁將 LLM 與 Ghidra 結合，用於自動還原反編譯變數名稱、解析晦澀演算法邏輯，甚至進行自主漏洞挖掘。這讓它成為觀察 LLM 在底層程式碼理解與自動化資安實戰中，不可或缺的工具載體。

---

## 9. [mattpocock/skills](https://github.com/mattpocock/skills)

> [→ GitHub 連結](https://github.com/mattpocock/skills)

這是一套專為 Coding Agent（如 Claude Code、Cursor、Copilot 等）設計的高階技能庫，旨在告別盲目的「Vibe Coding」，回歸紮實的軟體工程實踐。專案核心在解決 AI 寫程式常見的語意對齊不良、廢話過多與架構失控等問題，透過 `/grill-me` 深度反問釐清需求、建立領域術語（Glossary）降低溝通成本，並導入嚴謹的 TDD 與架構檢查機制。它展示了如何將傳統工程規範模組化為 Agent 技能，在自動化狂潮中守住代碼品質，極具借鑑價值。

---

## 10. [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context)

> [→ GitHub 連結](https://github.com/ranxianglei/billion-context)

billion-context 是一款專為 Coding Agent 設計的上下文壓縮代理（Proxy），旨在解決長對話導致 Token 費用暴增與超出視窗限制的痛點。它有別於傳統的強制截斷，而是透過注入工具讓模型自主決定分層壓縮與還原歷史訊息。最亮眼之處在於其設計對 Prefix Caching 極為友善，能在維持 95% 以上快取命中率的前提下省下數倍 Token。隨著 Agent 邁向長時間自主運作，這種兼顧小視窗與低成本的架構極具參考價值。
