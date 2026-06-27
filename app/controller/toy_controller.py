from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.auth.jwt_handler import get_current_user

from app.model.toy import Toy

from app.service.toy_service import ToyService

from app.schema.toy_schema import (
    ToyCreate,
    ToyUpdate,
    ToyResponse
)

router = APIRouter(
    prefix="/toys",
    tags=["Toys"]
)

service = ToyService()


@router.get(
    "/all",
    response_model=list[ToyResponse]
)
def get_all(
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return service.list_toys(db)


@router.get(
    "/{toy_id}",
    response_model=ToyResponse
)
def get_by_id(
        toy_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    toy = service.get_toy(
        db,
        toy_id
    )

    if not toy:
        raise HTTPException(
            status_code=404,
            detail="Toy not found"
        )

    return toy
@router.get(
    "/report/toys-by-donor"
)
def toys_by_donor(
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return service.toys_by_donor(db)


@router.post(
    "/add",
    response_model=ToyResponse
)
def add(
        toy_data: ToyCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    toy = Toy(
        name=toy_data.name,
        category=toy_data.category,
        condition=toy_data.condition,
        donor_id=toy_data.donor_id
    )

    return service.create_toy(
        db,
        toy
    )


@router.put(
    "/update/{toy_id}",
    response_model=ToyResponse
)
def update(
        toy_id: int,
        toy_data: ToyUpdate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    toy = service.get_toy(
        db,
        toy_id
    )

    if not toy:
        raise HTTPException(
            status_code=404,
            detail="Toy not found"
        )

    toy.name = toy_data.name
    toy.category = toy_data.category
    toy.condition = toy_data.condition
    toy.donor_id = toy_data.donor_id

    return service.update_toy(
        db,
        toy
    )


@router.delete(
    "/delete/{toy_id}"
)
def delete(
        toy_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    toy = service.get_toy(
        db,
        toy_id
    )

    if not toy:
        raise HTTPException(
            status_code=404,
            detail="Toy not found"
        )

    service.delete_toy(
        db,
        toy
    )

    return {
        "message": "Toy deleted"
    }