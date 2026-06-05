
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/marks")
def get_all():
    return data

@router.post("/marks")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/marks" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
