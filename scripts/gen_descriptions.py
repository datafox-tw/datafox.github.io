"""
批量為 content/posts/ 下 description 為空的文章生成 SEO meta description。

用法：
  python scripts/gen_descriptions.py          # dry-run，只印結果
  python scripts/gen_descriptions.py --write  # 實際寫入檔案
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

SYSTEM_PROMPT = """你是 SEO 文案專家。根據文章標題與內文，生成一段繁體中文 meta description。

規則：
- 長度：40～120 字（中文字符計算）
- 必須涵蓋文章核心關鍵字
- 口吻自然，像人寫的，不像機器摘要
- 不要重複標題，補充標題沒說清楚的「這篇文章在說什麼」
- 只回傳 description 字串本身，不要加引號或任何前綴
"""


def load_api_key():
    env = dotenv_values(ENV_FILE)
    key = env.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("找不到 GEMINI_API_KEY，請確認 .env.local 存在")
    return key


def parse_frontmatter(text):
    """Return (frontmatter_str, body_str) or (None, text) if no frontmatter."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not m:
        return None, text
    return m.group(1), m.group(2)


def needs_description(frontmatter):
    return bool(re.search(r'^description:\s*""?\s*$', frontmatter, re.MULTILINE))


def get_title(frontmatter):
    m = re.search(r'^title:\s*"(.+?)"', frontmatter, re.MULTILINE)
    return m.group(1) if m else ""


def collect_posts():
    posts = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        if fm and needs_description(fm):
            posts.append({"path": path, "frontmatter": fm, "body": body, "full": text})
    return posts


def generate_description(client, title, body):
    # Strip HTML/shortcodes and trim body to ~800 chars to save tokens
    clean_body = re.sub(r"\{\{[^}]*\}\}", "", body)
    clean_body = re.sub(r"<[^>]+>", "", clean_body)
    clean_body = re.sub(r"\n{3,}", "\n\n", clean_body).strip()[:800]

    prompt = f"標題：{title}\n\n內文節錄：\n{clean_body}"
    response = client.models.generate_content(
        model=MODEL,
        config={"system_instruction": SYSTEM_PROMPT},
        contents=prompt,
    )
    return response.text.strip().strip('"').strip("'")


def update_description(frontmatter, description):
    return re.sub(
        r'^(description:\s*)""?\s*$',
        f'description: "{description}"',
        frontmatter,
        flags=re.MULTILINE,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="實際寫入檔案")
    args = parser.parse_args()

    api_key = load_api_key()
    client = genai.Client(api_key=api_key)

    posts = collect_posts()
    if not posts:
        print("所有文章都已有 description，無需更新。")
        return

    print(f"找到 {len(posts)} 篇需要補 description 的文章\n")
    if not args.write:
        print(">>> DRY-RUN 模式：只印出結果，不寫入檔案")
        print(">>> 加上 --write 參數才會實際修改\n")
        print("=" * 60)

    for i, post in enumerate(posts, 1):
        title = get_title(post["frontmatter"])
        print(f"[{i}/{len(posts)}] {post['path'].name}")
        print(f"  標題：{title}")

        description = generate_description(client, title, post["body"])
        print(f"  生成：{description}\n")

        if args.write:
            new_fm = update_description(post["frontmatter"], description)
            new_text = f"---\n{new_fm}\n---\n{post['body']}"
            post["path"].write_text(new_text, encoding="utf-8")
            print(f"  ✓ 已寫入 {post['path'].name}\n")

        # 避免打太快被 rate limit
        if i < len(posts):
            time.sleep(1)

    if args.write:
        print(f"完成！已更新 {len(posts)} 篇文章。")
    else:
        print("=" * 60)
        print("Dry-run 完成。執行 `python scripts/gen_descriptions.py --write` 寫入。")


if __name__ == "__main__":
    main()
