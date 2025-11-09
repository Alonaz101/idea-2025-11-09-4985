# backend/models.py

from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

# User model
class User(BaseModel):
    id: int
    username: str
    email: str
    preferences: Optional[List[str]] = []

# Recipe model
class Recipe(BaseModel):
    id: int
    name: str
    ingredients: List[str]
    dietary_restrictions: Optional[List[str]] = []
    cook_time_minutes: int

# Mood model
class Mood(BaseModel):
    id: int
    mood_name: str
    description: Optional[str] = None

# UserMoodRecord model
class UserMoodRecord(BaseModel):
    id: int
    user_id: int
    mood_id: int
    recorded_at: datetime = Field(default_factory=datetime.utcnow)

