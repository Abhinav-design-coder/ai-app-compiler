
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/products")
def get_all():
    return data

@router.post("/products")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/products" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
