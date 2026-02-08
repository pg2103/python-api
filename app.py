from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify({"message": "Hello from Azure App Service!"})

@app.get("/health")
def health():
    return jsonify({"status": "ok"})
