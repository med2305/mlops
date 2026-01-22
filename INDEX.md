# 📚 MLOps Project Documentation Index

Welcome to your complete MLOps project! This index will help you navigate all documentation.

## 🚀 Getting Started

**Start here if you're new to this project:**

1. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Overview of what's included
2. **[QUICKSTART.md](QUICKSTART.md)** - Fast setup instructions
3. **[GUIDE.md](GUIDE.md)** - Complete usage guide with all commands

## 📖 Documentation Files

### Essential Reading

| File | Description | When to Read |
|------|-------------|--------------|
| **[README.md](README.md)** | Main project documentation | First time setup |
| **[GUIDE.md](GUIDE.md)** | Complete command reference | Daily usage |
| **[QUICKSTART.md](QUICKSTART.md)** | Quick setup guide | Initial setup |
| **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** | Project overview | Understanding scope |

### Advanced Topics

| File | Description | When to Read |
|------|-------------|--------------|
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | System design & diagrams | Understanding structure |

### Configuration Files

| File | Description | Purpose |
|------|-------------|---------|
| `requirements.txt` | Python dependencies | Package management |
| `docker-compose.yml` | Docker services | Container orchestration |
| `Dockerfile` | Container definition | Building images |
| `.gitignore` | Git ignore rules | Version control |
| `.dvcignore` | DVC ignore rules | Data versioning |
| `.env.example` | Environment template | Configuration |

### Scripts

| File | Description | Usage |
|------|-------------|-------|
| `setup.ps1` | Automated setup | Initial installation |
| `verify_installation.py` | Check installation | Verify setup |
| `run_experiments.py` | Multiple experiments | Hyperparameter tuning |

## 📂 Project Structure

```
mlops/
├── 📚 Documentation
│   ├── README.md              - Main documentation
│   ├── GUIDE.md               - Complete usage guide
│   ├── QUICKSTART.md          - Quick start
│   ├── PROJECT_SUMMARY.md     - Project overview
│   ├── ARCHITECTURE.md        - System design
│   └── INDEX.md               - This file
│
├── 🔧 Setup & Configuration
│   ├── setup.ps1              - Setup script
│   ├── requirements.txt       - Dependencies
│   ├── Dockerfile             - Docker image
│   ├── docker-compose.yml     - Services
│   └── .env.example           - Config template
│
├── 📝 Source Code
│   └── src/
│       ├── config.py          - Settings
│       ├── data/              - Data processing
│       ├── models/            - Model training
│       └── pipelines/         - ML pipelines
│
├── 💾 Data (DVC)
│   ├── data/raw/              - Raw data
│   └── data/processed/        - Processed data
│
├── 🤖 Models (DVC)
│   └── models/                - Trained models
│
└── 📓 Notebooks
    └── exploration.ipynb      - Data exploration
```

## 🎯 Quick Navigation

### I want to...

#### Setup the Project
→ Read: [QUICKSTART.md](QUICKSTART.md)  
→ Run: `.\setup.ps1`

#### Understand What's Included
→ Read: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

#### Run My First Experiment
→ Read: [GUIDE.md](GUIDE.md) - "Running the Project" section  
→ Run: `python src\pipelines\training_pipeline.py`

#### View Experiment Results
→ Read: [GUIDE.md](GUIDE.md) - "View Results" section  
→ Run: `mlflow ui --host 0.0.0.0 --port 5000`

#### Try Multiple Experiments
→ Run: `python run_experiments.py`

#### Use Docker
→ Read: [GUIDE.md](GUIDE.md) - "Method 3: Use Docker"  
→ Run: `docker-compose up --build`

#### Understand the Architecture
→ Read: [ARCHITECTURE.md](ARCHITECTURE.md)

#### Track Data with DVC
→ Read: [GUIDE.md](GUIDE.md) - "DVC Commands" section  
→ Run: `dvc add data\raw`

#### Troubleshoot Issues
→ Read: [GUIDE.md](GUIDE.md) - "Troubleshooting" section  
→ Run: `python verify_installation.py`

## 🔑 Key Concepts

### Git - Code Versioning
- Tracks all source code and configuration files
- Initialized and ready to use
- See: [GUIDE.md](GUIDE.md) - "Git Commands"

### DVC - Data & Model Versioning
- Tracks large data files and models
- Keeps your repository lightweight
- See: [GUIDE.md](GUIDE.md) - "DVC Commands"

