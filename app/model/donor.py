from sqlalchemy import Column, Integer, String

from app.config.database import Base


class Donor(Base):
    __tablename__ = "donors"

    donor_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(150), unique=True, nullable=False)