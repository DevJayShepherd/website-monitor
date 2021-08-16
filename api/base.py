from api.v1 import route_login
from api.v1 import route_users
from api.v1 import route_websites
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/users", tags=["Users"])
api_router.include_router(route_websites.router, prefix="/website", tags=["Websites"])
api_router.include_router(route_login.router, prefix="/login", tags=["Login"])
