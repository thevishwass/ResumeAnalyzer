# backend/routes/upload.py

from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile
import os
import pdfplumber
import docx2txt

from utils.masking import mask_emails, mask_phone_numbers

router = APIRouter()


def parse_resume(file_path: str) -> dict:
    """
    Extract text from PDF or DOCX and mask emails/phone numbers.
    """
    try:
        text = ""

        if file_path.lower().endswith(".pdf"):
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

        elif file_path.lower().endswith(".docx"):
            text = docx2txt.process(file_path)

        else:
            raise ValueError("Unsupported file type. Only PDF or DOCX allowed.")

        text = text.strip()

        # Mask sensitive information
        masked_text = mask_emails(text)
        masked_text = mask_phone_numbers(masked_text)

        return {"fullMaskedText": masked_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing resume: {e}")


@router.post("/uploadResume/")
async def upload_resume(file: UploadFile = File(...)):
    """
    Accepts a PDF or DOCX resume file, parses it, masks sensitive info,
    and returns the result.
    """
    if not file.filename.lower().endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files are allowed.")

    suffix = os.path.splitext(file.filename)[1]

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        parsed_data = parse_resume(tmp_path)
        return {"filename": file.filename, "parsed": parsed_data}

    finally:
        # Clean up temporary file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
