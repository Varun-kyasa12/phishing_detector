# Phishing Website Detection Application

This project is a full stack phishing URL detection system with:

- `springboot-backend`: Java Spring Boot REST API
- `python-ml-api`: Flask ML service using a Random Forest classifier
- `frontend`: Static web UI for URL checks and history dashboard
- `database`: Optional SQL schema reference

## Project Structure

```text
phishing-detection-app/
|-- database/
|-- frontend/
|-- python-ml-api/
`-- springboot-backend/
```

## Features

- Submit a URL from the frontend
- Spring Boot calls the Flask ML API for phishing prediction
- Prediction, risk score, URL, and timestamp are stored in backend memory during runtime
- View runtime scan history on the dashboard page

## Prerequisites

- Java 17+
- Maven 3.9+ or the Maven wrapper
- Python 3.10+

## 1. Runtime Storage

The current backend uses in-memory storage for URL history.

- No MySQL setup is required
- History remains available while the backend is running
- History resets when the backend restarts

## 2. Start the Python ML API

```powershell
cd python-ml-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train_model.py
python app.py
```

The Flask API runs on `http://localhost:5000`.

## 3. Start the Spring Boot Backend

Then run:

```powershell
cd springboot-backend
build-backend.bat
run-backend.bat
```

The backend runs on `http://localhost:8080`.

You can also use the helper script:

```powershell
cd springboot-backend
run-backend.bat
```

## 4. Open the Frontend

You can open the frontend files directly in a browser or serve them with a lightweight server:

```powershell
cd frontend
python -m http.server 5500
```

Then open:

- `http://localhost:5500/index.html`
- `http://localhost:5500/dashboard.html`

## API Endpoints

- `POST /check-url`
- `GET /history`

### `POST /check-url`

Request:

```json
{
  "url": "https://example.com/login"
}
```

Response:

```json
{
  "id": 1,
  "url": "https://example.com/login",
  "result": "Legitimate",
  "riskScore": 0.18,
  "date": "2026-03-24T10:20:15"
}
```

## Notes

- `train_model.py` creates the Random Forest model file used by Flask.
- If the trained model is missing, the Flask app can bootstrap one from the bundled synthetic dataset.
- The frontend expects the backend at `http://localhost:8080`.
- The backend reads `ML_API_URL` from environment variables if you want to override the default Flask endpoint.
- The Flask service can be started with `run-flask.bat`.
- [schema.sql](/C:/Users/varun/OneDrive/Documents/New%20project/phishing-detection-app/database/schema.sql) is kept only as an optional reference if you later want to restore MySQL persistence.
