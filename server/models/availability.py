from unittest.mock import Base
from sqlalchemy import Column, ForeignKey, Integer, Time


class Availability(Base):
    __tablename__ = "availabilities"

    id = Column(Integer, primary_key=True)
    gardener_id = Column(Integer, ForeignKey("users.id"))
    weekday = Column(Integer)  # 0=Segunda, 6=Domingo
    start_time = Column(Time)
    end_time = Column(Time)
