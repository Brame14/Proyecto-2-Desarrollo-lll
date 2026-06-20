from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.model.campaign import Campaign

from app.service.campaign_service import CampaignService

from app.schema.campaign_schema import (
    CampaignCreate,
    CampaignUpdate,
    CampaignResponse
)

router = APIRouter(
    prefix="/campaigns",
    tags=["Campaigns"]
)

service = CampaignService()


@router.get(
    "/all",
    response_model=list[CampaignResponse]
)
def get_all(
        db: Session = Depends(get_db)
):
    return service.list_campaigns(db)


@router.get(
    "/{campaign_id}",
    response_model=CampaignResponse
)
def get_by_id(
        campaign_id: int,
        db: Session = Depends(get_db)
):

    campaign = service.get_campaign(
        db,
        campaign_id
    )

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    return campaign


@router.post(
    "/add",
    response_model=CampaignResponse
)
def add(
        campaign_data: CampaignCreate,
        db: Session = Depends(get_db)
):

    campaign = Campaign(
        name=campaign_data.name,
        description=campaign_data.description,
        date=campaign_data.date,
        location=campaign_data.location
    )

    return service.create_campaign(
        db,
        campaign
    )


@router.put(
    "/update/{campaign_id}",
    response_model=CampaignResponse
)
def update(
        campaign_id: int,
        campaign_data: CampaignUpdate,
        db: Session = Depends(get_db)
):

    campaign = service.get_campaign(
        db,
        campaign_id
    )

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    campaign.name = campaign_data.name
    campaign.description = campaign_data.description
    campaign.date = campaign_data.date
    campaign.location = campaign_data.location

    return service.update_campaign(
        db,
        campaign
    )


@router.delete(
    "/delete/{campaign_id}"
)
def delete(
        campaign_id: int,
        db: Session = Depends(get_db)
):

    campaign = service.get_campaign(
        db,
        campaign_id
    )

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    service.delete_campaign(
        db,
        campaign
    )

    return {
        "message": "Campaign deleted"
    }