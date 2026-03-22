from fastapi import FastAPI
from member import member_router

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to the Gym API"}

# router 
app.include_router(member_router)