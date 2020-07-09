from fastapi import APIRouter

from app.api.api_v1.endpoints import data, label_options, projects, annotion_types

api_router = APIRouter()
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(data.router, prefix="/data", tags=["data"])
api_router.include_router(
    label_options.router, prefix="/label_options", tags=["label_options"]
)
api_router.include_router(
    annotion_types.router, prefix="/annotion_types", tags=["annotion_types"]
)