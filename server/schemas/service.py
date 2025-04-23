from pydantic import BaseModel

class ServiceCreate(BaseModel):
    description: str
    gardener_id: int  # ID do jardineiro
