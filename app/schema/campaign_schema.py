from datetime import date
from pydantic import BaseModel


class CampaignBase(BaseModel):
    name: str
    description: str
    date: date
    location: str


class CampaignCreate(CampaignBase):
    pass


class CampaignUpdate(CampaignBase):
    pass


class CampaignResponse(CampaignBase):
    campaign_id: int

    class Config:
        from_attributes = True