from typing import List, Optional, Union

from pydantic import UUID4, BaseModel


# Shared properties
class DataBase(BaseModel):
    project_id: UUID4
    name: str


# Using Union of dict and None for JSONB columns as per
# https://github.com/tiangolo/fastapi/issues/211
# Properties to receive on data creation
class DataCreate(DataBase):
    properties: Optional[Union[dict, None]]
    scopes: Optional[List[Union[dict, None]]]


# Properties to recieve on project update
class DataUpdate(DataCreate):
    pass


# Properties shared by models stored in DB
class DataInDBBase(DataCreate):
    id: UUID4

    class Config:
        orm_mode = True


# Properties to return to client
class Data(DataInDBBase):
    pass


# Properties properties stored in DB
class DataInDB(DataInDBBase):
    pass
