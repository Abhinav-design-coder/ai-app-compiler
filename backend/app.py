from fastapi import FastAPI

from pipeline.intent_extractor import extract_intent
from pipeline.architecture_generator import generate_architecture
from pipeline.schema_generator import generate_schemas
from pipeline.validator import validate_schemas

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "AI App Compiler API", "endpoint": "/compile"}


@app.post("/compile")
def compile_app(prompt: str):

    intent = extract_intent(prompt)

    architecture = generate_architecture(intent)

    schemas = generate_schemas(
        intent,
        architecture
    )

    validation = validate_schemas(
        schemas
    )

    return {
        "intent": intent.model_dump(),
        "architecture": architecture,
        "schemas": schemas,
        "validation": validation
    }
