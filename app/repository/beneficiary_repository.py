from sqlalchemy.orm import Session

from app.model.beneficiary import Beneficiary


class BeneficiaryRepository:

    def get_all(self, db: Session):
        return db.query(Beneficiary).all()

    def get_by_id(self, db: Session, beneficiary_id: int):
        return db.query(Beneficiary).filter(
            Beneficiary.beneficiary_id == beneficiary_id
        ).first()

    def create(self, db: Session, beneficiary: Beneficiary):
        db.add(beneficiary)
        db.commit()
        db.refresh(beneficiary)
        return beneficiary

    def update(self, db: Session, beneficiary: Beneficiary):
        db.commit()
        db.refresh(beneficiary)
        return beneficiary

    def delete(self, db: Session, beneficiary: Beneficiary):
        db.delete(beneficiary)
        db.commit()