from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Website(Base):
    id = Column(Integer, primary_key=True, index=True)
    website_name = Column(String, unique=True, nullable=False)
    website_url = Column(String, unique=True, nullable=False)
    website_description = Column(String, nullable=False)  # This will be metadata
    website_keywords = Column(String, nullable=True)
    twitter_account = Column(String, unique=False, nullable=True)
    youtube_account = Column(String, unique=False, nullable=True)
