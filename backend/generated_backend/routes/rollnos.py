
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/rollnos")
def get_all():
    return data

@router.post("/rollnos")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/rollnos" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
