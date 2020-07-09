from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

# TODO: Needs to be udpated with a better pagination model
@router.get("/", response_model=List[schemas.AnnotationType])
def read_annotation_types(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve annotion types.
    """
    annotation_types = crud.annotation_types.get_multi(db, skip=skip, limit=limit)
    return annotation_types


@router.get("/{id}", response_model=schemas.AnnotationType)
def read_annotation_type(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Get annotation type by ID.
    """
    annotation_type = crud.annotation_types.get(db=db, id=id)
    if not annotation_type:
        raise HTTPException(status_code=404, detail="Annotation type not found")
    return annotation_type


@router.post("/", response_model=schemas.AnnotationType)
def create_annotation_type(
    *,
    db: Session = Depends(deps.get_db),
    annotation_type_in: schemas.AnnotationTypeCreate
) -> Any:
    """
    Create new annotation type.
    """
    annotation_type = crud.annotation_types.create(db=db, obj_in=annotation_type_in)
    return annotation_type


@router.put("/{id}", response_model=schemas.AnnotationType)
def update_annotation_type(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    annotation_type_in: schemas.AnnotationTypeUpdate
) -> Any:
    """
    Update a label option.
    """
    annotation_type = crud.annotation_types.get(db=db, id=id)
    if not annotation_type:
        raise HTTPException(status_code=404, detail="Annotation type not found")
    annotation_type = crud.annotation_types.update(
        db=db, db_obj=annotation_type, obj_in=annotation_type_in
    )
    return annotation_type


@router.delete("/{id}", response_model=schemas.AnnotationType)
def delete_annotation_type(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Delete a annotation type.
    """
    annotation_type = crud.annotation_types.get(db=db, id=id)
    if not annotation_type:
        raise HTTPException(status_code=404, detail="Annotation type not found")
    annotation_type = crud.annotation_types.remove(db=db, id=id)
    return annotation_type
