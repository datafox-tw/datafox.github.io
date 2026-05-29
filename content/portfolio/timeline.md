---
title: "📚 專案時間軸導覽 (Project Timeline)"
description: "依照時間軸整理我在不同階段的修課與專案實作，紀錄我從程式開發到系統設計的演化軌跡。"
date: 2026-03-02
draft: false
hideMeta: true
---
{{< lang-toggle >}}

<div class="lang-zh">

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

</div>

<div class="lang-en">

This page organizes my coursework and projects chronologically. It's not just a list of assignments, but rather a reflection of my evolving capabilities, tracking my journey from "writing code" to "designing systems and researching problems."

👉 Each item includes a GitHub repo; feel free to click through to read about topics that interest you.

---

## 🟢 Freshman Year — First Contact with Programming

### Programming for Business Computing
🔖 `Python` `OOP` `Pygame` `Game Development`
Creating an RPG game using Pygame was my first complete exposure to Python and object-oriented design. This was my first time transforming "writing code" into "making a complete product," personally implementing everything from object-oriented design to game logic. This laid the foundation for my long-term use of Python as a core language.
📎 [PBC2021-final](https://github.com/datafox-tw/PBC2021-final)

---

## 🔵 Sophomore Year — The Budding of NLP and System Implementation

### Introduction to Text Mining
🔖 `BERT` `NLP` `TensorFlow` `Flask`
Before ChatGPT emerged, I fully trained and deployed an sentiment classification system. This allowed me to truly understand the NLP pipeline (training → inference → deployment), marking a crucial starting point for my entry into the LLM / NLP field.
📎 [toxic_comment_detector](https://github.com/datafox-tw/toxic_comment_detector)

### Computer Programming (C++)
🔖 `C++` `Game Development` `Rendering`
Practiced C++ and low-level control capabilities, understanding performance and system behavior differences. Implemented a Windows OS-style game, transforming abstract logic into a real-time interactive system.
📎 [windowskill_windowOS](https://github.com/datafox-tw/windowskill_windowOS)

### Introduction to Python Data Analysis and Machine Learning
🔖 `Machine Learning` `LangChain` `LLM Integration`
Integrated GPT-3 into a system to suggest how to rephrase emotionally manipulative sentences. This was my first attempt to connect "traditional NLP" with "early LLMs," prompting me to consider how AI can practically change user behavior.
📎 [toxic_comment_detector (LLM update)](https://github.com/datafox-tw/toxic_comment_detector)

### Big Data and Business Analytics
🔖 `Apriori` `Recommendation Systems` `Data Mining`
Designed a clothing recommendation system. This demonstrated my ability to translate business scenarios into data problems, even designing a functional recommendation logic without real transaction data.
📎 [BDA2023_final_apriori](https://github.com/datafox-tw/BDA2023_final_apriori)

---

## 🟡 Junior Year — Databases, Cloud-Native, and Finance × CS

### Database Management
🔖 `DBMS` `SQL` `Normalization` `System Design`
Designed an airline data management system. Established the concept that "data structure design IS system design," which profoundly influenced any subsequent projects requiring schema and data flow design.
📎 [Airlines_DBMS](https://github.com/datafox-tw/Airlines_DBMS)

### Cloud Native Application Development
🔖 `React` `Express` `API Testing` `Stress Testing` `System Architecture`
A large interdisciplinary team project. Refactored parts of it in 2026, demonstrating my progress from mere participation to understanding the entire cloud-native architecture.
📎 [CloudNative_Stadium_System](https://github.com/datafox-tw/CloudNative_Stadium_System)

### Robo-Advisor Special Topic Research
🔖 `Quantitative Finance` `Risk Measurement` `Python`
Transformed financial background into a reusable Python modular analysis system, beginning to develop a mindset of "engineering financial problems."
📎 [robo_advisor](https://github.com/datafox-tw/robo_advisor)

---

## 🟣 Senior Year — Information Retrieval and Exchange Period Exploration

### Information Retrieval and Text Mining (IRTM)
🔖 `RAG` `BM25` `Vector Retrieval` `GraphRAG`
Systematically compared multiple RAG strategies in a Traditional Chinese context. Developed my research capabilities in IR (Information Retrieval) and LLM retrieval.
📎 [IRTM_project](https://github.com/datafox-tw/IRTM_project)

---

## 🔴 First Year Master's — Deep Learning, LLM, and Research-Oriented

### Deep Learning and Applications — Financial Time Series Research
🔖 `GARCH` `LSTM` `TSMixer` `Loss Design`
Explored hybrid architectures combining traditional econometric models with deep learning. Attempted to reflect financial risk through loss design, representing a key highlight of my current research capabilities.
📎 [GLoVE](https://github.com/datafox-tw/GLoVE)

### Practical Computer Vision (AI Cup)
🔖 `3D Medical Imaging` `Low-Resolution Learning` `Paper Reproduction`
Achieved 56th place out of 568 teams. Completed the full competition process from paper reproduction to model tuning.
📎 [valve_abnormality_examination](https://github.com/datafox-tw/valve_abnormality_examination)

### Instruction Tuning — Classical Chinese ↔ Modern Chinese
🔖 `QLoRA` `LLM Fine-tuning` `Prompt Engineering`
Fully completed the fine-tuning process using QLoRA, learning how to fine-tune LLMs under resource constraints and design inference strategies.

---

## 🧭 How to Read This Portfolio

You can explore in different ways:
- **By Topic**: NLP / LLM, Finance × AI, Systems & Full-stack, Recommendation Systems
- **By Depth**: Basic Implementation → Model Training → System Integration → Research-Oriented

---

## ✨ Conclusion
This timeline shows not just my projects, but a transformation in how I approach problems: from "implementing models" to "integrating them into systems," and finally conducting research at the intersection of "Finance × AI."

</div>
