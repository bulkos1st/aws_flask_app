# Sample code by chatgpt
import json
import os
import requests

from flask import Flask
from flask import Flask, jsonify, render_template, render_template_string, url_for, redirect, flash, g
import boto3


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Flask AWS Deployment Demo!</h1>"

@app.route("/health")
def health_check():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
