import openai
from docx import Document
import pdfplumber
apikey='AIzaSyByBDsl8gqHfwnzNXWYtkOzjCob3KROV3I'
# ---------------------------
# 1. Load notes (from text, PDF, or Word)
# ---------------------------
def load_notes_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Example: load notes from PDF
# notes = load_notes_from_pdf("logic_notes.pdf")

# Or: paste notes manually (if no PDF available)
notes = """
Propositional logic deals with propositions that are either true or false.
Predicate logic extends propositional logic by adding quantifiers and predicates.
A tautology is always true regardless of truth values.
A contradiction is always false regardless of truth values.
"""

# ---------------------------
# 2. Define exam structure
# ---------------------------
exam_structure = """
Set an exam with the following structure:
- 3 multiple choice questions (1 mark each)
- 2 short answer questions (5 marks each)
- 1 essay question (10 marks)
Provide a marking guide with expected answers and marks allocation.
"""

# ---------------------------
# 3. Call AI model
# ---------------------------



import os
from openai import OpenAI




from openai import OpenAI

client = OpenAI(
    api_key=apikey,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    reasoning_effort="low",
    messages=[
        {"role": "system", "content": "You are an experienced lecturer who generates exam papers and detailed marking guides."},
        {
            "role": "user",
            "content": f"Lecture Notes:\n{notes}\n\n{exam_structure}"
        }
    ]
)

print(response.choices[0].message)
exam_text=response.choices[0].message.content



# ---------------------------
# 4. Save to Word
# ---------------------------
#print(exam_text)
doc = Document()
doc.add_heading("Exam Paper", level=1)
for line in exam_text.split('\n'):
    doc.add_paragraph(line)



doc.save("exam_and_marking_guide_version2.docx")

print("✅ Exam and marking guide saved to exam_and_marking_guide.docx")
