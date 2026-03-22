from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain", "experience": 10, "specialty": "Leadership"},
    {"id": 2, "name": "Alice", "role": "Engineer", "experience": 8, "specialty": "Mechanical"},
    {"id": 3, "name": "Bob", "role": "Scientist", "experience": 5, "specialty": "Biology"}
]

# Pydantic model
class CrewMember(BaseModel):
    name: str
    role: str
    experience: int
    specialty: str


# POST endpoint
@app.post("/crew/")
async def add_crew_member(member: CrewMember):

    new_id = max(c["id"] for c in crew) + 1 if crew else 1

    new_member = {
        "id": new_id,
        "name": member.name,
        "role": member.role,
        "experience": member.experience,
        "specialty": member.specialty
    }

    crew.append(new_member)

    return {"message": "Crew member added successfully", "details": new_member}