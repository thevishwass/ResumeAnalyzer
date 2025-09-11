# 📄 Resume Analyzer

A smart tool that analyzes resumes against job descriptions, highlighting skill matches, missing skills, and overall suitability. It helps job seekers optimize their resumes and tailor them to specific roles by providing actionable insights using natural language processing.


## ✨ Features

- ✅ Automatically compare resumes with job descriptions  
- ✅ MASKED private information such as phone numbers and email addresses
- ✅ Generates an ATS score based on skill matching
- ✅ Highlight missing skills and areas for improvement  
- ✅ Interactive Next.js frontend with real-time feedback  
- ✅ FastAPI backend that securely sends data to the ChatGPT API for processing  
- ✅ Easy to set up and run



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



### 🟠 Setup Backend

``` python
# Clone the repository
git clone https://github.com/thevishwass/ResumeAnalyzer.git
cd ResumeAnalyzer


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
```



- Don't forget to make .env file, without this it wont work
- Set .env like this only: (EXAMPLE) --> OPENROUTER_API_KEY = Abcdefghijkl1234567890_
- Users email address and phone number in resume are never sent outside; they are securely masked before processing.

- For API Key, go to https://openrouter.ai/



### 🟢 Setup Frontend

``` javascript

cd ../frontend

# Install dependencies
npm install

# Run the Next.js development server
npm run dev

# The frontend will be available at http://localhost:3000

```




### 📂 Folder Structure
```bash
ResumeAnalyzer/
├── backend/            # FastAPI server logic
├── frontend/           # Next.js frontend components
├── README.md           # Project documentation
```

### 📌 How It Works

- Users upload or paste their resume and job description in the frontend.
- The backend masks sensitive information like phone numbers and email addresses.
- The sanitized data is securely sent to the ChatGPT API for analysis.
- ChatGPT API returns a suitability score, matched skills, missing skills, and suggestions.
- The frontend displays the results in real time for users to improve their resume.

### 📬 Contact

Feel free to open an issue or submit a pull request for feedback, suggestions, or collaborations.
