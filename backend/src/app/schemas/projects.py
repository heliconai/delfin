from typing import Optional

from pydantic import UUID4, BaseModel


# Shared properties
class ProjectBase(BaseModel):
    name: str
    instructions: Optional[str] = None


# Properties to recieve on project creation
class ProjectCreate(ProjectBase):
    data_modality: str


# Properties to recieve on project update
class ProjectUpdate(ProjectBase):
    pass


# Properties shared by models stored in DB
class ProjectInDBBase(ProjectCreate):
    id: UUID4

    class Config:
        orm_mode = True


# Properties to return to client
class Project(ProjectInDBBase):
    pass


# Properties properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass
