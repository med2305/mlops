# 🚨 Fraud Detection MLOps Project

## Overview

This is a complete **fraud detection machine learning project** that demonstrates modern MLOps practices. The system detects fraudulent transactions using machine learning while maintaining full reproducibility, version control, and experiment tracking.

## Business Problem

**Objective**: Identify fraudulent transactions in real-time to prevent financial losses.

**Challenges**:
- Imbalanced data (fraud is rare, typically <1-10% of transactions)
- High cost of false negatives (missed fraud)
- Need to minimize false positives (legitimate transactions flagged as fraud)
- Requirement for model explainability and monitoring

## Technical Solution

### Machine Learning Approach

**Model**: Random Forest Classifier
- Handles non-linear patterns well
- Robust to outliers
- Provides feature importance
- Good performance on imbalanced data with `class_weight='balanced'`

**Features** (Synthetic Data):
- `amount`: Transaction amount
- `time_of_day`: Hour of transaction (0-23)
- `transaction_frequency`: Number of recent transactions
- `account_age_days`: Age of the account
- `merchant_category`: Type of merchant
- `distance_from_home`: Distance from usual location
- `previous_fraud_rate`: Historical fraud rate for the account

**Target**: `is_fraud` (0 = legitimate, 1 = fraudulent)

### Key Metrics

For fraud detection, we focus on:

1. **ROC-AUC** (Primary metric)
   - Measures overall discrimination ability
   - Important for ranking transactions by risk

2. **Recall** (Fraud Detection Rate)
   - Percentage of actual frauds detected
   - Critical: Missing fraud is costly

3. **Precision**
   - Percentage of fraud alerts that are real
   - Important: Too many false alarms hurt user experience

4. **Confusion Matrix**
   - True Positives (TP): Correctly identified fraud
   - False Positives (FP): Legitimate flagged as fraud
   - False Negatives (FN): Missed fraud ⚠️
   - True Negatives (TN): Correctly identified legitimate

## Project Structure

```
fraud-detection-mlops/
├── data/
│   ├── raw/                    # Generated fraud transaction data
│   │   └── fraud_transactions.csv
│   └── processed/              # Preprocessed train/test splits
│       ├── X_train.npy
│       ├── X_test.npy
│       ├── y_train.npy
│       ├── y_test.npy
│       ├── scaler.pkl
│       └── encoders.pkl
│
├── models/                     # Trained fraud detection models
│   └── fraud_detector.pkl
│
├── src/
│   ├── config.py              # Project configuration
│   ├── data/
│   │   ├── data_loader.py     # Fraud data generation
│   │   └── preprocessing.py   # Feature engineering
│   ├── models/
│   │   └── train.py           # Model training & evaluation
│   └── pipelines/
│       └── training_pipeline.py  # ZenML orchestration
│
├── .dvc/                      # DVC configuration
├── .zen/                      # ZenML configuration
├── mlruns/                    # MLflow experiments
└── docker-compose.yml         # Deployment configuration
```

## MLOps Components

### 1. Git - Code Version Control
- All source code tracked
- Branching for feature development
- Collaboration-ready

### 2. DVC - Data Version Control
- Tracks fraud transaction datasets
- Versions trained models
- Enables data reproducibility
- Supports remote storage (S3, GCS, Azure, etc.)

### 3. MLflow - Experiment Tracking
- Logs all experiments automatically
- Tracks parameters: `n_estimators`, `max_depth`, `class_weight`
- Records metrics: ROC-AUC, precision, recall, F1
- Stores model artifacts
- Provides web UI for comparison

### 4. ZenML - Pipeline Orchestration
Defines a 5-step pipeline:
1. **Data Generation**: Create synthetic fraud data
2. **Preprocessing**: Feature engineering and scaling
3. **Training**: Train Random Forest with balanced classes
4. **Evaluation**: Calculate fraud detection metrics
5. **Model Saving**: Persist model and artifacts

### 5. Docker - Containerization
- Consistent development environment
- Easy deployment to production
- Multi-service orchestration (MLflow + App + Jupyter)

## Data Generation

Since real fraud data is sensitive, we generate **synthetic data** that mimics real-world patterns:

**Legitimate Transactions**:
- Lower amounts (exponential distribution, mean ~$50)
- Normal business hours
- Moderate frequency
- Established accounts
- Common merchant categories

