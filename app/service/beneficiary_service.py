from sqlalchemy.orm import Session

from app.repository.beneficiary_repository import BeneficiaryRepository
from app.model.beneficiary import Beneficiary


class BeneficiaryService:

    def __init__(self):
        self.repo = BeneficiaryRepository()

    def create_beneficiary(self, db: Session, beneficiary: Beneficiary):
        return self.repo.create(db, beneficiary)

    def get_beneficiary(self, db: Session, beneficiary_id: int):
        return self.repo.get_by_id(db, beneficiary_id)

    def list_beneficiaries(self, db: Session):
        return self.repo.get_all(db)

    def update_beneficiary(self, db: Session, beneficiary: Beneficiary):
        return self.repo.update(db, beneficiary)

    def delete_beneficiary(self, db: Session, beneficiary: Beneficiary):
        return self.repo.delete(db, beneficiary)