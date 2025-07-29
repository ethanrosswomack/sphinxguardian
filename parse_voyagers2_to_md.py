import fitz  # PyMuPDF
import os
import re

pdf_path = "Source/voyagers-2-secrets-of-amenti.pdf"
output_dir = "Codex/Voyagers_II"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# More flexible chapter title matching
chapter_pattern = re.compile(
    r'^(\d{1,2}[\w\/-]*\s+[A-Z][^\n]+|[A-Z][^\n]{10,})', re.IGNORECASE
)

chapter_index = 1
current_chapter = None
chapter_text = ""

for page_num in range(len(doc)):
    text = doc[page_num].get_text("text")
    lines = text.split("\n")

    for line in lines:
        line = line.strip()
        match = chapter_pattern.match(line)

        if match:
            if chapter_text:
                filename = f"Entry_002_{chapter_index:02d}_{current_chapter.replace(' ', '_').replace('/', '-')}.md"
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "w") as f:
                    f.write(f"# {current_chapter}\n\n")
                    f.write(chapter_text.strip())
                chapter_index += 1

            chapter_title = match.group(0)
            current_chapter = chapter_title.replace(":", "").strip()
            chapter_text = ""

        if current_chapter:
            chapter_text += line + "\n"

# Save final chapter
if current_chapter and chapter_text:
    filename = f"Entry_002_{chapter_index:02d}_{current_chapter.replace(' ', '_').replace('/', '-')}.md"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w") as f:
        f.write(f"# {current_chapter}\n\n")
        f.write(chapter_text.strip())
