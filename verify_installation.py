"""
Verify MLOps Project Installation
This script checks if all required components are properly installed.
"""

import sys
import subprocess

def check_command(command, name):
    """Check if a command is available."""
    try:
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            shell=True
        )
        print(f"✅ {name} is installed")
        return True
    except Exception as e:
        print(f"❌ {name} is NOT installed")
        return False

def check_python_package(package, name):
    """Check if a Python package is installed."""
    try:
        __import__(package)
        print(f"✅ {name} is installed")
        return True
    except ImportError:
        print(f"❌ {name} is NOT installed")
        return False

def main():
    print("=" * 50)
    print("MLOps Project Installation Verification")
    print("=" * 50)
    print()
    
    # Check system commands
    print("Checking system commands...")
    print("-" * 50)
    git_ok = check_command("git --version", "Git")
    docker_ok = check_command("docker --version", "Docker")
    
    print()
    print("Checking Python packages...")
    print("-" * 50)
    
    # Check Python packages
    packages = [
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("sklearn", "scikit-learn"),
        ("mlflow", "MLflow"),
        ("zenml", "ZenML"),
        ("dvc", "DVC"),
        ("matplotlib", "Matplotlib"),
        ("seaborn", "Seaborn"),
        ("jupyter", "Jupyter")
    ]
    
    package_results = []
    for package, name in packages:
        result = check_python_package(package, name)
        package_results.append(result)
    
    print()
    print("=" * 50)
    print("Summary")
    print("=" * 50)
    
    all_ok = git_ok and all(package_results)
    docker_optional = docker_ok
    
    if all_ok:
        print("✅ All required components are installed!")
        print()
        print("You can now:")
        print("1. Run the pipeline: python src\\pipelines\\training_pipeline.py")
        print("2. Start MLflow UI: mlflow ui --host 0.0.0.0 --port 5000")
        print("3. Explore data: jupyter notebook notebooks\\exploration.ipynb")
    else:
        print("❌ Some components are missing.")
        print()
        print("Please install missing components:")
        print("1. Activate virtual environment: .\\venv\\Scripts\\Activate.ps1")
        print("2. Install dependencies: pip install -r requirements.txt")
    
    if not docker_optional:
        print()
        print("⚠️  Docker is not installed (optional for development)")
        print("   Install Docker to use: docker-compose up --build")
    
    print()
    print("=" * 50)

if __name__ == "__main__":
    main()
