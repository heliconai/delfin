from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

# TODO: Needs to be udpated with a better pagination model
@router.get("/", response_model=List[schemas.DataModality])
def read_data_modalities(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve data modalities.
    """
    data_modalities = crud.data_modality.get_multi(db, skip=skip, limit=limit)
    return data_modalities


@router.get("/{id}", response_model=schemas.DataModality)
def read_data_modality(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Get data modality by ID.
    """
    data_modality = crud.data_modality.get(db=db, id=id)
    if not data_modality:
        raise HTTPException(status_code=404, detail="Data modality not found")
    return data_modality


@router.post("/", response_model=schemas.DataModality)
def create_data_modality(
    *,
    db: Session = Depends(deps.get_db),
    data_modality_in: schemas.DataModalityCreate
) -> Any:
    """
    Create new data modality.
    """
    data_modality = crud.data_modality.create(db=db, obj_in=data_modality_in)
    return data_modality


@router.put("/{id}", response_model=schemas.DataModality)
def update_data_modality(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    data_modality_in: schemas.DataModalityUpdate
) -> Any:
    """
    Update a data modality.
    """
    data_modality = crud.data_modality.get(db=db, id=id)
    if not data_modality:
        raise HTTPException(status_code=404, detail="Data modality not found")
    data_modality = crud.data_modality.update(
        db=db, db_obj=annotation_type, obj_in=data_modality_in
    )
    return data_modality


@router.delete("/{id}", response_model=schemas.DataModality)
def delete_data_modality(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Delete a data modality.
    """
    data_modality = crud.data_modality.get(db=db, id=id)
    if not data_modality:
        raise HTTPException(status_code=404, detail="Data modality not found")
    data_modality = crud.data_modality.remove(db=db, id=id)
    return data_modality
