import feedparser
import os
import re
import json
import sys
import random
import time
from datetime import datetime
from html.parser import HTMLParser
from zoneinfo import ZoneInfo
from google import genai
from google.genai import errors

RSS_URL = "https://mshibanami.github.io/GitHubTrendingRSS/weekly/all.xml"
KEYWORDS = [
    'gemini', 'claude', 'gpt', 'llm', 'ai', 'artificial intelligence',
    'skill', 'skills',
]
TOP_N = 15
CONTENT_DIR = "content/news"
TZ = ZoneInfo("Asia/Taipei")

PRIMARY_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
FALLBACK_MODEL = os.environ.get("GEMINI_FALLBACK_MODEL", "gemini-3.5-flash")


class _HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self._parts = []

    def handle_data(self, data):
        self._parts.append(data)

    def get_text(self):
        return " ".join(self._parts)


def strip_html(text):
    s = _HTMLStripper()
    s.feed(text)
    return s.get_text()


def fetch_trending(n=15):
    feed = feedparser.parse(RSS_URL)
    repos = []
    for entry in feed.entries[:n]:
        name = entry.get("title", "").strip()
        raw = entry.get("summary", "") or entry.get("description", "")
        description = strip_html(raw).strip()
        link = entry.get("link", "").strip()
        language = ""
        for tag in entry.get("tags", []):
            if tag.get("label") == "Language":
                language = tag.get("term", "")
                break
        repos.append({"name": name, "description": description, "link": link, "language": language})
    return repos


def keyword_filter(repos):
    matched = []
    for repo in repos:
        text = (repo["name"] + " " + repo["description"]).lower()
        if any(kw in text for kw in KEYWORDS):
            matched.append(repo)
    return matched


def call_gemini_with_retry(client, prompt, max_retries=4):
    """
    呼叫 Gemini API，具備指數退避重試（因應 503 UNAVAILABLE, 429 等暫時性錯誤）。
    若主模型重試後仍持續失敗，自動切換至備用模型。
    """
    models_to_try = [PRIMARY_MODEL]
    if FALLBACK_MODEL and FALLBACK_MODEL != PRIMARY_MODEL:
        models_to_try.append(FALLBACK_MODEL)

    last_err = None
    for model_name in models_to_try:
        for attempt in range(1, max_retries + 1):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )
                return response.text.strip()
            except errors.APIError as e:
                last_err = e
                code = getattr(e, "code", None)
                is_transient = code in (429, 500, 502, 503, 504) or "503" in str(e) or "UNAVAILABLE" in str(e)
                if not is_transient and attempt == 1:
                    raise
                if attempt < max_retries:
                    sleep_time = (2 ** attempt) + random.uniform(0.5, 2.0)
                    print(f"    [Retry {attempt}/{max_retries}] Model {model_name} error ({code or e}): waiting {sleep_time:.1f}s...")
                    time.sleep(sleep_time)
                else:
                    print(f"    [Warning] Model {model_name} failed after {max_retries} attempts: {e}")
            except Exception as e:
                last_err = e
                if attempt < max_retries:
                    sleep_time = (2 ** attempt) + random.uniform(0.5, 2.0)
                    print(f"    [Retry {attempt}/{max_retries}] Unexpected error: {e}. Waiting {sleep_time:.1f}s...")
                    time.sleep(sleep_time)
                else:
                    print(f"    [Warning] Failed after {max_retries} attempts: {e}")

        if model_name != models_to_try[-1]:
            print("    [Info] Switching to fallback model...")

    raise last_err


