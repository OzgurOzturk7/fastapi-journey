from fastapi import FastAPI

app = FastAPI()

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.delete("/delete_member/{crew_id}")
async def delete_member(crew_id: int):
    for member in crew:
        if member["id"] == crew_id:
            crew.remove(member)
            return {"message": f"Crew member with ID {crew_id} has been removed", "deleted_member": member}
    return {"message": "Crew member not found"}