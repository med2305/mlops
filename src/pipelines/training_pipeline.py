"""ZenML fraud detection training pipeline with MLflow integration."""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from zenml import pipeline, step
import mlflow
import logging

from src.config import (
    RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR,
    MLFLOW_TRACKING_URI, EXPERIMENT_NAME, MODEL_PARAMS,
    TEST_SIZE, RANDOM_STATE, IMBALANCE_RATIO
)
from src.data.data_loader import generate_fraud_data
from src.data.preprocessing import preprocess_data
from src.models.train import train_model, evaluate_model, save_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@step
def load_data_step() -> dict:
    """Load or generate the fraud detection dataset."""
    logger.info("Step 1: Loading fraud detection data...")
    df = generate_fraud_data(
        n_samples=10000, 
        fraud_ratio=IMBALANCE_RATIO,
        save_path=RAW_DATA_DIR
    )
    return {"dataframe": df}


@step
def preprocess_data_step(data: dict) -> dict:
    """Preprocess the fraud detection data."""
    logger.info("Step 2: Preprocessing fraud detection data...")
    df = data["dataframe"]
    X_train, X_test, y_train, y_test, scaler, encoders = preprocess_data(
        df, test_size=TEST_SIZE, random_state=RANDOM_STATE, save_path=PROCESSED_DATA_DIR
    )
    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "scaler": scaler,
        "encoders": encoders
    }


@step
def train_model_step(data: dict) -> dict:
    """Train the fraud detection model."""
    logger.info("Step 3: Training fraud detection model...")
    
    # Set MLflow tracking URI
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    
    model = train_model(
        data["X_train"],
        data["y_train"],
        params=MODEL_PARAMS,
        experiment_name=EXPERIMENT_NAME
    )
    return {"model": model, **data}


@step
def evaluate_model_step(data: dict) -> dict:
    """Evaluate the fraud detection model."""
    logger.info("Step 4: Evaluating fraud detection model...")
    
    metrics = evaluate_model(
        data["model"],
        data["X_test"],
        data["y_test"],
        log_to_mlflow=True
    )
    return {"metrics": metrics, **data}


@step
def save_model_step(data: dict) -> None:
    """Save the fraud detection model."""
    logger.info("Step 5: Saving fraud detection model...")
    save_model(data["model"], MODELS_DIR, model_name="fraud_detector.pkl")
    
    logger.info("\n" + "="*60)
    logger.info("FRAUD DETECTION PIPELINE COMPLETED!")
    logger.info("="*60)
    logger.info(f"\nModel Performance:")
    logger.info(f"  Accuracy: {data['metrics']['accuracy']:.4f}")
    logger.info(f"  Precision: {data['metrics']['precision']:.4f}")
    logger.info(f"  Recall (Fraud Detection Rate): {data['metrics']['recall']:.4f}")
    logger.info(f"  F1-Score: {data['metrics']['f1_score']:.4f}")
    logger.info(f"  ROC-AUC: {data['metrics']['roc_auc']:.4f}")
    logger.info(f"\nConfusion Matrix:")
    logger.info(f"  True Negatives: {data['metrics']['true_negatives']}")
    logger.info(f"  False Positives: {data['metrics']['false_positives']}")
    logger.info(f"  False Negatives: {data['metrics']['false_negatives']}")
    logger.info(f"  True Positives: {data['metrics']['true_positives']}")
    logger.info("="*60)


@pipeline
def fraud_detection_pipeline():
    """Complete fraud detection ML pipeline."""
    data = load_data_step()
    preprocessed_data = preprocess_data_step(data)
    trained_data = train_model_step(preprocessed_data)
    evaluated_data = evaluate_model_step(trained_data)
    save_model_step(evaluated_data)


if __name__ == "__main__":
    logger.info("="*60)
    logger.info("STARTING FRAUD DETECTION PIPELINE")
    logger.info("="*60)
    logger.info(f"MLflow tracking URI: {MLFLOW_TRACKING_URI}")
    logger.info(f"Experiment name: {EXPERIMENT_NAME}")
    
    # Run the pipeline
    pipeline_instance = fraud_detection_pipeline()
    pipeline_instance.run()
    
    logger.info("\n✅ Pipeline execution completed successfully!")
    logger.info(f"📊 View results in MLflow UI: {MLFLOW_TRACKING_URI}")
