import re
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINIAPIKEY")
client = genai.Client(api_key=api_key)

router = APIRouter(prefix="/gemini", tags=["Gemini LLM"])

class LLMRequest(BaseModel):
    resume_text: str
    job_description: str

@router.post("/analyze_llm")
async def analyze_llm(req: LLMRequest):
    prompt = f"""
    Resume Text:
    {req.resume_text}

    Job Description:
    {req.job_description}

    Analyze the resume for this job and provide a JSON response like this:
    {{
      "score": 0,
      "missing_skills": [],
      "suggestions": []
    }}
    """

    try:
        # Call the LLM
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        raw_text = response.text

        # Remove ```json fences if present
        cleaned_text = re.sub(r"^```json\s*|```$", "", raw_text, flags=re.MULTILINE).strip()

        # Attempt to parse JSON
        result = {}
        try:
            result = json.loads(cleaned_text)
        except json.JSONDecodeError:
            # Fallback: extract JSON substring
            json_match = re.search(r"\{.*\}", cleaned_text, flags=re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())

        # Ensure keys exist and have correct types
        result.setdefault("score", 0)
        result.setdefault("missing_skills", [])
        result.setdefault("suggestions", [])

        # Always return plain JSON (not wrapped in {"result": ...})
        # return result
        return {"result": result}  # <- important


    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM analysis failed: {str(e)}")
