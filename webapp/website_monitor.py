from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.repository.websites import list_websites
from sqlalchemy.orm import Session
from db.session import get_db

templates = Jinja2Templates(directory="webapp")
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    websites = list_websites(db=db)
    for website in websites:
        website.website_card_desc = f"Check if {website.website_name} is running..."

    return templates.TemplateResponse("website/homepage.html", {"request": request, "websites": websites})
