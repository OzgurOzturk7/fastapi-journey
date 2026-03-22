from pydantic import BaseModel, Field
from typing import List, Optional


class WorkoutSession(BaseModel):
    workout_type: str = Field(..., min_length=3, max_length=50)
    duration_minutes: int = Field(..., gt=0)
    calories_burned: int = Field(..., ge=0)


class Member(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=100)
    membership_active: Optional[bool] = True
    sessions: List[WorkoutSession] = []