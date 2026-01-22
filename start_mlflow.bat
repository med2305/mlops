@echo off
REM Start MLflow UI - Windows Batch Script
REM Optimized for Windows + Python 3.12

echo.
echo ============================================================
echo  Starting MLflow UI (Windows Optimized)
echo ============================================================
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run: python -m venv .venv
    pause
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat
echo Virtual environment activated
echo.

echo Starting MLflow UI Server...
echo   - URL: http://localhost:5000
echo   - Workers: 1 (Windows optimized)
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start MLflow with single worker to avoid Windows multiprocessing issues
mlflow ui --host 0.0.0.0 --port 5000 --workers 1 --backend-store-uri file:./mlruns

echo.
echo MLflow UI stopped
pause
