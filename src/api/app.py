"""FastAPI application for fraud detection model serving."""

import os
import pickle
import numpy as np
from typing import Dict, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Fraud Detection API",
    description="Real-time fraud detection using ML model",
    version="1.0.0"
)

# Global variables for model and preprocessing artifacts
model = None
scaler = None
encoders = None
feature_names = None


class Transaction(BaseModel):
    """Transaction input schema."""
    amount: float = Field(..., description="Transaction amount", example=150.75)
    merchant_category: str = Field(..., description="Merchant category", example="grocery")
    time_of_day: str = Field(..., description="Time of day", example="morning")
    location: str = Field(..., description="Location", example="online")
    transaction_type: str = Field(..., description="Transaction type", example="purchase")
    
    class Config:
        schema_extra = {
            "example": {
                "amount": 150.75,
                "merchant_category": "grocery",
                "time_of_day": "morning",
                "location": "online",
                "transaction_type": "purchase"
            }
        }


class PredictionResponse(BaseModel):
    """Prediction response schema."""
    is_fraud: bool = Field(..., description="Whether transaction is fraudulent")
    fraud_probability: float = Field(..., description="Probability of fraud (0-1)")
    confidence: str = Field(..., description="Confidence level: low, medium, high")


def load_model_artifacts():
    """Load model and preprocessing artifacts."""
    global model, scaler, encoders, feature_names
    
    try:
        # Load model - try different paths and formats
        model_paths = [
            "models/fraud_detection_model.pkl",
            "models/fraud_detector.pkl"
        ]
        
        model_loaded = False
        for model_path in model_paths:
            if os.path.exists(model_path):
                try:
                    with open(model_path, "rb") as f:
                        # Try loading with different protocols
                        try:
                            model = pickle.load(f)
                            model_loaded = True
                            print(f"✅ Loaded model from: {model_path}")
                            break
                        except Exception:
                            # Try with joblib if pickle fails
                            import joblib
                            f.seek(0)
                            model = joblib.load(f)
                            model_loaded = True
                            print(f"✅ Loaded model from: {model_path} (using joblib)")
                            break
                except Exception as e:
                    print(f"⚠️  Failed to load {model_path}: {e}")
                    continue
        
        if not model_loaded:
            raise Exception("No valid model file found")
        
        # Load preprocessing artifacts
        with open("data/processed/scaler.pkl", "rb") as f:
            scaler = pickle.load(f)
        
        with open("data/processed/encoders.pkl", "rb") as f:
            encoders = pickle.load(f)
        
        with open("data/processed/feature_names.pkl", "rb") as f:
            feature_names = pickle.load(f)
        
        print("✅ Model and artifacts loaded successfully!")
        
    except Exception as e:
        print(f"❌ Error loading model artifacts: {e}")
        raise


@app.on_event("startup")
async def startup_event():
    """Load model on startup."""
    load_model_artifacts()


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Fraud Detection API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "batch_predict": "/batch-predict",
            "docs": "/docs"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "scaler_loaded": scaler is not None,
        "encoders_loaded": encoders is not None
    }


def preprocess_transaction(transaction: Transaction) -> np.ndarray:
    """Preprocess transaction data for prediction."""
    # Create feature dictionary
    features = {
        'amount': transaction.amount,
        'merchant_category': transaction.merchant_category,
        'time_of_day': transaction.time_of_day,
        'location': transaction.location,
        'transaction_type': transaction.transaction_type
    }
    
    # Encode categorical features
    encoded_features = []
    for feature_name in feature_names:
        if feature_name == 'amount':
            encoded_features.append(features['amount'])
        else:
            # Extract the original feature name from encoded feature name
            # e.g., 'merchant_category_grocery' -> 'merchant_category'
            for orig_feature in ['merchant_category', 'time_of_day', 'location', 'transaction_type']:
                if feature_name.startswith(orig_feature):
                    value = features[orig_feature]
                    # Check if this is the matching encoded feature
                    expected_name = f"{orig_feature}_{value}"
                    encoded_features.append(1.0 if feature_name == expected_name else 0.0)
                    break
    
    # Convert to numpy array and reshape
    X = np.array(encoded_features).reshape(1, -1)
    
    # Scale features
    X_scaled = scaler.transform(X)
    
    return X_scaled


@app.post("/predict", response_model=PredictionResponse)
async def predict(transaction: Transaction):
    """Predict fraud for a single transaction."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Preprocess transaction
        X = preprocess_transaction(transaction)
        
        # Make prediction
        fraud_prob = model.predict_proba(X)[0][1]
        is_fraud = bool(fraud_prob > 0.5)
        
        # Determine confidence level
        if fraud_prob < 0.3 or fraud_prob > 0.7:
            confidence = "high"
        elif fraud_prob < 0.4 or fraud_prob > 0.6:
            confidence = "medium"
        else:
            confidence = "low"
        
        return PredictionResponse(
            is_fraud=is_fraud,
            fraud_probability=float(fraud_prob),
            confidence=confidence
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


class BatchTransactions(BaseModel):
    """Batch transactions input schema."""
    transactions: List[Transaction]


class BatchPredictionResponse(BaseModel):
    """Batch prediction response schema."""
    predictions: List[PredictionResponse]
    total_transactions: int
    fraud_count: int
    fraud_percentage: float


@app.post("/batch-predict", response_model=BatchPredictionResponse)
async def batch_predict(batch: BatchTransactions):
    """Predict fraud for multiple transactions."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        predictions = []
        fraud_count = 0
        
        for transaction in batch.transactions:
            result = await predict(transaction)
            predictions.append(result)
            if result.is_fraud:
                fraud_count += 1
        
        total = len(batch.transactions)
        fraud_pct = (fraud_count / total * 100) if total > 0 else 0
        
        return BatchPredictionResponse(
            predictions=predictions,
            total_transactions=total,
            fraud_count=fraud_count,
            fraud_percentage=round(fraud_pct, 2)
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch prediction error: {str(e)}")


@app.get("/model-info")
async def model_info():
    """Get model information."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return {
        "model_type": type(model).__name__,
        "n_features": len(feature_names),
        "feature_names": feature_names,
        "categorical_features": list(encoders.keys()) if encoders else []
    }


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
