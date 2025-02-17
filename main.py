from fastapi import FastAPI, HTTPException
from models import User, House, Room, Device

app = FastAPI()

users_db = {}
houses_db = {}
rooms_db = {}
devices_db = {}

# User Endpoints
@app.post("/users/register")
def register_user(user: User):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.email] = user
    return {"message": "User registered successfully"}

@app.post("/users/login")
def login_user(email: str, password: str):
    user = users_db.get(email)
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    for user in users_db.values():
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")