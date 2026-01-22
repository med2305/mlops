"""
Example: Running Multiple Fraud Detection Experiments with Different Parameters
This script demonstrates how to run multiple experiments with MLflow tracking.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

import mlflow
from src.config import MLFLOW_TRACKING_URI, EXPERIMENT_NAME, RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, IMBALANCE_RATIO
from src.data.data_loader import generate_fraud_data
from src.data.preprocessing import preprocess_data
from src.models.train import train_model, evaluate_model, save_model

# Different parameter configurations to test for fraud detection
EXPERIMENT_CONFIGS = [
    {
        "name": "Baseline: Balanced Classes",
        "params": {"n_estimators": 100, "max_depth": 8, "class_weight": "balanced", "random_state": 42}
    },
    {
        "name": "Deep Trees: Better Patterns",
        "params": {"n_estimators": 150, "max_depth": 15, "class_weight": "balanced", "random_state": 42}
    },
    {
        "name": "Many Trees: Ensemble Power",
        "params": {"n_estimators": 300, "max_depth": 10, "class_weight": "balanced", "random_state": 42}
    },
    {
        "name": "Optimized: High Recall",
        "params": {"n_estimators": 200, "max_depth": 12, "min_samples_split": 5, 
                  "min_samples_leaf": 2, "class_weight": "balanced", "random_state": 42}
    },
    {
        "name": "Conservative: Low False Positives",
        "params": {"n_estimators": 200, "max_depth": 8, "min_samples_split": 20, 
                  "min_samples_leaf": 10, "class_weight": "balanced", "random_state": 42}
    }
]

def run_experiment(config, X_train, X_test, y_train, y_test):
    """Run a single experiment with the given configuration."""
    print(f"\n{'='*60}")
    print(f"Running: {config['name']}")
    print(f"Parameters: {config['params']}")
    print(f"{'='*60}")
    
    # Set MLflow tracking
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)
    
    with mlflow.start_run(run_name=config['name']):
        # Log configuration name
        mlflow.log_param("experiment_name", config['name'])
        
        # Train model
        model = train_model(X_train, y_train, config['params'], EXPERIMENT_NAME)
        
        # Evaluate model
        metrics = evaluate_model(model, X_test, y_test, log_to_mlflow=True)
        
        # Log additional tags
        mlflow.set_tag("experiment_type", "hyperparameter_tuning")
        mlflow.set_tag("model_type", "RandomForest")
        
        print(f"\nResults for {config['name']}:")
        for metric_name, metric_value in metrics.items():
            print(f"  {metric_name}: {metric_value:.4f}")
    
    return metrics

def main():
    print("="*60)
    print("Fraud Detection - Multiple Experiments Demo")
    print("="*60)
    
    # Load and preprocess data once
    print("\nGenerating and preprocessing fraud detection data...")
    df = generate_fraud_data(n_samples=10000, fraud_ratio=IMBALANCE_RATIO, save_path=RAW_DATA_DIR)
    X_train, X_test, y_train, y_test, scaler, encoders = preprocess_data(
        df, test_size=0.3, random_state=42, save_path=PROCESSED_DATA_DIR
    )
    
    print(f"Training set: {len(X_train)} samples (Fraud: {y_train.mean()*100:.2f}%)")
    print(f"Test set: {len(X_test)} samples (Fraud: {y_test.mean()*100:.2f}%)")
    
    # Run all experiments
    results = []
    for config in EXPERIMENT_CONFIGS:
        metrics = run_experiment(config, X_train, X_test, y_train, y_test)
        results.append({
            "name": config['name'],
            "params": config['params'],
            "metrics": metrics
        })
    
    # Print summary
    print("\n" + "="*70)
    print("FRAUD DETECTION EXPERIMENT SUMMARY")
    print("="*70)
    print()
    print(f"{'Experiment':<40} {'ROC-AUC':<12} {'Recall':<12} {'Precision':<12}")
    print("-"*70)
    
    for result in results:
        print(f"{result['name']:<40} "
              f"{result['metrics']['roc_auc']:<12.4f} "
              f"{result['metrics']['recall']:<12.4f} "
              f"{result['metrics']['precision']:<12.4f}")
    
    # Find best model by ROC-AUC (important for fraud detection)
    best_result = max(results, key=lambda x: x['metrics']['roc_auc'])
    
    print()
    print("="*70)
    print(f"🏆 Best Model (by ROC-AUC): {best_result['name']}")
    print(f"   ROC-AUC: {best_result['metrics']['roc_auc']:.4f}")
    print(f"   Recall (Fraud Detection Rate): {best_result['metrics']['recall']:.4f}")
    print(f"   Precision: {best_result['metrics']['precision']:.4f}")
    print(f"   Parameters: {best_result['params']}")
    print("="*70)
    print()
    print("✅ All fraud detection experiments completed!")
    print(f"📊 View results in MLflow UI: {MLFLOW_TRACKING_URI}")
    print()
    print("To view MLflow UI:")
    print("  mlflow ui --host 0.0.0.0 --port 5000")

if __name__ == "__main__":
    main()
