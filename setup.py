"""Setup configuration for fraud-detection-mlops package."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="fraud-detection-mlops",
    version="1.0.0",
    author="Mohamed Administrateur",
    author_email="your.email@example.com",
    description="Complete MLOps pipeline for fraud detection using Random Forest, MLflow, DVC, and ZenML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/fraud-detection-mlops",
    project_urls={
        "Bug Tracker": "https://github.com/YOUR_USERNAME/fraud-detection-mlops/issues",
        "Documentation": "https://github.com/YOUR_USERNAME/fraud-detection-mlops#readme",
        "Source Code": "https://github.com/YOUR_USERNAME/fraud-detection-mlops",
    },
    packages=find_packages(exclude=["tests", "tests.*", "docs", ".github"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.26.0",
        "pandas>=2.0.0",
        "scikit-learn>=1.3.0",
        "mlflow>=2.9.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0",
        "joblib>=1.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "flake8>=6.1.0",
            "black>=23.7.0",
            "isort>=5.12.0",
            "mypy>=1.5.0",
        ],
        "zenml": [
            "zenml>=0.55.0",
            "sqlalchemy-utils>=0.41.0",
            "sqlmodel>=0.0.8",
        ],
        "dvc": [
            "dvc>=3.0.0",
        ],
        "notebook": [
            "jupyter>=1.0.0",
            "notebook>=7.0.0",
        ],
        "all": [
            "zenml>=0.55.0",
            "dvc>=3.0.0",
            "jupyter>=1.0.0",
            "notebook>=7.0.0",
            "sqlalchemy-utils>=0.41.0",
            "sqlmodel>=0.0.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "fraud-detection=run_simple_fraud_detection:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yml", "*.yaml", "*.md", "*.txt"],
    },
    keywords=[
        "mlops",
        "fraud-detection",
        "machine-learning",
        "mlflow",
        "dvc",
        "zenml",
        "random-forest",
        "scikit-learn",
        "docker",
        "ci-cd",
    ],
    zip_safe=False,
)
