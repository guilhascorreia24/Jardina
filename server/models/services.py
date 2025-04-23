from sqlalchemy import Column, Integer, String, ForeignKey
from server.core.database import Base

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"))
    gardener_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String)
    status = Column(String, default="pendente")  # pendente, concluido
    