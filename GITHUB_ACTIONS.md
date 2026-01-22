# GitHub Actions Workflows Summary

This document provides an overview of all GitHub Actions workflows configured for the Fraud Detection MLOps project.

## 📋 Workflow Overview

| Workflow | File | Triggers | Purpose |
|----------|------|----------|---------|
| CI/CD Pipeline | `ci.yml` | Push, PR | Run tests and quality checks |
| Code Quality | `code-quality.yml` | Push, PR | Linting and formatting |
| Deploy | `deploy.yml` | Tags | Deploy to production |
| Run Pipeline | `run-pipeline.yml` | Manual, Schedule | Execute fraud detection |
| Docker Publish | `docker-publish.yml` | Push, Release | Build and publish Docker images |
| PyPI Publish | `publish-pypi.yml` | Release | Publish Python package |
| Release | `release.yml` | Version tags | Create GitHub releases |

## 🔄 Detailed Workflow Descriptions

### 1. CI/CD Pipeline (`ci.yml`)

**Purpose**: Continuous integration and testing

**Triggers**:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop`

**Jobs**:
- **Test**: 
  - Matrix testing on Python 3.9, 3.10, 3.11, 3.12
  - Tests on Ubuntu and Windows
  - Code coverage reporting
  - Upload to Codecov

**Key Features**:
- Multi-platform testing
- Comprehensive coverage reporting
- Automatic artifact uploads

---

### 2. Code Quality (`code-quality.yml`)

**Purpose**: Enforce code quality standards

**Triggers**:
- Push to any branch
- Pull requests

**Jobs**:
- **Lint**: Flake8 linting
- **Format**: Black formatting check
- **Sort**: isort import sorting
- **Type Check**: MyPy type checking

**Key Features**:
- PEP 8 compliance
- Consistent code formatting
- Import organization

---

### 3. Deploy (`deploy.yml`)

**Purpose**: Automated deployment

**Triggers**:
- Push to `main` with version tags
- Manual workflow dispatch

**Jobs**:
- Build and test
- Deploy to staging
- Deploy to production
- Health checks

**Key Features**:
- Staging environment testing
- Blue-green deployment support
- Rollback capabilities

---

### 4. Run Fraud Detection Pipeline (`run-pipeline.yml`)

**Purpose**: Automated pipeline execution

**Triggers**:
- Manual workflow dispatch
- Weekly schedule (Sunday 00:00 UTC)

**Jobs**:
- Install dependencies
- Execute pipeline
- Generate reports
- Upload artifacts

**Key Features**:
- Scheduled fraud detection runs
- Artifact retention (30 days)
- Performance reporting

**Artifacts**:
- Trained models (`models/`)
- MLflow tracking data (`mlruns/`)
- Performance reports

---

### 5. Docker Image Publishing (`docker-publish.yml`)

**Purpose**: Build and publish Docker images

**Triggers**:
- Push to `main` branch
- Version tags (`v*`)
- Release published
- Manual dispatch

**Jobs**:
- **Build and Push**:
  - Build multi-platform images
  - Push to GitHub Container Registry (ghcr.io)
  - Tag with version and SHA
  - Cache optimization

- **Security Scan**:
  - Trivy vulnerability scanning
  - Upload results to GitHub Security

**Published Images**:
- `ghcr.io/YOUR_USERNAME/fraud-detection-mlops:latest`
- `ghcr.io/YOUR_USERNAME/fraud-detection-mlops:v1.0.0`
- `ghcr.io/YOUR_USERNAME/fraud-detection-mlops-mlflow:latest`

**Key Features**:
- Automated security scanning
- Multi-architecture support
- Layer caching for faster builds

---

### 6. PyPI Package Publishing (`publish-pypi.yml`)

**Purpose**: Publish Python package to PyPI

**Triggers**:
- Release published
- Manual dispatch (with Test PyPI option)

**Jobs**:
- Build Python package
- Validate with Twine
- Publish to Test PyPI (manual)
- Publish to PyPI (release)

**Key Features**:
- Test PyPI testing before production
- Package validation
- Automatic on release

**Requirements**:
- PyPI API token in secrets (`PYPI_API_TOKEN`)
- Test PyPI token (`TEST_PYPI_API_TOKEN`)

---

### 7. Automated Release Creation (`release.yml`)

**Purpose**: Create GitHub releases automatically

**Triggers**:
- Version tags matching `v*.*.*` pattern

**Jobs**:
- Generate changelog from commits
- Create GitHub release
- Attach installation instructions
- Mark pre-releases (alpha, beta, rc)

**Release Notes Include**:
- Changelog with commits since last tag
- Installation instructions (pip, Docker)
- Links to full changelog
- Automatic release note generation

**Key Features**:
- Semantic versioning support
- Pre-release detection
- Comprehensive release notes

---

## 🚀 Usage Examples

### Running CI Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov flake8 black isort

# Run tests
pytest tests/ -v --cov=src

# Check linting
flake8 src/

# Check formatting
black --check src/
isort --check-only src/
```

