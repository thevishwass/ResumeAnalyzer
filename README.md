# 📄 Resume Analyzer

A smart tool that analyzes resumes against job descriptions, highlighting skill matches, missing skills, and overall suitability. It helps job seekers optimize their resumes and tailor them to specific roles by providing actionable insights using natural language processing.

---

## ✨ Features

- ✅ Automatically compare resumes with job descriptions  
- ✅ Generate a suitability score based on skill matching  
- ✅ Highlight missing skills and areas for improvement  
- ✅ Interactive Next.js frontend with real-time feedback  
- ✅ FastAPI backend powered by Python and NLP tools  
- ✅ Easy to set up and run locally  



## 🛠 Tech Stack

- **Frontend:** Next.js (React)  
- **Backend:** FastAPI (Python)  
- **NLP:** Regex and Python libraries  
- **Development Tools:** VS Code, Git, Python, Node.js  


## 🚀 Installation & Setup

### ✅ Prerequisites

Make sure you have the following installed:

- Python 3.8 or later  
- Node.js 14 or later  
- Git  
- VS Code (optional but recommended)

---

### 🟠🟢 Setup Backend & Frontend

```bash
# Clone the repository
git clone https://github.com/thevishwass/ResumeAnalyzer.git
cd ResumeAnalyzer

# ----------------------------
# Setup Backend
# ----------------------------
cd backend

# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate      # Windows
# source venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# The backend server will be available at http://localhost:8000

# ----------------------------
# Setup Frontend
# ----------------------------
# Open a new terminal and run:

cd ../frontend

# Install dependencies
npm install

# Run the Next.js development server
npm run dev

# The frontend will be available at http://localhost:3000
