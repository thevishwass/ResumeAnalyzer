import os
import pdfplumber
import docx2txt
from PIL import Image


def parse_resume(file_path: str):
    text = ""

    if file_path.endswith(".pdf"):
        try:
            # Try normal extraction first
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

            # If text is empty, fallback to OCR
            

        except Exception as e:
            print(f"PDF parsing error: {e}")

    elif file_path.endswith(".docx"):
        try:
            text = docx2txt.process(file_path)
        except Exception as e:
            print(f"DOCX parsing error: {e}")

    text = text.strip()

    parsed = {
        "name": "Vishwas Singh",
        "skills": ["Python", "React", "Node.js"],
        "text_preview": text[:500],
        "full_text": text
    }

    return parsed
