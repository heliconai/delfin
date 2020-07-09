from typing import Optional

from pydantic import UUID4, BaseModel


# Shared properties
class DataModalityBase(BaseModel):
    data_modality: str
    description: str


# Properties to receive on data creation
class DataModalityCreate(DataModalityBase):
    pass

# Properties to recieve on project update
class DataModalityUpdate(DataModalityCreate):
    pass


# Properties shared by models stored in DB
class DataModalityInDBBase(DataModalityCreate):
    id: UUID4

    class Config:
        orm_mode = True


# Properties to return to client
class DataModality(DataModalityInDBBase):
    pass


# Properties properties stored in DB
class DataModalityInDB(DataModalityInDBBase):
    pass
