# MLOps Project Architecture

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                          MLOps Project                               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                       Version Control Layer                          │
├─────────────────────────────────────────────────────────────────────┤
│  Git                │  DVC                                           │
│  - Source code      │  - Data versioning                            │
│  - Configurations   │  - Model versioning                           │
│  - Pipelines        │  - Remote storage                             │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        Data Pipeline (ZenML)                         │
├─────────────────────────────────────────────────────────────────────┤
│  Step 1: Load Data                                                   │
│     │                                                                │
│     ▼                                                                │
│  Step 2: Preprocess Data                                            │
│     │                                                                │
│     ▼                                                                │
│  Step 3: Train Model  ──────────►  MLflow Tracking                  │
│     │                              - Log parameters                  │
│     ▼                              - Log metrics                     │
│  Step 4: Evaluate Model ─────────►  - Log artifacts                 │
│     │                              - Model registry                  │
│     ▼                                                                │
│  Step 5: Save Model ──────────►  DVC (model versioning)             │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      Deployment Layer (Docker)                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │
│  │   MLflow     │  │     App      │  │   Jupyter    │             │
│  │   Server     │  │  Container   │  │   Notebook   │             │
│  │              │  │              │  │              │             │
│  │  Port: 5000  │  │  Pipeline    │  │  Port: 8888  │             │
│  └──────────────┘  └──────────────┘  └──────────────┘             │
│         │                  │                  │                     │
│         └──────────────────┴──────────────────┘                     │
│                     Docker Network                                   │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Flow

```
Raw Data (data/raw/)
       │
       │ (tracked by DVC)
       ▼
  Data Loader ────────► Load Iris Dataset
       │
       ▼
  Preprocessing ──────► Train/Test Split + Scaling
       │
       ▼
Processed Data (data/processed/)
       │
       │ (tracked by DVC)
       ▼
  Model Training ─────► Random Forest Classifier
       │                         │
       │                         ├─► Log to MLflow
       │                         │   - Parameters
       │                         │   - Metrics
       │                         │   - Artifacts
       ▼                         │
  Model Evaluation ──────────────┘
       │
       ▼
Trained Model (models/)
       │
       │ (tracked by DVC)
       ▼
    Deployment
```

## Technology Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                         │
├─────────────────────────────────────────────────────────────┤
│  Python 3.9+                                                 │
│  - scikit-learn (ML models)                                 │
│  - pandas/numpy (data processing)                           │
│  - matplotlib/seaborn (visualization)                       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      MLOps Tools                             │
├─────────────────────────────────────────────────────────────┤
│  ZenML (Pipeline Orchestration)                             │
│  MLflow (Experiment Tracking)                               │
│  DVC (Data Version Control)                                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   Infrastructure Layer                       │
├─────────────────────────────────────────────────────────────┤
│  Docker (Containerization)                                   │
│  Docker Compose (Multi-service orchestration)               │
│  Git (Version Control)                                       │
└─────────────────────────────────────────────────────────────┘
```

## Pipeline Execution Flow

```
User Action: python src/pipelines/training_pipeline.py
       │
       ▼
┌──────────────────────────────────────────────────────┐
│              ZenML Pipeline Starts                    │
└──────────────────────────────────────────────────────┘
       │
       ├─► Step 1: load_data_step()
       │   └─► Load Iris dataset
       │   └─► Save to data/raw/ (DVC tracked)
       │
       ├─► Step 2: preprocess_data_step()
       │   └─► Split train/test
       │   └─► Scale features
       │   └─► Save to data/processed/ (DVC tracked)
       │
       ├─► Step 3: train_model_step()
       │   └─► Create MLflow run
       │   └─► Log parameters to MLflow
       │   └─► Train Random Forest model
       │   └─► Log model to MLflow
       │
       ├─► Step 4: evaluate_model_step()
       │   └─► Calculate metrics (accuracy, precision, etc.)
       │   └─► Log metrics to MLflow
       │
       └─► Step 5: save_model_step()
           └─► Save model to models/ (DVC tracked)
           └─► Pipeline complete
```

## MLflow Tracking Structure

```
MLflow Server (http://localhost:5000)
       │
       ├─► Experiments
       │   └─► iris_classification
       │       └─► Runs
       │           ├─► Run 1
       │           │   ├─► Parameters
       │           │   │   ├─ n_estimators: 100
       │           │   │   ├─ max_depth: 5
       │           │   │   └─ random_state: 42
       │           │   ├─► Metrics
       │           │   │   ├─ accuracy: 0.97
       │           │   │   ├─ precision: 0.97
       │           │   │   ├─ recall: 0.97
       │           │   │   └─ f1_score: 0.97
       │           │   └─► Artifacts
       │           │       └─ model/
       │           └─► Run 2...
       │
       └─► Models (Registry)
           └─► iris_classifier
```

## Docker Compose Services

```
docker-compose.yml
       │
       ├─► mlflow (Service)
       │   ├─ Image: python:3.9-slim
       │   ├─ Port: 5000
       │   ├─ Volumes: ./mlruns, ./mlartifacts
       │   └─ Command: mlflow server
       │
       ├─► app (Service)
       │   ├─ Build: ./Dockerfile
       │   ├─ Depends on: mlflow
       │   ├─ Volumes: ./data, ./models, ./src
       │   └─ Command: python training_pipeline.py
       │
       └─► jupyter (Service)
           ├─ Build: ./Dockerfile
           ├─ Port: 8888
           ├─ Volumes: ./notebooks, ./data, ./models
           └─ Command: jupyter notebook
```

## File Organization

```
mlops/
│
├── Version Control
│   ├── .git/           (Git repository)
│   └── .dvc/           (DVC configuration)
│
├── Source Code
│   └── src/
│       ├── config.py           (Configuration)
│       ├── data/               (Data utilities)
│       ├── models/             (Model utilities)
│       └── pipelines/          (ZenML pipelines)
│
├── Data (DVC tracked)
│   ├── data/raw/               (Raw datasets)
│   └── data/processed/         (Processed datasets)
│
├── Models (DVC tracked)
│   └── models/                 (Trained models)
│
├── Deployment
│   ├── Dockerfile              (Container definition)
│   └── docker-compose.yml      (Multi-service setup)
│
└── Development
    ├── notebooks/              (Jupyter notebooks)
    └── requirements.txt        (Dependencies)
```

## Workflow Integration

```
Developer Workflow:

1. Code Changes
   └─► Git commit ───► Push to repository

2. Data Changes
   └─► DVC add ───► DVC push ───► Git commit

3. Experiment
   └─► Run pipeline ───► MLflow tracks ───► Review results

4. Model Update
   └─► Train new model ───► DVC add ───► Git commit

5. Deployment
   └─► Docker build ───► Docker compose up ───► Production
```

## Benefits of This Architecture

✅ **Reproducibility**: Every experiment is tracked and can be reproduced
✅ **Versioning**: Code, data, and models are all versioned
✅ **Scalability**: Docker containers can be deployed anywhere
✅ **Collaboration**: Team members can share experiments via MLflow
✅ **Automation**: ZenML orchestrates the entire pipeline
✅ **Monitoring**: MLflow provides experiment tracking and comparison
