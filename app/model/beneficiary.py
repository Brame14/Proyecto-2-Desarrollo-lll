from sqlalchemy import Column, Integer, String

from app.config.database import Base


class Beneficiary(Base):
    __tablename__ = "beneficiaries"

    beneficiary_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    community = Column(String(150), nullable=False)