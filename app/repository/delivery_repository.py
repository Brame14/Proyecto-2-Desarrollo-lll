from sqlalchemy.orm import Session

from app.model.delivery import Delivery


class DeliveryRepository:

    def get_all(self, db: Session):
        return db.query(Delivery).all()

    def get_by_id(self, db: Session, delivery_id: int):
        return db.query(Delivery).filter(
            Delivery.delivery_id == delivery_id
        ).first()

    def create(self, db: Session, delivery: Delivery):
        db.add(delivery)
        db.commit()
        db.refresh(delivery)
        return delivery

    def update(self, db: Session, delivery: Delivery):
        db.commit()
        db.refresh(delivery)
        return delivery

    def delete(self, db: Session, delivery: Delivery):
        db.delete(delivery)
        db.commit()

    def deliveries_by_campaign(
            self,
            db: Session
    ):

        result = {}

        deliveries = db.query(
            Delivery
        ).all()

        for delivery in deliveries:

            campaign_id = delivery.campaign_id

            if campaign_id not in result:
                result[campaign_id] = 0

            result[campaign_id] += 1

        return result