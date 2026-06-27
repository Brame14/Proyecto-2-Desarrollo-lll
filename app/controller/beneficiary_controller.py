from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.auth.jwt_handler import get_current_user

from app.model.beneficiary import Beneficiary

from app.service.beneficiary_service import BeneficiaryService

from app.schema.beneficiary_schema import (
    BeneficiaryCreate,
    BeneficiaryUpdate,
    BeneficiaryResponse
)

router = APIRouter(
    prefix="/beneficiaries",
    tags=["Beneficiaries"]
)

service = BeneficiaryService()


@router.get(
    "/all",
    response_model=list[BeneficiaryResponse]
)
def get_all(
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return service.list_beneficiaries(db)


@router.get(
    "/{beneficiary_id}",
    response_model=BeneficiaryResponse
)
def get_by_id(
        beneficiary_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    beneficiary = service.get_beneficiary(
        db,
        beneficiary_id
    )

    if not beneficiary:
        raise HTTPException(
            status_code=404,
            detail="Beneficiary not found"
        )

    return beneficiary


@router.post(
    "/add",
    response_model=BeneficiaryResponse
)
def add(
        beneficiary_data: BeneficiaryCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    beneficiary = Beneficiary(
        name=beneficiary_data.name,
        age=beneficiary_data.age,
        gender=beneficiary_data.gender,
        community=beneficiary_data.community
    )

    return service.create_beneficiary(
        db,
        beneficiary
    )


@router.put(
    "/update/{beneficiary_id}",
    response_model=BeneficiaryResponse
)
def update(
        beneficiary_id: int,
        beneficiary_data: BeneficiaryUpdate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    beneficiary = service.get_beneficiary(
        db,
        beneficiary_id
    )

    if not beneficiary:
        raise HTTPException(
            status_code=404,
            detail="Beneficiary not found"
        )

    beneficiary.name = beneficiary_data.name
    beneficiary.age = beneficiary_data.age
    beneficiary.gender = beneficiary_data.gender
    beneficiary.community = beneficiary_data.community

    return service.update_beneficiary(
        db,
        beneficiary
    )


@router.delete(
    "/delete/{beneficiary_id}"
)
def delete(
        beneficiary_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    beneficiary = service.get_beneficiary(
        db,
        beneficiary_id
    )

    if not beneficiary:
        raise HTTPException(
            status_code=404,
            detail="Beneficiary not found"
        )

    service.delete_beneficiary(
        db,
        beneficiary
    )

    return {
        "message": "Beneficiary deleted"
    }