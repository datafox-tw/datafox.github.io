import os
import glob
import re

def main():
    md_files = glob.glob("content/**/*.md", recursive=True)
    md_files = [f for f in md_files if not f.endswith(".en.md")]

    count = 0
    en_count = 0

    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "<div class=\"lang-zh\">" not in content and "{{< lang-toggle >}}" not in content:
            continue
            
        print(f"Processing {filepath}")
        count += 1
        
        # Split frontmatter
        match = re.match(r'^(---.*?---)\s*(.*)', content, re.DOTALL)
        if not match:
            print(f"  No frontmatter found in {filepath}")
            continue
            
        frontmatter = match.group(1)
        body = match.group(2)
        
        # Extract zh and en using safe splitting
        clean_zh = ""
        en_text = ""
        
        parts = body.split('<div class="lang-en">')
        zh_part = parts[0]
        if len(parts) > 1:
            en_part = parts[1]
        else:
            en_part = ""

        # Clean zh_part
        if '<div class="lang-zh">' in zh_part:
            zh_part = zh_part.split('<div class="lang-zh">', 1)[1]
            if zh_part.strip().endswith('</div>'):
                zh_part = zh_part.strip()[:-6]
        
        clean_zh = re.sub(r'\{\{<\s*lang-toggle\s*>\}\}\s*\n?', '', zh_part).strip()
        
        # Clean en_part
        if en_part.strip().endswith('</div>'):
            en_text = en_part.strip()[:-6].strip()
        else:
            en_text = en_part.strip()
            
        # Check if en_text is valid (not fake)
        is_valid_en = False
        if en_text:
            zh_chars = len(re.findall(r"[\u4e00-\u9fff]", en_text))
            if zh_chars <= 20:
                is_valid_en = True
                
        # Write clean zh back
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"{frontmatter}\n\n{clean_zh}\n")
            
        # Write en file if valid
        if is_valid_en:
            en_filepath = filepath[:-3] + ".en.md"
            with open(en_filepath, "w", encoding="utf-8") as f:
                f.write(f"{frontmatter}\n\n{en_text}\n")
            print(f"  Created {en_filepath}")
            en_count += 1
        else:
            print(f"  Skipped creating .en.md (fake translation or missing)")
            
    print(f"\nMigration complete: {count} files processed, {en_count} .en.md files created.")

if __name__ == "__main__":
    main()
