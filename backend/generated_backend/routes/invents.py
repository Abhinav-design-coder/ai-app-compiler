
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/invents")
def get_all():
    return data

@router.post("/invents")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/invents" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
