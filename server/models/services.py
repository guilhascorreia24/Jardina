from sqlalchemy import Column, Date, Integer, String, ForeignKey, Time
from server.core.database import Base

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"))
    gardener_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String)
    status = Column(String, default="pendente")  # pendente, concluido
    date = Column(Date, nullable=True)
    start_time = Column(Time, nullable=True)
    