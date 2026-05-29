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
        
        # Extract zh and en
        zh_match = re.search(r'<div class="lang-zh">(.*?)</div>', body, re.DOTALL)
        en_match = re.search(r'<div class="lang-en">(.*?)</div>', body, re.DOTALL)
        
        clean_zh = ""
        if zh_match:
            clean_zh = zh_match.group(1).strip()
        else:
            # If no lang-zh block, try removing lang-toggle manually
            clean_zh = re.sub(r'\{\{<\s*lang-toggle\s*>\}\}\s*\n?', '', body).strip()
            # Remove any standalone lang-en blocks just in case
            clean_zh = re.sub(r'<div class="lang-en">.*?</div>', '', clean_zh, flags=re.DOTALL).strip()
            clean_zh = re.sub(r'<div class="lang-zh">.*?</div>', '', clean_zh, flags=re.DOTALL).strip()

        en_text = ""
        if en_match:
            en_text = en_match.group(1).strip()
            
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
