from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

# TODO: Needs to be udpated with a better pagination model
@router.get("/", response_model=List[schemas.LabelOption])
def read_label_options(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve label options.
    """
    label_options = crud.label_options.get_multi(db, skip=skip, limit=limit)
    return label_options


@router.get("/{id}", response_model=schemas.LabelOption)
def read_label_option(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Get label options by ID.
    """
    label_option = crud.label_options.get(db=db, id=id)
    if not label_option:
        raise HTTPException(status_code=404, detail="Label option not found")
    return label_option


@router.post("/", response_model=schemas.LabelOption)
def create_label_option(
    *, db: Session = Depends(deps.get_db), label_option_in: schemas.LabelOptionCreate
) -> Any:
    """
    Create new label option.
    """
    label_option = crud.label_options.create(db=db, obj_in=label_option_in)
    return label_option


@router.put("/{id}", response_model=schemas.LabelOption)
def update_label_option(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    label_option_in: schemas.LabelOptionUpdate
) -> Any:
    """
    Update a label option.
    """
    label_option = crud.label_options.get(db=db, id=id)
    if not label_option:
        raise HTTPException(status_code=404, detail="Label option not found")
    label_option = crud.label_options.update(
        db=db, db_obj=label_option, obj_in=label_option_in
    )
    return label_option


@router.delete("/{id}", response_model=schemas.LabelOption)
def delete_label_option(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Delete a label option.
    """
    label_option = crud.label_options.get(db=db, id=id)
    if not label_option:
        raise HTTPException(status_code=404, detail="Label option not found")
    label_option = crud.label_options.remove(db=db, id=id)
    return label_option
