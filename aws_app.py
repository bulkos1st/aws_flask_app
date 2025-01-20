# Sample code by chatgpt
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Flask AWS Deployment Demo!</h1>"

@app.route("/health")
def health_check():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
