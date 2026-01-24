from pydantic import BaseModel
from enum import Enum

class Status(str, Enum):
    completed = "completed"
    pending = "pending"
    in_progress = "in_progress"

class Profile(str, Enum):
    admin = "admin"
    leader = "leader"
    member = "member"
    freelancer = "freelancer"

class Login(BaseModel):
    email: str
    password: str

class Register(BaseModel):
    email: str
    password: str
    username: str|None = None
    full_name: str

class Tasks(BaseModel):
    user: str
    task: str
    status: Status|None = Status.pending
