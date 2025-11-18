# MLOps DataScience Pipeline

A modular, YAML-driven end-to-end MLOps pipeline in Python covering:
Data Ingestion → Validation → Transformation → Model Training → Evaluation (MLflow logging).  
All artifacts are written to the `artifacts/` directory for reproducibility.

---

## Table of contents
- [Overview](#overview)  
- [Architecture diagram](#architecture-diagram)  
- [Quick start (Windows)](#quick-start-windows)  
- [Configuration (YAML notes)](#configuration-yaml-notes)  
- [Running the pipeline](#running-the-pipeline)  
- [Troubleshooting & common fixes](#troubleshooting--common-fixes)  
- [Project structure](#project-structure)  
- [Next steps & contribution](#next-steps--contribution)

---

## Overview
Purpose: automate the lifecycle from raw data download to model evaluation and logging.  
Key principles: modular components, YAML configuration, dataclass config entities, and artifact-based outputs.

## Architecture diagram
Mermaid (renders on platforms that support Mermaid):

```mermaid
graph TD
  U[(User / CI)] -->|run main.py| Orchestrator[main.py Orchestrator]
  Orchestrator --> Config[ConfigurationManager (read_yaml)]
  Config -->|provides configs| PipelineManager[Pipeline Stages]
  PipelineManager --> DI[Data Ingestion]
  PipelineManager --> DV[Data Validation]
  PipelineManager --> DT[Data Transformation]
  PipelineManager --> MT[Model Trainer]
  PipelineManager --> ME[Model Evaluation]
  DI -->|downloads ZIP -> extracts CSV| ArtifactsRaw[artifacts/data_ingestion]
  DV -->|reads CSV, writes status| ArtifactsVal[artifacts/data_validation]
  DT -->|splits -> train/test| ArtifactsTrans[artifacts/data_transformation]
  MT -->|trains -> model artifact| ArtifactsModel[artifacts/model_trainer]
  ME -->|evaluates -> metrics & mlflow| ArtifactsEval[artifacts/model_evaluation]
  ArtifactsModel --> MLFlow[MLflow / Model Registry]
```

Plaintext overview:
- main.py (Orchestrator) → ConfigurationManager reads YAMLs → Stage pipelines:
  - Data Ingestion → artifacts/data_ingestion
  - Data Validation → artifacts/data_validation/status.txt
  - Data Transformation → artifacts/data_transformation/train.csv, test.csv
  - Model Trainer → artifacts/model_trainer/model.pkl
  - Model Evaluation → artifacts/model_evaluation (MLflow)

## Quick start (Windows)
1. Create & activate venv (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
2. Ensure these files exist at project root:
- `config/config.yaml`
- `params.yaml`
- `schema.yaml`

3. Run:
```cmd
python main.py
```

## Configuration (YAML notes)
- Always use a space after `:` (e.g. `key: value`).  
- Keep nested mappings indented.
- Important keys:
  - config/config.yaml: `artifacts_root`, `data_ingestion`, `data_validation`, `data_transformation`, `model_trainer`, `model_evaluation`
  - params.yaml: hyperparameters (e.g. `model_trainer: { alpha: 0.2, l1_ratio: 0.1 }`)
  - schema.yaml: `COLUMNS:` mapping and `TARGET_COLUMN: name: <col>`

## Troubleshooting & common fixes
- "YAML content must be a mapping/dict" → fix YAML spacing/indentation.
- "ConfigBox object has no attribute 'X'" → key missing or misspelled in YAML (case-sensitive).
- FileNotFoundError reading CSV/status → ensure ingestion completed and check `artifacts/*` paths.
- TypeError: 'DataFrame' object is not callable → use `df[col]` not `df(col)`.
- After code edits, restart Python/Jupyter kernel or use `importlib.reload()`.

Quick debug:
```python
from src.mlops_pipeline.utils.common import read_yaml
print(read_yaml("config/config.yaml"))
print(read_yaml("params.yaml"))
print(read_yaml("schema.yaml"))
```

Find produced CSV:
```python
from pathlib import Path
print(list(Path("artifacts/data_ingestion").glob("*.csv")))
```

## Project structure (high-level)
- main.py — orchestrator  
- config/ — config files  
- params.yaml — hyperparameters  
- schema.yaml — dataset schema  
- src/mlops_pipeline/
  - config/ configuration.py (ConfigurationManager)
  - pipeline/ stage pipelines
  - components/ implementations for each stage
  - entity/ dataclass config types
  - utils/ helpers (read_yaml, create_directories, save/load)
- research/ — notebooks  
- artifacts/ — generated outputs

## Next steps & contribution
- Add unit tests for utils and components.  
- Harden configuration parsing and defaults.  
- Integrate MLflow server and model registry.  
- Add CI (lint/tests) and Dockerfile for reproducible runs.

## License
Add your chosen license file (e.g., MIT) at the repo root.
