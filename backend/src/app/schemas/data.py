from typing import Any, List, Optional

from pydantic import BaseModel, UUID4


# Shared properties
class DataBase(BaseModel):
    project_id: UUID4
    name: str


# TODO: Add support for type checking JSONB returns
# Properties to receive on data creation
class DataCreate(DataBase):
    properties: Optional[Any]
    scopes: Optional[List[Any]]


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