**Fraudulent Transactions**:
- Higher amounts (exponential distribution, mean ~$200)
- Unusual hours (late night/early morning)
- Higher frequency (burst activity)
- Newer accounts
- Risky merchant categories
- Far from home location

Default: 10,000 transactions with 10% fraud rate

## Running the Project

### Quick Start
```powershell
# Setup everything
.\setup.ps1

# Run the fraud detection pipeline
.\venv\Scripts\Activate.ps1
python src\pipelines\training_pipeline.py

# View results in MLflow
mlflow ui --host 0.0.0.0 --port 5000
```

### Run Multiple Experiments
```powershell
python run_experiments.py
```

Tests different configurations:
- Baseline model
- Deep trees for complex patterns
- Many trees for ensemble power
- Optimized for high recall (catch more fraud)
- Conservative for low false positives

### Docker Deployment
```powershell
docker-compose up --build
```

Services:
- MLflow UI: http://localhost:5000
- Jupyter Notebook: http://localhost:8888

## Experiment Tracking Example

When you run the pipeline, MLflow automatically logs:

**Parameters**:
```python
{
    "n_estimators": 200,
    "max_depth": 10,
    "class_weight": "balanced",
    "min_samples_split": 10,
    "min_samples_leaf": 5
}
```

**Metrics**:
```python
{
    "accuracy": 0.9567,
    "precision": 0.8234,
    "recall": 0.8912,      # 89% of frauds detected
    "f1_score": 0.8560,
    "roc_auc": 0.9745,     # Excellent discrimination
    "true_positives": 267,
    "false_positives": 58,
    "false_negatives": 33,  # 33 frauds missed
    "true_negatives": 2642
}
```

**Artifacts**:
- Trained model
- Scaler
- Encoders
- Feature names

## Model Performance Interpretation

### Good Model Example:
- ROC-AUC > 0.95: Excellent at ranking risky transactions
- Recall > 0.85: Catching 85%+ of fraud
- Precision > 0.75: Most fraud alerts are real
- Low FN count: Minimizing missed fraud

### Trade-offs:
- **High Recall**: Catch more fraud, but more false alarms
- **High Precision**: Fewer false alarms, but miss some fraud
- **Balanced**: Optimize F1-score for overall performance

Adjust threshold based on business requirements!

## Customization

### Change Fraud Rate
Edit `src/config.py`:
```python
IMBALANCE_RATIO = 0.05  # 5% fraud instead of 10%
```

### Adjust Model Parameters
Edit `src/config.py`:
```python
MODEL_PARAMS = {
    "n_estimators": 300,      # More trees
    "max_depth": 15,          # Deeper trees
    "class_weight": "balanced" # Handle imbalance
}
```

### Use Real Data
Replace `generate_fraud_data()` in `src/data/data_loader.py` with your own data loader.

## Production Considerations

For real-world deployment:

1. **Data Pipeline**
   - Connect to transaction database
   - Real-time feature engineering
   - Data quality checks

2. **Model Monitoring**
   - Track prediction distribution
   - Monitor fraud detection rate
   - Alert on model drift

3. **Threshold Tuning**
   - Adjust based on business costs
   - A/B test different thresholds
   - Dynamic thresholds by merchant/user

4. **Explainability**
   - Use SHAP values
   - Feature importance
   - Provide reasons for fraud flags

5. **Compliance**
   - Model documentation
   - Audit trail
   - Fairness testing

## Next Steps

1. ✅ Run baseline experiments
2. ✅ Compare models in MLflow UI
3. ✅ Analyze feature importance
4. 🔄 Tune hyperparameters
5. 🔄 Implement real-time scoring API
6. 🔄 Add model monitoring
7. 🔄 Deploy to production

## Resources

- **MLflow UI**: View all experiments and compare metrics
- **Documentation**: See README.md, GUIDE.md, QUICKSTART.md
- **Code**: All source in `src/` directory
- **Examples**: Run `run_experiments.py` for comparisons

## Success Metrics

This project successfully demonstrates:
- ✅ Handling imbalanced classification
- ✅ Fraud-specific metrics (ROC-AUC, recall, precision)
- ✅ Full MLOps pipeline (Git + DVC + MLflow + ZenML)
- ✅ Reproducible experiments
- ✅ Containerized deployment
- ✅ Version control for code, data, and models

---

**Built with**: Python, scikit-learn, MLflow, ZenML, DVC, Docker
**Use Case**: Financial Fraud Detection
**Status**: Ready for experimentation and extension
