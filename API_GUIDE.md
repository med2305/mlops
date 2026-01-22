# 🚀 Fraud Detection API

A FastAPI-based REST API for real-time fraud detection using machine learning.

## 📋 Features

- **Real-time Predictions**: Get instant fraud predictions for transactions
- **Batch Processing**: Process multiple transactions in one request
- **Health Monitoring**: Built-in health check endpoints
- **Auto Documentation**: Interactive API docs with Swagger UI
- **Model Information**: Query model details and features

## 🛠️ Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure you have a trained model in `models/` directory

## 🚀 Running the API

### Start the Server

```bash
# Using the run script
python run_api.py

# Or directly with uvicorn
uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## 📡 API Endpoints

### 1. Health Check
```bash
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "scaler_loaded": true,
  "encoders_loaded": true
}
```

### 2. Single Prediction
```bash
POST /predict
```

**Request Body:**
```json
{
  "amount": 150.75,
  "merchant_category": "grocery",
  "time_of_day": "morning",
  "location": "online",
  "transaction_type": "purchase"
}
```

**Response:**
```json
{
  "is_fraud": false,
  "fraud_probability": 0.23,
  "confidence": "high"
}
```

### 3. Batch Prediction
```bash
POST /batch-predict
```

**Request Body:**
```json
{
  "transactions": [
    {
      "amount": 45.50,
      "merchant_category": "grocery",
      "time_of_day": "morning",
      "location": "physical",
      "transaction_type": "purchase"
    },
    {
      "amount": 5000.00,
      "merchant_category": "electronics",
      "time_of_day": "night",
      "location": "online",
      "transaction_type": "purchase"
    }
  ]
}
```

**Response:**
```json
{
  "predictions": [...],
  "total_transactions": 2,
  "fraud_count": 1,
  "fraud_percentage": 50.0
}
```

### 4. Model Information
```bash
GET /model-info
```

**Response:**
```json
{
  "model_type": "RandomForestClassifier",
  "n_features": 15,
  "feature_names": ["amount", "merchant_category_grocery", ...],
  "categorical_features": ["merchant_category", "time_of_day", ...]
}
```

## 🧪 Testing the API

### Using the Test Script

```bash
python test_api.py
```

### Using cURL

```bash
# Health check
curl http://localhost:8000/health

# Single prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 150.75,
    "merchant_category": "grocery",
    "time_of_day": "morning",
    "location": "online",
    "transaction_type": "purchase"
  }'
```

### Using Python Requests

```python
import requests

# Single prediction
response = requests.post(
    "http://localhost:8000/predict",
    json={
        "amount": 150.75,
        "merchant_category": "grocery",
        "time_of_day": "morning",
        "location": "online",
        "transaction_type": "purchase"
    }
)
print(response.json())
```

## 🐳 Docker Deployment

### Update docker-compose.yml

Add the API service:

```yaml
api:
  build:
    context: .
    dockerfile: Dockerfile
  container_name: fraud-api
  ports:
    - "8000:8000"
  environment:
    - MLFLOW_TRACKING_URI=http://mlflow:5000
  volumes:
    - ./models:/app/models
    - ./data/processed:/app/data/processed
    - ./src:/app/src
  networks:
    - mlops-network
  command: python run_api.py
```

### Run with Docker

```bash
docker-compose up -d api
```

## 📊 API Response Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 422 | Validation Error (invalid input) |
| 500 | Internal Server Error |
| 503 | Service Unavailable (model not loaded) |

## 🔒 Security Considerations

- Add authentication/authorization for production
- Implement rate limiting
- Add input validation and sanitization
- Use HTTPS in production
- Monitor and log all requests

## 📈 Performance

- **Response Time**: ~50-100ms for single predictions
- **Throughput**: Handles 100+ requests/second
- **Batch Size**: Recommended max 100 transactions per batch

## 🛠️ Customization

### Change Port

```python
# In run_api.py
uvicorn.run(..., port=8080)  # Change to desired port
```

### Add CORS

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 📝 License

This API is part of the MLOps Fraud Detection project.