### Manual Pipeline Execution

1. Go to **Actions** tab on GitHub
2. Select "Run Fraud Detection Pipeline"
3. Click "Run workflow"
4. Select branch
5. Click "Run workflow" button

### Creating a Release

```bash
# Update version in setup.py and pyproject.toml
# Commit changes
git add setup.py pyproject.toml
git commit -m "Bump version to 1.0.0"

# Create and push tag
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# GitHub Actions will automatically:
# - Run all tests
# - Create GitHub release
# - Publish to PyPI
# - Build and push Docker images
```

### Publishing to PyPI Manually

```bash
# Build package
python -m build

# Test upload to Test PyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

### Building Docker Images

```bash
# Build locally
docker build -t fraud-detection:local .

# Build with compose
docker-compose build

# Push to registry (after GitHub Actions builds)
docker pull ghcr.io/YOUR_USERNAME/fraud-detection-mlops:latest
```

## 🔒 Required Secrets

Configure these secrets in **Settings** → **Secrets and variables** → **Actions**:

| Secret | Purpose | Required For |
|--------|---------|--------------|
| `PYPI_API_TOKEN` | PyPI publishing | `publish-pypi.yml` |
| `TEST_PYPI_API_TOKEN` | Test PyPI | `publish-pypi.yml` |
| `CODECOV_TOKEN` | Coverage reports | `ci.yml` (optional) |
| `GITHUB_TOKEN` | Auto-generated | All workflows |

## 📊 Status Badges

Add these to your README.md:

```markdown
[![CI/CD](https://github.com/YOUR_USERNAME/fraud-detection-mlops/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/fraud-detection-mlops/actions/workflows/ci.yml)

[![Code Quality](https://github.com/YOUR_USERNAME/fraud-detection-mlops/actions/workflows/code-quality.yml/badge.svg)](https://github.com/YOUR_USERNAME/fraud-detection-mlops/actions/workflows/code-quality.yml)

[![Docker](https://github.com/YOUR_USERNAME/fraud-detection-mlops/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/YOUR_USERNAME/fraud-detection-mlops/actions/workflows/docker-publish.yml)

[![PyPI version](https://badge.fury.io/py/fraud-detection-mlops.svg)](https://badge.fury.io/py/fraud-detection-mlops)
```

## 🛠️ Workflow Customization

### Modify Test Matrix

Edit `.github/workflows/ci.yml`:

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]  # Add macOS
    python-version: ['3.9', '3.10', '3.11', '3.12']
```

### Change Schedule

Edit `.github/workflows/run-pipeline.yml`:

```yaml
schedule:
  - cron: '0 0 * * 0'  # Weekly on Sunday
  - cron: '0 0 * * 1'  # Add Monday
```

### Add Deployment Environments

Edit `.github/workflows/deploy.yml`:

```yaml
environment:
  name: production
  url: https://your-app.com
```

## 📝 Best Practices

1. **Branch Protection**: Enable branch protection for `main`
2. **Required Checks**: Make CI tests required before merging
3. **Code Review**: Require at least one approval
4. **Semantic Versioning**: Follow semver for releases
5. **Changelog**: Keep CHANGELOG.md updated
6. **Documentation**: Update docs with each release

## 🔍 Monitoring

Monitor workflow runs:
- Go to **Actions** tab
- Click on specific workflow
- View run history and logs
- Download artifacts from successful runs

## ❓ Troubleshooting

### Workflow Fails

1. Check the logs in Actions tab
2. Verify all secrets are configured
3. Ensure dependencies are compatible
4. Test locally before pushing

### Docker Build Fails

1. Verify Dockerfile syntax
2. Check base image availability
3. Ensure all files are included
4. Review build logs for errors

### PyPI Upload Fails

1. Verify API token is valid
2. Check version isn't already published
3. Ensure package metadata is complete
4. Test with Test PyPI first

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Docker Publishing](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

---

**Last Updated**: January 21, 2026
