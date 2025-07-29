import os
import re

BASE_DIR = "Codex/Voyagers_I"

for filename in os.listdir(BASE_DIR):
  clean_name = re.sub(r'_([a-zA-Z])_', r'\1', filename) # removes spacing artifacts like _T_H_E -> _THE_
  clean_name = re.sub(r'__+','_', clean_name) # compress double underscores
  clean_name = clean_name.replace(" ","") # remove any literal spaces
  if filename != clean_name:
    os.rename(os.path.join(BASE_DIR, filename), os.path.join(BASE_DIR, clean_name))
    print(f"Renamed: {filename} -> {clean_name}")
