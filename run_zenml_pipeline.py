"""
Simple ZenML Pipeline Runner for Fraud Detection
This version bypasses authentication issues by running pipeline steps manually.
"""

import sys
from pathlib import Path
import logging

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from src.config import (
    RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR,
    MLFLOW_TRACKING_URI, EXPERIMENT_NAME, MODEL_PARAMS,
    TEST_SIZE, RANDOM_STATE, IMBALANCE_RATIO
)
from src.data.data_loader import generate_fraud_data
from src.data.preprocessing import preprocess_data
from src.models.train import train_model, evaluate_model, save_model

import mlflow

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_fraud_detection_pipeline():
    """
    Run the complete fraud detection pipeline without ZenML client issues.
    Executes the same steps as the ZenML pipeline but directly.
    """
    
    logger.info("=" * 70)
    logger.info("STARTING FRAUD DETECTION PIPELINE (ZenML Architecture)")
    logger.info("=" * 70)
    logger.info(f"MLflow tracking URI: {MLFLOW_TRACKING_URI}")
    logger.info(f"Experiment name: {EXPERIMENT_NAME}")
    logger.info("")
    
    try:
        # Step 1: Load/Generate Data
        logger.info("=" * 70)
        logger.info("STEP 1: LOADING/GENERATING FRAUD DETECTION DATA")
        logger.info("=" * 70)
        df = generate_fraud_data(
            n_samples=10000,
            fraud_ratio=IMBALANCE_RATIO,
            save_path=RAW_DATA_DIR
        )
        logger.info(f"✅ Data loaded successfully: {df.shape[0]} transactions")
        logger.info(f"   - Fraudulent: {df['is_fraud'].sum()}")
        logger.info(f"   - Legitimate: {(~df['is_fraud']).sum()}")
        logger.info("")
        
        # Step 2: Preprocess Data
        logger.info("=" * 70)
        logger.info("STEP 2: PREPROCESSING DATA")
        logger.info("=" * 70)
        X_train, X_test, y_train, y_test, scaler, encoders = preprocess_data(
            df,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
            save_path=PROCESSED_DATA_DIR
        )
        logger.info(f"✅ Data preprocessed successfully")
        logger.info(f"   - Training samples: {X_train.shape[0]}")
        logger.info(f"   - Test samples: {X_test.shape[0]}")
        logger.info(f"   - Features: {X_train.shape[1]}")
        logger.info("")
        
        # Step 3: Train Model
        logger.info("=" * 70)
        logger.info("STEP 3: TRAINING FRAUD DETECTION MODEL")
        logger.info("=" * 70)
        logger.info(f"Model parameters: {MODEL_PARAMS}")
        
        # Set MLflow tracking
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        
        model = train_model(
            X_train,
            y_train,
            params=MODEL_PARAMS,
            experiment_name=EXPERIMENT_NAME
        )
        logger.info("✅ Model trained successfully")
        logger.info("")
        
        # Step 4: Evaluate Model
        logger.info("=" * 70)
        logger.info("STEP 4: EVALUATING MODEL")
        logger.info("=" * 70)
        metrics = evaluate_model(
            model,
            X_test,
            y_test,
            log_to_mlflow=True
        )
        
        logger.info("✅ Model evaluated successfully")
        logger.info("")
        logger.info("📊 EVALUATION METRICS:")
        logger.info(f"   - Accuracy:          {metrics['accuracy']:.4f}")
        logger.info(f"   - Precision:         {metrics['precision']:.4f}")
        logger.info(f"   - Recall:            {metrics['recall']:.4f}")
        logger.info(f"   - F1-Score:          {metrics['f1_score']:.4f}")
        logger.info(f"   - ROC-AUC:           {metrics['roc_auc']:.4f}")
        logger.info(f"   - False Positive Rate: {metrics.get('false_positive_rate', 'N/A')}")
        logger.info("")
        logger.info("📈 CONFUSION MATRIX:")
        logger.info(f"   - True Negatives:    {metrics['true_negatives']}")
        logger.info(f"   - False Positives:   {metrics['false_positives']}")
        logger.info(f"   - False Negatives:   {metrics['false_negatives']}")
        logger.info(f"   - True Positives:    {metrics['true_positives']}")
        logger.info("")
        
        # Step 5: Save Model
        logger.info("=" * 70)
        logger.info("STEP 5: SAVING MODEL")
        logger.info("=" * 70)
        save_model(model, MODELS_DIR, model_name="fraud_detector.pkl")
        logger.info(f"✅ Model saved to: {MODELS_DIR / 'fraud_detector.pkl'}")
        logger.info("")
        
        # Pipeline Summary
        logger.info("=" * 70)
        logger.info("🎉 PIPELINE EXECUTION COMPLETED SUCCESSFULLY!")
        logger.info("=" * 70)
        logger.info("")
        logger.info("📁 Output Files:")
        logger.info(f"   - Raw data: {RAW_DATA_DIR}")
        logger.info(f"   - Processed data: {PROCESSED_DATA_DIR}")
        logger.info(f"   - Model: {MODELS_DIR / 'fraud_detector.pkl'}")
        logger.info(f"   - MLflow runs: ./mlruns")
        logger.info("")
        logger.info("🔍 Next Steps:")
        logger.info("   1. View results in MLflow UI:")
        logger.info(f"      mlflow ui")
        logger.info("   2. Access the UI at: http://localhost:5000")
        logger.info("   3. Deploy the model using the saved pickle file")
        logger.info("")
        logger.info("=" * 70)
        
        return {
            'model': model,
            'metrics': metrics,
            'data': {
                'X_train': X_train,
                'X_test': X_test,
                'y_train': y_train,
                'y_test': y_test
            }
        }
        
    except Exception as e:
        logger.error("=" * 70)
        logger.error("❌ PIPELINE EXECUTION FAILED!")
        logger.error("=" * 70)
        logger.error(f"Error: {str(e)}")
        logger.error("")
        import traceback
        traceback.print_exc()
        raise


if __name__ == "__main__":
    result = run_fraud_detection_pipeline()
    
    # Print final summary
    print("\n" + "=" * 70)
    print("✨ ZenML-STYLE PIPELINE COMPLETED")
    print("=" * 70)
    print(f"\n🎯 Final Performance: ROC-AUC = {result['metrics']['roc_auc']:.4f}")
    print(f"📊 Fraud Detection Rate (Recall) = {result['metrics']['recall']:.4f}")
    print(f"🎯 Precision = {result['metrics']['precision']:.4f}")
    print("\n" + "=" * 70)
