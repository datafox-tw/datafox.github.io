import os
import re
import glob
import time
import sys
from google import genai

def split_frontmatter(content):
    match = re.match(r'^(---\n.*?\n---\n)(.*)', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return "", content

def extract_yaml_field(frontmatter, field):
    match = re.search(rf'^{field}:\s*(["\']?)(.*?)\1\s*$', frontmatter, re.MULTILINE)
    if match:
        return match.group(2)
    return ""

def replace_yaml_field(frontmatter, field, new_value):
    # Escape quotes if necessary
    new_value = new_value.replace('"', '\\"')
    pattern = rf'^({field}:\s*)(["\']?)(.*?)\2(\s*)$'
    if re.search(pattern, frontmatter, re.MULTILINE):
        return re.sub(pattern, rf'\1"{new_value}"\4', frontmatter, count=1, flags=re.MULTILINE)
    else:
        # If field doesn't exist, append it before the closing ---
        return re.sub(r'\n---$', rf'\n{field}: "{new_value}"\n---', frontmatter)

def translate_content(client, title,subtitle, description, body):
    prompt = f"""You are a professional translator. Translate the following Chinese content into fluent English.
Maintain all markdown formatting, headings, links, and code blocks exactly as they are.

Output the translated content in the exact following format:
TITLE: [translated title]
SUBTITLE: [translated subtitle]
DESCRIPTION: [translated description]
BODY:
[translated body]

Here is the original content:
TITLE: {title},
SUBTITLE: {subtitle}
DESCRIPTION: {description}
BODY:
{body}"""
    
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
    elif out.startswith("```"):
        out = out[3:].strip()
        if out.endswith("```"):
            out = out[:-3].strip()

    title_match = re.search(r'^TITLE:\s*(.*?)$', out, re.MULTILINE)
    subtitle_match = re.search(r'^SUBTITLE:\s*(.*?)$', out, re.MULTILINE)
    desc_match = re.search(r'^DESCRIPTION:\s*(.*?)$', out, re.MULTILINE)
    
    # Body is everything after BODY:
    body_match = re.search(r'^BODY:\s*\n(.*)', out, re.DOTALL | re.MULTILINE)
    
    t_title = title_match.group(1).strip() if title_match else title
    t_subtitle = subtitle_match.group(1).strip() if subtitle_match else subtitle
    t_desc = desc_match.group(1).strip() if desc_match else description
    
    if not body_match:
        raise ValueError("Could not parse BODY from Gemini response")
    t_body = body_match.group(1).strip()
    
    return t_title, t_subtitle, t_desc, t_body

def process_file(filepath, client):
    en_filepath = filepath[:-9] + ".md"
    if os.path.exists(en_filepath):
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    frontmatter, body = split_frontmatter(content)
    
    if not body.strip():
        print(f"  -> Empty body, skipping.")
        return False
        
    title = extract_yaml_field(frontmatter, 'title')
    subtitle = extract_yaml_field(frontmatter, 'subtitle')
    description = extract_yaml_field(frontmatter, 'description')
    
    print(f"Translating: {filepath}")
    
    try:
        t_title, t_subtitle, t_desc, t_body = translate_content(client, title, description, body)
    except Exception as e:
        print(f"  -> Error translating: {e}")
        return False
        
    new_frontmatter = frontmatter
    if t_title and t_title != title:
        new_frontmatter = replace_yaml_field(new_frontmatter, 'title', t_title)
    if t_subtitle and t_subtitle != subtitle:
        new_frontmatter = replace_yaml_field(new_frontmatter, 'subtitle', t_subtitle)
    if t_desc and t_desc != description:
        new_frontmatter = replace_yaml_field(new_frontmatter, 'description', t_desc)
        
    with open(en_filepath, 'w', encoding='utf-8') as f:
        f.write(new_frontmatter + "\n\n" + t_body + "\n")
        
    print(f"  -> Successfully created {en_filepath}")
    return True

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY environment variable is not set.")
        sys.exit(1)
        
    client = genai.Client(api_key=api_key)
    
    md_files = glob.glob("content/**/*.zh-tw.md", recursive=True)
    
    translated_count = 0
    for filepath in md_files:
        success = process_file(filepath, client)
        if success:
            translated_count += 1
            print("  -> Sleeping 4 seconds to respect rate limits...")
            time.sleep(4)
            
    print(f"Done. Translated {translated_count} files.")

if __name__ == "__main__":
    main()
