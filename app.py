from __future__ import annotations

import os
from pathlib import Path
import sys

import joblib
import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from feature_extractor import FEATURE_NAMES, extract_features
from train_model import MODEL_PATH, train_and_save_model


app = Flask(__name__)
CORS(app)


def load_model():
    path = Path(MODEL_PATH)
    if not path.exists():
        train_and_save_model()
    return joblib.load(path)


MODEL = load_model()


@app.get("/health")
def health():
    return jsonify({"status": "UP"})


@app.post("/predict")
def predict():
    payload = request.get_json(silent=True) or {}
    url = (payload.get("url") or "").strip()

    if not url:
        return jsonify({"error": "URL is required"}), 400

    features = extract_features(url)
    probabilities = MODEL.predict_proba([features])[0]
    phishing_probability = float(probabilities[1])
    label = int(np.argmax(probabilities))

    return jsonify(
        {
            "url": url,
            "prediction": "Phishing" if label == 1 else "Legitimate",
            "risk_score": round(phishing_probability, 4),
            "features": dict(zip(FEATURE_NAMES, features)),
        }
    )


if __name__ == "__main__":
    debug_enabled = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    app.run(host="0.0.0.0", port=5000, debug=debug_enabled)
