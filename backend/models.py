from pydantic import BaseModel
from enum import Enum

class status(str, Enum):
    completed = "completed"
    pending = "pending"
    in_progress = "in_progress"

class profile(str, Enum):
    admin = "admin"
    leader = "leader"
    member = "member"
    freelancer = "freelancer"

class login(BaseModel):
    email: str
    password: str

class register(BaseModel):
    email: str
    password: str
    username: str|None = None
    full_name: str

class tasks(BaseModel):
    user: str
    task: str
    status: str|None = status.pending

class 