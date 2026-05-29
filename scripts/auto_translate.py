import os
import re
import glob
import time
import sys
from google import genai

def split_frontmatter(content):
    # Regex to match frontmatter (yaml block between `---` at start of file)
    match = re.match(r'^(---\n.*?\n---\n)(.*)', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return "", content

def clean_body(body):
    # Remove existing lang-toggle shortcode if present
    body = re.sub(r'\{\{<\s*lang-toggle\s*>\}\}\s*\n?', '', body)
    
    # If the body is already wrapped in <div class="lang-zh">...</div>, unwrap it
    # We do a somewhat flexible regex to remove the opening and closing tags.
    # Note: this assumes there's only one main wrapper.
    body = body.strip()
    if body.startswith('<div class="lang-zh">'):
        body = body[len('<div class="lang-zh">'):]
        if body.endswith('</div>'):
            body = body[:-len('</div>')]
        
    return body.strip()

def translate_text(client, text):
    prompt = f"""You are a professional translator. Translate the following Chinese markdown content into fluent English.
Maintain all markdown formatting, headings, links, and code blocks exactly as they are.
Only output the translated text without any other conversational text. Do not wrap in ```markdown if not necessary.

{text}"""
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    
    out = response.text.strip()
    # Strip markdown block quotes if Gemini adds them
    if out.startswith("```markdown"):
        out = out[len("```markdown"):].strip()
        if out.endswith("```"):
            out = out[:-3].strip()
    return out

def process_file(filepath, client):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already has English translation
    if '<div class="lang-en">' in content or 'class="lang-en"' in content:
        return False
        
    print(f"Translating: {filepath}")
    frontmatter, body = split_frontmatter(content)
    
    if not body.strip():
        print(f"  -> Empty body, skipping.")
        return False

    clean_zh = clean_body(body)
    
    # Translate
    try:
        en_translated = translate_text(client, clean_zh)
    except Exception as e:
        print(f"  -> Error translating: {e}")
        return False
        
    new_body = f"""{{{{< lang-toggle >}}}}

<div class="lang-zh">

{clean_zh}

</div>

<div class="lang-en">

{en_translated}

</div>
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + new_body)
        
    print(f"  -> Successfully updated {filepath}")
    return True

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY environment variable is not set.")
        sys.exit(1)
        
    client = genai.Client(api_key=api_key)
    
    # We will search all markdown files in the content directory
    md_files = glob.glob("content/**/*.md", recursive=True)
    
    translated_count = 0
    for filepath in md_files:
        # Skip some files if necessary (e.g. _index.md might need translation too, but let's allow it)
        success = process_file(filepath, client)
        if success:
            translated_count += 1
            # Sleep to avoid hitting rate limit (15 RPM for free tier)
            print("  -> Sleeping 4 seconds to respect rate limits...")
            time.sleep(4)
            
    print(f"Done. Translated {translated_count} files.")

if __name__ == "__main__":
    main()
