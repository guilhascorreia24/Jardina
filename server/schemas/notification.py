from pydantic import BaseModel

class NotificationOut(BaseModel):
    id: int
    content: str
    is_read: bool

    class Config:
        orm_mode = True
