import os
import re
import glob
import time
import sys
from google import genai

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def extract_yaml_field(frontmatter, field):
    match = re.search(rf'^{field}:\s*(["\']?)(.*?)\1\s*$', frontmatter, re.MULTILINE)
    if match:
        return match.group(2)
    return ""

def replace_yaml_field(frontmatter, field, new_value):
    new_value = new_value.replace('"', '\\"')
    pattern = rf'^({field}:\s*)(["\']?)(.*?)\2(\s*)$'
    if re.search(pattern, frontmatter, re.MULTILINE):
        return re.sub(pattern, rf'\1"{new_value}"\4', frontmatter, count=1, flags=re.MULTILINE)
    else:
        return re.sub(r'\n---$', rf'\n{field}: "{new_value}"\n---', frontmatter)

def translate_text(client, text, is_title=False):
    prompt = f"Translate this {'title' if is_title else 'description'} to English concisely. Output ONLY the English text, no quotes or extra text.\n\n{text}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text.strip().strip('"\'')

def process_file(filepath, client):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    match = re.match(r'^(---\n.*?\n---\n)(.*)', content, re.DOTALL)
    if not match:
        return False
        
    frontmatter = match.group(1)
    body = match.group(2)
    
    title = extract_yaml_field(frontmatter, 'title')
    description = extract_yaml_field(frontmatter, 'description')
    
    needs_update = False
    new_title = title
    new_description = description
    
    if has_chinese(title):
        print(f"Translating title for {filepath}")
        new_title = translate_text(client, title, is_title=True)
        needs_update = True
        
    if has_chinese(description):
        print(f"Translating description for {filepath}")
        new_description = translate_text(client, description, is_title=False)
        needs_update = True
        
    if needs_update:
        new_frontmatter = frontmatter
        if new_title != title:
            new_frontmatter = replace_yaml_field(new_frontmatter, 'title', new_title)
        if new_description != description:
            new_frontmatter = replace_yaml_field(new_frontmatter, 'description', new_description)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_frontmatter + body)
        return True
        
    return False

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY environment variable is not set.")
        sys.exit(1)
        
    client = genai.Client(api_key=api_key)
    
    md_files = glob.glob("content/**/*.en.md", recursive=True)
    
    count = 0
    for filepath in md_files:
        if process_file(filepath, client):
            count += 1
            time.sleep(4)
            
    print(f"Done. Translated frontmatter for {count} files.")

if __name__ == "__main__":
    main()
