
from fastapi import FastAPI

from routes.users import router as users_router
from routes.contacts import router as contacts_router

app = FastAPI()

app.include_router(users_router)
app.include_router(contacts_router)

@app.get("/")
def root():
    return {
        "message": "Generated Backend Running"
    }
