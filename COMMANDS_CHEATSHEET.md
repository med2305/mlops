# 🚀 MLOps Fraud Detection - Commands Cheat Sheet

Quick reference for all available commands in this project.

## ⚡ Quick Commands

```powershell
# Complete workflow - Run everything
.\.venv\Scripts\Activate.ps1           # Activate environment
python run_zenml_pipeline.py            # Run pipeline
mlflow ui --port 5000                   # View results
```

---

## 📦 Environment Setup

### Create Virtual Environment

**Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
# Install all dependencies
pip install -r requirements.txt

# Install specific extras
pip install -e ".[dev]"      # Development tools
pip install -e ".[zenml]"    # ZenML pipeline
pip install -e ".[dvc]"      # DVC data versioning
pip install -e ".[all]"      # Everything

# Verify installation
python verify_installation.py
```

---

## 🔄 Pipeline Execution

### Run Pipelines

```bash
# ZenML-style pipeline (recommended)
python run_zenml_pipeline.py

# Simple MLflow pipeline
python run_simple_fraud_detection.py

# Multiple experiments
python run_experiments.py

# Direct ZenML pipeline (may have auth issues on Python 3.12)
python src/pipelines/training_pipeline.py
```

### Pipeline with Custom Parameters

```python
# Edit src/config.py or pass parameters
MODEL_PARAMS = {
    'n_estimators': 300,
    'max_depth': 15,
    'min_samples_split': 5
}
```

---

## 📊 MLflow Commands

### Start MLflow UI

```bash
# Default (port 5000)
mlflow ui

# Custom port
mlflow ui --port 5001

# Allow network access
mlflow ui --host 0.0.0.0 --port 5000

# Specify backend
mlflow ui --backend-store-uri file:./mlruns
```

### MLflow Experiments

```bash
# List all experiments
mlflow experiments list

# Create new experiment
mlflow experiments create --experiment-name "new_experiment"

# List runs in experiment
mlflow runs list --experiment-id 0

# Get run details
mlflow runs describe --run-id <RUN_ID>
```

### MLflow Models

```bash
# Serve model
mlflow models serve -m models:/fraud_detector/production -p 5001

# Serve from local path
mlflow models serve -m ./models/fraud_detector.pkl -p 5001

# Test model endpoint
curl -X POST http://localhost:5001/invocations \
  -H 'Content-Type: application/json' \
  -d '{"dataframe_split": {"data": [[100.50, 1, 15.5, 2, 1, 0, 45.2]]}}'
```

---

## 🐳 Docker Commands

### Docker Compose

```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f mlflow

# List running containers
docker-compose ps

# Rebuild images
docker-compose build

# Rebuild without cache
docker-compose build --no-cache
```

### Individual Docker Commands

```bash
# Build image
docker build -t fraud-detection:latest .

# Run container
docker run -p 5000:5000 fraud-detection:latest

# Run with volume mount
docker run -p 5000:5000 -v $(pwd)/data:/app/data fraud-detection:latest

# List containers
docker ps

# Stop container
docker stop <CONTAINER_ID>

# Remove container
docker rm <CONTAINER_ID>

# Remove image
docker rmi fraud-detection:latest
```

---

## 📂 DVC Commands

### Initialize and Track

```bash
# Initialize DVC
dvc init

# Track data file
dvc add data/raw/fraud_transactions.csv

# Track model
dvc add models/fraud_detector.pkl

# Track directory
dvc add data/processed/
```

### Remote Storage

```bash
# Add remote storage
dvc remote add -d myremote s3://mybucket/dvcstore

# Push to remote
dvc push

# Pull from remote
dvc pull

# Check status
dvc status
```

### Pipeline Reproduction

```bash
# Reproduce pipeline
dvc repro

# Force reproduce
dvc repro --force

# Show pipeline graph
dvc dag
```

---

## 🔧 Git Commands

### Basic Git

```bash
# Check status
git status

# Stage files
git add .
git add README.md

# Commit
git commit -m "Add new feature"

# Push to GitHub
git push origin main

# Pull changes
git pull origin main
```

### Branching

```bash
# Create branch
git checkout -b feature/new-feature

# Switch branch
git checkout main

# Merge branch
git merge feature/new-feature

# Delete branch
git branch -d feature/new-feature
```

### Tagging (for Releases)

```bash
# Create tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag
git push origin v1.0.0

# List tags
git tag -l

# Delete tag
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## 🧪 Testing Commands

### Run Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_model.py

# Run specific test
pytest tests/test_model.py::test_train_model

# Run with coverage
pytest tests/ --cov=src

# Generate HTML coverage report
pytest tests/ --cov=src --cov-report=html

# Open coverage report
start htmlcov/index.html  # Windows
open htmlcov/index.html   # macOS
```

---

## ✨ Code Quality

### Linting

```bash
# Lint with flake8
flake8 src/

# Lint specific file
flake8 src/models/train.py

# Lint with config
flake8 src/ --config=.flake8
```

### Formatting

```bash
# Format with black
black src/

