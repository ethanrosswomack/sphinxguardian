import fitz # PyMuPDF

doc = fitz.open("Source/voyagers-2-secrets-of-amenti.pdf")

for i in range(10,20): # First 10 pages
  print(f"\n\n-- Page {i+1} ---\n")
  print(doc[i].get_text("text"))
