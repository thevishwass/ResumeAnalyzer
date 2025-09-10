import re
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI  # OpenRouter-compatible OpenAI SDK

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OpenRouter API Key is not set. Check your .env file.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

router = APIRouter(prefix="/gpt", tags=["GPT LLM"])

class LLMRequest(BaseModel):
    resume_text: str
    job_description: str

@router.post("/analyze_llm")
async def analyze_llm(req: LLMRequest):
    prompt = f"""
Extract all skills from the resume and job description, normalizing variations 
(e.g., ReactJS, React.js → React).

Resume:
{req.resume_text}

Job Description:
{req.job_description}

Compare skills from the resume against the job description and calculate a match score:
- score = (number of matching skills / total skills required in job description) * 100
- Round score to nearest integer

Return JSON like this:
{{
    "score": int,  # percentage of job-required skills present in resume
    "missing_skills": [list of skills present in job description but missing in resume],
    "suggestions": [short actionable points to improve resume]
}}
"""

    try:
        # Call OpenRouter API using OpenAI SDK
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",  # or your desired model
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",  # optional
                "X-Title": "<YOUR_SITE_NAME>"      # optional
            },
            extra_body={}
        )

        raw_text = completion.choices[0].message.content

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
            else:
                raise ValueError("Could not parse JSON from response.")

        # Ensure keys exist
        result.setdefault("score", 0)
        result.setdefault("missing_skills", [])
        result.setdefault("suggestions", [])

        return {"result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM analysis failed: {str(e)}")