# Check formatting (no changes)
black --check src/

# Format specific file
black src/models/train.py

# Set line length
black src/ --line-length 100
```

### Import Sorting

```bash
# Sort imports
isort src/

# Check only
isort --check-only src/

# Sort with profile
isort src/ --profile black
```

### Type Checking

```bash
# Type check with mypy
mypy src/

# Type check specific file
mypy src/models/train.py

# Ignore missing imports
mypy src/ --ignore-missing-imports
```

---

## 📦 Package Management

### Build Package

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Check built packages
ls dist/
```

### Publish Package

```bash
# Check package
twine check dist/*

# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*

# Install from PyPI
pip install fraud-detection-mlops
```

---

## 📓 Jupyter Notebook

### Start Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook

# Start Jupyter Lab
jupyter lab

# Start on specific port
jupyter notebook --port 8888

# Allow network access
jupyter notebook --ip 0.0.0.0
```

### Notebook Operations

```bash
# Convert notebook to Python
jupyter nbconvert --to python notebook.ipynb

# Convert to HTML
jupyter nbconvert --to html notebook.ipynb

# Execute notebook
jupyter nbconvert --execute --to notebook notebook.ipynb
```

---

## 🔍 Debugging & Monitoring

### Check Processes

**Windows:**
```powershell
# Check port usage
netstat -ano | findstr :5000

# Kill process by PID
taskkill /PID <PID> /F
```

**Linux/macOS:**
```bash
# Check port usage
lsof -i :5000

# Kill process by PID
kill -9 <PID>
```

### View Logs

```bash
# Python logging
tail -f logs/app.log

# Docker logs
docker-compose logs -f

# Specific service
docker-compose logs -f mlflow
```

### System Info

```bash
# Python version
python --version

# Installed packages
pip list

# Package info
pip show mlflow

# Environment info
python -c "import sys; print(sys.executable)"
python -c "import mlflow; print(mlflow.__version__)"
```

---

## 🚨 Troubleshooting Commands

### Reset Environment

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment
rm -rf .venv  # Linux/macOS
rmdir /s .venv  # Windows

# Recreate environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Clear Cache

```bash
# Clear Python cache
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Clear MLflow cache
rm -rf mlruns/

# Clear DVC cache
dvc cache clear
```

### Reinstall Dependencies

```bash
# Reinstall all packages
pip install -r requirements.txt --force-reinstall

# Upgrade all packages
pip install -r requirements.txt --upgrade
```

---

## 📋 Common Workflows

### Complete Development Cycle

```powershell
# 1. Activate environment
.\.venv\Scripts\Activate.ps1

# 2. Run pipeline
python run_zenml_pipeline.py

# 3. View results
mlflow ui --port 5000

# 4. Run tests
pytest tests/ -v

# 5. Check code quality
black src/
flake8 src/
mypy src/

# 6. Commit changes
git add .
git commit -m "Improve model performance"
git push origin main
```

### Deploy to Production

```bash
# 1. Run tests
pytest tests/ --cov=src

# 2. Build Docker image
docker build -t fraud-detection:v1.0.0 .

# 3. Tag for registry
docker tag fraud-detection:v1.0.0 ghcr.io/username/fraud-detection:v1.0.0

# 4. Push to registry
docker push ghcr.io/username/fraud-detection:v1.0.0

# 5. Create release tag
git tag -a v1.0.0 -m "Production release v1.0.0"
git push origin v1.0.0
```

### Experiment Iteration

```bash
# 1. Modify parameters in src/config.py
# 2. Run experiment
python run_zenml_pipeline.py

# 3. View in MLflow
mlflow ui

# 4. Track with DVC
dvc add models/fraud_detector.pkl
git add models/fraud_detector.pkl.dvc
git commit -m "Update model with new parameters"
```

---

## 🎯 Performance Optimization

### Profile Code

```bash
# Profile Python code
python -m cProfile -o profile.stats run_zenml_pipeline.py

# Analyze profile
python -m pstats profile.stats
```

### Monitor Resources

**Windows:**
```powershell
# Task Manager
taskmgr

# PowerShell monitoring
Get-Process python | Format-Table -Property ProcessName, CPU, WorkingSet
```

**Linux/macOS:**
```bash
# Monitor CPU/Memory
htop

# Python specific
ps aux | grep python
```

---

## 📖 Help & Documentation

```bash
# Python help
python --help

# MLflow help
mlflow --help
mlflow ui --help

# DVC help
dvc --help
dvc add --help

# Pytest help
pytest --help

# Package help
pip help install
```

---

## 🔗 Useful URLs (when services are running)

- **MLflow UI**: <http://localhost:5000>
- **Jupyter Notebook**: <http://localhost:8888>
- **Docker MLflow**: <http://localhost:5000> (via Docker Compose)

---

**💡 Tip**: Bookmark this file for quick reference!

**📚 For detailed explanations, see [README.md](README.md)**
