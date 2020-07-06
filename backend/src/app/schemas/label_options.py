from typing import Optional, List, Any

from pydantic import UUID4, BaseModel, Json

# Shared properties
class LabelOptionBase(BaseModel):
    project_id: UUID4
    annotation_type_id: UUID4

# TODO: Add support for type checking JSONB returns
# Properties to receive on data creation
class LabelOptionCreate(LabelOptionBase):
    labels: Optional[List[Any]]

# Properties to recieve on project update
class LabelOptionUpdate(LabelOptionBase):
    pass


# Properties shared by models stored in DB
class LabelOptionInDBBase(LabelOptionCreate):
    id: UUID4

    class Config:
        orm_mode = True

# Properties to return to client
class LabelOption(LabelOptionInDBBase):
    pass


# Properties properties stored in DB
class LabelOptionInDB(LabelOptionInDBBase):
    pass
