
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/users")
def get_all():
    return data

@router.post("/users")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/users" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
