# 🌐 How to Access ZenML Dashboard in Browser

## ⚠️ Important Note for Windows Users

Due to Python 3.12 compatibility issues with bcrypt/passlib and Windows limitations, the ZenML dashboard has some constraints:

1. **Daemon mode not supported** on Windows
2. **bcrypt authentication issues** with Python 3.12
3. **Server dependencies** require special installation

## 🔧 Solutions Available

### **Option 1: Use Docker (Recommended for Windows)**

This is the easiest and most reliable method on Windows:

```powershell
# Start ZenML server with Docker
cd C:\Users\Administrateur.Mohamed\OneDrive\Desktop\mlops
docker run -it -d -p 8080:8080 --name zenml zenmldocker/zenml-server
```

Then access the dashboard at: **http://localhost:8080**

**Default credentials:**
- Username: `default`
- Password: `(leave empty or use 'password')`

---

### **Option 2: Use ZenML Cloud (Free Tier)**

ZenML offers a free cloud dashboard:

1. **Create account** at: https://cloud.zenml.io
2. **Connect your local environment:**

```powershell
# Login to ZenML Cloud
.\.venv\Scripts\zenml.exe connect --url https://cloud.zenml.io
```

3. Access your dashboard online at: https://cloud.zenml.io

---

### **Option 3: Local Server in Blocking Mode (If dependencies installed)**

If server dependencies are installed successfully:

```powershell
# Start ZenML dashboard (keeps terminal open)
.\.venv\Scripts\zenml.exe up --blocking

# Or with specific port
.\.venv\Scripts\zenml.exe up --blocking --port 8080
```

Then access at: **http://localhost:8080**

**To stop:** Press `Ctrl+C` in the terminal

---

### **Option 4: Run with Docker Compose (Integrated)**

Use the existing Docker Compose setup:

```powershell
# Start all services including ZenML
docker-compose up -d

# Check if ZenML is configured in docker-compose.yml
```

---

## 🎯 Current Project Alternative: MLflow UI

Since our project is currently configured to work better with **MLflow** (which doesn't have the same compatibility issues), you can use MLflow for experiment tracking:

```powershell
# Start MLflow UI (already working)
mlflow ui --host 0.0.0.0 --port 5000
```

Access at: **http://localhost:5000**

**MLflow provides:**
- ✅ Experiment tracking
- ✅ Model registry
- ✅ Metrics visualization
- ✅ Parameter comparison
- ✅ Artifact storage
- ✅ Run comparison

---

## 📊 What You Can See in Each Dashboard

### **MLflow UI** (Port 5000)
- All pipeline runs and experiments
- Model performance metrics (ROC-AUC, Recall, Precision, F1)
- Hyperparameters used
- Confusion matrices
- Model artifacts
- Comparison between runs

### **ZenML Dashboard** (Port 8080 - if available)
- Pipeline visualization
- Step-by-step execution flow
- Artifact lineage
- Stack components
- Pipeline runs history

---

## 🚀 Quick Start: View Your Results

Since you just ran the pipeline successfully, view the results:

### **Method 1: MLflow UI (Easiest)**

```powershell
# Activate environment
.\.venv\Scripts\Activate.ps1

# Start MLflow
mlflow ui --port 5000
```

**Open browser:** http://localhost:5000

You'll see:
- Experiment: `fraud_detection`
- Latest run with 99.5%+ metrics
- All parameters and artifacts

### **Method 2: Check ZenML Status**

```powershell
# Check ZenML configuration
.\.venv\Scripts\zenml.exe status

# List pipeline runs
.\.venv\Scripts\zenml.exe pipeline runs list
```

---

## 🔍 Troubleshooting

### Issue: "Daemon functionality not supported on Windows"
**Solution:** Use `--blocking` flag or Docker

```powershell
.\.venv\Scripts\zenml.exe up --blocking
```

### Issue: "Missing module 'multipart'" or server dependencies
**Solution:** Install server extras (with admin permissions)

```powershell
# Close any running processes
# Run PowerShell as Administrator
pip install "zenml[server]==0.93.1" --force-reinstall
```

### Issue: bcrypt/passlib errors
**Solution:** This is a known Python 3.12 compatibility issue. Use Docker or MLflow instead.

### Issue: Port already in use
**Solution:** Use different port

```powershell
# Check what's using port 8080
netstat -ano | findstr :8080

# Use different port
.\.venv\Scripts\zenml.exe up --blocking --port 8888
```

---

## 📝 Recommended Workflow for This Project

Given the current setup and compatibility considerations:

### **For Development & Experimentation:**

```powershell
# 1. Run the pipeline
python run_zenml_pipeline.py

# 2. View results in MLflow
mlflow ui --port 5000

# 3. Open browser
# Go to: http://localhost:5000
```

### **For Production Deployment:**

Use Docker:

```yaml
# Add to docker-compose.yml
zenml:
  image: zenmldocker/zenml-server
  ports:
    - "8080:8080"
  environment:
    - ZENML_DEFAULT_PROJECT=fraud_detection
```

---

## 🌐 URLs Quick Reference

| Service | URL | Status |
|---------|-----|--------|
| **MLflow UI** | http://localhost:5000 | ✅ Working |
| **ZenML Dashboard** | http://localhost:8080 | ⚠️ Requires Docker |
| **ZenML Cloud** | https://cloud.zenml.io | ✅ Free tier available |
| **Jupyter Notebook** | http://localhost:8888 | ✅ Via Docker Compose |

---

## 💡 Recommendation

**For this project on Windows with Python 3.12:**

1. **Use MLflow UI** for experiment tracking (already working perfectly)
2. **Run pipelines** with `run_zenml_pipeline.py` (ZenML architecture without auth)
3. **If you need full ZenML dashboard**, use Docker option
4. **For cloud access**, sign up for ZenML Cloud (free)

**Current working setup:**
```powershell
# This is what's working now:
python run_zenml_pipeline.py  # ZenML-style pipeline
mlflow ui --port 5000          # View results
# Browser: http://localhost:5000
```

---

## 📚 Additional Resources

- **MLflow Documentation**: https://mlflow.org/docs/latest/index.html
- **ZenML Documentation**: https://docs.zenml.io/
- **ZenML Docker Guide**: https://docs.zenml.io/getting-started/deploying-zenml
- **Project README**: See [README.md](README.md) for all commands

---

**✨ Your pipeline results are already tracked and visible in MLflow UI!**

Just run: `mlflow ui --port 5000` and open http://localhost:5000 in your browser! 🚀
