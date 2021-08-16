from fastapi import APIRouter
from templates import website_monitor

api_router = APIRouter()

api_router.include_router(website_monitor.router, prefix="", tags=["Homepage"])
