from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="webapp")
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("website/homepage.html", {"request": request})

