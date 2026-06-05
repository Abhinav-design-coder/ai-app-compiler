
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/students")
def get_all():
    return data

@router.post("/students")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/students" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
