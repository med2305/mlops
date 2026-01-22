"""
Simple Fraud Detection Pipeline Runner (Without ZenML)
This script runs the fraud detection pipeline using only MLflow tracking.
"""

import sys
import os
import logging
from pathlib import Path

# Add src directory to path
sys.path.append(str(Path(__file__).parent / "src"))

import mlflow
import joblib
from src.config import EXPERIMENT_NAME, MLFLOW_TRACKING_URI, MODEL_PARAMS
from src.data.data_loader import generate_fraud_data
from src.data.preprocessing import preprocess_data
from src.models.train import train_model, evaluate_model

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Run the fraud detection pipeline."""
    
    print("=" * 60)
    print("FRAUD DETECTION PIPELINE (MLFLOW VERSION)")
    print("=" * 60)
    
    # Configure MLflow (use local file storage if server is not running)
    mlflow.set_tracking_uri("file:./mlruns")
    mlflow.set_experiment(EXPERIMENT_NAME)
    
    logger.info(f"MLflow tracking URI: file:./mlruns")
    logger.info(f"Experiment name: {EXPERIMENT_NAME}")
    
    # Start MLflow run
    with mlflow.start_run():
        # Log parameters
        mlflow.log_params(MODEL_PARAMS)
        
        # Step 1: Load data
        logger.info("\n📊 Step 1/5: Loading fraud transaction data...")
        df = generate_fraud_data(n_samples=10000, fraud_ratio=0.1)
        logger.info(f"Generated {len(df)} transactions ({df['is_fraud'].sum()} fraudulent)")
        
        # Step 2: Preprocess data
        logger.info("\n🔧 Step 2/5: Preprocessing data...")
        result = preprocess_data(df)
        X_train, X_test, y_train, y_test = result[:4]  # Get first 4 elements
        logger.info(f"Train set: {len(X_train)} samples")
        logger.info(f"Test set: {len(X_test)} samples")
        
        # Step 3: Train model
        logger.info("\n🤖 Step 3/5: Training fraud detection model...")
        model = train_model(X_train, y_train, MODEL_PARAMS)
        logger.info("Model training completed!")
        
        # Step 4: Evaluate model
        logger.info("\n📈 Step 4/5: Evaluating model performance...")
        metrics = evaluate_model(model, X_test, y_test)
        
        # Log metrics to MLflow
        for metric_name, metric_value in metrics.items():
            if not metric_name.startswith("confusion_matrix"):
                mlflow.log_metric(metric_name, metric_value)
        
        logger.info(f"ROC-AUC Score: {metrics['roc_auc']:.4f}")
        logger.info(f"Recall (Fraud Detection Rate): {metrics['recall']:.4f}")
        logger.info(f"Precision: {metrics['precision']:.4f}")
        logger.info(f"F1 Score: {metrics['f1_score']:.4f}")
        logger.info(f"False Positive Rate: {metrics['false_positive_rate']:.4f}")
        
        # Step 5: Save model
        logger.info("\n💾 Step 5/5: Saving model...")
        os.makedirs("models", exist_ok=True)
        model_path = "models/fraud_detection_model.pkl"
        joblib.dump(model, model_path)
        logger.info(f"Model saved to: {model_path}")
        
        # Log model to MLflow
        mlflow.sklearn.log_model(model, "model")
        
    print("\n" + "=" * 60)
    print("✅ PIPELINE EXECUTION COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print(f"\n📊 Results saved in mlruns directory")
    print(f"🚀 To view in MLflow UI run: mlflow ui")
    print("=" * 60)

if __name__ == "__main__":
    main()
