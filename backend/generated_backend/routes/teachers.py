
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/teachers")
def get_all():
    return data

@router.post("/teachers")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/teachers" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
