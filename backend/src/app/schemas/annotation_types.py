from typing import Optional

from pydantic import UUID4, BaseModel


# Shared properties
class AnnotationTypeBase(BaseModel):
    data_modality_id: UUID4
    annotation_type: str


# Properties to receive on data creation
class AnnotationTypeCreate(AnnotationTypeBase):
    description: Optional[str]


# Properties to recieve on project update
class AnnotationTypeUpdate(AnnotationTypeCreate):
    pass


# Properties shared by models stored in DB
class AnnotationTypeInDBBase(AnnotationTypeCreate):
    id: UUID4

    class Config:
        orm_mode = True


# Properties to return to client
class AnnotationType(AnnotationTypeInDBBase):
    pass


# Properties properties stored in DB
class AnnotationTypeInDB(AnnotationTypeInDBBase):
    pass
