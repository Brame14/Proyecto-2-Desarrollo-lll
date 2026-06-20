from sqlalchemy.orm import Session

from app.repository.donor_repository import DonorRepository
from app.model.donor import Donor


class DonorService:

    def __init__(self):
        self.repo = DonorRepository()

    def create_donor(self, db: Session, donor: Donor):
        return self.repo.create(db, donor)

    def get_donor(self, db: Session, donor_id: int):
        return self.repo.get_by_id(db, donor_id)

    def list_donors(self, db: Session):
        return self.repo.get_all(db)

    def update_donor(self, db: Session, donor: Donor):
        return self.repo.update(db, donor)

    def delete_donor(self, db: Session, donor: Donor):
        return self.repo.delete(db, donor)