from db.models.sites import Website
from schemas.websites import WebsiteCreate
from sqlalchemy.orm import Session


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





