# Start MLflow UI - Windows Optimized
# This script starts MLflow with settings optimized for Windows + Python 3.12

Write-Host "🚀 Starting MLflow UI (Windows Optimized)..." -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment
if (Test-Path ".\.venv\Scripts\Activate.ps1") {
    & .\.venv\Scripts\Activate.ps1
    Write-Host "✅ Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "❌ Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run: python -m venv .venv" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "📊 Starting MLflow UI Server..." -ForegroundColor Cyan
Write-Host "   - URL: http://localhost:5000" -ForegroundColor White
Write-Host "   - Workers: 1 (Windows optimized)" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Start MLflow with single worker (avoids Windows multiprocessing issues)
& .\.venv\Scripts\mlflow.exe ui `
    --host 0.0.0.0 `
    --port 5000 `
    --workers 1 `
    --backend-store-uri file:./mlruns

Write-Host ""
Write-Host "MLflow UI stopped" -ForegroundColor Yellow
