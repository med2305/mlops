"""Model training utilities for fraud detection."""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)
import mlflow
import mlflow.sklearn
import logging
from pathlib import Path
import pickle

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def train_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    params: dict,
    experiment_name: str = "default"
) -> RandomForestClassifier:
    """
    Train a Random Forest model for fraud detection with MLflow tracking.
    
    Args:
        X_train: Training features
        y_train: Training labels
        params: Model hyperparameters
        experiment_name: MLflow experiment name
        
    Returns:
        Trained model
    """
    logger.info("Starting model training for fraud detection...")
    logger.info(f"Training samples: {len(X_train)}, Fraud rate: {y_train.mean()*100:.2f}%")
    
    # Train model
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
        
    logger.info("Model training completed")
        
    return model


def evaluate_model(
    model: RandomForestClassifier,
    X_test: np.ndarray,
    y_test: np.ndarray,
    log_to_mlflow: bool = True
) -> dict:
    """
    Evaluate fraud detection model with comprehensive metrics.
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test labels
        log_to_mlflow: Whether to log to MLflow
        
    Returns:
        Dictionary of metrics
    """
    logger.info("Evaluating model...")
    
    # Predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # Calculate metrics
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_pred_proba)
    }
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()
    
    # Additional fraud-specific metrics
    metrics["true_negatives"] = int(tn)
    metrics["false_positives"] = int(fp)
    metrics["false_negatives"] = int(fn)
    metrics["true_positives"] = int(tp)
    metrics["fraud_detection_rate"] = recall_score(y_test, y_pred)  # Same as recall
    metrics["false_positive_rate"] = fp / (fp + tn) if (fp + tn) > 0 else 0
    
    logger.info(f"Metrics: {metrics}")
    logger.info("\nConfusion Matrix:")
    logger.info(f"  TN: {tn}, FP: {fp}")
    logger.info(f"  FN: {fn}, TP: {tp}")
    logger.info(f"\nFraud Detection Rate (Recall): {metrics['fraud_detection_rate']:.4f}")
    logger.info(f"False Positive Rate: {metrics['false_positive_rate']:.4f}")
    logger.info(f"ROC-AUC Score: {metrics['roc_auc']:.4f}")
    
    # Log to MLflow
    if log_to_mlflow:
        mlflow.log_metrics(metrics)
        
        # Log confusion matrix as text
        cm_text = f"TN={tn}, FP={fp}, FN={fn}, TP={tp}"
        mlflow.log_param("confusion_matrix", cm_text)
    
    return metrics


def save_model(model: RandomForestClassifier, save_path: Path, model_name: str = "fraud_model.pkl"):
    """
    Save model to disk.
    
    Args:
        model: Trained model
        save_path: Directory to save model
        model_name: Name of the model file
    """
    save_path.mkdir(parents=True, exist_ok=True)
    model_path = save_path / model_name
    
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    logger.info(f"Model saved to {model_path}")
