@'
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "project": "Water Potability Prediction"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
'@ | Set-Content app\app.py
