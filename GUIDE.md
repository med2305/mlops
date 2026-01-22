# 🎯 MLOps Project - Complete Setup & Usage Guide

## ✨ What You Have

A complete MLOps project with:
- ✅ **Git** - Code versioning (initialized)
- ✅ **DVC** - Data/model versioning (configured)
- ✅ **Docker** - Containerization (ready to use)
- ✅ **MLflow** - Experiment tracking (integrated)
- ✅ **ZenML** - Pipeline orchestration (implemented)

## 📋 Prerequisites

Before starting, ensure you have:
- Python 3.9 or higher
- Git
- Docker Desktop (optional, for containerization)

## 🚀 Quick Start (Choose One)

### Option A: Automated Setup (Recommended)

```powershell
# Run the automated setup script
.\setup.ps1
```

### Option B: Manual Setup

```powershell
# 1. Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3. Initialize DVC
dvc init

# 4. Initialize ZenML
zenml init

# 5. Verify installation
python verify_installation.py
```

## 🎮 Running the Project

### Method 1: Run Single Pipeline

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run the training pipeline
python src\pipelines\training_pipeline.py
```

### Method 2: Run Multiple Experiments

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run multiple experiments with different parameters
python run_experiments.py
```

### Method 3: Use Docker

```powershell
# Start all services
docker-compose up --build

# Stop services
docker-compose down
```

## 📊 View Results

### MLflow UI

```powershell
# Start MLflow server (in a separate terminal)
mlflow ui --host 0.0.0.0 --port 5000

# Open browser to:
# http://localhost:5000
```

### Jupyter Notebook

```powershell
# Start Jupyter (in virtual environment)
jupyter notebook

# Or use Docker:
# Jupyter will be available at http://localhost:8888
```

## 🔧 Common Commands

### Git Commands

```powershell
# Check status
git status

# View commit history
git log --oneline

# Create a new branch
git checkout -b feature/new-feature

# Commit changes
git add .
git commit -m "Your message"
```

### DVC Commands

```powershell
# Track new data
dvc add data\raw\new_dataset.csv

# Track models
dvc add models\my_model.pkl

# Push to remote storage
dvc push

# Pull from remote storage
dvc pull

# Check DVC status
dvc status

# View DVC configuration
dvc config -l
```

### ZenML Commands

```powershell
# Check ZenML version
zenml version

# List pipelines
zenml pipeline list

# View pipeline runs
zenml pipeline runs list

# Clean ZenML (reset)
zenml clean
```

### Docker Commands

```powershell
# Build and start services
docker-compose up --build

# Start in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs

# View running containers
docker-compose ps
```

### MLflow Commands

```powershell
# Start UI
mlflow ui --host 0.0.0.0 --port 5000

# Start UI with specific backend
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlartifacts

# List experiments
mlflow experiments list
```

## 📁 File Structure Reference

```
mlops/
├── 📄 Documentation
│   ├── README.md              - Main documentation
│   ├── QUICKSTART.md          - Quick start guide
│   ├── PROJECT_SUMMARY.md     - Project overview
│   └── ARCHITECTURE.md        - Architecture diagrams
│
├── ⚙️ Configuration
│   ├── requirements.txt       - Python dependencies
│   ├── .gitignore            - Git ignore rules
│   ├── .dvcignore            - DVC ignore rules
│   ├── .env.example          - Environment variables template
│   ├── Dockerfile            - Docker container definition
│   └── docker-compose.yml    - Multi-service setup
│
├── 🔧 Scripts
│   ├── setup.ps1             - Automated setup
│   ├── verify_installation.py - Installation checker
│   └── run_experiments.py    - Multiple experiments example
│
├── 💾 Data (DVC tracked)
│   ├── data/raw/             - Raw datasets
│   └── data/processed/       - Processed datasets
│
├── 🤖 Models (DVC tracked)
│   └── models/               - Trained models
│
├── 📓 Notebooks
│   └── exploration.ipynb     - Data exploration
│
└── 📦 Source Code
    └── src/
        ├── config.py         - Configuration
        ├── data/             - Data utilities
        │   ├── data_loader.py
        │   └── preprocessing.py
        ├── models/           - Model utilities
        │   └── train.py
        └── pipelines/        - ZenML pipelines
            └── training_pipeline.py
```

