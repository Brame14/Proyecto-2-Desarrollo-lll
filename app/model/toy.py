from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base


class Toy(Base):
    __tablename__ = "toys"

    toy_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    category = Column(String(100), nullable=False)
    condition = Column(String(50), nullable=False)

    donor_id = Column(Integer, ForeignKey("donors.donor_id"))

    donor = relationship("Donor")