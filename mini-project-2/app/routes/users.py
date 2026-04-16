from fastapi import APIRouter, HTTPException, status
from database.connection import Database
from models.users import User, UserSignIn

user_router = APIRouter(tags=["Users"])
user_database = Database(User)

@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    existing = await User.find_one(User.email == user.email)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User with this email already exists")
    await user_database.save(user)
    return {"message": "User created successfully"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    existing = await User.find_one(User.email == user.email)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    if existing.password == user.password:
        return {"message": "User signed in successfully"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid credentials")