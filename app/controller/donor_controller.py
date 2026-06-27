from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.auth.jwt_handler import get_current_user

from app.model.donor import Donor

from app.service.donor_service import DonorService

from app.schema.donor_schema import (
    DonorCreate,
    DonorUpdate,
    DonorResponse
)

router = APIRouter(
    prefix="/donors",
    tags=["Donors"]
)

service = DonorService()


@router.get(
    "/all",
    response_model=list[DonorResponse]
)
def get_all(
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return service.list_donors(db)


@router.get(
    "/{donor_id}",
    response_model=DonorResponse
)
def get_by_id(
        donor_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    donor = service.get_donor(
        db,
        donor_id
    )

    if not donor:
        raise HTTPException(
            status_code=404,
            detail="Donor not found"
        )

    return donor


@router.post(
    "/add",
    response_model=DonorResponse
)
def add(
        donor_data: DonorCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    donor = Donor(
        name=donor_data.name,
        phone=donor_data.phone,
        email=donor_data.email
    )

    return service.create_donor(
        db,
        donor
    )


@router.put(
    "/update/{donor_id}",
    response_model=DonorResponse
)
def update(
        donor_id: int,
        donor_data: DonorUpdate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    donor = service.get_donor(
        db,
        donor_id
    )

    if not donor:
        raise HTTPException(
            status_code=404,
            detail="Donor not found"
        )

    donor.name = donor_data.name
    donor.phone = donor_data.phone
    donor.email = donor_data.email

    return service.update_donor(
        db,
        donor
    )


@router.delete(
    "/delete/{donor_id}"
)
def delete(
        donor_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    donor = service.get_donor(
        db,
        donor_id
    )

    if not donor:
        raise HTTPException(
            status_code=404,
            detail="Donor not found"
        )

    service.delete_donor(
        db,
        donor
    )

    return {
        "message": "Donor deleted"
    }