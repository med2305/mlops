# 🗺️ Project Navigation Map

Quick navigation guide for the MLOps Fraud Detection project.

## 📖 Documentation Files

| File | Purpose | When to Use |
|------|---------|-------------|
| **[README.md](README.md)** | Complete project overview with all commands | First-time setup and reference |
| **[COMMANDS_CHEATSHEET.md](COMMANDS_CHEATSHEET.md)** | Quick command reference | Daily development work |
| **[QUICKSTART.md](QUICKSTART.md)** | Get started in 5 minutes | Quick start guide |
| **[GUIDE.md](GUIDE.md)** | Detailed usage guide | Deep dive into features |
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | System architecture | Understanding design |
| **[FRAUD_DETECTION.md](FRAUD_DETECTION.md)** | Fraud detection methodology | Understanding the ML model |
| **[GITHUB_ACTIONS.md](GITHUB_ACTIONS.md)** | CI/CD workflows documentation | Setting up automation |
| **[PUBLISHING.md](PUBLISHING.md)** | Publishing guide | Deploying to production |
| **[CONTRIBUTING.md](CONTRIBUTING.md)** | Contribution guidelines | Contributing to project |

## 🎯 I Want to...

### ...Get Started Quickly
1. Read [QUICKSTART.md](QUICKSTART.md)
2. Run: `python run_zenml_pipeline.py`
3. Run: `mlflow ui --port 5000`

### ...Understand the Project Structure
1. Read [README.md](README.md) - Project Structure section
2. Read [ARCHITECTURE.md](ARCHITECTURE.md)

### ...Run the Pipeline
1. **Simple way**: `python run_zenml_pipeline.py`
2. **MLflow only**: `python run_simple_fraud_detection.py`
3. **With experiments**: `python run_experiments.py`

See [COMMANDS_CHEATSHEET.md](COMMANDS_CHEATSHEET.md) for more options.

### ...View Experiment Results
1. Start MLflow UI: `mlflow ui --port 5000`
2. Open browser: <http://localhost:5000>
3. Navigate to "Experiments" → "fraud_detection"

### ...Modify the Model
1. Edit parameters in `src/config.py`
2. Or modify `src/models/train.py`
3. Run pipeline again
4. Compare results in MLflow UI

### ...Use Docker
1. Read [README.md](README.md) - Docker Commands section
2. Run: `docker-compose up`
3. Access services:
   - MLflow: <http://localhost:5000>
   - Jupyter: <http://localhost:8888>

### ...Set Up CI/CD
1. Read [GITHUB_ACTIONS.md](GITHUB_ACTIONS.md)
2. Configure GitHub secrets
3. Push to GitHub
4. Workflows run automatically

### ...Publish the Package
1. Read [PUBLISHING.md](PUBLISHING.md)
2. Build: `python -m build`
3. Publish: `twine upload dist/*`

### ...Contribute
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Create feature branch
3. Make changes
4. Submit pull request

### ...Debug Issues
1. Check [README.md](README.md) - Troubleshooting section
2. Use [COMMANDS_CHEATSHEET.md](COMMANDS_CHEATSHEET.md) - Troubleshooting Commands
3. Check logs: `docker-compose logs -f`

## 📂 Important Directories

| Directory | Contains | Purpose |
|-----------|----------|---------|
| `src/` | Source code | Core application logic |
| `src/data/` | Data processing | Data loading and preprocessing |
| `src/models/` | Model code | Training and evaluation |
| `src/pipelines/` | Pipeline definitions | ZenML pipeline orchestration |
| `data/raw/` | Raw data | Original transaction data |
| `data/processed/` | Processed data | Features ready for training |
| `models/` | Trained models | Saved model artifacts |
| `mlruns/` | MLflow experiments | Experiment tracking data |
| `notebooks/` | Jupyter notebooks | Exploratory analysis |
| `.github/workflows/` | CI/CD workflows | GitHub Actions automation |
| `.dvc/` | DVC configuration | Data version control |
| `.zen/` | ZenML configuration | Pipeline orchestration config |

## 🔑 Key Files

### Configuration Files

