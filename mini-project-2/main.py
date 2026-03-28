from fastapi import FastAPI
from database.connection import Settings
from routes.events import event_router
from routes.users import user_router

app = FastAPI()
settings = Settings()

app.include_router(event_router, prefix="/event")
app.include_router(user_router, prefix="/user")

@app.on_event("startup")
async def on_startup():
    await settings.initialize_database()