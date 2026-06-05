
from fastapi import APIRouter

router = APIRouter()

data = []

@router.get("/managements")
def get_all():
    return data

@router.post("/managements")
def create(item: dict):
    data.append(item)
    return item

@router.delete("/managements" + "/{item_id}")
def delete(item_id: int):
    return {
        "deleted": item_id
    }
