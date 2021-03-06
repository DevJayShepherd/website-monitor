from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean, Date


class Users(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=True)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    alerts_active = Column(Boolean, default=False)
    date_joined = Column(Date)
