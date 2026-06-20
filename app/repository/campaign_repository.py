from sqlalchemy.orm import Session

from app.model.campaign import Campaign


class CampaignRepository:

    def get_all(self, db: Session):
        return db.query(Campaign).all()

    def get_by_id(self, db: Session, campaign_id: int):
        return db.query(Campaign).filter(
            Campaign.campaign_id == campaign_id
        ).first()

    def create(self, db: Session, campaign: Campaign):
        db.add(campaign)
        db.commit()
        db.refresh(campaign)
        return campaign

    def update(self, db: Session, campaign: Campaign):
        db.commit()
        db.refresh(campaign)
        return campaign

    def delete(self, db: Session, campaign: Campaign):
        db.delete(campaign)
        db.commit()