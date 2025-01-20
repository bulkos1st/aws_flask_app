# Sample code by chatgpt
import json
import os
import requests

from flask import Flask, jsonify, render_template, render_template_string, url_for, redirect, flash, g
import boto3


def get_instance_document():
    try:
        r = requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document")
        if r.status_code == 401:
            token=(
                requests.put(
                    "http://169.254.169.254/latest/api/token", 
                    headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'}, 
                    verify=False, timeout=1
                )
            ).text
            r = requests.get(
                "http://169.254.169.254/latest/dynamic/instance-identity/document",
                headers={'X-aws-ec2-metadata-token': token}, timeout=1
            )
        r.raise_for_status()
        return r.json()
    except:
        print(" * Instance metadata not available")
        return { "availabilityZone" : "us-fake-1a",  "instanceId" : "i-fakeabc" }



app = Flask(__name__)

doc = get_instance_document()
availablity_zone = doc["availabilityZone"]
instance_id = doc["instanceId"]


@app.before_request
def before_request():
    "Set up globals referenced in jinja templates"
    g.availablity_zone = availablity_zone
    g.instance_id = instance_id


@app.route("/")
def home():
    return "<h1>Welcome to the Flask AWS Deployment Demo!</h1>"

@app.route("/health")
def health_check():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
