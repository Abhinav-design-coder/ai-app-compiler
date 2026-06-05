from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from pipeline.intent_extractor import extract_intent
from pipeline.architecture_generator import generate_architecture
from pipeline.schema_generator import generate_schemas
from pipeline.validator import validate_schemas
from pipeline.repair_engine import repair_schemas
from pipeline.runtime_simulator import simulate_runtime
from pipeline.code_generator import generate_react_app
from pipeline.api_generator import generate_fastapi_routes
from pipeline.server_generator import generate_fastapi_server

class CompileRequest(BaseModel):
    prompt: str

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "AI App Compiler API", "endpoint": "/compile"}


@app.post("/compile")
def compile_app(request: CompileRequest):

    intent = extract_intent(request.prompt)

    architecture = generate_architecture(intent)

    schemas = generate_schemas(
        intent,
        architecture
    )

    validation = validate_schemas(
        intent,
        architecture,
        schemas
    )

    repair_result = repair_schemas(
        schemas,
        validation["errors"]
    )

    runtime = simulate_runtime(
        repair_result["schemas"]
    )

    schemas = repair_result["schemas"]

    generated_app = generate_react_app(
        schemas
    )

    generate_fastapi_routes(schemas)

    generate_fastapi_server(schemas)

    return {
        "intent": intent.model_dump(),
        "architecture": architecture,
        "schemas": schemas,
        "validation": validation,
        "repairs": repair_result["repairs"],
        "runtime": runtime,
        "generated_app": generated_app
    }

