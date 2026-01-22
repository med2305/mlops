# MLOps Project Setup Script for Windows PowerShell

Write-Host "Setting up MLOps project..." -ForegroundColor Green

# 1. Initialize Git repository
Write-Host "`n1. Initializing Git repository..." -ForegroundColor Cyan
if (Test-Path .git) {
    Write-Host "Git repository already exists." -ForegroundColor Yellow
} else {
    git init
    git add .
    git commit -m "Initial commit: MLOps project structure"
    Write-Host "Git repository initialized." -ForegroundColor Green
}

# 2. Initialize DVC
Write-Host "`n2. Initializing DVC..." -ForegroundColor Cyan
if (Test-Path .dvc) {
    Write-Host "DVC already initialized." -ForegroundColor Yellow
} else {
    dvc init
    
    # Add DVC remote (local storage for demonstration)
    $dvcStorage = Join-Path $PSScriptRoot "dvc_storage"
    New-Item -ItemType Directory -Force -Path $dvcStorage | Out-Null
    dvc remote add -d localstorage $dvcStorage
    
    # Track data and models directories with DVC
    dvc add data/raw
    dvc add data/processed
    dvc add models
    
    git add .dvc data\raw.dvc data\processed.dvc models.dvc .dvcignore
    git commit -m "Initialize DVC and track data/models"
    
    Write-Host "DVC initialized with local storage at $dvcStorage" -ForegroundColor Green
}

# 3. Create Python virtual environment
Write-Host "`n3. Creating Python virtual environment..." -ForegroundColor Cyan
if (Test-Path venv) {
    Write-Host "Virtual environment already exists." -ForegroundColor Yellow
} else {
    python -m venv venv
    Write-Host "Virtual environment created." -ForegroundColor Green
}

# 4. Install dependencies
Write-Host "`n4. Installing Python dependencies..." -ForegroundColor Cyan
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"
pip install --upgrade pip
pip install -r requirements.txt
Write-Host "Dependencies installed." -ForegroundColor Green

# 5. Initialize ZenML
Write-Host "`n5. Initializing ZenML..." -ForegroundColor Cyan
$env:ZENML_CONFIG_PATH = ".\.zen"
zenml init
Write-Host "ZenML initialized in .zen folder." -ForegroundColor Green

Write-Host "`n======================================" -ForegroundColor Green
Write-Host "Setup completed successfully!" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Green

Write-Host "`nNext steps:" -ForegroundColor Cyan
Write-Host "1. Activate virtual environment: .\venv\Scripts\Activate.ps1"
Write-Host "2. Start MLflow UI: mlflow ui --host 0.0.0.0 --port 5000"
Write-Host "3. Run pipeline: python src\pipelines\training_pipeline.py"
Write-Host "4. Or use Docker: docker-compose up --build"
