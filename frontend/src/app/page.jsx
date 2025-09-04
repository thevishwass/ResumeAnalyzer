"use client";
import { useState } from "react";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import ResumeUpload from "@/components/ResumeUpload";
import Content from "@/components/Content";
import AnalysisResult from "@/components/AnalysisResult";

export default function Page() {
  const [resumeData, setResumeData] = useState(null);

  return (
    <>
      <Navbar />
      <main className="container">
        <ResumeUpload onResumeParsed={setResumeData} />
        
        {/* Only show AnalysisResult if we have resumeData */}
        {resumeData?.resume_text && (
  <AnalysisResult
    resumeText={resumeData.resume_text}
    jobDescription={resumeData.job_description || ""}
  />
)}

        {/* {resumeData?.resume_text && (
          <AnalysisResult
            resumeText={resumeData.resume_text}
            jobDescription={resumeData.job_description || ""}
          />
        )} */}

        <Content />
      </main>
      <Footer />
    </>
  );
}
