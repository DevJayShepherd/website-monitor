from db.repository.websites import create_new_website, retrieve_website_by_id
from schemas.websites import WebsiteCreate
from sqlalchemy.orm import Session


def test_retrieve_website_by_id(db_session: Session):
    website_name = "test"
    website_url = "test.com"
    website_description = "test"
    website_keywords = "test"
    website_schema = WebsiteCreate(website_name=website_name,
                                   website_url=website_url,
                                   website_description=website_description,
                                   website_keywords=website_keywords)
    new_website = create_new_website(website_schema, db=db_session)
    website_id = retrieve_website_by_id(1, db_session)
    assert website_id.id == 1


