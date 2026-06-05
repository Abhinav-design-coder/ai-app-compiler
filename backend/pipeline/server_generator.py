import os


def generate_fastapi_server(schemas):

    backend_dir_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    backend_dir = os.path.join(backend_dir_root, "generated_backend")

    os.makedirs(
        backend_dir,
        exist_ok=True
    )

    tables = schemas.get(
        "database",
        {}
    ).get(
        "tables",
        []
    )

    imports = []
    includes = []

    for table in tables:

        name = table["name"]

        imports.append(
            f"from routes.{name} import router as {name}_router"
        )

        includes.append(
            f'app.include_router({name}_router)'
        )

    server_code = f"""
from fastapi import FastAPI

{chr(10).join(imports)}

app = FastAPI()

{chr(10).join(includes)}

@app.get("/")
def root():
    return {{
        "message": "Generated Backend Running"
    }}
"""

    with open(
        f"{backend_dir}/main.py",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(server_code)