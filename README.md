# Resume Analyzer

A smart tool that analyzes resumes against job descriptions, highlighting skill matches, missing skills, and overall suitability. This project helps job seekers optimize their resumes and tailor them for specific roles.

## ✨ Features

- Compare a resume with a job description automatically  
- Generate a suitability score based on skill matching  
- Highlight missing skills and improvement areas  
- Simple, interactive Next.js frontend  
- FastAPI-powered backend with Python NLP processing  

## 🛠️ Tech Stack

- **Frontend:** Next.js (React)  
- **Backend:** FastAPI (Python)  
- **Development:** VS Code  
- **NLP & Processing:** Regex, Python libraries  

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/thevishwass/ResumeAnalyzer.git
cd ResumeAnalyzer


cd backend
python -m venv venv
.\venv\Scripts\activate      # Windows
# source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000


cd frontend
npm install
npm run dev
