import feedparser
import os
import re
import json
import sys
from datetime import datetime
from html.parser import HTMLParser
from zoneinfo import ZoneInfo
from google import genai

RSS_URL = "https://mshibanami.github.io/GitHubTrendingRSS/weekly/all.xml"
KEYWORDS = [
    'gemini', 'claude', 'gpt', 'llm', 'ai', 'artificial intelligence',
    'skill', 'skills',
]
TOP_N = 15
CONTENT_DIR = "content/posts"
TZ = ZoneInfo("Asia/Taipei")


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


def generate_content(repos):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set")

    client = genai.Client(api_key=api_key)

    repos_json = json.dumps(
        [{"name": r["name"], "description": r["description"], "language": r["language"]} for r in repos],
        ensure_ascii=False,
        indent=2,
    )

    prompt = f"""你是一位 AI/LLM 技術社群的技術寫作者。

以下是本週 GitHub Trending 前 {TOP_N} 名中篩選出的 AI 相關專案：
{repos_json}

請完成兩件事：

1. 為每個專案寫 150～200 字的繁體中文介紹：
   - 說明專案是什麼、解決什麼問題
   - 為何在 AI/LLM 領域值得關注
   - 口吻：技術部落客，自然有見地，不浮誇
   - 直接開始段落，不要加標題

2. 根據這批專案的整體主題，生成 4～6 個繁體中文標籤（一定要包含「GitHub趨勢」和「AI週報」）

嚴格用以下 JSON 格式回應，不要有任何其他文字：
{{
  "intros": [
    {{"name": "repo名稱（與輸入完全一致）", "intro": "介紹文字"}},
    ...
  ],
  "tags": ["GitHub趨勢", "AI週報", "..."]
}}"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()
    # strip markdown fences if model wraps in ```json
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    return json.loads(text)


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

    filename = now.strftime("%y%m%d_%H%M") + ".md"
    filepath = os.path.join(CONTENT_DIR, filename)

    os.makedirs(CONTENT_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Written to {filepath}")


if __name__ == "__main__":
    main()
