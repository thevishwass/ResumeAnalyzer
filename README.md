# 📄 Resume Analyzer

A smart tool that analyzes resumes against job descriptions, highlighting skill matches, missing skills, and overall suitability. It helps job seekers optimize their resumes and tailor them to specific roles by providing actionable insights using natural language processing.

---

## ✨ Features

- ✅ Compare resumes with job descriptions automatically  
- ✅ Generate a suitability score based on skill matching  
- ✅ Highlight missing skills and improvement areas  
- ✅ Interactive Next.js frontend with real-time feedback  
- ✅ FastAPI backend powered by Python and NLP tools  
- ✅ Easy to set up and run locally  

---

## 🛠 Tech Stack

- **Frontend:** Next.js (React)  
- **Backend:** FastAPI (Python)  
- **NLP:** Regex and Python libraries  
- **Development:** VS Code, Git, Python, Node.js  

---

## 🚀 Installation & Setup

### ✅ Prerequisites

Make sure you have installed:

- Python 3.8 or later  
- Node.js 14 or later  
- Git  
- VS Code (optional but recommended)

---

### 🔽 Clone the Repository

```bash
git clone https://github.com/thevishwass/ResumeAnalyzer.git
cd ResumeAnalyzer
cd backend

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate      # Windows
# source venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000

cd ../frontend

# Install dependencies
npm install

# Run the Next.js development server
npm run dev


ResumeAnalyzer/
├── backend/            # FastAPI server logic
├── frontend/           # Next.js frontend components
├── README.md           # Project documentation




📌 How to Use

Upload or paste your resume and job description in the frontend.

View the analysis results highlighting matched and missing skills.

Get suggestions to improve your resume for specific job roles.

Iterate and optimize your resume for better job applications.

🤝 Contributing

Contributions, issues, and feature requests are welcome!

Fork the project

Create a feature branch (git checkout -b feature-name)

Commit your changes (git commit -m "Add new feature")

Push to your branch (git push origin feature-name)

Open a pull request

📜 License

This project is open-source and available under the MIT License.

📬 Contact

Feel free to reach out via GitHub issues or pull requests for feedback, suggestions, or collaborations.
