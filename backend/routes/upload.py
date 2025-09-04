from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile
import os
import pdfplumber
import docx2txt

router = APIRouter()

def parse_resume(file_path: str):
    text = ""

    if file_path.endswith(".pdf"):
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            print(f"PDF parsing error: {e}")

    elif file_path.endswith(".docx"):
        try:
            text = docx2txt.process(file_path)
        except Exception as e:
            print(f"DOCX parsing error: {e}")

    text = text.strip()

    parsed = {
        "name": "Vishwas Singh",  # could enhance with regex/NLP later
        "skills": ["Python", "React", "Node.js"],  # could enhance
        "text_preview": text[:500],  # first 500 chars
        "full_text": text
    }

    return parsed

@router.post("/uploadResume/")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX allowed")

    # Save file temporarily
    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        parsed_data = parse_resume(tmp_path)
        return {"filename": file.filename, "parsed": parsed_data}
    finally:
        os.remove(tmp_path)
