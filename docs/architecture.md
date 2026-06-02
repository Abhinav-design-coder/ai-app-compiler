# Architecture Overview

The AI App Compiler is structured into frontend, backend, and evaluation modules.

## Frontend

- `frontend/src/App.jsx` - React entrypoint for the application UI.

## Backend

- `backend/app.py` - Flask API that orchestrates the compilation pipeline.
- `backend/pipeline/` - Modular pipeline stages:
  - `intent_extractor.py`
  - `architecture_generator.py`
  - `schema_generator.py`
  - `validator.py`
  - `repair_engine.py`
  - `runtime_simulator.py`
- `backend/schemas/` - Schema definitions for intents, application architecture, and validation rules.

## Evaluation

- `backend/evaluation/prompts.json` - Evaluation prompt examples.
- `backend/evaluation/metrics.py` - Metrics utilities for assessing output quality.
