import os
from google import genai

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GEMINIAPIKEY")
client = genai.Client(api_key=API_KEY)

def analyze_with_gemini(resume_text: str, job_description: str) -> dict:
    prompt = f"""
    Analyze the following resume and job description.
    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Output a JSON with:
    - score (0-100)
    - missing_skills (list)
    - suggestions (list of recommendations)
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    # Convert string response to JSON
    import json
    try:
        return json.loads(response.text)
    except:
        return {"error": "Failed to parse LLM response", "raw": response.text}