def generate_content(repos):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set")

    client = genai.Client(api_key=api_key)

    intros = []
    
    print("  -> Generating intros one by one to avoid context fatigue...")
    for idx, r in enumerate(repos):
        repo_json = json.dumps(
            {"name": r["name"], "description": r["description"], "language": r["language"]},
            ensure_ascii=False,
            indent=2,
        )
        
        prompt = f"""你是一位 AI/LLM 技術社群的技術寫作者。

以下是一個 GitHub Trending 上熱門的 AI 相關專案：
{repo_json}

請為這個專案寫 150～200 字的繁體中文介紹：
- 說明專案是什麼、解決什麼問題
- 為何在 AI/LLM 領域值得關注
- 口吻：技術部落客，自然有見地，不浮誇
- 直接開始介紹段落，不要加標題

嚴格用以下 JSON 格式回應，不要有任何其他文字：
{{
  "name": "{r['name']}",
  "intro": "介紹文字"
}}"""

        try:
            text = call_gemini_with_retry(client, prompt)
            text = re.sub(r"^```(?:json)?\s*", "", text)
            text = re.sub(r"\s*```$", "", text)
            res_json = json.loads(text)
            intros.append(res_json)
        except Exception as e:
            print(f"    [Warning] Failed to generate intro for {r['name']}: {e}")
            intros.append({"name": r["name"], "intro": r["description"]})

        # 請求之間稍作停頓，降低 rate limit 與尖峰負載機率
        if idx < len(repos) - 1:
            time.sleep(1.5)

    print("  -> Generating overall tags...")
    repo_names = [r["name"] for r in repos]
    tags_prompt = f"""請根據以下本週 GitHub Trending AI 專案清單：
{json.dumps(repo_names, ensure_ascii=False)}

生成 4～6 個繁體中文標籤（一定要包含「GitHub趨勢」和「AI週報」）。
嚴格用以下 JSON 格式回應，不要有任何其他文字：
{{
  "tags": ["GitHub趨勢", "AI週報", "..."]
}}"""

    try:
        tags_text = call_gemini_with_retry(client, tags_prompt)
        tags_text = re.sub(r"^```(?:json)?\s*", "", tags_text)
        tags_text = re.sub(r"\s*```$", "", tags_text)
        tags_json = json.loads(tags_text)
        tags = tags_json.get("tags", ["GitHub趨勢", "AI週報"])
    except Exception as e:
        print(f"    [Warning] Failed to generate tags: {e}. Using default tags.")
        tags = ["GitHub趨勢", "AI週報"]

    return {
        "intros": intros,
        "tags": tags
    }


def build_markdown(repos, generated, now):
    date_display = now.strftime("%Y/%m/%d")
    date_iso = now.strftime("%Y-%m-%d")

    intro_map = {item["name"]: item["intro"] for item in generated["intros"]}
    tags_yaml = json.dumps(generated["tags"], ensure_ascii=False)

    sections = []
    for i, repo in enumerate(repos, 1):
        lang_part = f"**語言**: {repo['language']} ｜ " if repo["language"] else ""
        intro = intro_map.get(repo["name"], repo["description"])
        sections.append(
            f"## {i}. [{repo['name']}]({repo['link']})\n\n"
            f"> {lang_part}[→ GitHub 連結]({repo['link']})\n\n"
            f"{intro}\n"
        )

    body = "\n---\n\n".join(sections)

    return (
        f'---\n'
        f'title: "{date_display} 本週 GitHub AI 趨勢"\n'
        f'date: {date_iso}\n'
        f'draft: false\n'
        f'tags: {tags_yaml}\n'
        f'ShowToc: true\n'
        f'description: "本週 GitHub Trending 前 {TOP_N} 名中篩選出的 AI/LLM 相關專案整理"\n'
        f'---\n\n'
        f'本週從 GitHub Trending 前 {TOP_N} 名中，篩選出 **{len(repos)} 個** AI/LLM 相關專案：\n\n'
        f'---\n\n'
        f'{body}'
    )


def main():
    now = datetime.now(tz=TZ)

    print("Fetching GitHub Trending RSS...")
    repos = fetch_trending(TOP_N)
    print(f"Fetched {len(repos)} repos")

    matched = keyword_filter(repos)
    print(f"Keyword matched: {len(matched)} repos")

    if not matched:
        print("No AI-related repos found this week — skipping post.")
        sys.exit(0)

    for r in matched:
        print(f"  - {r['name']}")

    print("Calling Gemini API...")
    generated = generate_content(matched)

    markdown = build_markdown(matched, generated, now)

    existing = [
        f for f in os.listdir(CONTENT_DIR)
        if re.match(r"trending_ep\d+\.md", f)
    ] if os.path.isdir(CONTENT_DIR) else []
    next_ep = len(existing) + 1
    filename = f"trending_ep{next_ep}.md"
    filepath = os.path.join(CONTENT_DIR, filename)

    os.makedirs(CONTENT_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Written to {filepath}")


if __name__ == "__main__":
    main()
