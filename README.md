# AI App Compiler

## Overview

AI App Compiler is a compiler-style system that converts natural language application requirements into structured, validated, and executable application configurations.

The system follows a multi-stage pipeline inspired by modern AI application generators. Instead of generating code directly, it produces a reliable configuration containing:

* UI Schema
* API Schema
* Database Schema
* Authentication & Authorization Rules
* Business Logic Definitions

The generated configuration is validated, repaired when necessary, and tested through a runtime simulation layer.

---

## System Architecture

Natural Language Prompt
↓
Intent Extraction
↓
Architecture Generation
↓
Schema Generation
↓
Validation Engine
↓
Repair Engine
↓
Runtime Simulation
↓
Executable Application Configuration

---

## Features

### Intent Extraction

Extracts:

* Entities
* Roles
* Features
* Authentication requirements
* Payment requirements

### Architecture Generation

Generates:

* Application modules
* System structure
* Functional components

### Schema Generation

Produces:

* Database schema
* API schema
* UI schema
* Auth schema

### Validation Engine

Checks:

* Module ↔ UI consistency
* Entity ↔ API consistency
* Required roles
* Cross-layer correctness

### Repair Engine

Automatically fixes:

* Missing roles
* Missing pages
* Missing endpoints
* Schema inconsistencies

### Runtime Simulator

Simulates execution readiness by verifying:

* Required schemas exist
* Modules are deployable
* No critical validation errors remain

---

## Evaluation Framework

Dataset:

* 10 Real Product Prompts
* 10 Edge Case Prompts

Metrics:

* Success Rate
* Failure Count
* Repair Count
* Average Latency

Example Result:

* Total Prompts: 20
* Successful: 20
* Failed: 0
* Success Rate: 100%

---

## Project Structure

backend/
│
├── app.py
├── pipeline/
│   ├── intent_extractor.py
│   ├── architecture_generator.py
│   ├── schema_generator.py
│   ├── validator.py
│   ├── repair_engine.py
│   └── runtime_simulator.py
│
├── schemas/
│
└── evaluation/
├── prompts.json
├── metrics.py
├── run_evaluation.py
└── evaluation_results.json

frontend/
│
└── React + Tailwind UI

---

## Running the Project

Backend

pip install -r backend/requirements.txt

uvicorn app:app --reload

Frontend

npm install

npm run dev

---

## Example Prompt

Build a CRM with login, contacts, dashboard, role-based access, and premium plan with payments. Admins can view analytics.

The system generates a validated application configuration containing architecture, schemas, authentication rules, and deployment readiness information.
