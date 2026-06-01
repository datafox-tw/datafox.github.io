import glob
import re

files = glob.glob("content/posts/*.md")
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove aliases: [...] line
    new_content = re.sub(r'^aliases:\s*\[.*?\]\n', '', content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Fixed {f}")
