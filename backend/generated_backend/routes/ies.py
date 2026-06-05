
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/ies")
def get_all():
    return data

@router.post("/ies")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/ies" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
