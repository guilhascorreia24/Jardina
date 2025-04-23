from pydantic import BaseModel

class GardenerCreate(BaseModel):
    bio: str
    location: str
