# Contributing to Fraud Detection MLOps Project

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🚀 Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/mlops.git
   cd mlops
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🔄 Development Workflow

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following our coding standards

3. Run tests:
   ```bash
   python run_simple_fraud_detection.py
   ```

4. Format your code:
   ```bash
   black src/
   isort src/
   ```

5. Commit your changes:
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

6. Push and create a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

## 📝 Commit Message Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

## 🧪 Testing

- Ensure the fraud detection pipeline runs successfully
- Check that model metrics are within acceptable ranges (ROC-AUC > 0.95)
- Verify all code changes are properly tested

## 📋 Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and modular

## 🐛 Reporting Bugs

Create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version)

## 💡 Suggesting Features

Create an issue with:
- Clear description of the feature
- Use case and benefits
- Possible implementation approach

## 📄 License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

## 🤝 Code of Conduct

Be respectful, inclusive, and professional in all interactions.
