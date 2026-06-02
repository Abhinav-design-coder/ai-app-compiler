# AI App Compiler

This repository contains a sample architecture for an AI application compiler with separate frontend and backend components.

Structure:

- `frontend/` - React-based UI shell
- `backend/` - Flask API and compilation pipeline
- `backend/pipeline/` - intent extraction, architecture generation, schema creation, validation, repair, and runtime simulation
- `backend/schemas/` - application and validation schema definitions
- `backend/evaluation/` - evaluation prompts and metrics utilities
- `docs/` - architecture and design documentation

## Getting Started

- Frontend: `npm install` then `npm start`
- Backend: `pip install -r backend/requirements.txt` then `python backend/app.py`
