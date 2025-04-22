from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ RNAI-NEOX Backend está vivo."

@app.route('/run-seed')
def run_seed():
    try:
        result = subprocess.run(["python", "seed_rnai.py"], capture_output=True, text=True)
        return jsonify({"output": result.stdout})
    except Exception as e:
        return jsonify({"error": str(e)})
