# symbols_api_server.py

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='public')
CORS(app, origins=["https://algomin-ui-production.up.railway.app"])

@app.route("/symbols.json")
def get_symbols():
    try:
        return send_from_directory(app.static_folder, "symbols.json")
    except FileNotFoundError:
        return jsonify({"error": "symbols.json not found"}), 404

@app.route("/")
def root():
    return {"status": "ok", "message": "Symbol fetcher is live"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
