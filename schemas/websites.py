from typing import Optional

from pydantic import BaseModel


class WebsiteBase(BaseModel):
    website_name: Optional[str] = None
    website_url: Optional[str] = None
    website_description: Optional[str] = None
    website_keywords: Optional[str] = None


class WebsiteCreate(WebsiteBase):
    website_name: str
    website_url: str
    website_description: str
    website_keywords: Optional[str] = None


class ShowWebsite(WebsiteBase):
    website_name: str
    website_url: str
    website_description: str
    website_keywords: Optional[str] = None

    class Config:
        orm_mode = True


