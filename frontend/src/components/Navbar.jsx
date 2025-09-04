// src/components/Navbar.jsx
"use client"
export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <h1 className="navbar-brand">Resume Analyzer</h1>
        <div className="navbar-links">
          <a href="#">Home</a>
          <a href="#contact01">Contact Us</a>
        </div>
      </div>
    </nav>
  );
}
