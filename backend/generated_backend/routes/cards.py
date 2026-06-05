
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/cards")
def get_all():
    return data

@router.post("/cards")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/cards" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
