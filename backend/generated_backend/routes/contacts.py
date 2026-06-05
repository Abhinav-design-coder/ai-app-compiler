
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/contacts")
def get_all():
    return data

@router.post("/contacts")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/contacts" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
