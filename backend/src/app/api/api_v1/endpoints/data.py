from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

# TODO: Needs to be udpated with a better pagination model
@router.get("/", response_model=List[schemas.Data])
def read_datas(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve data.
    """
    data = crud.data.get_multi(db, skip=skip, limit=limit)
    return data


@router.get("/{id}", response_model=schemas.Project)
def read_data(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Get data by ID.
    """
    data = crud.data.get(db=db, id=id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data


@router.post("/", response_model=schemas.Data)
def create_data(
    *, db: Session = Depends(deps.get_db), data_in: schemas.DataCreate
) -> Any:
    """
    Create new project.
    """
    data = crud.data.create(db=db, obj_in=data_in)
    return data


@router.put("/{id}", response_model=schemas.Data)
def update_data(
    *, db: Session = Depends(deps.get_db), id: UUID4, data_in: schemas.DataUpdate
) -> Any:
    """
    Update a data row.
    """
    data = crud.data.get(db=db, id=id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    data = crud.data.update(db=db, db_obj=data, obj_in=data_in)
    return data


@router.delete("/{id}", response_model=schemas.Project)
def delete_data(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    """
    Delete a data row.
    """
    data = crud.data.get(db=db, id=id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    data = crud.data.remove(db=db, id=id)
    return data
