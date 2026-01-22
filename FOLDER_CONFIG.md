# Folder Configuration Reference

## MLOps Tool Directories

This project uses the following directory structure for MLOps tools:

### DVC - Data Version Control
- **Location**: `.dvc/`
- **Purpose**: DVC configuration and metadata
- **What it contains**:
  - DVC configuration files
  - Cache information
  - Remote storage settings
- **Version Control**: Tracked by Git
- **Note**: The actual data files are NOT in this folder, they're tracked via `.dvc` files

### ZenML - Pipeline Orchestration
- **Location**: `.zen/`
- **Purpose**: ZenML configuration and metadata
- **What it contains**:
  - ZenML stack configuration
  - Pipeline metadata
  - Artifact store information
- **Version Control**: Ignored by Git (see `.gitignore`)
- **Configuration**: Set via `ZENML_CONFIG_PATH` environment variable

### MLflow - Experiment Tracking
- **Location**: `mlruns/` and `mlartifacts/`
- **Purpose**: MLflow experiment data
- **What it contains**:
  - `mlruns/`: Experiment metadata, metrics, parameters
  - `mlartifacts/`: Model artifacts and files
- **Version Control**: Ignored by Git (see `.gitignore`)
- **Note**: Can be configured to use remote storage (S3, Azure, etc.)

### Git - Version Control
- **Location**: `.git/`
- **Purpose**: Git repository metadata
- **What it contains**:
  - Commit history
  - Branches
  - Remote configuration

## Environment Variables

### ZenML Configuration
Set the ZenML configuration path:

```powershell
# Windows PowerShell
$env:ZENML_CONFIG_PATH = ".\.zen"

# Or in .env file
ZENML_CONFIG_PATH=./.zen
```

### MLflow Configuration
Set the MLflow tracking URI:

```powershell
# Windows PowerShell
$env:MLFLOW_TRACKING_URI = "http://localhost:5000"

# Or in .env file
MLFLOW_TRACKING_URI=http://localhost:5000
```

## Docker Volume Mounts

The `docker-compose.yml` file mounts these folders into containers:

```yaml
volumes:
  - ./.dvc:/app/.dvc          # DVC configuration
  - ./.zen:/app/.zen          # ZenML configuration
  - ./mlruns:/app/mlruns      # MLflow experiments
  - ./data:/app/data          # Data files
  - ./models:/app/models      # Trained models
  - ./src:/app/src            # Source code
```

## Initialization Commands

### Initialize DVC
```powershell
# DVC automatically creates .dvc/ folder
dvc init
```

### Initialize ZenML
```powershell
# Set environment variable to use .zen folder
$env:ZENML_CONFIG_PATH = ".\.zen"
zenml init
```

### Initialize Git
```powershell
# Git automatically creates .git/ folder
git init
```

## .gitignore Configuration

The following folders are configured in `.gitignore`:

```gitignore
# DVC - Configuration is tracked, data is not
/data/raw/*
/data/processed/*
/models/*

# ZenML - Configuration is ignored (local only)
.zen/
zenml_local_store/

# MLflow - Experiments are ignored (local only)
mlruns/
mlartifacts/

# Git - This is never ignored (it's Git itself!)
# .git/ is automatically handled by Git
```

## Folder Structure Overview

```
mlops/
├── .dvc/                   # DVC configuration (Git tracked)
├── .zen/                   # ZenML configuration (Git ignored)
├── .git/                   # Git repository (Git managed)
├── mlruns/                 # MLflow experiments (Git ignored)
├── mlartifacts/            # MLflow artifacts (Git ignored)
├── data/
│   ├── raw/               # Raw data (DVC tracked, Git ignored)
│   └── processed/         # Processed data (DVC tracked, Git ignored)
├── models/                # Trained models (DVC tracked, Git ignored)
├── src/                   # Source code (Git tracked)
├── notebooks/             # Jupyter notebooks (Git tracked)
└── ...
```

## Why This Configuration?

### DVC in `.dvc/`
- ✅ Standard DVC convention
- ✅ Automatically created by `dvc init`
- ✅ Configuration tracked by Git for team collaboration
- ✅ Actual data files kept separate and tracked via `.dvc` metadata files

### ZenML in `.zen/`
- ✅ Clean, short folder name
- ✅ Keeps local configuration separate
- ✅ Allows different team members to have different local setups
- ✅ Can be shared via Docker volumes for container consistency

### MLflow in `mlruns/` and `mlartifacts/`
- ✅ Standard MLflow convention
- ✅ Can be easily configured for remote storage
- ✅ Keeps experiment data separate from code

## Sharing & Collaboration

### What to commit to Git
- ✅ `.dvc/` folder (DVC configuration)
- ✅ `*.dvc` files (data tracking metadata)
- ✅ `.dvcignore`
- ✅ All source code
- ✅ `requirements.txt`
- ✅ `docker-compose.yml`
- ✅ Documentation

### What NOT to commit to Git
- ❌ `.zen/` folder (local ZenML config)
- ❌ `mlruns/` and `mlartifacts/` (MLflow data)
- ❌ Actual data files in `data/`
- ❌ Actual model files in `models/`
- ❌ `venv/` (virtual environment)

### What to share via DVC
- ✅ Data files in `data/raw/` and `data/processed/`
- ✅ Model files in `models/`
- ✅ Use `dvc push` to share
- ✅ Use `dvc pull` to retrieve

## Quick Commands Reference

```powershell
# Setup with correct folders
.\setup.ps1

# Or manually set ZenML path
$env:ZENML_CONFIG_PATH = ".\.zen"
zenml init

# Check DVC configuration
dvc config -l

# Check ZenML configuration
zenml status

# Push data to DVC remote
dvc push

# Pull data from DVC remote
dvc pull

# View MLflow experiments
mlflow ui --host 0.0.0.0 --port 5000
```

## Notes

- The `.dvc/` folder is created automatically when you run `dvc init`
- The `.zen/` folder is created when you run `zenml init` with `ZENML_CONFIG_PATH` set
- Both folders work seamlessly with Docker containers via volume mounts
- This configuration ensures clean separation of concerns and proper version control
