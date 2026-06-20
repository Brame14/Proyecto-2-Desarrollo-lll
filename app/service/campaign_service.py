from sqlalchemy.orm import Session

from app.repository.campaign_repository import CampaignRepository
from app.model.campaign import Campaign


class CampaignService:

    def __init__(self):
        self.repo = CampaignRepository()

    def create_campaign(self, db: Session, campaign: Campaign):
        return self.repo.create(db, campaign)

    def get_campaign(self, db: Session, campaign_id: int):
        return self.repo.get_by_id(db, campaign_id)

    def list_campaigns(self, db: Session):
        return self.repo.get_all(db)

    def update_campaign(self, db: Session, campaign: Campaign):
        return self.repo.update(db, campaign)

    def delete_campaign(self, db: Session, campaign: Campaign):
        return self.repo.delete(db, campaign)