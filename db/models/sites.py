from db.base_class import Base
from sqlalchemy import Column, Integer, String


class Website(Base):
    id = Column(Integer, primary_key=True, index=True)
    website_name = Column(String, unique=True, nullable=False)
    website_url = Column(String, unique=True, nullable=False)
    website_description = Column(String, nullable=False)  # This will be metadata
    website_keywords = Column(String, nullable=True)
