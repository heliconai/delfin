from fastapi import APIRouter

from app.api.api_v1.endpoints import projects, data

api_router = APIRouter()
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(data.router, prefix="/data", tags=["data"])