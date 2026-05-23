from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>GKE Frontend App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 100px;
            }}
            .card {{
                background: white;
                width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #4285F4;
            }}
            p {{
                font-size: 18px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Frontend App Running on GKE 🚀</h1>
            <p><b>Hostname:</b> {socket.gethostname()}</p>
            <p><b>Environment:</b> {os.getenv("ENV", "dev")}</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)