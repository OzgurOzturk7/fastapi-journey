from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CrewMember(BaseModel):
    name: str
    role: str

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.get("/")
def home():
    return {"message": "Crew API is running"}

@app.post("/add_crew/")
def add_crew(member: CrewMember):
    new_id = 1 if len(crew) == 0 else crew[-1]["id"] + 1
    new_member = {"id": new_id, "name": member.name, "role": member.role}
    crew.append(new_member)
    return new_member