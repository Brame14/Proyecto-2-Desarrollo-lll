from sqlalchemy.orm import Session

from app.repository.toy_repository import ToyRepository
from app.model.toy import Toy


class ToyService:

    def __init__(self):
        self.repo = ToyRepository()

    def create_toy(self, db: Session, toy: Toy):
        return self.repo.create(db, toy)

    def get_toy(self, db: Session, toy_id: int):
        return self.repo.get_by_id(db, toy_id)

    def list_toys(self, db: Session):
        return self.repo.get_all(db)

    def update_toy(self, db: Session, toy: Toy):
        return self.repo.update(db, toy)

    def delete_toy(self, db: Session, toy: Toy):
        return self.repo.delete(db, toy)

    def toys_by_donor(self, db: Session):
        return self.repo.toys_by_donor(db)