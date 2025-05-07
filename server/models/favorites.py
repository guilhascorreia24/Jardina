from unittest.mock import Base

from sqlalchemy import Column, ForeignKey, Integer


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("users.id"))
    gardener_id = Column(Integer, ForeignKey("users.id"))
