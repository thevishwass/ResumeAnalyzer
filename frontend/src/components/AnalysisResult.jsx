"use client";
import { useEffect, useState } from "react";

export default function AnalysisResult({ resumeText, jobDescription }) {
  const [loading, setLoading] = useState(false);
  const [llmData, setLlmData] = useState(null);
  const [showCard, setShowCard] = useState(false);

  useEffect(() => {
    if (!resumeText || !jobDescription) return;

    const fetchLLMResult = async () => {
      setLoading(true);
      setShowCard(true);
      setLlmData(null);

      try {
        const res = await fetch("http://localhost:8000/gpt/analyze_llm", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ resume_text: resumeText, job_description: jobDescription }),
        });

        const data = await res.json();
        setLlmData(data.result ?? {});
      } catch (err) {
        alert(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchLLMResult();
  }, [resumeText, jobDescription]);

  if (!showCard) return null;

  return (
    <div className="analysis-card">
      <h2 className="analysis-title">LLM Analysis Result</h2>

      {loading && <p className="loading-text">Analyzing resume...</p>}

      {!loading && llmData && (
        <div className="analysis-content">
          <p><strong>Score:</strong> <span className="score">{llmData.score ?? "N/A"}</span></p>

          {/* <p><strong>Skills:</strong></p>
          {llmData.skills?.length ? (
            <ul className="skills-list">
              {llmData.skills.map((s, i) => <li key={i}>{s}</li>)}
            </ul>
          ) : <p className="none-text">None</p>} */}
          
          <p><strong>Missing Skills:</strong></p>
          {llmData.missing_skills?.length ? (
            <ul className="skills-list">
              {llmData.missing_skills.map((s, i) => <li key={i}>{s}</li>)}
            </ul>
          ) : <p className="none-text">None</p>}

          <p><strong>Suggestions:</strong></p>
          {llmData.suggestions?.length ? (
            <ul className="suggestions-list">
              {llmData.suggestions.map((s, i) => <li key={i}>{s}</li>)}
            </ul>
          ) : <p className="none-text">None</p>}
        </div>
      )}
    </div>
  );
}
