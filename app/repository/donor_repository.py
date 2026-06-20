from sqlalchemy.orm import Session

from app.model.donor import Donor


class DonorRepository:

    def get_all(self, db: Session):
        return db.query(Donor).all()

    def get_by_id(self, db: Session, donor_id: int):
        return db.query(Donor).filter(
            Donor.donor_id == donor_id
        ).first()

    def create(self, db: Session, donor: Donor):
        db.add(donor)
        db.commit()
        db.refresh(donor)
        return donor

    def update(self, db: Session, donor: Donor):
        db.commit()
        db.refresh(donor)
        return donor

    def delete(self, db: Session, donor: Donor):
        db.delete(donor)
        db.commit()