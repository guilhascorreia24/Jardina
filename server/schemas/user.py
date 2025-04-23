from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    is_gardener: bool = False

class UserLogin(BaseModel):
    email: str
    password: str
