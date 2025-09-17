from flask import Flask, jsonify, render_template_string
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    # Get environment information for Jenkins deployment
    environment = os.environ.get('ENVIRONMENT', 'development')
    build_number = os.environ.get('BUILD_NUMBER', 'unknown')
    jenkins_url = os.environ.get('JENKINS_URL', 'not-set')
    hostname = socket.gethostname()
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jenkins Flask App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .container {{
                margin-top: 50px;
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
                padding: 20px;
            }}
            .jenkins-info {{
                background-color: #d4edda;
                border: 1px solid #c3e6cb;
                border-radius: 5px;
                padding: 20px;
                margin: 20px 0;
            }}
            h1 {{
                color: #333;
                margin-bottom: 30px;
            }}
            p {{
                font-size: 18px;
                color: #555;
                margin: 10px 0;
            }}
            .info-item {{
                background-color: white;
                padding: 10px;
                margin: 10px 0;
                border-radius: 3px;
                border-left: 4px solid #007bff;
            }}
            .status-ok {{
                color: #155724;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Jenkins Deployed Flask App</h1>
            <p>This application was deployed using Jenkins CI/CD pipeline.</p>
            
            <div class="jenkins-info">
                <h3>Deployment Information</h3>
                <div class="info-item">
                    <strong>Environment:</strong> {environment}
                </div>
                <div class="info-item">
                    <strong>Build Number:</strong> {build_number}
                </div>
                <div class="info-item">
                    <strong>Hostname:</strong> {hostname}
                </div>
                <div class="info-item">
                    <strong>Jenkins URL:</strong> {jenkins_url}
                </div>
            </div>
            
            <p class="status-ok">✅ Application Status: Running</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route("/health")
def health():
    """Health check endpoint for Jenkins and monitoring"""
    return jsonify({
        "status": "OK",
        "environment": os.environ.get('ENVIRONMENT', 'development'),
        "build_number": os.environ.get('BUILD_NUMBER', 'unknown'),
        "hostname": socket.gethostname()
    })

@app.route("/jenkins-info")
def jenkins_info():
    """Endpoint to display Jenkins-specific information"""
    jenkins_data = {
        "build_number": os.environ.get('BUILD_NUMBER', 'unknown'),
        "build_id": os.environ.get('BUILD_ID', 'unknown'),
        "build_url": os.environ.get('BUILD_URL', 'unknown'),
        "job_name": os.environ.get('JOB_NAME', 'unknown'),
        "jenkins_url": os.environ.get('JENKINS_URL', 'unknown'),
        "workspace": os.environ.get('WORKSPACE', 'unknown'),
        "node_name": os.environ.get('NODE_NAME', 'unknown'),
        "environment": os.environ.get('ENVIRONMENT', 'development')
    }
    return jsonify(jenkins_data)

@app.route("/version")
def version():
    """Version endpoint for deployment tracking"""
    return jsonify({
        "version": "1.0.0",
        "build_number": os.environ.get('BUILD_NUMBER', 'unknown'),
        "deployed_at": os.environ.get('BUILD_TIMESTAMP', 'unknown')
    })

if __name__ == "__main__":
    # Get port from environment variable (useful for Jenkins deployments)
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
