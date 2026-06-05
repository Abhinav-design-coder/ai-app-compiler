
from fastapi import FastAPI

from routes.users import router as users_router
from routes.products import router as products_router
from routes.managements import router as managements_router

app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)
app.include_router(managements_router)

@app.get("/")
def root():
    return {
        "message": "Generated Backend Running"
    }
