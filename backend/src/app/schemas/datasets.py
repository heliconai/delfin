from typing import Optional

from pydantic import UUID4, BaseModel
from app.schemas.base_schema import BaseSchema

# Shared properties
class DatasetBase(BaseSchema):
    name: str
    instructions: Optional[str] = None


# Properties to recieve on dataset creation
class DatasetCreate(DatasetBase):
    data_modality: str


# Properties to recieve on dataset update
class DatasetUpdate(DatasetBase):
    pass


# Properties shared by models stored in DB
class DatasetInDBBase(DatasetCreate):
    id: UUID4

    class Config:
        orm_mode = True


# Properties to return to client
class Dataset(DatasetInDBBase):
    pass


# Properties properties stored in DB
class DatasetInDB(DatasetInDBBase):
    pass
