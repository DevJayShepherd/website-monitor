from typing import List

from db.repository.websites import create_new_website, retrieve_website_by_id, list_websites, update_website_by_id, \
    delete_website_by_id
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.websites import WebsiteCreate, ShowWebsite
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/add_website", response_model=ShowWebsite)
def add_website(website: WebsiteCreate, db: Session = Depends(get_db)):
    website = create_new_website(website=website, db=db)
    return website


@router.get("/get/{id}", response_model=ShowWebsite)
def retrieve_website_with_id(id: int, db: Session = Depends(get_db)):
    website = retrieve_website_by_id(id, db=db)
    if not website:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Website with id {id} does not exist")
    return website


@router.get("/all", response_model=List[ShowWebsite])
def retrieve_all_websites(db: Session = Depends(get_db)):
    websites = list_websites(db=db)
    return websites


@router.put("/update/{id}")
def update_website(id: int, website: WebsiteCreate, db: Session = Depends(get_db)):
    response = update_website_by_id(id=id, website=website, db=db)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"website with id {id} not found")
    return {"detail": f"website with id {id} updated successfully."}


@router.delete("/delete/{id}")
def delete_website(id: int, db: Session = Depends(get_db)):
    response = delete_website_by_id(id=id, db=db)
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"website with id {id} not found")
    return f"Website with {id} has been deleted successfully."
