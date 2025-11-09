# backend/api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory storage (for MVP example)
users = {}
recipes = {}
moods = {}
user_moods = []

class MoodInput(BaseModel):
    user_id: int
    mood_name: str

class UserCreate(BaseModel):
    username: str
    email: str

class RecipeResponse(BaseModel):
    id: int
    name: str
    ingredients: List[str]
    dietary_restrictions: Optional[List[str]] = []
    cook_time_minutes: int

class UserPreferences(BaseModel):
    preferences: List[str]

@app.post('/api/mood')
def post_mood(mood_input: MoodInput):
    # Process mood input: store it and retrieve matching recipes (mocked logic)
    user_moods.append({'user_id': mood_input.user_id, 'mood': mood_input.mood_name})
    # Return mocked recipe list
    matching_recipes = list(recipes.values())[:3]  # Top 3 recipes
    return {'recipes': matching_recipes}

@app.get('/api/recipes/{recipe_id}')
def get_recipe(recipe_id: int):
    if recipe_id not in recipes:
        raise HTTPException(status_code=404, detail='Recipe not found')
    return recipes[recipe_id]

@app.post('/api/users')
def create_user(user: UserCreate):
    user_id = len(users) + 1
    users[user_id] = {'id': user_id, 'username': user.username, 'email': user.email, 'preferences': []}
    return users[user_id]

@app.get('/api/users/{user_id}/preferences')
def get_preferences(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    return {'preferences': users[user_id].get('preferences', [])}

@app.put('/api/users/{user_id}/preferences')
def put_preferences(user_id: int, prefs: UserPreferences):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    users[user_id]['preferences'] = prefs.preferences
    return {'preferences': prefs.preferences}

# Mock initial data
recipes[1] = {'id': 1, 'name': 'Tomato Pasta', 'ingredients': ['tomato', 'pasta', 'garlic'], 'dietary_restrictions': [], 'cook_time_minutes': 20}
recipes[2] = {'id': 2, 'name': 'Avocado Salad', 'ingredients': ['avocado', 'lettuce', 'lemon'], 'dietary_restrictions': ['vegan'], 'cook_time_minutes': 10}
recipes[3] = {'id': 3, 'name': 'Chicken Curry', 'ingredients': ['chicken', 'curry powder', 'rice'], 'dietary_restrictions': [], 'cook_time_minutes': 40}
