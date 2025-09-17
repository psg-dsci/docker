from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Shoolini University - DevOps Project</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                color: white;
                min-height: 100vh;
            }
            .header {
                background-color: rgba(255, 255, 255, 0.1);
                padding: 30px;
                text-align: center;
                border-bottom: 3px solid #ffd700;
            }
            .university-logo {
                font-size: 36px;
                font-weight: bold;
                color: #ffd700;
                margin-bottom: 10px;
            }
            .tagline {
                font-size: 18px;
                color: #e0e0e0;
                font-style: italic;
                margin-bottom: 10px;
            }
            .location {
                font-size: 16px;
                color: #b0b0b0;
            }
            .container {
                max-width: 1000px;
                margin: 40px auto;
                padding: 20px;
            }
            .welcome-section {
                text-align: center;
                margin-bottom: 50px;
            }
            .welcome-section h1 {
                font-size: 42px;
                margin-bottom: 20px;
                color: #ffd700;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            .welcome-section p {
                font-size: 20px;
                color: #e0e0e0;
                line-height: 1.6;
                max-width: 800px;
                margin: 0 auto;
            }
            .info-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 25px;
                margin: 40px 0;
            }
            .info-card {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 30px;
                border: 2px solid rgba(255, 215, 0, 0.3);
                backdrop-filter: blur(15px);
                transition: transform 0.3s ease;
            }
            .info-card:hover {
                transform: translateY(-5px);
                border-color: #ffd700;
            }
            .info-card h3 {
                color: #ffd700;
                margin-bottom: 20px;
                font-size: 22px;
                text-align: center;
            }
            .info-item {
                background: rgba(255, 255, 255, 0.08);
                padding: 15px 20px;
                margin: 12px 0;
                border-radius: 8px;
                border-left: 4px solid #ffd700;
                font-size: 16px;
            }
            .status-indicator {
                text-align: center;
                margin: 40px 0;
                padding: 30px;
                background: rgba(40, 167, 69, 0.2);
                border-radius: 15px;
                border: 2px solid #28a745;
            }
            .status-indicator .status-icon {
                font-size: 64px;
                margin-bottom: 15px;
            }
            .status-indicator h3 {
                color: #28a745;
                font-size: 24px;
                margin-bottom: 10px;
            }
            .achievements {
                background: rgba(255, 215, 0, 0.1);
                border: 2px solid #ffd700;
                border-radius: 15px;
                padding: 30px;
                margin: 30px 0;
            }
            .achievements h3 {
                color: #ffd700;
                text-align: center;
                font-size: 24px;
                margin-bottom: 20px;
            }
            .achievements ul {
                list-style: none;
                padding: 0;
            }
            .achievements li {
                padding: 10px 0;
                font-size: 16px;
                border-bottom: 1px solid rgba(255, 215, 0, 0.2);
            }
            .achievements li:last-child {
                border-bottom: none;
            }
            .footer {
                text-align: center;
                padding: 40px;
                background: rgba(0, 0, 0, 0.3);
                margin-top: 60px;
                border-top: 2px solid #ffd700;
            }
            .footer p {
                color: #b0b0b0;
                font-size: 14px;
                margin: 5px 0;
            }
            .footer .copyright {
                color: #ffd700;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <div class="university-logo">🎓 SHOOLINI UNIVERSITY</div>
            <div class="tagline">"Learning for Life"</div>
            <div class="location">📍 Solan, Himachal Pradesh, India</div>
        </div>
        
        <div class="container">
            <div class="welcome-section">
                <h1>🚀 DevOps & Cloud Computing Project</h1>
                <p>
                    This Flask application demonstrates modern CI/CD practices and containerization technologies 
                    developed by students of the Computer Science & Engineering Department at Shoolini University.
                </p>
            </div>
            
            <div class="info-grid">
                <div class="info-card">
                    <h3>🏛️ University Information</h3>
                    <div class="info-item">
                        <strong>Institution:</strong> Shoolini University
                    </div>
                    <div class="info-item">
                        <strong>Established:</strong> 2009
                    </div>
                    <div class="info-item">
                        <strong>Location:</strong> Solan, Himachal Pradesh
                    </div>
                    <div class="info-item">
                        <strong>Type:</strong> Private Research University
                    </div>
                    <div class="info-item">
                        <strong>Recognition:</strong> UGC Approved
                    </div>
                </div>
                
                <div class="info-card">
                    <h3>💻 Department Details</h3>
                    <div class="info-item">
                        <strong>Department:</strong> Computer Science & Engineering
                    </div>
                    <div class="info-item">
                        <strong>Course:</strong> DevOps & Cloud Computing
                    </div>
                    <div class="info-item">
                        <strong>Technology Stack:</strong> Flask, Docker, Jenkins
                    </div>
                    <div class="info-item">
                        <strong>Focus:</strong> Modern Software Development
                    </div>
                    <div class="info-item">
                        <strong>Methodology:</strong> Agile & DevOps
                    </div>
                </div>
                
                <div class="info-card">
                    <h3>🌟 University Specializations</h3>
                    <div class="info-item">
                        <strong>Biotechnology:</strong> Leading Research
                    </div>
                    <div class="info-item">
                        <strong>Engineering:</strong> Innovation Hub
                    </div>
                    <div class="info-item">
                        <strong>Management:</strong> Industry Connect
                    </div>
                    <div class="info-item">
                        <strong>Pharmaceutical:</strong> World-class Labs
                    </div>
                    <div class="info-item">
                        <strong>Applied Sciences:</strong> Research Excellence
                    </div>
                </div>
                
                <div class="info-card">
                    <h3>🏆 Rankings & Recognition</h3>
                    <div class="info-item">
                        <strong>Research:</strong> Top Private University in HP
                    </div>
                    <div class="info-item">
                        <strong>Innovation:</strong> ARIIA Ranked
                    </div>
                    <div class="info-item">
                        <strong>Placement:</strong> 100% Placement Record
                    </div>
                    <div class="info-item">
                        <strong>Industry:</strong> Strong Corporate Ties
                    </div>
                    <div class="info-item">
                        <strong>Global:</strong> International Collaborations
                    </div>
                </div>
            </div>
            
            <div class="status-indicator">
                <div class="status-icon">✅</div>
                <h3>Application Status: Successfully Deployed!</h3>
                <p style="font-size: 18px;">Jenkins CI/CD Pipeline Implementation Complete</p>
            </div>
            
            <div class="achievements">
                <h3>🎯 DevOps Learning Objectives Achieved</h3>
                <ul>
                    <li>✅ <strong>Flask Web Framework:</strong> Created responsive web application with modern UI</li>
                    <li>✅ <strong>Jenkins Integration:</strong> Implemented automated CI/CD pipeline</li>
                    <li>✅ <strong>Docker Containerization:</strong> Packaged application for consistent deployment</li>
                    <li>✅ <strong>Environment Management:</strong> Configured development and production environments</li>
                    <li>✅ <strong>Health Monitoring:</strong> Implemented application health checks and status endpoints</li>
                    <li>✅ <strong>Version Control:</strong> Git-based source code management</li>
                    <li>✅ <strong>Automated Testing:</strong> Continuous integration testing pipeline</li>
                    <li>✅ <strong>Infrastructure as Code:</strong> Automated deployment and scaling</li>
                </ul>
            </div>
        </div>
        
        <div class="footer">
            <p class="copyright">© 2024 Shoolini University</p>
            <p>Department of Computer Science and Engineering</p>
            <p>Empowering Innovation Through Technology Excellence</p>
            <p>🌐 www.shooliniuniversity.com | 📧 info@shooliniuniversity.com</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route("/health")
def health():
    """Health check endpoint with Shoolini University information"""
    return jsonify({
        "status": "OK",
        "university": "Shoolini University",
        "location": "Solan, Himachal Pradesh, India",
        "department": "Computer Science & Engineering",
        "course": "DevOps & Cloud Computing",
        "established": "2009",
        "motto": "Learning for Life",
        "application": "Flask DevOps Demo",
        "version": "2.0.0"
    })

@app.route("/university")
def university_info():
    """Complete Shoolini University information endpoint"""
    return jsonify({
        "university_details": {
            "name": "Shoolini University",
            "established": "2009",
            "location": "Solan, Himachal Pradesh, India",
            "type": "Private Research University",
            "motto": "Learning for Life",
            "recognition": "UGC Approved",
            "website": "www.shooliniuniversity.com"
        },
        "specializations": [
            "Biotechnology & Life Sciences",
            "Computer Science & Engineering", 
            "Management & Business Administration",
            "Pharmaceutical Sciences",
            "Applied Sciences & Humanities",
            "Engineering & Technology"
        ],
        "achievements": {
            "research_ranking": "Top Private University in Himachal Pradesh",
            "innovation_ranking": "ARIIA Ranked University",
            "placement_record": "100% Placement in Top Companies",
            "industry_connect": "Strong Corporate Partnerships",
            "global_presence": "International Collaborations"
        },
        "cse_department": {
            "focus_areas": [
                "Artificial Intelligence & Machine Learning",
                "Data Science & Analytics", 
                "DevOps & Cloud Computing",
                "Cybersecurity",
                "Software Engineering",
                "Web & Mobile Development"
            ],
            "current_project": "DevOps Pipeline Implementation",
            "technologies": ["Flask", "Docker", "Jenkins", "Python", "Git"]
        }
    })

@app.route("/student-portal")
def student_portal():
    """Student information and project portal"""
    return jsonify({
        "portal_name": "Shoolini University - CSE DevOps Portal",
        "department": "Computer Science & Engineering",
        "current_project": {
            "title": "CI/CD Pipeline Implementation",
            "description": "Flask application with Jenkins automation",
            "technologies": ["Python", "Flask", "Docker", "Jenkins", "Git"],
            "learning_outcomes": [
                "Web Application Development",
                "Containerization Technologies", 
                "Continuous Integration/Deployment",
                "Infrastructure Automation",
                "Version Control Systems"
            ]
        },
        "student_resources": {
            "lab_facilities": "Modern Computing Labs with Cloud Access",
            "software_tools": "Industry-standard DevOps Tools",
            "mentorship": "Expert Faculty & Industry Professionals",
            "placement_support": "100% Placement Assistance"
        },
        "contact_info": {
            "department": "Computer Science & Engineering",
            "university": "Shoolini University",
            "address": "Solan, Himachal Pradesh - 173229, India",
            "website": "www.shooliniuniversity.com"
        }
    })

if __name__ == "__main__":
    print("🎓 Starting Shoolini University Flask Application...")
    print("🏛️ Department: Computer Science & Engineering")
    print("📍 Location: Solan, Himachal Pradesh")
    print("🚀 DevOps Project: CI/CD Pipeline Implementation")
    print("=" * 60)
    
    app.run(host="0.0.0.0", port=5000, debug=True)
