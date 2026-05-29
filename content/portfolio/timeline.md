---
title: "📚 專案時間軸導覽 (Project Timeline)"
description: "依照時間軸整理我在不同階段的修課與專案實作，紀錄我從程式開發到系統設計的演化軌跡。"
date: 2026-03-02
draft: false
hideMeta: true
---

這個頁面以時間軸方式整理我在不同階段的修課與專案。它不只是作業列表，而是我如何從「寫程式」一路走到「設計系統與研究問題」的能力演化軌跡。

👉 每個項目都附上 GitHub repo，歡迎依照有興趣的主題點進去閱讀。

---

## 🟢 大一 — 與程式設計的第一次接觸

### 商管程式設計 Programming for Business Computing
🔖 `Python` `OOP` `Pygame` `遊戲開發`
使用 pygame 製作 RPG 遊戲，是我第一次完整接觸 Python 與物件導向設計。這是我第一次把「寫程式」變成「做出完整產品」，從物件導向設計到遊戲邏輯都親自實作。這奠定了我之後長期以 Python 作為核心語言的基礎。
📎 [PBC2021-final](https://github.com/datafox-tw/PBC2021-final)

---

## 🔵 大二 — NLP 與系統實作的萌芽

### 文字探勘導論 Introduction to Text Mining
🔖 `BERT` `NLP` `TensorFlow` `Flask`
在 ChatGPT 出現之前，完整訓練並部署情緒分類系統。這讓我真正理解 NLP pipeline（訓練 → 推論 → 部署），是我進入 LLM / NLP 領域最關鍵的起點。
📎 [toxic_comment_detector](https://github.com/datafox-tw/toxic_comment_detector)

### 計算機程式 Computer Programming（C++）
🔖 `C++` `遊戲開發` `Rendering`
練習 C++ 與底層控制能力，理解效能與系統行為差異。透過實作 WindowOS 風格的遊戲，將抽象邏輯轉成即時互動系統。
📎 [windowskill_windowOS](https://github.com/datafox-tw/windowskill_windowOS)

### Python 資料分析與機器學習導論
🔖 `Machine Learning` `LangChain` `LLM 整合`
將 GPT-3 串接進系統，讓 AI 建議如何改寫情緒勒索語句。這是我第一次嘗試將「傳統 NLP」與「早期 LLM」串接，開始思考 AI 如何實際改變使用者行為。
📎 [toxic_comment_detector (LLM update)](https://github.com/datafox-tw/toxic_comment_detector)

### Big Data and Business Analytics
🔖 `Apriori` `推薦系統` `資料探勘`
設計服飾推薦系統。展現了我把商業情境轉成資料問題的能力，即使沒有真實交易資料，仍設計出可運作的推薦邏輯。
📎 [BDA2023_final_apriori](https://github.com/datafox-tw/BDA2023_final_apriori)

---

## 🟡 大三 — 資料庫、雲原生與 Finance × CS

### 資料庫管理 Database Management
🔖 `DBMS` `SQL` `正規化` `系統設計`
設計航空公司資料管理系統。建立了「資料結構設計就是系統設計」的觀念，對後來做任何需要 schema 與資料流設計的專案影響很大。
📎 [Airlines_DBMS](https://github.com/datafox-tw/Airlines_DBMS)

### 雲原生應用程式開發 Cloud Native Application Development
🔖 `React` `Express` `API 測試` `壓力測試` `系統架構`
跨系大型團隊專案。2026 年重新回頭重構部分內容，代表我從單純參與進步到理解整個雲原生架構。
📎 [CloudNative_Stadium_System](https://github.com/datafox-tw/CloudNative_Stadium_System)

### 機器人理財專題研究 Robo-Advisor
🔖 `量化金融` `風險衡量` `Python`
將財金背景轉化成可重複使用的 Python 模組化分析系統，開始建立「金融問題工程化」的思維模式。
📎 [robo_advisor](https://github.com/datafox-tw/robo_advisor)

---

## 🟣 大四 — 資訊檢索與交換期間探索

### 資訊檢索與文字探勘 (IRTM)
🔖 `RAG` `BM25` `向量檢索` `GraphRAG`
系統性比較多種 RAG 策略在繁體中文語境下的表現。建立了我在 IR (資訊檢索) 與 LLM retrieval 的研究能力。
📎 [IRTM_project](https://github.com/datafox-tw/IRTM_project)

---

## 🔴 碩一 — 深度學習、LLM 與研究導向

### 深度學習與應用 — 金融時間序列研究
🔖 `GARCH` `LSTM` `TSMixer` `Loss 設計`
探索傳統計量模型與深度學習的混合架構。嘗試透過 loss 設計反映金融風險，是我目前研究能力的重點代表作。
📎 [GLoVE](https://github.com/datafox-tw/GLoVE)

### 電腦視覺實務 (AI Cup)
🔖 `3D 醫學影像` `低解析度學習` `論文復現`
在 568 隊中取得第 56 名。完整走過 paper reproduction 到模型調整的競賽流程。
📎 [valve_abnormality_examination](https://github.com/datafox-tw/valve_abnormality_examination)

### Instruction Tuning — 文言文 ↔ 白話文
🔖 `QLoRA` `LLM 微調` `Prompt Engineering`
完整透過 QLoRA 走過微調流程，學會在資源受限下微調 LLM 並設計推論策略。

---

## 🧭 如何閱讀這份作品集

你可以用不同方式探索：
- **依主題**：NLP / LLM, Finance × AI, 系統與全端, 推薦系統
- **依深度**：基礎實作 → 模型訓練 → 系統整合 → 研究導向

---

## ✨ 結語
這條時間軸呈現我不只是專案，而是看問題方式的轉變：從「實作模型」到「整合成系統」，最後在 「Finance × AI」 的交界做研究。
