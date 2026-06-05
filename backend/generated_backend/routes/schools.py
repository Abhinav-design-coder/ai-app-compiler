
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/schools")
def get_all():
    return data

@router.post("/schools")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/schools" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
