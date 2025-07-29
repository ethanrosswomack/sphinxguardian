import fitz # PyMuPDF
import os
import re

PDF_PATH = "Source/voyagers-1-the-sleeping-abductees.pdf"
OUTPUT_DIR = "Codex/Voyagers_I"

os.makedirs(OUTPUT_DIR, exist_ok=True)

doc = fitz.open(PDF_PATH)
chapter_text = ""
current_chapter = "Prologue"
chapter_index = 1

# Regex pattern to detect chapter titles (customize this as needed)
chapter_pattern = re.compile(r'^(Chapter\s+\d+|Prologue|Introduction|Section\s+\d+):?\s*(.+)?',
re.IGNORECASE)

for page_num in range(len(doc)):
  text = doc[page_num].get_text("text")
  lines = text.split("\n")

  for line in lines:
    line = line.strip()
    match = chapter_pattern.match(line)

    if match:
      # Save current chapter to file
      if chapter_text:
        filename = f"Entry_001_{chapter_index:02d}_{current_chapter.replace('','_')}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w") as f:
          f.write(f"# {current_chapter}\n\n")
          f.write(chapter_text.strip())
        chapter_index += 1
        chapter_text = ""

      # Start new chapter
      chapter_title = match.group(0)
      current_chapter = chapter_title.replace(":", "").strip()
    else:
      chapter_text += line + "\n"

# Save the final chunk
if chapter_text:
    filename = f"Entry_001_{chapter_index:02d}_{current_chapter.replace('','_')}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w") as f:
      f.write(f"# {current_chapter}\n\n")
      f.write(chapter_text.strip())

print(f"Chapters extracted to {OUTPUT_DIR}")
