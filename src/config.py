"""Configuration settings for the MLOps project."""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create directories if they don't exist
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# MLflow configuration
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
EXPERIMENT_NAME = "fraud_detection"

# Model parameters for fraud detection
MODEL_PARAMS = {
    "n_estimators": 200,
    "max_depth": 10,
    "min_samples_split": 10,
    "min_samples_leaf": 5,
    "class_weight": "balanced",  # Important for imbalanced fraud data
    "random_state": 42
}

# Data parameters
TEST_SIZE = 0.3
RANDOM_STATE = 42

# Fraud detection specific parameters
FRAUD_THRESHOLD = 0.5  # Probability threshold for fraud classification
IMBALANCE_RATIO = 0.1  # Expected ratio of fraud cases in synthetic data