| File | Purpose |
|------|---------|
| `src/config.py` | Main configuration (model params, paths, etc.) |
| `requirements.txt` | Python dependencies |
| `setup.py` | Package configuration |
| `pyproject.toml` | Modern Python packaging |
| `docker-compose.yml` | Multi-container setup |
| `Dockerfile` | Container image definition |

### Pipeline Files

| File | Purpose |
|------|---------|
| `run_zenml_pipeline.py` | Main pipeline runner (recommended) |
| `run_simple_fraud_detection.py` | Simplified MLflow pipeline |
| `run_experiments.py` | Multiple experiment runner |
| `src/pipelines/training_pipeline.py` | ZenML pipeline definition |

### Data Files

| File | Purpose |
|------|---------|
| `src/data/data_loader.py` | Generate/load fraud data |
| `src/data/preprocessing.py` | Feature engineering |

### Model Files

| File | Purpose |
|------|---------|
| `src/models/train.py` | Model training and evaluation |
| `models/fraud_detector.pkl` | Saved trained model |

## 🔄 Typical Workflows

### Development Workflow

```
1. Edit code (src/) 
   ↓
2. Run pipeline (python run_zenml_pipeline.py)
   ↓
3. View results (mlflow ui)
   ↓
4. Test (pytest tests/)
   ↓
5. Format (black src/)
   ↓
6. Commit (git commit)
   ↓
7. Push (git push)
   ↓
8. CI/CD runs automatically
```

### Experiment Workflow

```
1. Modify parameters (src/config.py)
   ↓
2. Run experiment (python run_zenml_pipeline.py)
   ↓
3. Compare in MLflow UI
   ↓
4. Track with DVC (dvc add models/)
   ↓
5. Commit (git commit)
```

### Production Deployment

```
1. Finalize model
   ↓
2. Run tests (pytest tests/)
   ↓
3. Build Docker (docker build)
   ↓
4. Tag version (git tag v1.0.0)
   ↓
5. Push tag (git push origin v1.0.0)
   ↓
6. GitHub Actions deploys automatically
```

## 🚀 Quick Commands Reference

### Most Used Commands

```bash
# Activate environment (Windows)
.\.venv\Scripts\Activate.ps1

# Activate environment (Linux/macOS)
source .venv/bin/activate

# Run pipeline
python run_zenml_pipeline.py

# Start MLflow UI
mlflow ui --port 5000

# Run tests
pytest tests/ -v

# Format code
black src/

# Docker Compose
docker-compose up -d

# Git commit
git add . && git commit -m "message" && git push
```

## 📊 Performance Metrics

### Expected Results

After running the pipeline, you should see:

- **ROC-AUC**: ~0.9999 (near perfect)
- **Recall**: ~99.5% (fraud detection rate)
- **Precision**: ~99.3% (accuracy of predictions)
- **F1-Score**: ~99.5%
- **False Positive Rate**: <0.1%

View detailed results in MLflow UI at <http://localhost:5000>

## 🛠️ Tools & Technologies

### Core Tools

- **Python 3.12**: Programming language
- **Git**: Version control
- **Docker**: Containerization
- **MLflow**: Experiment tracking
- **ZenML**: Pipeline orchestration
- **DVC**: Data versioning

### Python Libraries

- **scikit-learn**: Machine learning
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **mlflow**: Experiment tracking

### Development Tools

- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Linting
- **mypy**: Type checking
- **isort**: Import sorting

## 🔗 Important Links

### Local Services (when running)

- MLflow UI: <http://localhost:5000>
- Jupyter Notebook: <http://localhost:8888>

### External Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [ZenML Documentation](https://docs.zenml.io/)
- [Docker Documentation](https://docs.docker.com/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)

## 📞 Need Help?

1. **Quick reference**: [COMMANDS_CHEATSHEET.md](COMMANDS_CHEATSHEET.md)
2. **Full documentation**: [README.md](README.md)
3. **Troubleshooting**: README.md - Troubleshooting section
4. **GitHub Issues**: Create an issue on GitHub

---

**Happy MLOps! 🚀**