## 🔄 Typical Workflows

### Workflow 1: Run Experiment

```powershell
# 1. Activate environment
.\venv\Scripts\Activate.ps1

# 2. (Optional) Modify parameters in src\config.py

# 3. Run pipeline
python src\pipelines\training_pipeline.py

# 4. View results in MLflow
# Start MLflow UI: mlflow ui --host 0.0.0.0 --port 5000
# Open: http://localhost:5000
```

### Workflow 2: Track Data Changes

```powershell
# 1. Add new data to data\raw\

# 2. Track with DVC
dvc add data\raw

# 3. Commit to Git
git add data\raw.dvc .gitignore
git commit -m "Update dataset"

# 4. Push DVC data
dvc push
```

### Workflow 3: Save New Model

```powershell
# 1. Train model (it saves automatically)
python src\pipelines\training_pipeline.py

# 2. Track with DVC
dvc add models

# 3. Commit to Git
git add models.dvc
git commit -m "New model version"

# 4. Push DVC data
dvc push
```

### Workflow 4: Deploy with Docker

```powershell
# 1. Build and start all services
docker-compose up --build

# 2. Services will be available at:
#    - MLflow UI: http://localhost:5000
#    - Jupyter: http://localhost:8888

# 3. Stop when done
docker-compose down
```

## 🐛 Troubleshooting

### Problem: Virtual environment activation fails

```powershell
# Set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate again
.\venv\Scripts\Activate.ps1
```

### Problem: Module not found

```powershell
# Ensure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Reinstall dependencies
pip install -r requirements.txt
```

### Problem: MLflow UI not starting

```powershell
# Check if port 5000 is in use
netstat -ano | findstr :5000

# Use a different port
mlflow ui --host 0.0.0.0 --port 5001
```

### Problem: Docker containers won't start

```powershell
# Check Docker is running
docker --version

# Remove old containers
docker-compose down
docker-compose up --build --force-recreate
```

### Problem: DVC issues

```powershell
# Check DVC configuration
dvc doctor

# Reinitialize DVC
dvc init --force
```

## 📚 Additional Resources

### Learn More
- [Git Documentation](https://git-scm.com/doc)
- [DVC Documentation](https://dvc.org/doc)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [ZenML Documentation](https://docs.zenml.io/)
- [Docker Documentation](https://docs.docker.com/)

### Example Commands

```powershell
# Check Python version
python --version

# Check installed packages
pip list

# Check Git status
git status

# Check DVC status
dvc status

# Check Docker version
docker --version

# Check running Docker containers
docker ps
```

## 🎯 Next Steps

1. ✅ **Setup**: Run `.\setup.ps1` or setup manually
2. ✅ **Verify**: Run `python verify_installation.py`
3. ✅ **Experiment**: Run `python src\pipelines\training_pipeline.py`
4. ✅ **Explore**: Open `notebooks\exploration.ipynb`
5. ✅ **Compare**: Try `python run_experiments.py`
6. ✅ **Deploy**: Use `docker-compose up --build`

## 💡 Tips

- Always activate virtual environment before running Python scripts
- Use MLflow UI to compare experiments
- Track data and models with DVC
- Commit code changes to Git regularly
- Use Docker for consistent environments
- Check `ARCHITECTURE.md` for system design

## 🎉 You're Ready!

Your MLOps project is fully set up and ready to use. Start with:

```powershell
.\venv\Scripts\Activate.ps1
python src\pipelines\training_pipeline.py
```

Then open MLflow UI to see your results:

```powershell
mlflow ui --host 0.0.0.0 --port 5000
```

Happy ML Engineering! 🚀
