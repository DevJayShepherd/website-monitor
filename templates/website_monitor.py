from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.repository.websites import list_websites, process_websites
from sqlalchemy.orm import Session
from db.session import get_db
import requests as req

from core.config import settings

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    websites = list_websites(db=db)
    websites = process_websites(websites, db=db)

    return templates.TemplateResponse("website/homepage.html", {"request": request, "websites": websites})


@router.get("/contact")
def about(request: Request):
    return templates.TemplateResponse("/website/contact.html", {"request": request})
