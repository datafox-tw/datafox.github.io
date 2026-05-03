"""
為 content/posts/ 下的文章自動生成 SEO slug，並以 aliases 保留舊 URL。

每篇文章會：
  1. 新增 slug: "seo-friendly-english-slug"  ← 成為新的 canonical URL
  2. 新增 aliases: ["/posts/260418_1600/"]   ← 舊 URL 自動 redirect 過去

用法：
  python scripts/gen_slugs.py          # dry-run，只印結果
  python scripts/gen_slugs.py --write  # 實際寫入
"""

import os
import re
import sys
import time
import argparse
from pathlib import Path
from dotenv import dotenv_values
from google import genai

POSTS_DIR = Path("content/posts")
ENV_FILE = Path(".env.local")
MODEL = "gemini-2.5-flash"

SLUG_PROMPT = """你是 SEO 專家。根據文章標題，生成一個英文 URL slug。

規則：
- 全小寫英文，用連字號 (-) 分隔
- 3～6 個單字，精準概括文章主題
- 優先使用技術關鍵字（例如 llmops、rag、hugo、ai-agent）
- 不要用冠詞 (a, the, an)、介係詞或連接詞填充
- 只回傳 slug 字串本身，不要有其他文字

範例輸入：datafox 竣工後記：2026 個人網站實戰指南
範例輸出：hugo-github-pages-personal-site-guide

範例輸入：為什麼「多說話」的 AI Agent，在金融場景可能是場災難？
範例輸出：verbose-ai-agent-financial-risk

範例輸入：六頂思考帽作為人機協作的新通訊協定
範例輸出：six-thinking-hats-human-ai-protocol
"""


def load_api_key():
    env = dotenv_values(ENV_FILE)
    key = env.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("找不到 GEMINI_API_KEY，請確認 .env.local 存在")
    return key


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not m:
        return None, text
    return m.group(1), m.group(2)


def has_slug(frontmatter):
    return bool(re.search(r"^slug:", frontmatter, re.MULTILINE))


def get_title(frontmatter):
    m = re.search(r'^title:\s*"(.+?)"', frontmatter, re.MULTILINE)
    return m.group(1) if m else ""


def stem_to_old_path(stem):
    """260418_1600 → /posts/260418_1600/"""
    return f"/posts/{stem}/"


def generate_slug(client, title):
    response = client.models.generate_content(
        model=MODEL,
        config={"system_instruction": SLUG_PROMPT},
        contents=title,
    )
    raw = response.text.strip().strip('"').strip("'").lower()
    # 確保只有合法字元
    raw = re.sub(r"[^a-z0-9-]", "-", raw)
    raw = re.sub(r"-{2,}", "-", raw).strip("-")
    return raw


def inject_slug_and_alias(frontmatter, slug, old_path):
    """在 date: 那行後面插入 slug 和 aliases。"""
    alias_line = f'aliases: ["{old_path}"]'
    slug_line = f"slug: {slug}"

    # 插在 date: 行之後
    fm = re.sub(
        r"(^date:.*$)",
        rf"\1\n{slug_line}\n{alias_line}",
        frontmatter,
        count=1,
        flags=re.MULTILINE,
    )
    return fm


def collect_posts():
    posts = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        if fm and not has_slug(fm):
            posts.append({
                "path": path,
                "stem": path.stem,          # e.g. "260418_1600"
                "frontmatter": fm,
                "body": body,
            })
    return posts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="實際寫入檔案")
    args = parser.parse_args()

    api_key = load_api_key()
    client = genai.Client(api_key=api_key)

    posts = collect_posts()
    if not posts:
        print("所有文章都已有 slug，無需更新。")
        return

    print(f"找到 {len(posts)} 篇需要產生 slug 的文章\n")
    if not args.write:
        print(">>> DRY-RUN 模式：只印出結果，不寫入檔案")
        print(">>> 加上 --write 參數才會實際修改\n")
        print("=" * 60)

    for i, post in enumerate(posts, 1):
        title = get_title(post["frontmatter"])
        old_path = stem_to_old_path(post["stem"])

        print(f"[{i}/{len(posts)}] {post['path'].name}")
        print(f"  標題  : {title}")

        slug = generate_slug(client, title)
        print(f"  slug  : {slug}")
        print(f"  alias : {old_path}\n")

        if args.write:
            new_fm = inject_slug_and_alias(post["frontmatter"], slug, old_path)
            new_text = f"---\n{new_fm}\n---\n{post['body']}"
            post["path"].write_text(new_text, encoding="utf-8")
            print(f"  ✓ 已寫入 {post['path'].name}\n")

        if i < len(posts):
            time.sleep(1)

    if args.write:
        print(f"完成！已更新 {len(posts)} 篇文章。")
        print("\n提醒：執行 hugo build 後，舊 URL 會生成 redirect HTML，確認沒問題再 push。")
    else:
        print("=" * 60)
        print("Dry-run 完成。執行 `python scripts/gen_slugs.py --write` 寫入。")


if __name__ == "__main__":
    main()
