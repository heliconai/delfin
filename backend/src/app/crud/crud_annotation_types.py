from app.crud.base import CRUDBase
from app.models.annotation_types import AnnotationTypes
from app.schemas.annotation_types import AnnotationTypeCreate, AnnotationTypeUpdate


class CRUDAnnotationType(
    CRUDBase[AnnotationTypes, AnnotationTypeCreate, AnnotationTypeUpdate]
):
    pass


annotation_types = CRUDAnnotationType(AnnotationTypes)