### MLflow - Experiment Tracking
- Logs parameters, metrics, and artifacts
- Provides web UI for comparison
- See: [GUIDE.md](GUIDE.md) - "MLflow Commands"

### ZenML - Pipeline Orchestration
- Defines reproducible ML workflows
- Manages pipeline execution
- See: [src/pipelines/training_pipeline.py](src/pipelines/training_pipeline.py)

### Docker - Containerization
- Ensures consistent environments
- Simplifies deployment
- See: [docker-compose.yml](docker-compose.yml)

## 📊 Workflows

### Complete Workflow Examples

All workflows are detailed in [GUIDE.md](GUIDE.md) - "Typical Workflows" section:

1. **Run Experiment** - Train a model and track results
2. **Track Data Changes** - Version your datasets
3. **Save New Model** - Version trained models
4. **Deploy with Docker** - Run in containers

## 🛠️ Tools & Technologies

| Tool | Version | Documentation |
|------|---------|---------------|
| Python | 3.9+ | [python.org](https://python.org) |
| Git | Latest | [Git Docs](https://git-scm.com/doc) |
| DVC | 3.35.0 | [DVC Docs](https://dvc.org/doc) |
| MLflow | 2.9.2 | [MLflow Docs](https://mlflow.org/docs/latest/index.html) |
| ZenML | 0.55.0 | [ZenML Docs](https://docs.zenml.io/) |
| Docker | Latest | [Docker Docs](https://docs.docker.com/) |

## 🎓 Learning Path

### Beginner

1. Read [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
2. Run setup: `.\setup.ps1`
3. Verify: `python verify_installation.py`
4. Run first pipeline: `python src\pipelines\training_pipeline.py`
5. Explore notebook: `jupyter notebook notebooks\exploration.ipynb`

### Intermediate

1. Read [ARCHITECTURE.md](ARCHITECTURE.md)
2. Modify `src/config.py` parameters
3. Run multiple experiments: `python run_experiments.py`
4. Track data with DVC
5. View results in MLflow UI

### Advanced

1. Create custom pipeline steps
2. Configure remote DVC storage
3. Deploy with Docker Compose
4. Integrate with CI/CD
5. Add custom models

## 📝 File Purposes

### Documentation Files

- **INDEX.md** (this file) - Navigate documentation
- **README.md** - Main project overview
- **GUIDE.md** - Comprehensive command reference
- **QUICKSTART.md** - Fast setup instructions
- **PROJECT_SUMMARY.md** - What's included overview
- **ARCHITECTURE.md** - System design diagrams

### Python Scripts

- **src/pipelines/training_pipeline.py** - Main ZenML pipeline
- **src/models/train.py** - Model training utilities
- **src/data/data_loader.py** - Data loading
- **src/data/preprocessing.py** - Data preprocessing
- **src/config.py** - Configuration settings
- **run_experiments.py** - Multiple experiments example
- **verify_installation.py** - Installation checker

### Configuration

- **requirements.txt** - Python packages to install
- **docker-compose.yml** - Multi-service Docker setup
- **Dockerfile** - Docker image definition
- **.gitignore** - Files Git should ignore
- **.dvcignore** - Files DVC should ignore
- **.env.example** - Environment variables template

### Setup

- **setup.ps1** - Automated PowerShell setup script

## 🆘 Getting Help

### Having Issues?

1. Check [GUIDE.md](GUIDE.md) - "Troubleshooting" section
2. Run `python verify_installation.py`
3. Review error messages carefully
4. Check that virtual environment is activated

### Common Commands

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Verify installation
python verify_installation.py

# Check Git status
git status

# Check DVC status
dvc status

# Run pipeline
python src\pipelines\training_pipeline.py
```

## ✅ Checklist

Before starting work:
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] Git initialized
- [ ] DVC configured (after running setup)
- [ ] ZenML initialized (after running setup)

Ready to experiment:
- [ ] Run `python verify_installation.py` successfully
- [ ] MLflow UI accessible
- [ ] Pipeline runs without errors

## 🎯 Next Steps

**New User?**  
→ Start with [QUICKSTART.md](QUICKSTART.md)

**Ready to Code?**  
→ Read [GUIDE.md](GUIDE.md) and run your first pipeline

**Want to Understand Design?**  
→ Explore [ARCHITECTURE.md](ARCHITECTURE.md)

**Need Quick Reference?**  
→ Keep [GUIDE.md](GUIDE.md) open while working

---

**Happy ML Engineering! 🚀**

Last Updated: January 21, 2026
