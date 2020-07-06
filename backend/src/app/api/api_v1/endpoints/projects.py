from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

# TODO: Needs to be udpated with a better pagination model
@router.get("/", response_model=List[schemas.Project])
def read_projects(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve projects.
    """
    projects = crud.projects.get_multi(db, skip=skip, limit=limit)
    return projects


@router.get("/{id}", response_model=schemas.Project)
def read_project(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Get project by ID.
    """
    project = crud.projects.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("/", response_model=schemas.Project)
def create_project(
    *, db: Session = Depends(deps.get_db), project_in: schemas.ProjectCreate
) -> Any:
    """
    Create a new project.
    """
    project = crud.projects.create(db=db, obj_in=project_in)
    return project


@router.put("/{id}", response_model=schemas.Project)
def update_project(
    *, db: Session = Depends(deps.get_db), id: UUID4, project_in: schemas.ProjectUpdate
) -> Any:
    """
    Update a project.
    """
    project = crud.projects.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project = crud.projects.update(db=db, db_obj=project, obj_in=project_in)
    return project


@router.delete("/{id}", response_model=schemas.Project)
def delete_project(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Delete a project.
    """
    project = crud.projects.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project = crud.projects.remove(db=db, id=id)
    return project
