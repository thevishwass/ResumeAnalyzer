import pdfkit
import os
import tempfile

def generate_pdf_report(data: dict) -> str:
    """Generate PDF report from analysis data"""
    html_content = f"""
    <h1>Resume Analysis Report</h1>
    <p><b>Skills Found:</b> {", ".join(data.get("skills", []))}</p>
    <p><b>Score:</b> {data.get("score", 0)} / 100</p>
    <p><b>Preview:</b> {data.get("raw_text", "")}</p>
    """

    tmp_report = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdfkit.from_string(html_content, tmp_report.name)

    return tmp_report.name
