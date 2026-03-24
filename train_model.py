from __future__ import annotations

from pathlib import Path
import sys

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from feature_extractor import FEATURE_NAMES


MODEL_DIR = CURRENT_DIR / "models"
MODEL_PATH = MODEL_DIR / "phishing_rf_model.joblib"


def build_training_data() -> pd.DataFrame:
    records = [
        [18, 1, 1, 1, 0, 0, 0],
        [24, 2, 1, 2, 0, 0, 0],
        [30, 2, 1, 3, 1, 0, 0],
        [42, 3, 0, 8, 2, 2, 1],
        [55, 4, 0, 11, 3, 3, 1],
        [67, 5, 0, 14, 4, 4, 1],
        [36, 3, 1, 5, 1, 1, 0],
        [73, 6, 0, 16, 5, 5, 1],
        [28, 2, 1, 2, 0, 0, 0],
        [60, 5, 0, 12, 3, 2, 1],
        [19, 1, 1, 0, 0, 0, 0],
        [44, 3, 0, 9, 2, 2, 1],
        [33, 2, 1, 3, 1, 1, 0],
        [71, 5, 0, 15, 4, 4, 1],
        [27, 2, 1, 1, 0, 0, 0],
        [63, 4, 0, 13, 3, 3, 1],
        [39, 3, 1, 4, 1, 1, 0],
        [78, 6, 0, 18, 5, 4, 1],
        [22, 1, 1, 0, 0, 0, 0],
        [52, 4, 0, 10, 2, 3, 1],
    ]
    columns = FEATURE_NAMES + ["label"]
    return pd.DataFrame(records, columns=columns)


def train_and_save_model() -> Path:
    df = build_training_data()
    X = df[FEATURE_NAMES]
    y = df["label"]

    model = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42)
    model.fit(X, y)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return MODEL_PATH


if __name__ == "__main__":
    model_path = train_and_save_model()
    print(f"Model saved to {model_path}")
