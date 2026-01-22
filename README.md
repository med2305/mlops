# 🔐 MLOps Fraud Detection Project

[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)](https://github.com/actions)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)](https://mlflow.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A **complete end-to-end MLOps project** for fraud detection using state-of-the-art tools and practices.

## 🎯 Project Overview

This project demonstrates a **production-ready fraud detection system** with:
- **Git**: Version control for code and configurations
- **DVC**: Data and model versioning (stored in `.dvc/` folder)
- **Docker & Docker Compose**: Containerized deployment and reproducibility
- **MLflow**: Experiment tracking, metrics logging, and model registry
- **ZenML**: ML pipeline orchestration (configured in `.zen/` folder)
- **GitHub Actions**: Automated CI/CD, testing, and deployment

### 🌟 Key Features

- 🔍 **Synthetic Data Generation**: Realistic fraud transaction datasets
- 🤖 **Advanced ML Model**: Random Forest optimized for imbalanced data
- 📊 **Fraud-Specific Metrics**: ROC-AUC, Recall, Precision, False Positive Rate
- 🔄 **Reproducible Pipelines**: Automated with ZenML architecture
- 📈 **Experiment Tracking**: Complete MLflow integration
- 🐳 **Containerized**: Docker Compose with MLflow, Jupyter, and app services
- 🚀 **CI/CD Ready**: GitHub Actions workflows for testing and deployment
- 📦 **PyPI Package**: Ready for distribution to Python Package Index

## 📁 Complete Project Structure

```
mlops/
├── 📂 .github/
│   └── workflows/              # GitHub Actions CI/CD pipelines
│       ├── ci.yml              # Continuous Integration tests
│       ├── code-quality.yml    # Linting and formatting checks
│       ├── deploy.yml          # Deployment automation
│       ├── run-pipeline.yml    # Automated pipeline execution
│       ├── docker-publish.yml  # Docker image publishing
│       ├── publish-pypi.yml    # PyPI package publishing
│       └── release.yml         # Release automation
│
├── 📂 data/
│   ├── raw/                    # Raw transaction data (DVC tracked)
│   │   └── fraud_transactions.csv
│   └── processed/              # Preprocessed features (DVC tracked)
│       ├── X_train.npy
│       ├── X_test.npy
│       ├── y_train.npy
│       ├── y_test.npy
│       ├── scaler.pkl
│       └── encoders.pkl
│
├── 📂 models/                  # Trained models (DVC tracked)
│   └── fraud_detector.pkl      # Production model
│
├── 📂 mlruns/                  # MLflow experiment tracking
│   └── 0/                      # Default experiment
│       └── [run_id]/           # Individual run artifacts
│
├── 📂 notebooks/               # Jupyter notebooks for analysis
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_evaluation.ipynb
│
├── 📂 src/                     # Source code
│   ├── __init__.py
│   ├── config.py               # Configuration and parameters
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loader.py      # Data generation and loading
│   │   └── preprocessing.py    # Feature engineering
│   ├── models/
│   │   ├── __init__.py
│   │   └── train.py            # Model training and evaluation
│   └── pipelines/
│       ├── __init__.py
│       └── training_pipeline.py # ZenML pipeline definition
│
├── 📂 .dvc/                    # DVC configuration (data versioning)
│   ├── config
│   └── .gitignore
│
├── 📂 .zen/                    # ZenML configuration (pipeline orchestration)
│   └── config.yaml
│
├── 📂 .venv/                   # Python virtual environment
│
├── 📄 docker-compose.yml       # Multi-container orchestration
├── 📄 Dockerfile               # Container image definition
├── 📄 requirements.txt         # Python dependencies
├── 📄 setup.py                 # Package setup for PyPI
├── 📄 pyproject.toml          # Modern Python packaging
├── 📄 MANIFEST.in             # Package file manifest
│
├── 📄 run_zenml_pipeline.py   # ZenML pipeline runner
├── 📄 run_simple_fraud_detection.py  # Simplified MLflow runner
├── 📄 run_experiments.py      # Experiment runner
├── 📄 verify_installation.py  # Environment verification
│
├── 📄 README.md               # This file
├── 📄 QUICKSTART.md          # Quick start guide
├── 📄 GUIDE.md               # Detailed usage guide
├── 📄 ARCHITECTURE.md        # System architecture
├── 📄 FRAUD_DETECTION.md     # Fraud detection specifics
├── 📄 GITHUB_ACTIONS.md      # GitHub Actions documentation
├── 📄 PUBLISHING.md          # Publishing guide
├── 📄 CONTRIBUTING.md        # Contribution guidelines
└── 📄 LICENSE                # MIT License
```

## 🛠️ Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| **Python** | 3.9+ (Tested on 3.12) | Runtime environment |
| **Git** | 2.0+ | Version control |
| **Docker** | 20.0+ | Containerization |
| **Docker Compose** | 2.0+ | Multi-container orchestration |
| **DVC** | 3.0+ (Optional) | Data versioning |

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd mlops
```

### 2. Set Up Python Environment

**On Windows (PowerShell):**
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

**On Linux/macOS:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Fraud Detection Pipeline

**Option A: ZenML-Style Pipeline (Recommended)**
```bash
python run_zenml_pipeline.py
```

**Option B: Simple MLflow Pipeline**
```bash
python run_simple_fraud_detection.py
```

### 4. View Results in MLflow UI

```bash
mlflow ui --host 0.0.0.0 --port 5000
```

Then open your browser at: **http://localhost:5000**

## 📋 Available Commands

### **Environment Setup**

| Command | Description |
|---------|-------------|
| `python -m venv .venv` | Create virtual environment |
| `.\.venv\Scripts\Activate.ps1` | Activate venv (Windows) |
| `source .venv/bin/activate` | Activate venv (Linux/macOS) |
| `pip install -r requirements.txt` | Install dependencies |
| `python verify_installation.py` | Verify environment setup |

### **Pipeline Execution**

| Command | Description |
|---------|-------------|
| `python run_zenml_pipeline.py` | Run complete fraud detection pipeline (ZenML architecture) |
| `python run_simple_fraud_detection.py` | Run simplified pipeline (MLflow only) |
| `python run_experiments.py` | Run multiple experiments with different parameters |
| `python src/pipelines/training_pipeline.py` | Run ZenML pipeline directly |

### **MLflow Commands**

| Command | Description |
|---------|-------------|
| `mlflow ui` | Start MLflow UI on http://localhost:5000 |
| `mlflow ui --host 0.0.0.0 --port 5000` | Start MLflow UI (accessible from network) |
| `mlflow ui --backend-store-uri file:./mlruns` | Specify MLflow tracking directory |
| `mlflow models serve -m models:/fraud_detector/production` | Serve model for predictions |
| `mlflow experiments list` | List all experiments |
| `mlflow runs list --experiment-id 0` | List runs in experiment |

### **Docker Commands**

| Command | Description |
|---------|-------------|
| `docker-compose up` | Start all services (MLflow, Jupyter, App) |
| `docker-compose up -d` | Start services in background |
| `docker-compose down` | Stop all services |
| `docker-compose logs -f` | View logs (follow mode) |
| `docker-compose ps` | List running containers |
| `docker-compose build` | Rebuild Docker images |
| `docker build -t fraud-detection .` | Build single Docker image |
| `docker run -p 5000:5000 fraud-detection` | Run container |

### **DVC Commands**

| Command | Description |
|---------|-------------|
| `dvc init` | Initialize DVC in project |
| `dvc add data/raw/fraud_transactions.csv` | Track data file with DVC |
| `dvc add models/fraud_detector.pkl` | Track model with DVC |
| `dvc push` | Push data to remote storage |
| `dvc pull` | Pull data from remote storage |
| `dvc status` | Check DVC status |
| `dvc repro` | Reproduce pipeline |

### **Git Commands**

| Command | Description |
|---------|-------------|
| `git status` | Check repository status |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit changes |
| `git push origin main` | Push to GitHub |
| `git log --oneline` | View commit history |
| `git tag -a v1.0.0 -m "Release v1.0.0"` | Create version tag |
| `git push origin v1.0.0` | Push tag (triggers release) |

### **Testing Commands**

| Command | Description |
|---------|-------------|
| `pytest tests/` | Run all tests |
| `pytest tests/ -v` | Run tests (verbose) |
| `pytest tests/ --cov=src` | Run tests with coverage |
| `pytest tests/ --cov=src --cov-report=html` | Generate HTML coverage report |

### **Code Quality Commands**

| Command | Description |
|---------|-------------|
| `flake8 src/` | Lint code (PEP 8) |
| `black src/` | Format code |
| `black --check src/` | Check formatting without changes |
| `isort src/` | Sort imports |
| `isort --check-only src/` | Check import sorting |
| `mypy src/` | Type checking |

### **Package Publishing**

| Command | Description |
|---------|-------------|
| `python -m build` | Build distribution packages |
| `twine check dist/*` | Validate packages |
| `twine upload --repository testpypi dist/*` | Upload to Test PyPI |
| `twine upload dist/*` | Upload to PyPI |
| `pip install fraud-detection-mlops` | Install from PyPI |

### **Jupyter Notebook**

| Command | Description |
|---------|-------------|
| `jupyter notebook` | Start Jupyter Notebook |
| `jupyter lab` | Start Jupyter Lab |
| `jupyter notebook --port 8888` | Start on specific port |

## 🔧 Configuration

### **Project Configuration (`src/config.py`)**

Key configuration parameters:

```python
# Data parameters
IMBALANCE_RATIO = 0.10  # 10% fraud rate
TEST_SIZE = 0.3         # 30% test split
RANDOM_STATE = 42       # Reproducibility seed

# Model parameters
MODEL_PARAMS = {
    'n_estimators': 200,
    'max_depth': 10,
    'min_samples_split': 10,
    'min_samples_leaf': 5,
    'class_weight': 'balanced',
    'random_state': 42
}

# MLflow configuration
MLFLOW_TRACKING_URI = "http://localhost:5000"
EXPERIMENT_NAME = "fraud_detection"
```

### **Docker Compose Services**

The `docker-compose.yml` defines three services:

1. **MLflow Server** (port 5000): Experiment tracking UI
2. **Jupyter Notebook** (port 8888): Interactive analysis
3. **App Service**: Main application container

## 📊 Model Performance

The fraud detection model achieves excellent results:

| Metric | Value | Description |
|--------|-------|-------------|
| **ROC-AUC** | 0.9999+ | Near-perfect discrimination |
| **Recall** | 99.5%+ | Fraud detection rate |
| **Precision** | 99.3%+ | Accuracy of fraud predictions |
| **F1-Score** | 99.5%+ | Harmonic mean of precision/recall |
| **False Positive Rate** | <0.1% | Very low false alarms |

**Confusion Matrix (typical run):**
- True Negatives: 2,698 (legitimate correctly identified)
- False Positives: 2 (legitimate flagged as fraud)
- False Negatives: 1 (fraud missed)
- True Positives: 299 (fraud correctly caught)

## 🏗️ Architecture Overview

### **Data Flow**

```
┌─────────────────┐
│ Data Generation │
│  (10K samples)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Preprocessing   │
│ - Encoding      │
│ - Scaling       │
│ - Train/Test    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Model Training  │
│ Random Forest   │
│ (200 trees)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Evaluation      │
│ - Metrics       │
│ - MLflow Log    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Model Saving    │
│ - Pickle        │
│ - DVC Track     │
└─────────────────┘
```

### **Technology Stack**

#### **Version Control**

- **Git**: Code versioning and collaboration
- **DVC**: Data and model versioning (stored in `.dvc/` folder)

#### **ML Pipeline**

- **ZenML**: Pipeline orchestration (configured in `.zen/` folder)
- **MLflow**: Experiment tracking and model registry
- **scikit-learn**: Machine learning library

#### **Deployment**

- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **GitHub Actions**: CI/CD automation

## 🎓 Usage Examples

### **Example 1: Train Model with Custom Parameters**

```python
from src.models.train import train_model
from src.data.data_loader import generate_fraud_data
from src.data.preprocessing import preprocess_data

# Generate data
df = generate_fraud_data(n_samples=20000, fraud_ratio=0.15)

# Preprocess
X_train, X_test, y_train, y_test, _, _ = preprocess_data(df)

# Train with custom parameters
custom_params = {
    'n_estimators': 300,
    'max_depth': 15,
    'class_weight': 'balanced'
}

model = train_model(X_train, y_train, params=custom_params)
```

### **Example 2: Load and Use Saved Model**

```python
import pickle
import numpy as np

# Load model
with open('models/fraud_detector.pkl', 'rb') as f:
    model = pickle.load(f)

# Make predictions
new_transaction = np.array([[100.50, 1, 15.5, 2, 1, 0, 45.2]])
prediction = model.predict(new_transaction)
probability = model.predict_proba(new_transaction)[0][1]

print(f"Fraud: {prediction[0]}")
print(f"Probability: {probability:.2%}")
```

### **Example 3: Run Multiple Experiments**

```python
from run_experiments import run_experiment

# Test different configurations
configs = [
    {'n_estimators': 100, 'max_depth': 5},
    {'n_estimators': 200, 'max_depth': 10},
    {'n_estimators': 300, 'max_depth': 15}
]

for config in configs:
    run_experiment(config, experiment_name="parameter_tuning")
```

## 🔄 CI/CD with GitHub Actions

The project includes automated workflows:

- **CI/CD Pipeline**: Run tests on every push/PR
- **Code Quality**: Linting and formatting checks
- **Run Pipeline**: Weekly automated fraud detection runs
- **Docker Publish**: Build and publish Docker images
- **PyPI Publish**: Publish package on releases
- **Release**: Automated changelog and release creation

See [GITHUB_ACTIONS.md](GITHUB_ACTIONS.md) for details.

## 📦 Publishing

### **To PyPI**

```bash
# Build package
python -m build

# Upload to PyPI
twine upload dist/*
```

### **To Docker Hub / GitHub Container Registry**

```bash
# Build image
docker build -t fraud-detection:v1.0.0 .

# Tag for registry
docker tag fraud-detection:v1.0.0 ghcr.io/username/fraud-detection:v1.0.0

# Push
docker push ghcr.io/username/fraud-detection:v1.0.0
```

## 🐛 Troubleshooting

### **Issue: MLflow UI Not Starting**

```bash
# Check if port 5000 is already in use
netstat -ano | findstr :5000  # Windows
lsof -i :5000                 # Linux/macOS

# Use different port
mlflow ui --port 5001
```

### **Issue: MLflow UI - OSError [WinError 10022] on Windows**

This is a known issue with uvicorn multiprocessing on Windows + Python 3.12.

**Solution: Use single worker mode**

```powershell
# Method 1: Use the provided script
.\start_mlflow.ps1

# Method 2: Manual command with --workers 1
mlflow ui --host 0.0.0.0 --port 5000 --workers 1

# Method 3: Use batch script
.\start_mlflow.bat
```

**Note:** The server will still start successfully despite initial error messages. Look for:
```
INFO:     Application startup complete.
INFO:     127.0.0.1 - "GET / HTTP/1.1" 200 OK
```

### **Issue: Import Errors**

```bash
# Ensure you're in the virtual environment
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### **Issue: Docker Container Won't Start**

```bash
# Check logs
docker-compose logs

# Rebuild containers
docker-compose down
docker-compose build --no-cache
docker-compose up
```

### **Issue: ZenML Authentication Errors**

Due to Python 3.12 compatibility issues with bcrypt/passlib, use the simplified runner:

```bash
python run_zenml_pipeline.py
```

This provides the same ZenML pipeline architecture without authentication issues.

## 📚 Additional Documentation

- **[QUICKSTART.md](QUICKSTART.md)**: Get started in 5 minutes
- **[GUIDE.md](GUIDE.md)**: Detailed usage guide
- **[ARCHITECTURE.md](ARCHITECTURE.md)**: System architecture details
- **[FRAUD_DETECTION.md](FRAUD_DETECTION.md)**: Fraud detection methodology
- **[GITHUB_ACTIONS.md](GITHUB_ACTIONS.md)**: CI/CD workflows
- **[PUBLISHING.md](PUBLISHING.md)**: Publishing to PyPI and registries
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Contribution guidelines

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **MLflow** for experiment tracking
- **ZenML** for pipeline orchestration
- **scikit-learn** for machine learning tools
- **Docker** for containerization
- **GitHub Actions** for CI/CD automation

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ for the MLOps community**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize DVC

```bash
dvc init
dvc remote add -d myremote /path/to/dvc/storage
```

### 5. Pull data

