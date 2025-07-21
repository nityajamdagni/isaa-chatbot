import fitz  # PyMuPDF
import re
import json

# Step 1: Open the cleaned PDF
pdf_path = "ISAA_Questions.pdf"
doc = fitz.open(pdf_path)

# Step 2: Read all text
full_text = ""
for page in doc:
    full_text += page.get_text()

# Optional: Check the raw extracted text
# print(full_text)

# Step 3: Remove newlines to prevent broken lines
cleaned_text = full_text.replace("\n", " ")

# Step 4: Split on numbers like "1. ", "2. ", ..., "40. "
raw_questions = re.split(r'\s?\d+\.\s+', cleaned_text)[1:]  # skip the first empty string

# Step 5: Trim and format
questions = [{"question": q.strip()} for q in raw_questions if q.strip()]

# Step 6: Save to JSON
with open("isaa_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"✅ Extracted {len(questions)} questions and saved to isaa_questions.json")
