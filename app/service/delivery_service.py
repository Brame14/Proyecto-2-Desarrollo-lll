from sqlalchemy.orm import Session

from app.repository.delivery_repository import DeliveryRepository
from app.model.delivery import Delivery


class DeliveryService:

    def __init__(self):
        self.repo = DeliveryRepository()

    def create_delivery(self, db: Session, delivery: Delivery):
        return self.repo.create(db, delivery)

    def get_delivery(self, db: Session, delivery_id: int):
        return self.repo.get_by_id(db, delivery_id)

    def list_deliveries(self, db: Session):
        return self.repo.get_all(db)

    def update_delivery(self, db: Session, delivery: Delivery):
        return self.repo.update(db, delivery)

    def delete_delivery(self, db: Session, delivery: Delivery):
        return self.repo.delete(db, delivery)

    def total_deliveries(self, db: Session):
        deliveries = self.repo.get_all(db)
        return len(deliveries)

    def deliveries_by_campaign(
            self,
            db: Session
    ):
        return self.repo.deliveries_by_campaign(db)