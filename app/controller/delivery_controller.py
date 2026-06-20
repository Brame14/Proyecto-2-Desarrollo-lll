from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.model.delivery import Delivery

from app.service.delivery_service import DeliveryService

from app.schema.delivery_schema import (
    DeliveryCreate,
    DeliveryUpdate,
    DeliveryResponse
)

router = APIRouter(
    prefix="/deliveries",
    tags=["Deliveries"]
)

service = DeliveryService()


@router.get(
    "/all",
    response_model=list[DeliveryResponse]
)
def get_all(
        db: Session = Depends(get_db)
):
    return service.list_deliveries(db)


@router.get(
    "/{delivery_id}",
    response_model=DeliveryResponse
)
def get_by_id(
        delivery_id: int,
        db: Session = Depends(get_db)
):

    delivery = service.get_delivery(
        db,
        delivery_id
    )

    if not delivery:
        raise HTTPException(
            status_code=404,
            detail="Delivery not found"
        )

    return delivery


@router.post(
    "/add",
    response_model=DeliveryResponse
)
def add(
        delivery_data: DeliveryCreate,
        db: Session = Depends(get_db)
):

    delivery = Delivery(
        beneficiary_id=delivery_data.beneficiary_id,
        toy_id=delivery_data.toy_id,
        campaign_id=delivery_data.campaign_id,
        delivery_date=delivery_data.delivery_date
    )

    return service.create_delivery(
        db,
        delivery
    )


@router.put(
    "/update/{delivery_id}",
    response_model=DeliveryResponse
)
def update(
        delivery_id: int,
        delivery_data: DeliveryUpdate,
        db: Session = Depends(get_db)
):

    delivery = service.get_delivery(
        db,
        delivery_id
    )

    if not delivery:
        raise HTTPException(
            status_code=404,
            detail="Delivery not found"
        )

    delivery.beneficiary_id = delivery_data.beneficiary_id
    delivery.toy_id = delivery_data.toy_id
    delivery.campaign_id = delivery_data.campaign_id
    delivery.delivery_date = delivery_data.delivery_date

    return service.update_delivery(
        db,
        delivery
    )


@router.delete(
    "/delete/{delivery_id}"
)
def delete(
        delivery_id: int,
        db: Session = Depends(get_db)
):

    delivery = service.get_delivery(
        db,
        delivery_id
    )

    if not delivery:
        raise HTTPException(
            status_code=404,
            detail="Delivery not found"
        )

    service.delete_delivery(
        db,
        delivery
    )

    return {
        "message": "Delivery deleted"
    }


@router.get("/report/total")
def total_deliveries(
        db: Session = Depends(get_db)
):
    return {
        "total_deliveries":
            service.total_deliveries(db)
    }
@router.get(
    "/report/deliveries-by-campaign"
)
def deliveries_by_campaign(
        db: Session = Depends(get_db)
):
    return service.deliveries_by_campaign(
        db
    )