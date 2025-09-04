from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from google import genai
from dotenv import load_dotenv
from utils.llm_client import analyze_with_gemini

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GEMINIAPIKEY")
if not api_key:
    raise ValueError("❌ GEMINIAPIKEY environment variable is not set")

client = genai.Client(api_key=api_key)

router = APIRouter(prefix="/analyze", tags=["Analyze"])

# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel

router = APIRouter(prefix="/analyze", tags=["Analyze"])

class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str

@router.post("/ats_score")
def ats_score(req: AnalyzeRequest):
    try:
        result = analyze_with_gemini(req.resume_text, req.job_description)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Request schema
class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str

# Existing improve_resume endpoint (kept static)
class ImproveRequest(BaseModel):
    bullets: list[str]

@router.post("/ats_score")
def ats_score(req: AnalyzeRequest):
    """
    Use Gemini LLM to analyze resume vs job description.
    Returns JSON: {score, missing_skills, suggestions}
    """
    prompt = f"""
    Resume Text:
    {req.resume_text}

    Job Description:
    {req.job_description}

    Analyze the resume for this job and return JSON only in this format:
    {{
      "score": int,
      "missing_skills": [list of skills],
      "suggestions": [list of suggestions]
    }}
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        # The response.text should already be JSON
        import json
        result_json = json.loads(response.text)  # parse Gemini output
        return result_json
    except json.JSONDecodeError:
        # In case Gemini returns text not parseable as JSON
        raise HTTPException(status_code=500, detail=f"Invalid JSON from LLM: {response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/improve_resume")
def improve_resume(req: ImproveRequest):
    # static logic
    improved = [f"Developed: {b}" for b in req.bullets]
    return {"improved_bullets": improved}
