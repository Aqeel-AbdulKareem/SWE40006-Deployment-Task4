from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "Development")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SWE40006 Deployment Task 4</title>
        <style>
            body {{
                background-color: #111827;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}

            .container {{
                background-color: #1f2937;
                padding: 40px;
                border-radius: 15px;
                width: 600px;
            }}

            h1 {{
                color: #60a5fa;
            }}

            .success {{
                color: #4ade80;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>SWE40006 Deployment Task 4</h1>

            <h2>Docker Web Application</h2>

            <p class="success">
                Container Application Running Successfully
            </p>

            <p><strong>Environment:</strong> {environment}</p>

            <p>
                This Python Flask application is running
                inside a Docker container.
            </p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "deployment-task4"
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)