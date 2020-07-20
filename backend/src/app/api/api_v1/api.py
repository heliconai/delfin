from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    annotation_types,
    data,
    data_modality,
    datasets,
    label_options,
)

api_router = APIRouter()
api_router.include_router(datasets.router, prefix="/datasets", tags=["datasets"])
api_router.include_router(data.router, prefix="/data", tags=["data"])
api_router.include_router(
    label_options.router, prefix="/label_options", tags=["label_options"]
)
api_router.include_router(
    annotation_types.router, prefix="/annotation_types", tags=["annotation_types"]
)
api_router.include_router(
    data_modality.router, prefix="/data_modality", tags=["data_modality"]
)
