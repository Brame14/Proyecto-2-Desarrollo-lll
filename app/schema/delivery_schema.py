from datetime import date
from pydantic import BaseModel


class DeliveryBase(BaseModel):
    beneficiary_id: int
    toy_id: int
    campaign_id: int
    delivery_date: date


class DeliveryCreate(DeliveryBase):
    pass


class DeliveryUpdate(DeliveryBase):
    pass


class DeliveryResponse(DeliveryBase):
    delivery_id: int

    class Config:
        from_attributes = True