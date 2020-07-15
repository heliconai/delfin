from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

# TODO: Needs to be udpated with a better pagination model
@router.get("/", response_model=List[schemas.Dataset])
def read_datasets(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve datasets.
    """
    datasets = crud.datasets.get_multi(db, skip=skip, limit=limit)
    return datasets


@router.get("/{id}", response_model=schemas.Dataset)
def read_project(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Get dataset by ID.
    """
    dataset = crud.datasets.get(db=db, id=id)
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return dataset


@router.post("/", response_model=schemas.Dataset)
def create_project(
    *, db: Session = Depends(deps.get_db), project_in: schemas.DatasetCreate
) -> Any:
    """
    Create a new dataset.
    """
    dataset = crud.datasets.create(db=db, obj_in=project_in)
    return dataset


@router.put("/{id}", response_model=schemas.Dataset)
def update_project(
    *, db: Session = Depends(deps.get_db), id: UUID4, project_in: schemas.DatasetUpdate
) -> Any:
    """
    Update a dataset.
    """
    dataset = crud.datasets.get(db=db, id=id)
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    dataset = crud.datasets.update(db=db, db_obj=dataset, obj_in=project_in)
    return dataset


@router.delete("/{id}", response_model=schemas.Dataset)
def delete_project(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Delete a dataset.
    """
    dataset = crud.datasets.get(db=db, id=id)
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    dataset = crud.datasets.remove(db=db, id=id)
    return dataset
