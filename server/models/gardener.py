from sqlalchemy import Column, Integer, String, ForeignKey
from server.core.database import Base

class Gardener(Base):
    __tablename__ = "gardeners"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    bio = Column(String)
    location = Column(String)
