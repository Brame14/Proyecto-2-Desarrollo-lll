from sqlalchemy.orm import Session

from app.model.toy import Toy


class ToyRepository:

    def get_all(self, db: Session):
        return db.query(Toy).all()

    def get_by_id(self, db: Session, toy_id: int):
        return db.query(Toy).filter(
            Toy.toy_id == toy_id
        ).first()

    def create(self, db: Session, toy: Toy):
        db.add(toy)
        db.commit()
        db.refresh(toy)
        return toy

    def update(self, db: Session, toy: Toy):
        db.commit()
        db.refresh(toy)
        return toy

    def delete(self, db: Session, toy: Toy):
        db.delete(toy)
        db.commit()

    def toys_by_donor(self, db: Session):

        result = {}

        toys = db.query(Toy).all()

        for toy in toys:

            donor_id = toy.donor_id

            if donor_id not in result:
                result[donor_id] = 0

            result[donor_id] += 1

        return result