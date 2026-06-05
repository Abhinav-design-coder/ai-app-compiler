
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/patients")
def get_all():
    return data

@router.post("/patients")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/patients" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
