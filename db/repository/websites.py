from db.models.sites import Website
from schemas.websites import WebsiteCreate
from sqlalchemy.orm import Session
from typing import List
import requests as req


def get_status(website_url: str):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
    resp = req.get(url=website_url, headers=headers)
    if resp.status_code == 200:
        print("upupup")
        return True


def create_new_website(website: WebsiteCreate, db: Session):
    website = Website(**website.dict())
    db.add(website)
    db.commit()
    db.refresh(website)
    return website


def retrieve_website_by_id(id: int, db: Session):
    website = db.query(Website).filter(Website.id == id).first()
    return website


def list_websites(db: Session):
    websites = db.query(Website).all()
    return websites


def update_website_by_id(id: int, website: WebsiteCreate, db: Session):
    existing_website = db.query(Website).filter(Website.id == id)
    existing_website.update(website.__dict__)
    db.commit()
    return "done"


def delete_website_by_id(id: int, db: Session):
    existing_website = db.query(Website).filter(Website.id == id)
    if not existing_website.first():
        return None
    existing_website.delete()
    db.commit()
    return "done"


def process_websites(websites: List[Website], db: Session):
    new_list = []
    for website in websites:
        website.website_ico = f"static/images/{website.website_name.lower()}.ico"
        website.image_file = "static/images/001-youtube.png"
        status = get_status(website.website_url)
        if status:
            website.status = True
        else:
            website.status = False
        website_description = website.website_description
        new_list.append(website)
    return new_list




