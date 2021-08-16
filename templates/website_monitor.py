from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.repository.websites import list_websites
from sqlalchemy.orm import Session
from db.session import get_db
import requests as req

from core.config import settings

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


def get_status(website_url: str):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
    resp = req.get(url=website_url, headers=headers)
    if resp.status_code == 200:
        print("upupup")
        return True


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    websites = list_websites(db=db)
    for website in websites:
        website.image_file = "static/images/001-youtube.png"
        status = get_status(website.website_url)
        if status:
            website.status = True
        else:
            website.status = False
        website.website_card_desc = f"Check if {website.website_name} is running..."

    return templates.TemplateResponse("website/homepage.html", {"request": request, "websites": websites})
