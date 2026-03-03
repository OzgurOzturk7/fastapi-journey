from fastapi import FastAPI, Request

app = FastAPI()

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.get("/members/{crew_id}")
async def read_crew_member(crew_id: int):
    for member in crew:
        if member["id"] == crew_id:
            return member
    return {"message": "Crew member not found"}

@app.post("/members/")
async def add_crew_member(request: Request):
    data = await request.json()
    new_id = crew[-1]["id"] + 1 if crew else 1
    new_member = {"id": new_id, "name": data["name"], "role": data["role"]}
    crew.append(new_member)
    return new_member

@app.put("/members/{crew_id}")
async def update_crew_member(crew_id: int, request: Request):
    data = await request.json()
    for member in crew:
        if member["id"] == crew_id:
            member["name"] = data["name"]
            member["role"] = data["role"]
            return member
    return {"message": "Crew member not found"}

@app.delete("/members/{crew_id}")
async def delete_crew_member(crew_id: int):
    for member in crew:
        if member["id"] == crew_id:
            crew.remove(member)
            return {"message": f"Crew member {crew_id} deleted"}
    return {"message": "Crew member not found"}