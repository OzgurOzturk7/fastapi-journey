from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models import Member
import asyncio

member_router = APIRouter()

# Template engine
# Template engine
templates = Jinja2Templates(directory="templates")

# Mock database
members = []

# ───────── API ENDPOINTS ─────────

@member_router.get("/members/")
async def get_members():
    await asyncio.sleep(1)
    return members


@member_router.get("/members/{member_id}")
async def get_member(member_id: int):
    for member in members:
        if member.id == member_id:
            return member

    raise HTTPException(
        status_code=404,
        detail=f"Member with ID {member_id} not found"
    )


@member_router.post("/members/")
async def add_member(member: Member):
    members.append(member)
    return member


@member_router.put("/members/{member_id}")
async def update_member(member_id: int, updated_member: Member):
    for index, member in enumerate(members):
        if member.id == member_id:
            members[index] = updated_member
            return updated_member

    raise HTTPException(
        status_code=404,
        detail=f"Member with ID {member_id} not found"
    )


@member_router.delete("/members/{member_id}")
async def delete_member(member_id: int):
    for member in members:
        if member.id == member_id:
            members.remove(member)
            return {"message": "Member deleted"}

    raise HTTPException(
        status_code=404,
        detail=f"Member with ID {member_id} not found"
    )


# ───────── HTML ROUTES ─────────

@member_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "members": members
    })


@member_router.get("/member/{id}", response_class=HTMLResponse)
async def get_member_page(request: Request, id: int):
    for member in members:
        if member.id == id:
            return templates.TemplateResponse("member.html", {
                "request": request,
                "member": member,
                "members": members
            })

    raise HTTPException(status_code=404, detail="Member not found")


# ───────── FORM SUBMIT ─────────

@member_router.post("/add-member")
async def add_member_form(
    name: str = Form(...),
    age: int = Form(...),
    workout_type: str = Form(...)
):
    new_member = Member(
        id=len(members) + 1,
        name=name,
        age=age,
        workout_type=workout_type,
        duration_minutes=30,
        calories_burned=200
    )

    members.append(new_member)

    return RedirectResponse(url="/home", status_code=303)