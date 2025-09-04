"use client"
export default function ContentPage() {
  return (
    <div className="content-page">

      {/* Hero Section */}
      <header className="hero-section" style={{ display: "flex", alignItems: "center", gap: "3rem", padding: "4rem 2rem" }}>
        <div className="hero-text" style={{ flex: 1 }}>
          <h1 style={{ fontSize: "2.5rem", marginBottom: "1rem" }}>Boost Your Career with Resume Analyzer</h1>
          <p style={{ fontSize: "1.2rem", lineHeight: "1.6" }}>
            AI-powered insights to optimize your resume and land your dream job faster.
          </p>
        </div>
        <div className="hero-image" style={{ flex: 1 }}>
  <img 
    src="/images/hero-placeholder.png" 
    alt="Resume Analysis" 
    style={{ width: "100%", borderRadius: "1rem", objectFit: "cover" }} 
  />
</div>

      </header>

      <main className="main-content" >

        {/* About Section */}
        <section className="about-section" style={{ display: "flex", gap: "3rem", marginBottom: "4rem", alignItems: "center" }}>
          <div className="about-image" style={{ flex: 1 }}>
            <img src="/images/about-placeholder.png" alt="About us" style={{ width: "100%", borderRadius: "1rem" }} />
          </div>
          <div className="about-text" style={{ flex: 1 }}>
            <h2 style={{ fontSize: "2rem", marginBottom: "1rem" }}>About Us</h2>
            <p style={{ fontSize: "1.1rem", lineHeight: "1.6" }}>
              Resume Analyzer helps job seekers understand and optimize their resumes instantly.
              Our AI engine scans your resume for skills, experience, and keywords to provide actionable insights.
            </p>
          </div>
        </section>

        {/* How It Works */}
        <section className="how-it-works" style={{ marginBottom: "4rem" }}>
          <h2 style={{ fontSize: "2rem", marginBottom: "2rem" }}>How It Works</h2>
          <div className="steps" style={{ display: "flex", gap: "2rem", flexWrap: "wrap" }}>
            {[
              { img: "/images/step1.png", title: "Upload Resume", desc: "Upload your resume in PDF, DOC, or DOCX format." },
              { img: "/images/step2.png", title: "AI Analysis", desc: "Our AI scans and extracts key information like skills, experience, and keywords." },
              { img: "/images/step3.png", title: "Get Insights", desc: "Receive a detailed report highlighting strengths and areas of improvement." },
            ].map((step, i) => (
              <div key={i} className="step" style={{ flex: "1 1 250px", background: "#f9f9f9", padding: "2rem", borderRadius: "1rem", textAlign: "center" }}>
                <img src={step.img} alt={step.title} style={{ width: "80px", marginBottom: "1rem" }} />
                <h3 style={{ fontSize: "1.3rem", marginBottom: "0.5rem" }}>{step.title}</h3>
                <p style={{ fontSize: "1rem", lineHeight: "1.5" }}>{step.desc}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Benefits Section */}
        <section className="benefits-section" style={{ marginBottom: "4rem" }}>
          <h2 style={{ fontSize: "2rem", marginBottom: "2rem" }}>Why Use Resume Analyzer?</h2>
          <div className="benefits-cards" style={{ display: "flex", gap: "2rem", flexWrap: "wrap" }}>
            {[
              { img: "/images/benefit1.png", title: "Save Time", desc: "Instant analysis in seconds, no manual checking needed." },
              { img: "/images/benefit2.png", title: "Accurate Insights", desc: "AI identifies missing skills and keywords for your industry." },
              { img: "/images/benefit3.png", title: "Privacy First", desc: "Your resume is never stored or shared with third parties." },
            ].map((benefit, i) => (
              <div key={i} className="benefit-card" style={{ flex: "1 1 250px", background: "#f1f5f9", padding: "2rem", borderRadius: "1rem", textAlign: "center" }}>
                <img src={benefit.img} alt={benefit.title} style={{ width: "80px", marginBottom: "1rem" }} />
                <h3 style={{ fontSize: "1.3rem", marginBottom: "0.5rem" }}>{benefit.title}</h3>
                <p style={{ fontSize: "1rem", lineHeight: "1.5" }}>{benefit.desc}</p>
              </div>
            ))}
          </div>
        </section>

        {/* FAQ Section */}
        <section className="faq-section" style={{ marginBottom: "4rem" }}>
          <h2 style={{ fontSize: "2rem", marginBottom: "1.5rem" }}>Frequently Asked Questions</h2>
          <ul style={{ fontSize: "1.05rem", lineHeight: "1.8", listStyle: "disc", paddingLeft: "1.5rem" }}>
            <li><strong>Do you store my resume?</strong> No, all files are processed temporarily and deleted immediately after analysis.</li>
            <li><strong>Which file formats are supported?</strong> PDF, DOC, and DOCX.</li>
            <li><strong>Is it free?</strong> Yes, basic resume analysis is completely free.</li>
          </ul>
        </section>

        {/* Contact Section */}
        <section id="contact01" className="contact-section" style={{ display: "flex", gap: "3rem", alignItems: "center", marginBottom: "4rem" }}>
          <div className="contact-text" style={{ flex: 1 }}>
            <h2 style={{ fontSize: "2rem", marginBottom: "1rem" }}>Contact Us</h2>
            <p style={{ fontSize: "1.1rem" }}>
              If you have any questions or suggestions, reach out at <a href="mailto:thevishwass@gmail.com" style={{ color: "#0070f3" }}>thevishwass@gmail.com</a> OR <a href="mailto:sahanikamal345@gmail.com" style={{ color: "#0070f3" }}>sahanikamal345@gmail.com</a>
            </p>
          </div>
          
        </section>

      </main>
    </div>
  );
}
