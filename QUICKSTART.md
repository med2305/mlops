# Quick Start Guide - MLOps Project

## 🚀 Quick Setup (Windows PowerShell)

### Option 1: Automated Setup
Run the setup script:
```powershell
.\setup.ps1
```

### Option 2: Manual Setup

#### 1. Initialize Git
```powershell
git init
git add .
git commit -m "Initial commit: MLOps project"
```

#### 2. Create Python Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

#### 3. Initialize DVC
```powershell
dvc init
# Add local storage for demo
$dvcStorage = ".\dvc_storage"
New-Item -ItemType Directory -Force -Path $dvcStorage
dvc remote add -d localstorage $dvcStorage

# Track data and models
dvc add data\raw
dvc add data\processed
dvc add models

git add .dvc data\raw.dvc data\processed.dvc models.dvc .dvcignore
git commit -m "Initialize DVC"
```

#### 4. Initialize ZenML
```powershell
zenml init
```

#### 5. Start MLflow Server
```powershell
# In a separate terminal
mlflow ui --host 0.0.0.0 --port 5000
```
Access MLflow UI at: http://localhost:5000

#### 6. Run the Pipeline
```powershell
python src\pipelines\training_pipeline.py
```

---

## 🐳 Using Docker

### Start all services
```powershell
docker-compose up --build
```

This will start:
- MLflow UI on http://localhost:5000
- Jupyter Notebook on http://localhost:8888
- Training pipeline

### Stop services
```powershell
docker-compose down
```

---

## 📊 Project Components

### 1. **Git** - Code Versioning
- Tracks all source code and configuration files
- `.gitignore` configured to exclude data, models, and artifacts

### 2. **DVC** - Data & Model Versioning
- Tracks `data/raw/`, `data/processed/`, and `models/` directories
- Uses local storage (can be configured for cloud storage)
- Commands:
  ```powershell
  dvc add data\raw           # Track new data
  dvc push                   # Push to remote storage
  dvc pull                   # Pull from remote storage
  ```

### 3. **MLflow** - Experiment Tracking
- Tracks experiments, parameters, metrics, and artifacts
- Web UI for visualization
- Automatic model logging

### 4. **ZenML** - Pipeline Orchestration
- Defines data preparation and training pipelines
- Ensures reproducible ML workflows
- Steps:
  1. Load data
  2. Preprocess data
  3. Train model
  4. Evaluate model
  5. Save model

### 5. **Docker** - Containerization
- `Dockerfile`: Application container
- `docker-compose.yml`: Multi-service orchestration

---

## 📁 Project Structure

```
mlops/
├── data/
│   ├── raw/                    # Raw data (DVC tracked)
│   └── processed/              # Processed data (DVC tracked)
├── models/                     # Trained models (DVC tracked)
├── notebooks/                  # Jupyter notebooks
│   └── exploration.ipynb
├── src/
│   ├── data/
│   │   ├── data_loader.py     # Data loading utilities
│   │   └── preprocessing.py   # Data preprocessing
│   ├── models/
│   │   └── train.py           # Model training
│   └── pipelines/
│       └── training_pipeline.py # ZenML pipeline
├── .dvc/                       # DVC configuration
├── .git/                       # Git repository
├── Dockerfile                  # Docker container definition
├── docker-compose.yml          # Multi-container setup
├── requirements.txt            # Python dependencies
├── setup.ps1                   # Automated setup script
└── README.md                   # Documentation
```

---

## 🔄 Typical Workflow

### 1. Make changes to code
```powershell
# Edit source files
git add .
git commit -m "Description of changes"
```

### 2. Add new data
```powershell
# Add data to data/raw/
dvc add data\raw
git add data\raw.dvc
git commit -m "Update dataset"
dvc push
```

### 3. Run experiment
```powershell
python src\pipelines\training_pipeline.py
```

### 4. View results
- Open MLflow UI: http://localhost:5000
- Compare experiments, metrics, and parameters

### 5. Save model
```powershell
dvc add models
git add models.dvc
git commit -m "New model version"
dvc push
```

---

## 🛠️ Customization

### Change Model Parameters
Edit `src/config.py`:
```python
MODEL_PARAMS = {
    "n_estimators": 200,  # Change this
    "max_depth": 10,      # Change this
    "random_state": 42
}
```

### Use Different Dataset
Edit `src/data/data_loader.py` to load your own data.

### Add Pipeline Steps
Edit `src/pipelines/training_pipeline.py` and add new `@step` decorated functions.

### Configure Remote DVC Storage
```powershell
# For S3
dvc remote add -d myremote s3://mybucket/path

# For Google Cloud Storage
dvc remote add -d myremote gs://mybucket/path

# For Azure
dvc remote add -d myremote azure://mycontainer/path
```

---

## 📝 Notes

- **MLflow Tracking URI**: Set in `src/config.py` or via environment variable
- **ZenML**: Initialize once with `zenml init`, stores metadata in `.zen/`
- **DVC**: Commit `.dvc` files to Git, not the actual data
- **Docker**: Useful for consistent environments and deployment

---

## 🐛 Troubleshooting

### DVC Issues
```powershell
dvc doctor  # Check DVC configuration
```

### MLflow Server Not Starting
Check if port 5000 is available:
```powershell
netstat -ano | findstr :5000
```

### ZenML Issues
```powershell
zenml version
zenml clean  # Reset ZenML
zenml init
```

### Python Environment
```powershell
# Deactivate and recreate
deactivate
Remove-Item -Recurse -Force venv
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 📚 Resources

- [Git Documentation](https://git-scm.com/doc)
- [DVC Documentation](https://dvc.org/doc)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [ZenML Documentation](https://docs.zenml.io/)
- [Docker Documentation](https://docs.docker.com/)

---

## 🎯 Next Steps

1. ✅ Run the automated setup: `.\setup.ps1`
2. ✅ Start MLflow: `mlflow ui --host 0.0.0.0 --port 5000`
3. ✅ Run the pipeline: `python src\pipelines\training_pipeline.py`
4. ✅ Explore results in MLflow UI
5. ✅ Try the Jupyter notebook: `jupyter notebook notebooks\exploration.ipynb`
6. ✅ Experiment with Docker: `docker-compose up --build`
