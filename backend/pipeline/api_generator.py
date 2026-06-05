import os


def generate_fastapi_routes(schemas):

    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    api_folder = os.path.join(backend_dir, "generated_backend", "routes")

    os.makedirs(
        api_folder,
        exist_ok=True
    )

    tables = schemas.get(
        "database",
        {}
    ).get(
        "tables",
        []
    )

    for table in tables:

        table_name = table["name"]

        route_code = f'''
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/{table_name}")
def get_all():
    return data

@router.post("/{table_name}")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/{table_name}" + "/{{item_id}}")
def delete(item_id: int):
    return {{
        "deleted": item_id
    }}
'''

        with open(
            f"{api_folder}/{table_name}.py",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(route_code)