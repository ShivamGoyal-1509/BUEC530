from pydantic import BaseModel, EmailStr
from uuid import uuid4

class User(BaseModel):
    id: str = str(uuid4())
    name: str
    email: EmailStr
    password: str

class House(BaseModel):
    id: str = str(uuid4())
    name: str
    address: str
    owner_id: str

class Room(BaseModel):
    id: str = str(uuid4())
    name: str
    house_id: str

class Device(BaseModel):
    id: str = str(uuid4())
    name: str
    type: str
    room_id: str
    status: str