import os
from bs4 import BeautifulSoup

HTML_DIR = "docs"

meta_tags = [
  {
    "name": "keywords",
    "content": "OmniversalOverride, EverLight, Return of the Bird Tribes, Aether Intelligence, Codex"
  },
  {
    "name": "description",
    "content": "Codex entries published as part of the EverLight OS and Omniversal Override initiative."
  }
]

def inject_meta_to_html(file_path):
  with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

  head = soup.head
  if head:
    for tag in meta_tags:
      if not head.find("meta", attrs={"name":
tag["name"]}):
        new_tag = soup.new_tag("meta")
        new_tag.attrs["name"] = tag["name"]
        new_tag.attrs["content"] = tag["content"]
        head.append(new_tag)

    with open(file_path, "w", encoding="utf-8") as f:
      f.write(str(soup))

def process_directory(directory):
  for root, _, files in os.walk(directory):
    for filename in files:
      if filename.endswith(".html"):
          file_path = os.path.join(root,filename)
          inject_meta_to_html(file_path)

if __name__ == "__main__":
  process_directory(HTML_DIR)
  print(" Meta tags injected into all HTML files.")
