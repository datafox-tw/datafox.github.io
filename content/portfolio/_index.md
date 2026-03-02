---
title: "作品集導覽 (Portfolio Guide)"
description: "我的背景橫跨財務分析、量化建模與系統導向的軟體開發，這裡呈現我的技術成長與專案路徑。"
date: 2026-03-02
draft: false
hideMeta: true
---

這個作品集導覽提供了一條清楚的閱讀路徑，而不單純是羅列所有專案。

我的背景橫跨財務分析、量化建模與系統導向的軟體開發，因此這裡的專案更重視「問題如何被拆解與重構」，而不只是功能或模型表現。

這份 portfolio 會持續滾動式更新。  
每個被選入的專案，除了說明做了什麼，也會標註：

- 初次完成的時間與背景脈絡
- 後續 refactor 的時間點與動機
- 現在這個版本想解決的問題

因此閱讀這這裡的方式，會比較像是在看一條隨時間演化的工程軌跡。

---

## 🔎 快速導覽（給不同背景的朋友）

不同領域的讀者可以從下表快速找到最相關的專案與技術內容。

| 如果你正在找…                               | 建議閱讀的專案                                                                                                                                                                                                       | 你會看到的能力與內容                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| Finance × AI / Quant / FinTech        | [GLoVE](https://github.com/datafox-tw/GLoVE) <br> [robo_advisor](https://github.com/datafox-tw/robo_advisor) <br> [Meme_stock_analysis_and_prediction](https://github.com/datafox-tw/Meme_stock_analysis_and_prediction) | GARCH × 深度學習混合建模、模組化金融分析系統、另類資料與市場訊號研究                         |
| LLM / RAG / NLP 系統開發                  | 深度學習 HW3 – RAG system <br> [IRTM_project](https://github.com/datafox-tw/IRTM_project) <br> [Toxic Comment Detector（BERT & GPT 版本）](https://github.com/datafox-tw/toxic_comment_detector)                                                                                         | Retriever / reranker 微調、繁體中文 RAG 策略實驗、LLM 出現前後的完整 NLP pipeline |
| LLM 微調 / Transformer 訓練               | Instruction tuning（QLoRA） <br> Chinese Extractive QA（BERT）                                                                                                                                                               | 參數高效微調、span prediction 訓練流程、prompt 與推論策略設計                     |
| Machine Learning / Deep Learning 基礎能力 | [data_analysis](https://github.com/datafox-tw/data_analysis) <br> [AI Cup 3D 醫學影像建模與預測](https://github.com/datafox-tw/valve_abnormality_examination)                                                                                                                                         | End-to-end 建模流程、時間序列預測、論文復現與實驗設計能力                             |
| 系統整合 / 全端工程                           | [CloudNative_Stadium_System](https://github.com/datafox-tw/CloudNative_Stadium_System) <br> [Airlines_DBMS](https://github.com/datafox-tw/Airlines_DBMS)                                                                 | React + Express 架構、API 測試與壓力測試、資料庫 schema 與交易設計                |
| 推薦系統 / 資料探勘                           | [BDA2023_final_apriori](https://github.com/datafox-tw/BDA2023_final_apriori)                                                                                                                                             | 關聯規則推薦系統與商業問題轉換能力                                              |
| 產品導向的 AI 應用                           | [youtube_nlp_analysis](https://github.com/datafox-tw/youtube_nlp_analysis)                                                                                                                                               | 從使用者資料推導內容策略與商業洞察                                              |
| 程式設計基礎與系統思維起點                         | [PBC2021-final](https://github.com/datafox-tw/PBC2021-final) <br> [windowskill](https://github.com/datafox-tw/windowskill_windowOS)                                                                                               | OOP 設計、互動式系統實作、C++ 與 Python 的實作差異                              |

---

## 🧭 建議閱讀路線

- **GenAI / LLM 相關 →** RAG system → IRTM → QLoRA
- **Quant / FinTech 相關 →** GLoVE → Robo-advisor
- **軟體工程 / 全端 →** Cloud Native → DBMS
- **ML Engineer →** Data Analytics → AI Cup

👉 [**點此查看：完整的專案時間軸導覽**](/portfolio/timeline)

---

## 💡 我目前的核心關注方向

- LLM / RAG 系統設計與最佳化
- Finance × AI 的可驗證建模
- 可落地的 Machine Learning 系統

---

## 建議閱讀專案

如果你是第一次來，建議從下列幾個專案開始，它們代表我在不同階段的思考方式：

### 1. Airlines_DBMS (資料庫設計與系統重構)
這是我將學術作業轉化為可操作系統的代表作。
- **2023.12 初版**：學習 ER model 與正規化。
- **2026.02 重構**：強化 schema 與應用層設計，讓使用者可實際操作查詢。

### 2. stock_analysis (金融量化工作流)
從簡單的分析導向轉向系統化的研究工作流。
- **2023.06 初版**：基礎策略發想。
- **2026.03 重構**：模組化資料處理，建立可重現的實驗結構。

---

## 最後
這份作品集也是我的工程筆記。如果你是為了面試或合作而來，謝謝你從這份導覽開始認識我。
