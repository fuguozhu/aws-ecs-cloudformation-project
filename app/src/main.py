
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from AWS ECS Fargate!",
        "application": "AWS Containerized Web Application",
        "version": "1.0.0",
        "hostname": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/info")
def info():
    return jsonify({
        "environment": os.getenv("APP_ENV", "development"),
        "hostname": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
