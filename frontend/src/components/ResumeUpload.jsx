// "use client";
"use client"; // must be first line

import { useState, useRef } from "react";

export default function ResumeUpload({ onResumeParsed }) {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState(""); // <-- add this
  const [loading, setLoading] = useState(false);
  const fileInputRef = useRef();

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const removeFile = () => {
    setFile(null);
    fileInputRef.current.value = null;
  };

  const handleAnalyze = async () => {
    if (!file) return alert("Please choose a file first");
    if (!jobDescription.trim()) return alert("Please enter a job description");

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://localhost:8000/uploadResume/", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("Upload failed");

      const data = await res.json();
      onResumeParsed({
        resume_text: data.parsed.full_text,
        job_description: jobDescription, // pass the job description too
      });
    } catch (err) {
      alert(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-card">
      <h2 className="upload-title">Upload Your Resume</h2>

      <input
        type="text"
        placeholder="Job Description"
        value={jobDescription}           // <-- use state variable
        onChange={(e) => setJobDescription(e.target.value)}
        className="job-desc-input"
      />

      <input
        type="file"
        ref={fileInputRef}
        onChange={handleFileChange}
        style={{ display: "none" }}
        accept=".pdf,.docx"
      />

      <button
        type="button"
        className="upload-btn"
        onClick={() => fileInputRef.current.click()}
      >
        Choose File
      </button>

      {file && (
        <div className="selected-file">
          <span className="file-name">{file.name}</span>
          <button className="remove-file" onClick={removeFile}>
            &times;
          </button>
        </div>
      )}

      <button
        className="analyze-btn"
        onClick={handleAnalyze}
        disabled={loading}
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>
    </div>
  );
}
