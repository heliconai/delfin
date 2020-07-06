from app.crud.base import CRUDBase
from app.models.projects import Projects
from app.schemas.projects import ProjectCreate, ProjectUpdate


class CRUDProjects(CRUDBase[Projects, ProjectCreate, ProjectUpdate]):
    pass


projects = CRUDProjects(Projects)
