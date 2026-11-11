# CLAUDE.md — datafox.tw 個人網站

> AI 助手請先讀完本文件再動手。本文件是這個專案的「單一事實來源」：結構、格式、流程都以這裡為準。

## 1. 專案目的

datafox.tw 是柯宥圻 (Yuchi Ko, datafox) 的個人網站，內容包含技術筆記、作品集、Podcast、每週 GitHub AI 趨勢、Coffee Chat 預約。
- 受眾：潛在合作對象、面試官、對 AI 系統 / LLMOps / Agentic AI 有興趣的讀者。
- 原則：**內容優先**。新增內容不需要碰程式碼或版型，只要新增 Markdown 檔。

## 2. 技術棧

- 靜態網站產生器：**Hugo**（設定檔 `hugo.yaml`），主題 **PaperMod**（`themes/PaperMod`，git submodule，**不要修改**）。
- 客製化只放在 `layouts/`（覆寫主題）與 `assets/`、`static/`。
- 部署：push 到 `main` → GitHub Actions（`.github/workflows/hugo.yml`）→ GitHub Pages → 網域 `datafox.tw`。
- 本機預覽：`hugo server -D`（`-D` 會顯示 `draft: true` 的文章）。建置檢查：`hugo --gc --minify`。

## 3. 目錄結構

```
content/
  posts/        技術筆記與隨筆（最常新增）
  news/         每週 GitHub AI 趨勢（由 scripts/weekly_github_ai.py 自動產生，不要手寫）
  portfolio/    作品集、時間軸、證書
  podcast/      Podcast 列表
  coffeechat/   Coffee Chat 說明
  about/        關於我
layouts/        覆寫 PaperMod 的版型 partial
static/images/  圖片（引用路徑 /images/xxx.jpg）
scripts/        自動化腳本（翻譯、週報、slug/description 產生）
.github/workflows/  hugo.yml（部署）、auto_translate.yml（翻譯）、weekly-github-ai.yml（週報）
```

## 4. 雙語規則（最重要）

網站有兩種語言：**中文 `zh-tw`（原稿）** 與 **英文 `en`（自動翻譯）**。

| 檔案 | 語言 | 誰負責 |
|---|---|---|
| `名稱.zh-tw.md` | 繁體中文 | **人 / AI 撰寫**（原稿） |
| `名稱.md` | English | `scripts/auto_translate.py` 以 Gemini 自動產生 |

- 新增內容時 **只寫 `.zh-tw.md`**。push 後 `auto_translate.yml` 會產生對應英文檔並自動 commit。
- 若英文檔已存在，翻譯腳本會跳過它——所以修改中文後，若要更新英文，需手動刪除舊的 `.md` 再 push，或直接改英文檔。
- 不要手寫英文檔，除非使用者明確要求。

## 5. 新增一篇文章（posts）的 SOP

1. **檔名**：`content/posts/YYMMDD_HHMM.zh-tw.md`（例：`261111_2030.zh-tw.md`），用現在時間，不要用中文或空白。
2. **Front matter**（必填欄位，順序固定）：

```yaml
---
title: "文章標題"
date: 2026-11-11
slug: english-kebab-case-slug     # 純小寫英文與連字號，網址會是 /posts/<檔名>/
draft: false
ShowToc: true
subtitle: "一句話副標（可省略）"
description: "100~200 字摘要，用於 SEO 與列表預覽"
tags: ["標籤1", "標籤2"]          # 可省略
---
```

3. **內文**：
   - 用繁體中文（台灣用語），語氣為第一人稱、口語但有結構。
   - 小節用 `##`，不要使用 `#`（標題已由 front matter 的 `title` 產生）。
   - 程式碼必須標明語言（```python）。
   - 圖片放 `static/images/`，在文中用 `![說明](/images/檔名.png)`，必須有 alt 文字。
4. **驗證**：跑 `hugo --gc --minify`，確認沒有錯誤與 warning。
5. 草稿用 `draft: true`；準備發佈才改成 `false`。

## 6. 其他區塊的規則

- `news/`：**禁止手動新增或修改**，由每週日的 workflow 自動生成。
- `portfolio/`：條列式、以時間倒序；新增項目時保持與既有 `timeline.zh-tw.md` 相同的格式。
- 新增頁面區塊（例如新的 section）：需要同時修改 `hugo.yaml` 中 **zh-tw 與 en 兩份** `menu.main` 與 `permalinks`，並建立 `_index.md` 與 `_index.zh-tw.md`。

## 7. 風格與設計

- 沿用 PaperMod 的極簡、可讀性優先風格；`defaultTheme: auto`（支援深淺色）。
- 不引入新的 CSS 框架或 JS 套件；需要客製時，寫在 `layouts/partials/extend_head.html`。
- 站內連結用相對路徑（`/posts/xxx/`），外部連結用完整 URL。

## 8. AI 助手行為準則

**可以做**
- 新增 / 修改 `content/` 下的中文原稿。
- 依第 5 節的格式生成 front matter 與 slug、description。
- 修改 `layouts/` 以調整版型（先說明改動範圍）。

**不可以做（除非使用者明確要求）**
- 修改 `themes/PaperMod`、`public/`、`resources/`（建置產物，已 gitignore）。
- 讀取、輸出或提交 `.env`、`.env.local`、任何 API key。
- 手動編輯 `content/news/`。
- 刪除既有文章，或更動既有文章的 `slug`（會破壞舊網址）。
- `git push`、`git commit`：先給出變更摘要，等使用者同意。

**完成任務前的檢查清單**
- [ ] 檔名符合 `YYMMDD_HHMM.zh-tw.md`
- [ ] front matter 欄位齊全、`slug` 不重複
- [ ] `hugo --gc --minify` 通過
- [ ] 沒有動到禁止區域
- [ ] 用一兩句話回報：新增 / 修改了哪些檔案
